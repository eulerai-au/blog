# Mem0 Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status**, Website https://www.mem0.ai/ or https://mem0.ai/research |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ Hierarchical management: core vector storage + graph relation layer, uses LLM to extract key information and automatically build memory |
| **Memory Retrieval Method**                | ✅ Based on vector similarity search + graph relation query (supports BM25 reranking) |
| **Performance (Latency, token, accuracy)** | ✅ On LOCOMO benchmark, 26% higher accuracy than OpenAI Memory, p95 latency reduced by 91%, token usage reduced by 90%, details https://mem0.ai/research |
| **PostgreSQL Integration (Extension)**     | ✅ Native support pgvector, supports DiskANN and HNSW indexes, full SQL interaction interface |
| **Integration with langgraph**             | ✅ Provides official integration documentation and example code |
| **API Design Reference**                   | ✅ https://docs.mem0.ai/open-source/python-quickstart         |
| **Community Activity**                     | ✅ GitHub stars 32.8k, Y Combinator S24 support, active Discord community |
| **Paper**                                  | ✅ https://arxiv.org/abs/2504.19413 (2025)                    |

##### Mem0 System Summary

![img](pictures/ur60uTft3XImAXN9Bfr5bOK9uUI.png)

![img](pictures/DkaUXgJt22p9REFF5265ZJajtmQ.png)



#### Question 1: What is Mem0’s Memory Management Method? Is Hierarchical Management Used?

Mem0 adopts a hierarchical memory management model, combining vector storage, graph storage, and memory history, to achieve efficient memory storage and retrieval. Its core design explicitly uses hierarchical management, directly inspired by human short-term memory (STM), long-term memory (LTM) cognitive structures, combined with modern AI system architecture.

| Memory Level                | Corresponding Module                                         | Function Role                                                |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Short-term Memory (STM)** | **Conversation History + Working Memory + Attention Context** | **Within the current conversation window, it tracks the latest turn and context focus in real time, for immediate reasoning. Note: this part is usually maintained directly by the LLM, not stored.** |
| **Long-term Memory (LTM)**  | **Factual Memory + Episodic Memory + Semantic Memory**       | **Uses vector databases (such as Faiss, Qdrant) to store semantically long-term memory, including facts, episodes, concepts. Enables cross-session calls via embedding search.** |
| Relational Memory (Graph)   | Graph Database (such as Memgraph, Neo4j)                     | Stores entity-relationship networks, used for reasoning, contradiction detection, fast retrieval, and visualization of complex relationships. |
| History Record (Audit)      | SQLite log library                                           | Tracks all memory operation history (add, update, delete), including timestamps, roles, operator, providing traceability, audit, version control functions. |

##### Core Management Mechanism

**1️⃣ Dual Storage Architecture** 
Mem0 combines:  

- **Vector Storage (Vector Database)** 
  Stores semantically processed facts and conversations, supports efficient approximate nearest neighbor (ANN) search.

- **Graph Database** 
  Stores entities, events and their relationships, provides relational reasoning, cross-node search.

**2️⃣ Memory Processing**  

- **LLM Extraction (Information Extraction)** → Identifies key information, entities, and relationships in dialogue.  
- **Conflict Detection and Resolution** → Compares old and new data, updates or overwrites conflicting information.  
- **Storage (Memory Storage)** → Writes to vector database and graph database, ensuring global consistency.

**3️⃣ Memory Retrieval**  

- Query Preprocessing → LLM optimizes input query, determines filtering conditions.  
- Semantic Search (Vector Search) → Semantic matching based on embedding.  
- Result Processing (Fusion and Ranking) → Aggregates multi-source results, scoring, ranking, returning.

Summary: Mem0 indeed adopts hierarchical management mechanism, combined with dual storage architecture and LLM, providing significant performance advantages.



#### Question 2: What is Mem0’s Memory Retrieval Method?

### ![search_architecture.png](pictures/search_architecture.png)

| Retrieval             | Technical Module                      | Function Role                                                |
| --------------------- | ------------------------------------- | ------------------------------------------------------------ |
| Vector Search         | Vector Store (such as Faiss, Qdrant)  | Perform approximate nearest neighbor (ANN) search on vector database, return most relevant semantic match result, with relevance score (score). |
| Graph Relation Search | Graph Store (such as Memgraph, Neo4j) | Perform entity-relation-based query on graph database, find upstream/downstream nodes, relationship chains related to the query entity or node. |

**2️⃣ Vector Semantic Search**  

- Call:  

```python
embeddings = self.embedding_model.embed(query, "search")
memories = self.vector_store.search(query=query, vectors=embeddings, limit=limit, filters=filters)
```

- Feature: Find memories closest in semantic similarity, return detailed score, memory, metadata, timestamp, etc.

**3️⃣ Graph Relation Query**  
When Graph Store (such as Memgraph) is enabled:  

```python
if self.enable_graph:
    graph_entities = self.graph.search(query, effective_filters, limit)
```



#### Question 3: How does Mem0 perform in terms of latency, token cost, and accuracy?

**A scalable memory-centric algorithm that dynamically extracts and retrieves key conversation facts — achieving 26% higher relative accuracy on the LOCOMO benchmark compared to OpenAI, p95 latency reduced by 91%, and token use reduced by 90%.**



![img](pictures/latency.png)

This chart compares each method’s **search latency** (pink represents median p50, green represents tail p95) with its reasoning accuracy (blue bar). Mem0 achieves **66.9% accuracy**, **0.20 sec median search latency**, **0.15 sec p95 latency**, keeping memory retrieval firmly in real-time. By contrast, the standard RAG setup achieves only **61.0% accuracy**, **0.70 sec median**, **0.26 sec p95 search time**. The graph-enhanced variant Mem0ᵍ further improves accuracy to **68.4%**, median **0.66 sec**, **0.48 sec p95 search latency**. By extracting and indexing only the most salient facts, Mem0 provides near state-of-the-art long-term reasoning capability while minimizing search overhead.



![img](pictures/measurement.png)

This end-to-end measurement (memory retrieval + answer generation) demonstrates Mem0’s production readiness. The full-context method reaches 72.9% accuracy but has **9.87 sec median**, **17.12 sec p95** latency. In contrast, **Mem0** achieves **66.9% accuracy**, only **0.71 sec median**, **1.44 sec p95** end-to-end response time. Its graph-enhanced variant **Mem0ᵍ** raises accuracy to **68.4%** while keeping **1.09 sec median** and **2.59 sec p95** latency. By extracting and indexing only the most relevant facts, Mem0 delivers near state-of-the-art long-term reasoning at true production speeds.



![img](pictures/performance.png)

Table 1: Performance comparison of different memory-augmented systems on various question types in the LOCOMO dataset. Evaluation metrics include F1 score (F1), BLEU-1 (B1), and LLM-as-a-Judge score (J); higher scores indicate better performance. 
A-Mem∗ indicates our re-run of A-Mem with temperature set to 0 to produce LLM-as-a-Judge scores.  
Mem0g indicates our proposed graph memory-augmented architecture. Bold numbers indicate the best performance across methods. 
(↑) means higher score is better.



![img](pictures/performance2.png)

Table 2: Performance comparison of various baselines and the proposed method. Latency measures show p50 (median) and p95 (95th percentile) values, corresponding to search time (memory/fragment retrieval time) and total time (complete response generation time). Overall LLM-as-a-Judge score (J) reflects the quality metric of responses generated over the LOCOMO dataset.



#### Question 4: How does Mem0 support PostgreSQL integration? Especially integration with pgvector / Apache AGE extension databases.

Mem0 provides seamless integration with PostgreSQL and pgvector, supporting high-performance vector storage and retrieval through these implementations.

##### PostgreSQL Connection and Initialization

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
            "index_method": "hnsw",
            "index_measure": "cosine_distance"
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movie? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})
```

##### pgvector Extension Support

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
            "port": "5432"
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movie? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})
```

##### Advanced Index Support

Mem0 supports automatic creation of two types of vector indexes: **DiskANN Index** – suitable for large-scale vector datasets, **HNSW Index** – hierarchical navigable small-world graph index.



#### Question 5: Does Mem0 support integration with LangGraph? How to integrate?

##### Official LangGraph Integration Documentation: https://docs.mem0.ai/integrations/langgraph#langgraph

Mem0's official documentation provides detailed integration steps with LangGraph and example code for building AI agents with long-term memory capabilities.

```
# init
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

# Define the state graph, set the conversation state and LangGraph structure:
class State(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    mem0_user_id: str

graph = StateGraph(State)

# Create chatbot functionality, define the core logic for the customer support AI agent： 
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

# Graph structure setup, full LangGraph structure integration：
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "chatbot")

compiled_graph = graph.compile()

# Create conversation runner, implement a function to manage the conversation flow： 
def run_conversation(user_input: str, mem0_user_id: str):
    config = {"configurable": {"thread_id": mem0_user_id}}
    state = {"messages": [HumanMessage(content=user_input)], "mem0_user_id": mem0_user_id}

    for event in compiled_graph.stream(state, config):
        for value in event.values():
            if value.get("messages"):
                print("Customer Support:", value["messages"][-1].content)
                return

# Main interaction loop, set up the main program loop for user interaction： 
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



#### Question 6: API Design Reference

Mem0 provides a simple yet powerful API design: https://docs.mem0.ai/open-source/python-quickstart  
If you have a `Mem0 API key`, you can use it to initialize the client. Alternatively, if you run Mem0 locally, you can initialize it without an API key.

```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

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



# Letta Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status**, Website https://www.letta.com/           |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ Layered, with context memory storage and long-term memory storage |
| **Memory Retrieval Method**                | ✅ String text matching and semantic similarity retrieval     |
| **Performance (Latency, token, accuracy)** | ✅ See details in paper: https://arxiv.org/abs/2310.08560     |
| **PostgreSQL Integration (Extension)**     | ✅ Defaults to PostgreSQL, supports pgvector                  |
| **Integration with langgraph**             | ❌ Not integrated by default                                  |
| **API Design Reference**                   | ✅ https://docs.letta.com/api-reference/overview              |
| **Community Activity**                     | ✅ GitHub stars 16.6k                                         |
| **Paper**                                  | ✅ memgpt: https://arxiv.org/abs/2310.08560                   |

![img](pictures/platform_overview.png)

![img](pictures/platform_system.png)

![img](pictures/example_ade_screenshot_light.png)



#### Question 1: What is Letta (formerly MemGPT)'s Memory Management Method? Does it use layered management?

Letta adopts a layered memory management mechanism, directly inspired by the layered memory management of computer operating systems.

It divides the agent's memory into two parts:

| Memory Layer                           | Corresponding Letta Module                                   | Function Role                                                |
| -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Main Context (Main Memory)**         | **`core memory` (core memory block)**                        | **Exists in the LLM prompt window, used for real-time reasoning. Stores persona, human, system settings, etc.** |
| **External Context (External Memory)** | **`archival memory` (archive block), `recall memory` (recall block)** | **Outside the context window, used to store long-term history, complete conversation records, etc., requires explicit function call to load into main context.** |
| FIFO Queue                             | Recent conversation message queue                            | Temporarily maintains the last few rounds of messages, with window length limit. Automatically evicts, summarizes, archives to recall memory when over the limit. |

**1️⃣ Fixed window + infinite external storage**

Since the LLM context window is limited (e.g., 8k, 16k, 32k tokens),  
Letta is designed so that:

Important, frequently used memory → stays in main context for real-time low-latency reasoning.

Historical, long-tail, low-frequency information → moved to external context, archived and retrieved on demand.

**2️⃣ Actively calling memory functions**

Letta defines special memory functions (called by LLM through prompts):

- `core_memory_append` → append to core memory block.
- `core_memory_replace` → replace core memory block content.
- `archival_memory_insert` → archive message into long-term storage.
- `archival_memory_search` / `conversation_search` → retrieve from archive/history.

Through these functions, cross-layer data flow is autonomously driven by the LLM.

**3️⃣ Automated queue management and memory pressure awareness**

Corresponding code location:

```bash
letta/settings.py → summarizer_settings.memory_warning_threshold
```

Default parameter:

When the FIFO queue exceeds 75%, the system issues a memory pressure warning, prompting the LLM to quickly trigger memory functions for organization.

**4️⃣ Core Design Value**

Letta can efficiently manage the limited context window, keeping the most important information in core memory for direct access, while storing a large amount of historical information externally, retrieving it when needed. This architecture is similar to the memory hierarchy of computer systems, with core memory like RAM, external storage like disk, achieving layered memory management.

| Challenge                                                   | Letta Solution                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| Limited LLM context window                                  | Layered management → main memory (core memory) for real-time reasoning, external memory (archival + recall) for long-term archive + retrieval. |
| Maintaining consistency and coherence in long conversations | Uses memory blocks, archiving, summarization, retrieval mechanisms to ensure both short-term context and long-term memory can be flexibly accessed. |
| Complex memory management requiring smart scheduling        | Combines memory pressure awareness (e.g., 75% threshold), FIFO automated summarization, function chain scheduling to let the agent balance memory automatically. |



#### Question 2: What is Letta's Memory Retrieval Method?

**1️⃣ String text matching retrieval**

    def conversation_search(self: "Agent", query: str, page: Optional[int] = 0) -> Optional[str]:

**2️⃣ Semantic similarity retrieval**

    Vector retrieval: From embeddings.py and passage_manager.py, we see that Letta uses vector embeddings for semantic search
        Text is first chunked via parse_and_chunk_text function to ensure each chunk fits the embedding model
        Uses various embedding models (OpenAIEmbeddings, AzureOpenAIEmbedding, etc.) to convert text to vectors
        query_embedding function handles the search query, generating normalized vector representations

In `PassageManager.insert_passage`:

```python
embedding = embed_model.get_text_embedding(text)
```

Call:

```python
from letta.embeddings import embedding_model
embed_model = embedding_model(agent_state.embedding_config)
```

Example:

```python
response = self.client.embeddings.create(input=text, model=self.model)
```

The resulting embedding (768-dimensional or 1536-dimensional vector) is stored in `AgentPassage` or `SourcePassage`.

When you query (`archival_memory_search`):

- Convert query text `query` to embedding.  
- Compare in database (dot product or cosine similarity) to find nearest embedding.  
- Return top-N matching passages.

**3️⃣ Explicit function call**
In `letta/memory.py`:

```python
functions = get_memory_functions(cls: Memory)
```

LLM calls:

- `archival_memory_insert()` → insert  
- `archival_memory_search()` → semantic retrieval  
- `conversation_search()` → semantic search within conversation  

These functions serve to: 
Route the LLM’s request to `PassageManager`, perform retrieval or write, and send the final result back to core memory.

graph TD
A[User inputs query] --> B[LLM triggers archival_memory_search]
B --> C[Call PassageManager]
C --> D[Query to embedding]
D --> E[Compare with database embedding]
E --> F[Get top-N passages]
F --> G[Fill back into core memory (Memory.blocks)]
G --> H[Enter LLM reasoning window]

**Summary Table**

| Mechanism                  | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| Storage structure evidence | Database stores text + embedding; ORM layer uses AgentPassage, SourcePassage encapsulation |
| Keyword retrieval          | Direct query on ORM by ID, time, label                       |
| Vector semantic retrieval  | Use embedding vectors, compare similarity (code can be extended to connect vector databases) |
| Call method                | LLM calls memory functions to explicitly initiate retrieval  |
| After retrieval fill-in    | Retrieved content summarized, trimmed, then put into core memory to enter prompt window |

Letta's memory retrieval system combines the advantages of direct access (core memory) and semantic search (external memory), allowing the agent to efficiently access in-context information while retrieving relevant content from large-scale external storage when needed. Vector embeddings and database support enable it to handle large-scale memory data and achieve efficient semantic search.



#### Question 3: How does Letta perform in terms of performance (latency, token overhead, accuracy)?

##### Table 1: Deep Memory Retrieval (DMR) Task Performance

| Model                  | Accuracy | ROUGE-L (R) |
| ---------------------- | -------- | ----------- |
| GPT-3.5 Turbo          | 38.7%    | 0.394       |
| GPT-3.5 Turbo + MemGPT | 66.9%    | 0.629       |
| GPT-4                  | 32.1%    | 0.296       |
| GPT-4 + MemGPT         | 92.5%    | 0.814       |
| GPT-4 Turbo            | 35.3%    | 0.359       |
| GPT-4 Turbo + MemGPT   | 93.4%    | 0.827       |

This table shows MemGPT's performance on the deep memory retrieval task. This task requires the agent to answer questions about topics discussed in previous conversations, testing the agent's long-term memory capabilities. Results show that adding MemGPT significantly improves all models' performance, especially GPT-4 and GPT-4 Turbo, with accuracy rising from ~30% to over 90%.

##### Table 2: Conversation Opener Performance

| Method        | SIM-1 | SIM-3 | SIM-H |
| ------------- | ----- | ----- | ----- |
| Human         | 0.800 | 0.800 | 1.000 |
| GPT-3.5 Turbo | 0.830 | 0.812 | 0.817 |
| GPT-4         | 0.868 | 0.843 | 0.773 |
| GPT-4 Turbo   | 0.857 | 0.828 | 0.767 |

Conversation opener performance. The agent's conversation openers are evaluated by similarity scores to gold persona tags (SIM-1/3) and human-crafted openers (SIM-H). MemGPT, using various base models, can outperform human-crafted openers. This table shows the performance of different models in generating personalized conversation openers. SIM-1 and SIM-3 represent similarity to gold-standard personal tags; SIM-H represents similarity to human-created openers. Results show that MemGPT can generate openers rivaling or even better than human ones.

##### Table 3: Nested Key-Value Retrieval Task Accuracy

![Screenshot from 2025-05-28 07-29-29.png](pictures/nesting.png)

Nested key-value (KV) retrieval task performance. MemGPT is the only method that can consistently complete nested KV tasks beyond 2 layers of nesting. While GPT-4 Turbo performs better as a baseline, MemGPT combined with GPT-4 Turbo performs worse than MemGPT with GPT-4. This task requires the agent to perform multi-hop retrieval, finding key-values linked through multiple layers of reference. Results show that only MemGPT using GPT-4 can maintain 100% accuracy at all nesting levels, demonstrating superior multi-hop information retrieval capabilities.

##### Table 4: Document Question-Answering Task Performance

![Screenshot from 2025-05-28 07-26-13.png](pictures/retrieved.png)

Document QA task performance. MemGPT's performance is unaffected by increases in context length. Methods like truncation can extend the effective context length of fixed-length models (like GPT-4), but as the required compression ratio increases, such compression methods degrade performance. On this task, MemGPT combined with GPT-4 and GPT-4 Turbo produces equivalent results. This task tests the model's ability to handle large volumes of documents. Results show that MemGPT can process document volumes beyond the base model’s context window while maintaining stable performance, unaffected by document count growth.

**Summary of Experimental Conclusions**

1. **Long-Term Memory Ability**: MemGPT significantly enhances the model's long-term memory, enabling consistency and personalization across multi-session dialogues.

2. **Large Document Processing**: MemGPT can analyze documents far beyond the base model’s context limitations.

3. **Multi-Hop Information Retrieval**: MemGPT excels at tasks requiring multi-step reasoning, such as nested key-value retrieval.

4. **Resource Efficiency**: Through layered memory management, MemGPT achieves more efficient resource use within a limited context window.



#### Question 4: How does Letta support integration with PostgreSQL? Especially integration with pgvector/Apache AGE extension databases?

Native support for PostgreSQL and pgvector vector retrieval

##### Letta Architecture Entry

Letta’s database access is mainly concentrated in these modules:

- `letta/server/db.py`: database registration, connection management (PostgreSQL/SQLite auto-switching)
- `letta/orm/sqlalchemy_base.py`: ORM base class, supports embedding retrieval
- `letta/services/passage_manager.py`: business logic layer, inserts embedding passages

##### PostgreSQL Integration Mechanism

Core logic in letta/server/db.py:

```python
if settings.letta_pg_uri_no_default:
    engine = create_engine(settings.letta_pg_uri, **self._build_sqlalchemy_engine_args(is_async=False))
    self._engines["default"] = engine
```

Explanation: If `LETTA_PG_URI` is set, it automatically switches to PostgreSQL; otherwise, it uses the default `sqlite.db`.

##### pgvector Support (Vector Retrieval)

In `letta/orm/sqlalchemy_base.py::_list_preprocess()`:

```python
if query_embedding:
    if settings.letta_pg_uri_no_default:
        # PostgreSQL with pgvector
        query = query.order_by(cls.embedding.cosine_distance(query_embedding).asc())
```

##### Embedding Vector Generation and Storage

In `letta/services/passage_manager.py::insert_passage()`:

```python
embedding = embed_model.get_text_embedding(text)
```

Then wrapped as a passage for storage:

```python
PydanticPassage(
    text=text,
    embedding=embedding,
    embedding_config=...,
)
```

ORM models: `AgentPassage`, `SourcePassage`

Database field `embedding` is mapped to `vector`, supporting pgvector queries.

##### Apache AGE Support

Currently, Letta source code **does not directly integrate Apache AGE** (AGE is a PostgreSQL extension and can coexist with pgvector).



#### Question 5: Does Letta support integration with LangGraph? How to integrate?

No official support or documentation was found indicating Letta (formerly MemGPT) has direct integration with LangGraph.



#### Question 6: API Design Reference

https://docs.letta.com/api-reference/overview





# LangMem Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status**: https://github.langchain.ac.cn/langmem/  |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ Layered management: short-term memory summary + long-term semantic/contextual/procedural memory, supports active and background extraction |
| **Memory Retrieval Method**                | ✅ Direct access (retrieve specific memory by key), semantic access (semantic similarity search, vectors), metadata filtering (filter based on memory attributes) |
| **Performance (Latency, token, accuracy)** | ❌ Not found                                                  |
| **PostgreSQL Integration (Extension)**     | ✅ Supports pgvector via LangGraph's BaseStore abstraction    |
| **Integration with langgraph**             | ✅ Deep integration with LangGraph, provides dedicated graph nodes and tools, supports state flow and configuration sharing |
| **API Design Reference**                   | ✅ https://github.langchain.ac.cn/langmem/reference/          |
| **Community Activity**                     | ⚠️ Relatively new project, but developed within LangGraph ecosystem, has professional support and active maintenance, Star 502 github |
| **Paper**                                  | ❌ No directly related academic paper found, but detailed concept and technical documentation available |

![Hot Path Quickstart Diagram](pictures/hot_path_vs_background.png)

#### Question 1: What is LangMem's Memory Management Method? Does it use layered management?

| Memory Type | Purpose             | Agent Example                                  | Human Example                            | Typical Storage Pattern    |
| ----------- | ------------------- | ---------------------------------------------- | ---------------------------------------- | -------------------------- |
| Semantic    | Facts and knowledge | User preferences; knowledge triples            | Knowing Python is a programming language | Archive or collection      |
| Contextual  | Past experiences    | Few-shot examples; past conversation summaries | Remembering your first day at work       | Collection                 |
| Procedural  | System instructions | Core personality and response patterns         | Knowing how to ride a bicycle            | Prompt rules or collection |

##### Integration Modes

LangMem's memory tools are organized at two integration mode layers

##### 1. Core API

At its core, LangMem provides functions that transform memory state without side effects. These primitives are the building blocks of memory operations.

- [**Memory Managers**](https://github.langchain.ac.cn/langmem/reference/memory/#langmem.create_memory_manager): Extract new memories, update or delete outdated memories, and consolidate and summarize existing memories based on new conversation information
- [**Prompt Optimizers**](https://github.langchain.ac.cn/langmem/reference/prompt_optimization/#langmem.create_prompt_optimizer): Update prompt rules and core behaviors based on conversation information (with optional feedback)

These core functions do not depend on any specific database or storage system. You can use them in any application.

##### 2. Stateful Integration

One layer above depends on LangGraph's long-term memory storage. These components use the above core APIs to transform existing stored memories and perform upsert/delete as needed when new conversation information arrives.

- [**Store Managers**](https://github.langchain.ac.cn/langmem/reference/memory/#langmem.create_memory_store_manager): Automatically persist extracted memories
- [**Memory Management Tools**](https://github.langchain.ac.cn/langmem/reference/tools/#langmem.create_manage_memory_tool): Give agents direct access to memory operations

If you are using LangGraph Platform or LangGraph OSS, you can use these tools as they provide an easy way to add memory capabilities to your agents.



#### Question 2: What is LangMem's Memory Retrieval Method?

- [**Direct Access**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.get): Retrieve specific memory by key
- [**Semantic Search**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.search): Find memories via semantic similarity
- [**Metadata Filtering**](https://github.langchain.ac.cn/langgraph/reference/store/#langgraph.store.base.BaseStore.search): Filter based on memory attributes



#### Question 3: How does LangMem perform in terms of performance (latency, token overhead, accuracy)?

No specific performance benchmark data found



#### Question 4: How does LangMem support integration with PostgreSQL? Especially integration with pgvector/Apache AGE extension databases?

LangMem supports PostgreSQL and pgvector integration via LangGraph's BaseStore abstraction layer.



#### Question 5: Does LangMem support integration with LangGraph? How to integrate?

LangMem not only supports integration with LangGraph, it is a memory management system specifically designed for LangGraph, providing a seamless integration experience.
You can integrate LangMem's **memory tools** into LangGraph's agent framework.
LangMem's integration with LangGraph is native and comprehensive, offering multiple integration modes: graph nodes, tools, state access, and configuration sharing.

For example: The `graphs/semantic.py` file shows LangMem's native integration with LangGraph:

```python
# graphs/semantic.py - Official integration example
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
    # Hardcoded response (example)
    response = {"role": "assistant", "content": "I'll remember that preference"}
    await manager.ainvoke(
        {"messages": [{"role": "user", "content": message}, response]}
    )
    return response
```

#### Question 6: API Design Reference

LangMem provides clear API design: https://github.langchain.ac.cn/langmem/reference/



# Memary Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status**: https://github.com/kingjulio8238/Memary  |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ Layered management: MemoryStream (short-term) + EntityKnowledgeStore (long-term), external knowledge graph storage |
| **Memory Retrieval Method**                | ✅ Knowledge graph retrieval + frequency weighting + time sorting + synonym expansion, supports hybrid internal and external retrieval |
| **Performance (Latency, token, accuracy)** | ❌ No paper or official website provided                      |
| **PostgreSQL Integration (Extension)**     | ❌ No native support, currently only supports Neo4j and FalkorDB graph databases |
| **Integration with langgraph**             | ❌ No native support, no LangGraph dependency                 |
| **API Design Reference**                   | ❌ No official website provided                               |
| **Community Activity**                     | ❌ Star 2.2k github, no updates after 7 months ago            |
| **Paper**                                  | ❌ No related academic paper seen                             |

Summary:

![memary overview](pictures\system.png)

#### Question 1: What is Memary's Memory Management Method? Does it use layered management?

1️⃣ Short-term Memory (MemoryStream)

- **Module** :`memary.memory.memory_stream.MemoryStream`

- **Storage** : Individual `MemoryItem`s, recording each entity and timestamp.

- **Source** : Directly added from each conversation or call.

- **Role** : Temporarily retains encountered entities, like “recently seen/thought items”.

- **Code Evidence**

  ```python
  self.memory_stream.add_memory(entities)
  self.memory_stream.save_memory()
  ```

2️⃣ Long-term Memory (EntityKnowledgeStore)

- **Module** : `memary.memory.entity_knowledge_store.EntityKnowledgeStore`

- **Storage** : Individual `KnowledgeMemoryItem`s, aggregating entity occurrence counts and most recent occurrence time.

- **Source** : Aggregates short-term memory from MemoryStream into long-term statistics.

- **Role** : Builds more stable “knowledge preferences” or “important entities” for subsequent reasoning.

- **Code Evidence**

  ```python
  self.entity_knowledge_store.add_memory(self.memory_stream.get_memory())
  self.entity_knowledge_store.save_memory()
  ```

3️⃣ Layered structure clear code evidence
In `ChatAgent.add_chat()`:

```python
if entities:
    self.memory_stream.add_memory(entities)
    self.memory_stream.save_memory()
    self.entity_knowledge_store.add_memory(self.memory_stream.get_memory())
    self.entity_knowledge_store.save_memory()
```

This clearly shows: 
Short-term memory (MemoryStream) → Aggregated into long-term memory (EntityKnowledgeStore)  
And long-term memory is not just simple stacking, but: aggregates occurrence frequency (`count`) and most recent time (`date`) 
This is a typical **layered management, hierarchical storage**.

| Aspect              | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Layered or not      | Yes, divided into short-term (MemoryStream) and long-term (EntityKnowledgeStore) |
| Short-term memory   | Stores entity + timestamp, grows as a stream                 |
| Long-term memory    | Aggregates entities → occurrence count, most recent time, forms knowledge storage |
| Main use            | Short-term provides context recall, long-term provides importance aggregation and reasoning |
| Clear code location | `ChatAgent.add_chat()` calls MemoryStream and EntityKnowledgeStore's add_memory and save_memory methods |



#### Question 2: What is Memary's Memory Retrieval Method?

Memary implements multiple memory retrieval methods:

**Graph Retrieval**: Uses `KnowledgeGraphRAGRetriever` for graph-structure-based retrieval

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
# Cypher query: supports direct graph query language
# /src/memary/agent/base_agent.py
def generate_string(entities):
    cypher_query = "MATCH p = (n) - [*1 .. 2] - ()\n"
    cypher_query += "WHERE n.id IN " + str(entities) + "\n"
    cypher_query += "RETURN p"
```

**Hybrid Retrieval Strategy**: Combines internal knowledge graph memory and external web query

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

Feature: First tries internal knowledge graph retrieval, falls back to external query if retrieval fails.



#### Question 3: How does Memary perform in terms of performance (latency, token overhead, accuracy)?

No specific performance benchmark data



#### Question 4: How does Memary support integration with PostgreSQL? Especially integration with pgvector/Apache AGE extension databases?

Based on provided source code, Memary currently **does not** natively support direct integration with PostgreSQL and pgvector or Apache AGE. Code shows Memary mainly supports the following graph databases: Neo4j graph database and FalkorDB graph database



#### Question 5: Does Memary support integration with LangGraph? How to integrate?

According to the provided source code, Memary currently **does not** have an implementation directly integrating with LangGraph. No traces of importing or using LangGraph in the code.



#### Question 6: Memary's API Design Reference

No website provided, none available



# Graphiti Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status:** https://help.getzep.com/graphiti/graphiti/overview |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ System based on graph structure, builds knowledge graph through Node and Edge |
| **Memory Retrieval Method**                | ✅ Supports semantic vector, text, and graph-based three search methods |
| **Performance (Latency, token, accuracy)** | ✅https://arxiv.org/abs/2501.13956                            |
| **PostgreSQL Integration (Extension)**     | ❌ Natively uses Neo4j graph database, no PostgreSQL/pgvector integration code seen |
| **Integration with langgraph**             | ✅ Provides example agent.ipynb showing integration with LangGraph, supports use as tool |
| **API Design Reference**                   | ✅https://help.getzep.com/graphiti/graphiti/quick-start       |
| **Community Activity**                     | ✅Star 9.8k github                                            |
| **Paper**                                  | ✅https://arxiv.org/abs/2501.13956                            |

Summary: Graphiti is a temporal knowledge graph framework developed by the Zep team, part of the Zep product line, used for agent memory scenarios.

Traditional RAG methods often rely on batch processing and static data aggregation, making them inefficient in the face of frequently changing data. Graphiti addresses these challenges by providing the following features:
Real-time incremental updates: No need for batch recalculation, instantly integrates new datasets.
Bi-temporal data model: Explicitly tracks event occurrence and ingestion time, allowing accurate point-in-time queries.
Efficient hybrid retrieval: Combines semantic embedding, keywords (BM25), and graph traversal for low-latency queries without relying on LLM summarization.
Custom entity definitions: Supports flexible ontology creation and developer-defined entities via simple Pydantic models.
Scalability: Efficiently manages large datasets, suitable for enterprise environments.

![graphiti intro slides](pictures/graphiti-graph-intro.gif)

![graphiti demo slides](pictures/graphiti-intro-slides-stock-2.gif)

#### Question 1: What is Graphiti's Memory Management Method? Does it use layered management?

Graphiti is essentially not a traditional memory module (like LangChain, Memary style RAM/archive memory) and does not explicitly implement the standard short-term/long-term memory hierarchy, but its graph structure has implicit hierarchical capabilities, allowing access to recent or distant memories through different traversal depths, achieving a more flexible memory layering approach.

It uses:
Neo4j graph database → Persistently stores nodes (Node), relationships (Edge), communities (Community)
Vector embedding → Enhances semantic similarity retrieval between nodes and edges
Reranker (such as cross-encoder, RRF, MMR) → Optimizes search results
In other words, Graphiti's “memory” = complete knowledge graph + real-time embedding retrieval.
Graphiti adopts a Neo4j graph database-based management model, building a multidimensional knowledge graph system, structured graph storage management.

| Module    | What is stored                                               | Feature                                    |
| --------- | ------------------------------------------------------------ | ------------------------------------------ |
| Node      | Node information (with embedding)                            | Directly stored to Neo4j, searched by uuid |
| Edge      | Relationships between nodes (with embedding)                 | Directly stored to Neo4j, searched by uuid |
| Embedding | Called when needed using `EmbedderClient` to generate, used for similarity, but not required by default |                                            |



#### Question 2: What is Graphiti's Memory Retrieval Method?

Graphiti is actually a hybrid system centered around graph database (Neo4j) + embedding vectorization + reranker combination search.

Its “memory” ≈ persistent knowledge graph, and its “retrieval” mainly relies on:
✅ Fulltext search
✅ Vector similarity search
✅ Graph traversal (graph traversal / BFS search)
✅ Multi-round reranker re-ranking (RRF, MMR, cross-encoder)

What problems does it solve?

Graphiti mainly addresses these pain points of traditional RAG:
1️⃣ Slow batch processing → switched to incremental updates, no need to recompute the entire graph.
2️⃣ Weak temporal tracking → introduced bi-temporal data model, distinguishing: event occurrence time, system ingestion time
3️⃣ Low retrieval efficiency → adopts:
    semantic embedding vector search
    keyword (BM25) keyword search
    graph traversal (graph traversal)
4️⃣ Cannot define custom entities → supports developer-defined node/edge types via Pydantic models.



#### Question 3: How does Graphiti perform in terms of performance (latency, token overhead, accuracy)?

**Table 2: LongMemEvals**

| Memory       | Model       | Score | Latency | Latency IQR | Average Context [Tokens](https://sharenet.ai/tokenization/) |
| ------------ | ----------- | ----- | ------- | ----------- | ----------------------------------------------------------- |
| Full Context | gpt-4o-mini | 55.4% | 31.3 s  | 8.76 s      | 115k                                                        |
| Zep          | gpt-4o-mini | 63.8% | 3.20 s  | 1.31 s      | 1.6k                                                        |
| Full Context | gpt-4o      | 60.2% | 28.9 s  | 6.01 s      | 115k                                                        |
| Zep          | gpt-4o      | 71.2% | 2.58 s  | 0.684 s     | 1.6k                                                        |

Analysis by question type shows that using Zep's gpt-4o-mini improves in four of six categories, with the largest improvements in complex question types: single-session preferences, multi-session, and temporal reasoning. When using gpt-4o, Zep further demonstrates improved performance in the knowledge update category, highlighting its greater effectiveness when paired with stronger models. However, additional development may be needed to improve less powerful models' understanding of Zep's temporal data.

**Table 3: LongMemEvals Question Type Breakdown**

| Question Type             | Model       | Full Context | Zep   | Increment |
| ------------------------- | ----------- | ------------ | ----- | --------- |
| Single-session preference | gpt-4o-mini | 30.0%        | 53.3% | 77.7%↑    |
| Single-session assistant  | gpt-4o-mini | 81.8%        | 75.0% | 90'6%↑    |
| Temporal reasoning        | gpt-4o-mini | 36.5%        | 54.1% | 48.2%↑    |
| Multi-session             | gpt-4o-mini | 40.6%        | 47.4% | 16.7%↑    |
| Knowledge update          | gpt-4o-mini | 76.9%        | 74.4% | 3.36%↓    |
| Single-session user       | gpt-4o-mini | 81.4%        | 92.9% | 14.1%↑    |
| Single-session preference | gpt-4o      | 20.0%        | 56.7% | 184%↑     |
| Single-session assistant  | gpt-4o      | 94.6%        | 80.4% | 17.7%↓    |
| Temporal reasoning        | gpt-4o      | 45.1%        | 62.4% | 38.4%↑    |
| Multi-session             | gpt-4o      | 44.3%        | 57.9% | 30.7%↑    |
| Knowledge update          | gpt-4o      | 78.2%        | 83.3% | 6.52%↑    |
| Single-session user       | gpt-4o      | 81.4%        | 92.9% | 14.1%↑    |

These results demonstrate Zep's ability to improve performance at scale, with the most significant improvements observed in complex and nuanced question types when used with stronger models. Latency improvements are particularly notable, with Zep reducing response time by about 90% while maintaining higher accuracy.



#### Question 4: How does Memary support integration with PostgreSQL? Especially integration with pgvector/Apache AGE extension databases?

Not mentioned as supported, no support in source code



#### Question 5: Does Graphiti support integration with LangGraph? How to integrate?

Can be integrated with LangGraph, especially within agent workflows.

| **Tool**  | **Positioning**                                              |
| --------- | ------------------------------------------------------------ |
| Graphiti  | A temporal knowledge graph backend framework for managing, updating, querying graph-structured memories and relationships (memory layer) |
| LangGraph | Part of LangChain, used to build multi-step, multi-state, branching agent flow diagrams (reasoning layer) |

Graphiti does support integration with LangGraph, and the provided example code `examples/langgraph-agent/agent.ipynb` shows the integration method:

```
# Graphiti: Graph database client for context management
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType

# LangGraph: Flowchart and dialogue management
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

# LangChain LLM integration
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

# 1. Use Graphiti to initialize graph database connection (Neo4j)
client = Graphiti(neo4j_uri, neo4j_user, neo4j_password)

# 2. Define LangChain's LLM, binding tools provided by Graphiti
llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0).bind_tools([get_shoe_data])

# 3. Define chatbot node in LangGraph, internally calls Graphiti to query user context
async def chatbot(state):
    # Graphiti query: Search graph database based on latest message
    edge_results = await client.search(
        f"{state['user_name']}: {state['messages'][-1].content}",
        center_node_uuid=state['user_node_uuid'],
        num_results=5
    )
    facts_string = '-' + '\n- '.join([edge.fact for edge in edge_results]) or 'No facts found.'

    # LangGraph + LangChain: Construct system prompt message and call LLM
    system_message = SystemMessage(content=f"User-related facts: {facts_string}")
    messages = [system_message] + state['messages']
    response = await llm.ainvoke(messages)

    # Graphiti write: Record generated result into graph database
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

# 4. Use LangGraph to build flowchart, combining LLM node and tool node
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

1. LangGraph is responsible for: managing multi-step agent flows (branching, conditions, loops), controlling calls to different modules (such as LLM, external APIs, tools)

2. Graphiti provides: storing knowledge (facts, episodes, entities) generated by agents during runtime, providing fast, rich graph query interfaces for agents to use in reasoning (e.g., looking up past interactions, querying related entities)



#### Question 6: Graphiti API Design Reference

See: https://help.getzep.com/graphiti/graphiti/quick-start





# Cognee Integration and Feature Analysis Summary

| **Focus Point**                            | **Support Status:** https://docs.cognee.ai/                  |
| ------------------------------------------ | ------------------------------------------------------------ |
| **Memory Management**                      | ✅ Memory system based on graph structure, builds knowledge graph through Node and Edge, supports flexible representation of attributes and relationships |
| **Memory Retrieval Method**                | ✅ Similarity retrieval based on vectors + graph-based retrieval |
| **Performance (Latency, token, accuracy)** | ✅ Human-LLM Correctness, DeepEval Correctness, DeepEval F1, EM — among these four indicators, Cognee (dreamify) outperforms Graphiti and mem0 |
| **PostgreSQL Integration (Extension)**     | ✅ Native support for PostgreSQL + pgvector                   |
| **Integration with langgraph**             | ❌ No explicit native integration with langgraph              |
| **API Design Reference**                   | ✅ https://docs.cognee.ai/tutorials/use-the-api               |
| **Community Activity**                     | ✅ Star 2.2k github                                           |

Cognee Architecture Overview Cognee's architecture revolves around tasks, pipelines, and typed data points, working together to transform raw data into meaningful knowledge graphs.

![Cognification Process](pictures/architecture.png)

Cognee Architecture.

![Cognee Architecture](pictures/architecture2.png)

Cognee Pipeline.

![Cognee Pipeline Flow](pictures/cognee-pipeline-flow.85364707.png)

#### 1. How does Cognee manage memory? Does it use layered/hierarchical management?

Although Cognee does not explicitly implement the standard short-term/long-term memory hierarchy, its graph structure has implicit hierarchical capabilities, allowing access to recent or distant memories through different traversal depths, achieving a more flexible memory layering approach.

**Repository file path**: `cognee/modules/graph/cognee_graph/CogneeAbstractGraph.py` and `cognee/modules/graph/cognee_graph/CogneeGraph.py`

**Repository source code**:

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
    
    # ...other methods omitted...
```

**Explanation**: Cognee adopts a graph-based memory management approach, fundamentally different from traditional sequential or hierarchical memory systems. From source code analysis, its memory management has the following characteristics:

1. **Graph-structured memory**: Implemented through the `CogneeGraph` class, memory is stored as nodes (Node) and edges (Edge), forming a knowledge graph instead of a simple linear structure. This allows for more complex semantic associations and multidimensional memory organization.

2. **Hybrid memory representation**: Combines vector embeddings and graph structure, using methods like `map_vector_distances_to_graph_nodes` to map semantic similarity in vector space onto the graph structure.

3. **Relationship-prioritized**: Edges (Edge) not only connect nodes but also contain relationship types and attributes, making memory not just about storing content but also the relationships between contents. This approach is closer to human associative networks.

4. **Extensible abstraction layer**: By separating the `CogneeAbstractGraph` abstract base class and the `CogneeGraph` implementation class, the system can adapt to different underlying databases and representation methods.

5. **Context awareness**: The graph structure naturally supports context; relevant information can be quickly retrieved via associated edges, enhancing the contextual understanding of memory.



#### 2. Cognee Memory Retrieval Method

Mainly vector retrieval and graph structure retrieval.

**Repository file path**: `cognee/modules/retrieval` 

```
await vector_engine.search
...
graph_engine = await get_graph_engine()
exact_node = await graph_engine.extract_node(node_id)
```



#### 3. Performance Indicators

**Question**: How does Cognee perform in terms of latency, token cost, accuracy? What measurable indicators are available?

![metrics_comparison.png](pictures/metrics_comparison.png)

![cognee_comparison.png](pictures/cognee_comparison.png)

Human-LLM Correctness: This is a hybrid evaluation assisted by human + LLM, i.e., overall correctness judged by humans (or LLM reviewers with human verification). It is usually more tolerant, allowing different expressions, allowing reasonable reasoning, rather than rigid matching. [0–1 (the closer to 1 the better)]

DeepEval Correctness: Uses automated evaluation tools (DeepEval) to determine whether the system's answer is "generally" correct. It leans more toward semantic correctness, i.e., whether the answer captures the main idea, even if not matching word-for-word. [0–1 (the closer to 1 the better)]

DeepEval F1: F1 score is a traditional composite metric in information retrieval, combining: Precision: Of what you answered, how much was correct? Recall: Of the reference answer, how much did you cover? [0–1 (the closer to 1, the more comprehensive and accurate)]

EM (Exact Match): Exact Match means strict "word-for-word exact match," i.e., the predicted answer and the reference answer are completely identical.
Even one extra space, one missing word, or one synonym counts as non-match. [0–1 (the closer to 1, the more exact the match)]



Cognee's performance tests show that its graph-based memory management achieves a good balance between accuracy, coverage, and efficiency, especially excelling in Human-LLM scores, indicating its generated results align more with human judgment standards.



#### 4. How to integrate with PostgreSQL? Does it support pgvector extension?

**Repository file path**: `cognee/infrastructure/databases/vector/pgvector/PGVectorAdapter.py`

**Repository source code**:

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

        if relational_db.engine.dialect.name == "postgresql":
            self.engine = relational_db.engine
            self.sessionmaker = relational_db.sessionmaker
        else:
            self.engine = create_async_engine(self.db_uri)
            self.sessionmaker = async_sessionmaker(bind=self.engine, expire_on_commit=False)

        from pgvector.sqlalchemy import Vector
        self.Vector = Vector
```

**Explanation**: Cognee provides comprehensive support for PostgreSQL and pgvector, specifically:

1. **Vector similarity query**: The `search` method uses `cosine_distance` for similarity calculation, which is the core function of pgvector, supporting efficient Approximate Nearest Neighbor (ANN) search.
2. **Asynchronous operations**: All database operations are executed asynchronously using `async/await`, combined with `async_sessionmaker` to improve system throughput.
3. **Flexible query mechanism**: Supports querying via text (`query_text`) or directly supplying vectors (`query_vector`), meeting different scenario needs.



#### 5. Does it support integration with langgraph?

Cognee does not explicitly indicate native integration with langgraph.



#### 6. API Design Reference

#### Overview (https://docs.cognee.ai/tutorials/use-the-api)

This tutorial demonstrates how to interact with Cognee's API service using Docker and cURL. The API allows you to:

- **Set up** your environment and configure API key
- **Start** the API service (via Docker)
- **Authenticate** to get access token
- **Upload** a document (in this case, the text file of Alice in Wonderland)
- **Process** the document through Cognee's pipeline
- **Search** the processed content using natural language queries

#### Step 1: Environment Setup

First, create a .env file containing your API key. This key is used to support Cognee's underlying Language Model (LLM).

```
echo 'LLM_API_KEY="YOUR-KEY"' > .env
```

*This step ensures Cognee can access your LLM credentials.*

#### Step 2: Start the API Service

Pull and run Cognee's Docker container:

```
docker pull cognee/cognee:main
docker run -d -p 8000:8000 --name cognee_container -v $(pwd)/.env:/app/.env cognee/cognee:main
```

*This command pulls the latest Cognee image and starts it, mounting your environment file.*

#### Step 3: Authenticate

Use the default account and password to get an access token:

```
access_token=$(curl --location 'http://127.0.0.1:8000/api/v1/auth/login'   --form 'username="default_user@example.com"'   --form 'password="default_password"' | sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p')

echo "Access Token: $access_token"
```

*The obtained access token will be used for authentication in all subsequent API requests.*

#### Step 4: Upload Document

Upload Alice in Wonderland to a dataset named test-dataset:

```
curl -s https://raw.githubusercontent.com/topoteretes/cognee/main/examples/data/alice_in_wonderland.txt | curl --location 'http://127.0.0.1:8000/api/v1/add'   --header "Authorization: Bearer $access_token"   --form 'data=@-'   --form 'datasetName="test-dataset"'
```

*This uploads the document and associates it with the specified dataset name.*

#### Step 5: Process Document

Process the newly uploaded dataset:

```
curl --location 'http://127.0.0.1:8000/api/v1/cognify' --header 'Content-Type: application/json' --header "Authorization: Bearer $access_token" --data '{
 "datasets": ["test-dataset"]
}'
```

*This step sends the document into Cognee's processing pipeline to prepare it for subsequent queries.*

#### Step 6: Execute Search Queries

You can now query the processed dataset. Here are three example queries using GRAPH_COMPLETION search type:

#### Query 1: List Important Characters

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "List me all the important characters in Alice in Wonderland."
}'
```

#### Query 2: How Did Alice Enter Wonderland?

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "How did Alice end up in Wonderland?"
}'
```

#### Query 3: Describe Alice's Personality

```
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "GRAPH_COMPLETION",
 "query": "Tell me about Alice'\''s personality."
}'
```

#### Step 7: Delete Document

Let's remove the uploaded dataset:

```
curl -s https://raw.githubusercontent.com/topoteretes/cognee/main/examples/data/alice_in_wonderland.txt | \
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/delete' \
  --header "Authorization: Bearer $access_token" \
  --form 'data=@-' \
  --form 'datasetName="test-dataset"' \
  --form 'mode="hard"'
}'
```