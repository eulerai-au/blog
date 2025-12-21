# AI Agents' "Passport" and "Highway": How ANP Reshapes the Internet

When you open your phone to book a flight, reserve a restaurant, check the weather, and arrange a ride—how many apps do you switch between? Now imagine if an AI assistant could handle all of this. How many services would it need to call? And how should these services collaborate seamlessly?

This is the core challenge of the AI agent era: **on an internet designed for humans, agents struggle to "communicate" freely**.

![alt text](images/Figure1-The%20Architecture%20of%20the%20ANP%20protocol.png)
*Image source: Agent Network Protocol Technical White Paper, Figure 1*

## When Internet Meets AI: Four Trends Reshaping the Web

With rapid development of large language models, AI agents are becoming the internet's new protagonists. Research shows four fundamental transformations:

**Agents will completely replace traditional software**. Personal AI assistants will become users' primary gateway to the internet, while enterprises will deploy agents to interact directly with users.

**Universal interconnection between agents** will break down data silos, allowing AI to access complete cross-platform contextual information for more precise decision-making.

**Protocol-based native connections become mainstream**. AI is inherently better at processing structured data directly rather than simulating human operations. Future agents will connect through specially designed communication protocols, like HTTP for the human internet.

**Agents possess self-organizing collaborative capabilities**. Through standard protocols, agents can use natural language for flexible negotiation, dynamically forming collaborative relationships to complete complex tasks.

However, reality is harsh. Existing internet infrastructure presents three core problems: **data silos** limit information access; **unfriendly interfaces** force agents to simulate human operations; **high collaboration costs** as different agents lack direct communication mechanisms.

Against this backdrop, the Agent Network Protocol (ANP) was born.

## ANP: Communication Standard for the AI Era

If HTTP defines how humans exchange information online, ANP defines how agents connect, communicate, and collaborate. This is an open-source communication protocol designed natively for AI.

The agent communication landscape is rapidly evolving. Anthropic's MCP focuses on connecting models with tools, Google's A2A addresses cross-platform agent interoperability, while ANP aims to build a decentralized agent collaboration network. **If MCP is the "USB" connecting models to tools, ANP's vision is to become the "HTTP" enabling agents to freely connect with each other**. The core difference lies in worldview: MCP is model-centric, treating the internet as its context; ANP is agent-centric, where every agent has equal standing, forming a decentralized network.

ANP follows six core principles: **AI-native design** (emphasizing structured data and semantic expression), **compatibility and reuse** (compatible with OpenAPI, JSON-RPC, etc.), **composability** (modular design for flexible combination), **simplicity and extensibility** (keeping core simple while reserving extension space), **pragmatic deployability** (based on existing internet infrastructure), and **principle of least trust** (all interactions require authentication and authorization).

![alt text](images/Figure3Agent%20authentication%20and%20token%20exchange%20sequence.png)
*Image source: Agent Network Protocol Technical White Paper, Figure 3*

## Three-Layer Architecture: Technical Foundation for Agent Internet

ANP employs a carefully designed three-layer architecture, each addressing specific core problems.

### Identity and Secure Communication Layer

The foundation layer, based on W3C's Decentralized Identifier (DID) standard, designs a lightweight decentralized identity authentication mechanism. Through the did:wba method, any two agents can securely verify each other's identities and establish encrypted communication channels without central authorities.

This is like issuing each agent a "digital passport" that doesn't require central authority issuance yet is globally recognized. More importantly, the end-to-end encryption scheme based on DID key pairs ensures that even if communication passes through third-party platforms, intermediate nodes cannot decrypt content.

### Meta-Protocol Layer

This is ANP's most innovative design. Agent A sends a meta-protocol request to Agent B, describing needs, inputs, expected outputs, and proposed candidate communication protocols in natural language. B uses AI to process the description and, combined with its capabilities, decides whether to accept. After both parties reach agreement, they generate and deploy protocol processing code, conduct joint testing, then begin formal communication.

![alt text](images/Figure4-Illustration%20of%20Meta%20Protocol%20Communication.png)
*Image source: Agent Network Protocol Technical White Paper, Figure 4*

Even smarter, agents can save negotiation results. When encountering similar needs later, they can directly use previous results or even share them with other agents, forming an accumulating "protocol knowledge base."

### Application Protocol Layer

Contains two core modules: **agent description** and **agent discovery**.

The Agent Description Protocol (ADP) uses JSON-LD format, like an agent's "business card," containing basic information, capability descriptions, interface protocols, and security authorization. Other agents can understand how to interact by reading this document.

The agent discovery protocol provides two complementary methods: **active discovery** based on Web's well-known path allows accessing a unified directory under a domain to obtain all agent descriptions; **passive discovery** is like search engines, where agents proactively register information with search services.

## AI-Native Data Network: A New Network Designed for AI

The existing internet is designed for humans, with web pages connected through hyperlinks and information presented in visual interfaces. This mode isn't suitable for efficient AI access.

ANP proposes an AI-native data network structure. Through ADP and discovery protocols, each agent publicizes service interfaces and capability information in a structured manner, automatically exposing itself to the entire network. Within this framework, all agents and their data resources form a machine-friendly open network: each node is describable, discoverable, and callable; each connection is semantically clear and structurally unified; agents can quickly retrieve and call resources based on unified standards.

![alt text](images/Figure5-Illustration%20of%20the%20structure%20of%20AI-native%20data%20network.png)
*Image source: Agent Network Protocol Technical White Paper, Figure 5*

This enables agents to directly and efficiently access widely distributed capabilities and knowledge on the internet without relying on web crawling or interface simulation, greatly liberating AI's potential.

## Security and Privacy: Maintaining Control in Openness

ANP has incorporated security mechanisms as core components from initial design.

**Distinction between human and agent authorization** is a key innovation. Low-risk operations (like querying public information) allow agent automatic authorization; high-risk operations (like fund transfers) require explicit human user authorization, ensuring important decisions are driven by human will.

**Multi-DID strategy** achieves fine-grained privacy protection. Primary DID maintains long-term relationships, while independent sub-DIDs are generated for different scenarios, achieving identity isolation and preventing behavioral correlation analysis.

**Minimal information disclosure** requires agents to transmit only necessary information, with sensitive fields using end-to-end encryption and all communication sessions bound to identity verification information to prevent man-in-the-middle attacks.

## Connection is Power: Reshaping the Open Network

Internet evolution validates the concept of "Connection is Power." However, today's internet ecosystem is dominated by a few platforms, with data and services confined within "digital silos."

ANP's goal is to drive the internet from its closed state back to its open origins. In the future agent network, every agent simultaneously plays roles as information consumer and service provider, with each node able to discover and connect with any other node without barriers.

This marks an important shift: from **platform-centered closed ecosystems** to **protocol-centered open ecosystems**. Value acquisition depends on unique capabilities and contributions brought by following open protocols, not controlling closed platforms. This will stimulate more intense application-layer innovation, as success is no longer about "locking in" users but providing superior agent services.

In the evolution of agent communication protocols, various protocols are forming a complementary landscape: **MCP connects AI with tools, A2A connects AIs across platforms, ACP focuses on local edge agent coordination, while ANP is dedicated to building an agent network on the open internet**. Ideally, these protocols will converge and complement each other, jointly building a unified agent communication ecosystem; open-source tools and middleware will play key roles in abstracting protocol differences and providing unified APIs for developers.

[**Image 5**: ANP ecosystem position diagram - relationship with MCP, A2A and other protocols]

Currently, ANP has been presented at the W3C WebAgents community, its technical white paper published on arXiv, and the GitHub open-source community continues to develop. As one of the world's earliest open-source communication protocols designed for agents, ANP works alongside other protocols to advance the agent interoperability ecosystem.

## Are You Ready for the Agent Internet?

Imagine when your personal AI assistant can seamlessly collaborate with banking, medical, travel, and education agents; when enterprise customer service agents can directly interface with supply chain and logistics agents; when research agents can freely collaborate across institutions and borders—this isn't science fiction, but the future ANP is building.

Realizing this future requires extensive collaboration. Whether you're a researcher, developer, enterprise, or individual interested in agent technology, you can participate in ANP's development, testing, and promotion.

Because in this coming age of agents, **the power of connection will return to every user and every agent**.

---

**What's your view on the future of the agent internet? How do you expect AI assistants to collaborate? Share your thoughts in the comments.**

---

**References:**
- Agent Network Protocol Technical White Paper (arXiv:2508.00007)
- Agent Network Protocol GitHub Repository
- W3C WebAgents Community Group