# Preface
The explosive growth of generative AI has made technology selection a primary challenge for developers. Almost every day, new frameworks, tools, or technologies emerge. Whether you're an individual developer or part of an enterprise team, building innovative applications with large language models (LLMs) raises a critical question: "Which framework is best suited for my use case?" This article provides a deep, practical comparison of five mainstream AI Agent frameworks—LangGraph, LlamaIndex, PydanticAI, AutoGen, and CrewAI—from a developer's perspective, across multiple dimensions, to serve as a hands-on reference. **Note that this article focuses primarily on evaluating these frameworks' performance in building non-agentic AI workflows.**

## Why Do We Need LLM Frameworks?
LLM development frameworks are software platforms designed to simplify the creation, deployment, and management of AI applications (e.g., Agents, Workflows, RAG). These frameworks provide pre-built components, abstracted interfaces, and development tools to help developers efficiently build complex AI systems. Through standardized development paradigms and modular architectures, LLM frameworks allow developers to focus on the unique logic and innovation of their applications without reinventing the wheel. Whether for rapid prototyping or production-grade deployment, choosing the right LLM framework for your use case can significantly reduce development barriers and time costs.

## The Core Value of Workflows
Workflows are event-driven, step-based methods for controlling the execution flow of applications. As generative AI applications become increasingly complex, managing data flows and controlling application execution becomes more challenging. Workflows break tasks into modular sub-steps, offering greater flexibility and maintainability. This is particularly valuable in scenarios involving multi-agent collaboration or cross-system interactions, significantly improving development efficiency and system robustness.

## Agentic vs. Non-Agentic Workflows
AI workflows can be categorized into non-agentic and agentic based on their level of autonomy:

+ **Non-Agentic Workflows**: Rely on the input-output capabilities of LLMs to execute predefined, deterministic steps. For example, a text summarization task might involve: input long text → LLM generates summary → output result. Such workflows are suitable for well-defined scenarios like content generation or data processing but lack dynamic decision-making or environmental adaptability.
+ **Agentic Workflows**: Dynamically executed by AI agents with reasoning, tool-calling, and contextual memory capabilities. Agents can autonomously gather information, call external APIs, or make decisions within their authorized scope. For instance, an intelligent customer service agent can analyze user intent, query a CRM system, and generate personalized responses, dynamically handling complex interactions. Agentic workflows are particularly suited for multi-step, interactive, or cross-system scenarios due to their responsiveness and adaptability.

## How to Choose?
We recommend developers consider the following three aspects to evaluate their actual development needs:

### Can the Task Be Broken Down into Clear Steps?
+ **Yes**: Consider choosing a **non-agentic workflow** and breaking it into a Workflow.  
If the task can be decomposed into clear steps (e.g., data extraction → analysis → report generation), a non-agentic workflow is the most efficient choice. Each step acts like a pipeline, stable and controllable, suitable for rule-based scenarios like content generation or data processing.  
**When to Break Down?** When the task has reliable intermediate checkpoints (similar to a "Process Reward Model" PRM), such as verifiable outputs at each step, it’s ideal to break it into a Workflow. This allows inserting validation tools to catch errors and retry if needed, reducing the risk of mistakes.  
**Example**: Generating financial reports, broken into "fetch data → calculate → format," with each step verifiable to ensure accuracy.
+ **No**: Consider choosing an **agentic workflow** and relying on model intelligence.  
If the task is dynamic and variable (e.g., an intelligent customer service agent needing to understand users in real-time and call tools), an agentic workflow’s autonomous reasoning and tool-calling capabilities are more suitable. Agents act like intelligent assistants, dynamically planning paths.  
**When to Rely on the Model?** If intermediate processes are hard to verify or breaking down into a Workflow is too complex and costly, rely on the model. You can use off-the-shelf models for agents, fine-tune with SFT/RFT for specific scenarios, or even train with synthetic data for deeper customization.  
**Example**: Real-time fault diagnosis requiring dynamic log checking and API calls, where agents can flexibly adapt.

### Are Stability and Interpretability Requirements High?
+ **High**: Consider choosing a **non-agentic workflow** with task decomposition.  
In fields like finance or healthcare, high stability and controllability are critical. A Workflow’s fixed steps reduce risks from model randomness.  
**Interpretability Needs**: If the business requires transparent intermediate results (e.g., for user display or manual intervention), a Workflow’s step-by-step outputs are easier to inspect and control, even if this sacrifices some performance.  
**Example**: Medical data processing, with steps broken down and intermediate results shown to meet regulatory and trust requirements.
+ **Low**: Consider choosing an **agentic workflow** and relying on the model.  
For prototyping or interactive scenarios (e.g., intelligent assistants), some uncertainty is acceptable, and an agent’s flexibility is ideal for rapid iteration. In the long term, tasks without reliable checkpoints will increasingly rely on model intelligence.  
**Fusion or Training?** For fusion, using off-the-shelf models for agents is cost-effective; for niche scenarios (e.g., highly open-ended tasks where existing models underperform), consider fine-tuning or custom training.  
**Example**: Experimental conversational systems, where agents run directly and are fine-tuned if performance is inadequate.

### Should You Build a Workflow Now or Wait for Model Advancements?
+ **Build a Workflow Now**:  
If the task can be broken down with reliable checkpoints, build a Workflow ASAP to validate its effectiveness. Workflows are ideal for rapid deployment, especially in new scenario validation, with manageable development costs.  
**Intuition Pump**: Ask yourself, “Will this Workflow be obsolete in six months due to new models?” If 80% of the effort will be wasted, consider pausing and assessing model development speed.
+ **Wait for Models or Rely on Agents**:  
If the Workflow is too complex after decomposition or current models perform poorly (e.g., in open-ended scenarios), start with an agent-based baseline and monitor model advancements. In the long term, tasks without checkpoints will increasingly be solved by model fusion.  
**Example**: Highly complex tasks (e.g., fully automated code generation), where current models fall short, can start with agents and wait for stronger models.

> 💡 Tips:
> + **Hybrid Strategy**: Complex tasks often combine both—Workflows for deterministic subtasks and Agents for dynamic decision-making.
> + **Don’t Over-Optimize Proven Solutions**: Stick with validated Product-Market Fit (PMF) solutions unless there’s a strong need for change. With rapid tech iteration, reassess every 0.5–1 year.
> + **Workflows Won’t Be Obsolete**: They remain efficient for decomposable, high-stability scenarios, especially when interpretability and intermediate validation are critical.

# Five Mainstream Agent Development Frameworks
## Open-Source Status and Community Activity
_Table 1: Overview of Community Activity for Mainstream AI Agent Frameworks_

| Framework | Stars | Commits | Issues | Forks | PR Creators | Primary Language |
| --- | --- | --- | --- | --- | --- | --- |
| **LangGraph** | 11,353 | 9,624 | 646 | 2,022 | 259 | Python |
| **LlamaIndex** | 39,568 | 14,044 | 8,826 | 5,881 | 1,603 | Python |
| **PydanticAI** | 8,218 | 2,303 | 724 | 798 | 159 | Python |
| **AutoGen** | 41,610 | 14,143 | 2,667 | 6,624 | 571 | Python |
| **CrewAI** | 29,091 | 5,245 | 1,290 | 4,129 | 364 | Python |

_Table 2: Community Activity for Mainstream AI Agent Frameworks in the Last 28 Days_

| Framework | Stars Growth | PR (Open) | PR (Merged) | Issues (Open) | Issues (Closed) | Commits |
| --- | --- | --- | --- | --- | --- | --- |
| **LangGraph** | 1,018 | 157 | 141 | 49 | 45 | 630 |
| **LlamaIndex** | 657 | 100 | 85 | 85 | 382 | 202 |
| **PydanticAI** | 969 | 99 | 67 | 119 | 102 | 313 |
| **AutoGen** | 1,233 | 103 | 88 | 54 | 65 | 167 |
| **CrewAI** | 1,265 | 113 | 48 | 70 | 69 | 393 |

## Evaluation Overview
**Key Conclusions:**

+ **LangGraph**: Ideal for building **highly controllable, state-clear complex agent systems**, such as conversational bots or code analyzers. Its graph-based workflow architecture is perfect for enterprise-grade scenarios requiring clear state transitions, error recovery, and task backtracking.
+ **LlamaIndex**:  
Best for **data-driven Q&A systems or multi-round document processing tasks**, such as internal knowledge base Q&A or enterprise search. Its strong data awareness and document structure handling make it a mature choice for RAG applications.
+ **PydanticAI**:  
Perfect for **AI services requiring strict, safe, and stable outputs**, especially when integrating LLMs into backend systems. Its precise input/output format control is ideal for high-reliability, type-validated scenarios, seamlessly integrating with APIs or microservices.
+ **AutoGen**:  
Excels in **rapid prototyping, dynamic collaboration, and multi-agent message interactions**, such as research-oriented conversational tools or code suggestion systems. Its flexibility and out-of-the-box usability make it suitable for exploratory projects, innovative experiments, or building multi-agent systems with conversational memory and reasoning chains.
+ **CrewAI**:  
Best for building **multi-role collaboration and business process automation systems**, such as content team orchestration or cross-department workflow management. Its role-based division and process-driven approach naturally map to real-world team collaboration and task execution logic.

Below is a comprehensive evaluation of the five frameworks across technical features, control capabilities, state persistence, observability, and deployment convenience:

| Feature / Framework | **LangGraph** | **LlamaIndex** | **PydanticAI** | **AutoGen** | **CrewAI** |
| --- | --- | --- | --- | --- | --- |
| **Technical Features** | Stateful graph orchestration framework supporting complex control flows and multi-agent systems. Uses DAG architecture with finely defined nodes and edges. Supports state persistence, error recovery, and streaming output. | Event-driven workflow model simplifying data flow. Supports document retrieval and processing with a rich toolchain. | Built on Pydantic, emphasizing type safety and structured output. Lightweight design, ideal for backend integration. | Multi-agent collaboration framework based on conversation and messaging. Supports async execution and code generation. | Focused on multi-role collaboration with a Crew + Flow model, supporting concurrency, caching, and task delegation. |
| **Use Cases** | Complex applications requiring high controllability and observability, such as intelligent assistants, code generation, or business processes. | Data-driven Q&A and research tasks, such as knowledge base retrieval or Q&A generation. | Scenarios emphasizing safety and structure, ideal for data processing, structured generation, and backend API integration. | Conversational, code-writing, or research discussion tasks; suitable for dynamic multi-agent orchestration. | Workflow automation and multi-agent task collaboration, such as content production or approval workflows. |
| **State Management** | Built-in state mechanism with TypedDict shared between nodes; supports state reducers and checkpoints. | Passes global context via Context, simplifying state sharing and updates. | Uses dependency injection for state passing; agent inputs/outputs defined via Pydantic models. | State shared via messages; users manage state storage or contextual memory. | Flow provides built-in state support; Crews retain context for multi-round tasks. |
| **Granular Control** | Supports branching, loops, parallelism, and conditional jumps. Send API enables dynamic task scheduling. | Supports branching and loop events; sub-workflows and nested workflows can build complex execution graphs. | Supports task organization via Python control flows; concurrency requires manual implementation. | Multi-agent parallelism, topic subscription, and message patterns, suitable for unstructured interactions. | Uses logical conditions for branching and synchronization; supports task delegation and multi-path collaboration. |
| **Async & Concurrency** | Supports async node execution, compatible with asyncio; extensible to distributed systems with Ray. | Fully async model, supporting `await`, async event triggers, and parallel steps. | Natively supports async functions and concurrent execution; async validation and call compatibility. | Architecture natively supports asyncio; agent tasks can run concurrently or asynchronously. | Supports async execution and concurrent Flow steps, maximizing multi-core resource utilization. |
| **Distributed Support** | Integrates with Ray for distributed deployment; enterprise edition includes scheduling and clustering. | Supports distributed execution with Ray; multi-node task concurrency requires user management. | No built-in distributed support; can integrate with Celery, FastAPI, etc., for horizontal scaling. | Supports local and remote deployment with multi-process and distributed mechanisms. | Enterprise edition supports cluster deployment and load balancing; open-source version requires manual scaling. |
| **Streaming Output** | Multiple modes: per-node updates, token-by-token, or structured result streams; suitable for real-time frontend interactions. | Supports step-level and token-level event streams, ideal for dynamic UI feedback. | Supports generation with validation, suitable for progressive LLM output checking. | Supports sentence/token-level output, enabling real-time generation visibility. | Supports task callback listeners for indirect streaming interactions. |
| **Persistence Mechanism** | Supports local and remote database persistence (e.g., Postgres); thread-level/cross-thread state saving. | Requires manual integration with vector databases or caching systems for state persistence. | No persistence layer; developers manage data storage. | Application-layer persistence with external databases for session recording. | Built-in Memory module automatically caches task states; supports cross-task context. |
| **Observability** | Integrates with LangSmith for call chain and token consumption tracking; requires custom monitoring. | Supports logging and verbose debugging; users build monitoring logic. | Natively integrates with Logfire for visualized debugging and log tracking. | Can integrate with logging systems for behavior analysis; no dedicated visualization panel. | Provides control plane views showing each Crew’s calls and consumption statistics. |
| **Learning Curve** | Graph models and reducer mechanisms are slightly challenging for beginners; detailed documentation. | Moderate difficulty, requiring understanding of event flows and workflow orchestration; supports visualization. | Easy to learn for Python developers; emphasizes engineering practices. | Multi-module collaboration is complex, requiring understanding of Agent patterns and extensions. | Clear but new model; requires familiarity with Crew/Flow mechanisms and lifecycle. |
| **Community Activity** | Active community within the LangChain ecosystem; used in production by multiple companies. | Large user base, rich community documentation; actively maintained with frequent updates. | Emerging framework backed by Pydantic community; rapid growth. | Large community support, comprehensive documentation, high GitHub activity. | High star count, rich documentation and tutorials, strong enterprise support. |
| **LLM Support** | Supports mainstream models like OpenAI, Anthropic, Mistral, Llama; customizable. | Supports all LangChain-compatible LLMs; customizable tool-calling. | Supports OpenAI, Claude, Gemini, DeepSeek, Cohere, etc. | Supports mainstream API providers (OpenAI, Azure OpenAI, Hugging Face, etc.). | Connects to any API-based LLM, highly flexible integration. |
| **Framework Compatibility** | Highly compatible with LangChain/LangSmith/MemoryStore ecosystem components. | Integrates with vector databases and toolchains (llama_hub). | Tightly integrates with FastAPI, databases, and message queues for backend services. | Python/.NET compatible; Studio visualization supports multi-platform integration. | Compatible with Python’s native ecosystem, easy integration with logging, caching, and data platforms. |
| **DevOps Deployment** | Supports local deployment or platform version; Docker/K8s compatible for CI/CD integration. | Supports containerized deployment, no SaaS support; requires manual production setup. | Easily embedded in servers; supports REST API exposure and containerized deployment. | Deployed as Python packages; Studio UI supports server hosting. | Enterprise edition supports centralized management and cloud deployment; open-source version supports scripted auto-deployment. |

---

# LangGraph
## 🔗 Basic Introduction
LangGraph is an extension library built on top of LangChain, designed to enhance the capabilities of LangChain Expression Language (LCEL). It introduces graph structures (e.g., Directed Acyclic Graphs, DAGs), enabling developers to clearly define and manage complex workflows, including loops, conditional branching, and multi-agent collaboration. While LangGraph is more complex than LCEL, it offers superior process control and state management, making it suitable for building highly controllable and scalable AI applications.

+ **State Graph Modeling**: Defines application flows using nodes and edges for precise process control.
+ **Supports Loops and Conditional Flows**: Dynamically determines execution paths based on state, suitable for complex conversations and task flows.
+ **Multi-Agent Collaboration**: Coordinates multiple Chains, Agents, Tools, etc., to collaboratively complete tasks.
+ **State Persistence**: Automatically saves and manages state, supporting pause and resume for long-running conversations.

Unlike LangChain’s linear flows, **LangGraph is a graph-based framework specifically designed for complex, stateful workflows**.

LangGraph organizes workflows as **graphs**, with the following key features:

+ **Node**: Represents a step in the workflow, such as an LLM call, API request, or tool execution.
+ **Edge** and **Conditional Edge**: Define the flow of information between nodes. Conditional edges allow dynamic branching based on state logic.
+ **State**: A developer-defined TypedDict object that records the current execution graph’s contextual information. LangGraph automatically updates the state after each node execution, ensuring continuity and context awareness.
+ **Cyclical Graphs**: Supports loops for task retries, result feedback, and state backtracking, enabling advanced control flows.

> _Official Reference_: [LangGraph Documentation](https://langchain-ai.github.io/langgraph/tutorials/introduction/), [LangGraph GitHub](https://github.com/langchain-ai/langgraph).
>

## 🔗 Framework Evaluation
### Usage Instructions
#### 📌 Simple Sequential Chain:
For tasks that can be cleanly broken into fixed subtasks, LangGraph can implement a simple sequential chain:

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

### State Management
#### 📌 LangGraph’s StateGraph has the following key components:
+ **Node**: Represents a step in the workflow, such as an LLM call, API request, or tool execution.
+ **Edge** and **Conditional Edge**: Define the flow of information between nodes. Conditional edges allow dynamic branching based on state logic.
+ **State**: A developer-defined TypedDict object that records the current execution graph’s contextual information. The state is passed between nodes, and each node updates it based on its defined logic. State can be defined using `TypedDict`, `Pydantic` models, or `dataclass`.

> 💡 By default, `StateGraph` operates with a single state schema, and all nodes communicate using this schema. However, you can define different `InputState` and `OutputState` schemas for `StateGraph`.
>

#### 📌 Each key in the State can have its own reducer function, controlling how updates from nodes are applied.
+ If no reducer is specified, updates to a key overwrite it by default. For example, by assigning the `append_chunks` reducer to the `parsed_chunks` field, new text chunks returned by a node are **automatically accumulated** in the current State, eliminating the need for nodes to manually manage merge logic, ensuring **data processing consistency**.

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

### Granular Control
#### 📌 Basic Usage
LangGraph enables highly flexible control over node execution granularity. It natively supports parallel execution of multiple nodes, as well as **result aggregation** (fan-in) and **conditional branching**. Here are some basic usage patterns:

+ **Fan-out**: A node can trigger multiple child nodes concurrently.
+ **Fan-in**: All child nodes complete before proceeding to the next node.
+ **Reducer**: Merges updates to the same State field from multiple concurrent nodes (e.g., accumulating lists).
+ **Conditional Branch**: Dynamically selects paths based on conditions in the State. Loops can include conditional edges with specified termination conditions. (You can also use a `Command` object to control node routing without explicitly adding edges.)
+ **Loop & Termination**: Supports loops in the graph with conditional edges for termination, and a `recursion_limit` to prevent infinite loops, raising a `GraphRecursionError`.

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
    return {"body_chunks": ["Chinese paragraph"]}

def extract_body_english(state: State):
    print("Extracting English body text...")
    return {"body_chunks": ["English paragraph"]}

def extract_table(state: State):
    print("Extracting table of contents...")
    return {"table_chunks": ["Table of contents"]}

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

> 💡 Notes:
>
> 1. **Error Handling**: After fan-out, if a node fails, the framework lacks a mechanism to handle exceptions, potentially interrupting the entire pipeline.
> 2. Practical applications may require prioritizing scheduling.
>

#### 📌 Parallel Execution
**Super-Step Concept**

LangGraph’s execution model is based on **super-steps**. A super-step represents one iteration in the graph, where all concurrently executing nodes belong to the same super-step, while sequentially executing nodes are assigned to different super-steps. When the graph runs, all nodes start in an **inactive** state. A node becomes **active** when its incoming edge receives a new message (state), runs its function, and responds with updates. At the end of each super-step, nodes **halt** by marking themselves **inactive**, signaling no further incoming messages. The graph terminates when all nodes are **inactive** and no messages are in transit.

+ **Parallel Execution**: When multiple nodes execute in the same super-step, they run concurrently. For example, if node `a` triggers nodes `b` and `c`, they execute in parallel.
+ **Sequential Execution**: When a node depends on the completion of multiple other nodes, it waits for their results. For example, if node `d` depends on nodes `b2` and `c`, `d` executes only after both `b2` and `c` complete.

> 💡 For the above case, where `b` and `c` are in the same super-step, use `add_edge(["b_2", "c"], "d")` to ensure node `d` runs only after both `b_2` and `c` complete. Adding separate edges would cause `d` to execute twice.
>

**Map-Reduce Parallelism**

In practice, we often need to process a batch of subtasks (e.g., text chunks, document sections, images) in parallel and merge results, such as summarizing multiple parts of a large document (each text chunk → summary). This naturally fits the **Map-Reduce** pattern. However, two challenges arise:

+ The number of text chunks to process is unknown at design time (dynamic quantity).
+ Each child node should process only its own chunk, not share the entire State.

LangGraph’s `Send` API addresses this by:

+ **Dynamically creating child node tasks** at runtime.
+ **Distributing distinct States** to each child task.

```python
Send("target_node_name", {"key": value})   
```

Where:

+ `"target_node_name"` is the target node.
+ `{"key": value}` is the new, task-specific input State.

This enables flexible handling of **dynamic quantities + independent States**, as shown below:

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

#### 📌 Node Retry Strategy
LangGraph introduces node-level **RetryPolicy**. You can pass a `RetryPolicy` object when calling `add_node`.

```python
from langgraph.pregel import RetryPolicy

RetryPolicy()
RetryPolicy(initial_interval=0.5, backoff_factor=2.0, max_interval=128.0, max_attempts=3, jitter=True, retry_on=<function default_retry_on at 0x78b964b89940>)

# Define a new graph
builder = StateGraph(AgentState)
builder.add_node("model", call_model, retry=RetryPolicy(max_attempts=5))
```

#### 📌 Returning State Before Reaching Recursion Limit
In complex workflows, graphs may hit recursion limits (`GraphRecursionError`) due to loops or deep nesting. By default, exceeding the limit raises an error, degrading user experience. LangGraph introduces the `RemainingSteps` mechanism.

By annotating the **State** type with **RemainingSteps**, the framework automatically tracks recursion depth. LangGraph creates and decrements `remaining_steps` for each graph execution, monitoring the current step and remaining executions.

```python
class State(TypedDict):
    value: str
    action_result: str
    remaining_steps: RemainingSteps
```

### Asynchronous Execution
Using asynchronous execution can significantly improve performance when running I/O-bound code concurrently (e.g., making concurrent API requests to chat model providers).

To switch from synchronous to asynchronous:

+ Change node functions from `def` to `async def`.
+ Use `await` correctly within nodes.

Since many LangChain objects follow the Runnable protocol, and synchronous methods typically have asynchronous counterparts, migration is usually straightforward.

```python
async def call_model(state: State):
    messages = state["messages"]
    response = await model.ainvoke(messages)
    return {"messages": [response]}
    
from langchain_core.messages import HumanMessage
async def main():
    inputs = {"messages": [HumanMessage(content="What are the keywords in this text?")]}
    # Streaming Node Output
    async for output in graph.astream(inputs, stream_mode="updates"):
        # stream_mode="updates" yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print(value["messages"][-1].pretty_print())
```

### Distributed Support
LangGraph supports distributing agent tasks across multiple compute nodes or threads for concurrent execution.

For example, integrating with Ray is straightforward:

+ **Encapsulate StateGraph in an Actor class**.
+ **Register as an Actor with `@ray.remote`**.
+ **In the main program (Driver), instantiate with `GraphActor.remote()`**.
+ **Ray schedules worker processes in the cluster to run the Actor instance**.
+ **Asynchronously call Actor methods remotely**, with Actors executing **independently, concurrently, and distributedly**.

Code example:

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

# Create and run multiple GraphActors
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

### Streaming Output
#### 📌 Different Streaming Output Modes
Streaming is critical for improving the responsiveness of LLM-based applications, particularly in reducing latency. LangGraph supports multiple streaming output modes, including:

1. **values**: Emits all state values after each step.
2. **updates**: Emits only the node name and updates for each step.
3. **custom**: Uses StreamWriter for custom data output.
4. **messages**: Emits LLM messages and metadata token by token.
5. **debug**: Emits detailed debugging information.

Using `graph.stream(..., stream_mode=<stream_mode>)`, you can stream outputs during graph execution.

```python
# sync
for chunk in graph.stream(inputs, stream_mode=["updates", "custom"]):
    print(chunk)
    
# async
async for chunk in graph.astream(inputs, stream_mode=["updates", "custom"]):
    print(chunk)
```

#### 📌 Async Streaming Output Implementation
The `astream` method returns an asynchronous iterator (`AsyncIterator`) that progressively outputs data during graph execution. Key components in `astream` include `AsyncQueue` and `StreamProtocol`, leveraging `async for` and the `asyncio` library for asynchronous streaming.

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

The `AsyncQueue` is a thread-safe asynchronous queue for storing stream data. `stream_put` is an async method that pushes data into the queue using `aioloop.call_soon_threadsafe` to ensure asynchronous delivery.

```python
stream = AsyncQueue()
aioloop = asyncio.get_running_loop()
stream_put = cast(
    Callable[[StreamChunk], None],
    partial(aioloop.call_soon_threadsafe, stream.put_nowait),
)
```

#### 📌 Core Steps of Async Streaming:
+ Data is progressively added to the `stream` queue.
+ The `output()` function asynchronously retrieves data from the `stream` queue and yields it.
+ `async for` fetches these results asynchronously until the `stream` queue is empty.

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

#### 📌 LLM Streaming Output:
Below is an example of a single node with two LLM calls:

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
        # We can use the streamed metadata and filter events using the tags we've added to the LLMs previously
        # if msg.content and "summary" in metadata.get("tags", []):
        #     print(msg.content, end="|", flush=True)

if __name__ == "__main__":
    asyncio.run(main())

############ Result #############
# Generating summary...
# Artificial| intelligence| (AI) involves| machines simulating human| intelligence processes. Key| applications of AI include| expert systems, natural| language processing, speech| recognition, and machine| vision.|

# Extracting keywords...
# Here| are| the| important keywords extracted from| the text:

# -| Artificial intelligence (AI|)  
# - Simulation|  
# - Human intelligence|
# ...
```

### Persistence
#### 📌 Thread-Level Persistence
Many AI applications require memory to share context across interactions. In LangGraph, thread-level persistence can be added to any StateGraph by including a `checkpointer` during graph compilation to maintain its state.

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
# ================================== AI Message ==================================
# Hi Alen! Nice to meet you. How can I assist you today? 😊
# ================================ Human Message =================================
# what's my name?
# ================================== AI Message ==================================
# Your name is **Alen**! 😊 Did I get it right?
# ================================ Human Message =================================
# what's my name?
# ================================== AI Message ==================================
# I don't have access to specific personal information about you, so I don't know your name. 😊
```

#### 📌 Cross-Thread Persistence
LangGraph also supports persisting data across **multiple threads**. The core is using the `Store` interface to store shared data across threads (e.g., user preferences). A `namespace` (e.g., `("memories", user_id)`) isolates different users’ memories.

#### 📌 Using Postgres Checkpointer for Persistence
```python
from langgraph.graph import StateGraph

builder = StateGraph(....)
# ... define the graph
checkpointer = # postgres checkpointer 
graph = builder.compile(checkpointer=checkpointer)
```

> 💡 You need to run `.setup()` on the checkpointer once to initialize the database before use.
>

**Synchronous Connection**

Synchronous connections execute operations in a blocking manner, meaning each operation waits for completion before proceeding. Below are three common approaches:

+ With a connection
+ With a connection pool
+ With a connection string

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
    res = graph.invoke({"messages": [("human", "What's the language of this paper?")]}, config)

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
    res = graph.invoke({"messages": [("human", "What's the language of this paper?")]}, config)
    checkpoint = checkpointer.get(config)

# ===========With a connection string============
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "3"}}
    res = graph.invoke({"messages": [("human", "What's the language of this paper?")]}, config)

    checkpoint_tuples = list(checkpointer.list(config))
```

**Asynchronous Connection**

Asynchronous connections enable non-blocking database operations, allowing other parts of the application to continue running while waiting for database operations to complete. This is particularly useful for high-concurrency scenarios or I/O-bound operations.

```python
from psycopg import AsyncConnection

async with await AsyncConnection.connect(DB_URI, **connection_kwargs) as conn:
    checkpointer = AsyncPostgresSaver(conn)
    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "5"}}
    res = await graph.ainvoke(
        {"messages": [("human", "What's the weather in NYC?")]}, config
    )
    checkpoint_tuple = await checkpointer.aget_tuple(config)
```

### Logging & Observability
LangSmith is specifically designed for **monitoring and debugging LLM applications**, offering real-time tracking of workflows and model performance. LangSmith provides **LLM-optimized observability features**, ideal for development, testing, and production environments. LangSmith is framework-agnostic—it works with LangChain, LangGraph, or standalone. For LangGraph, integrating LangSmith enables **tracking of the entire pipeline**, facilitating debugging and monitoring.

---

## Basic Introduction
AutoGen is an open-source framework developed by Microsoft, designed to solve complex tasks through collaborative AI agents. **AutoGen** focuses on **conversational agents**, allowing developers to extend simple agents with customizable components or combine multiple agents into more powerful **agent workflows**. Its modular design simplifies implementation, offering great convenience to developers.

Core components include:

+ **AutoGen Studio**: A no-code development tool with a visual interface for rapidly building and debugging multi-agent systems.
+ **autogen-agentchat**: A Python library for building conversational single-agent and multi-agent applications.
+ **autogen-core**: An event-driven programming framework for building scalable multi-agent AI systems.

AutoGen’s design goal is to simplify the orchestration, automation, and optimization of complex LLM workflows, maximizing LLM performance while overcoming their limitations. If you aim to build a system with multiple collaborating AI agents, AutoGen is a strong candidate.

---

# LlamaIndex
## Basic Introduction
LlamaIndex is a data framework for LLM applications, designed to ingest, structure, and access private or domain-specific data, specializing in providing external data access for large language models (LLMs).

Unlike traditional frameworks that organize workflows using **Directed Acyclic Graphs (DAGs)**, LlamaIndex introduces a more natural and expressive **Workflow mechanism**, addressing challenges in complex AI workflows, such as loops, branches, and dynamic data passing. Its key advantages include:

+ **More Intuitive Control Flow**: Loops and branches are first-class citizens in Workflows, eliminating the need to simulate them implicitly through edges, greatly improving readability and maintainability.
+ **Simplified Data Flow Management**: Data passing between nodes is clearer, reducing the complexity of handling defaults, optional parameters, and data alignment common in DAGs.
+ **Natural Developer Experience**: Aligns with how developers think when building complex, dynamic AI applications (e.g., Agent systems, interactive reasoning chains), without needing to align with low-level graph structures.

> _Official Reference_: [LlamaIndex Documentation](https://docs.llamaindex.ai/), [LlamaIndex GitHub](https://github.com/run-llama/llama_index).
>

## Framework Evaluation
### Usage Instructions
In the **LlamaIndex** framework, a workflow (`Workflow`) consists of multiple steps (`step`). Each step accepts one or more **events (Event)** and generates a new event. Workflows typically start with a special **StartEvent** and end with a **StopEvent**.

#### 📌 Core Concepts:
1. `**StartEvent**`: The event that initiates the workflow, typically the input for the first step.
2. `**StopEvent**`: The event that terminates the workflow, returning the final result.
3. `**Event**`: All events (including StartEvent and StopEvent) must inherit from the `Event` class. Developers can define custom events to pass data between steps.

#### 📌 Step Definition:
+ `**@step**` Decorator: Marks a method as a step in the workflow.
+ Each step accepts an event as input and returns an event as output.

#### 📌 Workflow Execution:
1. Create a workflow instance.
2. Call the `run()` method to start the workflow with an initial event.
3. Steps execute sequentially, each generating a new event based on the previous step’s output.
4. By default, workflows are asynchronous, so use `await` to retrieve the result of the `run` command.

```python
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
)
import asyncio

# Define event classes
class PDFLoadedEvent(Event):
    pdf_content: str

class ParsedTextEvent(Event):
    parsed_text: str

class SummarizedTextEvent(Event):
    summary: str

class DatabaseStoredEvent(Event):
    result: str

# Create workflow
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

#### 📌 Built-in Visualization Tools
LlamaIndex’s standout feature is its built-in visualization tools, which can generate HTML for viewing:

```python
from llama_index.utils.workflow import draw_all_possible_flows
draw_all_possible_flows(MyWorkflow, filename="multi_step_workflow.html")
```

### State Management
The demo example uses attributes of custom events to pass data sequentially, but this chained approach lacks flexibility, such as **cross-node data passing** or global context state management. To address this, LlamaIndex introduces the `Context` type parameter, as shown below:

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

Now, we define a `start` event to check if data is loaded into the context. If not, it returns a `SetupEvent`, triggering data loading and looping back to `start`’s `setup`.

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

        # Do something with the query
        return StepTwoEvent(query=ev.query)

    @step
    async def setup(self, ctx: Context, ev: SetupEvent) -> StartEvent:
        # Load data
        await ctx.set("some_database", [1, 2, 3])
        return StartEvent(query=ev.query)
```

Then, in `step_two`, we can directly access data from the context without explicitly passing it.

```python
@step
async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StopEvent:
    # Do something with the data
    print("Data is ", await ctx.get("some_database"))

    return StopEvent(result=await ctx.get("some_database"))

w = StatefulFlow(timeout=10, verbose=False)
result = await w.run(query="Some query")
print(result)
```

### Granular Control
#### 📌 Branching
As shown below, we create two event types. `Start` randomly decides to follow one branch or another, and multiple steps in each branch complete the workflow.

> 💡 Supports combining branches and loops in any order to meet diverse business needs. You can also use `send_event` to run multiple branches in parallel and `collect_events` to synchronize them.
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

#### 📌 Looping
To create a loop, we extend the `MyWorkflow` example from the previous tutorial and add a new custom event type called `LoopEvent`, though it can have any name.

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

#### 📌 Subclassing Workflows
Workflows can be extended or redefined like regular Python classes through inheritance (`class NewWorkflow(BaseWorkflow)`).

+ Subclasses can override specific steps in the parent class (same method name, event types may vary).
+ Subclasses can add new steps.
+ Step execution order is determined by the event passing chain (event types), not method order.

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

+ Here, the subclass **overrides** `step_two` and **adds** `step_two_b`, extending the processing flow.

#### 📌 Workflow Nesting
In the main workflow, reserve one or more **sub-workflow slots (Workflow Slot)** and dynamically inject complete sub-workflow instances at runtime.

+ In a main workflow step, accept a `Workflow` type parameter (e.g., `reflection_workflow`).
+ Use `.run()` to start the sub-workflow, which handles its internal logic.
+ Inject sub-workflows via `add_workflows(reflection_workflow=YourSubWorkflow())`.
+ Optionally set a **default sub-workflow** for the slot, allowing the main workflow to run standalone.

Example: Define a main workflow with a sub-workflow slot and a sub-workflow

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

Running with a custom sub-workflow:

```python
w = MainWorkflow(timeout=10, verbose=False)
w.add_workflows(reflection_workflow=ReflectionFlow())
result = await w.run(query="Initial query")
```

### Asynchronous Concurrency
Concurrent execution of steps in a workflow can significantly improve efficiency, especially when steps are independent and time-consuming. By emitting multiple events, workflows can execute tasks in parallel, reducing overall execution time.

#### 📌 Emitting Multiple Events
```python
class ParallelFlow(Workflow):
    @step
    async def start(self, ctx: Context, ev: StartEvent) -> StepTwoEvent:
        # Emit multiple events to start independent tasks
        ctx.send_event(StepTwoEvent(query="Query 1"))
        ctx.send_event(StepTwoEvent(query="Query 2"))
        ctx.send_event(StepTwoEvent(query="Query 3"))

    @step(num_workers=4)
    async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StopEvent:
        print("Running slow query ", ev.query)
        await asyncio.sleep(random.randint(1, 5))  # Simulate time-consuming operation
        return StopEvent(result=ev.query)
```

+ In `start`, three queries are sent in parallel.
+ `step_two` uses `num_workers=4` to indicate up to four concurrent instances, even with multiple queries.

#### 📌 Collecting Events
To wait for all parallel tasks to complete before proceeding, use the `collect_events` method to synchronize multiple events. `collect_events` waits for a specified number of events of a given type before continuing.

```python
class ConcurrentFlow(Workflow):
    @step
    async def start(self, ctx: Context, ev: StartEvent) -> StepTwoEvent:
        # Emit multiple events to start independent tasks
        ctx.send_event(StepTwoEvent(query="Query 1"))
        ctx.send_event(StepTwoEvent(query="Query 2"))
        ctx.send_event(StepTwoEvent(query="Query 3"))

    @step(num_workers=4)
    async def step_two(self, ctx: Context, ev: StepTwoEvent) -> StepThreeEvent:
        print("Running query ", ev.query)
        await asyncio.sleep(random.randint(1, 3))  # Simulate time-consuming operation
        return StepThreeEvent(result=ev.query)

    @step
    async def step_three(self, ctx: Context, ev: StepThreeEvent) -> StopEvent:
        # Wait for all three events
        result = ctx.collect_events(ev, [StepThreeEvent] * 3)
        if result is None:
            return None  # Return if events are incomplete

        # Proceed after collecting all results
        print(result)
        return StopEvent(result="Done")
```

> 💡 `collect_events` returns a list of events in the order they are received.
>

#### 📌 Waiting for Multiple Event Types
The `collect_events` method can wait for a combination of event types, processing them in the order received.

```python
@step
async def step_three(
    self,
    ctx: Context,
    ev: StepACompleteEvent | StepBCompleteEvent | StepCCompleteEvent,
) -> StopEvent:
    print("Received event ", ev.result)

    # Wait for three types of events
    if (
        ctx.collect_events(
            ev,
            [StepCCompleteEvent, StepACompleteEvent, StepBCompleteEvent],
        )
        is None
    ):
        return None  # Return if events are incomplete

    # Proceed after collecting all events
    return StopEvent(result="Done")
```

### Distributed Support
+ LlamaIndex is inherently asynchronous and event-driven, suitable for single-machine concurrency but requires external frameworks (e.g., Ray) for distributed execution.
+ Supports distributed data ingestion, indexing, and querying, enabling sharding and parallelization for large-scale tasks.
+ LlamaIndex officially supports integration with Ray via `@ray.remote`, Ray Datasets, and Ray Serve for distributed Workflow execution.
+ Ideal for parallel data processing, index building, and high-concurrency queries in production-grade RAG applications.

**Ray Integration Example:**

```python
import ray
from llama_index.core.workflow import Workflow, step, StartEvent, StopEvent
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader

# Initialize Ray
ray.init()

# Define distributed Workflow
@ray.remote
class DistributedWorkflow(Workflow):
    @step
    async def ingest_data(self, ev: StartEvent) -> None:
        # Load documents in parallel
        documents = SimpleDirectoryReader("data_directory").load_data()
        index = VectorStoreIndex.from_documents(documents)
        return {"index": index}

    @step
    async def query_step(self, ev: dict) -> StopEvent:
        index = ev["index"]
        query_engine = index.as_query_engine()
        result = query_engine.query("What is the main topic?")
        return StopEvent(result=str(result))

# Run distributed Workflow
workflow = DistributedWorkflow.remote()
result = ray.get(workflow.run.remote())
print(result)
```

### Streaming Output
LlamaIndex supports streaming events to users in real-time via the `ctx.write_event_to_stream()` method. Here, we define a workflow using the `Workflow` class and output event streams in each step.

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
            # Send progress event for each response chunk
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

+ In `step_one` and `step_three`, progress events are written directly.
+ In `step_two`, we use an `OpenAI` generator to asynchronously fetch LLM responses, sending progress events for each response chunk.

To run the workflow asynchronously and listen for events, use the `stream_events()` method, which returns each streaming event until the workflow completes.

```python
async def main():
    w = MyWorkflow(timeout=30, verbose=True)
    handler = w.run(first_input="Start the workflow.")

    async for ev in handler.stream_events():
        if isinstance(ev, ProgressEvent):
            print(ev.msg)  # Output real-time progress information

    final_result = await handler
    print("Final result", final_result)
```

### Persistence
By default, LlamaIndex stores data **in memory** and requires **explicit calls** to persist it to disk or other backends.

LlamaIndex’s **storage layer** is highly modular and pluggable, supporting the following data types:

| Type | Description |
| --- | --- |
| Document Store | Stores ingested documents (Node objects) |
| Index Store | Stores index structures and metadata |
| Vector Store | Stores embedded vectors |
| Property Graph Store | Stores property graph data (for knowledge graph indices) |
| Chat Store | Stores chat messages and conversation history |

Document and index stores are based on a unified **Key-Value storage abstraction layer**.

#### 📌 Local Persistence
```python
storage_context.persist(persist_dir="<persist_dir>")
```

+ `<persist_dir>`: Specifies the persistence directory, defaulting to `./storage`.
+ Multiple indices can be saved in the same directory, but `index_id` must be managed.
+ Local persistence is suitable for development, single-machine applications, or simple deployments.

Note: If using custom remote storage (e.g., MongoDB), calling `persist()` may be **unnecessary or ineffective**, depending on the backend implementation.

#### 📌 Loading
Loading persisted data involves **rebuilding the StorageContext** and using helper functions to load indices or graph structures.

Typical process:

+ **Rebuild StorageContext**:

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

+ **Load Objects (Single Index / Multiple Indices / Graph Structure)**:

```python
from llama_index.core import (
    load_index_from_storage,
    load_indices_from_storage,
    load_graph_from_storage,
)

# Load a single index (specify index_id)
index = load_index_from_storage(storage_context, index_id="<index_id>")

# Load all indices
indices = load_indices_from_storage(storage_context)

# Load knowledge graph (specify root_id)
graph = load_graph_from_storage(storage_context, root_id="<root_id>")
```

> Note:
>
> + If there’s only one index in the directory, `index_id` is optional.
> + For multiple indices, **specify** the `index_id` to load.
>

#### 📌 Using Remote Backends (e.g., S3/R2)
### Observability
#### 📌 Visualizing Workflow Structure (Global Perspective)
**Purpose**: View **all possible step transition paths** to aid in understanding and designing workflows.

+ Outputs HTML for interactive browser viewing.
+ Targets the **Workflow Class**, not instances.

```python
from llama_index.utils.workflow import draw_all_possible_flows

draw_all_possible_flows(MyWorkflow, filename="workflow.html")
```

#### 📌 Verbose Mode (Detailed Logs)
**Purpose**: Observe each step’s execution, event transitions in real-time.

```python
w = MyWorkflow(timeout=10, verbose=True)
result = await w.run()
```

Logs include:

+ **Step execution status**
+ **Event generation**
+ **Event types**

#### 📌 Stepwise Execution
**Purpose**: **Manually advance each step** for fine-grained debugging, ideal for complex concurrent or branched workflows.

```python
w = MyWorkflow(timeout=10, verbose=True)
handler = w.run(stepwise=True)

while produced_events := await handler.run_step():
    for ev in produced_events:
        handler.ctx.send_event(ev)

result = await handler
```

+ Each `run_step()` call advances one step.
+ Requires **manual sending** of newly produced events to drive subsequent steps.

#### 📌 Checkpoints
**Purpose**: **Save and restore** intermediate execution states to avoid restarting from scratch.

**Usage**:

```python
from llama_index.core.workflow.checkpointer import WorkflowCheckpointer

w = MyWorkflow()
w_ckptr = WorkflowCheckpointer(workflow=w)

handler = w_ckptr.run()
await handler

# View all generated checkpoints
w_ckptr.checkpoints[handler.run_id]

# Resume from a specific checkpoint
ckpt = w_ckptr.checkpoints[handler.run_id][0]
handler = w_ckptr.run_from(checkpoint=ckpt)
await handler
```

+ Each step records a checkpoint.
+ Enables **quick state restoration**, accelerating development and debugging cycles.

#### 📌 Third-Party Observability Tools
+ Integration with external platforms like **Arize** for advanced monitoring and visualization.
+ Currently, LlamaIndex primarily supports its own observability methods.

---

# Pydantic AI
## Basic Introduction
Pydantic AI, developed by the creators of the renowned Pydantic library, is an agent development framework that integrates Pydantic with LLMs. Its unique strength lies in leveraging Pydantic’s **type validation, serialization, and structured output** capabilities. Pydantic AI excels in **natural structured output and strong type validation**, is lightweight and easy to use, and integrates well with other frameworks.

> _Official Reference_: [PydanticAI Documentation](https://ai.pydantic.dev/), [PydanticAI GitHub](https://github.com/pydantic/pydantic-ai).
>

## Framework Evaluation
### Usage Instructions
#### 📌 Agent
PydanticAI’s agent module is its core component, designed to provide a structured, type-safe, and highly extensible way to build AI applications interacting with large language models (LLMs).

An agent instance combines:

+ **System Prompt**: Developer-defined instructions guiding LLM behavior.
+ **Function Tools**: Functions the LLM can call during response generation to fetch information or perform actions.
+ **Structured Result Type**: Specifies the structured data type the LLM must return upon completion.
+ **Dependency Type Constraint**: Dependencies available to system prompt functions, tools, and result validators at runtime.
+ **LLM Model**: The default LLM model associated with the agent, configurable at runtime.
+ **Model Settings**: Optional default model settings for fine-tuning requests, also configurable at runtime.

> 💡 In type terminology, an agent is generic in its dependency and result types. For example, an agent requiring `Foobar` dependencies and returning `list[str]` results is typed as `Agent[Foobar, list[str]]`.
>

PydanticAI offers multiple ways to run agents for different scenarios:

1. **Async Run**: `agent.run()` returns a coroutine, suitable for async environments.
2. **Sync Run**: `agent.run_sync()` is a synchronous function for sync environments.
3. **Streaming Run**: `agent.run_stream()` returns an async iterable for streaming responses.
4. **Iterative Run**: `agent.iter()` returns a context manager for manual control over the agent’s execution.

#### 📌 Function Tools
PydanticAI’s function tools mechanism allows agents to call external functions at runtime to fetch additional information or perform tasks, enhancing model responsiveness.

**Registration Methods**:

+ Use `@agent.tool` to register tools requiring access to the agent context.
+ Use `@agent.tool_plain` for tools not needing context access.
+ Register tool functions or `Tool` instances via the `tools` parameter in the `Agent` constructor.

**Dynamic Function Tools**

PydanticAI supports dynamic function tools, where tool definitions can be modified or included based on runtime context. This is achieved by defining a `prepare` function for the tool, called at runtime to customize behavior or decide whether to register the tool.

```python
# Define prepare function
async def only_if_42(ctx: RunContext[int], tool_def: ToolDefinition) -> Union[ToolDefinition, None]:
    if ctx.deps == 42:
        return tool_def

# Define tool and register prepare function
@agent.tool(prepare=only_if_42)
def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f'{ctx.deps} {answer}'

# Run agent
result = agent.run_sync('testing...', deps=41)
print(result.data)  # Tool not registered
result = agent.run_sync('testing...', deps=42)
print(result.data)  # Tool registered and called
```

**Tool and Structured Result Relationship**

Tool parameters and return values can be defined as Pydantic models, ensuring structured and type-safe data. PydanticAI extracts parameter descriptions from function docstrings, automatically generating JSON schemas for tools to enhance model understanding.

#### 📌 Result Validation
PydanticAI’s result module (`pydantic_ai.result`) provides a structured way to handle agent execution outputs, ensuring responses match expected formats and types.

+ **Result Type**: Defines the expected output format, ranging from simple `str` to complex Pydantic models.
+ **Result Wrapper Classes**:
  + `AgentRunResult`: Wraps results for synchronous runs.
  + `StreamedRunResult`: Wraps results for streaming runs.
+ **Structured Responses**: When the result type is a Pydantic model, PydanticAI generates corresponding JSON schemas and validates model outputs, ensuring type safety and structural consistency.

#### 📌 Dependency Injection
PydanticAI provides a unique dependency injection system to supply data and services to agent systems, prompts, tools, and result validators, particularly useful for testing.

+ **Define Dependencies**: Dependencies can be any Python type, often encapsulated in dataclasses (`@dataclass`) for multiple dependency objects, such as API keys and HTTP clients.

```python
from dataclasses import dataclass
import httpx

@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient
```

+ **Register Dependency Types**: Specify the dependency dataclass type via the `deps_type` parameter when creating an agent to enable type checking.

```python
from pydantic_ai import Agent

agent = Agent(
    model='openai:gpt-4o',
    deps_type=MyDeps
)
```

+ **Access Dependencies**: In system prompt functions, tool functions, and result validators, access dependencies via the `RunContext` type. `RunContext` uses generic parameters to specify dependency types, ensuring type safety.

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

> 💡 System prompt functions, function tools, and result validators run in the agent’s async context. If these functions are not coroutines (e.g., not `async def`), they are called in a thread pool via `run_in_executor`. For I/O operations, use `async` methods, though synchronous dependencies work fine.
>

#### 📌 Type Safety
The framework supports type safety through:

+ Pydantic models
+ Static type checking
+ Runtime validation
+ Structured output

It also integrates with static type checkers like mypy and pyrite to simplify type checking.

好的，我将继续基于您提供的原始文档内容，忠实翻译并完成 **PydanticAI** 部分的剩余内容，以及 **AutoGen** 和 **CrewAI** 的完整评估，确保不添加任何额外发挥，保持原文结构和细节。以下是翻译的完整内容：

### Message History 
#### 📌 Passing Messages in Multi-Turn Conversations
In subsequent agent runs, pass previous messages to the `message_history` parameter:

```python
from pydantic_ai import Agent
agent = Agent(model=llm, system_prompt='Be a helpful assistant.')

# Run the agent and get the result
result = agent.run_sync('My name is Alen.')
print(result.all_messages())
# [
#   {'role': 'system', 'content': 'Be a helpful assistant.'},
#   {'role': 'user', 'content': 'My name is Alen.'},
#   {'role': 'assistant', 'content': 'Nice to meet you, Alen! How can I assist you today?'}
# ]

# Pass message_history to maintain context
result = agent.run_sync(
    'What is my name?', 
    message_history=result.all_messages()
)
print(result.all_messages())
# [
#   {'role': 'system', 'content': 'Be a helpful assistant.'},
#   {'role': 'user', 'content': 'My name is Alen.'},
#   {'role': 'assistant', 'content': 'Nice to meet you, Alen! How can I assist you today?'},
#   {'role': 'user', 'content': 'What is my name?'},
#   {'role': 'assistant', 'content': 'Your name is Alen!'}
# ]
```

> 💡 In streaming runs, `all_messages()` and `new_messages()` include all messages seen so far, but the final output message is not included until the stream completes. Use `result.stream_messages()` to get an async iterable of new messages as they arrive:
>

```python
async def main():
    async with agent.run_stream('What is my name?', message_history=previous_result.all_messages()) as result:
        async for message in result.stream_messages():
            print(message)
            #> {'role': 'assistant', 'content': 'Your name is Alen!'}
```

### State Management
PydanticAI does not provide a built-in global state management mechanism like LangGraph’s `StateGraph` or LlamaIndex’s `Context`. Instead, state is managed explicitly through:

+ **Dependency Injection**: The `RunContext` object provides access to runtime dependencies, allowing tools, prompts, and validators to share state dynamically.
+ **Pydantic Models**: Structured inputs and outputs ensure type safety and consistency across steps.
+ **Message History**: Conversational state is preserved by passing message history between runs.

For persistent state across multiple executions, developers must implement external storage (e.g., databases or files) and pass state via dependencies.

```python
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel

# Define dependencies
@dataclass
class AppState:
    user_id: str
    session_data: dict

# Define structured output
class UserProfile(BaseModel):
    name: str
    preferences: dict

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    system_prompt='Retrieve and update user profile.',
    deps_type=AppState,
    result_type=UserProfile
)

# Define a tool to fetch state
@agent.tool
async def fetch_user_data(ctx: RunContext[AppState]) -> dict:
    # Simulate fetching data from a database
    return {'name': 'Alen', 'preferences': ctx.deps.session_data}

# Run the agent
result = agent.run_sync(
    'Get my profile.',
    deps=AppState(user_id='123', session_data={'theme': 'dark'})
)
print(result.data)
# Example output: UserProfile(name='Alen', preferences={'theme': 'dark'})
```

### Granular Control
PydanticAI does not offer a native workflow engine like LangGraph’s graph-based flows or LlamaIndex’s event-driven model. Control flow is managed through:

+ **Python Control Structures**: Developers use standard Python constructs (e.g., `if`, `for`, `try-except`) within tools or validators to implement branching and looping logic.
+ **Dynamic Tools**: The `prepare` function allows conditional tool registration based on runtime context, enabling dynamic behavior.
+ **Structured Outputs**: Pydantic models enforce strict output formats, allowing reliable branching based on validated results.

For complex workflows, PydanticAI can be combined with external orchestration tools like FastAPI (for API-driven workflows) or Celery (for task queues).

```python
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel

# Define structured output
class TaskResult(BaseModel):
    action: str
    data: dict

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    result_type=TaskResult
)

# Define a tool with conditional logic
@agent.tool
async def process_task(ctx: RunContext, task: str) -> dict:
    if task == 'analyze':
        return {'result': 'Analysis complete'}
    elif task == 'generate':
        return {'result': 'Generation complete'}
    else:
        raise ValueError('Unknown task')

# Run the agent
result = agent.run_sync('Perform task: analyze')
print(result.data)
# Example output: TaskResult(action='analyze', data={'result': 'Analysis complete'})
```

### Asynchronous & Concurrency
PydanticAI natively supports asynchronous execution, leveraging Python’s `asyncio` for concurrent operations. Key features include:

+ **Async Tools**: Tools can be defined as `async def` functions, enabling non-blocking I/O operations (e.g., API calls, database queries).
+ **Streaming Runs**: The `run_stream` method supports real-time response streaming for interactive applications.
+ **Concurrent Validation**: Pydantic’s validation is compatible with async contexts, ensuring type safety during concurrent execution.

For parallelism, developers can use Python’s `asyncio.gather` or third-party libraries like `concurrent.futures` to run multiple agent tasks concurrently.

```python
import asyncio
from pydantic_ai import Agent
from pydantic import BaseModel

# Define structured output
class AnalysisResult(BaseModel):
    task_id: int
    result: str

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    system_prompt='Analyze multiple documents concurrently.',
    result_type=AnalysisResult
)

# Define an async tool
@agent.tool
async def analyze_document(doc_id: int) -> dict:
    await asyncio.sleep(doc_id)  # Simulate async work
    return {'task_id': doc_id, 'result': f'Analyzed doc {doc_id}'}

# Run multiple tasks concurrently
async def main():
    tasks = [
        agent.run_async(f'Analyze doc {i}', deps=i)
        for i in range(1, 4)
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result.data)

if __name__ == '__main__':
    asyncio.run(main())
# Example output:
# AnalysisResult(task_id=1, result='Analyzed doc 1')
# AnalysisResult(task_id=2, result='Analyzed doc 2')
# AnalysisResult(task_id=3, result='Analyzed doc 3')
```

### Distributed Support
PydanticAI does not provide built-in support for distributed execution. To achieve distributed workflows, developers can integrate with:

+ **FastAPI**: Expose agents as REST APIs for distributed access across nodes.
+ **Celery**: Offload tasks to a distributed task queue for parallel processing.
+ **Ray**: Use Ray’s actor model to distribute agent execution across a cluster.

Example with FastAPI:

```python
from fastapi import FastAPI
from pydantic_ai import Agent
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    result_type=str
)

# Define input model
class TaskInput(BaseModel):
    input: str

# Define API endpoint
@app.post('/run-agent')
async def run_agent(task: TaskInput):
    result = await agent.run_async(task.input)
    return result.data
```

### Streaming Output
PydanticAI supports streaming responses via the `run_stream` method, which is ideal for real-time applications like chatbots or live data processing.

```python
from pydantic_ai import Agent

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    system_prompt='Tell engaging stories.'
)

# Stream responses
async def main():
    async with agent.run_stream('Tell me a story.') as result:
        async for text in result.stream_text():
            print(text, end='', flush=True)
            # Example output: Once upon a time, in a faraway kingdom...

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```

### Persistence
PydanticAI does not include a built-in persistence layer. Developers must implement persistence using external databases (e.g., PostgreSQL, MongoDB) or file storage, passing state via dependencies or message history.

Example with SQLite:

```python
import sqlite3
from pydantic_ai import Agent, RunContext

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    result_type=str
)

# Define a tool to save state
@agent.tool
async def save_state(ctx: RunContext, key: str, value: str) -> None:
    conn = sqlite3.connect('state.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value TEXT)')
    cursor.execute('INSERT OR REPLACE INTO state (key, value) VALUES (?, ?)', (key, value))
    conn.commit()
    conn.close()

# Run the agent
result = agent.run_sync('Save state: user=Alen', deps={})
print(result.data)
# Example output: State saved successfully
```

### Observability
PydanticAI integrates with **Logfire** for observability, providing:

+ **Logging**: Track agent execution, tool calls, and errors.
+ **Tracing**: Visualize call chains and performance metrics.
+ **Debugging**: Inspect inputs, outputs, and validation failures.

Example with Logfire:

```python
from pydantic_ai import Agent
import logfire

# Configure Logfire
logfire.configure()

# Initialize agent
agent = Agent(
    model='openai:gpt-4o-mini',
    result_type=str
)

# Run agent with logging
with logfire.span('Run agent'):
    result = agent.run_sync('Analyze this text.')
    logfire.info('Agent result', result=result.data)
```

### Learning Curve
PydanticAI is easy to learn for developers familiar with Python and Pydantic. Its emphasis on type safety, structured outputs, and dependency injection aligns with modern software engineering practices, making it accessible for backend developers integrating LLMs into existing systems.

### Community Activity
PydanticAI is an emerging framework with a growing community, backed by the established Pydantic ecosystem. It has moderate GitHub activity (8,218 stars, 159 PR creators) but benefits from Pydantic’s widespread adoption in the Python community.

### LLM Support
PydanticAI supports major LLMs, including:

+ OpenAI (e.g., GPT-4o, GPT-3.5)
+ Anthropic (e.g., Claude)
+ Google (e.g., Gemini)
+ DeepSeek
+ Cohere

It allows flexible configuration of model providers via API keys and settings.

### Framework Compatibility
PydanticAI integrates seamlessly with:

+ **FastAPI**: For building RESTful APIs with agent endpoints.
+ **SQLAlchemy**: For database interactions.
+ **Message Queues**: For asynchronous task processing (e.g., RabbitMQ, Kafka).
+ **Python Ecosystem**: Compatible with standard Python libraries and tools.

This makes PydanticAI ideal for microservices and API-driven applications.

### DevOps Deployment
PydanticAI agents can be deployed in several ways:

+ **Python Packages**: Run as standalone scripts or services.
+ **Docker Containers**: Package with Docker for consistent deployments.
+ **Kubernetes**: Scale with Kubernetes for high availability and load balancing.

Example Dockerfile:

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# AutoGen
## Framework Evaluation
### Usage Instructions
AutoGen’s core strength lies in its **conversational agent model**, enabling multi-agent collaboration through message passing. Agents can be defined with specific roles, capabilities, and tools, making it easy to build dynamic, interactive systems.

```python
from autogen import AssistantAgent, UserProxyAgent
import os

# Define agents
user_proxy = UserProxyAgent(
    name='User',
    human_input_mode='ALWAYS'
)
assistant = AssistantAgent(
    name='Assistant',
    llm_config={
        'model': 'gpt-4o-mini',
        'api_key': os.getenv('OPENAI_API_KEY')
    }
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message='Write a Python script to fetch weather data.'
)
```

### State Management
AutoGen manages state through:

+ **Message History**: Agents maintain conversational context via message logs, accessible via `chat_history`.
+ **External Storage**: Developers can save message history to databases or files for persistence.
+ **Group Chat**: A `GroupChatManager` coordinates multi-agent state in group conversations, ensuring context is shared appropriately.

```python
from autogen import GroupChat, GroupChatManager

# Define group chat
group_chat = GroupChat(
    agents=[user_proxy, assistant],
    messages=[]
)
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=assistant.llm_config
)

# Start group conversation
user_proxy.initiate_chat(
    manager,
    message='Plan a team project.'
)
```

### Granular Control
AutoGen provides flexible control over agent interactions through:

+ **Message Patterns**: Define custom message routing (e.g., broadcast, direct, topic-based).
+ **Conditional Logic**: Implement branching in agent logic using Python code.
+ **Topic Subscription**: Agents can subscribe to specific topics for dynamic, unstructured interactions.

```python
# Custom agent with conditional logic
class CustomAgent(AssistantAgent):
    def process_message(self, message):
        if 'urgent' in message['content'].lower():
            return {'content': 'Prioritizing urgent task!'}
        return super().process_message(message)

# Initialize custom agent
custom_agent = CustomAgent(
    name='CustomAgent',
    llm_config={'model': 'gpt-4o-mini'}
)
```

### Asynchronous & Concurrency
AutoGen supports asynchronous execution via Python’s `asyncio`, enabling concurrent agent interactions and efficient handling of I/O-bound tasks.

```python
import asyncio
from autogen import AssistantAgent

async def main():
    agent = AssistantAgent(
        name='AsyncAgent',
        llm_config={'model': 'gpt-4o-mini'}
    )
    response = await agent.a_initiate_chat({'message': 'Analyze data.'})
    print(response.chat_history)

if __name__ == '__main__':
    asyncio.run(main())
```

### Distributed Support
AutoGen supports distributed execution through:

+ **Local Processes**: Run agents in separate processes for parallelism.
+ **Remote Deployment**: Use RPC or WebSocket for remote agent communication.
+ **AutoGen Studio**: Provides a UI for managing distributed agents, simplifying deployment and monitoring.

### Streaming Output
AutoGen supports streaming responses for real-time interactions, allowing users to see partial outputs as they are generated.

```python
# Stream responses
for response in assistant.generate_streaming_reply({'message': 'Tell a story.'}):
    print(response['content'], end='', flush=True)
```

### Persistence
AutoGen does not provide a built-in persistence layer. Developers must implement persistence using external databases or file storage, similar to PydanticAI.

Example with JSON file storage:

```python
import json

# Save chat history
with open('chat_history.json', 'w') as f:
    json.dump(agent.chat_history, f)
```

### Observability
AutoGen integrates with standard logging frameworks (e.g., Python’s `logging`) and can be extended with observability tools like Prometheus or Grafana for monitoring and visualization.

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('AutoGen')
logger.info('Agent started')
```

### Learning Curve
AutoGen’s modular design is accessible, but building multi-agent systems requires understanding conversational patterns, message flows, and agent orchestration. The learning curve is moderate, especially for developers new to multi-agent architectures.

### Community Activity
AutoGen has a vibrant community with significant GitHub activity (41,610 stars, 571 PR creators). It benefits from comprehensive documentation, active development, and strong support from Microsoft.

### LLM Support
AutoGen supports a wide range of LLMs, including:

+ OpenAI (e.g., GPT-4o, GPT-3.5)
+ Azure OpenAI
+ Hugging Face models
+ Other API-based providers

It provides flexible configuration for model integration.

### Framework Compatibility
AutoGen is compatible with:

+ **Python Ecosystem**: Integrates with standard Python libraries and tools.
+ **.NET**: Supports .NET-based applications for cross-platform development.
+ **AutoGen Studio**: Provides a visual interface for multi-platform integration and debugging.

### DevOps Deployment
AutoGen can be deployed as:

+ **Python Services**: Run as standalone scripts or services.
+ **Docker Containers**: Package with Docker for consistent deployments.
+ **AutoGen Studio Server**: Host agents via Studio’s server mode for centralized management.

---

# CrewAI
## Framework Evaluation
### Usage Instructions
CrewAI organizes agents into **Crews** (teams of agents) and **Flows** (workflows), with a focus on role-based task delegation and process-driven automation.

```python
from crewai import Agent, Task, Crew

# Define agents
researcher = Agent(
    role='Researcher',
    goal='Find market trends.',
    llm='gpt-4o-mini'
)
writer = Agent(
    role='Writer',
    goal='Write a report.',
    llm='gpt-4o-mini'
)

# Define tasks
research_task = Task(
    description='Research AI market trends.',
    agent=researcher
)
write_task = Task(
    description='Write a report on findings.',
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task]
)

# Execute
result = crew.kickoff()
print(result)
```

### State Management
CrewAI uses a **Memory module** to manage state and context across tasks and agents.

```python
from crewai import Memory

# Initialize memory
memory = Memory()

# Save task context
memory.save_context(
    task_id='research_task',
    data={'trends': 'AI adoption rising'}
)
```

### Granular Control
CrewAI provides granular control through:

+ **Conditional Branching**: Define task dependencies and conditions for execution.
+ **Task Delegation**: Dynamically assign tasks to agents based on their roles.
+ **Synchronization**: Coordinate multi-agent tasks using callbacks and event listeners.

```python
# Conditional task
write_task = Task(
    description='Write if research complete.',
    agent=writer,
    condition=lambda: memory.get_context('research_task') is not None
)
```

### Asynchronous & Concurrency
CrewAI supports asynchronous task execution and concurrent Flows, leveraging Python’s `asyncio` for efficient resource utilization.

```python
async def main():
    result = await crew.kickoff_async()
    print(result)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```

### Distributed Support
CrewAI’s enterprise edition supports cluster deployment with load balancing, while the open-source version requires manual scaling (e.g., using Kubernetes or cloud platforms).

### Streaming Output
CrewAI uses task callbacks to provide indirect streaming support, allowing developers to monitor task progress in real-time.

```python
# Define callback for task completion
def on_task_complete(task, result):
    print(f'Task {task.description} completed: {result}')

write_task.callback = on_task_complete
```

### Persistence
CrewAI’s **Memory module** automatically caches task states and supports integration with external databases for persistent storage.

```python
# Save to database
memory.save_to_db('postgresql://user:pass@localhost:5432/crewai')
```

### Observability
CrewAI provides a control plane for monitoring agent performance, task execution, and resource consumption.

```python
# Enable monitoring
crew.enable_monitoring()
```

### Learning Curve
CrewAI’s Crew and Flow model is intuitive and aligns with real-world team collaboration concepts. The learning curve is low, especially for developers familiar with role-based workflows.

### Community Activity
CrewAI has strong community support with significant GitHub activity (29,091 stars, 364 PR creators). It offers rich documentation, tutorials, and enterprise-grade support.

### LLM Support
CrewAI connects to any API-based LLM, providing flexible integration with providers like OpenAI, Anthropic, and others.

### Framework Compatibility
CrewAI integrates with Python’s native ecosystem, including:

+ **Logging**: For monitoring and debugging.
+ **Caching**: For performance optimization.
+ **Data Platforms**: For integration with databases and storage systems.

### DevOps Deployment
CrewAI supports:

+ **Scripted Auto-Deployment**: In the open-source version, using Python scripts or Docker.
+ **Centralized Management**: In the enterprise edition, with cloud deployment and cluster management.

