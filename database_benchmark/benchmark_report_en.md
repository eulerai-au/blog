# Comprehensive Comparison Report of Modern Databases: PostgreSQL, SurrealDB, Redis, MongoDB, SQLite, and TiKV

This report provides a comprehensive comparison of six mainstream database systems, covering multiple dimensions such as data type flexibility, scalability, resource usage, concurrency performance, transaction support, query capabilities, ecosystem compatibility, ease of integration, and licensing. Each database has its unique features and is suitable for different application scenarios. This report will help you make the best choice based on your specific needs.

**PostgreSQL** is the best choice for general-purpose scenarios.

## Current [Database Rankings](https://db-engines.com/en/ranking) TOP-30
![alt text](image.png)

## Comparison of Open Source Status of Databases

*Table: Open Source Status Comparison*
| Project              |  Stars | Commits | Issues (Open) |  Forks | PR Creators | Main Language |
| :------------------- | -----: | ------: | ------------: | -----: | ----------: | :------------ |
| postgres/postgres    | 18,201 |  45,250 |             0 |  4,880 |         135 | C             |
| surrealdb/surrealdb  | 29,160 |   8,988 |         2,856 |    982 |         182 | Rust          |
| redis/redis          | 72,290 |  11,453 |         6,462 | 23,975 |       1,685 | C             |
| mongodb/mongo        | 28,977 |  80,544 |             0 |  5,649 |         657 | C++           |
| sqlite/sqlite        |  7,825 |   9,607 |             0 |  1,148 |          24 | C             |
| tikv/tikv            | 16,224 |  18,818 |         5,323 |  2,176 |         510 | Rust          |

*Table: Last 28 Days Overview*
| Project              | Stars (28 Days) | PRs Opened | PRs Merged | Issues Opened | Issues Closed | Commits (28 Days) |
| :------------------- | ---------------: | ---------: | ---------: | ------------: | ------------: | ----------------: |
| postgres/postgres    |              244 |          3 |          0 |             0 |             0 |                429 |
| surrealdb/surrealdb  |              201 |         56 |         39 |            36 |            19 |                296 |
| redis/redis          |              370 |         45 |         24 |            22 |            16 |                209 |
| mongodb/mongo        |              153 |          0 |          0 |             0 |             0 |              2,328 |
| sqlite/sqlite        |              134 |          2 |          0 |             0 |             0 |                 95 |
| tikv/tikv            |               91 |         40 |         43 |            20 |            24 |                 41 |

Based on the data from the above tables, the horizontal comparison of these databases in terms of open source status can be divided into the following dimensions:

### 1. **Community Activity**
   - **Stars**: 
     - Redis has the most Stars (72,290), showing its popularity in the community.
     - SurrealDB follows closely (29,160), attracting significant attention despite being a newer project.
     - SQLite has the fewest Stars (7,825), likely due to its positioning as an embedded database.
   - **Stars Growth in the Last 28 Days**:
     - Redis leads again (370), while Postgres (244) and SurrealDB (201) also show active growth.
     - TiKV has the least growth (91), indicating slower community expansion.

### 2. **Developer Participation**
   - **Commits**:
     - MongoDB has the highest cumulative commits (80,544), reflecting its development intensity and long-term maintenance.
     - In the last 28 days, MongoDB still leads (2,328), showcasing continuous development efforts.
     - SQLite has fewer commits, possibly because its functionality is relatively stable.
   - **PR Creators**:
     - Redis has the most PR creators (1,685), indicating a large number of contributors.
     - SQLite has only 24 PR creators, showing the least participation.

### 3. **Issue and Demand Response**
   - **Issues (Open)**:
     - Redis (6,462) and TiKV (5,323) have the most unresolved issues, indicating high user demand and feedback.
     - SurrealDB also has a significant number of unresolved issues (2,856) among open-source projects.
     - Postgres, MongoDB, and SQLite show zero open issues, possibly because they manage issues through other channels (e.g., mailing lists).
   - **Issues in the Last 28 Days**:
     - SurrealDB and TiKV show strong user interaction, with 36 and 20 new issues opened and 19 and 24 issues closed, respectively.
     - Redis also opened 22 new issues and closed 16, demonstrating good responsiveness.

### 4. **Code Contributions**
   - **Forks**:
     - Redis (23,975) and MongoDB (5,649) lead in the number of forks, indicating high developer interest in their code.
     - SQLite has fewer forks (1,148), likely due to its nature as an embedded database.
   - **PRs (Pull Requests)**:
     - Redis performs well in both cumulative and recent PRs, with 1,685 contributors and 45 new PRs in the last 28 days.
     - TiKV has the most merged PRs in the last 28 days (43), showing rapid development iterations.
     - Postgres has no merged PRs in the last 28 days, possibly due to high merging thresholds or maintenance strategies.

### 5. **Primary Language**
   - C dominates Postgres, Redis, and SQLite, indicating a focus on performance.
   - Rust-based databases (SurrealDB and TiKV) represent modern development trends, emphasizing safety and concurrency.
   - MongoDB uses C++, balancing complex functionality and performance.

---

### Summary
- **Redis**: Excels in community popularity, developer participation, and demand response, showcasing its value as a mature and efficient in-memory database.
- **MongoDB**: Leads in commits and contributors, suitable for scenarios requiring complex functionality and stability.
- **SurrealDB**: Rapid community growth, especially popular in the Rust ecosystem.
- **Postgres**: A classic database with high Stars and Forks, with contributors likely preferring mailing lists and community discussions over GitHub.
- **SQLite**: A lightweight and stable embedded database with low community participation but minimal maintenance needs.
- **TiKV**: A Rust-based project with recent active development, suitable for distributed storage and high-performance scenarios.

## Data Type Flexibility Comparison

**PostgreSQL** excels in data type support, earning the title of "**most flexible relational database**". It not only supports traditional relational data but also provides complete document storage capabilities through JSON/JSONB types. PG's extension ecosystem is particularly impressive—through extensions, it can support vectors (pgvector), time series (TimescaleDB), graph data (AGE), and many other specialized data types. This "**jack of all trades, master of many**" characteristic enables PostgreSQL to replace many specialized databases, making it a true full-stack database solution.

**SurrealDB**, as an emerging multi-model database, has its greatest advantage in **simultaneously supporting relational, document, and graph data models**. It stores data in JSON format, supports complex nested structures, and has a built-in GraphQL interface, making relationship data handling intuitive. Notably, SurrealDB allows developers to query graph data using familiar SQL syntax, significantly reducing the learning curve. For application scenarios requiring both document and relational processing, SurrealDB offers unique value.

**MongoDB** is a **typical representative of document databases**, using BSON (Binary JSON) format to store highly flexible unstructured data. MongoDB 8.0 further optimizes performance, with read and write operations improved by 20-36% and 35-58% respectively compared to version 7.0. Its "**schema-free**" feature allows documents in the same collection to have different structures, ideal for rapidly iterating development scenarios. However, MongoDB is less intuitive than relational databases when handling strongly structured data.

**Redis**, as an in-memory key-value database, supports **multiple basic data structures**: strings, lists, sets, sorted sets, and hashes. Although its data structures are relatively simple, Redis extends its capabilities through the module system (such as RedisSearch, RedisJSON) to handle JSON documents, perform full-text searches, and more. Redis's high-performance in-memory characteristics make it an ideal choice for caching and session storage.

**SQLite**, as a lightweight embedded database, primarily focuses on **structured data storage**. It supports standard SQL data types and ACID transactions but lacks native support for complex documents or graph data. SQLite's simplicity is its greatest advantage, but it cannot compete with multi-model databases in terms of data type flexibility.

**TiKV** is a distributed key-value storage engine with a relatively simple data model, mainly storing **raw key-value pairs**. As the underlying storage for TiDB, it focuses more on distributed features and consistency guarantees rather than data type diversity. TiKV stores data through RocksDB, suitable for structured but uncomplicated data scenarios.

*Table: Data Type Support Comparison Across Databases*

| **Database** | **Structured Data** | **Document Data** | **Graph Data**   | **Vector Data** | **Extensibility**   |
| ------------ | ------------------- | ----------------- | ---------------- | --------------- | ------------------- |
| PostgreSQL   | Excellent           | Excellent (JSONB) | Via extensions   | Via pgvector    | Very strong (400+ extensions) |
| SurrealDB    | Excellent           | Excellent (JSON)  | Excellent (SQL syntax) | Limited    | Moderate           |
| MongoDB      | Moderate            | Excellent (BSON)  | Limited          | Limited         | Moderate           |
| Redis        | Basic types         | Via modules       | None             | None            | Via modules        |
| SQLite       | Excellent           | Limited           | None             | None            | Limited            |
| TiKV         | Key-value pairs     | None              | None             | None            | Limited            |

## Scalability Comparison

**TiKV** stands out in scalability, employing a **Multi-Raft distributed architecture** that divides data into Regions (default 256MB) by key range. Each Region has multiple replicas (typically 3), with consistency ensured through the Raft protocol. This design allows TiKV to **scale linearly** in both storage and computing capacity. The PD (Placement Driver) component handles automatic Region balancing and scheduling, ensuring efficient cluster resource utilization. TiKV also supports **automatic shard splitting and merging** - Regions automatically split when their size exceeds 384MiB and may merge with adjacent Regions when smaller than 54MiB.

**MongoDB** offers a mature **sharded cluster** solution for horizontal scaling. MongoDB 8.0 further optimizes reshard performance, making shard adjustments more efficient. Its sharding strategies include range-based, hash-based, and zone-based approaches, suitable for different access patterns. Alibaba Cloud MongoDB also supports synchronizing node configurations during bulk configuration changes, simplifying large-scale cluster management. MongoDB's scalability capabilities have been proven in many large-scale internet applications.

**PostgreSQL** delivers strong single-machine performance but has limited native distributed support. However, through the **Citus extension**, it can transform into a distributed HTAP system supporting multi-tenancy and sharding. Recently, cloud-native storage engines like OrioleDB have emerged, claiming to achieve 4x throughput improvements. PostgreSQL's logical and physical replication mechanisms can also meet certain scale requirements, though they are not as elastic as specialized distributed databases.

**SurrealDB** is designed with distributed scenarios in mind, adopting a **multi-tenant architecture** that can distribute data and workload across multiple nodes. Though relatively young, its distributed architecture design principles are modern, with promising long-term scalability potential. SurrealDB's distributed support is still evolving and may not be as mature as TiKV or MongoDB yet.

**Redis** can implement distributed deployments through **Redis Cluster**, automatically sharding data across multiple nodes. Redis supports master-slave replication, allowing data to synchronize from master servers to any number of slave servers. However, Redis's distributed capabilities primarily target high availability and read-write separation rather than unlimited horizontal scaling. Large cluster management complexity is high, and cross-shard transactions are not supported.

**SQLite**, as an **embedded database**, inherently lacks distributed capabilities. While it can implement streaming backups through Litestream or provide distributed access using LiteFS, these solutions are more complementary for specific scenarios rather than enabling true elastic scaling. SQLite is suitable for scenarios with limited data volume or single-machine applications.

*Table: Database Scalability Comparison*

| **Database** | **Sharding Capability** | **Data Distribution** | **Auto Balancing** | **Multi-tenancy** | **Scalability Maturity** |
| ------------ | ----------------------- | --------------------- | ------------------ | ----------------- | ------------------------ |
| TiKV         | Auto Region sharding    | Multi-Raft            | PD scheduling      | Supported         | Production-ready         |
| MongoDB      | Manual/automatic sharding | Configuration-based | Balancer           | Supported         | Very mature              |
| PostgreSQL   | Via Citus extension     | Extension-dependent   | Limited            | Via extensions    | Moderate                 |
| SurrealDB    | Designed to support     | Multi-tenant architecture | Developing      | Native support    | Early stage              |
| Redis        | Redis Cluster           | Hash slots            | Manual reshard     | Limited           | Mature but limited       |
| SQLite       | Not supported           | Single-machine        | None               | None              | Not applicable           |

## Resource Usage and Efficiency Comparison

Resource utilization directly impacts deployment cost and operational complexity, especially important in resource-constrained environments or large-scale deployments.

**SQLite** is undoubtedly the **most lightweight** choice in terms of resource usage, requiring only a few hundred KB of memory, with the entire database stored in a single disk file. Its streamlined architecture makes it excel in embedded devices and mobile applications, with processing speeds sometimes even faster than some larger databases. SQLite's zero-configuration feature further reduces operational overhead, making it a model of resource efficiency.

**Redis**, as an **in-memory database**, keeps all data resident in memory, providing extremely high read-write performance. Memory usage is proportional to data volume and may become a cost-limiting factor. Redis periodically persists data to disk, but its primary design goal remains memory efficiency. In pure memory scenarios, Redis has extremely high resource utilization, especially considering its amazing throughput capacity.

**TiKV** uses RocksDB as its storage engine, with all Region data from the same node stored in one RocksDB instance, optimizing I/O efficiency. TiKV's design emphasizes **balancing performance and resource usage**, ensuring reasonable resource allocation through Region size control (default 256MB). As a distributed system, TiKV requires additional resources for Raft replication and PD scheduling, with overall resource overhead greater than single-machine databases but less than some similar distributed systems.

**PostgreSQL**'s resource usage is **highly configurable**, allowing parameters like shared buffers and work memory to be adjusted according to available resources. PG is not the lightest database, but its resource usage is proportional to its rich functionality. With proper configuration, PostgreSQL can perform well under limited resources, but it typically requires more memory and CPU resources to fully utilize all features.

**MongoDB** uses a **dynamic allocation** strategy for memory, actively utilizing available memory to cache hot data. MongoDB 8.0 introduces an upgraded TCMalloc, optimizing memory management. On SSDs, MongoDB has good storage efficiency, but compared to relational databases, its document storage approach may produce some redundancy. The WiredTiger storage engine provides compression options to help reduce disk usage.

**SurrealDB**, built on Rust, theoretically should have good **memory safety and efficiency**, but as a newer system, actual resource usage data is limited. Its multi-model features may bring certain overhead, but Rust's performance advantages might offset these costs. SurrealDB's distributed design also introduces additional coordination overhead, with specific resource requirements depending on deployment scale.

*Table: Database Resource Usage Comparison*

| **Database** | **Memory Usage**        | **Disk Usage**      | **CPU Efficiency** | **Suitable Scale** | **Tuning Space** |
| ------------ | ----------------------- | ------------------- | ------------------ | ------------------ | ---------------- |
| SQLite       | Extremely low           | Extremely low (single file) | Extremely high | Small datasets    | Limited         |
| Redis        | High (all in-memory)    | Low (for persistence) | Extremely high  | Small to medium datasets | Moderate   |
| TiKV         | Moderate                | Moderate (compressed) | High             | Very large scale   | Large           |
| PostgreSQL   | Medium to high          | Moderate            | High               | Small-medium to large | Very large    |
| MongoDB      | Medium to high          | Medium to high      | High               | Small-medium to large | Large         |
| SurrealDB    | Unknown (expected medium) | Expected moderate | Expected high     | Small-medium to large | Unknown        |

## Concurrency Performance Comparison

Concurrency performance determines a database's responsiveness under high load and is a critical indicator for supporting key business applications.

**Redis** **stands out most prominently** in concurrency performance, mainly benefiting from its **in-memory storage** design and single-threaded lockless architecture. Redis can handle extremely high throughput, with official benchmarks showing a single instance capable of 100,000+ QPS. Redis 6.0's introduction of multi-threaded I/O further enhances concurrency capabilities. When used as a cache, Redis response times typically remain at sub-millisecond levels, making it an ideal choice for low-latency applications.

**TiKV**'s concurrency performance stems from its **distributed architecture** and **Raft optimizations**. Write requests are processed on the Leader and require successful writes to a majority of replicas (at least 2 out of 3 by default) before returning. This design ensures strong consistency while achieving high throughput through parallel processing of requests across different Regions. TiKV's Coprocessor functionality can push computation down to the storage layer, reducing network overhead. For large-scale distributed scenarios, TiKV's concurrency capabilities exceed most single-machine databases.

**PostgreSQL**'s concurrency performance has improved significantly in recent years, with the latest PostgreSQL 17 showing 30%-70% improvement in write throughput compared to PG 10 from six years ago. In Mark Callaghan's sysbench tests, PostgreSQL 16 outperformed MySQL 8.0.34 by 200%-500% in certain write scenarios. PG's MVCC implementation and multi-version concurrency control make it perform exceptionally well under high-concurrency mixed read-write workloads.

**MongoDB**'s concurrency capabilities rank at the top among document databases, with version 8.0 showing 20-36% improvement in read performance and 35-58% in write performance compared to version 7.0. MongoDB's **lock granularity has been refined from collection-level to document-level**, greatly enhancing concurrent write capabilities. Sharded clusters further distribute the load, allowing MongoDB to handle extremely high throughput. The WiredTiger storage engine's compression and cache optimizations also contribute to performance improvements.

**SurrealDB** claims to have **high-performance** features, but as an emerging database, it lacks extensive third-party benchmarks. Its Rust implementation and real-time query engine design should theoretically provide good concurrent processing capabilities. SurrealDB's change stream functionality is suitable for real-time application scenarios, but specific performance limits still need verification.

**SQLite** performs well in **lightweight concurrency** scenarios, but its global write lock design limits high-concurrency write capabilities. SQLite is suitable for read-heavy, write-light, medium-to-low concurrency scenarios, performing excellently in mobile applications and small websites. For high-concurrency write requirements, SQLite may quickly become a bottleneck.

*Table: Database Concurrency Performance Comparison*

| **Database** | **Read Throughput**     | **Write Throughput**  | **Response Time** | **Lock Mechanism** | **Best Concurrency Scenario** |
| ------------ | ----------------------- | --------------------- | ----------------- | ------------------ | ----------------------------- |
| Redis        | Very high (100,000+ QPS) | High                  | Sub-millisecond   | Single-thread lockless | Cache/Sessions            |
| TiKV         | High                    | High (distributed)    | Millisecond       | Region-level       | Large-scale distributed      |
| PostgreSQL   | High                    | High (significant improvement) | Millisecond | Row-level MVCC     | Complex OLTP                 |
| MongoDB      | High (20-36% improvement) | High (35-58% improvement) | Millisecond  | Document-level     | Document-intensive           |
| SurrealDB    | Claims high (to be verified) | Claims high (to be verified) | Expected millisecond | Unknown | Real-time applications       |
| SQLite       | Moderate                | Low (global lock)     | Microsecond to millisecond | Database-level | Low-concurrency local applications |

## Transaction and Consistency Support Comparison

Transaction support is a key feature for ensuring data integrity, with different databases providing different levels of transaction guarantees and consistency models.

**TiKV** provides **strong consistency** **distributed transactions** based on two-phase commit for cross-Region ACID transactions. Its transaction model derives from Google Spanner, using the Raft protocol to ensure multi-replica data consistency, with any write request requiring success on a majority of replicas before returning. TiKV also supports an optimistic transaction model, suitable for scenarios with few conflicts. This strong consistency guarantee makes TiKV suitable for financial-grade applications.

**PostgreSQL** is a benchmark for transaction support among relational databases, providing complete **ACID guarantees** and multi-level isolation (including serializability). Compared to MySQL, PostgreSQL's transaction correctness is widely recognized, with JEPSEN tests confirming that its isolation level behaviors match documentation descriptions. PostgreSQL's MVCC implementation avoids lock contention while maintaining strong consistency, suitable for complex transaction scenarios.

**MongoDB** lacked multi-document transaction support in early versions, but since **version 4.0** has introduced **cross-document ACID transactions**. MongoDB 8.0 further optimizes transaction performance, making it more suitable for critical business scenarios. However, MongoDB's transaction overhead remains higher than relational databases, so use with caution is advised. Its default consistency model is adjustable, allowing trade-offs between consistency and latency.

**SurrealDB** claims to support **ACID transactions**, but as an emerging database, its implementation details and maturity await verification. The multi-model design may introduce complexity in transaction coordination, especially for cross-model operations. SurrealDB's distributed transaction capabilities particularly need evaluation, as this is typically challenging for distributed systems.

**Redis** ensures command atomicity through a **single-threaded execution model** but lacks traditional multi-operation transactions. Redis provides the MULTI/EXEC command group for simple transactions but doesn't support rollbacks. Redis modules can extend transaction capabilities, but overall transaction support is limited, suitable for non-critical data or compensation transaction scenarios.

**SQLite**, as an embedded database, surprisingly provides **complete ACID support**, maintaining data integrity even after system crashes. SQLite's locking mechanism is relatively simple, with global write locks limiting concurrent transaction throughput. For single-machine applications, SQLite's transaction guarantees are sufficiently strong but do not address distributed scenarios.

*Table: Database Transaction Support Comparison*

| **Database** | **ACID Support** | **Isolation Levels**    | **Distributed Transactions** | **Conflict Resolution** | **Suitable Scenarios** |
| ------------ | ---------------- | ----------------------- | ---------------------------- | ----------------------- | ---------------------- |
| TiKV         | Complete         | Serializable            | Supported (2PC)             | Optimistic locking      | Financial/Distributed  |
| PostgreSQL   | Complete         | Read committed to serializable | Single-machine       | MVCC                    | Enterprise OLTP        |
| MongoDB      | Multi-document ACID | Snapshot             | Limited support             | Document-level locks    | Document transactions  |
| SurrealDB    | Claims support   | Unknown                 | In design                   | Unknown                 | Multi-model applications |
| Redis        | Limited (single command) | No traditional isolation | Not supported      | None                    | Non-critical data      |
| SQLite       | Complete         | Serializable            | Not supported               | Global lock             | Single-machine applications |

## Query Capability Comparison

Query capabilities determine the flexibility and efficiency of extracting and analyzing data from a database, representing a core functionality of database systems.

**PostgreSQL** possesses the **most powerful query engine**, supporting all standard SQL functions plus numerous extensions. PG's query optimizer continuously improves, with significant performance enhancements for complex queries. Through extensions, PostgreSQL supports full-text search, geospatial queries, JSON path queries, and vector search (pgvector). Notably, pgvector has achieved a 150-fold performance leap in one year with AWS support, nearly replacing specialized vector databases. PostgreSQL also supports CTEs, window functions, and other advanced features, making it strong in analytical queries.

**SurrealDB**'s unique query capability lies in **processing graph data with SQL syntax**, greatly simplifying relationship queries. For example, querying all posts by a user only requires: `SELECT *, ->authored->post.* AS posts FROM user;`. This syntax combines SQL familiarity with graph query expressiveness. SurrealDB also includes built-in real-time queries and change streams, suitable for applications requiring immediate feedback. However, its analytical query capabilities may not be as comprehensive as PostgreSQL.

**MongoDB**'s query capabilities focus on **document operations** and **aggregation pipelines**, supporting rich query operators and index types. MongoDB's query language is document-oriented, suitable for nested data structures, but complex relationship queries (like multi-table JOINs) are less intuitive than SQL. MongoDB supports full-text search (via text indexes) and geospatial queries, but vector search capabilities are limited, typically requiring external tools (like Elasticsearch).

**Redis**'s query capabilities are relatively limited, primarily centered around **key-value operations** and **data structure commands** (like LPUSH, ZRANGE, etc.). Through the RedisSearch module, Redis can support full-text search and simple aggregation queries but is not suitable for complex analytical queries. The RedisJSON module extends JSON document query capabilities but remains less flexible than specialized document databases.

**SQLite** supports standard SQL queries, including JOINs, subqueries, and window functions, but lacks **advanced analytical features** (like full-text search, vector search). SQLite's query optimizer is highly optimized for small datasets but may degrade in performance with large data volumes.

**TiKV**, as a distributed key-value store, focuses its query capabilities around **key-value scans** and **range queries**, supporting pushing down some computation logic via coprocessors. TiKV itself doesn't provide an SQL layer and needs to be used with TiDB to support complex SQL queries.

*Table: Database Query Capability Comparison*

| **Database** | **SQL Support**        | **Full-text Search** | **Vector Search** | **Nested Queries**   | **Best Query Scenario** |
| ------------ | ---------------------- | -------------------- | ----------------- | ------------------- | ----------------------- |
| PostgreSQL   | Complete SQL           | Via extensions       | Via pgvector      | Excellent           | Complex analytical queries |
| SurrealDB    | SurrealQL (SQL variant) | Built-in            | Built-in          | Excellent (graph queries) | Mixed multi-model queries |
| MongoDB      | Limited (aggregation pipeline) | Built-in     | Limited           | Excellent (document nesting) | Document-oriented queries |
| Redis        | None                   | Via modules          | None              | Limited             | Key-value/simple aggregation |
| SQLite       | Standard SQL           | Limited              | None              | Moderate            | Small OLTP queries     |
| TiKV         | None (requires TiDB)   | None                 | None              | None                | Key-value/range queries |

---

## Ecosystem Compatibility and Integration Friendliness Comparison

**PostgreSQL** has the **most mature ecosystem**, supporting almost all mainstream programming languages (Python, Java, Go, etc.), with rich ORM frameworks (like Django ORM, SQLAlchemy, Hibernate) and complete operational tools (pgAdmin, PostGIS). PostgreSQL's deployment methods are flexible, supporting Docker, Kubernetes, and major cloud platforms, with comprehensive data migration tools (pg_dump, Logical Replication).

**MongoDB**'s ecosystem is equally powerful, with official **multi-language drivers** (MongoDB Driver), mature ORM frameworks (Mongoose, Spring Data MongoDB), and Atlas cloud services simplifying operations. MongoDB Compass provides graphical management, and data migration can be implemented through mongodump/mongorestore or Atlas Live Migration.

**Redis**'s ecosystem primarily consists of **client libraries** and **caching tools**, supporting Python (redis-py), Java (Jedis), Node.js (ioredis), and other languages. RedisInsight provides a management interface, but Redis lacks native ORM support, typically requiring manual encapsulation of the data access layer.

**SQLite**, due to its embedded nature, **requires no separate service**, making integration simple but lacking distributed support. Most languages (Python, C/C++, Java) provide SQLite bindings, with good ORM framework support (like SQLAlchemy, Room), but fewer operational tools.

**TiKV**'s ecosystem revolves around the **TiDB ecosystem** (such as TiUP, PD Control), with client libraries primarily supporting Go and Java. TiKV itself is relatively low-level and needs to be used with TiDB to obtain complete SQL capabilities, suitable for teams with existing TiDB experience.

**SurrealDB**, as an emerging database, still has a developing ecosystem but already provides **official SDKs** (JavaScript, Python, Go, Rust). Its HTTP/WebSocket API simplifies integration, but ORM support is limited (e.g., Prisma adaptation is still experimental). SurrealDB's cloud service (Surreal Cloud) reduces deployment difficulty, making it suitable for rapid prototype development.

*Table: Database Ecosystem and Integration Friendliness Comparison*

| **Database** | **Client Support**      | **ORM Support**        | **Operation Tools**  | **Deployment Complexity** | **Best Use Case** |
| ------------ | ----------------------- | ---------------------- | -------------------- | ------------------------- | ----------------- |
| PostgreSQL   | Extremely rich          | Rich (SQLAlchemy, etc.) | Complete (pgAdmin)  | Moderate                  | Enterprise applications |
| MongoDB      | Rich                    | Good (Mongoose)        | Complete (Compass)   | Low (Atlas)               | Document-oriented applications |
| Redis        | Rich                    | Limited                | RedisInsight         | Low                       | Cache/session storage |
| SQLite       | Widespread              | Good (Room, etc.)      | Limited              | Extremely low             | Embedded applications |
| TiKV         | Limited (Go/Java)       | None                   | TiUP/PD Control      | High                      | TiDB ecosystem users |
| SurrealDB    | Developing (JS/Rust, etc.) | Limited             | Cloud management console | Low (cloud service)    | Real-time/multi-model applications |

---

## Deployment 


### **1. Installing SurrealDB**
   ```bash
   curl -sSf https://install.surrealdb.com | sh
   ```
   Add to `.bashrc`:
   ```
   export PATH=/home/shinshi/.surrealdb:$PATH
   ```

   Testing:
   ```
   surreal start --log trace --user root --pass password
   curl http://127.0.0.1:8000/health
   ```
---

### **2. Installing PostgreSQL**

   ```bash
   sudo apt update
   sudo apt install -y postgresql
   ```

   Testing:
   ```bash
   sudo -i -u postgres
   psql
   CREATE DATABASE testdb;
   \q
   psql -d testdb
   ```

### **3. Installing Redis**

   ```bash
   sudo apt update
   sudo apt install -y redis-server
   ```

   Testing:
   ```
   redis-cli ping
   ```

### **4. Installing MongoDB**

   **Import MongoDB's official GPG key and source (Ubuntu 24.04):**
   ```bash
   sudo apt-get install gnupg curl
   curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
   echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
   ```

   **Install MongoDB:**
   ```bash
   sudo apt update
   sudo apt install -y mongodb-org
   sudo systemctl start mongod
   sudo systemctl enable mongod
   ```

   Testing:
   ```
   mongosh
   ```

### **5. Installing SQLite**
   ```bash
   sudo apt update
   sudo apt install -y sqlite3
   ```

   Testing:
   ```
   sqlite3
   ```

---

### **6. Installing TiKV**
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
   ```

   Testing:
   ```
   tiup playground
   ```

---

## License Type Comparison

- **SurrealDB**: Core code uses **Apache 2.0**, commercial hosting services require payment (e.g., Surreal Cloud's Start/Scale plans).
- **PostgreSQL**: **PostgreSQL License** (similar to BSD/MIT), no commercial restrictions.
- **MongoDB**: Community Edition uses **SSPL** (Server Side Public License), commercial version requires subscription.
- **Redis**: Core code uses **BSD 3-Clause**, some Redis Modules features require commercial licensing.
- **SQLite**: **Public Domain**, no usage restrictions.
- **TiKV**: **Apache 2.0**, commercial support provided by PingCAP.

---

## Practice

The testing environment is Ubuntu 24.04. All deployment methods are relatively simple.

Target data form: Each folder corresponds to a research paper, containing a PDF of the original paper and a set of JSON files extracting relevant information from the article.

### Target Data Compatibility Analysis

- SurrealDB: Supports JSON and structured data, suitable for this dataset.
- PostgreSQL: Supports JSON and binary data, suitable for this dataset.
- Redis: Primarily key-value storage, not suitable for deeply nested JSON or graph-like relationships.
- MongoDB: Natively supports JSON and binary data, highly suitable for this dataset.
- SQLite: Can store JSON and binary data but lacks advanced query capabilities for nested structures.
- TiKV: Key-value storage, not suitable for JSON or complex relationships.

Further comparison of the suitable databases: SurrealDB, PostgreSQL, and MongoDB:

- SurrealDB leans towards using standard web protocols (HTTP and WebSocket), making it more suitable for real-time applications and direct communication between frontend and backend. MongoDB and PostgreSQL support the same local communication methods, but MongoDB defaults to TCP/IP communication.
- MongoDB requires licensing for commercial use, whereas PostgreSQL has no commercial restrictions.
- In terms of functionality, both can meet the requirements.

### Performance Evaluation:

The databases that actually participated in testing were SurrealDB, PostgreSQL, and MongoDB.

<!-- Total write time for SurrealDB: 0.9940774440765381 seconds
Total read time for SurrealDB: 0.013937950134277344 seconds

Total write time for MongoDB: 1.087291955947876 seconds
Total read time for MongoDB: 0.004241466522216797 seconds

Total write time for PostgreSQL: 0.09826374053955078 seconds
Total read time for PostgreSQL: 0.005629062652587891 seconds -->

| Database       | Write Time (seconds) | Read Time (seconds) |
|----------------|-----------------------|----------------------|
| SurrealDB      | 0.9940774440765381    | 0.013937950134277344 |
| MongoDB        | 1.087291955947876     | 0.004241466522216797 |
| PostgreSQL     | 0.09826374053955078   | 0.005629062652587891 |


*Database schema obtained:*

 | Schema | Name         | Type  | Owner    |
 | ------ | ------------ | ----- | -------- |
 | public | _edges       | table | postgres |
 | public | background   | table | postgres |
 | public | challenge    | table | postgres |
 | public | contribution | table | postgres |
 | public | experiment   | table | postgres |
 | public | paper        | table | postgres |
 | public | solution     | table | postgres |
