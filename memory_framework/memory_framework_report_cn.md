# Mem0 集成与特性分析总结

| **关注点**                      | **支持情况**, 网站 https://www.mem0.ai/ 或 https://mem0.ai/research |
| ------------------------------- | ------------------------------------------------------------ |
| **Memory 管理**                 | ✅ 采用分层管理：核心Vector存储+图存储关系层，使用LLM提取重要信息自动构建记忆 |
| **记忆检索方式**                | ✅ 基于向量相似度搜索+图关系查询(支持BM25重排序)              |
| **性能（延迟、token、准确率）** | ✅ 在 LOCOMO 基准上比OpenAI Memory准确率高26%，p95延迟降低91%，token使用减少90%, 详情https://mem0.ai/research |
| **PostgreSQL 集成（扩展）**     | ✅ 原生支持pgvector，支持DiskANN和HNSW索引，完整SQL交互接口   |
| **与 langgraph 集成**           | ✅ 提供官方集成文档和范例代码                                 |
| **API 设计参考**                | ✅ https://docs.mem0.ai/open-source/python-quickstart         |
| **社区活跃度**                  | ✅ GitHub星标32.8k，Y Combinator S24支持，Discord社区活跃     |
| **论文**                        | ✅ https://arxiv.org/abs/2504.19413 (2025)                    |

##### Mem0  系统总结

![img](pictures/ur60uTft3XImAXN9Bfr5bOK9uUI.png)

![img](https://framerusercontent.com/images/DkaUXgJt22p9REFF5265ZJajtmQ.png)



#### 问题 1：Mem0 的 Memory 管理方式是什么？是否采用分级管理？

Mem0采用了分级内存管理模式，通过向量存储、图存储和记忆历史的组合，实现了高效的记忆存储与检索。它的核心设计明确采用了分级管理，灵感直接来自人类短期记忆（STM）、长期记忆（LTM）的认知结构，结合现代AI 系统的技术架构。

| 内存层次            | 对应模块                                                     | 功能作用                                                     |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **短期记忆（STM）** | **Conversation History + Working Memory + Attention Context** | **在当前会话窗口内，实时跟踪最近一轮对话、上下文焦点，用于即时推理。注意：这部分通常由 LLM 直接维护，不入存储。** |
| **长期记忆（LTM）** | **Factual Memory + Episodic Memory + Semantic Memory**       | **用向量数据库（如 Faiss、Qdrant）存储语义化的长期记忆，包括事实（facts）、事件（episodes）、概念（semantics）。通过 embedding 搜索实现跨会话调用。** |
| 关系记忆（Graph）   | Graph Database（如 Memgraph、Neo4j）                         | 存储实体-关系网络（entity-relationship graph），用于推理、矛盾检测、复杂关系的快速检索和可视化。 |
| 历史记录（Audit）   | SQLite 日志库                                                | 跟踪所有 memory 操作历史（增、改、删），包括时间戳、角色、操作人，提供回溯、审计、版本控制功能。 |

##### 核心管理机制

**1️⃣ Dual Storage Architecture（双存储架构）**
Mem0 同时结合：

- **向量存储（Vector Database）** 
  存储语义化的事实与对话，支持高效的近似最近邻（ANN）搜索。

- **图数据库（Graph Database）** 
  存储实体、事件及其之间的关系，提供关系推理、跨节点搜索。

**2️⃣ Memory Processing（内存处理）**

- **LLM 抽取（Information Extraction）** → 识别对话中的关键信息、实体及关系。
- **冲突检测与解决（Conflict Resolution）** → 比较新旧数据，更新或覆盖矛盾信息。
- **存储（Memory Storage）** → 写入向量数据库与图数据库，保证全局一致性。

**3️⃣ Memory Retrieval（内存检索）**

- 查询预处理（Query Processing） → LLM 优化输入查询，确定过滤条件。
- 语义搜索（Vector Search） → 基于 embedding 进行语义匹配。
- 结果处理(融合与排序)（Result Processing） → 聚合多源结果，打分、排序、返回。

总结：Mem0 确实采用分级管理机制，结合双存储架构与 LLM，具备显著性能优势。



#### 问题 2：Mem0 的记忆检索方式是什么？

### ![search_architecture.png](pictures/search_architecture.png)

| 检索                | 技术模块                          | 功能作用                                                     |
| ------------------- | --------------------------------- | ------------------------------------------------------------ |
| 向量搜索（Vector）  | Vector Store（如 Faiss、Qdrant）  | 对向量数据库执行近似最近邻（ANN）搜索，返回最相关的语义匹配结果，带相关性得分（score）。 |
| 图关系搜索（Graph） | Graph Store（如 Memgraph、Neo4j） | 对图数据库执行基于实体-关系的查询，找到与查询实体或节点相关的上下游节点、关系链条。 |

**2️⃣ 向量语义搜索**

- 调用：

```python
embeddings = self.embedding_model.embed(query, "search")
memories = self.vector_store.search(query=query, vectors=embeddings, limit=limit, filters=filters)
```

- 特点：基于语义相似度查找最接近的记忆，返回详细 score、memory、metadata、timestamp 等信息。

**3️⃣ 图关系查询**
当启用 Graph Store（如 Memgraph）时：

```python
if self.enable_graph:
    graph_entities = self.graph.search(query, effective_filters, limit)
```



#### 问题3：Mem0在性能方面（延迟、token开销、准确率）的表现如何？

**一种可扩展的以内存为中心的算法，可动态提取和检索关键对话事实 - 在 LOCOMO 基准上比 OpenAI 的相对准确度提高了 26％，p95 延迟降低了 91％，令牌减少了 90％。** 



![img](pictures/latency.png)

该图表比较了每种方法的 **搜索延迟** （粉色表示中位数 p50，绿色表示尾部 p95）与其推理准确度（蓝色条）。Mem0 实现了 **66.9% 的** 准确度， **中位数搜索延迟为 0.20 秒** ，  **p95 延迟为 0.15 秒** ，使记忆检索牢牢保持在实时范围内。相比之下，标准 RAG 设置 **情况下仅能达到61.0% 的** 准确度 **在中位数0.70 秒** 、  **p95 搜索时间为0.26 秒的** 。图形增强变体 Mem0ᵍ 进一步将准确度提升至 **68.4%，** 中位数为 **0.66 秒** ，  **p95 搜索延迟为0.48 秒** 。通过仅提取和索引最显著的事实，Mem0 提供了近乎最先进的长期推理能力，同时最大限度地降低了搜索开销。 



![img](pictures/measurement.png)

该图表端到端测量（内存检索 + 答案生成）展示了 Mem0 的生产就绪性。全上下文方法可以达到 72.9% 的准确率，但 **中位数为 9.87 秒** ，  **p95** 延迟为 17.12 秒。相比之下，  **Mem0 的** 准确率达到了 **66.9%，** 中位数仅为 **0.71 秒** ，  **p95** 端到端响应时间为 1.44 秒。其图增强变体 **Mem0ᵍ** 将准确率提升至 **68.4%**  ，同时保持了 **1.09 秒的中位数** 和 **2.59 秒的 p95** 延迟。通过仅提取和索引最相关的事实，Mem0 能够以真正的生产速度提供近乎最先进的长期推理能力。



![img](pictures/performance.png)

表 1：在 LOCOMO 数据集中，不同记忆增强系统在不同问题类型下的性能对比。
评估指标包括 F1 分数（F1）、BLEU-1（B1）以及 LLM-as-a-Judge 分数（J），分数越高表示性能越好。
A-Mem∗ 表示我们重新运行 A-Mem 时，通过将 temperature 设置为 0 所生成的 LLM-as-a-Judge 分数。
Mem0g 表示我们提出的、通过图记忆增强的架构。加粗的数字表示各个指标下所有方法中的最佳表现。
（↑）表示分数越高越好。

![img](pictures/performance2.png)

表 2：各种基线方法与所提出方法的性能对比。延迟测量显示 p50（中位数）和 p95（95 百分位）值，分别对应搜索时间（获取记忆/片段的时间）和总时间（生成完整响应的时间）。整体 LLM-as-a-Judge 得分（J）表示在整个 LOCOMO 数据集上生成响应的质量指标。



#### 问题4：Mem0如何支持与PostgreSQL集成？特别是pgvector/Apache AGE扩展数据库的集成。

Mem0通过这些实现提供了与PostgreSQL和pgvector的无缝集成，支持高性能向量存储和检索

##### PostgreSQL连接与初始化

```python
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "supabase",
        "config": {
            "connection_string": "postgresql://user:password@host:port/database",
            "collection_name": "memories",
            "index_method": "hnsw",  # Optional: defaults to "auto"
            "index_measure": "cosine_distance"  # Optional: defaults to "cosine_distance"
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})
```

##### pgvector扩展支持

```python
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "pgvector",
        "config": {
            "user": "test",
            "password": "123",
            "host": "127.0.0.1",
            "port": "5432",
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})
```

##### 高级索引支持

Mem0支持两种向量索引类型的自动创建：**DiskANN索引** - 适合大规模向量数据集，**HNSW索引** - 层次可导航小世界图索引



#### 问题5：Mem0是否支持与LangGraph集成？如何集成？

##### 官方LangGraph集成文档: https://docs.mem0.ai/integrations/langgraph#langgraph

Mem0官方文档详细介绍了与LangGraph的集成方法，提供了构建具有长期记忆能力的AI代理示例。

```python
# 初始化组件
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from mem0 import MemoryClient
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Configuration
OPENAI_API_KEY = 'sk-xxx'  # Replace with your actual OpenAI API key
MEM0_API_KEY = 'your-mem0-key'  # Replace with your actual Mem0 API key

# Initialize LangChain and Mem0
llm = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)
mem0 = MemoryClient(api_key=MEM0_API_KEY)

# 定义状态图, 设置对话状态和 LangGraph 结构：
class State(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    mem0_user_id: str

graph = StateGraph(State)

# 创建聊天机器人功能,定义客户支持 AI 代理的核心逻辑： 
def chatbot(state: State):
    messages = state["messages"]
    user_id = state["mem0_user_id"]

    # Retrieve relevant memories
    memories = mem0.search(messages[-1].content, user_id=user_id)

    context = "Relevant information from previous conversations:\n"
    for memory in memories:
        context += f"- {memory['memory']}\n"

    system_message = SystemMessage(content=f"""You are a helpful customer support assistant. Use the provided context to personalize your responses and remember user preferences and past interactions.
{context}""")

    full_messages = [system_message] + messages
    response = llm.invoke(full_messages)

    # Store the interaction in Mem0
    mem0.add(f"User: {messages[-1].content}\nAssistant: {response.content}", user_id=user_id)
    return {"messages": [response]}

# 图形结构设置,完整的LangGraph结构集成：
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "chatbot")

compiled_graph = graph.compile()

# 创建对话运行器, 实现一个功能来管理对话流： 
def run_conversation(user_input: str, mem0_user_id: str):
    config = {"configurable": {"thread_id": mem0_user_id}}
    state = {"messages": [HumanMessage(content=user_input)], "mem0_user_id": mem0_user_id}

    for event in compiled_graph.stream(state, config):
        for value in event.values():
            if value.get("messages"):
                print("Customer Support:", value["messages"][-1].content)
                return

# 主交互循环, 设置主程序循环以供用户交互： 
if __name__ == "__main__":
    print("Welcome to Customer Support! How can I assist you today?")
    mem0_user_id = "customer_123"  # You can generate or retrieve this based on your user management system
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Customer Support: Thank you for contacting us. Have a great day!")
            break
        run_conversation(user_input, mem0_user_id)
```



#### 问题6：API设计参考

Mem0提供了简洁而功能强大的API设计：https://docs.mem0.ai/open-source/python-quickstart
如果你有一个 `Mem0 API key`，您可以使用它来初始化客户端。或者，如果您在本地使用 Mem0，则可以不使用 API 密钥来初始化它。 

##### API设计参考

```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient() # get api_key from https://app.mem0.ai/

# Store messages
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]
result = client.add(messages, user_id="alex")
print(result)

# Retrieve memories
all_memories = client.get_all(user_id="alex")
print(all_memories)

# Search memories
query = "What do you know about me?"
related_memories = client.search(query, user_id="alex")

# Get memory history
history = client.history(memory_id="m1")
print(history)
```



# Letta 集成与特性分析总结

| **关注点**                      | **支持情况**, 网站 https://www.letta.com/       |
| ------------------------------- | ----------------------------------------------- |
| **Memory 管理**                 | ✅ 分层，有上下文记忆存储 和 长期记忆存储        |
| **记忆检索方式**                | ✅ 字符串文本匹配 和 语义相似度检索              |
| **性能（延迟、token、准确率）** | ✅ 详细看论文: https://arxiv.org/abs/2310.08560  |
| **PostgreSQL 集成（扩展）**     | ✅ 默认使用 PostgreSQL，支持 pgvector            |
| **与 langgraph 集成**           | ❌ 默认未集成                                    |
| **API 设计参考**                | ✅ https://docs.letta.com/api-reference/overview |
| **社区活跃度**                  | ✅ GitHub stars 16.6k                            |
| **论文**                        | ✅ memgpt: https://arxiv.org/abs/2310.08560      |

![img](pictures/platform_overview.png)

![img](pictures/platform_system.png)

![img](pictures/example_ade_screenshot_light.png)

#### 问题1：Letta(原MemGPT)的Memory管理方式是什么？是否采用分级管理？

Letta 采用了分级内存管理机制，灵感直接来自计算机操作系统的分层内存管理。

它把 Agent 的记忆分两个部分：

| 内存层次               | 对应 Letta 模块                                            | 功能作用                                                     |
| ---------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **主上下文（主存）**   | **`core memory`（核心内存块）**                            | **存在于 LLM 提示上下文（prompt window）内，用于实时推理。存储如 persona、human、系统设定等。** |
| **外部上下文（外存）** | **`archival memory`（归档块）、`recall memory`（召回块）** | **不在上下文窗口内，用于存储长期历史、完整对话记录等，需要显式 function 调用调入主上下文。** |
| FIFO 队列              | 最近对话消息队列                                           | 临时维护最近几轮消息，有窗口长度限制。超限后自动踢出、总结、归档到 recall memory。 |

**1️⃣ 固定窗口 + 无限外存**

由于 LLM 的上下文窗口（context window）是有限的（如 8k、16k、32k tokens），
Letta 通过设计：

重要、频繁使用的记忆 → 留在主上下文内，实时低延迟参与推理。

历史、长尾、低频信息 → 移入外部上下文，供归档和按需检索。

**2️⃣ 主动函数调用 memory 函数**

Letta 定义专门的 memory 函数（由 LLM 通过提示调用）：

- `core_memory_append` → 向核心记忆块追加。
- `core_memory_replace` → 替换核心记忆块内容。
- `archival_memory_insert` → 将消息归档入长期存储。
- `archival_memory_search` / `conversation_search` → 从归档/历史中检索。

通过这些函数，跨层数据流动由 LLM 自主驱动。

**3️⃣ 自动化队列管理与内存压力感知**

对应代码位置：

```bash
letta/settings.py → summarizer_settings.memory_warning_threshold
```

默认参数：

FIFO 队列超过 75% 时，系统发出 memory pressure 警告，提示 LLM 尽快触发 memory 函数整理。

**4️⃣ 核心设计价值**

Letta能够高效管理有限的上下文窗口，将最重要的信息保留在核心记忆中直接访问，同时将较大量的历史信息存储在外部，需要时再检索。此架构在设计上类似于计算机系统的内存层次结构，核心记忆类似RAM，外部存储类似磁盘，实现了记忆的分级管理。

| 挑战                         | Letta 解决方案                                               |
| ---------------------------- | ------------------------------------------------------------ |
| LLM 上下文窗口有限           | 分层管理 → 主存（core memory）用于实时推理，外存（archival + recall）用于长期归档 + 检索。 |
| 长时间对话保持一致性与连贯性 | 用 memory block、归档、总结、检索等机制，确保短期上下文 + 长期记忆都能被灵活调用。 |
| 内存管理复杂、需要智能调度   | 结合内存压力感知（如 75% 阈值）、FIFO 自动化总结、函数链调度，让 Agent 自动平衡 memory。 |



#### 问题2：Letta的记忆检索方式是什么？

**1️⃣ 字符串文本匹配检索**

    def conversation_search(self: "Agent", query: str, page: Optional[int] = 0) -> Optional[str]:

**2️⃣ 语义相似度检索**

    向量检索：从embeddings.py和passage_manager.py可以看出，Letta使用向量嵌入进行语义搜索
        文本首先通过parse_and_chunk_text函数分块，确保每块大小适合嵌入模型
        使用各种嵌入模型(OpenAIEmbeddings, AzureOpenAIEmbedding等)将文本转换为向量
        query_embedding函数处理搜索查询，生成标准化的向量表示

在 `PassageManager.insert_passage`：

```python
embedding = embed_model.get_text_embedding(text)
```

调用：

```python
from letta.embeddings import embedding_model
embed_model = embedding_model(agent_state.embedding_config)
```

例如：

```python
response = self.client.embeddings.create(input=text, model=self.model)
```

得到的 embedding（768 维或 1536 维向量）会存入 `AgentPassage` 或 `SourcePassage`。

当你做查询（`archival_memory_search`）时：  

- 将查询文本 `query` 转为 embedding。  
- 在数据库中比对（点积或余弦相似度），找最近的 embedding。  
- 返回 top-N 个匹配片段。

**3️⃣ 显式函数调用**
在 `letta/memory.py`：

```python
functions = get_memory_functions(cls: Memory)
```

LLM 调用：

- `archival_memory_insert()` → 插入  
- `archival_memory_search()` → 语义检索  
- `conversation_search()` → 对话中语义检索  

这些函数的作用是： 
把 LLM 的请求路由到 `PassageManager`，执行检索或写入，最终结果再送回 core memory。

graph TD
A[用户输入 query] --> B[LLM 触发 archival_memory_search]
B --> C[调用 PassageManager]
C --> D[query 转 embedding]
D --> E[与数据库 embedding 比对]
E --> F[取 top-N passage]
F --> G[回填 core memory (Memory.blocks)]
G --> H[进入 LLM 推理窗口]

**总结表**

| 机制         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| 存储结构证据 | 数据库存储 text + embedding；ORM 层用 AgentPassage、SourcePassage 封装 |
| 关键词检索   | 直接按 ID、时间、标签查询 ORM                                |
| 向量语义检索 | 用 embedding 向量，比对相似度（代码可扩展对接向量数据库）    |
| 调用方式     | LLM 调用 memory 函数，明确发起检索请求                       |
| 检索后填入   | 检索内容总结、剪裁后塞入 core memory，进入 prompt window     |

Letta的记忆检索系统综合了直接访问(核心记忆)和语义搜索(外部记忆)的优势，使代理能够高效访问上下文内信息，同时在需要时从大型外部存储中检索相关内容。向量嵌入和数据库支持使其能够处理大规模的记忆数据，实现高效的语义搜索。



#### 问题3：Letta在性能方面（延迟、token开销、准确率）的表现如何？

##### 表1：深度记忆检索(DMR)任务性能

| 模型                   | 准确率 | ROUGE-L (R) |
| ---------------------- | ------ | ----------- |
| GPT-3.5 Turbo          | 38.7%  | 0.394       |
| GPT-3.5 Turbo + MemGPT | 66.9%  | 0.629       |
| GPT-4                  | 32.1%  | 0.296       |
| GPT-4 + MemGPT         | 92.5%  | 0.814       |
| GPT-4 Turbo            | 35.3%  | 0.359       |
| GPT-4 Turbo + MemGPT   | 93.4%  | 0.827       |

这个表格展示了MemGPT在深度记忆检索任务上的表现。该任务要求代理回答关于之前会话中讨论过的话题的问题，测试了代理的长期记忆能力。结果显示，添加MemGPT后，所有模型的性能都有显著提升，特别是GPT-4和GPT-4 Turbo，准确率从约30%提升到90%以上。

##### 表2：对话开场白性能

| 方法          | SIM-1 | SIM-3 | SIM-H |
| ------------- | ----- | ----- | ----- |
| 人类          | 0.800 | 0.800 | 1.000 |
| GPT-3.5 Turbo | 0.830 | 0.812 | 0.817 |
| GPT-4         | 0.868 | 0.843 | 0.773 |
| GPT-4 Turbo   | 0.857 | 0.828 | 0.767 |

对话开场（conversation opener）性能。该代理的对话开场通过与黄金人格标签的相似度分数（SIM-1/3）以及与人工创建的开场白（SIM-H）的相似度分数进行评估。MemGPT 能够在使用多种底层模型的情况下，超越人工创建的对话开场的表现。这个表格展示了不同模型在生成个性化对话开场白时的表现。SIM-1和SIM-3分别表示与黄金标准个人标签的相似度，SIM-H表示与人类创建的开场白的相似度。结果表明，MemGPT能够生成与人类相媲美甚至更好的开场白。

##### 表3：嵌套键值检索任务准确率

![Screenshot from 2025-05-28 07-29-29.png](pictures/nesting.png)

嵌套键值（KV）检索任务性能。MemGPT 是唯一能够在超过 2 层嵌套水平上稳定完成嵌套 KV 任务的方法。
虽然 GPT-4 Turbo 作为基线表现更好，但与 GPT-4 Turbo 配合的 MemGPT 表现反而不如与 GPT-4 配合的 MemGPT。该任务要求代理执行多跳检索，找到通过多层引用关联的键值。结果表明，只有使用GPT-4的MemGPT能够在所有嵌套级别保持100%的准确率，展示了其优越的多跳信息检索能力。

##### 表4：文档问答任务性能

![Screenshot from 2025-05-28 07-26-13.png](pictures/retrieved.png)

文档问答（Document QA）任务性能。MemGPT 的性能不受上下文长度增加的影响。诸如截断（truncation）等方法可以扩展固定长度模型（如 GPT-4）的有效上下文长度，但随着所需压缩比例增大，这类压缩方法会导致性能下降。在该任务上，MemGPT 配合 GPT-4 与配合 GPT-4 Turbo 的运行结果是等效的。该任务测试了模型在处理大量文档时的能力。结果表明，MemGPT能够处理超出基础模型上下文窗口的文档量，并保持稳定的性能，不受文档数量增加的影响。

**实验结论摘要**

1. **长期记忆能力**：MemGPT显著提升了模型的长期记忆能力，使其能够在多会话对话中保持一致性和个性化

2. **大文档处理**：MemGPT能够分析远超基础模型上下文限制的大型文档

3. **多跳信息检索**：MemGPT在需要多步骤推理的任务中表现优异，如嵌套键值检索

4. **资源效率**：通过分层内存管理，MemGPT在有限的上下文窗口中实现了更高效的资源利用

   

#### 问题4：Letta如何支持与PostgreSQL集成？特别是pgvector/Apache AGE扩展数据库的集成？

已原生支持 PostgreSQL 和 pgvector 向量检索

##### Letta 架构入口

Letta 的数据库访问主要集中在以下模块：

- `letta/server/db.py`：数据库注册、连接管理（PostgreSQL/SQLite 自动切换）
- `letta/orm/sqlalchemy_base.py`：ORM 基类，支持 embedding 检索
- `letta/services/passage_manager.py`：业务逻辑层，插入 embedding 片段（passage）

##### PostgreSQL 集成机制

letta/server/db.py中核心逻辑：

```python
if settings.letta_pg_uri_no_default:
    engine = create_engine(settings.letta_pg_uri, **self._build_sqlalchemy_engine_args(is_async=False))
    self._engines["default"] = engine
```

说明：如果设置了 `LETTA_PG_URI`，将自动切换为 PostgreSQL；否则使用默认 `sqlite.db`。

##### pgvector 支持（向量检索）

在 `letta/orm/sqlalchemy_base.py::_list_preprocess()` 中：

```python
if query_embedding:
    if settings.letta_pg_uri_no_default:
        # PostgreSQL with pgvector
        query = query.order_by(cls.embedding.cosine_distance(query_embedding).asc())
```

##### embedding 向量生成与存储

在 `letta/services/passage_manager.py::insert_passage()` 中：

```python
embedding = embed_model.get_text_embedding(text)
```

然后包装成 passage 存储：

```python
PydanticPassage(
    text=text,
    embedding=embedding,
    embedding_config=...,
)
```

ORM 模型：`AgentPassage`， `SourcePassage`

数据库字段 `embedding` 会映射为 `vector`，支持 pgvector 查询。

##### Apache AGE 支持

当前 Letta 源码 **未直接集成 Apache AGE **（AGE 是 PostgreSQL 扩展，可与 pgvector 共存）



#### 问题5：Letta是否支持与LangGraph集成？如何集成？

没有找到任何官方支持或文档表明Letta(原MemGPT)与LangGraph有直接集成。



#### 问题6：API设计参考

https://docs.letta.com/api-reference/overview



# LangMem 集成与特性分析总结

| **关注点**                      | **支持情况**: https://github.langchain.ac.cn/langmem/        |
| ------------------------------- | ------------------------------------------------------------ |
| **Memory 管理**                 | ✅ 分层管理：短期记忆摘要+长期语义/情景/程序性记忆，支持主动与后台提取 |
| **记忆检索方式**                | ✅ 直接访问(通过键获取特定记忆)，语意访问(语义相似度查找记忆、向量)，元数据过滤(根据记忆的属性进行过滤) |
| **性能（延迟、token、准确率）** | ❌ 未找到                                                     |
| **PostgreSQL 集成（扩展）**     | ✅ 通过LangGraph的BaseStore抽象支持pgvector                   |
| **与 langgraph 集成**           | ✅ 深度集成LangGraph，提供专门的图节点和工具，支持状态流和配置共享 |
| **API 设计参考**                | ✅ https://github.langchain.ac.cn/langmem/reference/          |
| **社区活跃度**                  | ⚠️ 相对较新项目，但基于LangGraph生态开发，具备专业支持和活跃维护, Star 502 github |
| **论文**                        | ❌ 未找到直接相关学术论文，但有详细的概念和技术文档           |

![Hot Path Quickstart Diagram](pictures/hot_path_vs_background.png)

#### 问题1：LangMem的Memory管理方式是什么？是否采用分级管理？

| 记忆类型 | 目的       | 智能体示例               | 人类示例                   | 典型存储模式   |
| -------- | ---------- | ------------------------ | -------------------------- | -------------- |
| 语义     | 事实与知识 | 用户偏好；知识三元组     | 知道 Python 是一种编程语言 | 档案或集合     |
| 情景     | 过往经历   | 少样本示例；过往对话总结 | 记住你上班的第一天         | 集合           |
| 程序     | 系统指令   | 核心个性和响应模式       | 知道如何骑自行车           | 提示规则或集合 |

##### 集成模式

LangMem 的记忆工具被组织在两个集成模式层中

##### 1. 核心 API

核心来说，LangMem 提供了转换记忆状态且无副作用的函数。这些原语是记忆操作的构建块

- [**记忆管理器 (Memory Managers)**](https://github.langchain.ac.cn/langmem/reference/memory/#langmem.create_memory_manager)：根据新的对话信息，提取新记忆，更新或删除过时记忆，以及整合和概括现有记忆
- [**提示优化器 (Prompt Optimizers)**](https://github.langchain.ac.cn/langmem/reference/prompt_optimization/#langmem.create_prompt_optimizer)：根据对话信息（带有可选反馈）更新提示规则和核心行为

这些核心函数不依赖于任何特定的数据库或存储系统。您可以在任何应用中使用它们。

##### 2. 有状态集成

再往上一层依赖于 LangGraph 的长期记忆存储。这些组件使用上面的核心 API 来转换存储中存在的记忆，并在新的对话信息到来时根据需要进行 upsert/删除。

- [**存储管理器 (Store Managers)**](https://github.langchain.ac.cn/langmem/reference/memory/#langmem.create_memory_store_manager)：自动持久化提取的记忆
- [**记忆管理工具 (Memory Management Tools)**](https://github.langchain.ac.cn/langmem/reference/tools/#langmem.create_manage_memory_tool)：赋予智能体直接访问记忆操作的能力

如果您正在使用 LangGraph Platform 或 LangGraph OSS，可以使用这些工具，因为它们是为您的智能体添加记忆能力的简便方法。



#### 问题2：LangMem的记忆检索方式是什么？

- [**直接访问 (Direct Access)**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.get)：通过键获取特定记忆
- [**语义搜索 (Semantic Search)**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.search)：通过语义相似度查找记忆
- [**元数据过滤 (Metadata Filtering)**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.search)：根据记忆的属性进行过滤



#### 问题3：LangMem在性能方面（延迟、token开销、准确率）的表现如何？

没有找到具体的性能基准数据



#### 问题4：LangMem如何支持与PostgreSQL集成？特别是pgvector/Apache AGE扩展数据库的集成？

LangMem通过LangGraph的BaseStore抽象层支持PostgreSQL和pgvector集成。



#### 问题5：LangMem是否支持与LangGraph集成？如何集成？

LangMem不仅支持与LangGraph集成，而且是专为LangGraph设计的内存管理系统，提供无缝集成体验。
可以通过将 LangMem 的**记忆工具**集成到 LangGraph 的代理框架中。
LangMem与LangGraph的集成是原生和全面的，提供了多种集成方式：图节点、工具、状态访问和配置共享。

例如：`graphs/semantic.py`文件展示了LangMem与LangGraph的原生集成：

```python
# graphs/semantic.py - 官方集成示例
from langgraph.func import entrypoint
from langgraph.store.memory import InMemoryStore
from pydantic import BaseModel

from langmem import create_memory_store_manager

store = InMemoryStore(
    index={
        "dims": 1536,
        "embed": "openai:text-embedding-3-small",
    }
)
manager = create_memory_store_manager(
    "anthropic:claude-3-5-sonnet-latest",
    namespace=("memories", "{langgraph_user_id}"),
)

@entrypoint(store=store)
async def graph(message: str):
    # 硬编码回复(示例)
    response = {"role": "assistant", "content": "I'll remember that preference"}
    await manager.ainvoke(
        {"messages": [{"role": "user", "content": message}, response]}
    )
    return response
```

#### 问题6：API设计参考

LangMem提供了清晰API设计： https://github.langchain.ac.cn/langmem/reference/



# Memary 集成与特性分析总结

| **关注点**                      | **支持情况**: https://github.com/kingjulio8238/Memary        |
| ------------------------------- | ------------------------------------------------------------ |
| **Memory 管理**                 | ✅ 分层管理：MemoryStream记忆流(短期)+EntityKnowledgeStore实体知识存储(长期)，外接知识图谱存储 |
| **记忆检索方式**                | ✅ 知识图谱检索+频率权重+时间排序+同义词扩展，支持混合内外部检索 |
| **性能（延迟、token、准确率）** | ❌无论文或官方网站提供                                        |
| **PostgreSQL 集成（扩展）**     | ❌ 无原生支持，当前仅支持Neo4j和FalkorDB图数据库              |
| **与 langgraph 集成**           | ❌ 无原生支持，无LangGraph依赖                                |
| **API 设计参考**                | ❌暂无官方网站提供                                            |
| **社区活跃度**                  | ❌ Star 2.2k github, 7 months ago后没更新了                   |
| **论文**                        | ❌ 未见相关学术论文                                           |

简述：

![memary overview](pictures/system.png)

#### 问题1：Memary的Memory管理方式是什么？是否采用分级管理？

1️⃣ 短期记忆（MemoryStream）

- **模块** :`memary.memory.memory_stream.MemoryStream`
  
- **存储** : 一个个 `MemoryItem`，记录单个实体和时间戳。
  
- **来源** : 直接从每次对话、每次调用中添加。
  
- **作用** : 短期保留出现过的实体，类似“最近看过/最近想过的事”。
  
- **代码证据**

  ```python
  self.memory_stream.add_memory(entities)
  self.memory_stream.save_memory()
  ```

2️⃣ 长期记忆（EntityKnowledgeStore）

- **模块** : `memary.memory.entity_knowledge_store.EntityKnowledgeStore`
  
- **存储** : 一个个 `KnowledgeMemoryItem`，聚合实体出现次数和最近一次出现时间。
  
- **来源** : 把 MemoryStream 中的短期记忆“汇总”为长期统计。
  
- **作用** : 构建更稳定的“知识性偏好”或“重要实体”，用于后续推理。
  
- **代码证据**

  ```python
  self.entity_knowledge_store.add_memory(self.memory_stream.get_memory())
  self.entity_knowledge_store.save_memory()
  ```


  3️⃣ 分层结构在明显代码证据
        在 `ChatAgent.add_chat()` 中：

```python
if entities:
    self.memory_stream.add_memory(entities)
    self.memory_stream.save_memory()
    self.entity_knowledge_store.add_memory(self.memory_stream.get_memory())
    self.entity_knowledge_store.save_memory()
```

这段明确表明：
短期 memory（MemoryStream） → 汇总到  长期 memory（EntityKnowledgeStore）
并且长期 memory 不是简单叠加，而是：聚合出现频率（`count`）和 聚合最近时间（`date`）
这就是一种典型的 **分层管理、分级存储**。

| 方面         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| 是否分级     | 是，分为短期（MemoryStream）和长期（EntityKnowledgeStore）两层 |
| 短期记忆     | 存实体 + 时间戳，流式增长                                    |
| 长期记忆     | 聚合实体 → 出现次数、最近时间，形成知识性存储                |
| 主要用途     | 短期提供上下文回忆，长期提供重要性聚合、推理使用             |
| 明显代码位置 | `ChatAgent.add_chat()` 调用 MemoryStream 和 EntityKnowledgeStore 的 add_memory 和 save_memory 方法 |



#### 问题2：Memary的记忆检索方式是什么？

Memary实现了多种记忆检索方式：

**图谱检索**：通过`KnowledgeGraphRAGRetriever`实现基于图结构的检索

```python
# /src/memary/agent/base_agent.py
graph_rag_retriever = KnowledgeGraphRAGRetriever(
    storage_context=self.storage_context,
    verbose=True,
    llm=self.llm,
    retriever_mode="keyword",
    synonym_expand_fn=custom_synonym_expand_fn,
)

self.query_engine = RetrieverQueryEngine.from_args(
    graph_rag_retriever,
)
```

```
#Cypher查询：支持直接的图查询语言
# /src/memary/agent/base_agent.py
def generate_string(entities):
    cypher_query = "MATCH p = (n) - [*1 .. 2] - ()\n"
    cypher_query += "WHERE n.id IN " + str(entities) + "\n"
    cypher_query += "RETURN p"
```

**混合检索策略**：结合内部知识图记忆 和 外部查询web

```python
# /src/memary/agent/base_agent.py
def search(self, query: str) -> str:
    """Search the knowledge graph or perform search on the web if information is not present in the knowledge graph"""
    response = self.query_engine.query(query)

    if response.metadata is None:
        return self.external_query(query)
    else:
        return response
```

特点: 先尝试内部知识图谱检索，检索失败后回退到外部查询。



#### 问题3：Memary在性能方面（延迟、token开销、准确率）的表现如何？

没有具体的性能基准数据



#### 问题4：Memary如何支持与PostgreSQL集成？特别是pgvector/Apache AGE扩展数据库的集成？

基于提供的源代码，Memary当前**没有**直接提供对PostgreSQL与pgvector或Apache AGE的集成的原生支持。代码显示Memary主要支持以下图数据库：Neo4j 图数据库 和 FalkorDB 图数据库



#### 问题5：Memary是否支持与LangGraph集成？如何集成？

根据提供的源代码，Memary当前**没有**直接与LangGraph集成的实现。代码中没有导入或使用LangGraph的痕迹。



#### 问题6：Memary的API设计参考

无网站提供，暂无



# Graphiti 集成与特性分析总结

| **关注点**                      | **支持情况:** https://help.getzep.com/graphiti/graphiti/overview |
| ------------------------------- | ------------------------------------------------------------ |
| **Memory 管理**                 | ✅基于图结构的系统，通过Node和Edge构建知识图谱                |
| **记忆检索方式**                | ✅支持语义向量、文本和基于图的三种搜索方法                    |
| **性能（延迟、token、准确率）** | ✅https://arxiv.org/abs/2501.13956                            |
| **PostgreSQL 集成（扩展）**     | ❌ 原生使用Neo4j图数据库，未见PostgreSQL/pgvector集成代码     |
| **与 langgraph 集成**           | ✅ 提供示例agent.ipynb展示与LangGraph集成，支持作为工具使用   |
| **API 设计参考**                | ✅https://help.getzep.com/graphiti/graphiti/quick-start       |
| **社区活跃度**                  | ✅Star 9.8k github                                            |
| **论文**                        | ✅https://arxiv.org/abs/2501.13956                            |

简述：Graphiti 是 Zep 团队开发的一个 temporal knowledge graph（时间感知知识图谱）框架，是 Zep 产品线的一部分，用于 agent memory（代理记忆）这一场景。

传统的RAG方法通常依赖于批处理和静态数据汇总，使其在频繁变化的数据面前效率低下。Graphiti通过提供以下功能来解决这些挑战：
实时增量更新： 无需批量重新计算，立即集成新的数据集。
双时间数据模型： 明确跟踪事件发生和摄取时间，允许准确的时点查询。
高效的混合检索： 结合语义嵌入、关键词（BM25）和图遍历，实现低延迟查询，而无需依赖于LLM汇总。
自定义实体定义： 通过简单的Pydantic模型支持灵活的本体创建和开发者定义的实体。
可扩展性： 高效管理大数据集，适合企业环境。

![graphiti intro slides](pictures/graphiti-graph-intro.gif)

![graphiti demo slides](pictures/graphiti-intro-slides-stock-2.gif)

#### 问题1：Graphiti的Memory管理方式是什么？是否采用分级管理？

Graphiti 本质上 不是传统意义上的 memory 模块（如 LangChain、Memary 这种 RAM/档案式内存），没有显式地实现短期/长期记忆的标准分级，但其图结构具有隐式分层的能力，可以通过不同的遍历深度访问近期或远期记忆，实现了一种更灵活的记忆分级方式。

它用：
Neo4j 图数据库 → 持久存储节点（Node）、关系（Edge）、群体（Community）
向量 embedding → 强化节点与边的语义相似性检索
reranker（排序器，如 cross-encoder, RRF, MMR）→ 优化搜索结果
换句话说，Graphiti 的“记忆” = 完整的知识图 + 实时 embedding 检索。
Graphiti采用了基于Neo4j图数据库的管理模式，构建了一个多维度的知识图谱系统, 结构化图存储管理。

| 模块      | 存储什么                                                     | 特点                           |
| --------- | ------------------------------------------------------------ | ------------------------------ |
| Node      | 节点信息（带 embedding）                                     | 直接存储到 Neo4j，按 uuid 查找 |
| Edge      | 节点之间的关系（带 embedding）                               | 直接存储到 Neo4j，按 uuid 查找 |
| Embedding | 需要时调用 `EmbedderClient` 生成，用于 similarity，但不是默认必须 |                                |



#### 问题2：Graphiti的记忆检索方式是什么？

Graphiti 实际上是一套围绕 图数据库（Neo4j）+ embedding 向量化 + reranker 组合搜索 的混合系统。

它的“记忆” ≈ 持久化知识图，而它的“检索”主要靠：
✅ 文本全匹配（fulltext search）
✅ 向量相似度（vector similarity search）
✅ 图遍历（graph traversal / BFS 搜索）
✅ 多轮 reranker 重排（RRF, MMR, cross-encoder）

它解决了哪些问题？

Graphiti 主要针对传统 RAG 的这些痛点：
1️⃣ 批处理慢 → 改为 增量更新，不用重算整个图。
2️⃣ 时序追踪弱 → 引入 bi-temporal 数据模型，区分：事件发生时间, 系统收录时间
3️⃣ 检索效率低 → 采用：
	semantic embedding 语义向量检索
	keyword (BM25) 关键词检索
	graph traversal（图遍历）
4️⃣ 没法定义自定义实体 → 用 Pydantic 模型支持开发者自定义 node / edge 类型。



#### 问题3：Graphiti在性能方面（延迟、token开销、准确率）的表现如何？

**表2：LongMemEvals**

| 记忆     | 模型        | 分数  | 延迟   | 延迟 IQR | 平均上下文 [Tokens](https://sharenet.ai/tokenization/) |
| -------- | ----------- | ----- | ------ | -------- | ------------------------------------------------------ |
| 全上下文 | gpt-4o-mini | 55.4% | 31.3 s | 8.76 s   | 115k                                                   |
| Zep      | gpt-4o-mini | 63.8% | 3.20 s | 1.31 s   | 1.6k                                                   |
| 全上下文 | gpt-4o      | 60.2% | 28.9 s | 6.01 s   | 115k                                                   |
| Zep      | gpt-4o      | 71.2% | 2.58 s | 0.684 s  | 1.6k                                                   |

通过问题类型的分析显示，使用Zep的gpt-4o-mini在六种类别中的四种中表现出改进，其中在复杂的问类型中改进最大：单会话偏好、多会话和时序推理。当使用gpt-4o时，Zep在知识更新类别中进一步展示了改进的性能，突出了其与更强大的模型配合使用时更有效。然而，可能需要额外的开发来提高不太强大的模型对Zep的时间数据的理解。

**表3：LongMemEvals问题类型分解**

| 问题类型   | 模型        | 全上下文 | Zep   | 增量   |
| ---------- | ----------- | -------- | ----- | ------ |
| 单会话偏好 | gpt-4o-mini | 30.0%    | 53.3% | 77.7%↑ |
| 单会话助手 | gpt-4o-mini | 81.8%    | 75.0% | 90'6%↑ |
| 时序推理   | gpt-4o-mini | 36.5%    | 54.1% | 48.2%↑ |
| 多会话     | gpt-4o-mini | 40.6%    | 47.4% | 16.7%↑ |
| 知识更新   | gpt-4o-mini | 76.9%    | 74.4% | 3.36%↓ |
| 单会话用户 | gpt-4o-mini | 81.4%    | 92.9% | 14.1%↑ |
| 单会话偏好 | gpt-4o      | 20.0%    | 56.7% | 184%↑  |
| 单会话助手 | gpt-4o      | 94.6%    | 80.4% | 17.7%↓ |
| 时序推理   | gpt-4o      | 45.1%    | 62.4% | 38.4%↑ |
| 多会话     | gpt-4o      | 44.3%    | 57.9% | 30.7%↑ |
| 知识更新   | gpt-4o      | 78.2%    | 83.3% | 6.52%↑ |
| 单会话用户 | gpt-4o      | 81.4%    | 92.9% | 14.1%↑ |

这些结果证明了Zep能够在模型规模上提高性能，与更强大的模型配合使用时，在复杂和细腻的问题类型上观察到最显著的改进。延迟改进尤为显著，Zep将响应时间减少了大约90%，同时保持了更高的准确性。



#### 问题4：Memary如何支持与PostgreSQL集成？特别是pgvector/Apache AGE扩展数据库的集成？

没说支持，源码无支持



#### 问题5：Graphiti是否支持与LangGraph集成？如何集成？

可以和 LangGraph 搭配集成使用，尤其在 agent 流程里。

| **工具**  | **定位**                                                     |
| --------- | ------------------------------------------------------------ |
| Graphiti  | 一个时间感知知识图的底层框架，用于管理、更新、查询图结构化的记忆和关系（记忆层） |
| LangGraph | LangChain 的一部分，用于构建多步骤、多状态、分支的 agent 流程图 (推理层） |

Graphiti确实支持与LangGraph集成，提供的示例代码`examples/langgraph-agent/agent.ipynb`展示了集成方法：

```
# Graphiti: 图数据库客户端，用于上下文管理
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType

# LangGraph: 流程图和对话管理
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

# LangChain LLM 接入
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

# 1. 用 Graphiti 初始化图数据库连接（Neo4j）
client = Graphiti(neo4j_uri, neo4j_user, neo4j_password)

# 2. 定义 LangChain 的 LLM，并绑定 Graphiti 提供的工具
llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0).bind_tools([get_shoe_data])

# 3. 在 LangGraph 中定义 chatbot 节点，内部调用 Graphiti 查询用户上下文
async def chatbot(state):
    # Graphiti 查询：基于最近一条消息搜索图数据库
    edge_results = await client.search(
        f"{state['user_name']}: {state['messages'][-1].content}",
        center_node_uuid=state['user_node_uuid'],
        num_results=5
    )
    facts_string = '-' + '\n- '.join([edge.fact for edge in edge_results]) or 'No facts found.'

    # LangGraph + LangChain：构造系统提示消息并调用 LLM
    system_message = SystemMessage(content=f"用户相关事实：{facts_string}")
    messages = [system_message] + state['messages']
    response = await llm.ainvoke(messages)

    # Graphiti 写入：把生成结果记录进图数据库
    asyncio.create_task(
        client.add_episode(
            name='Chatbot Response',
            episode_body=f'{state["user_name"]}: {state["messages"][-1].content}\nSalesBot: {response.content}',
            source=EpisodeType.message,
            reference_time=datetime.now(timezone.utc),
            source_description='Chatbot',
        )
    )
    return {'messages': [response]}

# 4. 用 LangGraph 构建流程图，将 LLM 节点和工具节点组合起来
graph_builder = StateGraph(dict)
memory = MemorySaver()
tool_node = ToolNode([get_shoe_data])

graph_builder.add_node('agent', chatbot)
graph_builder.add_node('tools', tool_node)
graph_builder.add_edge(START, 'agent')
graph_builder.add_conditional_edges('agent', should_continue, {'continue': 'tools', 'end': END})
graph_builder.add_edge('tools', 'agent')
graph = graph_builder.compile(checkpointer=memory)
```

1. LangGraph 负责：管理多步 agent 流程(分支、条件、循环), 控制不同模块的调用(如 LLM、外部 API、工具)

2. Graphiti 提供：存储 agent 在运行中生成的知识（facts、episodes、entities）, 提供快速、丰富的 graph 查询接口，供 agent 在推理中用（例如查找过去交互、查询相关实体）



#### 问题6：Graphiti的API设计参考

查看: https://help.getzep.com/graphiti/graphiti/quick-start



# Cognee 集成与特性分析总结

| **关注点**                      | **支持情况:** https://docs.cognee.ai/                        |
| ------------------------------- | ------------------------------------------------------------ |
| **Memory 管理**                 | ✅基于图结构的记忆系统,通过Node和Edge构建知识图谱,支持属性和关系的灵活表示 |
| **记忆检索方式**                | ✅基于向量的相似度检索 + 基于图的检索                         |
| **性能（延迟、token、准确率）** | ✅Human-LLM Correctness，DeepEval Correctness，DeepEval F1，EM 在这四个指标中，Cognee(dreamify) 比 Graphiti 和 mem0 优秀 |
| **PostgreSQL 集成（扩展）**     | ✅原生支持 PostgreSQL + pgvector                              |
| **与 langgraph 集成**           | ❌没有明确标注与langgraph的原生集成                           |
| **API 设计参考**                | ✅https://docs.cognee.ai/tutorials/use-the-api                |
| **社区活跃度**                  | ✅Star 2.2k github                                            |

Cognee架构概述 Cognee架构围绕任务，管道和键入数据点，共同努力将原始数据转换为有意义的知识图。

![Cognification Process](pictures/architecture.png)

Cognee架构。

![Cognee Architecture](pictures/architecture2.png)

Cognee管道。

![Cognee Pipeline Flow](pictures/cognee-pipeline-flow.85364707.png)

#### 1. Cognee如何管理记忆？是否采用分层/分级管理？

虽然Cognee没有显式地实现短期/长期记忆的标准分级，但其图结构具有隐式分层的能力，可以通过不同的遍历深度访问近期或远期记忆，实现了一种更灵活的记忆分级方式。

**仓库文件路径**: `cognee/modules/graph/cognee_graph/CogneeAbstractGraph.py` 和 `cognee/modules/graph/cognee_graph/CogneeGraph.py`

**仓库源代码**:

```python
# CogneeAbstractGraph.py
from abc import ABC, abstractmethod
from typing import List, Dict, Union
from cognee.modules.graph.cognee_graph.CogneeGraphElements import Node, Edge
from cognee.infrastructure.databases.graph.graph_db_interface import GraphDBInterface

class CogneeAbstractGraph(ABC):
    """
    Abstract base class for representing a graph structure.
    """
    @abstractmethod
    def add_node(self, node: Node) -> None:
        """Add a node to the graph."""
        pass

    @abstractmethod
    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph."""
        pass
    
    # ...其他方法略...
```

**解释**: Cognee采用了基于图结构的记忆管理方式，与传统的序列或分层记忆系统有本质区别。从源码分析，其记忆管理具有以下特点：

1. **图结构化记忆**: 通过`CogneeGraph`类实现，记忆以节点(Node)和边(Edge)的形式存储，形成知识图谱，而不是简单的线性结构。这允许更复杂的语义关联和多维度的记忆组织。

2. **混合记忆表示**: 结合向量嵌入和图结构，通过`map_vector_distances_to_graph_nodes`等方法，将向量空间中的语义相似性映射到图结构中。

3. **关系优先**: 边(Edge)不仅连接节点，还包含关系类型和属性，使记忆不只存储内容，还存储内容间的关系。这种方式更接近人类记忆的联想网络。

4. **可扩展抽象层**: 通过`CogneeAbstractGraph`抽象基类和`CogneeGraph`实现类的分离，系统可以适配不同的底层数据库和表示方法。

5. **上下文感知**: 图结构天然支持上下文，通过节点的关联边可以快速检索相关信息，增强了记忆的上下文理解能力。

   

#### 2. Cognee记忆检索方式

主要是向量检索 和 图结构检索。

**仓库文件路径**: `cognee/modules/retrieval` 

```
await vector_engine.search
...
graph_engine = await get_graph_engine()
exact_node = await graph_engine.extract_node(node_id)
```



#### 3. 性能指标

**问题**: Cognee在性能方面(延迟、token开销、准确率)有何表现？有哪些可量化的指标？

![metrics_comparison.png](pictures/metrics_comparison.png)

![cognee_comparison.png](pictures/cognee_comparison.png)

Human-LLM Correctness: 这是通过人工 + LLM 协助的混合评估，即用人类（或者带人工校验的 LLM 评审）判断答案的总体正确性。它通常更宽容，允许不同表述、允许合理推理，而不是死板比对。[ 0–1（越接近 1 越好）]

DeepEval Correctness: 用自动化评估工具（DeepEval）判断系统回答是否“总体上”是正确的。它更偏向于语义层面的正确，即答案是否答对大意，而不一定要字词完全对上。[ 0–1（越接近 1 越好）]

DeepEval F1: F1 分数是传统信息检索里的综合指标，结合了：精确率（Precision）：你答出的内容中有多少是对的？召回率（Recall）：参考答案中有多少你覆盖到了？[ 0–1（越接近 1，表示覆盖和命中越全面）]

EM (Exact Match): Exact Match 指严格的“一字不差完全匹配”，也就是预测的答案和参考答案完全一致。
哪怕多了个空格、少了个词、换了个同义词，都算不完全匹配。[ 0–1（越接近 1，表示模型完全命中）]



Cognee的性能测试结果表明，其基于图结构的记忆管理方式能够在准确性、覆盖率和效率之间取得良好平衡，特别是在Human-LLM评分方面的优势，说明其生成结果更符合人类评判标准。



#### 4. 如何与PostgreSQL集成？是否支持pgvector扩展？

**仓库文件路径**: `cognee/infrastructure/databases/vector/pgvector/PGVectorAdapter.py`

**仓库源代码**:

```python
from pgvector.sqlalchemy import Vector

class PGVectorAdapter(SQLAlchemyAdapter, VectorDBInterface):
    def __init__(
        self,
        connection_string: str,
        api_key: Optional[str],
        embedding_engine: EmbeddingEngine,
    ):
        self.api_key = api_key
        self.embedding_engine = embedding_engine
        self.db_uri: str = connection_string

        relational_db = get_relational_engine()

        # If postgreSQL is used we must use the same engine and sessionmaker
        if relational_db.engine.dialect.name == "postgresql":
            self.engine = relational_db.engine
            self.sessionmaker = relational_db.sessionmaker
        else:
            # If not create new instances of engine and sessionmaker
            self.engine = create_async_engine(self.db_uri)
            self.sessionmaker = async_sessionmaker(bind=self.engine, expire_on_commit=False)

        # Has to be imported at class level
        # Functions reading tables from database need to know what a Vector column type is
        from pgvector.sqlalchemy import Vector
        self.Vector = Vector
```

**解释**: Cognee提供了全面的PostgreSQL和pgvector的支持，具体如下：

1. **向量相似度查询**: `search`方法使用`cosine_distance`进行相似度计算，这是pgvector的核心功能，支持高效的近似最近邻(ANN)搜索。
2. **异步操作**: 所有数据库操作都通过`async/await`实现异步执行，配合`async_sessionmaker`提高系统吞吐量。
3. **灵活查询机制**: 支持通过文本(`query_text`)或直接提供向量(`query_vector`)进行查询，满足不同场景需求。



#### 5. 是否支持与langgraph集成

Cognee没有明确标注与langgraph的原生集成



#### 6. API设计参考

#### 概述(https://docs.cognee.ai/tutorials/use-the-api)

本教程演示如何使用 Docker 和 cURL 与 cognee 的 API 服务交互。该 API 允许你:

- **设置** 你的环境并配置 API 密钥
- **启动** API 服务（通过 Docker）
- **认证** 以获取访问令牌（access token）
- **上传** 文档（本例中是《爱丽丝梦游仙境》的文本文件）
- **处理** 文档，通过 cognee 的处理管道
- **搜索** 处理后的内容，使用自然语言查询

#### 步骤 1: 环境设置

首先，创建一个 .env 文件，其中包含你的 API 密钥。这个密钥用于支持 cognee 的底层语言模型（LLM）

```
echo 'LLM_API_KEY="YOUR-KEY"' > .env
```

*此步骤确保 cognee 可以访问你的 LLM 凭证。*

#### 步骤 2: 启动 API 服务

拉取并运行 cognee 的 Docker 容器:

```
docker pull cognee/cognee:main
docker run -d -p 8000:8000 --name cognee_container -v $(pwd)/.env:/app/.env cognee/cognee:main
```

*此命令会拉取最新的 cognee 镜像，并启动它，同时挂载你的环境文件。*

#### 步骤 3: 认证

使用默认的账号密码获取访问令牌（access token）:

```
access_token=$(curl --location 'http://127.0.0.1:8000/api/v1/auth/login' \
  --form 'username="default_user@example.com"' \
  --form 'password="default_password"' | sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p')
 
echo "Access Token: $access_token"
```

*获取到的访问令牌将在后续所有 API 请求中用于认证。*

#### 步骤 4: 上传文档

将《爱丽丝梦游仙境》上传到名为 test-dataset 的数据集:

```
curl -s https://raw.githubusercontent.com/topoteretes/cognee/main/examples/data/alice_in_wonderland.txt | \
curl --location 'http://127.0.0.1:8000/api/v1/add' \
  --header "Authorization: Bearer $access_token" \
  --form 'data=@-' \
  --form 'datasetName="test-dataset"'
```

*这会上传文档并将其与指定的数据集名称关联起来。*

#### 步骤 5: 处理文档

处理刚刚上传的数据集:

```
curl --location 'http://127.0.0.1:8000/api/v1/cognify' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "datasets": ["test-dataset"]
}'
```

*这一步会将文档送入 cognee 的处理管道，为后续查询做好准备。*

#### 步骤 6: 执行搜索查询

现在你可以对已处理的数据集进行查询。以下是使用 COMPLETION 搜索类型的三个示例查询:

#### 查询 1: 列出重要角色

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "List me all the important characters in Alice in Wonderland."
}'
```

#### 查询 2: 爱丽丝是怎么进入仙境的？

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "How did Alice end up in Wonderland?"
}'
```

#### 查询 3: 描述爱丽丝的性格

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "Tell me about Alice'\''s personality."
}'
```

#### 步骤 7: 删除文档

我们来移除已上传的数据集:

```
curl -s https://raw.githubusercontent.com/topoteretes/cognee/main/examples/data/alice_in_wonderland.txt | \
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/delete' \
  --header "Authorization: Bearer $access_token" \
  --form 'data=@-' \
  --form 'datasetName="test-dataset"' \
  --form 'mode="hard"'
}'
```