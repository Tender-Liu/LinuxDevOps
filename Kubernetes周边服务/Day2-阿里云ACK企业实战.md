# 阿里云 ACK 企业实战

## 教学目标
- 掌握阿里云容器服务 ACK（Aliyun Container Service for Kubernetes）的基本概念和使用方法。
- 理解如何在阿里云 VPC 环境中部署和管理 Kubernetes 集群。
- 学会将已掌握的 Kubernetes 核心组件知识（Pod、ConfigMap、Secret、Deployment、StatefulSet、DaemonSet、Service、Ingress-Nginx 及调度策略）应用到 ACK 中。
- 熟悉阿里云 ACK 与 VPC、ECS 等核心组件的集成方式。

## 学习提前准备
- **Kubernetes 基础**：学员已在虚拟机实验环境中完成 Kubernetes 的全部学习，熟练掌握 Pod、ConfigMap、Secret、Deployment、StatefulSet、DaemonSet、Service、Ingress-Nginx 以及调度策略等核心组件的使用。
- **阿里云基础**：学员已学习阿里云 VPC 和 ECS 等核心组件，并为 ACK 的网络环境做好准备。


## 第一部分：阿里云 ACK 基础介绍
谢谢您的肯定！接下来我会为您详细介绍阿里云 ACK（Aliyun Container Service for Kubernetes）的理论知识，重点讲解其概念、架构、优势以及与其他 Kubernetes 解决方案的对比。以下内容将以清晰的结构呈现，方便您理解和使用。

### 一、什么是阿里云 ACK
**阿里云 ACK（Aliyun Container Service for Kubernetes）** 是阿里云提供的一种托管式 Kubernetes 服务，旨在帮助用户快速构建、部署和管理容器化应用，而无需手动管理底层基础设施。ACK 基于开源的 Kubernetes 技术，结合阿里云的云计算能力，提供了一个高可用、高性能、易于扩展的容器编排平台。

- **核心定位**：ACK 是一种 **PaaS（平台即服务）** 产品，专注于容器集群的管理，降低了用户自建 Kubernetes 集群的复杂性和运维成本。
- **发展背景**：随着容器技术（如 Docker）和容器编排工具（如 Kubernetes）的普及，企业对高效容器管理的需求日益增加。阿里云 ACK 应运而生，旨在为企业提供一站式的容器解决方案。


### 二、ACK 的架构与工作原理
ACK 的架构设计充分利用了阿里云的基础设施，并对 Kubernetes 进行了深度优化。以下是 ACK 的核心架构和运行机制：

#### 1. **集群类型**
ACK 提供两种主要集群类型，满足不同用户需求：
- **托管集群（Managed Cluster）**：
  - 控制平面（Master 节点，包括 kube-apiserver、etcd 等）由阿里云完全托管，用户无需关心控制平面的运维。
  - 用户只需管理 Worker 节点（运行工作负载的节点），可以自定义节点的配置和数量。
  - 适合大多数企业用户，降低了运维门槛。
- **专有集群（Dedicated Cluster）**：
  - 用户独占整个 Kubernetes 集群，包括控制平面和 Worker 节点。
  - 提供更高的隔离性和自定义能力，适合对安全性和合规性要求极高的场景。
  - 用户需要承担更多的运维工作，但仍可享受阿里云的技术支持。

#### 2. **核心组件**
ACK 的架构基于 Kubernetes 的标准组件，并结合阿里云的云原生技术进行优化：
- **控制平面（Control Plane）**：
  - 包括 kube-apiserver（API 服务器）、kube-controller-manager（控制器管理器）、kube-scheduler（调度器）和 etcd（分布式存储）。
  - 在托管集群中，这些组件由阿里云管理，运行在高可用的云基础设施上。
- **Worker 节点**：
  - 运行用户的容器工作负载，包含 kubelet（节点代理）和 kube-proxy（网络代理）。
  - 节点基于阿里云 ECS（弹性计算服务）实例，用户可选择不同规格和操作系统。
- **网络插件**：
  - 支持多种网络模式，包括 Flannel（Overlay 网络）和 Terway（基于阿里云 ENI 弹性网卡的 Underlay 网络）。
  - Terway 是阿里云推荐的网络插件，与 VPC 深度集成，提供高性能、低延迟的网络通信。
- **存储插件**：
  - 集成阿里云的存储服务，如 NAS（网络附加存储）、OSS（对象存储）和磁盘存储，支持动态卷分配（PV/PVC）。
- **其他插件**：
  - 提供日志（SLS）、监控（Prometheus）、安全（容器安全扫描）等增值服务。

#### 3. **工作流程**
- 用户通过阿里云控制台或 CLI 创建 ACK 集群，指定 VPC、子网、节点规格等参数。
- 阿里云自动完成控制平面和 Worker 节点的部署，并配置网络、存储等资源。
- 用户通过 kubectl 或控制台与集群交互，部署应用、配置资源和监控状态。
- ACK 自动处理集群的版本升级、节点修复和负载均衡等任务。


### 三、阿里云 ACK 的核心优势
ACK 相较于自建 Kubernetes 集群或其他云厂商的容器服务，具有以下显著优势：

#### 1. **托管服务，降低运维成本**
- **控制平面托管**：在托管集群模式下，控制平面的部署、升级和维护完全由阿里云负责，用户无需担心 Master 节点的可用性和稳定性。
- **自动化运维**：ACK 提供自动化的节点修复、版本升级和集群扩展功能，减少了人工干预的需求。
- **一键创建**：通过阿里云控制台，用户只需几分钟即可完成一个高可用 Kubernetes 集群的创建，无需手动安装和配置。

#### 2. **与阿里云生态深度集成**

- **网络集成**：通过 Terway 网络插件，ACK 与阿里云 VPC 无缝集成，支持弹性网卡（ENI）直接分配给 Pod，提供高性能网络。
- **存储集成**：支持阿里云多种存储服务（如 NAS、OSS、云盘），满足不同场景的存储需求。
- **负载均衡**：自动绑定阿里云 SLB（负载均衡），实现外部流量的高效分发。
- **其他服务**：与阿里云日志服务（SLS）、监控服务（ARMS）、数据库（RDS）等无缝对接，提供完整的云原生解决方案。

#### 3. **高可用性和弹性扩展**

- **多可用区部署**：ACK 支持将节点分布在多个可用区（如杭州的 B、D、E、F 区），确保集群的高可用性。
- **自动扩缩容**：支持 HPA（水平 Pod 自动扩展）和集群节点自动扩缩容，根据负载动态调整资源。
- **故障恢复**：阿里云基础设施提供高可靠性的底层支持，ACK 能够快速恢复节点故障。

#### 4. **安全性与合规性**
- **网络隔离**：通过 VPC 和子网划分（如您提供的 Public 和 Private 子网），实现集群与外部环境的隔离。
- **权限管理**：集成阿里云 RAM（资源访问管理），支持细粒度的权限控制。
- **合规支持**：ACK 符合多种行业标准和合规要求，适合金融、医疗等敏感行业。

#### 5. **丰富的生态与工具支持**
- **插件生态**：提供丰富的插件，如 Ingress-Nginx、Prometheus、Istio 等，支持一键安装。
- **DevOps 支持**：集成 CI/CD 工具，支持容器镜像构建和自动化部署。
- **社区兼容性**：完全兼容 Kubernetes 社区标准，用户熟悉的 kubectl 和 YAML 文件可直接使用。

#### 6. **成本优化**
- **按需付费**：Worker 节点基于 ECS 实例，按小时或按需计费，节省资源成本。
- **资源复用**：通过 Terway 网络模式，Pod 可直接使用 VPC 内的 IP 地址，避免 Overlay 网络的性能开销。


### 四、ACK 与自建 Kubernetes 集群的对比
为了帮助您更好地理解 ACK 的价值，以下是将 ACK 与虚拟机自建 Kubernetes 集群进行对比：

| **维度**            | **阿里云 ACK**                              | **自建 Kubernetes 集群**                  |
|---------------------|--------------------------------------------|------------------------------------------|
| **部署难度**        | 一键创建，几分钟完成                      | 手动安装配置，耗时长，需专业知识         |
| **运维成本**        | 控制平面托管，运维负担低                  | 需自行维护 Master 和 Worker 节点         |
| **高可用性**        | 自动支持多可用区部署，故障恢复快          | 需手动配置 HA，依赖硬件和网络稳定性      |
| **扩展性**          | 支持自动扩缩容，弹性强                    | 扩展需手动添加节点，配置复杂             |
| **生态集成**        | 与阿里云 VPC、存储、负载均衡无缝集成      | 需自行集成外部服务，适配成本高           |
| **安全性**          | 集成 RAM 和 VPC 隔离，安全性高            | 需自行配置网络隔离和权限管理             |
| **成本**            | 按需付费，初期成本低                      | 硬件和人力成本高，初期投入大             |

**总结**：对于大多数企业和开发者而言，ACK 提供了更低的入门门槛、更高效的运维体验和更强的生态支持，非常适合从虚拟机环境过渡到云原生环境的用户。


### 五、ACK 的适用场景
ACK 适用于以下常见场景，结合您的学员背景，这些场景可以作为学习的重点：
- **微服务架构**：通过 ACK 部署和管理复杂的微服务应用，利用 Service 和 Ingress 实现服务发现和流量管理。
- **CI/CD 流水线**：集成阿里云镜像服务（ACR），实现代码构建、镜像推送和自动化部署。
- **大数据与 AI 应用**：利用 ACK 的 GPU 节点支持，运行机器学习和深度学习任务。
- **高可用业务**：通过多可用区部署和自动扩缩容，确保业务系统的高可用性和稳定性。
- **混合云部署**：结合阿里云和本地环境，通过 ACK Anywhere 实现统一的容器管理。


## 第二部分：阿里云 ACR 理论与 Harbor 对比

### 一、什么是阿里云 ACR
**阿里云 ACR（Aliyun Container Registry）** 是阿里云提供的一种托管式容器镜像服务，用于存储、分发和管理 Docker 镜像。ACR 旨在帮助用户构建、存储和分发容器镜像，支持与阿里云 ACK（容器服务 Kubernetes）无缝集成，提供高效、安全的镜像管理能力。

#### 1. **核心功能**
- **镜像存储**：支持 Docker 镜像和 OCI（Open Container Initiative）标准的镜像存储，提供无限的存储空间。
- **镜像分发**：通过全球加速节点，提供高速的镜像拉取和推送服务，适合分布式团队和 CI/CD 流程。
- **权限管理**：集成阿里云 RAM（资源访问管理），支持细粒度的访问控制，确保镜像安全。
- **镜像安全**：内置镜像漏洞扫描功能，自动检测镜像中的安全漏洞并提供修复建议。
- **版本管理**：支持镜像标签（Tag）管理，方便版本控制和回滚。
- **触发器与自动化**：支持镜像构建触发器，自动触发 CI/CD 流水线中的构建和部署任务。

#### 2. **架构与工作原理**
- **镜像仓库**：ACR 提供两种仓库类型：
  - **企业版仓库**：面向企业用户，支持更高的并发和性能，提供镜像缓存和跨地域复制功能。
  - **个人版仓库**：适合个人开发者，免费使用但功能和性能受限。
- **地域与加速**：ACR 部署在阿里云的多个地域，每个地域有独立的镜像仓库，支持就近访问和全球加速。
- **与 ACK 集成**：ACR 可直接与 ACK 集群对接，集群中的 Pod 可通过内网快速拉取镜像，避免公网传输的延迟和成本。

#### 3. **使用场景**
- **CI/CD 集成**：在持续集成和持续部署流程中，ACR 作为镜像存储和分发的核心组件，支持自动化构建和部署。
- **微服务开发**：为微服务架构中的多个服务提供统一的镜像管理平台。
- **跨团队协作**：通过权限管理，允许多个团队共享镜像仓库，提高开发效率。
- **安全合规**：通过漏洞扫描和访问控制，满足企业对镜像安全和合规性的要求。


### 二、阿里云 ACR 的优势
ACR 作为云原生生态的一部分，具备以下显著优势：

#### 1. **与阿里云生态深度集成**
- **无缝对接 ACK**：ACR 与阿里云容器服务（ACK）无缝集成，集群可通过内网高速拉取镜像，提升部署效率。
- **支持其他服务**：与阿里云 CI/CD 工具、日志服务（SLS）等集成，提供完整的云原生开发体验。
- **内网传输**：在阿里云 VPC 环境中，镜像传输走内网，避免公网带宽成本和延迟。

#### 2. **高性能与全球加速**
- **全球节点**：ACR 在全球多个地域部署镜像仓库，支持就近访问和镜像分发。
- **镜像缓存**：企业版支持镜像缓存功能，加速镜像拉取，特别适合大规模集群部署。
- **跨地域复制**：支持镜像跨地域同步，确保分布式团队和应用的镜像一致性。

#### 3. **安全性与可靠性**
- **漏洞扫描**：自动扫描镜像中的安全漏洞，并提供修复建议，帮助用户构建安全的容器环境。
- **权限控制**：通过 RAM 实现细粒度的访问控制，支持子账号、角色和临时凭证管理。
- **高可用性**：基于阿里云基础设施，ACR 提供高可用性和数据冗余，确保镜像不会丢失。

#### 4. **易用性与自动化**
- **控制台与 CLI 支持**：通过阿里云控制台或 CLI 工具，用户可以轻松管理镜像仓库和镜像。
- **构建触发器**：支持基于代码提交或定时任务的镜像构建自动化，简化 CI/CD 流程。
- **免费额度**：个人版提供免费的基础服务，降低小型团队和个人开发者的使用成本。


### 三、Harbor 简介
**Harbor** 是一个开源的容器镜像仓库，由 VMware 发起并维护，广泛用于企业内部的私有镜像管理。Harbor 提供了一个安全、可靠的镜像存储和分发平台，特别适合需要自建镜像仓库的场景。

#### 1. **核心功能**
- **镜像存储与管理**：支持 Docker 镜像和 OCI 镜像，提供镜像标签管理和版本控制。
- **权限管理**：支持基于角色的访问控制（RBAC），允许多用户和多团队协作。
- **镜像安全**：集成漏洞扫描工具（如 Trivy），检测镜像中的安全问题。
- **镜像复制**：支持镜像跨仓库和跨实例的复制，适合分布式环境。
- **Web UI**：提供直观的图形界面，方便用户管理镜像和配置仓库。
- **API 支持**：提供 RESTful API，支持与 CI/CD 工具集成。

#### 2. **架构与工作原理**
- Harbor 是一个自建服务，通常部署在企业内部的服务器或虚拟机上。
- 核心组件包括代理服务、核心服务、数据库、镜像存储和日志系统。
- 支持多种存储后端，如本地文件系统、S3、Swift 等，灵活性较高。
- 可通过 Docker Compose 或 Helm Chart 快速部署。

#### 3. **使用场景**
- **私有化部署**：适合对数据安全和隐私有严格要求的企业，镜像数据完全存储在内部。
- **离线环境**：在无公网或限制公网访问的环境中，Harbor 可作为独立的镜像仓库使用。
- **开源生态**：作为开源项目，Harbor 允许企业根据需求定制功能。

### 四、阿里云 ACR 与 Harbor 的对比
为了帮助学员更清晰地理解两者的区别和适用场景，以下从多个维度对阿里云 ACR 和 Harbor 进行详细对比：

| **维度**            | **阿里云 ACR**                              | **Harbor**                               |
|---------------------|--------------------------------------------|-----------------------------------------|
| **部署方式**        | 托管服务，无需自建，直接在阿里云上使用     | 自建服务，需在企业内部服务器或云上部署   |
| **运维成本**        | 阿里云负责运维，用户无需关心基础设施      | 需自行维护服务器、存储和网络，运维成本高 |
| **与 Kubernetes 集成** | 与 ACK 无缝集成，内网高速拉取镜像         | 可与任何 Kubernetes 集群集成，但需配置   |
| **性能与加速**      | 全球加速节点，镜像缓存和跨地域复制         | 性能依赖部署环境，无内置全球加速功能     |
| **安全性**          | 集成 RAM 权限管理，内置漏洞扫描            | 支持 RBAC 和漏洞扫描，但需自行配置       |
| **存储与扩展**      | 无限存储空间，基于阿里云基础设施           | 存储受限于部署环境，需手动扩展           |
| **易用性**          | 阿里云控制台和 CLI，操作简单               | 提供 Web UI 和 API，但部署配置较复杂     |
| **成本**            | 按需付费，个人版免费，企业版按使用量计费   | 开源免费，但需承担硬件和人力成本         |
| **适用场景**        | 云原生开发、CI/CD 集成、分布式团队         | 私有化部署、离线环境、自定义需求         |

#### 1. **部署与运维**
- **ACR**：作为托管服务，用户无需关心底层基础设施，阿里云负责服务器、存储和网络的维护，适合希望快速上手的团队。
- **Harbor**：需要自建和维护，部署过程涉及服务器配置、存储选择和网络设置，适合有技术能力和私有化需求的团队。

#### 2. **性能与扩展**
- **ACR**：依托阿里云的全球基础设施，提供镜像加速和跨地域复制功能，适合大规模、分布式的应用场景。
- **Harbor**：性能受限于部署环境，扩展性依赖于硬件资源，适合中小规模或内部使用的场景。

#### 3. **安全性与合规性**
- **ACR**：通过阿里云 RAM 提供细粒度的权限控制，内置漏洞扫描，符合企业级安全要求。
- **Harbor**：支持 RBAC 和漏洞扫描，但安全功能的配置和维护需用户自行完成，适合对安全有自定义需求的场景。

#### 4. **成本与资源**
- **ACR**：按需付费模式，初期成本低，适合云上用户；个人版免费功能有限，企业版按流量和存储计费。
- **Harbor**：开源免费，但需要投入硬件和人力成本，长期运维成本可能较高。

#### 5. **适用场景总结**
- **选择 ACR 的场景**：
  - 已经在阿里云生态中，使用 ACK 进行容器管理。
  - 需要全球加速和跨地域镜像分发。
  - 希望降低运维成本，快速构建 CI/CD 流水线。
- **选择 Harbor 的场景**：
  - 需要私有化部署，镜像数据不能存储在云端。
  - 处于离线环境或对镜像仓库有高度定制化需求。
  - 团队有足够的技术能力进行部署和维护。


### 一、阿里云 ACR 中的命名空间（Namespace）
在阿里云 ACR 中，镜像仓库的管理引入了“命名空间（Namespace）”的概念，作为镜像仓库的逻辑分组单位。以下是命名空间的核心特点和作用：

- **定义**：命名空间是 ACR 中用于组织和管理镜像仓库的逻辑层级，类似于一个大的容器，用于容纳多个镜像仓库（Repository）。
- **层级结构**：
  - 命名空间（Namespace）：顶层分组单位，通常对应一个团队、部门或业务线。
  - 镜像仓库（Repository）：隶属于某个命名空间，用于存储具体的镜像及其版本（Tag）。
- **作用**：
  - **逻辑隔离**：通过命名空间，可以将不同团队或项目的镜像仓库隔离开来，避免命名冲突。
  - **权限管理**：ACR 支持对命名空间级别的权限控制，管理员可以为不同用户或角色分配命名空间的访问权限（如只读、读写）。
  - **管理便捷**：命名空间便于大规模镜像管理，尤其是在企业环境中，可以按业务线或开发团队划分。
- **创建与使用**：
  - 在阿里云控制台中，用户需要先创建一个命名空间（例如 `team-a`），然后在该命名空间下创建具体的镜像仓库（例如 `team-a/nginx`）。
  - 镜像的完整路径为 `命名空间/镜像仓库:标签`，如 `team-a/nginx:1.0.0`。

### 二、Harbor 中的项目（Project）管理
在 Harbor 中，镜像仓库的管理主要基于“项目（Project）”的概念，项目是镜像仓库的直接分组单位。以下是项目的核心特点和作用：

- **定义**：项目是 Harbor 中用于组织和管理镜像仓库的基本单位，通常对应一个具体的应用、团队或业务模块。
- **层级结构**：
  - 项目（Project）：直接作为镜像仓库的容器，没有额外的命名空间层级。
  - 镜像仓库（Repository）：隶属于某个项目，存储具体的镜像及其版本（Tag）。
- **作用**：
  - **逻辑分组**：项目用于将镜像仓库按业务或团队分组，类似于 ACR 的命名空间，但层级更扁平。
  - **权限管理**：Harbor 支持项目级别的权限控制，管理员可以为用户分配项目的角色（如管理员、开发者、访客）。
  - **管理方式**：项目是 Harbor 的核心管理单位，用户直接在项目中创建和管理镜像仓库。
- **创建与使用**：
  - 在 Harbor 的 Web UI 或 CLI 中，用户直接创建一个项目（例如 `team-a`），然后在该项目下创建镜像仓库（例如 `team-a/nginx`）。
  - 镜像的完整路径为 `项目/镜像仓库:标签`，如 `team-a/nginx:1.0.0`。

## 三、ACR 命名空间与 Harbor 项目的区别
根据您的描述，ACR 和 Harbor 在管理镜像仓库时的主要区别在于 ACR 多了一个“命名空间”的概念，而 Harbor 直接使用“项目”进行管理。以下是两者的详细对比：

| **维度**            | **阿里云 ACR（命名空间）**                  | **Harbor（项目）**                      |
|---------------------|--------------------------------------------|-----------------------------------------|
| **管理层级**        | 多层级：命名空间 → 镜像仓库                | 单层级：项目 → 镜像仓库                |
| **命名空间/项目作用** | 命名空间用于逻辑隔离和权限管理，通常对应团队或业务线 | 项目直接用于分组和权限管理，通常对应具体应用或团队 |
| **创建流程**        | 先创建命名空间，再在命名空间下创建镜像仓库  | 直接创建项目，在项目下创建镜像仓库      |
| **镜像路径**        | 命名空间/镜像仓库:标签（如 `team-a/nginx:1.0.0`） | 项目/镜像仓库:标签（如 `team-a/nginx:1.0.0`） |
| **适用场景**        | 适合大规模企业环境，支持更细粒度的逻辑分组  | 适合中小规模团队，管理结构更简单直接    |

### 1. **层级结构的差异**
- **ACR**：引入了“命名空间”作为额外的层级，使得镜像管理更加结构化，适合复杂的组织架构。例如，一个企业可以为每个部门创建一个命名空间（如 `marketing`、`engineering`），然后在每个命名空间下创建多个镜像仓库（如 `marketing/campaign-app`）。
- **Harbor**：直接以“项目”作为分组单位，层级更扁平，适合管理较为简单的场景。例如，一个团队可以为每个应用创建一个项目（如 `web-app`），然后在项目中管理镜像仓库（如 `web-app/frontend`）。

### 2. **创建与管理流程的差异**
- **ACR**：用户需要先创建一个命名空间，然后才能在该命名空间下创建镜像仓库。这增加了管理步骤，但也提供了更清晰的逻辑划分。
- **Harbor**：用户直接创建项目并在项目中管理镜像仓库，流程更简洁，适合快速上手。

### 3. **适用场景的差异**
- **ACR 的命名空间**：更适合大型企业或复杂项目，命名空间可以映射到组织结构中的部门、团队或业务线，便于大规模镜像管理和权限分配。
- **Harbor 的项目**：更适合中小型团队或简单项目，项目直接对应具体的业务需求，管理方式更直观。


### 第三部分：ACK 集群网络规划与 VPC 集成-前置条件
**目标**：理解 ACK 集群如何与已准备好的 VPC 网络环境集成。

- **内容**：
  1. **回顾 VPC 网络结构**：
     - VPC 名称：`vpc-prod-shiqi`，IP 范围：`10.8.0.0/16`，覆盖所有子网。
     - 可用区分布：杭州的 B、D、E、F 四个可用区，确保高可用性。
     - 交换机（子网）划分：
       - **Public 子网**：`switch-public-region-b`（10.8.0.0/24，B 区）、`switch-public-region-d`（10.8.1.0/24，D 区）。
       - **Private 子网**：`switch-private-region-b`（10.8.4.0/22，B 区）、`switch-private-region-d`（10.8.8.0/22，D 区）、`switch-private-region-e`（10.8.12.0/22，E 区）、`switch-private-region-f`（10.8.16.0/22，F 区）。
     - NAT 网关：`nat-route-private` 部署在 Public 子网（10.8.1.0/24，D 区），绑定 EIP `121.43.144.176`，用于 Private 子网访问公网。
     - 路由表：`route-prod-shiqi` 管理所有子网流量，Private 子网通过 NAT 网关访问互联网。
  2. **ACK 网络模式**：
     - **Flannel 模式**：适合简单的网络需求，基于 overlay 网络。
     - **Terway 模式**：推荐模式，基于阿里云 ENI（弹性网卡），与 VPC 深度集成，提供高性能网络。
  3. **ACK 集群网络规划**：
     - ACK 集群的 Pod 网络 CIDR：建议选择与 VPC CIDR 不重叠的范围（如 `172.16.0.0/16`）。
     - 节点分布：将 ACK 节点分布在 Private 子网的多个可用区（如 B、D、E、F），确保高可用性。
     - Service 网络：选择与 Pod 网络不重叠的 CIDR（如 `192.168.0.0/16`）。
     - 公网访问：通过 SLB（负载均衡）绑定 Public 子网的 EIP 实现外部访问。

- **学习任务**：
  - 在阿里云控制台查看 VPC 和子网配置，熟悉网络结构。
  - 学习 Terway 网络插件的配置方式，理解其与 VPC 的集成原理。


## 第四部分：VPC OpenVPN 部署

#### 理论背景
由于运维服务和后端服务部署在 VPC 的 Private 子网中，出于安全考虑，这些服务无法直接从外部访问。企业需要通过 OpenVPN 接入 VPC 网络，以安全地访问内部资源。因此，需要在 VPC 环境中部署 OpenVPN 服务。

#### 部署步骤
1. **获取 OpenVPN 安装脚本**
  - 项目地址：https://github.com/Nyr/openvpn-install/blob/master/openvpn-install.sh
  - 由于可能无法直接下载 GitHub 文件，需复制文件内容。
  - 登录到 OpenVPN ECS 主机，将内容保存为 `openvpn-install.sh` 文件，并赋予执行权限（例如：`chmod +x openvpn-install.sh`）。

2. **安装 OpenVPN**
   - 运行脚本 `./openvpn-install.sh`，按照提示完成安装。

3. **修改 OpenVPN 配置**
  - 编辑配置文件 `/etc/openvpn/server/server.conf`，修改为以下内容（需根据实际 VPC 网络地址调整）：
    ```
    ### 自动生成的 以上不要动
    local 10.133.0.191
    port 1194
    proto udp
    dev tun
    ca ca.crt
    cert server.crt
    key server.key
    dh dh.pem
    auth SHA512
    tls-crypt tc.key
    topology subnet

    # 推送 VPC 网络，需修改为自己的 VPC 网络范围
    server 10.8.0.0 255.255.255.0
    push "route 10.133.0.0 255.255.0.0"  # 只推送 VPC 网络，需修改为自己的 VPC 网络范围
    ifconfig-pool-persist ipp.txt
    # 结束位置，你们仔细找找

    # push "block-outside-dns"  这个注释掉，不然你们会上不了网
    keepalive 10 120
    user nobody
    group nogroup
    persist-key
    persist-tun
    verb 3
    crl-verify crl.pem
    explicit-exit-notify
    ```

4. **重启 OpenVPN 服务**
   - 执行命令：`systemctl restart openvpn-server@server.service`，确保配置生效。

5. **后续客户端管理**
   - 再次运行 `./openvpn-install.sh`，脚本会显示以下选项：
     ```
     OpenVPN is already installed.
     Select an option:
        1) Add a new client
        2) Revoke an existing client
        3) Remove OpenVPN
        4) Exit
     ```
   - 根据需要选择添加新客户端、撤销现有客户端等操作，并按照提示完成。

#### 注意事项
- 配置中的 `local` 地址（如 `10.133.0.191`）和推送的路由（如 `10.133.0.0 255.255.0.0`）需根据实际 VPC 网络环境调整。
- 确保 OpenVPN 服务器部署在可以被外部访问的子网（如 Public 子网），或通过 NAT 网关和 EIP 实现外部访问。


## 第五部分：企业级harbor仓库配置-阿里云SSL证书申请

### 数字证书管理服务简介
**阿里云数字证书管理服务（SSL Certificates Service）** 是阿里云提供的一种 SSL/TLS 证书管理解决方案，旨在帮助用户为其网站或服务启用 HTTPS 加密，保障数据传输的安全性。该服务支持用户购买、申请、托管和一键部署 SSL 证书，广泛应用于 Web 服务器、API 接口、容器服务（如 Harbor）等场景。

#### 核心功能与优势
1. **免费证书支持**：阿里云提供一定数量的免费 SSL 证书（通常为 DV 级别的域名验证证书），适合个人或小型企业用户快速启用 HTTPS。
2. **多种证书类型**：支持 DV（域名验证）、OV（组织验证）和 EV（扩展验证）证书，满足不同安全需求。
3. **一键部署**：证书可以一键部署到阿里云相关产品（如 SLB、CDN、WAF 等），简化配置流程。
4. **证书管理**：提供证书的申请、续期、下载和托管功能，方便用户集中管理。
5. **权威 CA 合作**：阿里云与全球知名证书颁发机构（CA）合作，如 DigiCert、GlobalSign、Symantec 等，确保证书的权威性和兼容性。
6. **免费额度**：阿里云为每个用户提供一定数量的免费证书（通常为 10 个或 20 个 DV 证书，具体以最新政策为准），非常适合初期测试或小型项目。

#### 适用场景
- 为 Web 应用、API 服务启用 HTTPS 加密。
- 为企业内部服务（如 Harbor 镜像仓库）提供权威认证的 SSL 证书，确保安全访问。
- 满足合规性要求，避免浏览器显示“不安全”警告。


### 申请 Harbor 免费 HTTPS 证书的流程
由于 Harbor 在企业环境中需要使用权威认证的 HTTPS 证书，阿里云数字证书管理服务可以免费提供证书（假设您的账户有免费额度）。以下是针对域名 `aliyun-harbor.labworlds.cc` 的证书申请流程，使用 CNAME 验证方式，并在 Cloudflare 中完成 DNS 验证。

#### 前提条件
1. 域名 `aliyun-harbor.labworlds.cc` 已解析到目标服务器（Harbor 所在服务器）。
2. 域名管理权限在 Cloudflare 上，可以添加 DNS 记录。
3. 阿里云账户已开通数字证书管理服务，并有免费证书额度（假设可免费申请 10 个证书）。

#### 申请流程
1. **登录阿里云控制台**
  - 访问阿里云官网（https://www.aliyun.com），登录您的阿里云账户。
  - 在顶部搜索栏输入“证书管理”或“SSL 证书”，进入“数字证书管理服务”页面。
  
![阿里云免费证书申请](/Kubernetes周边服务/enterprise/阿里云免费证书申请.png "阿里云免费证书申请")


2. **开通证书服务与免费证书服务**
   - 如果是首次使用，点击“开通服务”按钮，按照提示完成开通。
   - 在证书管理页面，点击“免费证书”或“申请证书”选项，查看是否有免费额度（通常阿里云会显示您可申请的免费证书数量，如 10 个）。
   - 确认有免费额度后，点击“申请免费证书”按钮。

3. **填写证书申请信息**
  - **证书类型**：选择“免费 DV SSL 证书”（域名验证型证书，适合 Harbor 场景）。
    ![创建证书信息](/Kubernetes周边服务/enterprise/创建证书信息.png "创建证书信息")
  - **域名信息**：
    - 输入域名：`aliyun-harbor.labworlds.cc`。
    - 如果支持多域名或泛域名，可根据需要添加（如 `*.labworlds.cc`，但免费证书可能不支持泛域名，具体以阿里云政策为准）。
    ![证书申请资料填写](/Kubernetes周边服务/enterprise/证书申请资料填写.png "证书申请资料填写")
  - **验证方式**：选择“CNAME 验证”（DNS 验证方式）。
  - 点击“下一步”或“提交申请”，系统会生成一个待验证的 CNAME 记录。
  ![证书验证提示](/Kubernetes周边服务/enterprise/证书验证提示.png "证书验证提示")

4. **获取 CNAME 验证记录**
  - 申请提交后，阿里云控制台会显示一个 CNAME 记录，格式通常如下：
    - **主机记录**：例如 `_acme-challenge.aliyun-harbor`（具体以控制台显示为准）。
    - **记录类型**：CNAME。
    - **记录值**：例如 `xxxxxxxxxxxx.verify.aliyun.com`（具体以控制台显示为准）。
  - 记录下这些信息，准备在 Cloudflare 中添加 DNS 记录。
  ![证书CNAME验证信息](/Kubernetes周边服务/enterprise/证书CNAME验证信息.png "证书CNAME验证信息")


5. **在 Cloudflare 中添加 CNAME 验证记录**
   - 登录 Cloudflare 账户，进入域名 `labworlds.cc` 的 DNS 管理页面。
   - 点击“添加记录”按钮，添加以下记录：
     - **类型**：选择 `CNAME`。
     - **名称**：输入阿里云提供的“主机记录”，例如 `_acme-challenge.aliyun-harbor`。
     - **目标**：输入阿里云提供的“记录值”，例如 `xxxxxxxxxxxx.verify.aliyun.com`。
     - **TTL**：选择默认值或设置为较短时间（如 120 秒），以便快速生效。
     - **代理状态**：选择“仅 DNS”（DNS Only），确保记录不被 Cloudflare 代理，验证才能通过。
   - 保存记录，等待 DNS 解析生效（通常需要几分钟，具体取决于 DNS 传播时间）。
  ![cloudflare-cname证书验证](/Kubernetes周边服务/enterprise/cloudflare-cname证书验证.png "cloudflare-cname证书验证")

6. **返回阿里云控制台完成验证**
   - 返回阿里云数字证书管理服务页面，点击“验证”或“检查验证状态”按钮。
   - 系统会自动检测 Cloudflare 中的 CNAME 记录是否正确配置。如果验证通过，状态会更新为“验证成功”；如果未通过，请检查 Cloudflare 中的记录是否正确或等待 DNS 传播完成。
   - 验证成功后，阿里云会向证书颁发机构（CA）提交申请，证书通常在几分钟到几小时内签发。

7. **下载证书**
  - 证书签发完成后，在阿里云控制台的“证书列表”中找到该证书，状态显示为“已签发”。
  - 点击“下载”按钮，下载证书文件（通常包含 PEM 格式的证书文件和私钥文件）。
  - 根据 Harbor 的配置要求，将证书文件和私钥文件上传到 Harbor 服务器，并在 Harbor 的配置文件中指定证书路径（例如 `/root/harbor/ssl/` 目录）。
  ![下载harbor证书](/Kubernetes周边服务/enterprise/下载harbor证书.png "下载harbor证书")


#### 注意事项
- **免费证书限制**：阿里云免费证书通常为 DV 级别，仅验证域名所有权，不包含组织信息，适合内部或测试环境。如果企业对证书有更高要求（如 OV/EV 证书），需购买付费证书。
- **DNS 解析时间**：Cloudflare 中的 DNS 记录可能需要几分钟到几小时生效，验证失败时请耐心等待或检查记录是否正确。
- **证书续期**：免费证书通常有效期为 3 月，到期前需手动续期或重新申请。阿里云控制台会提供续期提醒。
- **Cloudflare 代理**：验证期间确保 CNAME 记录为“仅 DNS”模式，否则阿里云无法直接访问记录导致验证失败。


### 第五部分：企业级 Harbor 仓库配置与域名配置

#### 目标
在 VPC 的 Private 子网中部署企业级 Harbor 镜像仓库，确保其安全性，并通过域名配置和 OpenVPN 实现内部网络访问。

#### 步骤说明
1. **创建 ECS 主机**
   - 在阿里云控制台中创建一台 ECS 实例，配置如下：
     - 规格：2 核 4G 内存（根据实际需求可调整）。
     - 网络：选择 VPC 的 **Private 子网**，确保主机无法直接从公网访问。
     - 安全组：选择或创建一个 **Private 安全组**，限制访问范围（例如仅允许 VPC 内部访问，或通过 OpenVPN 接入的客户端访问）。
     - 主机名称：命名为 `server-private-harbor`（可自定义）。
   - 创建完成后，记录 ECS 主机的内网 IP 地址（例如 `10.133.x.x`），后续配置域名解析时会用到。

2. **下载 Harbor 离线安装包**
   - 在本地电脑上访问 Harbor 官方发布页面：
     - 链接：https://github.com/goharbor/harbor/releases/download/v2.13.2/harbor-offline-installer-v2.13.2.tgz
   - 下载离线安装包 `harbor-offline-installer-v2.13.2.tgz` 到本地电脑。
   ![harbor下载](/Kubernetes周边服务/enterprise/harbor下载.png "harbor下载")

3. **使用 SFTP 上传安装包到 ECS 主机**
   - 使用 SFTP 工具（如 FileZilla、WinSCP 或命令行 `sftp`）连接到 ECS 主机。
     - 主机地址：ECS 内网 IP 或通过 OpenVPN 接入后的可达地址。
     - 用户名：默认通常为 `ecs-user`（根据实际系统用户调整）。
     - 密码/密钥：使用 ECS 登录凭据或 SSH 密钥。
   - 将下载的 `harbor-offline-installer-v2.13.2.tgz` 文件上传到 ECS 主机的 `/home/ecs-user/` 目录下。

4. **解压 Harbor 安装包**
   - 登录 ECS 主机（通过 SSH 或 OpenVPN 接入后 SSH）。
   - 执行以下命令解压安装包：
     ```bash
     tar -xvf /home/ecs-user/harbor-offline-installer-v2.13.2.tgz -C /home/ecs-user/
     ```
   - 解压后，`/home/ecs-user/` 目录下会出现 `harbor` 文件夹，包含 Harbor 的安装文件。

5. **复制并准备配置文件**
   - 进入 Harbor 目录：
     ```bash
     cd /home/ecs-user/harbor
     ```
   - 复制模板配置文件 `harbor.yml.tmpl` 为 `harbor.yml`：
     ```bash
     cp harbor.yml.tmpl harbor.yml
     ```

6. **修改 Harbor 配置文件**
   - 编辑 `harbor.yml` 文件（可以使用 `vim` 或 `nano` 编辑器，例如 `vim harbor.yml`）。
   - 根据您的证书路径和需求，修改以下配置内容：
     ```yaml
     # HTTPS 相关配置
     https:
       # Harbor 的 HTTPS 端口，默认是 443
       port: 443
       # Nginx 使用的证书和私钥文件路径
       certificate: /home/ecs-user/aliyun-harbor.labworlds.cc.pem
       private_key: /home/ecs-user/aliyun-harbor.labworlds.cc.key
       # 是否启用强 SSL 加密套件（默认：false）
       # strong_ssl_ciphers: false

     # Harbor 管理员密码
     harbor_admin_password: admin123
     ```
   - **注意**：
     - 请确保 `certificate` 和 `private_key` 路径正确，指向您从阿里云数字证书管理服务下载的证书文件（例如 `.pem` 和 `.key` 文件）。
     - 如果证书文件尚未上传，请通过 SFTP 将证书文件上传到指定路径（如 `/home/ecs-user/`）。
     - `harbor_admin_password` 可根据需要修改为更安全的密码。

7. **安装 Harbor 服务**
   - 在 `harbor` 目录下，执行安装脚本：
     ```bash
     ./install.sh
     ```
   - 脚本会自动安装 Docker（如果未安装）、Docker Compose，并启动 Harbor 服务。
   - 安装过程中，脚本会根据 `harbor.yml` 配置生成所需的容器和服务，安装完成后，Harbor 将以 HTTPS 方式运行在 443 端口。
   - 安装成功后，脚本会输出类似以下信息：
     ```
     ----Harbor has been installed and started successfully.----
     ```
   - 可以通过 `docker-compose ps` 查看 Harbor 相关容器是否正常运行。

8. **配置 Cloudflare 域名（仅限 VPC 内部访问）**
   - 获取 ECS 主机的内网 IP 地址（例如 `10.133.x.x`），可以在阿里云控制台查看，或在 ECS 主机上执行 `ifconfig` 或 `ip addr` 命令获取。
   - 登录 Cloudflare 账户，进入域名 `labworlds.cc` 的 DNS 管理页面。
   - 添加或更新 DNS 记录，将 `aliyun-harbor.labworlds.cc` 指向 ECS 内网 IP：
     - **类型**：选择 `A`（地址记录）。
     - **名称**：输入 `aliyun-harbor`（完整域名为 `aliyun-harbor.labworlds.cc`）。
     - **IPv4 地址**：输入 ECS 内网 IP，例如 `10.133.x.x`。
     - **TTL**：选择默认值或较短时间（如 120 秒）。
     - **代理状态**：选择“仅 DNS”（DNS Only），因为这是内网地址，Cloudflare 无法代理，且该域名仅在 VPC 网络内使用。
   - 保存记录，等待 DNS 解析生效（通常几分钟内生效）。

9. **访问 Harbor 仓库**
   - **访问方式**：由于 Harbor 部署在 Private 子网，域名 `aliyun-harbor.labworlds.cc` 只能在 VPC 网络内访问。如果您在 VPC 外部（如本地电脑），需通过 OpenVPN 接入 VPC 网络。
   - 接入 VPC 网络后，在浏览器中访问 `https://aliyun-harbor.labworlds.cc`，确认 Harbor 界面正常显示，且 HTTPS 证书有效（浏览器显示安全锁图标）。
   - 登录 Harbor，使用管理员账户：
     - 用户名：`admin`
     - 密码：`admin123`（或您在 `harbor.yml` 中设置的密码）
   - 登录后，可创建项目、上传镜像等操作。

#### 注意事项
- **网络限制**：Harbor 部署在 Private 子网，无法直接从公网访问，需通过 OpenVPN 接入 VPC 网络后才能访问 `aliyun-harbor.labworlds.cc`。
- **证书文件**：确保证书文件和私钥文件路径正确，且文件权限适当（例如 `chmod 600` 保护私钥文件）。
- **Harbor 版本**：本文使用的是 `v2.13.2`，如需其他版本，请从 Harbor 官方 GitHub 页面下载对应版本的离线安装包。
- **系统依赖**：Harbor 安装需要 Docker 和 Docker Compose，如果 ECS 主机未预装，`install.sh` 脚本会尝试自动安装；如遇问题，请手动安装后再运行脚本。
- **域名解析**：Cloudflare 中的 DNS 记录指向内网 IP，仅在 VPC 内部有效；如果 OpenVPN 未配置正确，可能无法解析或访问域名。



## 阿里云 ACK 集群创建与子账户授权及 kubectl config 本地配置

### 目标
在阿里云上创建企业级 ACK 集群，配置 Private 子网和安全组，授权子账户管理员权限，并完成本地 `kubectl` 工具的配置以管理集群。

### 步骤说明
1. **创建 ACK 集群**
  - 登录阿里云控制台（https://www.aliyun.com），进入“容器服务 Kubernetes 版（ACK）”页面。
    ![ack主页](/Kubernetes周边服务/enterprise/ack主页.png "ack主页")
  - 点击“创建集群”，命名集群为 `ack-labworlds-prod`，命名规则为 `ack-企业名-环境`（例如 `ack-labworlds-prod` 表示生产环境）。
    ![ack创建一](/Kubernetes周边服务/enterprise/ack创建一.png "ack创建一")

2. **选择集群类型及基本配置**
  - **集群类型**：选择“托管版 ACK 集群”（基础版），由阿里云托管控制平面，降低维护成本。
  - **地域**：选择“杭州”（或根据实际需求选择其他地域）。
  - **版本**：选择列表中的第一个 Kubernetes 版本（通常为最新稳定版本），方便后期进行集群升级。
  - **自动升级**：关闭自动升级选项，手动控制升级时间以确保稳定性。
  ![ack创建二](/Kubernetes周边服务/enterprise/ack创建二.png "ack创建二")  

3. **网络配置（VPC 和子网）**
  - **VPC**：选择您已创建的自定义 VPC（不要使用默认 VPC）。
  - **子网**：勾选所有 **Private 子网**（确保所有节点和 Pod 都在私有网络中运行）。
  - **NAT 网关**：由于您已配置 NAT 网关，不要勾选“配置 SNAT”（避免重复配置公网访问）。
  - 确保网络配置符合企业安全要求，节点和 Pod 均不可直接暴露在公网。
  ![ack创建三](/Kubernetes周边服务/enterprise/ack创建三.png "ack创建三")  

4. **安全组配置**
  - **安全组**：仅选择 **Private 安全组**，禁止选择 Public 安全组。
  - 确保安全组规则限制访问范围，例如只允许 VPC 内部或通过 OpenVPN 接入的客户端访问集群相关端口（如 API Server 端口 6443）。
  

5. **网络插件选择**
  - **网络插件**：选择阿里云提供的 **Terway** 网络插件，支持 VPC 与 Pod 直接通信，并启用 **IPVS 模式**，提升网络性能和负载均衡能力。
  - Terway 插件会为每个 Pod 分配 VPC 内的 IP 地址，方便与 VPC 内其他服务（如 Harbor）通信。
  

6. **创建节点池**
  - **节点类型**：选择“抢占式实例”（Spot Instance），价格更低，适合非关键性负载。
  - **节点规格**：选择 4 核 8G 内存，系统盘存储 40G（可根据需求调整）。
  - **节点数量**：设置为 2 台（初期测试或小型集群足够，后期可扩展）。
  - **密钥对**：选择您已创建的 SSH 密钥对，用于登录节点进行排查或管理。
  - 确认节点池配置，确保节点分布在 Private 子网中。
  ![ack创建四](/Kubernetes周边服务/enterprise/ack创建四.png "ack创建四") 
  ![ack创建五](/Kubernetes周边服务/enterprise/ack创建五.png "ack创建五")  
  ![ack创建六](/Kubernetes周边服务/enterprise/ack创建六.png "ack创建六")  


7. **安装附加组件**
  - 勾选以下组件以增强集群功能：
    - **监控组件**：如 Prometheus、阿里云监控（ARMS），用于集群和应用监控。
    - **Nginx Ingress Controller**：用于处理外部流量入口，方便后续部署服务。
  - 其他组件根据需求选择（如日志组件 Logtail 等）。
  ![ack创建七](/Kubernetes周边服务/enterprise/ack创建七.png "ack创建七")  

8. **提交创建集群**
  - 检查所有配置无误后，点击“创建集群”按钮。
  - 创建过程通常需要 10-20 分钟，期间控制台会显示进度。创建完成后，集群状态会变为“运行中”。

9. **子账户权限授权（安全管理）**
  - 进入集群信息页面，点击左侧菜单中的“安全管理”或“访问控制”。
  - 在“角色授权”或“用户管理”选项中，找到子账户授权功能。
  - 将需要管理集群的子账户添加到授权列表中，并分配“管理员”角色（Administrator），确保子账户拥有完全控制权限。
  - 保存配置，子账户即可通过控制台或 `kubectl` 管理集群。
  - **注意**：建议遵循最小权限原则，仅为必要人员分配管理员权限，避免安全风险。
  ![ack登录权限](/Kubernetes周边服务/enterprise/ack登录权限.png "ack登录权限")
  ![ack登录config获取](/Kubernetes周边服务/enterprise/ack登录config获取.png "ack登录config获取")  




10. **获取并配置 kubectl config 文件（本地配置）**
  - 在集群信息页面，点击“连接信息”或“集群连接”选项。
  - 找到 `kubectl` 连接配置部分，点击“复制”或“下载”按钮，获取 `kubeconfig` 文件内容。
  - 在本地电脑上（Windows 或 macOS），将该配置内容保存到以下路径：
    - **Windows**：`C:\Users\您的用户名\.kube\config`
    - **macOS/Linux**：`/home/您的用户名/.kube/config`
  - 确保文件名为 `config`，且目录 `.kube` 已存在（如果没有，需手动创建）。
  - **权限设置**（macOS/Linux）：执行以下命令保护配置文件：
    ```bash
    chmod 600 ~/.kube/config
    ```
  - **验证连接**：安装 `kubectl` 工具（如果未安装，可从 Kubernetes 官网下载或通过包管理器安装），然后执行以下命令检查是否能连接到集群：
    ```bash
    kubectl get nodes
    ```
  - 如果输出显示集群节点信息（如 2 个节点的状态为 `Ready`），则配置成功。

### 注意事项
- **网络安全**：集群节点和 Pod 均在 Private 子网中，无法直接从公网访问。如需本地管理集群，需通过 OpenVPN 接入 VPC 网络。
- **抢占式实例风险**：抢占式实例可能因资源不足被回收，建议后期关键负载切换为按量付费或包年包月实例。
- **Terway 网络插件**：Terway 绑定 VPC IP 地址，Pod IP 会占用 VPC 子网 IP 资源，确保子网 IP 范围足够大。
- **kubectl 工具**：确保本地安装的 `kubectl` 版本与集群版本兼容（通常选择与集群版本相同或略高的版本）。
- **子账户权限**：管理员权限包含集群所有操作权限，谨慎分配；如需限制权限，可自定义角色绑定。
- **集群升级**：关闭自动升级后，需定期手动检查 Kubernetes 版本更新，确保集群安全性和兼容性。



## Kubernetes 可视化界面 Kuboard 安装

### 目标
在阿里云 VPC 的 Private 子网中创建一台主机，部署 Kuboard 可视化管理工具，并通过 Agent 方式连接并管理 ACK 集群。

### 步骤说明
1. **创建 ECS 主机**
   - 登录阿里云控制台（https://www.aliyun.com），进入“云服务器 ECS”页面。
   - 点击“创建实例”，配置如下：
     - **规格**：选择 1 核 2G 内存（适合轻量级应用，如 Kuboard）。
     - **网络**：选择您已创建的 VPC，并分配到 **Private 子网**，确保主机无法直接从公网访问。
     - **安全组**：选择或创建一个 **Private 安全组**，限制访问范围（例如仅允许 VPC 内部或通过 OpenVPN 接入的客户端访问）。
     - **地域**：选择与 ACK 集群相同的地域（如杭州），以减少网络延迟。
     - **操作系统**：选择常见的 Linux 发行版（如 CentOS、Ubuntu），确保支持 Docker。
     - **其他配置**：按需选择磁盘大小（默认系统盘即可），并绑定 SSH 密钥或设置密码用于登录。
   - 创建完成后，记录 ECS 主机的内网 IP 地址（例如 `10.133.7.85`），后续配置 Kuboard 时会用到。
   - **访问方式**：确保可以通过 OpenVPN 接入 VPC 网络，并通过 SSH 登录到该主机。

2. **部署 Kuboard 容器**
   - 在 ECS 主机上执行以下命令，启动 Kuboard 容器：
     ```bash
     sudo docker run -d \
         --restart=unless-stopped \
         --name=kuboard \
         -p 80:80/tcp \
         -p 10081:10081/tcp \
         -e KUBOARD_ENDPOINT="http://10.133.7.85:80" \
         -e KUBOARD_AGENT_SERVER_TCP_PORT="10081" \
         -v /root/kuboard-data:/data \
         swr.cn-east-2.myhuaweicloud.com/kuboard/kuboard:v3
     ```
   - **参数说明**：
     - `-p 80:80/tcp` 和 `-p 10081:10081/tcp`：映射 Kuboard 的 Web 界面端口（80）和 Agent 通信端口（10081）。
     - `-e KUBOARD_ENDPOINT="http://10.133.7.85:80"`：设置 Kuboard 的访问端点，替换 `10.133.7.85` 为您 ECS 主机的实际内网 IP 地址。
     - `-e KUBOARD_AGENT_SERVER_TCP_PORT="10081"`：设置 Agent 通信端口，保持默认 10081。
     - `-v /root/kuboard-data:/data`：将数据持久化存储到主机目录 `/root/kuboard-data`。
     - `swr.cn-east-2.myhuaweicloud.com/kuboard/kuboard:v3`：Kuboard 镜像地址，使用 v3 版本。
   - 执行完成后，通过以下命令检查容器是否正常运行：
     ```bash
     docker ps
     ```
   - 如果容器状态为 `Up`，则 Kuboard 部署成功。

3. **访问 Kuboard Web 界面**
   - 确保已通过 OpenVPN 接入 VPC 网络（因为 Kuboard 部署在 Private 子网，无法直接从公网访问）。
   - 在浏览器中输入 `http://10.133.7.85:80`（替换为您的 ECS 内网 IP），访问 Kuboard 的 Web 界面。
   - 首次访问时，Kuboard 会提示设置管理员账户和密码，按照页面指引完成初始化。
   - 登录后，您将看到 Kuboard 的管理界面。

4. **为 Kubernetes 集群安装 Kuboard Agent**
   - 在 Kuboard Web 界面中，选择“添加集群”或“连接集群”选项。
   - 选择 **Agent 方式** 连接 Kubernetes 集群（适合 ACK 集群）。
   - Kuboard 会生成一组命令或 YAML 文件，用于在目标 Kubernetes 集群中部署 Agent。
   - 在本地电脑上，确保已配置好 `kubectl` 工具并能连接到 ACK 集群（参考之前步骤）。
   - 执行 Kuboard 提供的命令或应用 YAML 文件，例如：
     ```bash
     kubectl apply -f <kuboard-agent.yaml>
     ```
   - 或者直接复制 Kuboard 提供的 `kubectl` 命令并执行。
   - 部署完成后，Kuboard Agent 会与 Kuboard 服务建立连接，集群将出现在 Kuboard 界面中。
   - 在 Kuboard 中选择该集群，即可进行可视化管理（如查看节点、Pod、部署应用等）。

### 注意事项
- **网络限制**：Kuboard 部署在 Private 子网，无法直接从公网访问，需通过 OpenVPN 接入 VPC 网络后才能访问 Web 界面。
- **端口开放**：确保 ECS 主机安全组允许 VPC 内部访问 80 和 10081 端口，以便 Kuboard Web 界面和 Agent 通信正常。
- **内网 IP**：`KUBOARD_ENDPOINT` 参数中的 IP 必须是 ECS 主机的内网 IP，且在 VPC 网络内可达。
- **数据持久化**：Kuboard 数据存储在 `/root/kuboard-data` 目录，建议定期备份该目录以防数据丢失。
- **Agent 部署**：确保 ACK 集群的 API Server 可被 Kuboard Agent 访问（通常在 VPC 内部无问题），如有连接问题，检查安全组规则或网络配置。
- **Kuboard 版本**：本文使用的是 `v3` 版本，如需更新版本，请参考 Kuboard 官方文档或镜像仓库。



## 所有项目的镜像准备指南

### 1. 在 Harbor 页面创建项目
请在 Harbor 镜像仓库页面中创建以下项目，用于存储和管理Docker镜像：
- **admin3-ui**
- **admin3-server**
- **go-starter**
- **light-year-admin-template**
- **stars-emmision**

**操作步骤**：登录 Harbor 管理界面，进入“项目”选项卡，点击“新建项目”，依次输入上述项目名称并保存。


### 2. 创建打包镜像专用环境
为了确保每个队员独立完成自己的镜像打包任务，需要为每位队员配置独立的资源环境：
- **配置规格**：2核 CPU，4GB 内存，40GB 存储空间。
- **注意事项**：每位队员必须使用自己的环境打包镜像，禁止使用他人的环境或镜像。

### 3. 项目镜像构建与推送步骤
以下是针对各个项目的具体操作步骤，包括代码拉取、配置修改、镜像构建和推送。请按照以下步骤逐一完成。

### 3.1 admin3-ui 和 admin3-server
#### 代码拉取
```bash
git clone https://gitee.com/Tender-Liu/admin3.git
cd admin3/admin3-ui
```

#### 修改配置
- 打开 `.env` 文件，将 `VITE_BASE_URI` 的值修改为：
  ```
  VITE_BASE_URI=https://shiqi.admin.labworlds.cc/admin3
  ```
- **注意**：请将域名中的 `shiqi` 替换为您自己的域名，确保与您的环境一致。

#### 构建与推送镜像 (admin3-ui)
```bash
docker build -t aliyun-harbor.labworlds.cc/admin3-ui/master:shiqi-082020 .
docker push aliyun-harbor.labworlds.cc/admin3-ui/master:shiqi-082020
```
- **注意**：如果 `push` 失败，请检查是否已执行 `docker login` 登录到镜像仓库。如果未登录，请先登录后再重试。

#### 构建与推送镜像 (admin3-server)
```bash
cd ../admin3-server
docker build -t aliyun-harbor.labworlds.cc/admin3-server/master:shiqi-082020 .
docker push aliyun-harbor.labworlds.cc/admin3-server/master:shiqi-082020
```

### 3.2 Light-Year-Admin-Template
#### 代码拉取
```bash
git clone https://gitee.com/Tender-Liu/Light-Year-Admin-Template.git
cd Light-Year-Admin-Template
```

#### 构建与推送镜像
```bash
docker build -t aliyun-harbor.labworlds.cc/light-year-admin-template/master:shiqi-082020 .
docker push aliyun-harbor.labworlds.cc/light-year-admin-template/master:shiqi-082020
```

### 3.3 go-starter
#### 代码拉取
```bash
git clone https://gitee.com/Tender-Liu/go-starter.git
cd go-starter
```

#### 构建与推送镜像
```bash
docker build -t aliyun-harbor.labworlds.cc/go-starter/master:shiqi-082020 .
docker push aliyun-harbor.labworlds.cc/go-starter/master:shiqi-082020
```

### 3.4 stars-emmision
#### 代码拉取
```bash
git clone https://gitee.com/Tender-Liu/stars-emmision.git
cd stars-emmision
```

#### 构建与推送镜像
```bash
docker build -t aliyun-harbor.labworlds.cc/stars-emmision/master:shiqi-082020 .
docker push aliyun-harbor.labworlds.cc/stars-emmision/master:shiqi-082020
```

## 注意事项
1. **镜像标签个性化**：上述命令中镜像标签的 `shiqi-082020` 部分，请替换为您自己的标识（如您的名字或日期），以区分不同队员的镜像。
2. **Docker 登录**：在执行 `docker push` 前，请确保已使用 `docker login` 登录到 `aliyun-harbor.labworlds.cc` 镜像仓库。如果推送失败，请检查登录状态。
3. **独立操作**：每位队员需独立完成自己项目的镜像构建和推送，禁止使用他人资源或镜像。



## 练习教案：Kubernetes 部署 light-year-admin-template 项目

### 目标
通过本练习，学习如何在 Kubernetes 集群（如阿里云 ACK）中部署一个前端项目 `light-year-admin-template`，包括创建必要的 Kubernetes 资源（如 Deployment、HPA、Service、Ingress），并实现高可用性、自动扩展和域名访问。

### 前提条件
1. 已创建并配置好 Kubernetes 集群（如阿里云 ACK），并通过 `kubectl` 工具可以正常访问集群。
2. 已配置镜像仓库（如 Harbor）的登录凭据，并创建对应的 `imagePullSecrets`（名称为 `secret-harbor-login`）。
3. 已安装 Nginx Ingress Controller，用于处理外部流量入口。
4. 已通过 Cloudflare 或其他 DNS 服务配置好域名（如 `shiqi.light.labworlds.cc`），并指向 Ingress 控制器的外部 IP。
5. 已创建 TLS 证书，并存储为 Kubernetes Secret（名称为 `secret-shiqi-light-labworlds-cc`）。
6. 本地已安装 `kubectl` 工具，并配置好 `kubeconfig` 文件。

### 练习环境
- **Kubernetes 集群**：阿里云 ACK 集群（或其他符合要求的 Kubernetes 集群）。
- **命名空间**：`shiqi`（如未创建，需提前创建）。
- **项目名称**：`light-year-admin-template`。
- **镜像地址**：`aliyun-harbor.labworlds.cc/light-year-admin-template/master:shiqi-082020`。

### 步骤 1：创建项目文件夹结构
1. 在本地电脑上创建一个项目文件夹，命名为 `light-year-admin-template`，用于存放 Kubernetes 配置文件。
2. 在该文件夹中创建以下 4 个 YAML 文件，用于定义不同的 Kubernetes 资源：
   - `deployment.yml`：定义 Deployment 资源，用于管理 Pod 副本和反亲和性。
   - `hpa.yml`：定义 HorizontalPodAutoscaler 资源，用于自动扩展 Pod 数量。
   - `service.yml`：定义 Service 资源，用于集群内部访问 Pod。
   - `nginx-ingress.yml`：定义 Ingress 资源，用于通过域名访问服务。
3. 文件夹结构如下：
   ```
   light-year-admin-template/
   ├── deployment.yml
   ├── hpa.yml
   ├── service.yml
   └── nginx-ingress.yml
   ```

### 步骤 2：编写 Kubernetes 配置文件
以下是每个 YAML 文件的详细内容，请复制并保存到对应的文件中。每个文件都包含了注释，以便理解每个配置项的作用。

#### 2.1 `deployment.yml` 文件
该文件定义了 `light-year-admin-template` 项目的 Deployment 资源，包含 Pod 反亲和性策略、资源限制、探针配置等。
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-light-year-admin-template
  namespace: shiqi
spec:
  replicas: 2  # 指定 Pod 副本数，实现高可用性
  selector:    # 选择器，用于关联 Deployment 和 Pod
    matchLabels:
      app: pod-light-year-admin-template
  strategy:    # 定义更新策略
    type: RollingUpdate  # 设置为滚动更新，确保更新时服务不中断
    rollingUpdate:
      maxSurge: 1        # 最多允许 1 个额外 Pod
      maxUnavailable: 0  # 不允许有不可用 Pod，确保服务始终可用
  template:            # Pod 模板，包含 Pod 的完整定义
    metadata:
      labels:          # Pod 标签，必须与 selector.matchLabels 一致
        app: pod-light-year-admin-template
    spec:              # Pod 规格定义
      affinity:
        podAntiAffinity:  # 反亲和性，尽量分散部署以提高可用性
          preferredDuringSchedulingIgnoredDuringExecution:  # 软策略，调度时尽量满足
          - weight: 100  # 高权重，优先考虑分散
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app: pod-light-year-admin-template
              topologyKey: "kubernetes.io/hostname"  # 尽量部署在不同主机上
      containers:  # 容器配置列表
      - name: light-year-admin-template  # 容器名称
        image: aliyun-harbor.labworlds.cc/light-year-admin-template/master:shiqi-082020  # 容器镜像地址
        ports:  # 容器暴露的端口
        - containerPort: 80  # 容器内部端口
          name: http         # 端口名称
        resources:  # 资源限制和请求
          requests:  # 资源请求（最低需求）
            cpu: "100m"    # 请求 100 毫核 CPU
            memory: "64Mi" # 请求 64MB 内存
          limits:  # 资源限制（最大使用）
            cpu: "200m"    # 限制 200 毫核 CPU
            memory: "128Mi" # 限制 128MB 内存
        livenessProbe:  # 存活探针，检测容器是否存活
          httpGet:      # 使用 HTTP GET 请求检测
            path: /     # 检测路径
            port: 80    # 检测端口
          initialDelaySeconds: 15  # 首次检测延迟 15 秒
          periodSeconds: 10        # 每 10 秒检测一次
        readinessProbe:  # 就绪探针，检测容器是否准备好提供服务
          httpGet:       # 使用 HTTP GET 请求检测
            path: /      # 检测路径
            port: 80     # 检测端口
          initialDelaySeconds: 5  # 首次检测延迟 5 秒
          periodSeconds: 5        # 每 5 秒检测一次
      imagePullSecrets:  # 镜像拉取凭据
      - name: secret-harbor-login  # 镜像仓库登录密钥名称
```

#### 2.2 `hpa.yml` 文件
该文件定义了 HorizontalPodAutoscaler（HPA）资源，用于根据 CPU 使用率自动调整 Pod 副本数。
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: hpa-light-year-admin-template
  namespace: shiqi
spec:
  scaleTargetRef:  # 指定要扩展的目标资源
    apiVersion: apps/v1
    kind: Deployment
    name: deployment-light-year-admin-template  # 关联的 Deployment 名称
  minReplicas: 2  # 最小副本数，至少 2 个
  maxReplicas: 3  # 最大副本数，根据企业需求设置
  metrics:        # 定义扩展指标
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70  # 目标 CPU 使用率 70%，超过时增加副本
```

#### 2.3 `service.yml` 文件
该文件定义了 Service 资源，用于在集群内部访问 `light-year-admin-template` 的 Pod。
```yaml
apiVersion: v1
kind: Service
metadata:
  name: service-light-year-admin-template
  namespace: shiqi
spec:
  selector:  # 关联具有特定标签的 Pod
    app: pod-light-year-admin-template
  ports:
  - protocol: TCP
    port: 80        # Service 端口
    targetPort: 80  # 后端 Pod 容器端口
  type: ClusterIP   # 默认类型，集群内部访问
```

#### 2.4 `nginx-ingress.yml` 文件
该文件定义了 Ingress 资源，用于通过域名访问服务，并启用 TLS 加密。
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-light-year-admin-template
  namespace: shiqi
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /  # 可选：URL 重写规则
spec:
  ingressClassName: nginx  # 指定 Ingress 控制器类型为 Nginx
  rules:
  - host: shiqi.light.labworlds.cc  # 基于域名路由
    http:
      paths:
      - path: /  # 基于路径路由
        pathType: Prefix
        backend:
          service:
            name: service-light-year-admin-template  # 关联的 Service 名称
            port:
              number: 80
  tls:  # 配置 TLS 加密
  - hosts:
    - shiqi.light.labworlds.cc
    secretName: secret-shiqi-light-labworlds-cc  # 存储 TLS 证书的 Secret 名称
```

### 步骤 3：创建命名空间
在 Kubernetes 集群中创建用于部署项目的命名空间 `shiqi`（如果尚未创建）。
1. 执行以下命令创建命名空间：
   ```bash
   kubectl create namespace shiqi
   ```
2. 验证命名空间是否创建成功：
   ```bash
   kubectl get namespace
   ```
   确保 `shiqi` 出现在列表中。

### 步骤 4：部署项目资源
将之前创建的 YAML 文件应用到 Kubernetes 集群中，按顺序部署资源。
1. 进入项目文件夹：
   ```bash
   cd light-year-admin-template
   ```
2. 按以下顺序应用配置文件（建议按资源依赖顺序部署）：
   - 先部署 Deployment：
     ```bash
     kubectl apply -f deployment.yml
     ```
   - 再部署 Service：
     ```bash
     kubectl apply -f service.yml
     ```
   - 然后部署 HPA：
     ```bash
     kubectl apply -f hpa.yml
     ```
   - 最后部署 Ingress：
     ```bash
     kubectl apply -f nginx-ingress.yml
     ```
3. 验证资源是否创建成功：
   - 检查 Deployment 和 Pod 状态：
     ```bash
     kubectl get deployment -n shiqi
     kubectl get pod -n shiqi
     ```
     确保 `deployment-light-year-admin-template` 显示副本数为 2，且 Pod 状态为 `Running`。
   - 检查 Service：
     ```bash
     kubectl get service -n shiqi
     ```
     确保 `service-light-year-admin-template` 已创建。
   - 检查 HPA：
     ```bash
     kubectl get hpa -n shiqi
     ```
     确保 `hpa-light-year-admin-template` 已创建，并显示目标 CPU 使用率。
   - 检查 Ingress：
     ```bash
     kubectl get ingress -n shiqi
     ```
     确保 `ingress-light-year-admin-template` 已创建，并显示域名信息。

### 步骤 5：验证服务访问
1. 确保域名 `shiqi.light.labworlds.cc` 已通过 Cloudflare 或其他 DNS 服务解析到 Ingress 控制器的外部 IP 地址。
   - 如果不确定 Ingress 控制器的 IP，可以通过以下命令查看：
     ```bash
     kubectl get ingress -n shiqi -o wide
     ```
     或查看 Nginx Ingress Controller 的 Service 外部 IP：
     ```bash
     kubectl get service -n ingress-nginx  # 假设 Nginx Ingress 部署在 ingress-nginx 命名空间
     ```
2. 在浏览器中访问 `https://shiqi.light.labworlds.cc`，验证是否能正常加载 `light-year-admin-template` 项目页面。
   - 如果页面无法加载，可能原因包括：
     - DNS 解析未生效：等待 DNS 生效或检查解析记录。
     - TLS 证书问题：确保 `secret-shiqi-light-labworlds-cc` 中存储的证书有效。
     - Ingress 控制器问题：检查 Nginx Ingress Controller 是否正常运行。
     - Pod 未就绪：检查 Pod 日志，排查容器启动问题。

### 步骤 6：测试自动扩展（HPA）
1. 模拟高负载以触发 HPA 自动扩展（可选，需额外工具或手动增加负载）。
   - 可以使用工具（如 `ab` 或 `wrk`）对服务发起大量请求，增加 CPU 使用率。
   - 或者手动调整 HPA 的 `averageUtilization` 为较低值（如 10%），以便更容易触发扩展：
     ```bash
     kubectl edit hpa hpa-light-year-admin-template -n shiqi
     ```
2. 检查 HPA 是否增加 Pod 副本数：
   ```bash
   kubectl get hpa -n shiqi -w  # 实时监控 HPA 状态
   kubectl get pod -n shiqi -w   # 实时监控 Pod 数量
   ```
   当 CPU 使用率超过目标值（70%）时，Pod 数量应增加（最多到 3 个）。

### 注意事项
- **镜像拉取问题**：确保 `secret-harbor-login` 正确配置，且镜像地址 `aliyun-harbor.labworlds.cc/light-year-admin-template/master:shiqi-082020` 可访问。如果拉取失败，检查 Secret 或镜像是否存在。
- **反亲和性策略**：`podAntiAffinity` 配置为软策略（`preferredDuringSchedulingIgnoredDuringExecution`），如果集群节点不足，Pod 可能仍会部署在同一节点上。
- **HPA 依赖 Metrics Server**：确保集群中已安装 Metrics Server（用于收集 CPU 使用率数据），否则 HPA 无法工作。阿里云 ACK 通常默认安装，若未安装需手动部署。
- **域名和 TLS**：Ingress 配置依赖域名和 TLS 证书，确保 `shiqi.light.labworlds.cc` 和 `secret-shiqi-light-labworlds-cc` 已正确设置。
- **资源限制**：根据实际需求调整 CPU 和内存的 `requests` 和 `limits`，避免资源不足或浪费。
- **日志排查**：如果资源创建或服务访问失败，使用以下命令查看详细信息：
  - 查看 Pod 日志：
    ```bash
    kubectl logs -l app=pod-light-year-admin-template -n shiqi
    ```
  - 查看资源事件：
    ```bash
    kubectl describe pod -l app=pod-light-year-admin-template -n shiqi
    ```

### 练习总结
通过本练习，您学习了如何在 Kubernetes 集群中部署一个完整的前端项目 `light-year-admin-template`，并实现了以下功能：
1. 使用 Deployment 管理 Pod，确保高可用性和滚动更新。
2. 配置 Pod 反亲和性策略，尽量将 Pod 分布在不同节点上。
3. 使用 HPA 实现基于 CPU 使用率的自动扩展。
4. 通过 Service 提供集群内部访问。
5. 使用 Nginx Ingress 配置域名访问和 TLS 加密。


## 额外: cert-manager 和 Helm 的介绍

**cert-manager** 是一个 Kubernetes 上的开源工具，用于自动化管理 TLS 证书。它可以与多种证书颁发机构（CA）集成，比如 Let's Encrypt、HashiCorp Vault 等，通过自定义资源（如 `Certificate` 和 `Issuer`）来自动签发、续期和管理证书。cert-manager 简化了在 Kubernetes 集群中实现 HTTPS 加密的过程，特别适用于 Ingress 资源配置 TLS。

**Helm** 是 Kubernetes 的包管理工具，类似于 Linux 中的 apt 或 yum。它允许用户通过预定义的模板（称为 Chart）来快速部署和管理 Kubernetes 应用程序。Helm 通过 Chart 将复杂的 Kubernetes 资源配置打包，用户只需简单命令即可完成安装、升级或删除操作，极大地提高了部署效率。

### 2. 在阿里云 ACK 集群中安装 cert-manager 使用 Helm

在阿里云 ACK（容器服务 Kubernetes）集群中，可以通过 Helm 快速安装 cert-manager。步骤如下：

- 登录阿里云控制台，进入容器服务 ACK 集群的管理页面。
- 在左侧导航栏选择 **应用目录** 或 **Helm Chart**。
- 在搜索框中输入 `cert-manager`，找到对应的 Chart。
- 点击 **安装**，根据提示完成配置（如命名空间选择，通常建议使用 `cert-manager` 命名空间）。
- 安装完成后，确认 cert-manager 的 Pod 运行正常。

![cert-manager安装](/Kubernetes周边服务/enterprise/cert-manager安装.png "cert-manager安装")

如果您需要通过命令行操作，可以使用 Helm CLI：  (我们有可视化不用这个了)
```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --set installCRDs=true
```

**注意**：`installCRDs=true` 是必要的，因为 cert-manager 需要安装自定义资源定义（CRD）。

### 3. 修改 nginx-ingress.yml 并添加 cert-manager 相关配置

为了让 Ingress 资源自动使用 cert-manager 签发的证书，您需要在 Ingress 文件中添加 cert-manager 的注解，同时确保已经配置了对应的 `Issuer` 或 `ClusterIssuer`。以下是修改后的 `nginx-ingress.yml` 示例：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-light-year-admin-template
  namespace: shiqi
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /  # 可选：URL 重写规则
    cert-manager.io/cluster-issuer: "letsencrypt-prod"  # 指定 cert-manager 的 ClusterIssuer 名称
spec:
  ingressClassName: nginx  # 指定 Ingress 控制器类型为 Nginx
  rules:
  - host: shiqi.light.labworlds.cc  # 基于域名路由
    http:
      paths:
      - path: /  # 基于路径路由
        pathType: Prefix
        backend:
          service:
            name: service-light-year-admin-template  # 关联的 Service 名称
            port:
              number: 80
  tls:  # 配置 TLS 加密
  - hosts:
    - shiqi.light.labworlds.cc
    secretName: secret-shiqi-light-labworlds-cc  # 存储 TLS 证书的 Secret 名称，由 cert-manager 自动生成
```

**说明**：
- `cert-manager.io/cluster-issuer: "letsencrypt-prod"` 是关键注解，用于指定 cert-manager 使用哪个 `ClusterIssuer` 来签发证书。您需要提前创建并配置好 `ClusterIssuer`，例如使用 Let's Encrypt 作为证书颁发机构。
- `secretName` 是证书存储的 Secret 名称，cert-manager 会自动创建并管理这个 Secret，无需手动创建。

### 创建 ClusterIssuer 示例

如果您还没有创建 `ClusterIssuer`，可以参考以下配置（以 Let's Encrypt 为例）：

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: user@example.com  # 替换为您的邮箱，用于接收证书过期提醒
    privateKeySecretRef:
      name: letsencrypt-prod-key
    solvers:
    - http01:
        ingress:
          class: nginx
```

**说明**：
- `server` 指定 Let's Encrypt 的 ACME 服务器地址。
- `email` 用于接收证书相关通知。
- `solvers` 定义了域名所有权验证方式，这里使用 HTTP-01 挑战方式，适用于 Nginx Ingress。
