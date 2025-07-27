# Kafka 入门与集群实战：从零到企业级应用

## 技能掌握目标
通过本教案的学习，学员将掌握以下技能：
1. **Kafka 基础理论**：理解 Kafka 的核心概念和集群架构，掌握其解决的高并发消息流和系统解耦问题。
2. **架构认知**：熟悉 Kafka 集群的组成（如 Topic、Partition、Broker 等），以及新版本 KRaft 模式与传统 ZooKeeper 模式的区别。
3. **对比理解**：通过与 MySQL 和 Redis 的对比，明确 Kafka 的独特价值和使用场景。
4. **流量冲击应对**：理解 Kafka 如何作为消息中转站，缓解企业服务在流量高峰期的压力，避免服务崩溃。
5. **系统搭配**：了解 Kafka 与 MySQL、Redis 等工具如何在实际业务中协作，构建高效系统。
6. **分布式特性**：理解 Kafka 的分布式设计理念，为后续学习部署和运维打下理论基础。
7. **实践准备**：通过通俗讲解和图示，激发学习兴趣，为后续基于 Docker 的集群部署和企业级问题解决做好准备。


## 第一部分：Kafka 基础与集群架构

### 1.1 Kafka 简介
- **什么是 Kafka？**
  Kafka 是一种分布式流处理平台，简单来说，它就像一个“超级快递中心”，专门处理大量数据的接收、存储和分发。想象一下，每天有成千上万的包裹（数据）从不同地方寄来，Kafka 负责把这些包裹快速分类、存储，然后按需送到不同的收件人手中。
- **Kafka 解决的核心问题**：
  - **高并发消息流**：在互联网时代，数据量巨大且实时产生（如用户点击、订单信息、日志数据），Kafka 能高效处理每秒百万级别的消息，确保数据不丢失、不堵塞。
  - **异步解耦**：在复杂的系统中，不同模块（如订单系统和库存系统）需要交换数据，但它们不一定能同时在线。Kafka 就像一个“中间人”，让生产数据的系统（生产者）和消费数据的系统（消费者）不需要直接沟通，降低了耦合性。
  - **流量冲击防护**：在企业活动中（如电商大促、秒杀活动），流量会突然暴增，导致服务压力过大甚至崩溃。Kafka 作为“消息中转站”，可以先接收所有请求并存储起来，让后端服务按照自己的处理能力逐步消化这些请求，避免被流量直接冲垮。
- **生活化类比**：
  想象 Kafka 是一个巨大的“物流中转站”：
  - 生产者是“寄件人”，不断把包裹（消息）送到中转站。
  - 消费者是“收件人”，根据需求从中转站取走包裹。
  - 中转站（Kafka）负责存储和分发，确保包裹不会丢失，还能按顺序送到正确的人手中。特别是在“双11”这种高峰期，中转站可以先把所有包裹堆积起来，慢慢分拣，避免快递员直接被压垮。
- **目标**：让学员明白 Kafka 是一个处理大数据流的工具，核心作用是高效传递和存储消息，尤其在流量冲击时保护系统稳定。

### 1.2 为什么一定要学 Kafka？与 MySQL 和 Redis 的对比
- **MySQL、Redis 和 Kafka 的定位不同**：
  为了理解为什么需要 Kafka，我们先来看看大家可能更熟悉的两种工具：MySQL 和 Redis，然后对比它们的用途和局限性。
  - **MySQL（关系型数据库）**：
    - **作用**：MySQL 就像一个“档案室”，用来存储结构化数据（如用户信息、订单记录），支持复杂的查询和事务处理。
    - **局限性**：MySQL 不擅长处理高并发、实时的消息流。如果每秒有几十万条数据（如用户点击日志）需要写入，MySQL 会因为频繁的磁盘操作而变得很慢，甚至崩溃。特别是在企业活动流量暴增时，MySQL 无法承受突如其来的请求压力。
    - **适用场景**：存储需要长期保存和查询的数据，比如用户的账户余额。
  - **Redis（内存数据库）**：
    - **作用**：Redis 就像一个“快速便签本”，数据存储在内存中，读写速度极快，常用于缓存、计数器或简单的消息队列。
    - **局限性**：Redis 虽然快，但它更适合小规模、高速读写的场景。如果数据量巨大（如活动期间的订单流），内存成本会很高；而且 Redis 的持久化能力有限，数据容易丢失，难以应对大规模流量冲击。
    - **适用场景**：缓存热门数据、处理简单的实时任务，比如记录网站的访问量。
  - **Kafka（分布式消息系统）**：
    - **作用**：Kafka 就像一个“物流中转站”，专门处理大规模、实时的消息流。它能接收、存储和分发每秒百万级别的消息，同时保证数据不丢失。
    - **优势**：Kafka 既不像 MySQL 那样受限于磁盘性能，也不像 Redis 那样受限于内存成本。它通过分布式架构和磁盘顺序写入，实现了高吞吐量和可靠性。尤其是在企业活动流量暴增时，Kafka 作为“缓冲区”，可以先存储所有请求，让后端服务按自己的节奏处理，避免系统被直接冲垮。
    - **适用场景**：处理大规模实时数据流，比如收集用户行为日志、传递系统间消息，尤其是在流量高峰期保护系统稳定。
- **为什么一定要学 Kafka？**
  - **解决高并发问题**：在现代互联网应用中，数据量和实时性要求越来越高，MySQL 和 Redis 无法完全满足需求，而 Kafka 专为这种场景设计。
  - **流量冲击防护**：在企业活动中（如电商“双11”、秒杀活动），流量会突然暴增，Kafka 作为消息中转站，可以有效缓冲请求，保护后端服务不被压垮。这是 MySQL 和 Redis 难以实现的。
  - **系统解耦的关键**：Kafka 作为“中间人”，让不同系统（比如订单系统和库存系统）可以异步通信，减少直接依赖，提升系统的灵活性和稳定性。
  - **企业级标配**：几乎所有涉及大数据、实时处理的互联网公司（如电商、社交平台）都在使用 Kafka，学习 Kafka 是进入相关领域的必备技能。
- **生活化类比**：
  - MySQL 是“档案室”，适合存放需要仔细整理和查询的资料，但不适合快速收发大量包裹，尤其是在“双11”这种高峰期，档案室会直接瘫痪。
  - Redis 是“便签本”，适合快速记下小范围的事情，但不适合存储和管理海量包裹，一旦包裹太多，便签本就写不下了。
  - Kafka 是“物流中转站”，专门处理大规模包裹的收发和分发，效率高且可靠，尤其是在高峰期可以先堆积包裹，慢慢分拣，避免快递员被压垮。
- **目标**：通过与 MySQL 和 Redis 的对比，让学员理解 Kafka 的独特价值，明确它在高并发、系统解耦和流量冲击防护中的不可替代性。

### 1.3 Kafka 与 MySQL、Redis 如何搭配？
- **实际业务中的协作**：
  在一个完整的系统中，Kafka、MySQL 和 Redis 往往不是单独使用的，而是各司其职，相互配合。
  - **场景举例：电商平台秒杀活动**：
    1. 活动开始，用户疯狂下单，订单系统产生大量订单数据（生产者）。
    2. 订单数据首先发送到 Kafka，作为消息流存储在某个 Topic 中，缓冲流量冲击，避免直接冲击后端服务。
    3. 库存系统（消费者）从 Kafka 读取订单数据，按照自己的处理能力逐步更新库存，不会被瞬间流量压垮。
    4. 订单数据最终写入 MySQL，长期存储以供查询（如用户查看历史订单）。
    5. 热门商品的库存数据同时更新到 Redis，用于快速展示给其他用户（缓存）。
  - **为什么这样搭配？**
    - Kafka 负责“消息传递和缓冲”，处理高并发订单流，确保订单数据不丢失，并且让订单系统和库存系统异步通信，互不影响，尤其是在流量高峰期保护系统稳定。
    - MySQL 负责“数据存储”，保存订单的最终状态，支持复杂的查询和报表分析。
    - Redis 负责“快速访问”，缓存热门数据，提升用户体验。
- **搭配的优势**：
  - **高性能**：Kafka 处理高并发消息流，减轻 MySQL 的写入压力。
  - **低耦合**：通过 Kafka，订单系统和库存系统不需要直接通信，系统更灵活。
  - **流量防护**：Kafka 作为缓冲区，在活动高峰期存储大量请求，让后端服务按合理节奏处理，避免崩溃。
  - **用户体验**：Redis 提供快速缓存，页面响应更快。
- **生活化类比**：
  想象一个电商物流体系在“双11”高峰期：
  - Kafka 是“物流中转站”，接收和分发所有订单包裹，处理速度快，先堆积所有包裹，慢慢分拣，避免后端直接崩溃。
  - MySQL 是“档案室”，记录每个订单的最终状态，方便日后查账。
  - Redis 是“公告栏”，展示热门商品的库存，方便快速查看。
  这三者分工明确，共同保证电商平台在流量高峰期也能高效运转。
- **目标**：让学员明白 Kafka 不是孤立工具，它在实际业务中与 MySQL 和 Redis 配合，特别是在流量冲击时构建高效、稳定的系统。

### 1.4 集群架构详解
- **Kafka 的核心概念**：
  为了理解 Kafka 的工作原理，我们需要先认识它的几个“零件”：
  - **Topic（主题）**：消息的分类标签，类似物流中转站的“分类货架”。比如“订单”是一个 Topic，“用户日志”是另一个 Topic，消息会根据类型放到不同的 Topic 上。
  - **Partition（分区）**：一个 Topic 可以分成多个分区，每个分区就像货架上的“格子”，用来存放一部分消息。分区的作用是提高处理速度和存储能力，因为多个格子可以同时处理消息。
  - **Replica（副本）**：每个分区会有多个副本，就像“备份格子”，防止数据丢失。如果一个格子坏了，备份格子可以顶上。
  - **Broker（经纪人/节点）**：Kafka 集群中的一台服务器，负责存储和转发消息。就像物流中转站的一个“分站”，多个 Broker 组成集群，共同分担工作量。
  - **Consumer Group（消费者组）**：一组消费者共同消费某个 Topic 的消息，就像一队快递员一起取包裹，分工协作，确保每个消息只被处理一次。
- **这些概念如何协作？**
  - 生产者把消息发送到某个 Topic，Kafka 会根据规则把消息分配到 Topic 的某个 Partition 上。
  - 每个 Partition 存储在某个 Broker 上，同时有副本存储在其他 Broker 上，确保数据安全。
  - 消费者组订阅 Topic，组内不同消费者分别读取不同 Partition 的消息，实现高效并行处理。
- **生活化类比**：
  想象一个大型物流中心：
  - Topic 是“货架分类”（如“生鲜”“图书”）。
  - Partition 是货架上的“格子”，一个货架有多个格子，方便同时处理更多包裹。
  - Replica 是“备用格子”，防止某个格子坏了导致包裹丢失。
  - Broker 是“分站”，多个分站组成整个物流网络。
  - Consumer Group 是“快递小队”，小队成员分工取不同格子的包裹，确保高效配送。
- **目标**：通过类比和简单描述，让学员快速抓住 Kafka 集群的核心组件和它们之间的关系。

### 1.5 新版本架构变化：KRaft 模式
- **传统模式（ZooKeeper 模式）**：
  在 Kafka 的早期版本中，集群依赖一个叫 ZooKeeper 的工具来管理元数据（比如哪个 Broker 负责哪个 Partition，谁是 Leader）。ZooKeeper 就像一个“总调度员”，记录和管理整个集群的状态。
- **新版本变化（KRaft 模式）**：
  从 Kafka 2.8.0 开始，引入了 KRaft 模式（Kafka Raft Metadata 模式），Kafka 不再依赖 ZooKeeper，而是自己内置了一个元数据管理机制。简单来说，Kafka 集群中的几个 Broker 会选举出一个“Controller（控制器）”，由它来管理元数据和协调集群工作。
- **KRaft 模式的优势**：
  - **简化架构**：不需要额外部署和管理 ZooKeeper，减少了系统复杂度。
  - **性能提升**：元数据管理更高效，集群启动和恢复速度更快。
  - **更适合小型部署**：对于学习者和小型企业，KRaft 模式更容易上手。
- **生活化类比**：
  - ZooKeeper 模式就像物流中心请了一个“外部顾问”来指挥调度，顾问知道所有分站的情况。
  - KRaft 模式则是物流中心自己选一个“内部经理”来管理，不再需要外部顾问，沟通更快，成本更低。
- **目标**：让学员了解 Kafka 的技术演进，明白 KRaft 模式是当前趋势，后续实验将基于此模式。

### 1.6 架构图示
为了更直观地展示 Kafka 集群的结构，我们用 Mermaid 图来表示典型架构，并对比 KRaft 模式和 ZooKeeper 模式的差异。

- **Kafka 集群典型结构图**：
  ```mermaid
  graph TD
      P1[生产者 1] -->|发送消息| T1[Topic 1]
      P2[生产者 2] -->|发送消息| T1
      T1 --> P1_1[Partition 1]
      T1 --> P1_2[Partition 2]
      P1_1 --> B1[Broker 1]
      P1_1 -.->|副本| B2[Broker 2]
      P1_2 --> B2
      P1_2 -.->|副本| B3[Broker 3]
      B1 -->|读取消息| C1[消费者 1]
      B2 -->|读取消息| C2[消费者 2]
      C1 --- CG[消费者组]
      C2 --- CG
  ```
  **解释**：生产者将消息发送到 Topic，Topic 分成多个 Partition 存储在不同 Broker 上，每个 Partition 有副本备份。消费者组内的消费者分别读取不同 Partition 的消息。

- **ZooKeeper 模式 vs KRaft 模式对比图**：
  ```mermaid
  graph TD
      subgraph ZooKeeper 模式
          ZK[ZooKeeper 集群] -->|管理元数据| B1Z[Broker 1]
          ZK --> B2Z[Broker 2]
          ZK --> B3Z[Broker 3]
      end
      subgraph KRaft 模式
          B1K[Broker 1<br>Controller] -->|管理元数据| B2K[Broker 2]
          B1K --> B3K[Broker 3]
      end
  ```
  **解释**：
  - ZooKeeper 模式：ZooKeeper 作为一个独立集群，负责管理 Kafka 集群的元数据和协调工作。
  - KRaft 模式：Kafka 集群内部选举一个 Broker 作为 Controller，直接管理元数据，不需要外部 ZooKeeper。

- **Kafka 与 MySQL、Redis 搭配示意图（流量冲击场景）**：
  ```mermaid
  graph TD
      OS[订单系统<br>生产者<br>秒杀活动] -->|高并发订单消息| K[Kafka<br>Topic: 订单<br>缓冲流量]
      K -->|按节奏读取| IS[库存系统<br>消费者]
      K -->|按节奏读取| MS[MySQL<br>存储订单]
      IS -->|更新库存| R[Redis<br>缓存库存]
      US[用户系统] -->|查询库存| R
  ```
  **解释**：在秒杀活动中，订单系统产生高并发订单消息，Kafka 作为缓冲区存储所有请求，库存系统和 MySQL 按自己的处理能力逐步读取，避免被流量直接冲垮，Redis 缓存热门库存数据供用户快速查询。
  
## 第二部分：Kafka 单机部署（重点：Docker 部署）

### 2.1 单机部署的理论基础
在学习 Kafka 集群之前，我们先从最简单的单机部署开始。单机部署就像“一个人开的小型物流站”，虽然规模小，但包含了 Kafka 的核心功能，让你快速上手，理解基本操作和命令。

- **什么是单机部署？**
  单机部署是指在一台机器上运行一个 Kafka Broker（节点），负责接收、存储和转发消息。没有其他节点参与，也没有副本和分布式特性，适合学习和测试。
- **单机部署的核心作用**：
  - **学习基础命令**：通过单机环境，熟悉 Kafka 的基本操作，如创建 Topic、发送消息、消费消息等。
  - **理解核心概念**：掌握 Topic、Partition、Broker 等概念的实际含义，为后续集群学习打基础。
  - **快速验证**：单机环境简单，启动快，容易排查问题，适合初学者。
- **生活化类比**：
  想象你开了一个小型快递点（单机 Kafka），只有你一个人（一个 Broker），负责接收包裹（消息）、放到货架上（Topic 和 Partition），然后分发给收件人（消费者）。虽然规模小，但你能学会如何管理包裹，为将来开大物流中心（集群）做好准备。
- **目标**：
  让学员理解单机部署的意义，降低学习门槛，为后续集群部署打好理论和实践基础。

### 2.2 环境准备
在开始部署 Kafka 单机之前，我们需要准备好实验环境。步骤很简单，就像准备一次简单的家庭聚会。

- **确保安装 Docker**：
  Docker 是一个“容器工具”，就像一个能快速打包和运行软件的“魔法箱子”，可以让我们在不同电脑上运行相同的 Kafka 环境。
  - 如果你还没安装 Docker，可以参考以下简单步骤：
    1. 访问 Docker 官网（https://www.docker.com/get-started/），下载适合你系统的版本（Windows、Mac 或 Linux）。
    2. 按照提示安装，安装完成后在终端输入 `docker --version`，如果能看到版本号，说明安装成功。
  - 详细安装指南：https://docs.docker.com/get-docker/。
- **硬件要求**：
  单机部署对资源要求较低，建议你的电脑或云服务器至少有：
  - 内存：2GB（就像给 Kafka 提供一个小的“工作空间”）。
  - CPU：1 核（就像给 Kafka 提供一个“工人”来处理任务）。
- **Kafka 版本与镜像**：
  我们将使用指定镜像 `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0`，这是 Bitnami 提供的 Kafka 镜像，版本较新，支持 KRaft 模式（不需要 ZooKeeper）。
- **Kafka UI 镜像**：
  为了方便可视化管理，我们还会部署一个 Web UI 工具，使用镜像 `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0`，这是一个开源的 Kafka 管理界面，类似“物流中心的监控屏幕”，可以直观查看 Topic、消息等信息。
- **目标**：
  确保每位学员都能准备好 Docker 环境和硬件资源，为单机部署做好准备。

### 2.3 Docker 部署 Kafka 单机
现在我们开始用 Docker 部署一个单机的 Kafka Broker。步骤非常简单，就像“搭一个小型积木房子”，我会详细讲解每个命令的含义。

- **步骤 1：拉取 Kafka 镜像**
  镜像就像一个“预装好的软件包”，我们先从指定仓库下载 Kafka 的镜像。
  - 在终端输入以下命令：
    ```bash
    docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
    ```
  - 下载完成后，用 `docker images` 查看是否下载成功。
- **步骤 2：启动 Kafka 单机容器**
  我们将启动一个 Kafka 容器，作为单机 Broker。Bitnami 的镜像默认支持 KRaft 模式（不需要 ZooKeeper），配置非常简单。
  - 输入以下命令启动 Kafka：
    ```bash
    docker run -d \
      --name kafka-single \
      -p 9092:9092 \
      -p 9093:9093 \
      -e KAFKA_CFG_NODE_ID=1 \
      -e KAFKA_CFG_PROCESS_ROLES=broker,controller \
      -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@192.168.110.8:9093 \
      -e KAFKA_CFG_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
      -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://192.168.110.8:9092,CONTROLLER://192.168.110.8:9093 \
      -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
      -e ALLOW_PLAINTEXT_LISTENER=yes \
      -v kafka-data:/bitnami/kafka/data \
      --network bridge \
      swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
    ```
    **解释**：
    - `--name kafka-single`：给容器起个名字，就像给你的小型快递点取名“单机站”，方便后续管理。
    - `-p 9092:9092`：端口映射，让你可以通过本机的 9092 端口访问 Kafka 的 Broker 服务（用于消息收发）。
    - `-p 9093:9093`：端口映射，让你可以通过本机的 9093 端口访问 Kafka 的 Controller 服务（用于集群管理）。
    - `-e KAFKA_CFG_NODE_ID=1`：设置节点 ID，就像给快递点编号，确保每个节点有唯一标识。
    - `-e KAFKA_CFG_PROCESS_ROLES=broker,controller`：设置这个节点既是“快递员”（Broker，负责处理消息存储和转发），又是“管理者”（Controller，负责管理集群元数据）。
    - `-e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@192.168.110.8:9093`：定义 Controller 的投票成员，这里只有这一个节点，指定为 ID 为 1 的节点，地址是 `192.168.110.8:9093`（本机 IP 和 Controller 端口）。
    - `-e KAFKA_CFG_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093`：设置 Kafka 监听的地址和端口，`0.0.0.0` 表示监听所有网络接口，9092 端口用于 Broker 服务，9093 端口用于 Controller 服务。
    - `-e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://192.168.110.8:9092,CONTROLLER://192.168.110.8:9093`：设置 Kafka 对外公布的地址和端口，告诉客户端和其它 Broker 通过 `192.168.110.8` 这个 IP 地址的 9092 和 9093 端口来连接（请根据你的实际机器 IP 调整）。
    - `-e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER`：指定 Controller 的监听器名称，用于内部管理。
    - `-e ALLOW_PLAINTEXT_LISTENER=yes`：允许明文通信（不加密），简化测试环境配置（生产环境不建议这样设置，应启用加密和认证）。
    - `-v kafka-data:/bitnami/kafka/data`：数据卷挂载，就像给快递点分配一个“仓库”，将 Kafka 的数据存储在本地名为 `kafka-data` 的卷中，防止容器删除后数据丢失。
    - `--network bridge`：使用 Docker 的桥接网络模式，这是 Docker 的默认网络模式，容器通过桥接网络与主机通信，端口映射（如 `-p`）会生效。
    - `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0`：指定使用的 Docker 镜像及其版本，这里是 Bitnami 提供的 Kafka 4.0.0 版本镜像。
    
- **步骤 3：检查 Kafka 是否正常运行**
  启动后，我们检查一下容器状态，确保 Kafka 运行正常。
  - 输入以下命令查看容器状态：
    ```bash
    docker ps
    ```
    如果看到 `kafka-single` 容器状态为 `Up`，说明启动成功。
  - 也可以查看日志，确认是否有错误：
    ```bash
    docker logs kafka-single
    ```
    如果日志中没有明显错误信息（如 `ERROR`），说明 Kafka 基本运行正常。
- **目标**：
  通过简单命令，快速启动一个单机 Kafka 容器，掌握 Docker 部署的基本操作。

### 2.4 部署 Kafka UI（可视化管理工具）
为了更直观地管理 Kafka，我们部署一个 Web UI 工具——Kafka UI。它就像“物流中心的监控屏幕”，可以让你通过浏览器查看和管理 Topic、消息等信息。

- **步骤 1：拉取 Kafka UI 镜像**
  输入以下命令下载 Kafka UI 镜像：
  ```bash
  docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0
  ```
- **步骤 2：启动 Kafka UI 容器**
  输入以下命令启动 Kafka UI，并连接到我们的 Kafka 单机实例：
  ```bash
  docker run -d \
    --name kafka-ui \
    -p 8080:8080 \
    -e KAFKA_CLUSTERS_0_NAME=local \
    -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=192.168.110.8:9092 \
    --network bridge \
    swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0
  ```
  **解释**：
  - `--name kafka-ui`：给容器起个名字，方便管理。
  - `-p 8080:8080`：端口映射，让你可以通过本机的 8080 端口访问 Kafka UI 的 Web 界面。
  - `-e KAFKA_CLUSTERS_0_NAME=local`：设置 Kafka 集群的名称，这里随便起名为 `local`，用于 UI 显示。
  - `-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=192.168.110.8:9092`：设置 Kafka 的连接地址，指向我们单机 Kafka 的地址和端口（`192.168.110.8:9092`），需要与 Kafka 的 `ADVERTISED_LISTENERS` 配置一致。
  - `--network bridge`：使用桥接网络模式，与 Kafka 容器保持一致，确保两者可以通过 IP 地址通信。
  - `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0`：指定 Kafka UI 的 Docker 镜像及其版本。

- **步骤 3：访问 Kafka UI**
  启动后，打开浏览器，访问 `http://192.168.110.8:8080`，你会看到 Kafka UI 的界面。如果连接成功，界面上会显示你的 Kafka 集群信息（名为 `local`）。
  - 你可以点击左侧菜单查看 Topic、Broker 等信息。
  - 目前还没有 Topic，界面可能是空的，接下来我们会创建 Topic 并查看。
- **生活化类比**：
  Kafka UI 就像快递点的“监控屏幕”，你不用亲自去货架上看包裹（手动命令行操作），通过屏幕就能知道有哪些货架（Topic）、包裹数量等信息。
- **目标**：
  通过 Kafka UI，提供一个直观的管理界面，让学员更容易理解和操作 Kafka。

### 2.5 Kafka 单机基础操作实战
现在 Kafka 单机已经运行，我们通过命令行进行一些基础操作，熟悉 Kafka 的核心功能。就像在小型快递点学习如何接收和分发包裹。

- **步骤 1：进入 Kafka 容器**
  由于 Bitnami 镜像中已经包含了 Kafka 的命令行工具，我们直接进入容器操作：
  ```bash
  docker exec -it kafka-single /bin/bash
  ```
  进入后，你可以在容器内运行 Kafka 相关命令。
- **步骤 2：创建 Topic**
  创建一个名为 `test-topic` 的主题，就像在快递点建一个新货架：
  ```bash
  kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  ```
  **解释**：
  - `--topic test-topic`：主题名称。
  - `--partitions 1`：设置 1 个分区（单机只能是 1）。
  - `--replication-factor 1`：设置 1 个副本（单机只能是 1）。
  如果创建成功，会看到类似 `Created topic test-topic` 的输出。
- **步骤 3：发送消息（生产者）**
  启动一个生产者，发送消息到 `test-topic`，就像往货架上放包裹：
  ```bash
  kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
  ```
  然后输入一些消息，比如 `Hello Kafka!`，按 Enter 发送，可以多输入几条，按 Ctrl+D 退出。
- **步骤 4：消费消息（消费者）**
  在另一个终端，进入容器，启动一个消费者读取消息，就像从货架上取包裹：
  ```bash
  docker exec -it kafka-single /bin/bash
  kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092 --from-beginning
  ```
  你应该能看到刚才发送的消息，如 `Hello Kafka!`。
- **步骤 5：通过 Kafka UI 查看**
  打开浏览器，刷新 `http://192.168.110.8:8080`，在 Kafka UI 界面中：
  - 点击左侧 `Topics`，你会看到 `test-topic`。
  - 点击 `test-topic`，可以查看消息内容和分区信息。
- **生活化类比**：
  - 创建 Topic 就像建一个新货架。
  - 发送消息就像往货架上放包裹。
  - 消费消息就像从货架上取包裹。
  - Kafka UI 就像监控屏幕，随时查看货架状态。
- **目标**：
  通过基础命令和 UI 工具，让学员掌握 Kafka 的核心操作，理解消息的发送和消费流程。

### 2.6 单机部署的优势与局限性
- **优势**：
  - **简单易上手**：就像开一个小型快递点，一个人就能搞定，适合学习和测试。
  - **资源占用少**：只需要一台机器，配置要求低。
  - **快速验证**：启动快，操作简单，容易排查问题。
- **局限性**：
  - **无高可用性**：单机只有一个 Broker，如果机器宕机，数据和服务不可用，就像快递点关门就没人处理包裹。
  - **无分布式特性**：无法处理大规模数据和并发请求，就像一个人无法应对“双11”那样的包裹量。

