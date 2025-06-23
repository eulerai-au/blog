# Supabase Research Report

Supabase is a managed platform for PostgreSQL that enhances the following features:

1、Out-of-the-box pgvector: Direct support for AI vector storage.

2、Real-time API: Pushes database changes via WebSockets.

3、Management Interface: Visual operations for tables, permissions, and SQL editor.


# A simple vector storage demo and a basic RAG Q&A implementation integrated with OpenAI's service: 

Official reference documentation: https://python.langchain.com/docs/integrations/vectorstores/supabase/


``` python
# Install necessary libraries
!pip install --upgrade --quiet langchain langchain_community langchain-openai tiktoken supabase unstructured

# Import relevant modules
import os
from google.colab import userdata

os.environ["SUPABASE_URL"] = userdata.get('SUPABASE_URL')
os.environ["SUPABASE_SERVICE_KEY"] = userdata.get('SUPABASE_SERVICE_KEY')
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')  #OPENAI_API_KEY

from langchain_community.vectorstores import SupabaseVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from supabase.client import Client, create_client

# Configure Supabase client
supabase_url = "https://nggaknpgnesrwhoscznych.supabase.co"  
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5nZ2FrbnBnbmVzcndob3Njem55Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjM2NzgsImV4cCI6MjA2Mzg5OTY3OH0.oR5B_6tzpE8wbbARbbamERjZADb7JdxNIxp2L3bm8eY" 
supabase: Client = create_client(supabase_url, supabase_key)

# OpenAI Embedding
embeddings = OpenAIEmbeddings()

from langchain_community.document_loaders import UnstructuredURLLoader

# Load the webpage to analyze
urls = [ "https://supabase.com/blog/openai-embeddings-postgres-vector" ]


loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()

# Import document splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

# Split the loaded documents
splits = text_splitter.split_documents(docs)

# Convert documents into vector storage and store in Supabase
vectorstore = SupabaseVectorStore.from_documents(
    splits,
    embeddings,
    client=supabase,
    table_name="documents", 
    query_name="match_documents", 
)

# Create a retriever using similarity search
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# Execute a retrieval query to find documents related to the question
retrieved_docs = retriever.invoke("How to store embeddings with pgvector?")

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template for Q&A tasks
prompt = '''
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
'''

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = ({"context": (retriever | format_docs), "question": RunnablePassthrough()}
             | ChatPromptTemplate.from_template(prompt)
             | ChatOpenAI(model="gpt-3.5-turbo-0125")  # Using OpenAI's GPT-3.5 model
             | StrOutputParser()) 

rag_chain.invoke("How to store embeddings with pgvector?")

```

**Result: ![img.png](pictures/result.png)**

**Vector Database Storage:![img.png](pictures/vector database.png)**

# Query Methods

**Supabase includes a SQL editor that supports all PostgreSQL syntax**

SELECT, INSERT, UPDATE, DELETE

JOIN, GROUP BY, ORDER BY, WHERE

Complex subqueries, WITH, window functions

Full-text search

JSON and JSONB query support

**Supabase natively supports the pgvector extension, which can be used to build vector search engines and integrates seamlessly with large language models (LLMs)**

```SQL
SELECT *
FROM documents
ORDER BY embedding <-> '[0.1, 0.3, 0.9]'::vector
LIMIT 5;
```

Supports Euclidean distance, cosine similarity, and negative inner product.

Use cases: RAG (Retrieval-Augmented Generation), similar content recommendations, embedding search.

# Auth
Supabase Auth makes it easy to implement authentication and authorization in applications. It provides client SDKs and API endpoints to help create and manage users.

| Supported Authentication Methods	    | Method                                                        | Description                                               |
|----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| Email/Password           | Traditional Email + Password Login                                                     | Supports password hashing and password reset process                           |
| Magic Link          | Passwordless Login                                                         | Users receive a one-time login link via email                      |
| OAuth Third-Party Login     | Supports 20+ providers like Google, GitHub, Apple, Facebook, Twitter, Azure, GitLab, etc. | Offers support for various third-party service providers                             |
| Phone Number Login           | Login via SMS Code                                                     | Relies on SMS service providers                       |
| Anonymous Login             | Generate Temporary User                                                              | Provides a login method without registration                       |


# Supabase Realtime Updates 

Imagine building a chat application or a real-time dashboard. You want users to see new messages or updated data instantly without refreshing the page. This is where Supabase Realtime comes in.

Supabase uses PostgreSQL's **LISTEN/NOTIFY** feature to provide real-time updates whenever data changes. No manual refreshing required.

# Pricing

Supabase offers four pricing plans tailored to different user needs: Free, Pro, Team, and Enterprise.

**Free Plan**

Price: $0 / month

Ideal for: Prototyping, small projects, personal experiments

Includes:

Unlimited API requests

50,000 active users per month

500 MB database (shared CPU, 500 MB RAM)

5 GB bandwidth

1 GB file storage

Community support

**Pro Plan (Starting at $25/month)** 

Price: $25 / month

Ideal for: Small to medium-sized applications in production

Includes (expands on Free Plan):

100,000 active users per month (additional users at $0.00325 each)

8 GB database per project (additional storage at $0.125/GB)

250 GB bandwidth (additional at $0.09/GB)

100 GB file storage (additional at 0.021/GB)

Email support:

Daily backups (retained for 7 days)

Log retention for 7 days

The Pro Plan is suitable for developers scaling their deployments, offering good scalability and cost transparency.

**Team Plan (Starting at $599/month)**

Ideal for: Medium-sized teams requiring audit compliance and advanced access control

Includes (expands on Pro Plan):

SOC2 compliance support

Project-level and read-only access control

HIPAA compliance add-on

Single Sign-On (SSO) support

Priority email support + SLA

Daily backups retained for 14 days

Log retention for 28 days

Best for scenarios requiring higher security, compliance, and team collaboration controls.

**Enterprise Plan (Custom Pricing)**


# Comparison with Similar Products (Firebase, Supabase, Cloudflare, Upstash)

**Database Capabilities Comparison**

Supabase: Uses PostgreSQL, a relational database supporting complex queries, transactions, and table structures.

Firebase: Uses Firestore, a NoSQL database designed for real-time data sync, ideal for flexible document structures.

Cloudflare: Uses D1 (SQLite), a lightweight relational database for small apps, supporting basic SQL operations but with limited functionality.

Upstash: Primarily uses Redis and Kafka for efficient data caching and stream processing. Redis is a key-value store, while Kafka handles large-scale event streams.

Supabase: Supports the pgvector extension, enabling vector searches in PostgreSQL, ideal for embedding searches or similarity matching (e.g., recommendation systems, image retrieval).

Firebase: Does not support vector search. Focuses on real-time and unstructured data storage.

Cloudflare: Does not support vector search. Focuses on edge computing and caching.

Upstash: Does not support vector search. Focuses on efficient caching and event stream processing.

| Feature           | Supabase                 | Firebase              | Cloudflare           | Upstash               |
|----------------|--------------------------|-----------------------|----------------------|-----------------------|
| Database Type     | PostgreSQL                | Firestore (NoSQL)     | D1 (SQLite)          | Redis/Kafka           |
| ACID Transactions       | Full support                  | Limited support               |  (D1)               | ❌                    |
| Vector Search       | pgvector extension	              | ❌                       | ❌                    | ❌                    |



**Core Positioning Comparison**

| Platform        | Core Positioning                          | Tech Stack                 | Open Source Status        |
|-------------|-----------------------------------|------------------|-----------------|
| **Supabase** | Firebase alternative for PostgreSQL ecosystem   | PostgreSQL + open-source tools | Core components open-source    |
| **Firebase** | Google's full-stack mobile/Web solution  | Proprietary NoSQL database       | Closed-source            |
| **Cloudflare** | 	BaaS service for edge networking    | Workers + D1     | Partially open-source      |
| **Upstash**  | Serverless Redis/Kafka service      | Redis/Kafka      | Partially open-source           |


**Recommended Use Cases**

| Platform        | Best Use Cases                                      |
|-------------|-------------------------------------------------|
| **Supabase** | Web apps needing relational databases, AI integration, traditional backend replacement |
| **Firebase** | Rapid mobile app development, Google ecosystem integration, real-time collaboration apps |
| **Cloudflare** | Edge computing apps, globally distributed services, deep CDN integration |
| **Upstash**  | Apps requiring Serverless Redis/Kafka |


# Conclusion
**Ideal Use Cases for Supabase**

Full-stack apps requiring rapid development: Out-of-the-box Auth, real-time API, storage, and database.

Supabase natively supports the pgvector plugin, enabling efficient vector searches in the database. Ideal for:

Small to medium-scale RAG projects. The Pro Plan ($25/month) supports 8GB of vector data.

Upload text vectors → Store in Supabase → Query semantic similarity using pgvector → Integrate with LLMs for Q&A.

Supabase's Realtime module (based on PostgreSQL logical replication + WebSocket) is perfect for:

Chatrooms / message notification systems.

Collaborative editing.

