# Supabase 调研报告

Supabase 是 PostgreSQL 的托管平台，增强了以下功能：

1、开箱即用的 pgvector：直接支持 AI 向量存储。

2、实时 API：通过 WebSockets 推送数据库变更。

3、管理界面：可视化操作表、权限和 SQL 编辑器。


# 一个简单的存储向量demo以及结合 OpenAI 的服务的简单RAG问答实现： 

官方参考文档：https://python.langchain.com/docs/integrations/vectorstores/supabase/


``` python
# 安装必要的库
!pip install --upgrade --quiet langchain langchain_community langchain-openai tiktoken supabase unstructured

# 导入相关模块
import os
from google.colab import userdata

os.environ["SUPABASE_URL"] = userdata.get('SUPABASE_URL')
os.environ["SUPABASE_SERVICE_KEY"] = userdata.get('SUPABASE_SERVICE_KEY')
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')  #OPENAI_API_KEY

from langchain_community.vectorstores import SupabaseVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from supabase.client import Client, create_client

# 配置Supabase客户端
supabase_url = "https://nggaknpgnesrwhoscznych.supabase.co"  
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5nZ2FrbnBnbmVzcndob3Njem55Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjM2NzgsImV4cCI6MjA2Mzg5OTY3OH0.oR5B_6tzpE8wbbARbbamERjZADb7JdxNIxp2L3bm8eY" 
supabase: Client = create_client(supabase_url, supabase_key)

# OpenAI Embedding
embeddings = OpenAIEmbeddings()

from langchain_community.document_loaders import UnstructuredURLLoader

# 加载需要分析的网页
urls = [ "https://supabase.com/blog/openai-embeddings-postgres-vector" ]


loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()

# 导入文档拆分器
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

# 拆分加载的文档
splits = text_splitter.split_documents(docs)

# 将文档转化为向量存储，存储在Supabase中
vectorstore = SupabaseVectorStore.from_documents(
    splits,
    embeddings,
    client=supabase,
    table_name="documents", 
    query_name="match_documents", 
)

# 创建检索器，使用相似度搜索
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# 执行检索查询，找出与问题相关的文档
retrieved_docs = retriever.invoke("How to store embeddings with pgvector?")

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 定义问答任务的提示模板
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
             | ChatOpenAI(model="gpt-3.5-turbo-0125")  # 使用OpenAI的GPT-3.5模型
             | StrOutputParser()) 

rag_chain.invoke("How to store embeddings with pgvector?")

```

**效果： ![img.png](pictures/result.png)**

**向量数据库存储：![img.png](pictures/vector database.png)**

# 查询方式

**Supabase 附带一个 SQL 编辑器，支持全部 PostgreSQL 语法**

SELECT, INSERT, UPDATE, DELETE

JOIN, GROUP BY, ORDER BY, WHERE

复杂的子查询, WITH, 窗口函数

全文搜索

支持JSON查询 

**Supabase 原生支持 pgvector 扩展，可用于构建向量搜索引擎，与大模型（LLM）结合非常方便**

```SQL
SELECT *
FROM documents
ORDER BY embedding <-> '[0.1, 0.3, 0.9]'::vector
LIMIT 5;
```

支持欧式距离，余弦相似度，负内积   

应用场景：RAG（检索增强生成）、相似内容推荐、嵌入搜索

# Auth
Supabase Auth 可以轻松地在应用程序中实现身份验证和授权。提供客户端 SDK 和 API 终端节点来帮助创建和管理用户

| 支持的身份验证方式    | 方式               | 描述                                                |
|----------------------|--------------------|-----------------------------------------------------|
| 邮箱/密码            | 传统邮箱+密码登录  | 支持密码哈希和密码重置流程                           |
| Magic Link          | 无密码登录         | 用户通过邮箱接收一次性登录链接                       |
| OAuth 第三方登录     | 支持 Google、GitHub、Apple、Facebook、Twitter、Azure、GitLab 等 20+ 提供商 | 提供多种第三方服务商支持                             |
| 手机号登录           | 通过短信验证码登录 | 依赖 SMS 服务商                       |
| 匿名登录             | 生成临时用户       | 提供无需注册的临时用户登录方式                       |


# Supabase 实时更新 

想象正在构建一个聊天应用或一个实时仪表板。希望用户能够立刻看到新消息或更新的数据，无需刷新页面。这时，Supabase 实时就派上用场了。

Supabase 使用 PostgreSQL 的 **LISTEN/NOTIFY** 功能，每当数据发生变化时实时更新。无需手动刷新



# 成本

Supabase 提供四种不同的定价计划，分别针对不同规模的用户需求：Free（免费）、Pro（专业版）、Team（团队版）和 Enterprise（企业版）

**Free Plan（免费版）**

价格：$0 / 月

适用场景：原型开发、小项目、个人实验

包含资源： 

无限 API 请求  

每月 50,000 活跃用户   

数据库大小 500 MB（共享 CPU，500 MB RAM） 

5 GB 带宽  

1 GB 文件存储

社区支持

**Pro Plan（$25/月起)** 

价格：$25 / 月起

适用场景：生产环境中的中小型应用

包含资源（在免费计划基础上扩展）：

每月 100,000 活跃用户，超出部分每人 0.00325

每项目 8 GB 数据库（之后 0.125/GB）

250 GB 带宽（之后 0.09/GB）

100 GB 文件存储（之后 0.021/GB）

邮件支持
日常备份（保存 7 天）
日志保留 7 天

Pro 计划适合进入规模化部署阶段的开发者，具有良好的扩展性与成本透明度

**Team Plan（$599/月起)**


适用场景：中型团队、需要审计合规与高级访问控制

包含资源（在 Pro 基础上增加）：

SOC2 合规支持

项目级和只读访问控制

支持添加 HIPAA 合规

单点登录（SSO）支持

优先邮件支持 + 服务等级协议（SLA）

日常备份保存 14 天

日志保留 28 天

适合需要更高安全合规性和团队协作控制的场景。

**Enterprise Plan（定制价格）**


# 同类型产品对比（Firebase, Supabase, Cloudflare, Upstash）

**数据库能力对比**

Supabase：使用的是PostgreSQL，这是一种关系型数据库，支持复杂查询、事务、和表结构等。

Firebase：使用的是Firestore，它是一个NoSQL数据库，专为实时数据同步设计，适用于灵活的文档结构。

Cloudflare：使用的是D1 (SQLite)，SQLite 是一个轻量级的关系型数据库，适用于小型应用，支持基本的SQL操作，但功能相对简单。

Upstash：主要使用Redis和Kafka，两者都是用于高效的数据缓存和流式数据处理，Redis 是一个键值存储，而 Kafka 用于处理大规模的事件流。

Supabase：支持pgvector扩展，pgvector 是一个允许在 PostgreSQL 中执行向量搜索的扩展，适用于需要搜索嵌入向量或相似度匹配的场景（如推荐系统、图像检索等）。

Firebase：不支持向量搜索。Firebase 主要聚焦于实时数据和非结构化数据的存储，不适用于处理向量数据。

Cloudflare：不支持向量搜索。Cloudflare 主要提供边缘计算和缓存服务，重点不在向量搜索或复杂的数据库查询上。

Upstash：不支持向量搜索，Upstash 的重点是高效的缓存和事件流处理。

| 特性           | Supabase                 | Firebase              | Cloudflare           | Upstash               |
|----------------|--------------------------|-----------------------|----------------------|-----------------------|
| 数据库类型     | PostgreSQL                | Firestore (NoSQL)     | D1 (SQLite)          | Redis/Kafka           |
| ACID事务       | 完整支持                  | 有限支持               |  (D1)               | ❌                    |
| 向量搜索       | pgvector扩展              | ❌                       | ❌                    | ❌                    |



**核心定位对比**

| 平台        | 核心定位                          | 技术栈                    | 开源情况        |
|-------------|-----------------------------------|---------------------------|-----------------|
| **Supabase** | PostgreSQL生态的Firebase替代品   | PostgreSQL + 开源工具      | 核心组件开源    |
| **Firebase** | Google生态的全套移动/Web解决方案  | 专有NoSQL数据库            | 闭源            |
| **Cloudflare** | 边缘网络基础设施扩展的BaaS服务    | Workers + D1              | 部分开源        |
| **Upstash**  | Serverless Redis/ Kafka服务      | Redis/Kafka               | 闭源            |


**推荐场景**

| 平台        | 最佳使用场景                                      |
|-------------|-------------------------------------------------|
| **Supabase** | 需要关系型数据库的Web应用、AI集成项目、替代传统后端 |
| **Firebase** | 移动应用快速开发、需要Google生态集成、实时协作应用 |
| **Cloudflare** | 边缘计算应用、全球分布式服务、需要与CDN深度整合 |
| **Upstash**  | 需要Serverless Redis/Kafka的应用 |


# 结论
**Supabase适合使用场景**

需要快速开发的全栈应用：提供开箱即用的身份验证（Auth）、实时API、存储和数据库

Supabase 原生支持 pgvector 插件，可以直接在数据库中进行高效的向量搜索，适合：中小规模知识库RAG项目 专业版（$25/月）支持 8GB 向量数据
上传文本向量 → 存入 Supabase → 使用 pgvector 查询相似语义 → 配合 LLM 实现问答

Supabase 的 Realtime 模块（基于 PostgreSQL logical replication + WebSocket），非常适合： 聊天室 / 消息通知系统、协作编辑



