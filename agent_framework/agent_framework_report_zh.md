 # **如何选型？热门 AI Agent 框架深度横评**
生成式 AI 的爆发式发展让技术选型成为开发者面临的首要挑战。几乎每天都有新的框架、工具或技术涌现，无论是个人开发者还是企业团队，在利用大语言模型（LLM）构建创新应用时，都会直面一个问题：“哪款框架最适合我的场景？”本文将从开发人员的视角，从多个维度深度横评五个主流的 AI Agent 框架——LangGraph、LlamaIndex、PydanticAI、AutoGen 和 CrewAI，为开发者提供实操导向的参考。**需要说明的是，在本文中，我们主要侧重于评测这些框架在搭建非代理型（Non-Agentic）AI Workflow 时的表现。**

## 为什么需要LLM框架？
LLM 开发框架是为简化 AI 应用（如 Agent、Workflow、RAG 等）的创建、部署与管理而设计的软件平台。这些框架提供预构建组件、抽象接口与开发工具，帮助开发者高效构建复杂 AI 系统。通过标准化的开发范式与模块化架构，LLM 框架让开发者能够聚焦于应用的独特逻辑与创新，而无需重复造轮子。无论是快速原型验证还是生产级部署，根据自己的需求场景合理的选择LLM 框架，能够显著降低开发门槛与时间成本。

## 工作流的核心价值
<font style="color:rgba(0, 0, 0, 0.87);">工作流是一种事件驱动、基于步骤的方法，用于控制应用程序的执行流。随着生成式 AI 应用程序变得越来越复杂，管理数据流和控制应用程序的执行变得越来越困难。 工作流将任务拆解为模块化的子步骤，提供更高的灵活性和可维护性，特别在多代理协作或跨系统交互场景中，能显著提升开发效率和系统鲁棒性。  </font>

## <font style="color:rgba(0, 0, 0, 0.87);">代理型与非代理型工作流的区别</font>
![agentic_workflow.png](pictures/agentic_workflow.png)

<font style="color:rgba(0, 0, 0, 0.87);">AI 工作流根据自主性可分为非代理型（Non-Agentic）和代理型（Agentic）：</font>

+ **非代理型工作流**<font style="color:rgba(0, 0, 0, 0.87);">：依赖 LLM 的输入-输出能力，执行预定义的确定性步骤。例如，文本摘要任务可能是：输入长文本 → LLM 生成摘要 → 输出结果。此类工作流适合内容生成、数据处理等规则明确的场景，但缺乏动态决策和环境适应能力。</font>
+ **代理型工作流**<font style="color:rgba(0, 0, 0, 0.87);">：由 AI 代理动态执行任务，具备推理、工具调用和上下文记忆能力。代理能在授权范围内自主收集信息、调用外部 API 或做出决策。例如，一个智能客服代理可通过分析用户意图、查询 CRM 系统并生成个性化回复，动态处理复杂交互。代理型工作流因其响应性和自适应性，特别适合多步骤、交互式或跨系统的场景。</font>

## <font style="color:rgba(0, 0, 0, 0.87);">如何选择？</font>
这里推荐开发者可以从下面三个方向去思考和评估你的实际开发需求：

### 任务能不能拆成清晰步骤？
+ **能拆**：考虑选 **非代理型工作流**，拆成 Workflow。  
如果任务可以分解为明确的步骤（如数据提取 → 分析 → 生成报告），用非代理型工作流最省力。每个步骤像流水线，稳定、可控，适合内容生成、数据处理等规则明确的场景。  
**何时拆分？** 当任务有可靠的中间检查点（类似“过程奖励模型” PRM），比如每步输出可以验证正确性，就该拆分 Workflow。拆分后能插入验证工具，发现问题就打回重做，降低出错风险。  
**例子**：生成财务报表，拆成“拉数据 → 计算 → 格式化”，每步都能检查，确保不出错。
+ **不好拆**：考虑选 **代理型工作流**，靠模型智能。  
如果任务动态多变（如智能客服需实时理解用户、调用工具），代理型工作流的自主推理和工具调用更适合。Agent 像智能助手，能动态规划路径。  
**何时靠模型？** 如果中间过程难以验证，或拆分后 Workflow 过于复杂、研发成本过高，就该靠模型。可以用现成模型做 Agent，或针对场景做 SFT/RFT 微调，甚至合成数据进行深度训练。  
**例子**：实时故障诊断，需动态查日志、调 API，Agent 能灵活应对。

### 稳定性和可解释性要求高吗？
+ **高**：考虑选 **非代理型工作流**，拆分优先。  
金融、医疗等场景需要高稳定性和可控性，Workflow 的固定步骤能减少模型随机性带来的风险。  
**可解释性需求**：如果业务要求中间结果透明（如展示给用户或支持人工干预），拆分 Workflow 能提取每步输出，方便检查和控制，哪怕这可能牺牲点效果。  
**例子**：医疗数据处理，拆分步骤并展示中间结果，满足监管和用户信任需求。
+ **低**：考虑选 **代理型工作流**，靠模型。  
原型验证或交互式场景（如智能助手）可以接受一定不确定性，Agent 的灵活性更适合快速试错。长期看，无可靠检查点的环节会逐渐融合，靠模型智能解决问题。  
**融合还是训练？** 融合方向上，用现成模型做 Agent 成本低；若场景特殊（如开放性强、现有模型效果差），可考虑微调或自训模型。  
**例子**：实验性对话系统，Agent 直接跑，效果不好再微调。

### 现在做非代理型 Workflow 还是等模型进步？
+ **现在做非代理型 Workflow**：  
如果任务能拆分且有可靠检查点，尽快建 Workflow，验证效果。Workflow 适合快速上线，尤其在新场景验证阶段，研发成本可控。  
**直觉泵**：问自己，“这个 Workflow 半年后会被新模型颠覆吗？” 如果 80% 的工作量会白费，考虑暂停，评估模型发展速度。
+ **等模型或靠 Agent**：  
如果 Workflow 拆分后太复杂，或现有模型效果很差（如开放场景），可以先用 Agent 跑 baseline，观察模型进步。长期看，无检查点的环节会靠模型融合解决。  
**例子**：超复杂任务（如全自动代码生成），现有模型不行，先用 Agent 试，等待更强模型。

> 💡Tips：
> + **混合策略**：复杂任务常结合两者—— Workflow 应对确定性子任务，Agent 管动态决策。
> + **别轻易改 PMF 方案**：已验证有效的方案（Product-Market Fit）无需频繁调整，除非有强需求。技术迭代快，每隔一定周期（如半年）评估一次即可。
> + **非代理型Workflow 不会被淘汰**：它在可拆分、高稳定场景中始终高效，尤其当可解释性和中间验证至关重要时。
>

# 五个主流Agent开发框架
## 开源情况与社区热度
表1：主流 AI Agent 框架社区活跃度对比总览

| 框架名称 | Stars | Commits | Issues | Forks | PR 创建者数 | 主语言 |
| --- | --- | --- | --- | --- | --- | --- |
| **LangGraph** | 11,353 | 9,624 | 646 | 2,022 | 259 | Python |
| **LlamaIndex** | 39,568 | 14,044 | 8,826 | 5,881 | 1,603 | Python |
| **PydanticAI** | 8,218 | 2,303 | 724 | 798 | 159 | Python |
| **AutoGen** | 41,610 | 14,143 | 2,667 | 6,624 | 571 | Python |
| **CrewAI** | 29,091 | 5,245 | 1,290 | 4,129 | 364 | Python |


_表2： 近 28 天主流 AI Agent 框架社区活跃度对比表  _

| 框架名称 | Stars 增长 | PR（Open） | PR（merge） | Issues（Open） | Issues（Closed） |  Commits |
| --- | --- | --- | --- | --- | --- | --- |
| **LangGraph** | 1,018 | 157 | 141 | 49 | 45 | 630 |
| **LlamaIndex** | 657 | 100 | 85 | 85 | 382 | 202 |
| **PydanticAI** | 969 | 99 | 67 | 119 | 102 | 313 |
| **AutoGen** | 1,233 | 103 | 88 | 54 | 65 | 167 |
| **CrewAI** | 1,265 | 113 | 48 | 70 | 69 | 393 |


## 测评总览
**先给结论：**

+ **LangGraph：**如果你要构建**可控性强、状态清晰的复杂代理系统**，如对话机器人、代码分析器，推荐使用 LangGraph。它基于图模型的工作流架构，非常适合需要清晰状态流转、异常恢复、任务回溯的企业级场景。
+ **LlamaIndex：**  
如果你偏向**数据驱动的问答系统或多轮文档处理任务**，如内部知识库问答、企业搜索，LlamaIndex 是优选。  
它的数据感知能力强，擅长处理多模态数据与文档结构，是构建 RAG 应用的成熟方案。
+ **PydanticAI：**  
对于希望**输出结构严谨、安全稳定的 AI 服务**，特别是在后端系统中对接 LLM，PydanticAI 提供类型保障，极其适合。它在输入/输出格式控制上非常精细，适用于需要高可靠性、类型校验的场景，尤其便于集成到 API 或微服务中。
+ **AutoGen：**  
AutoGen 非常适合需要**快速原型、动态协作、多智能体消息交互**的场景，比如研究型对话工具、代码建议器等。它灵活且开箱即用，尤其适合用于探索性项目、创新实验或构建具有对话记忆与推理链的多代理系统。
+ **CrewAI：**  
想要构建**多角色协作、业务流自动化**的系统，如内容团队编排或跨部门流程管理，CrewAI 是实战导向最强的选择之一。它通过角色分工与流程驱动相结合，能够非常自然地映射现实中团队合作的任务分解与执行逻辑。

以下是从技术特性、控制能力、状态持久、可观测性、部署便利性等多个维度，对五大框架的全面评测对比：

| 特性 / 框架 | **LangGraph** | **LlamaIndex** | **PydanticAI** | **AutoGen** | **CrewAI** |
| --- | --- | --- | --- | --- | --- |
| **技术特点** | 有状态图编排框架，支持复杂控制流和多智能体。采用 DAG 架构，节点与边精细定义。支持状态持久化、异常恢复和流式输出。 | 事件驱动的工作流模型，简化数据流传递。支持文档检索与处理，集成丰富工具链。 | 基于 Pydantic，强调类型安全与结构化输出。设计轻量，适合后端集成。 | 多智能体协作框架，基于对话与消息传递。支持异步执行与代码自动生成。 | 专注多角色协作，采用 Crew + Flow 模式，支持并发、缓存和任务委派。 |
| **适用场景** | 面向高可控性、高可观测性的复杂应用，如智能助手、代码生成、业务流程。 | 数据驱动的问答与研究类任务，如知识库检索、问答生成等。 | 强调安全与结构性，适合数据处理、结构生成与后端接口集成。 | 对话、代码编写、研究讨论类任务；适合动态多代理编排场景。 | 工作流自动化、多智能体任务协同，如内容生产、审批流等。 |
| **状态管理** | 内建状态机制，节点间通过 TypedDict 共享状态；支持状态 reducer 和检查点。 | 通过 Context 传递全局上下文，简化状态共享与更新。 | 利用依赖注入传递状态，Agent 输入输出通过 Pydantic 模型定义。 | 状态通过消息共享；由用户管理状态存储或上下文记忆。 | Flow 提供内置状态支持；Crews 可保留上下文，适配多轮任务。 |
| **细粒度控制** | 支持分支、循环、并行、条件跳转等高级流程控制。Send API 实现动态任务调度。 | 支持分支与循环事件；子流程、嵌套流程可组合构建复杂执行图。 | 支持通过 Python 控制流组织任务；并发需手动实现。 | 多 Agent 并行、主题订阅、消息模式，适合非结构化交互。 | 可使用逻辑条件控制分支与同步；支持任务委派和多路径协作。 |
| **异步与并发** | 支持异步执行节点，兼容 asyncio；配合 Ray 可扩展为分布式。 | 完全异步模型，支持 `await`<br/>、事件异步触发和并行 Step。 | 原生支持异步函数与并发执行；异步校验和调用兼容性好。 | 架构原生支持 asyncio；Agent 任务可并发或异步运行。 | 支持异步执行、并发 Flow 步骤，最大限度利用多核资源。 |
| **分布式支持** | 可与 Ray 结合实现分布式部署；企业版内建调度与集群能力。 | 支持与 Ray 配合分布式执行；多节点任务并发需用户管理。 | 无内建分布式；可结合 Celery、FastAPI 等实现横向扩展。 | 支持本地和远程部署，具备多进程、分布式运行机制。 | 企业版支持集群部署与负载均衡；开源版需手动扩展。 |
| **流式输出** | 多种模式：按节点更新、逐 token、结构化结果流；适合前端实时交互。 | 步骤级和 token 级事件流支持，适合 UI 动态反馈。 | 支持边生成边验证，适配 LLM 输出逐步检查的场景。 | 支持逐句/逐 token 输出，方便用户实时查看生成过程。 | 支持任务回调监听，间接实现流式交互。 |
| **持久化机制** | 支持本地和远程数据库持久化（如 Postgres）；线程级/跨线程状态保存。 | 需自行集成向量数据库或缓存系统进行状态保存。 | 无持久层，需开发者管理数据存储。 | 应用层管理持久化，结合外部数据库记录会话等信息。 | 内置 Memory 模块，自动缓存任务状态；支持跨任务上下文。 |
| **可观测性** | 可集成 LangSmith，追踪调用链和 token 消耗；需自行添加监控。 | 支持日志记录和 Verbose 调试，需用户自建监控逻辑。 | 原生集成 Logfire，支持可视化调试与日志追踪。 | 可结合日志系统分析行为，无专用可视化面板。 | 提供控制平面视图，展示每个 Crew 的调用和消耗统计。 |
| **学习曲线** | 图模型与 reducer 机制对初学者略有挑战；文档详实。 | 中等难度，需理解事件流与流程编排；支持可视化分析。 | 易于入门，面向 Python 开发者；强调工程实践。 | 多模块协作较复杂，需理解 Agent 模式与扩展方式。 | 模型清晰但较新；需熟悉 Crew/Flow 机制与生命周期。 |
| **社区活跃度** | 活跃社区，基于 LangChain 生态；多公司已在生产中使用。 | 用户基数大，社区文档丰富；活跃维护与版本更新。 | 新兴框架，依托 Pydantic 社区；增长快速。 | 大型社区支持，文档完善，GitHub 活跃度高。 | Star 数多，文档和课程丰富，企业支持程度高。 |
| **LLM 支持范围** | OpenAI、Anthropic、Mistral、Llama 等主流模型；也支持自定义。 | 支持所有兼容 LangChain 的 LLM，支持自定义工具调用。 | 支持 OpenAI、Claude、Gemini、DeepSeek、Cohere 等。 | 支持主流 API 提供商（OpenAI、Azure OpenAI、HF 等）。 | 可连接任意 API 接口型 LLM，灵活集成。 |
| **框架兼容性** | 高度兼容 LangChain/LangSmith/MemoryStore 等生态组件。 | 可与向量数据库、工具链（llama_hub）配合使用。 | 与 FastAPI、数据库、消息队列等后端服务集成紧密。 | Python/.NET 通用，Studio 可视化接入多平台。 | 与 Python 原生生态兼容，易接入日志、缓存与数据平台。 |
| **DevOps 部署能力** | 可本地部署或使用平台版；支持 Docker/K8s，便于集成 CI/CD。 | 支持容器化部署，无 SaaS 支持；需手动配置生产环境。 | 可快速嵌入服务端；支持 REST 接口暴露与容器化部署。 | Python 包形式部署；Studio UI 支持服务器托管。 | 企业版支持集中管控和云部署；开源版支持脚本自动部署。 |


---

# LangGraph
## 🔗 基本介绍
![langgraph_workflow.png](pictures/langgraph_workflow.png)
LangGraph 是构建在 LangChain 之上的扩展库，旨在增强 LangChain Expression Language（LCEL）的能力，它引入了图结构（如有向无环图 DAG），使得开发者能够更清晰地定义和管理复杂的工作流，包括循环、条件分支和多智能体协作等。虽然 LangGraph 的使用相较于 LCEL 更为复杂，但它提供了更强的流程控制和状态管理能力，适用于构建需要高度可控性和可扩展性的 AI 应用。

+ **状态图建模**：通过节点和边的方式定义应用流程，实现精细的流程控制。
+ **支持循环和条件流程**：可根据状态动态决定执行路径，适应复杂的对话和任务流程。
+ **多代理协作**：协调多个 Chain、Agent、Tool 等共同协作完成任务。
+ **状态持久化**：自动保存和管理状态，支持暂停和恢复执行，便于处理长时间运行的对话。

不同于LangChain 的线性流程，**LangGraph 是专为构建复杂、有状态（stateful）工作流而设计的图结构框架**。

LangGraph 以 **图（Graph）** 的形式组织工作流，具备如下关键特性：

+ **Node（节点）**：代表工作流中的操作步骤，如 LLM 调用、API 请求、工具执行等。
+ **Edge（边）** 与 **Conditional Edge（条件边）**：定义节点间的信息流向。条件边允许开发者基于状态逻辑实现动态分支控制。
+ **State（状态）**：由开发者定义的 TypedDict 对象，记录当前执行图的上下文信息。LangGraph 在每个节点执行后自动更新状态，确保系统具备连续性和上下文感知能力。
+ **循环与反馈机制（Cyclical Graphs）**：图结构支持回环路径，可实现任务重试、结果反馈、状态回溯等高级控制流。

> _官方参考_：[Langraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) 文档，[Langgraph GitHub](about:blank)。
>

## 🔗 框架评测
### 使用说明
#### 📌 简单链式方式：
对于可以轻松、干净地将任务分解为固定子任务的情况，LangGraph可以通过链式方式简单实现：

```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# Define the pipeline state
class PipelineState(TypedDict):
    pdf_path: str
    raw_content: str
    parsed_content: dict
    summarized_content: str
    persist_status: str

# Node: Load PDF
def load_pdf(state: PipelineState):
    """Simulate loading a PDF file."""
    pdf_path = state["pdf_path"]
    return {"raw_content": f"Simulated raw content from {pdf_path}"}

# Node: Parse document
def parse_document(state: PipelineState):
    """Simulate parsing the loaded document."""
    raw_content = state["raw_content"]
    parsed_content = {...}
    return {"parsed_content": parsed_content}

# Node: Summarize text using LLM
def summarize_text(state: PipelineState):
    """Simulate summarizing the parsed content via LLM."""
    parsed_content = state["parsed_content"]
    summarized_text = "Summary: AI applications in various industries."
    return {"summarized_content": summarized_text}

# Node: Persist results into a database
def persist_to_db(state: PipelineState):
    """Simulate writing summarized content to the database."""
    summarized_content = state["summarized_content"]
    return {"persist_status": "success"}

# Build the workflow graph
workflow = StateGraph(PipelineState)

# Add nodes
workflow.add_node("load_pdf", load_pdf)
workflow.add_node("parse_document", parse_document)
workflow.add_node("summarize_text", summarize_text)
workflow.add_node("persist_to_db", persist_to_db)

# Add edges between nodes
workflow.add_edge(START, "load_pdf")
workflow.add_edge("load_pdf", "parse_document")
workflow.add_edge("parse_document", "summarize_text")
workflow.add_edge("summarize_text", "persist_to_db")
workflow.add_edge("persist_to_db", END)

# Compile the graph into a runnable chain
chain = workflow.compile()

# Execute the workflow
if __name__ == "__main__":
    init_state = {"pdf_path": "upload/pdf/ai_for_everyone.pdf"}
    final_state = chain.invoke(init_state)

    print("--- Pipeline Execution Result ---")
    for key, value in final_state.items():
        print(f"{key}: {value}")

# --- Pipeline Execution Result ---
# pdf_path: upload/pdf/ai_for_everyone.pdf
# raw_content: Simulated raw content from upload/pdf/ai_for_everyone.pdf
# parsed_content: {'metadata': {'title': 'AI for Everyone'}, 'text_chunks':{}...}
# summarized_content: Summary: AI applications in various industries.
# persist_status: success

```

### 状态管理（State Management）
#### 📌 LangGraph的一大特点是StateGraph，具备如下关键结构：
+ **Node（节点）**：代表工作流中的操作步骤，如 LLM 调用、API 请求、工具执行等。
+ **Edge（边）** 与 **Conditional Edge（条件边）**：定义节点间的信息流向。条件边允许开发者基于状态逻辑实现动态分支控制。
+ **State（状态）**是由开发者定义的 TypedDict 对象，记录当前执行图的上下文信息，state<font style="color:rgb(25, 27, 31);">会在每一个Node之间传递不同的状态信息。然后每一个节点会根据自己定义的逻辑去更新这个状态信息</font>。可以使用 `TypedDict`、`Pydantic` 模型或 `dataclass` 来定义状态结构。

> 💡 <font style="color:rgba(0, 0, 0, 0.87);">默认情况下，`StateGraph`<font style="color:rgba(0, 0, 0, 0.87);"> 使用单个`state schema` 运行，并且所有节点都应使用该 schema 进行通信。但是，也可以为 </font><font style="color:rgb(54, 70, 78);background-color:rgb(245, 245, 245);">StateGraph </font><font style="color:rgba(0, 0, 0, 0.87);">定义不同的</font>`InputState`和`OutputState`<font style="color:rgb(168, 70, 185);background-color:rgb(245, 245, 245);"> </font><font style="color:rgba(0, 0, 0, 0.87);">schema。</font>
>

#### 📌 State 中的每个 key 都可以有自己独立的 reducer 函数，该函数控制如何应用来自节点的更新。
+ 如果没有明确指定 reducer 函数，则默认对 key 的所有更新都应该覆盖它。比如以下示例通过给 `parsed_chunks` 字段加上 `append_chunks` reducer，每次节点返回新的文本片段时，系统会**自动累积**到当前 State 中，无需每个节点手动管理 merge 逻辑， 保证了**数据处理的一致性**。

```python
class State(TypedDict):
    parsed_chunks: Annotated[list[str], append_chunks]
    metadata: dict

def append_chunks(left, right):
    """Append two lists of parsed text chunks."""
    return left + right

def parse_document(state:State):
    """Mock parsing a document and returning new chunks."""
    new_chunks = ["This is a new paragraph extracted."]
    return {"parsed_chunks": new_chunks, "metadata": {"source": "upload/pdf/ai_for_everyone.pdf"}}

# Build the graph
graph = StateGraph(ExtractState)
graph.add_node("parse_document", parse_document)
graph.add_edge(START, "parse_document")

# Compile the graph
chain = graph.compile()

# Invoke the chain with an initial parsed chunk
initial_state = {"parsed_chunks": ["Introduction to AI..."], "metadata": {}}
result = chain.invoke(initial_state)

# Output
print("Accumulated parsed chunks:")
for idx, chunk in enumerate(result["parsed_chunks"], start=1):
    print(f"{idx}. {chunk}")

# =================================
# Accumulated parsed chunks:
# 1. Introduction to AI...
# 2. This is a new paragraph extracted.
# =================================
```

### 细粒度控制（Control Granularity）
#### 📌 基本使用方式
在基于 **LangGraph** 的流程管理中，我们可以非常灵活地控制节点执行的粒度，LangGraph原生支持并行执行多个节点， 还可以实现**结果聚合**（fan-in）与**条件分支**，以下是一些基本使用方式： 

+ **fan-out**：一个节点执行后，可以并发地启动多个子节点。
+ **fan-in**：子节点全部完成后，统一进入下一个节点。
+ **Reducer**：用于合并多个并发节点对同一 State 字段的更新（如累积列表）。
+ **Conditional Branch**：基于 State 中的条件字段动态决定分支路径。创建循环时，可以包含指定终止条件的条件边。（也可以使用<font style="color:rgb(54, 70, 78);background-color:rgb(245, 245, 245);">Command</font>对象来控制节点路由，此时无需显式增加边）
+ **Loop & Termination**：支持在图中创建循环，通过条件边控制终止，同时可设置 recursion_limit 次数防止无限循环并抛出<font style="color:rgb(54, 70, 78);background-color:rgb(245, 245, 245);">GraphRecursionError</font>。

```python
from langgraph.graph import StateGraph, START, END
from langgraph.errors import GraphRecursionError
from typing import Annotated, Sequence
import operator
from typing_extensions import TypedDict

# Define the State
class State(TypedDict):
    body_chunks: Annotated[list[str], operator.add]
    table_chunks: Annotated[list[str], operator.add]
    language: str
    retry_count: int 

# Define Nodes
def load_pdf(state: State):
    print("Loading PDF...")

def extract_body_chinese(state: State):
    print("Extracting Chinese body text...")
    return {"body_chunks": ["中文段落"]}

def extract_body_english(state: State):
    print("Extracting English body text...")
    return {"body_chunks": ["English paragraph"]}

def extract_table(state: State):
    print("Extracting table of contents...")
    return {"table_chunks": ["目录内容"]}

def merge_results(state: State):
    print(f"Merged Body Chunks: {state['body_chunks']}")
    print(f"Merged Table Chunks: {state['table_chunks']}")

# Branching
def route_body_extraction(state: State) -> Sequence[str]:
    if state["language"] == "zh":
        return ["extract_body_chinese", "extract_table"]
    else:
        return ["extract_body_english", "extract_table"]

# Loop Control
def check_retry(state: State):
    if state["retry_count"] <= 0:
        return END
    else:
        return {"retry_count": state["retry_count"] - 1}

# Build the Graph
builder = StateGraph(State)

# Add nodes
builder.add_node(load_pdf)
builder.add_node(extract_body_chinese)
builder.add_node(extract_body_english)
builder.add_node(extract_table)
builder.add_node(merge_results)

# Add edges
builder.add_edge(START, "load_pdf")
builder.add_conditional_edges("load_pdf", route_body_extraction, ["extract_body_chinese", "extract_body_english", "extract_table"])
builder.add_edge(["extract_body_chinese", "extract_body_english", "extract_table"], "merge_results")
builder.add_conditional_edges("merge_results", lambda state: END if state["retry_count"] <= 0 else "load_pdf", [END, "load_pdf"])

# Compile
graph = builder.compile()

# Run with recursion_limit to avoid infinite loop
try:
    result = graph.invoke(
        {"body_chunks": [], "table_chunks": [], "language": "zh", "retry_count": 2},
        config={"recursion_limit": 5}  
    )
    print(result)
except GraphRecursionError:
    print("Exceeded maximum recursion limit. Returning last known state.")
```

> 💡 注意点： 
>
> 1. 需要考虑**Error Handling**， 节点之间 fan-out 后，如果某个节点异常崩了， 当前框架没有机制处理异常，会导致整个 pipeline 中断。  
> 2. 实际应用可能需要考虑优先级调度。
>

#### 📌 并行执行
**Super-Step概念**

LangGraph 的执行模型基于 **super-step**。一个 super-step 可以被认为是图中的一次迭代，所有并行执行的节点都属于同一个 super-step，而顺序执行的节点则会被分配到不同的 super-step。<font style="color:rgb(51, 65, 85);">这每当图运行时，所有节点都处于一个</font>`inactive`<font style="color:rgb(51, 65, 85);">状态。每当传入边收到新消息（状态）时，该节点变为`active`<font style="color:rgb(51, 65, 85);">，运行函数并进行更新响应。在每个 super-step结束时，每个节点都会</font>`halt`<font style="color:rgb(51, 65, 85);">通过将自己标记为</font>`inactive`<font style="color:rgb(51, 65, 85);">不再有传入消息来投票。当所有节点都`inactive`<font style="color:rgb(51, 65, 85);">且没有消息在传输时，图终止。</font>

+ **并行执行**<font style="color:rgb(25, 27, 31);">：</font>**<font style="color:rgb(25, 27, 31);">当多个节点在同一个 super-step 中执行时，它们会并行运行</font>**<font style="color:rgb(25, 27, 31);">。比如，当节点 </font>`a`<font style="color:rgb(25, 27, 31);"> 之后有两个节点 </font>`b`<font style="color:rgb(25, 27, 31);"> 和 </font>`c`<font style="color:rgb(25, 27, 31);">，它们可以并行执行。</font>
+ **顺序执行**<font style="color:rgb(25, 27, 31);">：</font>**<font style="color:rgb(25, 27, 31);">当一个节点的执行依赖于多个其他节点的完成时，必须等待这些节点的执行结果</font>**<font style="color:rgb(25, 27, 31);">。比如，如果节点 </font>`d`<font style="color:rgb(25, 27, 31);"> 依赖于节点 `b2`<font style="color:rgb(25, 27, 31);"> 和 </font>`c`<font style="color:rgb(25, 27, 31);">，则 </font>`d`<font style="color:rgb(25, 27, 31);"> 会在 </font>`b2`<font style="color:rgb(25, 27, 31);"> 和 </font>`c`<font style="color:rgb(25, 27, 31);"> 都完成之后执行。</font>

<div style="text-align: center;">
  <img src="pictures/workflow_sample.png" alt="Workflow Sample">
</div>

> 💡对于上述情况，`b`、`c`同属一个`super step`，我们需要使用<font style="color:rgba(0, 0, 0, 0.87);"> </font>`add_edge([“b_2”, “c”], “d”)`<font style="color:rgba(0, 0, 0, 0.87);"> 来强制节点 </font>`“d”`<font style="color:rgba(0, 0, 0, 0.87);"> 仅在节点 </font>`“b_2”`<font style="color:rgba(0, 0, 0, 0.87);"> 和 </font>`“c”`<font style="color:rgba(0, 0, 0, 0.87);"> 都完成执行时运行。否则如果分别加两条边，会导致`d`执行两次</font>
>

**Map-Reduce并行**

在实际应用中，我们经常需要：针对一批子任务（如：文本块、文档段落、图片），并行处理，并最终合并结果，比如 对一份大文档的多个部分分别总结（每一块文本 -> summary）， 这种需求天然符合 **Map-Reduce** 模式。然而面临的两个问题是 ：

+ 流程设计时无法提前知道一共多少块文本要处理（数量是动态的） 
+ 每个子节点应该只处理属于自己的 chunk，不能共享整体 State  

对此，LangGraph 提供了 `Send` API，它允许：

+ 在运行时 **动态创建子节点任务**
+ **给每个子任务分发不同的 State**

```python
Send("target_node_name", {"key": value})   
```

其中：

+ `"target_node_name"` 是要发往的节点
+ `{"key": value}` 是新的、子任务特有的输入 State

这样就可以非常灵活地处理 **动态数量 + 独立 State** 的子任务，如下示例所示：

```python
from langgraph.types import Send

# Define the overall state
class OverallState(TypedDict):
    chunks: list[str]
    summaries: Annotated[list[str], operator.add]

# Define the dispatch logic using Send API
def dispatch_chunks(state: OverallState):
    return [Send("summarize_chunk", {"chunk": chunk}) for chunk in state["chunks"]]

# Define the node to summarize a single chunk
def summarize_chunk(state: OverallState):
    return {"summaries": [f"Summary of: {state['chunk'][:10]}..."]}

# Build the graph
builder = StateGraph(OverallState)
builder.add_node("summarize_chunk", summarize_chunk)
builder.add_conditional_edges(START, dispatch_chunks)
builder.add_edge("summarize_chunk", END)
graph = builder.compile()

# Run the graph
output = graph.invoke({"chunks": ["This is the first part.", "This is the second part."]})
print(output)

```

#### 📌 节点重试策略
 LangGraph 引入了节点级的** RetryPolicy **。  <font style="color:rgba(0, 0, 0, 0.87);">可以在调用</font>`add_node`<font style="color:rgba(0, 0, 0, 0.87);">函数时传递 </font>`RetryPolicy`<font style="color:rgba(0, 0, 0, 0.87);"> 对象</font>

```python
from langgraph.pregel import RetryPolicy

RetryPolicy()
RetryPolicy(initial_interval=0.5, backoff_factor=2.0, max_interval=128.0, max_attempts=3, jitter=True, retry_on=<function default_retry_on at 0x78b964b89940>)

# Define a new graph
builder = StateGraph(AgentState)
builder.add_node("model", call_model, retry=RetryPolicy(max_attempts=5))
```

#### 📌 如何在达到递归限制前返回State
在复杂流程中，图（Graph）可能因为循环调用或深度嵌套，意外达到递归限制 (`GraphRecursionError`)。默认情况下，超限直接报错，导致应用体验不佳。为此，LangGraph 引入了 `RemainingSteps` 机制。  

**通过在 **`**State**`** 类型中加上 **`**RemainingSteps**`** 注解，框架会自动为你管理递归深度。LangGraph 会为每次图的执行创建并递减 **`**remaining_steps**`**，它跟踪当前执行到哪一步，以及还需要执行多少次。  **

```python
class State(TypedDict):
    value: str
    action_result: str
    remaining_steps: RemainingSteps
```

### 异步执行（Asynchronously）
<font style="color:rgba(0, 0, 0, 0.87);">在并发运行io绑定代码时（例如，向聊天模型提供商发出并发 API 请求），使用异步方式可以显著提高性能。</font>

要将同步改为异步，只需要：

+ <font style="color:rgba(0, 0, 0, 0.87);">将节点函数从 </font>`def`<font style="color:rgba(0, 0, 0, 0.87);"> 修改为 </font>`async def`<font style="color:rgba(0, 0, 0, 0.87);">；</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">在节点内部正确使用 </font>`await`<font style="color:rgba(0, 0, 0, 0.87);">；</font>

<font style="color:rgba(0, 0, 0, 0.87);">由于许多 LangChain 对象遵循 Runnable 协议，且同步方法通常都有对应的异步版本，因此整体迁移过程通常较为简单。</font>

```python
async def call_model(state: State):
    messages = state["messages"]
    response = await model.ainvoke(messages)
    return {"messages": [response]}
    
from langchain_core.messages import HumanMessage
async def main():
    inputs = {"messages": [HumanMessage(content="what is the keywords in this text")]}
    # Streaming Node Output
    async for output in graph.astream(inputs, stream_mode="updates"):
        # stream_mode="updates" yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print(value["messages"][-1].pretty_print())
```

### 分布式支持
<font style="color:rgb(25, 27, 31);">Langgraph支持将智能体的任务分配到多个计算节点或线程上同时执行。</font>

<font style="color:rgb(25, 27, 31);">以ray为例，和ray集成简单的方式：</font>

+ <font style="color:rgb(25, 27, 31);"></font>**封装StateGraph的Actor类**<font style="color:rgb(25, 27, 31);">。</font>
+ <font style="color:rgb(25, 27, 31);"></font>**用 **`**@ray.remote**`** 注册成Actor**<font style="color:rgb(25, 27, 31);">。</font>
+ <font style="color:rgb(25, 27, 31);"></font>**在主程序（Driver）里，调用 **`**GraphActor.remote()**`** 实例化**<font style="color:rgb(25, 27, 31);">。</font>
+ **Ray在集群里调度worker进程，专门跑这个Actor实例**<font style="color:rgb(25, 27, 31);">。</font>
+ **异步远程调用Actor方法**<font style="color:rgb(25, 27, 31);">，各个Actor</font>**独立、并发、分布式执行**<font style="color:rgb(25, 27, 31);">。</font>

代码示例：

```python
import ray
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
import asyncio

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Define the state type for langgraph
class SimpleState(TypedDict):
    message_list: List[str]

# Node function
def add_message(state: SimpleState):
    state["message_list"].append("New message")
    print(f"Node executed, current message list: {state['message_list']}")
    return state

# Ray Actor class to encapsulate StateGraph
@ray.remote(num_cpus=1)  # Each Actor uses 1 CPU
class GraphActor:
    def __init__(self):
        # Initialize StateGraph and add node
        self.graph = StateGraph(SimpleState)
        self.graph.add_node("add_node", add_message)
        self.graph.set_entry_point("add_node")
        self.compiled_graph = self.graph.compile()

    async def execute(self, initial_state):
        # Execute the compiled graph
        return await self.compiled_graph.ainvoke(initial_state)

# Create and run multiple GraphActor
async def create_and_run_graphs(num_workers=4):
    # Create multiple GraphActors
    graph_actors = [GraphActor.remote() for _ in range(num_workers)]

    # Prepare initial state for each worker
    initial_states = [{"message_list": []} for _ in range(num_workers)]

    # Submit all execution tasks
    exec_tasks = [actor.execute.remote(state) for actor, state in zip(graph_actors, initial_states)]

    # Wait for all tasks to complete
    results = await asyncio.gather(*[asyncio.to_thread(ray.get, task) for task in exec_tasks])

    # Print results for each worker
    for idx, result in enumerate(results):
        print(f"Worker {idx} result: {result['message_list']}")

# Start the test
if __name__ == "__main__":
    asyncio.run(create_and_run_graphs(num_workers=4))  # Change num_workers as needed
    ray.shutdown()


```

### **流式输出（Streaming Output）**
#### 📌不同流式输出模式
流式处理对于提升基于 LLM 构建的应用响应能力至关重要，特别是在减少延迟方面。LangGraph 提供多种流式输出mode，包括：

1. **values**：每步后发出所有状态值。
2. **updates**：仅发出节点名和每步更新内容。
3. **custom**：通过 StreamWriter 自定义数据输出。
4. **messages**：逐个令牌发出 LLM 消息及其元数据。
5. **debug**：发出详细的调试信息。

通过使用 `graph.stream(..., stream_mode=<stream_mode>)` 方法，可以graph执行中流式返回输出。

```python
# sync
for chunk in graph.stream(inputs, stream_mode=["updates", "custom"]):
    print(chunk)
    
# async
async for chunk in graph.astream(inputs, stream_mode=["updates", "custom"]):
    print(chunk)
```

#### 📌 异步流式输出实现原理
`astream` 方法本身返回一个异步迭代器 (`AsyncIterator`)  ，它在graph执行过程中逐步输出数据。`astream` 方法中的关键组件是 `AsyncQueue` 和 `StreamProtocol`，并且会使用 `async for` 和 `asyncio` 库来支持异步流式处理。   

```python
async def astream(
        self,
        input: dict[str, Any] | Any,
        config: RunnableConfig | None = None,
        *,
        stream_mode: StreamMode | list[StreamMode] | None = None,
        output_keys: str | Sequence[str] | None = None,
        interrupt_before: All | Sequence[str] | None = None,
        interrupt_after: All | Sequence[str] | None = None,
        checkpoint_during: bool | None = None,
        debug: bool | None = None,
        subgraphs: bool = False,
    ) -> AsyncIterator[dict[str, Any] | Any]:
```

其中`AsyncQueue` 是一个线程安全的异步队列，它用于存储流数据。`stream_put` 是一个将数据放入队列的异步方法，它通过 `aioloop.call_soon_threadsafe` 来保证数据被异步推送到队列中

```python
stream = AsyncQueue()
aioloop = asyncio.get_running_loop()
stream_put = cast(
    Callable[[StreamChunk], None],
    partial(aioloop.call_soon_threadsafe, stream.put_nowait),
)
```

#### 📌 异步流的核心步骤：
+ 数据会逐步放入 `stream` 队列中。
+ `output()` 函数用于从 `stream` 异步队列逐步获取数据，并通过 `yield` 输出这些数据。
+ `async for` 会异步获取这些结果，直到 `stream` 队列为空。

```python
def output() -> Iterator:
    while True:
        try:
            ns, mode, payload = stream.get_nowait()
        except asyncio.QueueEmpty:
            break
        if subgraphs and isinstance(stream_mode, list):
            yield (ns, mode, payload)
        elif isinstance(stream_mode, list):
            yield (mode, payload)
        elif subgraphs:
            yield (ns, payload)
        else:
            yield payload

```

#### 📌 LLM流式输出：
下面是一个在单个节点中具有两个LLM调用的示例：

```python
from typing import TypedDict
from langgraph.graph import START, StateGraph
from langchain_openai import ChatOpenAI
import asyncio
import os

# Define two model instances with tags for filtering
summary_model = ChatOpenAI(model="gpt-4o-mini", tags=["summary"])
keyword_model = ChatOpenAI(model="gpt-4o-mini", tags=["keyword"])

# Define the state structure
class State(TypedDict):
    text: str
    summary: str
    keywords: str

async def call_model(state, config):
    text = state["text"]
    print("Generating summary...")
    summary_response = await summary_model.ainvoke(
        [{"role": "user", "content": f"Please summarize the following text:\n\n{text}"}],
        config,
    )
    print("\n\nExtracting keywords...")
    keyword_response = await keyword_model.ainvoke(
        [{"role": "user", "content": f"Please extract important keywords from the following text:\n\n{text}"}],
        config,
    )
    return {"summary": summary_response.content, "keywords": keyword_response.content}

graph = StateGraph(State).add_node(call_model).add_edge(START, "call_model").compile()

async def main():
    input_text = (
        "Artificial intelligence (AI) is the simulation of human intelligence processes "
        "by machines, especially computer systems. Specific applications of AI include "
        "expert systems, natural language processing, speech recognition, and machine vision."
    )
    async for msg, metadata in graph.astream(
        {"text": input_text},
        stream_mode="messages",
    ):
        if msg.content:
            print(msg.content, end="|", flush=True)
        #  We can use the streamed metadata and filter events using the tags we've added to the LLMs previously
        # if msg.content and "summary" in metadata.get("tags", []):
        #     print(msg.content, end="|", flush=True)

if __name__ == "__main__":
    asyncio.run(main())

############ Result #############
# Generating summary...
# Art|ificial| intelligence| (AI) involves| machines simulating human| intelligence processes. Key| applications of AI include| expert systems, natural| language processing, speech| recognition, and machine| vision.|

# Extracting keywords...
# Here| are| the| important keywords extracted from| the text:

# -| Artificial intelligence (AI|)  
# - Simulation|  
# - Human intelligence|
# ...

```

### 持久化（Persistence）
#### 📌 线程级持久化
<font style="color:rgba(0, 0, 0, 0.87);">许</font><font style="color:rgba(0, 0, 0, 0.87);">多 AI 应用程序需要内存才能在多个交互之间共享上下文。在 LangGraph 中，可以使用线程级持久化将这种内存添加到任何StateGraph 中，可以通过在编译 Graph 时添加</font>`checkpointer`<font style="color:rgba(0, 0, 0, 0.87);">来设置它以保持其状态。</font>

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

builder = StateGraph(MessagesState)
builder.add_node("call_model", call_model)
builder.add_edge(START, "call_model")
# Enable memory saving during execution
graph = builder.compile(checkpointer=memory)  

input_message = {"role": "user", "content": "hi! I'm Alen"}

# Stream the response with memory saving
for chunk in graph.stream({"messages": [input_message]}, {"configurable": {"thread_id": "1"}}, stream_mode="values"):
    chunk["messages"][-1].pretty_print()

# Send another message in the same thread, using memory to preserve the conversation context
input_message = {"role": "user", "content": "what's my name?"}
for chunk in graph.stream({"messages": [input_message]}, {"configurable": {"thread_id": "1"}}, stream_mode="values"):
    chunk["messages"][-1].pretty_print()

# Send a message in a new thread, demonstrating memory usage across threads
input_message = {"role": "user", "content": "what's my name?"}
for chunk in graph.stream(
    {"messages": [input_message]},
    {"configurable": {"thread_id": "2"}},  # New thread
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()
    
# ================================ Human Message =================================
# hi! I'm Alen
# ================================== Ai Message ==================================
# Hi Alen! Nice to meet you. How can I assist you today? 😊
# ================================ Human Message =================================
# what's my name?
# ================================== Ai Message ==================================
# Your name is **Alen**! 😊 Did I get it right?
# ================================ Human Message =================================
# what's my name?
# ================================== Ai Message ==================================
# I don't have access to specific personal information about you, so I don't know your name. 😊


```

#### 📌 跨线程持久化
<font style="color:rgba(0, 0, 0, 0.87);">当然LangGraph 还支持跨</font>**<font style="color:rgba(0, 0, 0, 0.87);">多个线程</font>**<font style="color:rgba(0, 0, 0, 0.87);">持久保存数据。核心是使用</font>`Store`<font style="color:rgba(0, 0, 0, 0.87);"> 接口存储跨线程共享数据（如用户偏好）。</font>`namespace`（如 </font>`("memories", user_id)`<font style="color:rgba(0, 0, 0, 0.87);">）隔离不同用户的记忆。</font>

#### 📌 使用Postgres checkpointer持久化
```python
from langgraph.graph import StateGraph

builder = StateGraph(....)
# ... define the graph
checkpointer = # postgres checkpointer 
graph = builder.compile(checkpointer=checkpointer)
```

> 💡<font style="color:rgba(0, 0, 0, 0.87);"> 需要在 checkpointer 上运行一次 </font>`.setup()`<font style="color:rgba(0, 0, 0, 0.87);"> 来初始化数据库，然后才能使用。</font>
>

**同步连接（****<font style="color:rgba(0, 0, 0, 0.87);">sync connection</font>****）**

<font style="color:rgba(0, 0, 0, 0.87);">同步连接以阻塞方式执行作，这意味着每个operation都会等待完成，然后再移动到下一个operation，以下展示了三种常见的方式：</font>

+ <font style="color:rgba(0, 0, 0, 0.87);">With a connection</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">With a connection pool</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">With a connection string</font>

```python
from langgraph.prebuilt import create_react_agent
from psycopg_pool import ConnectionPool
from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"
connection_kwargs = {
    "autocommit": True,
    "prepare_threshold": 0,
}

# =============With a connection ==============
with Connection.connect(DB_URI, **connection_kwargs) as conn:
    checkpointer = PostgresSaver(conn)
    checkpointer.setup()
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "2"}}
    res = graph.invoke({"messages": [("human", "what's the language of this paper")]}, config)

    checkpoint_tuple = checkpointer.get_tuple(config)

# ===========With a connection pool============
with ConnectionPool(
    # Example configuration
    conninfo=DB_URI,
    max_size=20,
    kwargs=connection_kwargs,
) as pool:
    checkpointer = PostgresSaver(pool)
    checkpointer.setup()
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "1"}}
    res = graph.invoke({"messages": [("human", "what's the language of this paper")]}, config)
    checkpoint = checkpointer.get(config)

# ===========With a connection string============
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "3"}}
    res = graph.invoke({"messages": [("human", "what's the language of this paper")]}, config)

    checkpoint_tuples = list(checkpointer.list(config))
```

**异步连接（a****<font style="color:rgba(0, 0, 0, 0.87);">sync connection</font>****）**

<font style="color:rgba(0, 0, 0, 0.87);">异步连接允许非阻塞数据库作。也就是说应用程序的其他部分可以在等待数据库操作完成时继续运行。适合高并发场景或处理 I/O 绑定操作时特别有用。</font>

```python
from psycopg import AsyncConnection

async with await AsyncConnection.connect(DB_URI, **connection_kwargs) as conn:
    checkpointer = AsyncPostgresSaver(conn)
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "5"}}
    res = await graph.ainvoke(
        {"messages": [("human", "what's the weather in nyc")]}, config
    )
    checkpoint_tuple = await checkpointer.aget_tuple(config)
```

### 日志与可观测性（Logging & Monitoring）
<font style="color:rgb(50, 56, 62);"> LangSmith 专门用来</font>**监控和调试 LLM 应用**<font style="color:rgb(50, 56, 62);">，能实时跟踪工作流、模型表现，并且 LangSmith 提供了</font>**针对大模型原生优化的可观测性功能**<font style="color:rgb(50, 56, 62);">，从开发、测试到上线 ，非常适合生产环境。 LangSmith本身</font>与框架无关 — 它可以与 langchain 和 langgraph 一起使用，也可以单独使用。对于LangGraph，我们可以集成LangSmith实现<font style="color:rgb(50, 56, 62);">生成对整个pipline的跟踪，方便调试与监看。</font>

---

# LlamaIndex
## 基本介绍
LlamaIndex 是一个用于LLM 应用程序的数据框架，用于注入，结构化，并访问私有或特定领域数据，专门为大语言模型（LLM）提供外部数据接入的能力。

相比传统使用**有向无环图（DAG）方式组织流程的框架，LlamaIndex提出了更自然、更具表达力的Workflow机制**，解决了复杂AI流程中循环（loops）、分支（branches）和动态数据传递的问题。其主要优势包括：

+ **更直观的控制流**：循环与分支作为一等公民存在于Workflow中，不再需要隐晦地通过边（edges）来模拟，大幅提升可读性与维护性。
+ **简化数据流管理**：节点之间的数据传递机制更加清晰，减少了在DAG中常见的默认值、可选参数、数据对齐等繁杂处理。
+ **开发体验自然**：符合开发者在构建复杂、动态AI应用（如Agent系统、交互式推理链）时的思考方式，无需对齐底层图结构。

> _官方参考_：[LlamaIndex文档](about:blank)，[LlamaIndex GitHub](https://github.com/run-llama/llama_index)。
>

## 框架评测
### 使用说明
在 **LlamaIndex** 框架中，工作流（`Workflow`）由多个步骤（`step`）组成。每个步骤接受一个或多个 **事件（Event）**，并生成一个新的事件。工作流通常会由一个特殊的 **StartEvent** 触发，并由 **StopEvent** 结束。

#### 📌 核心概念：
1. `**StartEvent**`: 启动工作流的事件，通常作为第一个步骤的输入。
2. `**StopEvent**`: 结束工作流的事件，它会结束工作流并返回最终结果。
3. `**Event**`: 所有事件（包括 StartEvent 和 StopEvent）都需要继承自 `Event` 类。用户可以定义自定义的事件来在步骤之间传递数据。

#### 📌 步骤（Step）定义：
+ `**@step**` 装饰器：用于标记一个方法为工作流中的步骤（step）。
+ 每个步骤接受一个事件作为输入，并返回一个事件作为输出。

#### 📌 工作流执行：
1. 创建工作流实例。
2. 调用 `run()` 方法，启动工作流并传入初始事件。
3. 步骤依次执行，每个步骤基于前一个步骤的输出生成新的事件。
4. <font style="color:rgba(0, 0, 0, 0.87);">默认情况下，工作流程是异步的，因此可以使用 </font>`await`<font style="color:rgba(0, 0, 0, 0.87);"> 来获取 </font>`run`<font style="color:rgba(0, 0, 0, 0.87);"> 命令的结果</font>

```python
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
)
import asyncio

# 定义事件类
class PDFLoadedEvent(Event):
    pdf_content: str

class ParsedTextEvent(Event):
    parsed_text: str

class SummarizedTextEvent(Event):
    summary: str

class DatabaseStoredEvent(Event):
    result: str

# 创建工作流
class MyWorkflow(Workflow):
    @step
    async def start_step(self, ev: StartEvent) -> PDFLoadedEvent:
        print("Starting the workflow...")
        return PDFLoadedEvent(pdf_content="Loaded PDF content here.")

    @step
    async def pdf_parser_step(self, ev: PDFLoadedEvent) -> ParsedTextEvent:
        print(f"Parsing PDF content: {ev.pdf_content}")
        return ParsedTextEvent(parsed_text="Parsed text from the PDF.")

    @step
    async def text_summary_step(self, ev: ParsedTextEvent) -> SummarizedTextEvent:
        print(f"Summarizing parsed text: {ev.parsed_text}")
        return SummarizedTextEvent(summary="Summary of the parsed text.")

    @step
    async def database_persistence_step(self, ev: SummarizedTextEvent) -> DatabaseStoredEvent:
        print(f"Storing summarized text in database: {ev.summary}")
        return DatabaseStoredEvent(result="Text stored in PostgreSQL database.")

    @step
    async def end_step(self, ev: DatabaseStoredEvent) -> StopEvent:
        print(f"Final result: {ev.result}")
        return StopEvent(result="Workflow complete.")

async def main():
    w = MyWorkflow(timeout=10, verbose=False)
    result = await w.run(first_input="Start the workflow.")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

```

#### 📌<font style="color:rgba(0, 0, 0, 0.87);"> 内置的可视化工具</font>
LlamaIndex的一大特色是内置了可视化工具，可以用下面这种方式生成html查看

```python
from llama_index.utils.workflow import draw_all_possible_flows
    draw_all_possible_flows(MyWorkflow, filename="multi_step_workflow.html")
```

![](pictures/llamaindex_wf.png)

### 状态管理（State Management）
Demo示例中使用的都是自定义事件的属性逐步传递数据，这种链式传输方式存在问题就是不够灵活，例如我们难以**跨节点传递数据**，缺少一个全局的上下文状态管理方式。因此，LlamaIndex引入了`Context`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">类型的参数来补充这一点，示例如下：</font>

```python
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
    Context,
)
```

<font style="color:rgba(0, 0, 0, 0.87);">现在，我们定义一个 </font>`start`<font style="color:rgba(0, 0, 0, 0.87);"> 事件，用于检查数据是否已加载到上下文中。否则，它将返回一个 </font>`SetupEvent`<font style="color:rgba(0, 0, 0, 0.87);">，该事件触发加载数据并循环回到 </font>`start`<font style="color:rgba(0, 0, 0, 0.87);"> 的 </font>`setup`<font style="color:rgba(0, 0, 0, 0.87);">。</font>

```python
class SetupEvent(Event):
    query: str


class StepTwoEvent(Event):
    query: str


class StatefulFlow(Workflow):
    @step
    async def start(
        self, ctx: Context, ev: StartEvent
    ) -> SetupEvent | StepTwoEvent:
        db = await ctx.get("some_database", default=None)
        if db is None:
            print("Need to load data")
            return SetupEvent(query=ev.query)

        # do something with the query
        return StepTwoEvent(query=ev.query)

    @step
    async def setup(self, ctx: Context, ev: SetupEvent) -> StartEvent:
        # load data
        await ctx.set("some_database", [1, 2, 3])
        return StartEvent(query=ev.query)
```

<font style="color:rgba(0, 0, 0, 0.87);">然后在 </font>`step_two`<font style="color:rgba(0, 0, 0, 0.87);"> 中，我们可以直接从上下文访问数据，而无需显式传递数据。</font>

```python
@step
async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StopEvent:
    # do something with the data
    print("Data is ", await ctx.get("some_database"))

    return StopEvent(result=await ctx.get("some_database"))

w = StatefulFlow(timeout=10, verbose=False)
result = await w.run(query="Some query")
print(result)
```

### 细粒度控制（Control Granularity）
#### 📌 分支（branch）
如下所示，我们新建了两个事件类型，`Start`<font style="color:rgba(0, 0, 0, 0.87);"> 随机决定采用一个分支或另一个分支，然后每个分支中的多个步骤完成工作流。</font>

> 💡 <font style="color:rgba(0, 0, 0, 0.87);">支持按任何 Order 组合分支和循环来满足不同业务应用需求。还可以 </font>`send_event`<font style="color:rgba(0, 0, 0, 0.87);"> 并行运行多个分支，并使用 </font>`collect_events`<font style="color:rgba(0, 0, 0, 0.87);"> 同步它们</font>
>

```python
class BranchA1Event(Event):
    payload: str
    
class BranchB1Event(Event):
    payload: str
    
class BranchWorkflow(Workflow):
    @step
    async def start(self, ev: StartEvent) -> BranchA1Event | BranchB1Event:
        if random.randint(0, 1) == 0:
            print("Go to branch A")
            return BranchA1Event(payload="Branch A")
        else:
            print("Go to branch B")
            return BranchB1Event(payload="Branch B")
```

#### 📌 循环（loop）
<font style="color:rgba(0, 0, 0, 0.87);">要创建循环，我们将采用上一教程中的示例 </font>`MyWorkflow`<font style="color:rgba(0, 0, 0, 0.87);"> 并添加一个新的自定义事件类型。我们将其命名为 </font>`LoopEvent`<font style="color:rgba(0, 0, 0, 0.87);">，但同样，它可以具有任意名称。</font>

```python
class LoopEvent(Event):
    loop_output: str

@step
async def text_summary_step(self, ev: ParsedTextEvent | LoopEvent) -> SummarizedTextEvent | LoopEvent:
    if random.randint(0, 1) == 0:
        print("fail")
        return LoopEvent(loop_output="Back to step one.")
    else:
        print(f"Summarizing parsed text: {ev.parsed_text}")
        return SummarizedTextEvent(summary="Summary of the parsed text.")
```

![](pictures/loop.png)

####  📌子类化工作流（Subclassing）  
可以向像普通 Python 类一样，通过继承（`class NewWorkflow(BaseWorkflow)`）来扩展或重定义已有工作流中的步骤 (`@step` 修饰的方法)。  

+ 子类中可以重写父类的某个步骤（方法名相同，事件类型可变化）。
+ 也可以在子类中添加新的步骤。
+ 步骤的执行顺序是根据事件传递链（事件类型）而不是方法顺序决定的。

```python
class CustomWorkflow(MainWorkflow):
    @step
    async def step_two(self, ev: Step2Event) -> Step2BEvent:
        print("Sending an email")
        return Step2BEvent(query=ev.query)

    @step
    async def step_two_b(self, ev: Step2BEvent) -> Step3Event:
        print("Also sending a text message")
        return Step3Event(query=ev.query)
```

+  这里，子类 **重写**了 `step_two`，并且**新增**了 `step_two_b`，扩展了处理流程。  

####  📌工作流嵌套
 在主工作流中，预留一个或多个 **子工作流插槽（Workflow Slot）**，在运行时动态传入完整的子工作流实例。  

+ 在主工作流的步骤方法中，接收一个 `Workflow` 类型的参数（如 `reflection_workflow`）。
+ 使用 `.run()` 启动子工作流，子工作流自己处理内部逻辑。
+ 可通过 `add_workflows(reflection_workflow=YourSubWorkflow())` 注入子流程。
+ 也可以为子工作流参数设置一个**默认子流程**，使主流程可以单独运行。

示例： 定义一个有子流程插槽的主工作流和一个子工作流

```python
class MainWorkflow(Workflow):
    @step
    async def start(self, ctx: Context, ev: StartEvent, reflection_workflow: Workflow = DefaultSubflow()) -> Step2Event:
        print("Need to run reflection")
        res = await reflection_workflow.run(query=ev.query)
        return Step2Event(query=res)

class ReflectionFlow(Workflow):
    @step
    async def sub_start(self, ctx: Context, ev: StartEvent) -> StopEvent:
        print("Doing custom reflection")
        return StopEvent(result="Improved query")
```

 运行时替换默认子工作流：  

```python
w = MainWorkflow(timeout=10, verbose=False)
w.add_workflows(reflection_workflow=ReflectionFlow())
result = await w.run(query="Initial query")
```



### 异步并发
在工作流中并发执行步骤可以显著提高效率，特别是当步骤彼此独立且执行时间较长时。通过发出多个事件，工作流可以并行执行多个任务，减少整体执行时间。  

#### 📌 **发出多个事件**
```python
class ParallelFlow(Workflow):
    @step
    async def start(self, ctx: Context, ev: StartEvent) -> StepTwoEvent:
        # 发送多个事件，启动多个独立的任务
        ctx.send_event(StepTwoEvent(query="Query 1"))
        ctx.send_event(StepTwoEvent(query="Query 2"))
        ctx.send_event(StepTwoEvent(query="Query 3"))

    @step(num_workers=4)
    async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StopEvent:
        print("Running slow query ", ev.query)
        await asyncio.sleep(random.randint(1, 5))  # 模拟耗时操作
        return StopEvent(result=ev.query)

```

+ 在 `start` 步骤中，三个查询被并行发送。
+ `step_two` 步骤通过设置 `num_workers=4`，指示最多4个并发实例同时执行，即使有多个查询。

#### 📌 **收集事件**
如果我们需要等待所有并行任务完成后再执行下一步。在这种情况下可以使用 `collect_events` 方法来等待多个事件完成。`collect_events` 会等待指定类型的所有事件，直到收到足够数量的事件后才继续执行。  

```python
class ConcurrentFlow(Workflow):
    @step
    async def start(self, ctx: Context, ev: StartEvent) -> StepTwoEvent:
        # 发出多个事件，启动多个独立的任务
        ctx.send_event(StepTwoEvent(query="Query 1"))
        ctx.send_event(StepTwoEvent(query="Query 2"))
        ctx.send_event(StepTwoEvent(query="Query 3"))

    @step(num_workers=4)
    async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StepThreeEvent:
        print("Running query ", ev.query)
        await asyncio.sleep(random.randint(1, 3))  # 模拟耗时操作
        return StepThreeEvent(result=ev.query)

    @step
    async def step_three(self, ctx: Context, ev: StepThreeEvent) -> StopEvent:
        # 等待所有3个事件
        result = ctx.collect_events(ev, [StepThreeEvent] * 3)
        if result is None:
            return None  # 如果事件不完整，则返回

        # 收集到所有结果后，执行后续操作
        print(result)
        return StopEvent(result="Done")

```

> 💡`collect_events` 返回一个按接收顺序排列的事件列表。  
>

#### 📌 等待多种类型的事件
可以通过 `collect_events` 方法等待事件类型的组合，并按接收到事件的顺序继续处理。  

```python
    @step
    async def step_three(
        self,
        ctx: Context,
        ev: StepACompleteEvent | StepBCompleteEvent | StepCCompleteEvent,
    ) -> StopEvent:
        print("Received event ", ev.result)

        # 等待三种类型的事件
        if (
            ctx.collect_events(
                ev,
                [StepCCompleteEvent, StepACompleteEvent, StepBCompleteEvent],
            )
            is None
        ):
            return None  # 如果事件不完整，则返回

        # 收集到所有事件后，执行后续操作
        return StopEvent(result="Done")
```

### 分布式支持（<font style="color:rgb(32, 33, 34);">Distributed Support</font>）
+ LlamaIndex本身基于异步事件驱动，适合单机并发，但需要外部框架（如 Ray）实现分布式执行。
+ 支持分布式数据摄取、索引和查询，可以通过分片和并行化处理大规模任务。
+ LlamaIndex 官方支持与 Ray 的集成，通过 @ray.remote、Ray Datasets 和 Ray Serve 实现 Workflow 的分布式运行。
+ 适用于并行数据处理、索引构建和高并发查询，适合生产级 RAG 应用。

**集成ray示例：**

```python
import ray
from llama_index.core.workflow import Workflow, step, StartEvent, StopEvent
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader

# 初始化 Ray
ray.init()

# 定义分布式 Workflow
@ray.remote
class DistributedWorkflow(Workflow):
    @step
    async def ingest_data(self, ev: StartEvent) -> None:
        # 并行加载文档
        documents = SimpleDirectoryReader("data_directory").load_data()
        index = VectorStoreIndex.from_documents(documents)
        return {"index": index}

    @step
    async def query_step(self, ev: dict) -> StopEvent:
        index = ev["index"]
        query_engine = index.as_query_engine()
        result = query_engine.query("What is the main topic?")
        return StopEvent(result=str(result))

# 运行分布式 Workflow
workflow = DistributedWorkflow.remote()
result = ray.get(workflow.run.remote())
print(result)
```

### **流式输出（Streaming Output）**
LlamaIndex支持通过 `ctx.write_event_to_stream()` 方法将事件写入流中，这样用户就能实时看到进度。  这里我们先使用 `Workflow` 类来定义工作流，并在每个步骤中定义事件流的输出。  

```python
from llama_index.utils.workflow import draw_all_possible_flows

...

class MyWorkflow(Workflow):
    @step
    async def step_one(self, ctx: Context, ev: StartEvent) -> FirstEvent:
        ctx.write_event_to_stream(ProgressEvent(msg="Step one is happening"))
        return FirstEvent(first_output="First step complete.")

    @step
    async def step_two(self, ctx: Context, ev: FirstEvent) -> SecondEvent:
        llm = OpenAI(model="gpt-4o-mini")
        generator = await llm.astream_complete(
            "Please give me the first 3 paragraphs of Moby Dick, a book in the public domain."
        )
        async for response in generator:
            # 每次接收到响应块时发送进度事件
            ctx.write_event_to_stream(ProgressEvent(msg=response.delta))
        return SecondEvent(
            second_output="Second step complete, full response attached",
            response=str(response),
        )

    @step
    async def step_three(self, ctx: Context, ev: SecondEvent) -> StopEvent:
        ctx.write_event_to_stream(ProgressEvent(msg="Step three is happening"))
        return StopEvent(result="Workflow complete.")

```

+ 在 `step_one` 和 `step_three` 中，直接写入了进度事件。
+ 在 `step_two` 中，我们使用 `OpenAI` 生成器异步获取 LLM 响应，并为每个响应块发送进度事件。

然后我们需要异步运行工作流，并通过 `stream_events()` 方法监听事件。`stream_events()` 会返回每个流式事件，直到工作流执行完毕。  

```python
async def main():
    w = MyWorkflow(timeout=30, verbose=True)
    handler = w.run(first_input="Start the workflow.")

    async for ev in handler.stream_events():
        if isinstance(ev, ProgressEvent):
            print(ev.msg)  # 输出实时进度信息

    final_result = await handler
    print("Final result", final_result)

```

### 持久化（Persistence）
默认情况下，LlamaIndex 的数据存在**内存中**，**需要显式调用**才能将其持久化到磁盘或其他后端。

在 LlamaIndex 中，**存储层**是高度模块化、可插拔的，主要支持以下几种数据类型的存储：

| 类型 | 说明 |
| --- | --- |
| 文档存储（Document Store） | 存储摄取后的文档（Node 对象） |
| 索引存储（Index Store） | 存储索引结构及元数据 |
| 向量存储（Vector Store） | 存储嵌入后的向量 |
| 知识图谱存储（Property Graph Store） | 存储属性图数据（用于知识图谱索引） |
| 聊天记录存储（Chat Store） | 存储聊天消息和对话历史 |


文档、索引存储都基于统一的**Key-Value存储抽象层**。

#### 📌 本地持久化
```python
storage_context.persist(persist_dir="<persist_dir>")
```

+ `<persist_dir>`：指定持久化的目录，默认是 `./storage`。
+ 可以在同一目录下保存**多个索引**，但需要管理好各自的 `index_id`。
+ 本地持久化适合开发阶段、单机应用、简单部署。

注意：如果你自定义了远程存储（如 MongoDB），调用 `persist()` 可能**不需要或无效**，具体取决于存储后端实现。

#### 📌 加载（Loading）
加载持久化的数据，本质是**重建 **`**StorageContext**`，然后**用辅助函数加载索引或图结构**。

典型流程：

+ **重建 **`**StorageContext**`**：**

```python
from llama_index.core import StorageContext
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.vector_stores import SimpleVectorStore

storage_context = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="<persist_dir>"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="<persist_dir>"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="<persist_dir>"),
)
```

+ **加载对象（单个索引 / 多个索引 / 图结构）：**

```python
from llama_index.core import (
load_index_from_storage,
load_indices_from_storage,
load_graph_from_storage,
)

# 加载单个索引（指定 index_id）
index = load_index_from_storage(storage_context, index_id="<index_id>")

# 加载所有索引
indices = load_indices_from_storage(storage_context)

# 加载知识图（指定 root_id）
graph = load_graph_from_storage(storage_context, root_id="<root_id>")
```

> 特别注意：
>
> + 如果同一目录下只有一个索引，可以不指定 `index_id`；
> + 如果有多个索引，**必须指定**要加载的 `index_id`。
>

####  📌 使用远程后端（如 S3/R2）  
### 可观测性（Monitoring）
####  📌 可视化工作流结构（全局视角）  
**目的**：查看 **所有可能的步骤流转路径**，帮助理解和设计流程。  .

+ 输出成 HTML，可在浏览器交互式查看。
+ **针对类（Workflow Class）**，而不是实例。

```python
from llama_index.utils.workflow import draw_all_possible_flows

draw_all_possible_flows(MyWorkflow, filename="workflow.html")
```

#### 📌 Verbose 模式（详细日志）  
**目的**：实时观察每个步骤的运行情况、事件流转。

```python
w = MyWorkflow(timeout=10, verbose=True)
result = await w.run()
```

会打印每个步骤：

+ **执行中**
+ **是否产生事件**
+ **事件类型**

#### 📌 逐步执行（Stepwise Execution）  
**目的**：**手动推进每一步**，细粒度控制调试，适合复杂并发或分支流程  

```python
w = MyWorkflow(timeout=10, verbose=True)
handler = w.run(stepwise=True)

while produced_events := await handler.run_step():
    for ev in produced_events:
        handler.ctx.send_event(ev)

result = await handler
```

+ 每调用一次 `run_step()`，推进一小步。
+ 需要**手动发送**新产生的事件继续驱动后续步骤。

#### 📌 检查点（Checkpoints）  
**目的**：**保存并恢复**中间执行状态，避免重复从头运行。

**用法**：

```python

from llama_index.core.workflow.checkpointer import WorkflowCheckpointer

w = MyWorkflow()
w_ckptr = WorkflowCheckpointer(workflow=w)

handler = w_ckptr.run()
await handler

# 查看产生的所有检查点
w_ckptr.checkpoints[handler.run_id]

# 从某个检查点继续运行
ckpt = w_ckptr.checkpoints[handler.run_id][0]
handler = w_ckptr.run_from(checkpoint=ckpt)
await handler
```

+ 每步都会记录一个检查点。
+ 可以**快速复现特定状态**，加速开发调试循环。

#### 📌 第三方可观测性工具  
+ 比如接入 **Arize** 等外部平台进行高级监控和可视化。
+ 目前官方原生主要支持的是 LlamaIndex 自己的一套方法。

---

# Pydantic AI
## 基本介绍
Pydantic AI来自于著名的Pydantic库开发者，是一个将Pydantic与LLM集成的Agents开发框架。其独特之处在于专注于在AI应用中利用Pydantic的**类型验证、序列化与结构化输出**等功能。Pydantic AI的特点是**天然的结构化输出与强类型验证**，且简洁易用，与其他框架也有良好的集成，可以结合使用。

> _官方参考_：[PydanticAI文档](https://ai.pydantic.dev/)，[PydanticAI GitHub](https://github.com/pydantic/pydantic-ai)。
>

## 框架评测
### 使用说明
#### 📌 代理（agent）
 PydanticAI 的代理（Agent）模块是其核心组件，旨在提供一种结构化、类型安全且高度可扩展的方式，以构建与大型语言模型（LLM）交互的 AI 应用。  

一个代理实例可视为以下元素的组合：

+ **系统提示（System Prompt）**：开发者定义的指令集，引导 LLM 的行为。
+ **函数工具（Function Tools）**：LLM 在生成响应时可调用的函数，用于获取信息或执行操作。
+ **结构化结果类型（Structured Result Type）**：指定 LLM 运行结束时必须返回的结构化数据类型。
+ **依赖类型约束（Dependency Type Constraint）**：系统提示函数、工具和结果验证器在运行时可使用的依赖项。
+ **LLM 模型（LLM Model）**：与代理关联的默认 LLM 模型，也可在运行时指定。
+ **模型设置（Model Settings）**：用于微调请求的可选默认模型设置，也可在运行时指定。

> 💡 在类型术语中，代理在其依赖类型和结果类型方面是通用的，例如，一个代理需要 `Foobar` 类型的依赖项并返回 `list[str]` 类型的结果，则其类型为 `Agent[Foobar, list[str]]`。
>

PydanticAI 提供了多种运行代理的方法，以适应不同的使用场景：

1. **异步运行**：`agent.run()` 返回一个协程，适用于异步环境。
2. **同步运行**：`agent.run_sync()` 是一个同步函数，适用于同步环境。
3. **流式运行**：`agent.run_stream()` 返回一个异步可迭代对象，支持流式响应。
4. **迭代运行**：`agent.iter()` 返回一个上下文管理器，允许手动控制代理的运行过程。

#### 📌 功能工具（Function Tools）
 PydanticAI 的功能工具（Function Tools）机制允许代理在运行时调用外部函数，以获取额外信息或执行特定任务，从而增强模型的响应能力。  

**注册方式**：

+ 使用 `@agent.tool` 装饰器注册需要访问代理上下文的工具。
+ 使用 `@agent.tool_plain` 装饰器注册不需要访问代理上下文的工具。
+ 通过 `Agent` 构造函数的 `tools` 参数注册工具函数或 `Tool` 实例

** 动态功能工具  **

PydanticAI 支持动态功能工具，即工具的定义可以在运行时根据上下文进行修改或决定是否包含。这通过为工具定义一个 `prepare` 函数实现，该函数在每次运行时被调用，以自定义工具的行为或决定是否注册该工具

```python
# 定义 prepare 函数
async def only_if_42(ctx: RunContext[int], tool_def: ToolDefinition) -> Union[ToolDefinition, None]:
    if ctx.deps == 42:
        return tool_def

# 定义工具并注册 prepare 函数
@agent.tool(prepare=only_if_42)
def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f'{ctx.deps} {answer}'

# 运行代理
result = agent.run_sync('testing...', deps=41)
print(result.data)  # 工具未注册
result = agent.run_sync('testing...', deps=42)
print(result.data)  # 工具被注册并调用
```

** 工具与结构化结果的关系  **

工具的参数和返回值可以定义为 Pydantic 模型，从而确保数据的结构化和类型安全。此外，PydanticAI 能够从函数的文档字符串中提取参数描述，自动生成工具的 JSON 模式，增强模型对工具的理解。

#### 📌 结果验证
PydanticAI 的结果模块（`pydantic_ai.result`）提供了结构化的方式来处理代理（Agent）执行后的输出，确保生成的响应符合预期的格式和类型。

+ **结果类型（Result Type）**：定义代理期望的输出格式。可以是简单的 `str` 类型，也可以是复杂的 Pydantic 模型。
+ **结果封装类**：
+ `AgentRunResult`: 用于同步运行的结果封装。
+ `StreamedRunResult`: 用于流式处理的结果封装。
+ **结构化响应**：当结果类型为 Pydantic 模型时，PydanticAI 会自动生成相应的 JSON 模式，并验证模型返回的数据，确保类型安全和结构一致性。

#### 📌 依赖注入
PydanticAI提供了一个独特的依赖关系注入系统，用于向代理系统、提示、工具和结果验证器提供数据和服务，这对于测试特别有用。

+ **定义依赖项**：依赖项可以是任何 Python 类型，通常使用数据类（`@dataclass`）来封装多个依赖对象，如 API 密钥和 HTTP 客户端。

```python
from dataclasses import dataclass
import httpx

@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient
```

+ **注册依赖类型**：在创建代理时，通过 `deps_type` 参数指定依赖项的数据类类型，以启用类型检查。

```python
from pydantic_ai import Agent

agent = Agent(
    model='openai:gpt-4o',
    deps_type=MyDeps
)
```

+ **访问依赖项**：在系统提示函数、工具函数和结果验证器中，通过 `RunContext` 类型访问依赖项。`RunContext` 使用泛型参数指定依赖项的类型，确保类型安全。

```python
from pydantic_ai import RunContext

@agent.system_prompt
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get(
        'https://example.com',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'}
    )
    return f'Prompt: {response.text}'
```

> 💡系统提示函数、函数工具 和 结果验证器 <font style="color:rgba(0, 0, 0, 0.87);">都在代理运行的异步上下文中运行。如果这些函数不是协程（例如</font>`async for`<font style="color:rgba(0, 0, 0, 0.87);">），则会使用</font>`run_in_executor` <font style="color:rgba(0, 0, 0, 0.87);">在线程池中调用它们，因此，如果依赖项执行 IO 操作，则最好使用</font>`async`<font style="color:rgba(0, 0, 0, 0.87);">方法，尽管同步依赖项也可以正常工作。</font>
>

#### 📌 类型安全
根据前文内容，该框架可以支持通过以下几种方式实施类型安全：

+ Pydantic 模型
+ 静态类型检查
+ 运行时验证
+ 结构化输出

同时也支持通过与 mypy 和 pyrite 等静态类型检查器集成，使类型检查尽可能简单。

### 消息历史记录
#### **访问消息历史**
+ `RunResult` 和 `StreamedRunResult` 对象提供了以下方法来访问消息：
+ `all_messages()`: 返回当前运行的所有消息，包括系统提示、用户输入和模型响应。
+ `new_messages()`: 仅返回当前运行中新生成的消息。
+ `all_messages_json()` 和 `new_messages_json()`: 分别返回上述方法的 JSON 字节表示。

> 💡在**流式运行**（`run_stream`）中，最终的输出消息不会立即包含在 `all_messages()` 中，直到流完成后才会添加进来，如下示例所示：
>

```python
agent = Agent(model=llm, system_prompt='Be a helpful assistant.')

async def main():
    async with agent.run_stream('Tell me a joke.') as result:
        # incomplete messages before the stream finishes
        # print(result.all_messages())
        async for text in result.stream_text():
            print(text)
            #> Did you hear
            #> Did you hear about the toothpaste
            #> Did you hear about the toothpaste scandal? They called
            #> Did you hear about the toothpaste scandal? They called it Colgate.

        # complete messages once the stream finishes
        # print(result.all_messages())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```

#### 在多轮对话中传递消息  
 在后续的代理运行中，可以将先前的消息传递给 `message_history` 参数，以维持对话上下文  

```python
result2 = agent.run_sync('Explain?', message_history=result1.new_messages())
```

 如果 `message_history` 不为空，系统提示将不会被重新生成，假设现有的消息历史已包含系统提示。  

####  存储和加载消息  
 可以将消息历史**序列化**为 JSON 格式，存储到文件中，以便后续加载和使用：  

```python
def log_messages(messages):
    serialized = [
        {
            "role": m.role if hasattr(m, "role") else "unknown", 
            "content": m.content if hasattr(m, "content") else str(m),
        }
        for m in messages
    ]
    with open("all_messages.json", "w") as f:
        json.dump(serialized, f, indent=2)
```

 这种方式适用于构建多代理系统，或在代理图（Agent Graph）中共享消息历史。  

### **流式输出（Streaming Output）**
+ 通过 `run_stream` 方法，可以启动一个流式会话，逐步接收模型的输出：

```python
async with agent.run_stream('Tell me a joke.') as result:
    async for message in result.stream_text(delta=True):
        print(message)
```

+ 在流式输出中，`stream_text(delta=True)` 方法允许以增量的方式获取模型的文本响应，适用于实时显示模型生成内容的场景。

### 持久化（Persistence）
**数据持久化方式**： 

+ PydanticAI 使用 Pydantic 模型定义结构化输出（如 BaseModel），这些输出可以在运行时通过工具或外部服务（如数据库）持久化。例如，代理运行的结果可以保存到外部数据库（如 PostgreSQL）或文件系统中。
+ 通过依赖注入（Dependency Injection），开发者可以注入数据库连接（如 DatabaseConn），将代理生成的结构化数据（如 SupportOutput）写入数据库或查询历史数据。
+ 集成 **Pydantic Logfire** 可持久化日志、追踪和指标数据到 Logfire 后端，支持 30 天保留期，适合调试和监控。

**运行时上下文与消息历史**： 

+ PydanticAI 支持通过 Messages and Chat History 传递先前运行的消息，提供短期上下文持久化，适合多轮对话场景。
+ 长期上下文持久化需开发者自行实现，例如通过外部状态管理（如 Postgre 等）保存代理状态或消息历史。

### 调试与监控（Debugging and Monitoring）
Pydantic Logfire 是一个由创建和维护 Pydantic 和 PydanticAI 的团队开发的可观察性平台。Logfire 旨在观测整个应用程序：Gen AI、经典预测 AI、HTTP 流量、数据库查询以及现代应用程序所需的一切。PydanticAI 具有对 Logfire 的内置（但可选）支持。如果安装并配置了 `logfire` 软件包并启用了代理检测，则会将有关代理运行的详细信息发送到 Logfire。否则，几乎没有开销，也不会发送任何内容。

> <font style="color:rgba(0, 0, 0, 0.87);">Logfire 是一个商业支持的托管平台，并通过开源 SDK（MIT 许可）和提供免费套餐降低使用门槛</font>
>

<font style="color:rgba(0, 0, 0, 0.87);">官方界面示例：</font>

![](pictures/logfire-weather-agent.png)

### 基于图的异步状态机  
`**pydantic-graph**` 是一个官方独立出来的库，可用于构建基于图的异步状态机 。它不依赖于 `pydantic-ai`，可用于任何需要图或状态机的工作流，如任务调度、流程自动化或事件驱动系统。 它采用图结构（Graph）来组织节点（Node）和状态（State），使得开发者可以以声明式的方式定义和执行多步骤的流程控制。 

虽然**图** 和 **状态机**(FSM)  是强大的工具，能够帮助建模和控制复杂工作流，但它们并不适合每一个场景。官方对这块的说法是： 如果你不喜欢 Python 的类型提示，那么这种图的方法可能并不适合你，因为 `pydantic-graph` 依赖**类型提示**和**泛型**，主要面向有一定基础的高级开发者和更复杂业务需求的情况。 在使用图之前，应该考虑是否真的需要这么复杂的工具。

#### 📌 核心组件
`pydantic-graph` 的主要组件包括：

+ **GraphRunContext**：<font style="color:rgba(0, 0, 0, 0.87);">图运行的上下文，类似于 PydanticAI 的</font> `RunContext`<font style="color:rgba(0, 0, 0, 0.87);">。它保存图的状态和依赖项，并在节点运行时传递给节点。</font>
+ **BaseNode**： 定义图中执行的节点。节点通常由以下部分组成：
    - 包含调用节点时需要的任何必需/可选参数的字段
    - 执行节点的业务逻辑，在 `run` 方法中
    - `run` 方法的返回注释，`pydantic-graph` 读取这些注释以确定节点的传出边
+ **End**：表示图的执行结束，返回最终结果。
+ **Graph**：由多个节点组成的图，管理节点之间的连接和执行流程。  围绕类型安全有下面三个泛型：
    - <font style="color:rgb(31, 35, 40);">StateType</font>
    - <font style="color:rgb(31, 35, 40);">DepsType</font>
    - <font style="color:rgb(31, 35, 40);">ReturnType</font>

#### 📌 特性亮点
+ **类型安全**
    - **类型提示与泛型支持**：pydanticai-graph 利用 Python 的类型提示和泛型机制，确保节点间数据传递、状态管理和依赖注入的类型一致性。每个节点（继承自 BaseNode）通过泛型参数明确指定状态类型（StateT）、依赖类型（DepsT）和返回类型（RunEndT），在编译时即可捕获类型错误。
    - **动态边缘类型检查**：节点通过 run 方法的返回类型注解定义出边（指向下一个节点或 End），确保图的结构在类型层面是安全的。例如，Union[AnotherNode, End[int]] 允许节点动态决定后续路径，同时保持类型约束。
+ **异步支持**
    - **全异步节点执行**：所有节点的 run 方法均为异步（async def），支持处理异步操作，如网络请求、文件 IO 或调用外部 API。这使得 `pydanticai-graph` 非常适合高并发场景，例如实时数据处理或与 LLM 的交互。
    - **异步迭代**：<font style="color:rgba(0, 0, 0, 0.87);">有时你希望在图执行时直接控制或深入了解每个节点。最简单的方法是使用</font>` Graph.iter`<font style="color:rgba(0, 0, 0, 0.87);">方法，该方法返回一个</font>**<font style="color:rgba(0, 0, 0, 0.87);">上下文管理器</font>**<font style="color:rgba(0, 0, 0, 0.87);">，该管理器产生一个</font>`GraphRun`<font style="color:rgba(0, 0, 0, 0.87);"> 对象。</font>`GraphRun`<font style="color:rgba(0, 0, 0, 0.87);"> 是图中节点的异步可迭代对象，允许你在节点执行时记录或修改它们</font>
+ **依赖注入**
    - **类型安全的依赖注入**：通过 GraphRunContext.deps 和泛型参数 DepsT，支持在节点中注入外部依赖（如数据库连接、执行器或配置对象）。开发者可通过 dataclass 或 Pydantic 模型定义依赖结构。
    - **测试友好**：依赖注入便于模拟依赖项，支持单元测试和集成测试。例如，可以注入模拟的数据库客户端或日志记录器。
    - **跨进程支持**：支持注入如 ProcessPoolExecutor 的资源，用于将计算任务卸载到单独进程（如 deps_example.py 中的示例）。

```python
@dataclass
class GraphDeps:
    executor: ProcessPoolExecutor

@dataclass
class Increment(BaseNode[None, GraphDeps]):
    foo: int
    async def run(self, ctx: GraphRunContext[None, GraphDeps]) -> DivisibleBy5:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(ctx.deps.executor, self.compute)
        return DivisibleBy5(result)
```

+ **状态图**
    - **状态传递与更新**：图的状态（StateT 类型，通常为数据类或 Pydantic 模型）可在节点间传递和修改。每个节点通过 GraphRunContext.state 访问和更新状态，类似生产线上逐步构建的工件。
    - **灵活状态管理**：支持无状态图（StateT 默认为 None）和有状态图，适应从简单逻辑到复杂多步工作流的各种场景。
+ **迭代图**
    - **异步迭代（Graph.iter）**：Graph.iter 方法返回一个异步上下文管理器，产生 GraphRun 对象，允许开发者通过 async for 逐节点迭代图的执行过程。这种方式适合需要精细控制或实时监控的工作流。 **支持记录节点状态、修改执行路径或提前终止。**

```python
async def main():
    state = CountDownState(counter=3)
    async with count_down_graph.iter(CountDown(), state=state) as run:
        async for node in run:
            print('Node:', node)  # 打印每个节点
        print('Final result:', run.result.output)  # 打印最终结果

# Node: CountDown()
# Node: CountDown()
# Node: CountDown()
# Node: End(data=0)
# Final result: 0
```

+ **状态持久化**
    - **中断与恢复：pydanticai-graph 通过状态持久化支持图执行的中断和恢复，**简化了处理暂停、用户输入或长时间运行的工作流。**状态持久化在每个节点运行前后快照图状态，允许从任意点恢复执行。**
        * **SimpleStatePersistence**：内存中保存最新快照，适合临时运行（默认实现）。
        * **FullStatePersistence****：内存中保存所有快照历史，适合调试或需要完整执行记录的场景。**
        * **FileStatePersistence****：将快照保存为 JSON 文件，适合跨进程或持久化存储。**
        * **自定义持久化：开发者可通过继承 BaseStatePersistence 实现自定义存储（如数据库持久化）。**

#### 📌 简单示例
```python
from dataclasses import dataclass

from pydantic_graph import BaseNode, End, GraphRunContext


@dataclass
class MyNode(BaseNode[MyState, None, int]):  
    foo: int

    async def run(
        self,
        ctx: GraphRunContext[MyState],
    ) -> AnotherNode | End[int]:  
        if self.foo % 5 == 0:
            return End(self.foo)
        else:
            return AnotherNode()

async def main():
    graph = Graph(  
# 通过将节点列表传递给 Graph 来创建图。节点的顺序并不重要，但它可能会影响图的显示方式。
    nodes=[MyNode]
)
    state = MyState()
# 初始化状态。这将传递给图运行并在图运行时发生变化。
    await graph.run(MyNode(), state=state)  
# 使用初始状态运行图。由于图可以从任何节点运行，因此我们必须传递起始节点 —— 在本例中为MyNode() 。Graph.run 返回一个 GraphRunResult，该结果提供最终数据和运行历史记录。
```

+ `BaseNode[MachineState]`：表示一个图中的节点，处理 `MachineState` 类型的状态。每个节点都包含业务逻辑，运行时会通过 `ctx` 更新或读取 `MachineState`。
+ `GraphRunContext[MachineState]`：表示运行上下文，包含图运行时所需的状态。在每个节点执行时，`GraphRunContext` 提供访问、修改状态的能力。

更进一步，以下是一个**Graph结合Agent**的示例：

```python
# Define the agents
@dataclass
class AgentResponse:
    property: bool
    field: str
    response: str

@dataclass
class AgentDeps:
    another_property: bool

agent_a = Agent(deps_type=AgentDeps, result_type=AgentResponse, system_prompt=..., tools=[...])
agent_b = Agent(deps_type=AgentDeps, result_type=AgentResponse, system_prompt=..., tools=[...])


# Graph state
class GraphState(BaseModel):
    user_prompt: str
    message_history: list[ModelMessage]
    graph_property: bool


# Graph nodes
class GraphNodeA(BaseNode[GraphState, None, str]):
    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> GraphNodeA | GraphNodeB | End[str]:
        ...
        # extract relevant graph state into agent deps
        deps = AgentDeps(another_property = not ctx.state.graph_property)

        # run agent
        r: AgentRunResult[AgentResponse] = await agent_a.run(
            user_prompt=ctx.state.user_prompt, message_history=ctx.state.message_history, deps=deps
        )
        ...
        if r.data.property:
            return End(r.data.response)

        if r.data.field == "A":
            return GraphNodeA()

        return GraphNodeB()


class GraphNodeB(BaseNode[GraphState, None, str]):
    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> GraphNodeA | GraphNodeB | End[str]:
        ...
       
        # extract relevant graph state into agent deps
        deps = AgentDeps(another_property = not ctx.state.graph_property)

        # run agent
        r: AgentRunResult[AgentResponse] = await agent_b.run(
            user_prompt=ctx.state.user_prompt, message_history=ctx.state.message_history, deps=deps
        )
        ...

        if r.data.property:
            return End(r.data.response)

        if r.data.field == "B":
            return GraphNodeB()

        return GraphNodeA()


# Define the graph
graph = Graph(nodes=[GraphNodeA, GraphNodeB])
state = GraphState(
    user_prompt="Hello, how are you?",
    message_history=[],
)

# Run the graph
r: GraphRunResult[GraphState, str] = await graph.run(
    start_node=GraphNodeA(), state=state
)

# Process the result
print(r.output)
```

#### 📌 框架局限
+ 注意，目前，官方尚**不支持节点并行**，见 [#704](https://github.com/pydantic/pydantic-ai/issues/704) ，<font style="color:rgb(31, 35, 40);">如果需要自己实现并行需要考虑</font>**<font style="color:rgb(31, 35, 40);">节点顺序依赖</font>**<font style="color:rgb(31, 35, 40);">，即如何知道何时启动一个依赖多个其他节点完成的节点？</font>
+ 当前 pydanticai-graph** 缺乏内置的流式输出支持**，需要自己实现为每个节点类型、代理内部逻辑和顶层图分别实现流式输出逻辑。这导致： 
    - 代码重复：大家都在重复造类似轮子。
    - 复杂性：实现流式输出需要深入了解代理的图结构、节点逻辑和图的组合方式。
    - 最好通过简单的 API（如 graph.iter）实现顶层图的流式输出，类似于 LangGraph 的 graph.stream 方法，能够逐个产生事件或消息，而无需等待整个图执行完成，类似下面这样：

```python
async with graph.iter(start_node=GraphNodeA(), state=state) as graph_run:
    async for node in graph_run:
        async with node.stream(graph_run.ctx) as node_stream:
            async for event in node_stream:
                yield event
```

+ pydanticai-graph目前**不支持内置的嵌套子图（pipeline）功能**，即无法直接将一个 Graph 实例作为另一个图的 BaseNode 节点。虽然可以通过手动封装子图的逻辑在节点中调用子图的执行，从而实现类似嵌套的效果，但这种方法需要开发者显式管理子图的执行和状态传递。 

---

# AutoGen
## 基本介绍
AutoGen 是由微软开发的一个开源框架，用于构建协作式对话 AI 代理，能够通过多代理对话完成复杂任务。它允许开发者创建多代理系统，代理通过消息交换协作，利用大语言模型（LLM）自主或结合人类输入完成任务。AutoGen 支持灵活的代理配置、工具集成和对话驱动的工作流，适用于需要动态代理协调的场景，如代码生成、数据分析和任务自动化。

**核心功能**：

+ **多代理对话**：代理通过消息协作，每个代理可拥有特定角色或工具。
+ **灵活代理类型**：支持基于 LLM 的代理、人类参与代理和工具执行代理。
+ **工具集成**：代理可调用外部工具或函数，如代码执行或 API 请求。
+ **对话模式**：支持自定义对话流，包括顺序、群聊或层次结构。
+ **人类反馈**：支持无缝集成人类输入以指导或验证代理行为。

AutoGen 适用于需要迭代推理和协作的任务，相较于基于图的框架如 LangGraph，其架构更轻量且扩展性强。

_官方参考_：[AutoGen 文档](https://microsoft.github.io/autogen/)，[AutoGen GitHub](https://github.com/microsoft/autogen)。

## 框架测评
### 使用说明
AutoGen 通过对话代理组织工作流，代理协作完成任务。对于 PDF 解析与摘要任务，可定义 **PDF 解析代理**（提取文本）和 **摘要代理**（生成结构化摘要）。每个代理配置角色、LLM 或工具。、

```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Configure LLM (e.g., OpenAI or local model)
config_list = config_list_from_json("OAI_CONFIG_LIST")

# Define agents
parser_agent = AssistantAgent(
    name="PDFParser",
    system_message="Extract text chunks from a PDF and return structured data.",
    llm_config={"config_list": config_list}
)
summarizer_agent = AssistantAgent(
    name="Summarizer",
    system_message="Summarize provided text chunks into a structured format with problem_definition, problem_value, and existing_solutions.",
    llm_config={"config_list": config_list}
)
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "output"}
)

# Initiate conversation
user_proxy.initiate_chat(
    parser_agent,
    message="Parse the PDF at 'upload/pdf/ai_foreveryone.pdf' and pass the text to the summarizer."
)

# Summarizer receives parsed text and generates summary
parser_agent.send(
    message="Here are the parsed text chunks: {...}",
    recipient=summarizer_agent
)
```

### 状态管理
AutoGen 通过 **对话历史** 管理状态，每个代理维护消息日志（包含发送者、接收者和内容的字典列表）。状态通过消息隐式传递，不像 LangGraph 使用集中式 StateGraph。开发者可访问或修改对话历史以跟踪任务进度。

+ **机制**：代理的 chat_messages 字典存储对话状态。PDF 任务中，解析代理的输出（文本块）作为消息传递给摘要代理。
+ **局限**：无内置类型化状态schema（如 TypedDict 或 Pydantic），需手动确保消息一致性。
+ **定制**：可定义自定义状态对象并作为消息负载传递，但需手动实现。

### 细粒度控制
AutoGen 通过对话模式和代理配置提供灵活控制：

+ **顺序工作流**：代理按预定顺序通信（如解析 → 摘要）。
+ **群聊**：通过 GroupChatManager 管理多代理协作，适合并行任务（如同时解析和关键词提取）。
+ **条件逻辑**：代理可通过分析消息内容或工具函数中的自定义代码实现分支。
+ **重试**：支持通过 LLM 响应验证或自定义错误处理实现重试。

```python
# Conditional branching example
def parse_document(message):
    text_chunks = extract_pdf_text(message["pdf_path"])
    if len(text_chunks) == 0:
        return {"error": "Empty PDF"}
    return {"text_chunks": text_chunks}

parser_agent.register_function(parse_document)
```

### 异步执行
AutoGen 通过 Python 的 asyncio 支持异步执行。代理可并发处理消息或执行工具，适合 I/O 密集任务如 API 调用或 LLM 推理。

```python
import asyncio
from autogen import AssistantAgent

# Async PDF parsing simulation
async def async_parse_pdf(pdf_path):
    return {"text_chunks": ["Sample text"]}

parser_agent = AssistantAgent(
    name="AsyncParser",
    system_message="Parse PDF asynchronously.",
    llm_config={"config_list": config_list}
)
parser_agent.register_async_function(async_parse_pdf)

# Run async conversation
async def main():
    result = await parser_agent.a_initiate_chat(
        recipient=user_proxy,
        message={"pdf_path": "upload/pdf/ai_foreveryone.pdf"}
    )
asyncio.run(main())
```

### 分布式支持
AutoGen 无内置分布式计算支持（如 Ray 或 Dask）。可通过在不同进程或机器上运行代理并通过 API 或消息队列通信实现分布式，但需自定义编排。

### 流式输出
AutoGen 通过兼容的 LLM 提供商（如 OpenAI 的流式 API）支持 LLM 响应的流式输出。流式中间结果（如解析过程中的部分文本块）需自定义实现，因对话模型通常等待完整消息。

```python
# Enable streaming for LLM output
parser_agent.llm_config["stream"] = True
user_proxy.initiate_chat(
    parser_agent,
    message="Parse and stream text chunks from the PDF."
)
```

> 💡流式输出限于 LLM 响应，非工作流事件（如 LangGraph 的 graph.stream）。
>

### 持久化
AutoGen 无内置状态持久化支持，需手动将对话历史保存到文件或数据库（如 JSON、SQLite），例如：

```python
import json
# Save state after each message
def save_state(state):
    with open("state.json", "w") as f:
        json.dump(state, f)

parser_agent.on_message(lambda msg: save_state(msg))
```

##### 8. 日志与可观测性
AutoGen 通过 Python 的 logging 模块提供基本日志，记录代理交互和错误。可启用详细模式或集成 LangSmith 进行 LLM 调用追踪，**无内置对话流可视化**。

---

# CrewAI
## 基本介绍
 CrewAI 是一个以“团队”概念为核心的智能代理框架，主打多代理协作。它通过共享内存、消息传递和代理自动连接等机制，把多代理协作中的常见功能封装成可复用模块，降低了开发复杂度。使用配置文件就能快速搭建系统，非技术人员也能参与。整体来看，CrewAI 上手简单、协作能力强，适合用来构建需要多智能体协同工作的应用。  <font style="color:rgb(36, 36, 36);">与 LangGraph 的确定性结构不同，CrewAI 代理旨在突出自主和协作。</font>

**<font style="color:rgb(36, 36, 36);">主要组成：</font>**

+ **CrewAI Crews**：针对自主性和协作智能进行优化，使得能够自由组建的AI团队，其中每个代理都有特定的角色、工具和目标。
+ **CrewAI Flows**：支持精细、事件驱动的控制、单个 LLM 调用以实现精确的任务编排，并原生支持 Crews。

**技术特点：**

**Crews：团队式多智能体系统**

+ Crews 是由多个 AI 代理组成的协作小组，每个代理都扮演一个具体角色（如 researcher、writer），并可配置专属工具（如网页爬虫、文档读取器）和目标任务。
+ 代理之间支持消息传递和共享记忆，具备一定的自主协作能力。你可以用代码或 YAML 文件来定义 Crews，其中 YAML 更适合多人协作和大规模项目。
+ Crews 的配置灵活，支持任务列表、执行顺序（顺序或嵌套）、最大请求频率（max_rpm）、短期/长期/实体记忆机制、缓存机制、嵌入器等。同时还支持 step/task 回调函数和日志输出，可用于调试和监控。

**Flows：流程级任务编排系统**

+ Flows 是一种事件驱动的工作流机制，用于组织和控制多个任务或 Crews 的执行流程。适合构建从数据收集到执行再到生成的多步骤流程。
+ 它支持条件判断（如 or_ / and_）、流程分支、循环执行等逻辑控制。你可以通过装饰器（如 `@start`、`@listen`、`@router`）来定义流程入口、监听事件和决策路径。
+ Flows 既可以串联多个任务，也可以嵌套多个 Crews，实现“智能协作 + 精准控制”的组合。此外，它还内置状态管理（支持结构化或非结构化状态）、持久化（基于 SQLite）和流程可视化功能，帮助开发者更好地理解和调试流程逻辑。

> _官方参考_：[CrewAI 文档](https://docs.crewai.com/)，[CrewAI GitHub](https://github.com/joaomdmoreno/crewai)。
>

## 框架测评
### 使用说明
+ <font style="color:rgb(36, 36, 36);">创建Agent → 定义具有独特技能的 AI Agent。</font>
+ <font style="color:rgb(36, 36, 36);">分配角色 → 每个Agent都有一个角色（例如，研究员、作家、验证者）。</font>
+ <font style="color:rgb(36, 36, 36);">执行 Crew Task → Agent 协作实现目标。</font>

```python
from crewai import Agent, Crew, Task

# Define Agents
researcher = Agent(role="Researcher", goal="Find recent AI advancements")
writer = Agent(role="Writer", goal="Summarize research into an article")

# Define Task
task = Task(agents=[researcher, writer], objective="Write an article on AI trends")

# Create and Run Crew
crew = Crew(agents=[researcher, writer], tasks=[task])
result = crew.kickoff()
print(result)
```

### 状态管理
+ **Crews**：
    - 状态通过代理间消息传递和共享记忆管理。
    - 支持短期记忆（当前任务上下文）、长期记忆（跨任务学习）和实体记忆（特定对象信息）。
    - 缓存机制存储工具执行结果，提高重复任务效率。
+ **Flows**：
    - 内置状态管理，支持任务间状态共享。
    - 状态可为结构化（Pydantic BaseModel）或非结构化（字典），每实例有唯一 UUID。
    - 通过 @persist 装饰器实现状态持久化，默认使用 SQLite 后端。

### 细粒度控制
+ **Crews**：
    - 高层次控制，通过角色分配、目标设定和流程类型（顺序或层次）管理。
    - 层次模式下，管理代理动态分配任务，支持条件逻辑。
    - 支持任务重试（max_retries）和回调函数，增强控制能力。
+ **Flows**：
    - 细粒度控制，支持：
        * 条件逻辑（or_、and_）。
        * 循环和分支（通过 @router 装饰器）。
        * 事件驱动触发（通过 @listen 响应事件）。
    - 允许精确定义任务依赖和执行顺序。

### 异步与并发
+ **Crews**：
    - 代理支持异步操作，任务可并发执行。
    - 提供异步启动方法：kickoff_async()（单次异步）和 kickoff_for_each_async()（并发处理多输入）。
+ **Flows**：
    - 支持异步任务执行，允许并行运行无关任务。
    - 事件驱动架构支持动态响应和并发优化

### 流式输出
+ **有限支持**：
    - 无原生流式输出支持，任务输出以完整单元交付。
    - 可通过支持流式的 LLM 提供商（如 OpenAI）实现有限流式响应，但需自定义。

### 持久化机制
+ **Crews**：
    - 通过记忆机制（短期、长期、实体）保留上下文。
    - 缓存存储工具执行结果，加速重复调用。
+ **Flows**：
    - 支持状态持久化，使用 @persist 装饰器。
    - 默认 SQLite 后端，支持结构化和非结构化状态。
    - 可跨任务和运行保留状态。

### 可观测性
+ **控制平面**：提供 Crew 性能、资源消耗和任务进度的监控视图（企业版更完善）。
+ **日志**：支持实时日志保存（.txt 或 .json），通过 output_log_file 配置。
+ **高级监控**：可集成 LangSmith 追踪 LLM 调用；提供使用指标（usage_metrics）分析 LLM 消耗。
+ **重放功能**：支持从特定任务重放（crewai replay -t <task_id>），便于调试。



