# **How to Choose? In-depth Comparison of Popular AI Agent Frameworks**
The explosive growth of generative AI has made technology selection a primary challenge for developers. Almost every day, new frameworks, tools, or technologies emerge. Whether you're an individual developer or part of an enterprise team, building innovative applications with large language models (LLMs) raises a critical question: "Which framework is best suited for my use case?" This article provides a deep, practical comparison of five popular AI Agent frameworks—LangGraph, LlamaIndex, PydanticAI, AutoGen, and CrewAI—from a developer's perspective, across multiple dimensions, to serve as a hands-on reference. **Note that this article focuses primarily on evaluating these frameworks' performance in building non-agentic AI workflows.**

## Why Do We Need LLM Frameworks?
LLM frameworks are like your intelligent assistants, simplifying the development process of complex AI applications into building blocks. They provide out-of-the-box components, interfaces, and tools, allowing you to quickly build AI systems—such as text generation, data processing, or RAG (Retrieval Augmented Generation) applications—without writing a lot of underlying code from scratch. Whether you want to quickly validate an idea or deploy a production-grade system, choosing the right framework can help you avoid detours and save valuable time.

Essentially, the ultimate goal of **Agent** frameworks is to **let developers focus on innovation rather than reinventing the wheel.** Specifically, the core advantages of frameworks lie in helping you manage **prompt engineering and data routing**, enabling seamless integration between large language models (LLMs) and external tools (like APIs, databases). They lower the development barrier through additional abstraction layers while providing robust functional support, such as structured output, error handling, result validation, observability, and deployment support. More importantly, frameworks help you organize code and easily tackle complex scenarios, like multi-agent collaborative systems.
![abstraction.png](pictures/abstraction.png)
However, frameworks are not a panacea. Some developers feel that using a full-fledged framework can be overkill, as **high abstraction layers** can complicate debugging—for instance, when an LLM tool call fails, pinpointing the issue can be like finding a needle in a haystack. Predefined flows and structures can also somewhat limit customization capabilities. When changing models, custom prompts might become incompatible, forcing you to rewrite logic. Conversely, **low-abstraction** frameworks offer greater flexibility and more straightforward debugging but also increase development costs, requiring manual implementation of many features. Therefore, **the true value of a framework lies in balancing ease of use with control, allowing you to find a sweet spot between rapid development and fine-grained debugging.**

## The Core Value of Workflows
Workflows are event-driven, step-based methods for controlling the execution flow of applications. As generative AI applications become increasingly complex, managing data flows and controlling application execution becomes more challenging. Workflows break tasks into modular sub-steps, offering greater flexibility and maintainability. This is particularly valuable in scenarios involving multi-agent collaboration or cross-system interactions, significantly improving development efficiency and system robustness.

## Agentic vs. Non-Agentic Workflows
![agentic_workflow.png](pictures/agentic_workflow.png)
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

# Five Popular Agent Development Frameworks
## Open-Source Status and Community Activity
_Table 1: Overview of Community Activity for Popular AI Agent Frameworks_

| Framework | Stars | Commits | Issues | Forks | PR Creators | Primary Language |
| --- | --- | --- | --- | --- | --- | --- |
| **LangGraph** | 11,353 | 9,624 | 646 | 2,022 | 259 | Python |
| **LlamaIndex** | 39,568 | 14,044 | 8,826 | 5,881 | 1,603 | Python |
| **PydanticAI** | 8,218 | 2,303 | 724 | 798 | 159 | Python |
| **AutoGen** | 41,610 | 14,143 | 2,667 | 6,624 | 571 | Python |
| **CrewAI** | 29,091 | 5,245 | 1,290 | 4,129 | 364 | Python |

_Table 2: Community Activity for Popular AI Agent Frameworks in the Last 28 Days_

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
![langgraph_workflow.png](pictures/langgraph_workflow.png)
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
    # Simulate actual PDF loading and content extraction
    return {"raw_content": f"Simulated raw content from {pdf_path}"}

# Node: Parse document
def parse_document(state: PipelineState):
    """Simulate parsing the loaded document."""
    raw_content = state["raw_content"]
    # Simulate document parsing
    parsed_content = {"metadata": {"title": "AI for Everyone"}, "text_chunks": ["Chunk 1...", "Chunk 2..."]}
    return {"parsed_content": parsed_content}

# Node: Summarize text using LLM
def summarize_text(state: PipelineState):
    """Simulate summarizing the parsed content via LLM."""
    parsed_content = state["parsed_content"]
    # Simulate LLM summarization
    summarized_text = "Summary: AI applications in various industries based on parsed chunks."
    return {"summarized_content": summarized_text}

# Node: Persist results into a database
def persist_to_db(state: PipelineState):
    """Simulate writing summarized content to the database."""
    summarized_content = state["summarized_content"]
    # Simulate database persistence
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
    init_state = {"pdf_path": "upload/pdf/ai_for_everyone.pdf", "raw_content": "", "parsed_content": {}, "summarized_content": "", "persist_status": ""}
    final_state = chain.invoke(init_state)

    print("--- Pipeline Execution Result ---")
    for key, value in final_state.items():
        print(f"{key}: {value}")

# --- Pipeline Execution Result ---
# pdf_path: upload/pdf/ai_for_everyone.pdf
# raw_content: Simulated raw content from upload/pdf/ai_for_everyone.pdf
# parsed_content: {'metadata': {'title': 'AI for Everyone'}, 'text_chunks': ['Chunk 1...', 'Chunk 2...']}
# summarized_content: Summary: AI applications in various industries based on parsed chunks.
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
from typing_extensions import TypedDict
from typing import Annotated # Ensure Annotated is imported
import operator # Ensure operator is imported for operator.add if used, though not in this specific example's reducer

# Define State (ensure it's defined before use, e.g. State or ExtractState)
class State(TypedDict):
    parsed_chunks: Annotated[list[str], operator.add] # If using operator.add as reducer
    # Or simply: parsed_chunks: Annotated[list[str], append_chunks] if append_chunks is the reducer
    metadata: dict

def append_chunks(left: list[str], right: list[str]) -> list[str]: # Explicit type hints
    """Append two lists of parsed text chunks."""
    if left is None: left = []
    if right is None: right = []
    return left + right

# Example node updating the state
def parse_document_node(state: State): # Renamed to avoid conflict
    """Mock parsing a document and returning new chunks."""
    # Simulate extracting new chunks
    new_chunks = ["This is a new paragraph extracted."]
    # Simulate extracting metadata
    metadata_update = {"source": "upload/pdf/ai_for_everyone.pdf", "status": "parsed"}
    return {"parsed_chunks": new_chunks, "metadata": metadata_update}

# Build the graph using the correct State definition and reducer for 'parsed_chunks'
# For this example, let's assume 'append_chunks' is registered with 'parsed_chunks'
# when StateGraph is instantiated or via a field annotation if the framework supports it directly.
# If State uses `Annotated[list[str], operator.add]`, then `operator.add` is the reducer.
# If `Annotated[list[str], append_chunks]`, then `append_chunks` is the reducer.
# For clarity, let's assume State is defined as:
# class State(TypedDict):
#     parsed_chunks: Annotated[list[str], append_chunks]
#     metadata: dict # Default reducer (overwrite)

graph_builder = StateGraph(State) # Use the defined State
graph_builder.add_node("parse_doc_node", parse_document_node) # Use unique node name
graph_builder.add_edge(START, "parse_doc_node")
graph_builder.add_edge("parse_doc_node", END) # Typically graphs have an end

# Compile the graph
chain = graph_builder.compile()

# Invoke the chain with an initial state
initial_state = {"parsed_chunks": ["Introduction to AI..."], "metadata": {"initial_source": "None"}}
result = chain.invoke(initial_state)

# Output
print("Accumulated parsed chunks:")
if "parsed_chunks" in result:
    for idx, chunk in enumerate(result["parsed_chunks"], start=1):
        print(f"{idx}. {chunk}")
print("
Final metadata:")
if "metadata" in result:
    print(result["metadata"])

# =================================
# Accumulated parsed chunks:
# 1. Introduction to AI...
# 2. This is a new paragraph extracted.
#
# Final metadata:
# {'initial_source': 'None', 'source': 'upload/pdf/ai_for_everyone.pdf', 'status': 'parsed'}
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
    current_step: str # For logging or simple state tracking

# Define Nodes
def load_pdf_node(state: State): # Renamed
    print("Loading PDF...")
    # Initialize or update state fields as necessary
    return {"current_step": "load_pdf_node", "language": state.get("language", "en"), "retry_count": state.get("retry_count", 2)}

def extract_body_chinese_node(state: State): # Renamed
    print("Extracting Chinese body text...")
    return {"body_chunks": ["Chinese paragraph"], "current_step": "extract_body_chinese_node"}

def extract_body_english_node(state: State): # Renamed
    print("Extracting English body text...")
    return {"body_chunks": ["English paragraph"], "current_step": "extract_body_english_node"}

def extract_table_node(state: State): # Renamed
    print("Extracting table of contents...")
    return {"table_chunks": ["Table of contents data"], "current_step": "extract_table_node"}

def merge_results_node(state: State): # Renamed
    print(f"Current Step: {state.get('current_step')}")
    print(f"Merged Body Chunks: {state.get('body_chunks', [])}")
    print(f"Merged Table Chunks: {state.get('table_chunks', [])}")
    remaining_retries = state.get("retry_count", 0) - 1
    return {"retry_count": remaining_retries, "current_step": "merge_results_node"}

# Branching
def route_language_extraction(state: State) -> str:
    if state.get("language") == "zh":
        return "extract_body_chinese_node"
    else:
        return "extract_body_english_node"

# Loop Control
def check_retry_or_end(state: State) -> str:
    if state.get("retry_count", 0) <= 0:
        print("Max retries reached or no retries needed. Ending.")
        return END
    else:
        print(f"Retries left: {state.get('retry_count')}. Retrying from load_pdf_node.")
        return "load_pdf_node" # Loop back to the start

# Build the Graph
builder = StateGraph(State)

# Add nodes
builder.add_node("load_pdf_node", load_pdf_node)
builder.add_node("extract_body_chinese_node", extract_body_chinese_node)
builder.add_node("extract_body_english_node", extract_body_english_node)
builder.add_node("extract_table_node", extract_table_node)
builder.add_node("merge_results_node", merge_results_node)

# Add edges
builder.add_edge(START, "load_pdf_node")

builder.add_conditional_edges(
    "load_pdf_node",
    route_language_extraction,
    {
        "extract_body_chinese_node": "extract_body_chinese_node",
        "extract_body_english_node": "extract_body_english_node",
    }
)

# Sequential flow after language-specific extraction
builder.add_edge("extract_body_chinese_node", "extract_table_node")
builder.add_edge("extract_body_english_node", "extract_table_node")
builder.add_edge("extract_table_node", "merge_results_node")

builder.add_conditional_edges(
    "merge_results_node",
    check_retry_or_end,
    {
        "load_pdf_node": "load_pdf_node", # If retry
        END: END  # If end
    }
)

# Compile
graph = builder.compile()

# Run with recursion_limit to avoid infinite loop
if __name__ == "__main__":
    try:
        initial_state = {
            "body_chunks": [],
            "table_chunks": [],
            "language": "zh", # Example: Chinese language
            "retry_count": 2, # Start with 2 retries
            "current_step": "initial"
        }
        # recursion_limit is important for graphs with cycles
        final_result = graph.invoke(initial_state, config={"recursion_limit": 10})
        print("
Final graph state:")
        print(final_result)
    except GraphRecursionError:
        print("Exceeded maximum recursion limit. Returning last known state.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
<div style="text-align: center;">
  <img src="pictures/workflow_sample.png" alt="Workflow Sample">
</div>
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
from typing_extensions import TypedDict
from typing import Annotated, List # Added List
import operator # Ensure operator is imported

# Define the overall state
class OverallState(TypedDict):
    chunks: List[str] # Use List[str]
    summaries: Annotated[List[str], operator.add] # Use List[str]
    processed_count: Annotated[int, operator.add] # Example of another field

# Define the dispatch logic using Send API
def dispatch_chunks(state: OverallState):
    # This will send each chunk to the 'summarize_chunk' node to be processed independently.
    # Each Send invocation creates a new task for 'summarize_chunk' with its own input state.
    return [Send("summarize_chunk", {"chunk": chunk, "processed_count": 0}) for chunk in state["chunks"]]

# Define the node to summarize a single chunk
def summarize_chunk(state: dict): # Receives the specific state sent by Send
    # Simulate summarization
    summary = f"Summary of: {state['chunk'][:20]}..."
    # Return updates for the OverallState
    return {"summaries": [summary], "processed_count": 1}


# Build the graph
builder = StateGraph(OverallState)
builder.add_node("summarize_chunk", summarize_chunk)

# The entry point will call dispatch_chunks, which then uses Send
# to dynamically route to 'summarize_chunk' for each chunk.
builder.add_conditional_edges(START, dispatch_chunks)

# After all 'summarize_chunk' tasks (spawned by Send) are done,
# LangGraph implicitly collects their outputs and updates the OverallState.
# Then, the graph proceeds to END.
builder.add_edge("summarize_chunk", END) # Edges from dynamically created tasks go to END

graph = builder.compile()

# Run the graph
if __name__ == "__main__":
    initial_chunks = ["This is the first long document part.", "This is the second part, a bit shorter.", "And a third one."]
    output = graph.invoke({"chunks": initial_chunks, "summaries": [], "processed_count": 0})
    print("Output from graph execution:")
    print(f"Original Chunks: {initial_chunks}")
    print(f"Summaries: {output['summaries']}")
    print(f"Total Processed Count: {output['processed_count']}")
# Expected output:
# Output from graph execution:
# Original Chunks: ['This is the first long document part.', 'This is the second part, a bit shorter.', 'And a third one.']
# Summaries: ['Summary of: This is the first lo...', 'Summary of: This is the second pa...', 'Summary of: And a third one....']
# Total Processed Count: 3
```

### Asynchronous Execution
Using asynchronous execution can significantly improve performance when running I/O-bound code concurrently (e.g., making concurrent API requests to chat model providers).

To switch from synchronous to asynchronous:

+ Change node functions from `def` to `async def`.
+ Use `await` correctly within nodes.

Since many LangChain objects follow the Runnable protocol, and synchronous methods typically have asynchronous counterparts, migration is usually straightforward.

```python
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage # Ensure BaseMessage, AIMessage are imported
from typing import List, Annotated # Ensure List, Annotated are imported
import operator # For Annotated
import asyncio # For async operations

# Assume 'model' is an initialized LangChain chat model, e.g., ChatOpenAI()
# from langchain_openai import ChatOpenAI 
# model = ChatOpenAI() # Example: Define the model

class AsyncState(TypedDict): # Renamed to avoid conflict
    messages: Annotated[List[BaseMessage], operator.add]
    # other fields if needed

async def call_model_async_node(state: AsyncState, config): # Renamed, added config
    print(f"Calling model with messages: {state['messages'][-1].content}")
    # Example: Using a LangChain model asynchronously
    # response = await model.ainvoke(state["messages"], config=config)
    # Simulate response
    await asyncio.sleep(0.1) # Simulate async work
    response = AIMessage(content=f"Async echo: {state['messages'][-1].content}")
    return {"messages": [response]} # Append new response

# Example graph setup (simplified)
# from langgraph.graph import StateGraph, START, END
# graph_builder_async = StateGraph(AsyncState)
# graph_builder_async.add_node("call_model_async_node", call_model_async_node)
# graph_builder_async.add_edge(START, "call_model_async_node")
# graph_builder_async.add_edge("call_model_async_node", END)
# async_graph = graph_builder_async.compile()
    
async def main_async_example(): # Renamed
    # This main function is for demonstrating the async node.
    # A full graph invocation would look like:
    # initial_messages = [HumanMessage(content="Hello, what is the weather?")]
    # async_result = await async_graph.ainvoke({"messages": initial_messages})
    # print("Async graph result:")
    # print(async_result["messages"][-1].pretty_print())

    # To demonstrate streaming output (as in Chinese version's example for astream):
    # print("
Streaming async graph output:")
    # async for output_chunk in async_graph.astream(
    #     {"messages": [HumanMessage(content="Tell me a joke.")]},
    #     stream_mode="updates" # or "values" or "messages"
    # ):
    #     for key, value in output_chunk.items():
    #         print(f"Update from node '{key}':")
    #         if "messages" in value and value["messages"]:
    #             print(value["messages"][-1].pretty_print())
    #         else:
    #             print(value)
    #     if output_chunk.get("event") == "on_chain_end":
    #         print("\n--- Async Graph Stream Ended ---")

    # For now, as the node is placeholder:
    # final_state = await compiled_llm_graph.ainvoke(initial_graph_state)
    # print("\nFinal State (after placeholder execution):")
    # print(f"Summary: {final_state['summary_output'][-1].content}")
    # print(f"Keywords: {final_state['keywords_output'][-1].content}")
    pass

if __name__ == "__main__":
    # To run the async main example:
    # asyncio.run(main_async_example())
    pass
```

### Distributed Support
LangGraph supports distributing tasks across multiple compute nodes or threads. This is particularly useful for scaling agentic applications or parallelizing steps in a complex workflow. A common way to achieve this is by integrating with distributed computing frameworks like Ray.

1.  **Encapsulate StateGraph in a Ray Actor**: Define a Ray actor that holds a compiled LangGraph.
2.  **Instantiate Actors**: Create multiple instances of this actor, which Ray can schedule on different workers in a cluster.
3.  **Remote Asynchronous Calls**: Invoke methods on these actors asynchronously. Each actor processes its tasks independently and concurrently.

```python
import ray
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
import asyncio
import time # For simulating work

# Initialize Ray (if not already initialized)
if not ray.is_initialized():
    ray.init(ignore_reinit_error=True)

# Define the state type for LangGraph
class DistributedState(TypedDict):
    task_id: int
    message_list: List[str]
    status: str

# Node function (can be async or sync)
async def process_task_node(state: DistributedState):
    task_id = state["task_id"]
    print(f"Worker (Ray Actor) processing task_id: {task_id}, current messages: {state['message_list']}")
    await asyncio.sleep(0.5) # Simulate some async work
    new_message = f"Task {task_id} processed at {time.time()}"
    return {"message_list": state["message_list"] + [new_message], "status": "completed"}

# Ray Actor class to encapsulate StateGraph
@ray.remote(num_cpus=1)  # Each Actor can use 1 CPU
class GraphWorkerActor:
    def __init__(self, actor_id: int):
        self.actor_id = actor_id
        self.graph_definition = StateGraph(DistributedState)
        self.graph_definition.add_node("process_task", process_task_node)
        self.graph_definition.add_edge(START, "process_task")
        self.graph_definition.add_edge("process_task", END)
        self.compiled_graph = self.graph_definition.compile()
        print(f"GraphWorkerActor {self.actor_id} initialized.")

    async def execute_graph(self, initial_state: DistributedState) -> DistributedState:
        print(f"Actor {self.actor_id} executing graph for task_id: {initial_state['task_id']}")
        result = await self.compiled_graph.ainvoke(initial_state)
        return result

# Main function to create and run multiple GraphWorkerActors
async def run_distributed_graphs(num_workers: int = 2, num_tasks_per_worker: int = 1):
    # Create multiple GraphWorkerActors
    actors = [GraphWorkerActor.remote(actor_id=i) for i in range(num_workers)]

    tasks_to_submit = []
    for i in range(num_workers):
        for j in range(num_tasks_per_worker):
            task_id = i * num_tasks_per_worker + j
            initial_task_state = DistributedState(
                task_id=task_id,
                message_list=[f"Initial message for task {task_id}"],
                status="pending"
            )
            # Submit task to an actor (e.g., round-robin or based on load)
            actor_index = i % num_workers
            tasks_to_submit.append(actors[actor_index].execute_graph.remote(initial_task_state))
    
    print(f"Submitted {len(tasks_to_submit)} tasks to Ray actors.")

    # Wait for all tasks to complete and retrieve results
    results = await asyncio.gather(*tasks_to_submit) # Ray ObjectRefs can be awaited directly

    print("\n--- Distributed Execution Results ---")
    for idx, result_state in enumerate(results):
        print(f"Result for submitted task {idx}:")
        print(f"  Task ID: {result_state['task_id']}")
        print(f"  Messages: {result_state['message_list']}")
        print(f"  Status: {result_state['status']}")

if __name__ == "__main__":
    # Example of running the distributed graph execution
    # asyncio.run(run_distributed_graphs(num_workers=2, num_tasks_per_worker=2))
    # ray.shutdown() # Shutdown Ray when done
    pass
```

### **Streaming Output**
Streaming is crucial for responsiveness in LLM applications, especially for reducing perceived latency. LangGraph offers various streaming modes:

1.  **`values`**: Emits all state values after each step.
2.  **`updates`**: Emits only the node name and the updates from each step.
3.  **`custom`** (via `StreamWriter`): Allows custom data output. (Note: `StreamWriter` is more of an internal mechanism or for advanced customization; `stream_mode` is the primary API for users).
4.  **`messages`**: Streams LLM messages token by token, along with their metadata. This is particularly useful for chat applications.
5.  **`debug`**: Emits detailed debugging information about the graph execution.

You can stream outputs during graph execution using `graph.stream(...)` (synchronous) or `graph.astream(...)` (asynchronous) with the `stream_mode` parameter.

```python
# Assume 'graph' is a compiled LangGraph instance and 'inputs' is the initial state.

# Synchronous streaming example
# for chunk in graph.stream(inputs, stream_mode="updates"): # or ["updates", "messages"]
#     print(chunk)
    
# Asynchronous streaming example
# async for chunk in graph.astream(inputs, stream_mode="messages"):
#     print(chunk)
```

#### 📌 LLM Streaming Example:
This example demonstrates streaming token-by-token output from LLM calls within a LangGraph node.

```python
from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage # Ensure BaseMessage is imported
from typing import List, Annotated # Ensure List, Annotated are imported
import operator # For Annotated
import asyncio
# Ensure you have an LLM provider library, e.g., langchain_openai
# from langchain_openai import ChatOpenAI 

# Example: Define LLM models (replace with your actual model initializations)
# summary_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, tags=["summary_llm"])
# keyword_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, tags=["keyword_llm"])


# Define the state structure for the graph
class LLMStreamState(TypedDict):
    text_input: str
    summary_output: Annotated[List[BaseMessage], operator.add] # To accumulate streamed summary
    keywords_output: Annotated[List[BaseMessage], operator.add] # To accumulate streamed keywords
    current_operation: str # To track which LLM is active

# Define the node that calls the LLMs
async def multi_llm_call_node(state: LLMStreamState, config):
    text_to_process = state["text_input"]
    
    # These would be actual LLM calls that support streaming.
    # LangGraph's astream_events will pick up streaming from runnables tagged within the config.
    # The node itself returns the final aggregated content.
    
    # Simulate invoking summary model (actual call would be `await summary_model.ainvoke(...)`)
    # For demonstration, we'll assume the graph's streaming mechanism handles the token output.
    # This node's role is to orchestrate the calls.
    
    # To make this example runnable without actual LLM calls,
    # we'll just update the state to indicate completion.
    # In a real scenario, the LLM calls would happen here.
    # summary_content = (await summary_model.ainvoke(f"Summarize this: {text_to_process}", config)).content
    # keywords_content = (await keyword_model.ainvoke(f"Extract keywords from: {text_to_process}", config)).content

    # This node would typically return the final content after streaming is done by the LLMs.
    # For this example, we'll return placeholder messages.
    # The actual streaming is observed via graph.astream_events.
    return {
        "summary_output": [AIMessage(content="[Placeholder Summary Complete]")],
        "keywords_output": [AIMessage(content="[Placeholder Keywords Complete]")]
    }

# Build the graph
# graph_llm_stream = StateGraph(LLMStreamState)
# graph_llm_stream.add_node("multi_llm_call", multi_llm_call_node)
# graph_llm_stream.add_edge(START, "multi_llm_call")
# graph_llm_stream.add_edge("multi_llm_call", END)
# compiled_llm_graph = graph_llm_stream.compile()

async def stream_llm_output_main():
    sample_text = (
        "LangGraph is a library for building stateful, multi-actor applications with LLMs, "
        "built on top of (and intended to be used with) LangChain. "
        "It extends the LangChain Expression Language with the ability to coordinate multiple "
        "chains (or actors) across multiple steps of computation in a cyclic manner."
    )
    
    initial_graph_state = LLMStreamState(
        text_input=sample_text, 
        summary_output=[], 
        keywords_output=[],
        current_operation=""
    )

    print("--- Streaming Summary (simulated via tags if LLMs were real) ---")
    # To observe streaming from a specific LLM, you'd typically tag your LLMs
    # and then filter events by those tags in the config.
    # e.g., config={"configurable": {"tags": ["summary_llm"]}}
    # Since we are not making real LLM calls in multi_llm_call_node for this snippet,
    # we'll simulate iterating through events.
    
    # Example of how you would use astream_events with actual LLMs:
    # async for event in compiled_llm_graph.astream_events(
    #     initial_graph_state, 
    #     config={"configurable": {"tags": ["summary_llm"]}}, # Filter for summary LLM
    #     version="v2" # Required for astream_events
    # ):
    #     if event["event"] == "on_chat_model_stream":
    #         chunk = event["data"]["chunk"]
    #         if isinstance(chunk, AIMessageChunk): # AIMessageChunk has 'content'
    #             print(chunk.content, end="", flush=True)
    #     elif event["event"] == "on_chain_end" and event["name"] == "RunnableSequence": # Or your LLM chain name
    #         print("\n--- Summary Stream Ended ---")

    # print("\n\n--- Streaming Keywords (simulated) ---")
    # async for event in compiled_llm_graph.astream_events(
    #     initial_graph_state, 
    #     config={"configurable": {"tags": ["keyword_llm"]}}, # Filter for keyword LLM
    #     version="v2"
    # ):
    #     if event["event"] == "on_chat_model_stream":
    #         chunk = event["data"]["chunk"]
    #         if isinstance(chunk, AIMessageChunk):
    #             print(chunk.content, end="", flush=True)
    #     elif event["event"] == "on_chain_end" and event["name"] == "RunnableSequence":
    #         print("\n--- Keyword Stream Ended ---")
    
    # For now, as the node is placeholder:
    # final_state = await compiled_llm_graph.ainvoke(initial_graph_state)
    # print("\nFinal State (after placeholder execution):")
    # print(f"Summary: {final_state['summary_output'][-1].content}")
    # print(f"Keywords: {final_state['keywords_output'][-1].content}")
    pass

if __name__ == "__main__":
    # asyncio.run(stream_llm_output_main())
    pass
```

### Persistence
Many AI applications require memory to share context across multiple interactions. In LangGraph, you can add memory to any `StateGraph` using checkpointers. Checkpointers save the state of the graph at various points, allowing you to resume execution later or inspect intermediate states.

![](pictures/checkpoints_full_story.jpg)

#### 📌 Thread-Level Persistence
This is useful for maintaining conversation history or state within a single session or thread of execution. `MemorySaver` is an in-memory checkpointer.

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import List, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage # Ensure AIMessage is imported
import operator

# Define a state for messages
class MessagesState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

# Example model (replace with your actual model)
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(temperature=0)

def simple_chat_node(state: MessagesState):
    # response = model.invoke(state["messages"]) # Actual model call
    # Simulate response
    last_message = state["messages"][-1].content if state["messages"] else "no message"
    response = AIMessage(content=f"Echo: {last_message}")
    return {"messages": [response]}

# Setup graph with checkpointer
memory_checkpointer = MemorySaver()
chat_graph_builder = StateGraph(MessagesState)
chat_graph_builder.add_node("chat_node", simple_chat_node)
chat_graph_builder.add_edge(START, "chat_node")
chat_graph_builder.add_edge("chat_node", END) # Or loop back for continuous chat

# Compile with the checkpointer
persisted_chat_graph = chat_graph_builder.compile(checkpointer=memory_checkpointer)

# Example usage
if __name__ == "__main__":
    thread_id_1 = "user_session_1"
    config_1 = {"configurable": {"thread_id": thread_id_1}}

    print(f"--- Conversation for Thread ID: {thread_id_1} ---")
    initial_messages_1 = [HumanMessage(content="Hi! I'm Alex.")]
    for chunk in persisted_chat_graph.stream({"messages": initial_messages_1}, config_1, stream_mode="values"):
        if chunk["messages"]:
            chunk["messages"][-1].pretty_print()

    follow_up_messages_1 = [HumanMessage(content="What's my name?")]
    for chunk in persisted_chat_graph.stream({"messages": follow_up_messages_1}, config_1, stream_mode="values"):
        if chunk["messages"]:
            chunk["messages"][-1].pretty_print()

    # Demonstrate a different thread (no memory of Alex)
    thread_id_2 = "user_session_2"
    config_2 = {"configurable": {"thread_id": thread_id_2}}
    print(f"\n--- Conversation for Thread ID: {thread_id_2} ---")
    initial_messages_2 = [HumanMessage(content="What's my name?")]
    for chunk in persisted_chat_graph.stream({"messages": initial_messages_2}, config_2, stream_mode="values"):
        if chunk["messages"]:
            chunk["messages"][-1].pretty_print()
```

#### 📌 Cross-Thread Persistence
LangGraph also supports persisting data across **multiple threads**. The core is using the `Store` interface to store shared data across threads (e.g., user preferences). A `namespace` (e.g., `("memories", user_id)`) isolates different users’ memories.

#### 📌 Using Postgres Checkpointer for Persistence
For production environments, a database like PostgreSQL is a common choice for persistence. LangGraph provides `PostgresSaver` (sync) and `AsyncPostgresSaver` (async).

```python
from langgraph.checkpoint.postgres import PostgresSaver, AsyncPostgresSaver
# from psycopg_pool import ConnectionPool # For sync pool
# from psycopg import Connection, AsyncConnection # For sync/async connections
# from langgraph.prebuilt import create_react_agent # Example agent

# DB_URI = "postgresql://user:password@host:port/dbname?sslmode=disable" # Your DB URI
# connection_kwargs = {"autocommit": True, "prepare_threshold": 0}

# Synchronous Connection Examples:
# 1. With a direct connection:
# with Connection.connect(DB_URI, **connection_kwargs) as conn:
#     pg_checkpointer_sync = PostgresSaver(conn)
#     # config_tuple = pg_checkpointer_sync.get_tuple(config) # 'config' needs thread_id

# 2. With a connection pool:
# with ConnectionPool(DB_URI, kwargs=connection_kwargs) as pool:
#     pg_checkpointer_pool = PostgresSaver(pool)
#     # checkpoint = pg_checkpointer_pool.get(config)

# 3. With a connection string (recommended for simplicity):
# with PostgresSaver.from_conn_string(DB_URI) as pg_checkpointer_conn_str:
#     # react_agent_graph = create_react_agent(model, tools, checkpointer=pg_checkpointer_conn_str)
#     # checkpoint_tuples = list(pg_checkpointer_conn_str.list(config))
#     pass


# Asynchronous Connection Examples:
# 1. With a direct async connection:
# async def use_async_postgres_direct():
#     async with await AsyncConnection.connect(DB_URI, **connection_kwargs) as aconn:
#         pg_checkpointer_async_direct = AsyncPostgresSaver(aconn)
#         # checkpoint_tuple_async = await pg_checkpointer_async_direct.aget_tuple(config)

# 2. With an async connection pool (e.g., using psycopg_pool.AsyncConnectionPool):
# async def use_async_postgres_pool():
#     async with AsyncConnectionPool(DB_URI, kwargs=connection_kwargs) as apool:
#         pg_checkpointer_async_pool = AsyncPostgresSaver(apool)
#         # checkpoint_async = await pg_checkpointer_async_pool.aget(config)

# 3. With an async connection string (recommended for simplicity):
# async def use_async_postgres_conn_str():
#     async with AsyncPostgresSaver.from_conn_string(DB_URI) as pg_checkpointer_async_conn_str:
#         # react_agent_graph_async = await create_react_agent_async(model, tools, checkpointer=pg_checkpointer_async_conn_str) # Fictional async agent
#         # checkpoint_tuples_async = [c async for c in pg_checkpointer_async_conn_str.alist(config)]
#         pass

# Remember to run .setup() on the checkpointer once to initialize the necessary database tables before first use.
# For example:
# sync_cp = PostgresSaver.from_conn_string(DB_URI)
# sync_cp.setup()
# async_cp = AsyncPostgresSaver.from_conn_string(DB_URI)
# await async_cp.setup()
```
> 💡 You need to run `.setup()` on the checkpointer instance once to initialize the necessary database tables before first use.

### Logging & Monitoring (Observability)
LangSmith is specifically designed for **monitoring and debugging LLM applications**. It provides real-time tracking of workflows, model performance, and offers observability features optimized for large models, covering development, testing, and production. LangSmith is framework-agnostic—it can be used with LangChain and LangGraph, or standalone. For LangGraph, integrating LangSmith allows for generating traces of the entire pipeline, facilitating debugging and monitoring.

To use LangSmith, you typically set environment variables for your API key and project, and LangChain/LangGraph runnables will automatically log traces.

```
# Example environment variables for LangSmith:
# export LANGCHAIN_TRACING_V2="true"
# export LANGCHAIN_API_KEY="YOUR_LANGSMITH_API_KEY"
# export LANGCHAIN_PROJECT="Your_LangGraph_Project_Name" 
```
When these are set, graph invocations will be traced in LangSmith, providing visibility into each node's execution, inputs, outputs, and any LLM calls made.

---

