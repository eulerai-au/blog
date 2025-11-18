# **PageIndex: The Next Generation of Vector-Free, Reasoning-Based RAG, Letting Models "Think Before They Search"**

## I. From "Long Context" to "Smart Retrieval": The Bottleneck of RAG

Large Language Models (LLMs) have become the universal engines for document Q\&A and knowledge retrieval, but they face an unavoidable physical limitation: the **Context Window**—the maximum number of tokens they can read at once.

Even though today's models support hundreds of thousands of tokens, do they really "understand everything" when the context gets long? Research like Chroma's *Context Rot* suggests that as context length increases, recall accuracy actually decreases. In other words, if you stuff a thick book into the model, it might "look like it's trying hard, but it actually remembers very little."

Consequently, **Retrieval-Augmented Generation (RAG)** has become the mainstream solution: first "fish out the small handful of most relevant content" from documents, then feed it to the model, ensuring the limited context is used where it matters most.

Mainstream RAG solutions almost exclusively use vectors + vector databases. However, this approach is exposing increasing structural problems. To address this, the Vectify AI team has proposed a new direction: **PageIndex—a new generation RAG framework that does not rely on vector databases but is based on "reasoning navigation,"** allowing models to act like humans: "read the table of contents, find the chapter, and follow references down the line."

## II. Why Does Traditional Vector RAG Feel Clunky?

The classic Vector RAG workflow looks roughly like this:

1.  **Preprocessing:** Chunk the document (e.g., every 512 / 1000 tokens).
2.  **Embedding:** Turn each chunk into a vector using an embedding model.
3.  **Storage:** Save into a vector database (e.g., Chroma, Pinecone).
4.  **Query:** User Question → Vector → Find the "Top K most similar chunks" in the DB.
5.  Combine these chunks with the question and send them to the LLM to answer.

This system is practical for short texts and coarse-grained retrieval. However, in scenarios involving long documents or professional documentation, it hits a series of pain points:

1.  **Misalignment Between Query and Knowledge Space**
    Vector retrieval defaults to: Semantic Similarity = Highest Relevance. But user questions often express "intent" rather than raw text fragments found in the document. For example: "How does this report control risk exposure?" The document might not contain this exact sentence, but the answer is scattered across multiple risk management chapters.

2.  **Semantic Similarity $\neq$ True Relevance**
    In technical, legal, or financial documents, it is very common for two paragraphs to use highly similar wording but state completely different conclusions. Conversely, a paragraph containing a critical conclusion might use ordinary wording that doesn't look "semantically similar" enough, yet it is the most important. Vector retrieval is good at catching "surface-level linguistic similarity" but struggles to directly understand "which paragraph is actually critical in this context."

3.  **"Hard Chunking" Breaks Semantics and Logic**
    For embedding, documents must be cut into fixed-length chunks. Under this setting, a paragraph, a formula, or a subsection might be split across two chunks. One chunk might look relevant, but the complete derivation lies in the previous or next page. The model sees a "fragmented context," leading to misunderstandings, errors, or hallucinations.

4.  **Inability to Naturally Utilize Chat History**
    Most Vector RAGs treat every query as an independent retrieval event. The retriever doesn't know what you asked before, what you've seen, or which paragraph the current topic continues from. This leads to a disjointed multi-turn Q\&A experience: the user is asking follow-up questions coherently, but the retriever treats every input as a "fresh question."

5.  **In-Text Citations Are Almost Impossible to Handle**
    Documents are full of sentences like: "See Appendix G," "Refer to Table 5.3," "As shown in Figure 7...". These directional relationships are barely captured in the semantic vector space: "Appendix G" and the actual content of the appendix look nothing alike. Unless you manually build a knowledge graph during preprocessing, Vector RAG often suffers from "broken links."

For these reasons, advanced systems (including Claude Code) have abandoned traditional Vector RAG in coding scenarios, switching to more structured, vector-free retrieval methods to gain precision and speed. Extending this logic to the world of documents gives us what we are discussing today: PageIndex.

## III. PageIndex: Let the Model Read the Table of Contents Before Searching

**The core idea of PageIndex is simply this:**

> Do not shatter the document into vectors for fuzzy matching first; instead, turn the document into a "reason-able directory tree," letting the model walk the tree and look up the original text.

It simulates the natural process of a **"human reading a long document":** When you encounter a question, you don't start gnawing from page one. Instead, you:

1.  **Glance at the Table of Contents (ToC)** to see which chapters might be relevant.
2.  **Lock onto one or two chapters** to read in detail.
3.  If not enough, check **adjacent sections / appendices / tables**.
4.  Constantly refine your judgment during this process until the information is sufficient to answer the question.

PageIndex mechanizes this process, letting the LLM work in an iterative loop:

![image.png](image/image.png)

1.  **Read ToC / PageIndex Tree:** Understand the overall document structure and identify potentially relevant chapters/subsections.
2.  **Select a Chapter:** Based on the current question, pick the node most likely to contain the information.
3.  **Extract Node Content:** Use the `node_id` to precisely pull the original text/tables/images.
4.  **Judge: Is the information sufficient?**
      * If "Yes," enter the answering phase.
      * If "No," return to the directory and pick the next batch of nodes to review.
5.  **Generate Answer based on collected content.**

In this process, the **Table of Contents (ToC / index tree) acts as the model's "internal index."** The model isn't looking for "similar vectors" in a library; it is performing "reasoning navigation" on a directory tree.

## IV. Turning Documents into a JSON Tree: The PageIndex Tree

To let the LLM "understand the directory," PageIndex unifies the document structure into a JSON tree, known as the **PageIndex Tree**. Each node represents a logical part of the document: chapter, subsection, paragraph, page... The structure is roughly as follows:

```json
Node {
  node_id: string,      // Unique Node ID
  name: string,         // Title or Label (e.g., 3.2 Bayesian Linear Regression)
  description: string,  // Summary of what this part is about (Optional)
  metadata: object,     // Any context info (source, page range, topic, tags, etc.)
  sub_nodes: [Node]     // Child nodes (Recursive structure)
}
```

Where:

  * **`node_id` is the "Index Key":**
    It allows for the accurate retrieval of the corresponding original content (text, images, tables, etc.).
  * **`sub_nodes` supports multi-level nesting:**
    This tree can be as granular as "Chapter → Subsection → Paragraph → Page Range."
  * **`metadata` holds various auxiliary information:**
    Such as page intervals, document types, tags, timestamps, relevance scores...
    These metadata can also serve as signals for "reasoning navigation."

Unlike the "external static index" of vector databases, in PageIndex:

  * The model can **recursively traverse, compare, and filter** on this tree.
  * It can reverse-lookup original content via `node_id`.
  * It can decide "where to check next" dynamically based on the question while looking at the ToC.

PageIndex calls this method: **"In-context index."**

## V. How Does PageIndex Solve the 5 Major Pain Points of RAG?

Let's look at how PageIndex resolves the 5 problems mentioned earlier one by one.

1.  **Mismatch of Query and Knowledge Space**

    *Traditional Vector RAG:*

    > "I'll throw whoever looks semantically most similar to this question at the model."

    *PageIndex:*

    > "Let me think. Logically, where should the answer to this question be hiding in this book?"

    For example: "Where is the total value of deferred assets?" The model can reason within the directory:

    > "Asset totals are usually in financial statements or statistical appendices, so let's check the appendices and statistical tables first."

    In other words, **shifting from "how similar are the sentences" to "reasoning where this type of information usually resides."**

2.  **Semantic Similarity $\neq$ True Relevance**

    In PageIndex, the model first reads and analyzes the **Title + Summary + Metadata** of the ToC nodes. For a question like "How to avoid overfitting?", PageIndex considers the intent of the question and compares the **role and context** of each node in the entire book. It finds the parts that actually discuss "regularization mechanisms" or "model complexity control," rather than just sentences that literally contain the word "overfitting." Therefore, it retrieves content that is **"most relevant in context,"** not just sentences with similar wording.

3.  **"Hard Chunking" Destroys Semantic Integration**

    PageIndex no longer brutally chops text by fixed token length but retrieves by **Chapter/Subsection/Page Range**:

      * One node = One semantically complete logical block.
      * If the current node is insufficient, the model can **explicitly request adjacent nodes** (e.g., the next subsection, other parts of the same chapter).

    This is closer to how humans read documents:

    > "I didn't quite get this section, let me flip back a page or read the next page."

4.  **Inability to Utilize Chat History**

    Since the PageIndex retrieval process is **reasoning-driven + multi-turn iterative**, it naturally integrates with conversation context:

      * The model remembers what you asked before and which nodes it has seen.
      * New questions can be understood as **extensions of the previous round**.
          * Example: First ask "How are financial assets defined?", then ask "What about liabilities?"
          * The model will automatically focus on the "Liabilities" related chapters in the same report, rather than searching randomly across the global scope again.

5.  **Cross-Document Citations Finally "Work"**

    The directory tree of PageIndex preserves the **hierarchy and associations between chapters**. When the text says:

    > "Refer to the statistical table in Appendix G"

    The model can:

    1.  See "Appendix G" in the sentence.
    2.  Go back to the PageIndex Tree to find the "Appendix G" node.
    3.  Pull the corresponding table content via `node_id`.
    4.  Synthesize the answer based on this foundation.

    This is crucial: The model can perform "tracking and jumping" using the structure of the directory itself without needing a manually constructed knowledge graph.

## VI. Vector RAG vs. Reasoning RAG: A Comparison Table

| Limitation | Approach of Vector RAG | Approach of PageIndex Reasoning RAG |
| :--- | :--- | :--- |
| **1. Query/Knowledge Mismatch** | Looks only at semantic similarity; may miss truly relevant chapters. | Reads the directory first, then reasons "where the answer likely lies." |
| **2. Semantics $\neq$ Relevance** | Prone to retrieving paragraphs that sound similar but are unimportant. | Emphasizes "role" in context and document structure to find truly key info. |
| **3. Hard Chunking** | Fixed token chunking breaks complete chapters. | Retrieves by Chapter/Subsection; expands structurally (forward/backward) if needed. |
| **4. No Chat Context** | Each retrieval is an isolated event. | Retrieval is a multi-turn reasoning process that fuses chat history. |
| **5. In-Text Citations** | Hard to track references like "Appendix" or "Table." | Uses ToC/PageIndex tree to naturally follow citation nodes. |

The difference between PageIndex (Reasoning RAG) and Vector RAG can be summarized in one sentence:

> Vector RAG is "finding similar text"; Reasoning RAG is "thinking about where to look and why to go there."

## VII. PageIndex Chat: A Classic Use Case

Taking *Pattern Recognition and Machine Learning* (Bishop) as an example, suppose a user asks:

> "How does Bayesian inference prevent overfitting?"

The overall flow of PageIndex is roughly as follows:

1.  **First, get the JSON directory tree of the entire book**
    Call `get document structure` to retrieve the `node_id`, title, and summary of each chapter/subsection.

    ![image.png](image/image%201.png)

2.  **"Think" on the directory tree about where to go**
    The model matches keywords like *Bayesian inference* and *overfitting* from the question against the title and summary of each node. For example:

      * Chapter 3 "Bayesian Linear Regression"
      * "The Evidence Approximation"
      * "Bayesian curve fitting" in Chapter 1, etc.

    And selects a few nodes most likely to hide the answer.

    ![image.png](image/image%202.png)

3.  **Precisely pull original content via `node_id`**
    PageIndex calls `get page content` to fetch the page ranges corresponding to these nodes, obtaining key paragraphs about "integration over parameters instead of point estimation," automatic regularization brought by prior distributions, effective number of parameters $\gamma$, model evidence, and Occam's razor.

4.  **Reason over this "planned-by-chapter" content**
    Finally, output a structured answer: explaining how Bayesian inference naturally avoids overfitting through mechanisms like priors and model evidence.

    ![image.png](image/image%203.png)

This process has a distinct characteristic: The model is not "blindly vector searching" across the whole book, but rather performing **"Zonal Positioning → Precise Drill-down → Multi-round Supplementation"** on the directory. This is exactly the **"Reasoning Navigation + Fine-grained Content Extraction"** that PageIndex emphasizes.

## VIII. PageIndex MCP: Enabling in Tools like Claude

PageIndex also supports the MCP protocol and can serve as an "external brain" for tools like Claude.

Taking Claude as an example, the setup steps are very simple:

1.  Select "Add custom connectors" in settings.
2.  Add the PageIndex service with the URL: `https://mcp.pageindex.ai/mcp`
3.  Login and authorize.
4.  Afterward, you can directly call PageIndex within Claude to perform "Directory Reasoning + Precise Original Text Retrieval" on long documents.

This way, you don't need to build a vector database yourself or hand-code complex retrieval logic. Just connect your documents to PageIndex, and you can give Claude the ability to "flip through a book to find answers like a human."

## IX. From "Piling Vectors" to "Teaching Models to Read Directories"

To end this article with a comparison:

  * The mindset of **Traditional Vector RAG** is:

    > "I'll chop the document, embed it, and store it. You match the similarity."

  * The mindset of **PageIndex** is:

    > "I'll organize the document into a clear directory tree. You think clearly about where to check first, then pull out the truly useful content step by step."

In scenarios involving long, structured, and professional documents (law, finance, technical white papers, textbooks...), **the latter is often closer to how human experts work** and aligns better with our expectations of "intelligent retrieval."

If you are:

  * Building an internal enterprise knowledge Q\&A system
  * Analyzing long documents/reports or navigating codebases
  * Wondering "Why does the model often give irrelevant answers even though I have a vector database?"

Try changing your approach: **Let the model understand the directory first, then look for the answer.**

## References

1.  [https://pageindex.ai/blog/pageindex-intro](https://pageindex.ai/blog/pageindex-intro)
2.  [https://chat.pageindex.ai/chat](https://chat.pageindex.ai/chat)
3.  [https://pageindex.ai/mcp](https://pageindex.ai/mcp)