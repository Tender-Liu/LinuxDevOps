好的，根据您的反馈“Docker Compose 去掉吧，还有新版本的 Kafka 已经不依赖 ZooKeeper 了”，我将对教案内容进行相应调整。以下是更新后的框架和设计思路：


### Kafka 教案内容框架
1. **Kafka 基础与集群架构**
   - Kafka 简介：什么是 Kafka，解决的核心问题（如高并发消息流、异步解耦）。
   - 集群架构详解：核心概念（Topic、Partition、Replica、Broker、Consumer Group 等）。
   - 新版本架构变化：介绍 KRaft 模式（Kafka 内置元数据管理，替代 ZooKeeper 的作用）。
   - 架构图示：使用 Mermaid 图展示 Kafka 集群的典型结构（生产者、消费者、Broker 分布、副本机制），并对比 KRaft 模式和 ZooKeeper 模式的架构差异。
   - 目标：帮助小白理解 Kafka 集群的基本组成、分布式特性以及新版本的技术更新。

2. **Kafka 集群部署（重点：Docker 部署 + KRaft 模式）**
   - **环境准备**：
     - 确保学员安装 Docker（提供安装指南链接或简单步骤）。
     - 硬件要求：建议每位学员的实验环境至少 4GB 内存和 2 核 CPU，以支持小型集群。
     - Kafka 版本：使用最新版本（如 Kafka 3.5.0 或以上），支持 KRaft 模式。
   - **Docker 部署方式（核心内容）**：
     - 使用纯 Docker 命令快速搭建 Kafka 集群（3 个 Broker，基于 KRaft 模式），提供详细的 Docker 命令和配置步骤。
       - 包括拉取 Kafka 镜像、设置环境变量、端口映射、数据卷挂载等。
       - 提供一个简单的 shell 脚本，方便学员一键执行部署。
     - KRaft 模式配置说明：解释如何配置 Kafka 的 `server.properties` 文件以启用 KRaft 模式（如设置 `process.roles`、`node.id` 等参数）。
     - 多人协作设计：
       - **共享环境**：提供统一的 Docker 命令和配置脚本，学员可以在本地或云服务器上快速启动相同配置的 Kafka 集群。
       - **分组实验**：建议将学员分组，每组 3-5 人，模拟企业团队协作，共同操作一个集群（通过共享云服务器或本地网络）。
       - **快速验证**：提供简单的测试命令（如创建 Topic、发送消息、消费消息），让学员在 10 分钟内验证集群是否正常运行。
     - 优势说明：强调 Docker 部署在环境一致性、快速部署和易于重置方面的优势，特别适合多人学习和实验；同时说明 KRaft 模式减少依赖、简化架构的优势。
   - **ZooKeeper 模式（简要介绍）**：
     - 简述传统 ZooKeeper 模式的基本原理和适用场景（作为补充知识点，不展开详细操作）。
     - 提供参考链接，供有兴趣的学员了解历史版本的部署方式。
   - **传统部署方式（简要介绍）**：
     - 简述传统部署（非 Docker）的基本步骤和适用场景（作为补充知识点，不展开详细操作）。
     - 提供参考链接，供有兴趣的学员自行学习。
   - **目标**：
     - 让学员通过纯 Docker 命令快速搭建基于 KRaft 模式的 Kafka 集群，降低环境配置难度，适应最新技术趋势。
     - 通过多人协作实验，模拟企业团队运维场景，提升学习效率和互动性。

3. **Kafka 高可用与故障恢复**
   - 高可用机制：副本机制（Leader 和 Follower），KRaft 模式下的控制器（Controller）选举机制。
   - 节点崩溃恢复流程：故障检测、Leader 切换、数据同步、节点重启加入集群。
   - 配置建议：副本因子（replication.factor）、最小同步副本（min.insync.replicas）等参数设置。
   - 实践模拟：基于 Docker 环境，模拟 Broker 宕机（通过 `docker stop` 命令）和恢复过程，提供操作步骤。
   - 目标：理解 Kafka 如何保证数据不丢失，掌握故障恢复方法，熟悉 Docker 环境下的操作。

4. **企业级问题解决：消息处理与优化**
   - **消息来得太快**：
     - 解决方法：增加分区数、扩展 Broker 节点、调整生产者配置（linger.ms、compression.type）、生产者限流。
     - 实践操作：基于 Docker 环境的分区扩展命令、Broker 扩容步骤（通过 Docker 命令添加容器）。
   - **限制最大消息数**：
     - 解决方法：限制单条消息大小（message.max.bytes）、控制存储总量（log.retention.bytes、log.retention.hours）。
     - 配置建议：合理设置消息保留策略，通过 Docker 环境变量或配置文件修改。
   - **消息积压处理不过来**：
     - 解决方法：增加消费者数量、优化消费者性能、临时扩容消费者组、跳过积压消息（重置偏移量）、回压生产者。
     - 实践操作：基于 Docker 的消费者组管理命令、偏移量重置步骤。
   - 目标：解决企业中常见的消息过载和积压问题，通过 Docker 环境提供具体操作方法。

5. **Kafka 监控与运维**
   - 监控工具：推荐一个轻量工具（如 Kafka Manager 或 Burrow），通过 Docker 部署（提供 Docker 命令和配置步骤）。
   - 监控指标：重点关注吞吐量、消费者 Lag、Broker 健康状态。
   - 运维命令：提供常用命令表格（Topic 管理、生产者消费者测试、消费者组管理等），基于 Docker 容器执行。
   - 权限管理：Kafka ACL 配置与测试（创建用户、设置权限），在 Docker 环境中操作。
   - 目标：掌握 Kafka 集群的实时监控和日常运维技能，熟悉 Docker 环境下的工具使用。

6. **性能优化配置**
   - 核心配置参数：提供生产环境优化建议（如 num.partitions、num.io.threads、log.segment.bytes），通过 Docker 环境变量或配置文件调整。
   - 不同场景优化：高吞吐量场景 vs 高可靠性场景的配置差异。
   - 目标：了解如何根据业务需求调整 Kafka 性能，掌握 Docker 配置修改方法。

7. **教学风格与实践设计（针对多人学习优化）**
   - 面向小白：用通俗语言和生活化类比解释复杂概念（如把 Topic 比作“快递分类”）。
   - 问题驱动：以“问题-解答-实践”结构组织内容，确保学员带着问题学习。
   - 实验任务（多人协作优化）：
     - 为每个模块设计简单实践任务（如创建 Topic、模拟故障、处理积压），提供详细步骤。
     - **分组任务**：每组学员共同完成一个任务（如一组内部分工，分别扮演生产者、消费者、运维角色）。
     - **快速重置**：利用 Docker 快速销毁和重建集群，方便学员多次尝试实验而不担心环境损坏。
     - **共享资源**：提供统一的 Docker 命令和配置脚本，确保所有学员实验环境一致，减少配置错误。
   - 目标：确保小白用户能理解理论并动手操作，通过多人协作提升学习体验和效率。

### 总结与设计思路
- **内容重点**：
  - 部署方式调整为纯 Docker 命令（不使用 Docker Compose），提供详细命令和一键部署脚本，简化操作流程。
  - 以 Kafka 新版本的 KRaft 模式为核心，ZooKeeper 模式和传统部署仅作为补充知识点，适应技术发展趋势。
- **多人学习优化**：
  - 提供统一的 Docker 命令和配置脚本，确保学员环境一致，降低配置难度。
  - 设计分组实验任务，模拟企业团队协作场景，增强互动性和实战感。
  - 利用 Docker 的快速部署和重置特性，让学员可以多次尝试实验，提升学习效率。
- **集群规模**：以 3 个 Broker 的小型集群为教学案例，基于 KRaft 模式，贴近企业入门级环境，同时适合学员实验资源限制。
- **实践导向**：所有实践任务基于 Docker 环境，确保操作步骤简单易懂，方便多人协作完成。







好的，我理解您的需求是将 Kafka 集群部署到三台主机上，由 3 个学员共同完成，并需要说明为什么 Kafka 集群通常使用奇数节点。以下是更新后的内容，包含了跨主机部署的详细步骤和奇数节点的必要性解释。如果有其他需求或优化方向，请随时告知。

---

### 为什么要使用 Kafka 集群？

在介绍 Kafka 集群部署之前，我们先来了解为什么要使用集群。Kafka 是一个分布式消息系统，单节点部署在实际生产环境中往往无法满足高可用性、高吞吐量和数据持久性的需求。以下是使用 Kafka 集群的主要原因：

1. **高可用性**：通过多个 Broker 节点组成集群，即使某个节点发生故障，其他节点仍能继续提供服务，确保系统不中断。
2. **负载均衡与高吞吐量**：集群可以将消息分发到多个节点上处理，支持更高的并发量，满足大规模数据处理需求。
3. **数据冗余与可靠性**：通过分区（Partition）和副本（Replica）机制，数据可以在多个节点上备份，防止数据丢失。
4. **可扩展性**：集群支持动态扩展，可以根据业务需求增加节点，提升处理能力。
5. **企业级应用场景**：在企业环境中，Kafka 集群能够支持多团队、多应用共享消息队列，适应复杂的业务需求。

因此，学习和部署 Kafka 集群不仅是技术要求，更是模拟真实生产环境、提升实战能力的重要一步。接下来，我们将重点介绍如何通过 Docker 在三台主机上部署一个基于 KRaft 模式的 Kafka 集群。

---

### 为什么要使用奇数节点？

在部署 Kafka 集群时，特别是在 KRaft 模式下（或传统 ZooKeeper 模式下），通常推荐使用奇数节点（例如 3、5、7 个节点）。原因如下：

1. **共识协议的需要**：
   - Kafka 的 KRaft 模式使用 Raft 协议来管理元数据和选举 Leader，而 Raft 协议（以及 ZooKeeper 模式下的 Zab 协议）在达成共识时依赖多数投票（majority voting）。
   - 奇数节点可以确保在节点故障时更容易形成多数。例如，3 个节点中只要有 2 个节点正常运行即可形成多数（2/3），而如果是 4 个节点，则需要 3 个节点正常运行（3/4），容错能力反而下降。
2. **容错能力**：
   - 奇数节点允许集群在少数节点故障时仍能正常运行。例如，3 个节点的集群可以容忍 1 个节点故障，而 4 个节点的集群同样只能容忍 1 个节点故障（因为需要多数节点存活），因此 4 个节点并未显著提升容错能力，反而增加了资源成本。
3. **避免脑裂（Split Brain）问题**：
   - 奇数节点可以有效避免在网络分区时出现脑裂问题。如果是偶数节点（例如 4 个），可能会出现两组节点各占一半，无法形成多数，导致集群无法决策。而奇数节点总能确保只有一组节点占据多数，避免冲突。
4. **资源效率与实际需求**：
   - 3 个节点是 Kafka 集群的最小推荐规模，既能满足高可用性和副本机制（replication factor=3），又能控制资源开销，非常适合学习和小型生产环境。

因此，在本次实验中，我们选择 3 个节点部署在 3 台主机上，既符合共识协议的要求，也便于 3 名学员分组协作，每人负责一台主机上的节点管理，模拟企业团队运维场景。

---

### Kafka 集群部署（重点：Docker 部署 + KRaft 模式，跨 3 台主机）

#### 1. 环境准备
- **分组安排**：将 3 名学员组成一组，每人负责一台主机上的 Kafka Broker 节点管理，模拟企业团队协作。
- **Docker 安装**：确保每台主机已安装 Docker。以下是简单安装步骤（以 Ubuntu 为例）：
  1. 更新包索引：`sudo apt update`
  2. 安装 Docker：`sudo apt install docker.io -y`
  3. 启动 Docker 服务：`sudo systemctl start docker`
  4. 验证安装：`docker --version`
  - 更多安装指南可参考官方文档：[Docker 安装指南](https://docs.docker.com/engine/install/)
- **硬件要求**：建议每台主机的实验环境至少有 4GB 内存和 2 核 CPU，以支持 Kafka Broker 节点运行。
- **Kafka 版本**：使用最新版本（如 Kafka 3.5.0 或以上），确保支持 KRaft 模式（Kafka Raft 模式，用于替代 ZooKeeper）。
- **网络要求**：确保 3 台主机在同一网络中，可以互相通信（通过内网 IP 或公网 IP），并记录每台主机的 IP 地址（例如：主机 1：`192.168.1.101`，主机 2：`192.168.1.102`，主机 3：`192.168.1.103`）。

#### 2. Docker 部署方式（核心内容：跨 3 台主机）
我们将通过纯 Docker 命令在 3 台主机上各部署一个 Kafka Broker 节点，组成一个基于 KRaft 模式的 Kafka 集群。以下是详细步骤：

##### 2.1 拉取 Kafka 镜像
在每台主机上执行以下命令，拉取 Confluent 提供的 Kafka 镜像，支持 KRaft 模式：
```bash
docker pull confluentinc/cp-kafka:latest
```

##### 2.2 启动 Kafka Broker 节点（KRaft 模式）
KRaft 模式下，Kafka 使用内置的 Raft 协议管理元数据，无需依赖 ZooKeeper。以下是每台主机上启动 Broker 的命令，包含环境变量、端口映射和数据卷挂载。注意需要根据主机的实际 IP 地址调整 `KAFKA_ADVERTISED_LISTENERS` 和 `KAFKA_CONTROLLER_QUORUM_VOTERS` 参数。

- **主机 1（Broker 1，node.id=1）**：
  假设主机 1 的 IP 为 `192.168.1.101`，在主机 1 上执行：
  ```bash
  docker run -d --name kafka-broker1 \
    -p 9092:9092 \
    -e KAFKA_BROKER_ID=1 \
    -e KAFKA_NODE_ID=1 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.101:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker1-data:/var/lib/kafka/data \
    confluentinc/cp-kafka:latest
  ```

- **主机 2（Broker 2，node.id=2）**：
  假设主机 2 的 IP 为 `192.168.1.102`，在主机 2 上执行：
  ```bash
  docker run -d --name kafka-broker2 \
    -p 9092:9092 \
    -e KAFKA_BROKER_ID=2 \
    -e KAFKA_NODE_ID=2 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.102:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker2-data:/var/lib/kafka/data \
    confluentinc/cp-kafka:latest
  ```

- **主机 3（Broker 3，node.id=3）**：
  假设主机 3 的 IP 为 `192.168.1.103`，在主机 3 上执行：
  ```bash
  docker run -d --name kafka-broker3 \
    -p 9092:9092 \
    -e KAFKA_BROKER_ID=3 \
    -e KAFKA_NODE_ID=3 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.103:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker3-data:/var/lib/kafka/data \
    confluentinc/cp-kafka:latest
  ```

**注意**：
- 请根据实际环境替换 IP 地址（`192.168.1.101`、`192.168.1.102`、`192.168.1.103`）。
- 每台主机上的端口映射均为 `9092:9092`，但由于它们在不同主机上，不会产生冲突。
- `KAFKA_ADVERTISED_LISTENERS` 必须使用主机的实际 IP 地址，以便其他主机和客户端能够连接。

##### 2.3 一键部署 Shell 脚本（每台主机单独执行）
为了方便每位学员在各自主机上快速部署，以下是一个简单的 shell 脚本模板，需根据主机 IP 进行调整后执行：

```bash
#!/bin/bash
# 部署 Kafka Broker 节点
# 请根据主机 IP 和 Broker ID 调整以下参数
BROKER_ID=1
NODE_ID=1
HOST_IP="192.168.1.101"
QUORUM_VOTERS="1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093"

docker run -d --name kafka-broker${BROKER_ID} \
  -p 9092:9092 \
  -e KAFKA_BROKER_ID=${BROKER_ID} \
  -e KAFKA_NODE_ID=${NODE_ID} \
  -e KAFKA_PROCESS_ROLES=broker,controller \
  -e KAFKA_CONTROLLER_QUORUM_VOTERS=${QUORUM_VOTERS} \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://${HOST_IP}:9092 \
  -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -v kafka-broker${BROKER_ID}-data:/var/lib/kafka/data \
  confluentinc/cp-kafka:latest

echo "Kafka Broker ${BROKER_ID} 已启动！"
```

每位学员保存为 `deploy-kafka-broker.sh`，并根据自己的主机 IP 和 Broker ID 修改参数，赋予执行权限：`chmod +x deploy-kafka-broker.sh`，然后运行：`./deploy-kafka-broker.sh`。

##### 2.4 KRaft 模式配置说明
KRaft 模式是 Kafka 3.0+ 引入的新特性，用于替代 ZooKeeper 管理元数据。以下是关键配置参数的说明（对应上述 Docker 环境变量）：
- `KAFKA_PROCESS_ROLES`：定义节点角色，可选 `broker`（处理消息）、`controller`（管理元数据），KRaft 模式下可以组合使用。
- `KAFKA_NODE_ID`：节点的唯一标识，与 `KAFKA_BROKER_ID` 一致。
- `KAFKA_CONTROLLER_QUORUM_VOTERS`：定义控制器节点的投票列表，用于 Raft 协议共识，格式为 `node_id@host:port`，必须包含所有节点的 IP 和端口。
- `KAFKA_LISTENERS` 和 `KAFKA_ADVERTISED_LISTENERS`：配置监听地址和对外暴露地址，确保节点间通信和客户端访问。

##### 2.5 快速验证集群是否正常运行
部署完成后，学员可以协作验证集群功能。以下命令可以在任意一台主机上执行：
1. **创建 Topic**：
   在主机 1 上执行（假设主机 1 的 IP 为 `192.168.1.101`）：
   ```bash
   docker exec -it kafka-broker1 kafka-topics --create --topic test-topic --bootstrap-server 192.168.1.101:9092 --partitions 3 --replication-factor 3
   ```
2. **发送消息**：
   在主机 2 上执行（假设主机 2 的 IP 为 `192.168.1.102`）：
   ```bash
   docker exec -it kafka-broker2 kafka-console-producer --topic test-topic --bootstrap-server 192.168.1.101:9092
   ```
   输入任意消息后回车，例如：`Hello, Kafka Cluster!`
3. **消费消息**：
   在主机 3 上执行（假设主机 3 的 IP 为 `192.168.1.103`）：
   ```bash
   docker exec -it kafka-broker3 kafka-console-consumer --topic test-topic --bootstrap




好的，我会根据你的需求重写教案，补充必要的参数解释，并确保内容对学员更友好、易于理解。以下是重写后的教案，包含 Kafka UI 的部署部分，并对所有命令和参数进行详细说明，确保学员能够轻松学习和操作。

---

### 为什么要使用 Kafka 集群？

在学习 Kafka 集群部署之前，我们先来了解为什么需要使用集群。Kafka 是一个分布式消息系统，如果只使用单节点部署，在实际生产环境中往往无法满足高可用性、高吞吐量和数据持久性的需求。以下是使用 Kafka 集群的主要原因：

1. **高可用性**：Kafka 集群由多个 Broker 节点组成，即使某个节点发生故障，其他节点仍能继续工作，确保系统不会中断。
2. **负载均衡与高吞吐量**：集群可以将消息分发到多个节点上处理，支持更高的并发量，满足大规模数据处理的需求。
3. **数据冗余与可靠性**：通过分区（Partition）和副本（Replica）机制，数据可以在多个节点上备份，避免数据丢失。
4. **可扩展性**：集群支持动态扩展，可以根据业务需求增加节点，提升处理能力。
5. **企业级应用场景**：在企业环境中，Kafka 集群能支持多个团队和应用共享消息队列，适应复杂的业务需求。

因此，学习和部署 Kafka 集群不仅是技术上的要求，也是模拟真实生产环境、提升实战能力的重要一步。接下来，我们将通过 Docker 在三台主机上部署一个基于 KRaft 模式的 Kafka 集群。

---

### 为什么要使用奇数节点？

在部署 Kafka 集群时，特别是在 KRaft 模式下（或传统的 ZooKeeper 模式下），通常推荐使用奇数节点（例如 3、5、7 个节点）。原因如下：

1. **共识协议的需要**：
   - Kafka 的 KRaft 模式使用 Raft 协议来管理元数据和选举 Leader，而 Raft 协议在达成共识时依赖多数投票（majority voting）。
   - 奇数节点更容易在节点故障时形成多数。例如，3 个节点中只要有 2 个正常运行即可形成多数（2/3），而如果是 4 个节点，则需要 3 个节点正常运行（3/4），容错能力反而下降。
2. **容错能力**：
   - 奇数节点允许集群在少数节点故障时仍能正常运行。例如，3 个节点的集群可以容忍 1 个节点故障，而 4 个节点的集群同样只能容忍 1 个节点故障，资源利用效率较低。
3. **避免脑裂（Split Brain）问题**：
   - 奇数节点可以有效避免网络分区时出现的脑裂问题。如果是偶数节点（例如 4 个），可能会出现两组节点各占一半，无法形成多数，导致集群无法决策。而奇数节点总能确保只有一组节点占据多数。
4. **资源效率与实际需求**：
   - 3 个节点是 Kafka 集群的最小推荐规模，既能满足高可用性和副本机制（副本因子=3），又能控制资源开销，非常适合学习和小型生产环境。

因此，在本次实验中，我们选择在 3 台主机上部署 3 个节点，既符合共识协议的要求，也便于 3 名学员分组协作，每人负责一台主机上的节点管理，模拟企业团队运维场景。

---

### Kafka 集群部署（重点：Docker 部署 + KRaft 模式，跨 3 台主机）

#### 1. 环境准备
- **分组安排**：将 3 名学员组成一组，每人负责一台主机上的 Kafka Broker 节点管理，模拟企业团队协作。
- **Docker 安装**：确保每台主机已安装 Docker。以下是简单安装步骤（以 Ubuntu 系统为例）：
  1. 更新软件包索引：`sudo apt update`
  2. 安装 Docker：`sudo apt install docker.io -y`
  3. 启动 Docker 服务：`sudo systemctl start docker`
  4. 验证安装是否成功：`docker --version`（如果输出 Docker 版本信息，说明安装成功）
  - 如果需要更多安装指南，可参考官方文档：[Docker 安装指南](https://docs.docker.com/engine/install/)
- **硬件要求**：建议每台主机的实验环境至少有 4GB 内存和 2 核 CPU，以支持 Kafka Broker 节点的运行。
- **Kafka 版本**：使用最新版本（如 Kafka 3.5.0 或以上），确保支持 KRaft 模式（Kafka Raft 模式，用于替代 ZooKeeper）。
- **网络要求**：确保 3 台主机在同一网络中，可以互相通信（通过内网 IP 或公网 IP），并记录每台主机的 IP 地址（例如：主机 1：`192.168.1.101`，主机 2：`192.168.1.102`，主机 3：`192.168.1.103`）。

#### 2. Docker 部署方式（核心内容：跨 3 台主机）
我们将通过 Docker 命令在 3 台主机上各部署一个 Kafka Broker 节点，组成一个基于 KRaft 模式的 Kafka 集群。以下是详细步骤，并对每个命令和参数进行解释。

##### 2.1 拉取 Kafka 镜像
在每台主机上执行以下命令，拉取 Confluent 提供的 Kafka 镜像（支持 KRaft 模式）：
```bash
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
```
**命令解释**：
- `docker pull`：Docker 的命令，用于从 Docker Hub 下载镜像。
- `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0`：指定要下载的镜像名称和标签，`4.0.0` 表示版本。

##### 2.2 启动 Kafka Broker 节点（KRaft 模式）
KRaft 模式是 Kafka 3.0+ 引入的新特性，使用内置的 Raft 协议管理元数据，无需依赖 ZooKeeper。以下是每台主机上启动 Broker 的命令，包含环境变量、端口映射和数据卷挂载。注意需要根据主机的实际 IP 地址调整参数。

- **主机 1（Broker 1，node.id=1）**：
  假设主机 1 的 IP 为 `192.168.1.101`，在主机 1 上执行：
  ```bash
  docker run -d --name kafka-broker1 \
    --network host \
    -e KAFKA_BROKER_ID=1 \
    -e KAFKA_NODE_ID=1 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.101:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker1-data:/var/lib/kafka/data \
    swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
  ```

- **主机 2（Broker 2，node.id=2）**：
  假设主机 2 的 IP 为 `192.168.1.102`，在主机 2 上执行：
  ```bash
  docker run -d --name kafka-broker2 \
    --network host \
    -e KAFKA_BROKER_ID=2 \
    -e KAFKA_NODE_ID=2 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.102:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker2-data:/var/lib/kafka/data \
    swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
  ```

- **主机 3（Broker 3，node.id=3）**：
  假设主机 3 的 IP 为 `192.168.1.103`，在主机 3 上执行：
  ```bash
  docker run -d --name kafka-broker3 \
    --network host \
    -e KAFKA_BROKER_ID=3 \
    -e KAFKA_NODE_ID=3 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.1.103:9092 \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -v kafka-broker3-data:/var/lib/kafka/data \
    swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0
  ```

**命令和参数解释**：
- `docker run`：Docker 命令，用于启动一个容器。
- `-d`：后台运行容器，不占用当前终端。
- `--name kafka-broker1`：为容器命名，便于后续管理（每个主机上的容器名称不同）。
- `-p 9092:9092`：端口映射，将容器内的 9092 端口映射到主机的 9092 端口，用于 Kafka 客户端连接。
- `-p 9093:9093`: Kafka 控制器之间的专用端口，用于 Broker 节点间进行元数据同步和 Leader 选举等操作`
- `-e`：设置环境变量，用于配置 Kafka 的运行参数：
  - `KAFKA_BROKER_ID`：Broker 的唯一标识符，每个节点不同。
  - `KAFKA_NODE_ID`：节点 ID，与 Broker ID 一致，用于 KRaft 模式。
  - `KAFKA_PROCESS_ROLES`：定义节点角色，`broker` 表示处理消息，`controller` 表示管理元数据，KRaft 模式下可以组合。
  - `KAFKA_CONTROLLER_QUORUM_VOTERS`：定义控制器节点的投票列表，用于 Raft 协议共识，格式为 `node_id@host:port`，包含所有节点的 IP 和端口。
  - `KAFKA_LISTENERS`：配置 Kafka 监听的地址和端口，`PLAINTEXT://0.0.0.0:9092` 用于消息通信，`CONTROLLER://0.0.0.0:9093` 用于元数据管理。
  - `KAFKA_ADVERTISED_LISTENERS`：配置对外暴露的地址，客户端和其它 Broker 通过此地址连接，必须使用主机的实际 IP。
  - `KAFKA_INTER_BROKER_LISTENER_NAME`：Broker 间通信使用的监听器名称，这里是 `PLAINTEXT`。
- `-v kafka-broker1-data:/var/lib/kafka/data`：数据卷挂载，将容器内 Kafka 数据存储到主机上，避免容器删除后数据丢失。
- `confluentinc/cp-kafka:latest`：指定使用的 Docker 镜像。

**注意**：
- 请根据实际环境替换 IP 地址（`192.168.1.101`、`192.168.1.102`、`192.168.1.103`）。
- 每台主机上的端口映射均为 `9092:9092`，但由于它们在不同主机上，不会产生冲突。

##### 2.3 一键部署 Shell 脚本（每台主机单独执行）
为了方便每位学员在各自主机上快速部署，以下是一个简单的 shell 脚本模板，需根据主机 IP 和 Broker ID 进行调整后执行-进公司用的-现在不许偷懒

```bash
#!/bin/bash
# 部署 Kafka Broker 节点
# 请根据主机 IP 和 Broker ID 调整以下参数
BROKER_ID=1
NODE_ID=1
HOST_IP="192.168.1.101"
QUORUM_VOTERS="1@192.168.1.101:9093,2@192.168.1.102:9093,3@192.168.1.103:9093"

docker run -d --name kafka-broker${BROKER_ID} \
  --network host \
  -e KAFKA_BROKER_ID=${BROKER_ID} \
  -e KAFKA_NODE_ID=${NODE_ID} \
  -e KAFKA_PROCESS_ROLES=broker,controller \
  -e KAFKA_CONTROLLER_QUORUM_VOTERS=${QUORUM_VOTERS} \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://${HOST_IP}:9092 \
  -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -v kafka-broker${BROKER_ID}-data:/var/lib/kafka/data \
  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/bitnami/kafka:4.0.0

echo "Kafka Broker ${BROKER_ID} 已启动！"
```

**使用方法**：
1. 每位学员将上述代码保存为文件 `deploy-kafka-broker.sh`。
2. 根据自己的主机 IP 和 Broker ID 修改脚本中的参数（`BROKER_ID`、`NODE_ID`、`HOST_IP`）。
3. 赋予执行权限：`chmod +x deploy-kafka-broker.sh`。
4. 运行脚本：`./deploy-kafka-broker.sh`。

##### 2.4 快速验证集群是否正常运行
部署完成后，学员可以协作验证集群功能。以下命令可以在任意一台主机上执行：

1. **创建 Topic**：
   在主机 1 上执行（假设主机 1 的 IP 为 `192.168.1.101`）：
   ```bash
   docker exec -it kafka-broker1 kafka-topics --create --topic test-topic --bootstrap-server 192.168.1.101:9092 --partitions 3 --replication-factor 3
   ```
   **命令解释**：
   - `docker exec -it kafka-broker1`：进入名为 `kafka-broker1` 的容器内部。
   - `kafka-topics --create`：Kafka 提供的工具，用于创建主题（Topic）。
   - `--topic test-topic`：指定主题名称为 `test-topic`。
   - `--bootstrap-server 192.168.1.101:9092`：指定连接的 Kafka Broker 地址。
   - `--partitions 3`：设置主题的分区数为 3。
   - `--replication-factor 3`：设置副本因子为 3，确保数据在 3 个 Broker 上备份。

2. **发送消息**：
   在主机 2 上执行（假设主机 1 的 IP 为 `192.168.1.101`）：
   ```bash
   docker exec -it kafka-broker2 kafka-console-producer --topic test-topic --bootstrap-server 192.168.1.101:9092
   ```
   **命令解释**：
   - `kafka-console-producer`：Kafka 提供的生产者工具，用于发送消息。
   - 输入任意消息后回车，例如：`Hello, Kafka Cluster!`，然后按 `Ctrl+C` 退出。

3. **消费消息**：
   在主机 3 上执行（假设主机 1 的 IP 为 `192.168.1.101`）：
   ```bash
   docker exec -it kafka-broker3 kafka-console-consumer --topic test-topic --bootstrap-server 192.168.1.101:9092 --from-beginning
   ```
   **命令解释**：
   - `kafka-console-consumer`：Kafka 提供的消费者工具，用于接收消息。
   - `--from-beginning`：从主题的开始位置读取消息，确保能看到之前发送的消息。
   - 如果看到主机 2 发送的消息，说明集群正常运行。

#### 3. 部署 Kafka UI（图形化管理工具）
为了更直观地管理 Kafka 集群，我们将部署一个 Kafka UI 工具，它是一个基于 Web 的图形化界面，可以查看主题、消息、Broker 状态等信息。

##### 3.1 部署 Kafka UI 容器
在任意一台主机上（建议选择主机 1）执行以下命令，部署 Kafka UI：

```bash
# 先删除现有容器（如果有，避免冲突）
docker rm -f kafka-ui

# 运行 Kafka UI 容器
docker run -d \
  --name kafka-ui \
  -p 8080:8080 \
  -e KAFKA_CLUSTERS_0_NAME=local \
  -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=192.168.1.101:9092,192.168.1.102:9092,192.168.1.103:9092 \
  --network bridge \
  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0
```

**命令和参数解释**：
- `docker rm -f kafka-ui`：删除名为 `kafka-ui` 的容器（如果存在），避免启动时冲突。`-f` 表示强制删除，即使容器正在运行。
- `docker run -d`：后台运行一个新容器。
- `--name kafka-ui`：为容器命名为 `kafka-ui`，便于管理。
- `-p 8080:8080`：端口映射，将容器内的 8080 端口映射到主机的 8080 端口，方便通过浏览器访问。
- `-e KAFKA_CLUSTERS_0_NAME=local`：设置 Kafka 集群的名称，显示在 UI 界面中，这里命名为 `local`。
- `-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=192.168.1.101:9092,192.168.1.102:9092,192.168.1.103:9092`：指定 Kafka 集群的 Broker 地址列表，UI 将通过这些地址连接到集群。请根据实际 IP 替换。
- `--network bridge`：使用 Docker 的桥接网络模式，确保容器可以与主机网络通信。
- `swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/kafbat/kafka-ui:v1.2.0`：指定 Kafka UI 的镜像名称和版本。

##### 3.2 访问 Kafka UI
部署完成后，在浏览器中访问 `http://你的主机IP:8080`（例如 `http://192.168.1.101:8080`），即可看到 Kafka UI 界面。你可以在界面中查看集群状态、主题列表、消息内容等。

