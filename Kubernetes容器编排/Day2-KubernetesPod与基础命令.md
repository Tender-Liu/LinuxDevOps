# 第1天：Pod 与配置管理（ConfigMap 和 Secret）

## 目标
- 掌握 Pod 的基本操作，包括创建、生命周期管理、资源限制和健康检查。
- 理解并实践 Namespace 的使用，学习资源隔离。
- 掌握 ConfigMap 和 Secret 的使用，学习如何管理配置和敏感数据。
- 结合命令行（`kubectl`）和 Kuboard 界面操作，帮助学员直观理解 Kubernetes 管理。
- 通过理论和实践结合，为后续部署案例打下基础。


## 第一部分：Namespace 与 Kubernetes 基础与 Pod 定位

### 什么是 Kubernetes？——从零开始理解容器编排

#### 为什么需要 Kubernetes？

想象一下，你是一个餐厅的经理，手下有很多厨师（就像服务器上的应用程序），每个厨师都在忙着做不同的菜（运行不同的容器）。如果没有一个好的管理系统，厨师们可能会互相抢占厨房资源（CPU、内存），有的菜做不出来（应用崩溃），有的菜做多了浪费（资源闲置）。这时候，你需要一个“超级调度员”来协调一切：谁用哪个炉灶、谁先做哪道菜、怎么保证厨房高效运转。这个“超级调度员”就是 Kubernetes。

Kubernetes（简称 K8s）是一个开源的容器编排平台，它就像餐厅里的经理，专门管理成百上千个容器（应用程序的最小运行单位），确保它们在服务器集群中高效、安全地运行。它的主要任务包括：
- **自动部署**：帮你快速把应用放到服务器上，不用手动操作。
- **资源调度**：合理分配服务器资源（CPU、内存、存储），避免浪费或冲突。
- **自动扩展**：当用户访问量增加时，自动增加应用副本；访问量减少时，自动减少副本。
- **故障恢复**：如果某个应用挂了，Kubernetes 会自动重启或替换它，保证服务不中断。

#### Kubernetes 的核心组件——认识“大家庭”

Kubernetes 是一个大系统，里面有很多“家庭成员”各司其职。以下是几个核心组件，理解它们就像认识餐厅里的不同岗位：

- **Master 节点（大脑）**：这是 Kubernetes 的“指挥中心”，负责决策和调度。Master 节点包含以下关键部分：
  - **kube-apiserver**：相当于“前台接待员”，接收用户的所有请求（比如创建应用、查看状态），然后转发给其他组件。
  - **kube-scheduler**：相当于“调度员”，决定哪个应用（Pod）应该运行在哪个服务器（节点）上，确保资源分配合理。
  - **kube-controller-manager**：相当于“监管员”，不断检查集群状态，确保一切按计划运行，比如应用数量是否正确。它包含多个控制器，比如 Replication Controller、Deployment Controller 等，分别管理不同的资源。
  - **etcd**：相当于“记账本”，存储集群的所有配置和状态信息，是 Kubernetes 的“数据库”。

- **Worker 节点（工人）**：这是“干活的地方”，实际运行你的应用。每个 Worker 节点包含：
  - **kubelet**：相当于“现场监工”，负责在节点上创建、运行、监控应用（Pod），并向 Master 汇报情况。
  - **kube-proxy**：相当于“网络管理员”，管理节点上的网络流量，确保应用之间、应用与外界能正常通信。
  - **容器运行时**：比如 Docker、containerd 等，相当于“工具箱”，真正运行容器的引擎，负责拉取镜像、启动容器、停止容器等具体操作。

#### Container Manager（容器管理器）——“工具箱”的管理者

在 Worker 节点中，Container Manager（容器管理器）是一个非常重要的角色，虽然它不像 Master 节点的组件那样“高调”，但却是实际运行容器的“幕后英雄”。容器管理器是 Kubernetes 与容器运行时之间的“桥梁”，负责管理容器的生命周期。

- **什么是 Container Manager？**
  容器管理器是 Kubernetes 用来与容器运行时（如 Docker、containerd、CRI-O）交互的组件，kubelet 通过它来控制容器的创建、启动、停止和删除。简单来说，kubelet 就像一个“监工”，而容器管理器是“监工”手里的“工具”，真正去执行具体的容器操作。

- **为什么需要 Container Manager？**
  Kubernetes 本身并不直接操作容器，它需要一个中间层来统一管理不同的容器运行时工具（比如 Docker 和 containerd 的接口和用法不同）。容器管理器通过 CRI（Container Runtime Interface，容器运行时接口）提供一个标准化的方式，让 Kubernetes 能够兼容多种容器运行时，而不用关心底层实现细节。这就像一个“翻译官”，让 Kubernetes 和不同的“工具箱”无缝沟通。

- **Container Manager 的工作内容**：
  - 接收 kubelet 的指令，比如“启动一个容器”。
  - 调用容器运行时（如 Docker）去拉取镜像、创建容器、配置网络等。
  - 监控容器状态，并将信息反馈给 kubelet。
  - 处理容器停止、删除等操作。

- **举个通俗的例子**：
  假设 kubelet 是“建筑工地的监工”，它接到任务要建一栋房子（运行一个容器），但监工不会自己动手挖地基、砌墙，它会把任务交给“施工队”（容器运行时，如 Docker）。而 Container Manager 就像监工和施工队之间的“协调员”，负责把监工的指令翻译成施工队能听懂的语言，确保房子按要求建好。

在早期的 Kubernetes 中，Docker 是最常用的容器运行时，kubelet 直接通过 Docker 的接口操作容器。后来为了支持更多的容器运行时（如 containerd、CRI-O），Kubernetes 引入了 CRI 标准，Container Manager 就变成了一个抽象层，统一管理这些工具。

#### Kubernetes 集群的运行流程——一个简单的故事

假设你要部署一个网站应用，流程是这样的：
1. 你（用户）通过命令或界面告诉 Kubernetes：“我要部署一个网站应用。”
2. 请求送到 Master 节点的“前台”（kube-apiserver），它记录下来并通知“调度员”（kube-scheduler）。
3. “调度员”查看所有 Worker 节点的情况，挑一个资源最合适的节点，说：“这个应用跑在节点 2 上。”
4. 节点 2 的“监工”（kubelet）接到任务，通过 Container Manager 协调“工具箱”（容器运行时），启动应用（Pod），并不断监控它的状态。
5. 如果应用出了问题，“监工”会报告给 Master，Master 再决定是否重启或换个节点运行。

下图用 Mermaid 流程图直观展示这个过程：

```mermaid
graph TD
    User[用户] -->|提交请求| API[kube-apiserver]
    API --> Scheduler[kube-scheduler]
    Scheduler -->|调度 Pod| Worker1[Worker 节点 1]
    Scheduler -->|调度 Pod| Worker2[Worker 节点 2]
    Worker1 --> Kubelet1[kubelet]
    Worker2 --> Kubelet2[kubelet]
    Kubelet1 --> CM1[Container Manager]
    Kubelet2 --> CM2[Container Manager]
    CM1 --> Runtime1[容器运行时]
    CM2 --> Runtime2[容器运行时]
    Runtime1 --> Pod1[Pod]
    Runtime2 --> Pod2[Pod]
```

**解释**：用户通过 API 提交请求，Master 节点负责调度，Worker 节点的 kubelet 通过 Container Manager 调用容器运行时，最终让 Pod（应用）运行在合适的节点上。

### Pod 是什么？——Kubernetes 的最小“工人”

#### Pod 的定义与作用

在 Kubernetes 中，Pod 是最小的调度单位，相当于一个“工作小组”。一个 Pod 通常包含一个或多个容器（container），这些容器共享相同的网络和存储资源，就像一个小组的成员共享同一个办公室和文件柜。

为什么不直接用容器而要用 Pod 呢？因为容器是独立的运行单元，但有些应用需要多个容器协作，比如一个 Web 服务器容器和一个日志收集容器，它们需要紧密配合。Pod 就像一个“套装”，把这些容器打包在一起，确保它们在同一个节点上运行，互相通信就像在同一个房间里聊天一样方便。

#### Pod 的特点——为什么这么重要？

- **共享资源**：Pod 内的容器共享 IP 地址和端口，就像住在同一栋房子里的家人，用同一个门牌号和电话号码。它们可以通过 `localhost` 直接通信，不需要额外的网络配置。
- **生命周期短暂**：Pod 通常是临时的，可能会因为任务完成、故障或调度需要被销毁和重建。Kubernetes 会通过控制器（如 Deployment）确保 Pod 的数量和状态符合你的要求。
- **不可分割**：Pod 是一个整体，Kubernetes 不会把 Pod 内的容器拆开调度，它们要么一起运行在某个节点，要么都不运行。

#### Pod 在 Kubernetes 中的定位

Pod 是 Kubernetes 的“基层工人”，直接运行你的业务逻辑（比如网站、数据库）。它位于整个架构的最底层，接收来自 Master 节点的指令，由 Worker 节点上的 kubelet 负责创建和监控。简单来说：
- 用户定义想要运行的应用（通过 YAML 文件或命令）。
- Master 节点决定 Pod 跑在哪里。
- Worker 节点通过 kubelet 和 Container Manager 让 Pod 真正跑起来。

想象一个工厂：Master 节点是“厂长办公室”，下达生产任务；Worker 节点是“车间”，负责生产；Pod 就是车间里的“生产小组”，完成具体的产品（应用功能）；Container Manager 是“协调员”，确保生产工具（容器运行时）按要求工作。

### Namespace 是什么？——Kubernetes 的“分区管理员”

#### Namespace 的定义与作用

Namespace（命名空间）是 Kubernetes 提供的一种逻辑隔离机制，相当于给集群划分了不同的“区域”或“部门”。在同一个 Kubernetes 集群中，你可能有多个团队、多个项目、多个环境（比如开发环境、测试环境、生产环境），如果不隔离，大家的资源名称可能会冲突，管理也会很混乱。

Namespace 就像在一栋大厦里划分不同的楼层：每个楼层有自己的房间（资源），互不干扰，但都在同一栋楼（集群）里。每个 Namespace 内的资源（如 Pod、ConfigMap）是独立的，名称可以重复，但不会影响其他 Namespace。

#### Namespace 的典型应用场景

- **团队隔离**：开发团队和测试团队各用一个 Namespace，避免误操作对方的资源。
- **环境隔离**：开发环境（dev）、测试环境（test）、生产环境（prod）分别用不同的 Namespace，确保生产环境不会被测试操作影响。
- **权限管理**：通过 Kubernetes 的 RBAC（基于角色的访问控制），可以给不同 Namespace 设置不同权限，比如只允许某些用户访问某个 Namespace。

#### Namespace 的基本操作

- **创建 Namespace**：通过命令行或配置文件创建。
  - 命令行：`kubectl create namespace my-namespace`
  - YAML 文件示例：
    ```yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: my-namespace
    ```
- **查看 Namespace**：列出集群中所有的 Namespace。
  - 命令行：`kubectl get namespaces`
- **指定 Namespace**：创建资源时，可以指定它属于哪个 Namespace。
  - 命令行：`kubectl apply -f pod.yaml -n my-namespace`
  - YAML 文件：在 `metadata` 中添加 `namespace` 字段。
- **删除 Namespace**：删除 Namespace 会同时删除它里面的所有资源。
  - 命令行：`kubectl delete namespace my-namespace`

#### Namespace 的可视化理解

下图用 Mermaid 图展示 Namespace 如何隔离资源：

```mermaid
graph TD
    Cluster[Kubernetes 集群] --> NS1[Namespace: dev]
    Cluster --> NS2[Namespace: test]
    Cluster --> NS3[Namespace: prod]
    NS1 --> Pod1[Pod 1]
    NS1 --> Pod2[Pod 2]
    NS2 --> Pod3[Pod 3]
    NS2 --> Pod4[Pod 4]
    NS3 --> Pod5[Pod 5]
    NS3 --> Pod6[Pod 6]
```

**解释**：Kubernetes 集群就像一个大容器，里面有多个 Namespace（dev、test、prod），每个 Namespace 管理自己的 Pod，互不干扰，就像不同楼层的办公室各自独立运作。

#### Namespace 与 Pod 的关系

Pod 通常属于某个 Namespace。如果你在创建 Pod 时没有指定 Namespace，它会默认放在 `default` 这个 Namespace 里。指定 Namespace 后，Pod 就只能被该 Namespace 内的其他资源或用户访问（除非有特殊权限设置）。这就像一个员工被分配到某个部门，只能使用该部门的资源和工具。

### 总结：Namespace、Kubernetes 基础与 Pod 的关系

- **Kubernetes** 是整个系统的“大脑”和“管理者”，负责协调容器化应用的运行，包含 Master 节点（决策）和 Worker 节点（执行）。
- **Pod** 是 Kubernetes 的最小工作单位，相当于“工人小组”，直接运行你的应用，接收 Master 节点的调度指令，由 Worker 节点上的 kubelet 管理。
- **Container Manager** 是 Kubernetes 与容器运行时之间的“桥梁”，通过 CRI 标准接口，让 kubelet 能够统一管理不同的容器运行时（如 Docker、containerd），确保容器按要求创建和运行。
- **Namespace** 是 Kubernetes 的“分区工具”，通过逻辑隔离让多个团队、项目或环境在同一个集群中和谐共存，避免冲突。


## 第二部分：实践练习——创建 Namespace 与 Pod

### 练习目标

通过本次实践练习，同学们将学会：
- 使用 VMware 准备 Harbor 镜像。
- 使用 `kubectl` 命令创建属于自己的 Namespace（命名空间）。
- 构建、运行和上传 Docker 镜像到 Harbor 私库。
- 在 Kubernetes 集群中创建 Pod，并将其运行在自己创建的 Namespace 中。
- 使用命令行和 Kuboard 界面查看 Pod 状态。

### 前期准备

在开始今天的练习之前，确保你已经完成了以下准备工作：
- **Windows 或 Mac 电脑**：所有操作（除 VMware 部分外）都在自己的 Windows 或 Mac 电脑上完成。
- **kubectl 工具**：已经安装并配置好，可以与 Kubernetes 集群通信。
- **Docker 环境**：已经安装 Docker Desktop，并配置好 `daemon.json` 和 Harbor 私库登录。
- **VMware**：确保 VMware 虚拟机环境已准备好，用于 Harbor 镜像相关操作。
- **Visual Studio Code (VS Code)**：安装并配置好，用于编写 Kubernetes YAML 文件。
- **Kuboard 访问权限**：确保你有权限访问 Kuboard 管理界面，并已知晓登录地址、用户名和密码（由老师提供）。

#### VS Code 插件安装

为了方便编写 Kubernetes YAML 文件和后期学习，推荐安装以下 VS Code 插件：

- **Kubernetes**：提供 Kubernetes 资源支持，包括语法高亮、自动补全和片段。
- **YAML**：提供 YAML 文件的语法高亮、验证和格式化支持。
- **Kube-Extension**：直接与 Kubernetes 集群交互，查看和管理资源。
- **Helm Intellisense**：支持 Helm Charts 的智能提示和语法高亮（可选）。
- **GitLens**：增强 Git 功能，方便跟踪文件版本变更。
- **Prettier - Code formatter**：统一代码格式，支持 YAML 文件格式化。

**安装方法**：
1. 打开 VS Code。
2. 点击左侧扩展图标（或按 `Ctrl + Shift + X`）。
3. 在搜索框中输入插件名称。
4. 点击“安装”按钮。

**使用技巧**：
- 使用插件提供的代码片段，快速生成 Kubernetes 配置。
- 利用 YAML 插件验证配置文件，确保格式正确。
- 通过 Kubernetes 插件直接与集群交互，方便调试。

### 练习步骤

#####步骤 1：打开 VMware 准备 Harbor 镜像

我们首先需要在 VMware 环境中准备 Harbor 镜像相关工作。请按照以下步骤操作：

1. 打开 VMware，启动你的虚拟机环境。
2. 确保虚拟机网络配置正确，可以访问外部网络和 Harbor 私库 `harbor.labworlds.cc`。
3. 如果老师已经在 VMware 环境中为大家准备好相关镜像或项目，直接确认 Harbor 私库是否可访问；如果需要自行准备，请登录 Harbor 私库并确保后续镜像上传和拉取操作顺畅。
   - 登录命令（如果需要）：
     ```bash
     docker login harbor.labworlds.cc
     ```
   - 输入用户名和密码，确保登录成功。

**小贴士**：VMware 环境主要用于模拟服务器或测试环境，确保你的虚拟机已配置好 Docker 和网络，后续镜像构建和上传可能需要用到虚拟机中的资源。

#### 步骤 2：构建和运行 Docker 镜像（在 Windows 或 Mac 电脑上操作）

接下来，我们将在自己的 Windows 或 Mac 电脑上构建 Docker 镜像，并测试运行。确保你已经安装了 Docker 并登录了 Harbor 私库 `harbor.labworlds.cc`。

1. **克隆代码仓库**：
   打开终端（Windows 使用 PowerShell 或 CMD，Mac 使用 Terminal），执行以下命令克隆项目代码：
   ```bash
   git clone https://gitee.com/Tender-Liu/stars-emmision.git
   ```
2. **进入项目目录**：
   ```bash
   cd stars-emmision
   ```
3. **构建 Docker 镜像**：
   使用 `docker build` 命令构建镜像，标签格式为 `harbor.labworlds.cc/stars-emmision/master:日期-名字拼音`。请根据当前日期和自己的名字拼音修改，例如日期 `08061743`（表示 08 月 06 日 17:43），名字 `shiqi`：
   ```bash
   docker build -t harbor.labworlds.cc/stars-emmision/master:08061743-shiqi .
   ```
   **注意**：命令末尾的 `.` 表示在当前目录构建镜像，请不要遗漏。
4. **测试运行镜像**：
   构建完成后，测试镜像是否可以正常运行。执行以下命令，替换为你的镜像标签：
   ```bash
   docker run --rm -p 80:80 harbor.labworlds.cc/stars-emmision/master:08061743-shiqi
   ```
   运行后，打开浏览器访问 `http://localhost`，检查是否能看到应用页面。如果正常显示，说明镜像构建成功。
5. **上传镜像到 Harbor 私库**：
   如果测试没有问题，将镜像上传到 Harbor 私库：
   ```bash
   docker push harbor.labworlds.cc/stars-emmision/master:08061743-shiqi
   ```
   **注意**：确保你已经登录 Harbor 私库（使用 `docker login harbor.labworlds.cc` 命令）。

**小贴士**：Harbor 是一个私有的镜像仓库，老师已经为大家创建好项目，上传镜像后可以在 Kubernetes 中使用这些镜像运行应用。

#### 步骤 3：创建自己的 Namespace（在 Windows 或 Mac 电脑上操作）

我们将使用 `kubectl` 命令创建一个属于自己的命名空间。命名空间名称请使用自己名字的拼音全拼，这样方便老师认识大家。

1. 打开终端（Windows 使用 PowerShell 或 CMD，Mac 使用 Terminal）。
2. 输入以下命令创建 Namespace，替换 `your-pinyin-name` 为你名字的拼音全拼，例如 `zhangwei`：
   ```bash
   kubectl create namespace your-pinyin-name
   ```
3. 验证 Namespace 是否创建成功：
   ```bash
   kubectl get namespaces
   ```
   在输出结果中，你应该能看到自己创建的 Namespace 名称。

**小贴士**：Namespace 就像 Kubernetes 集群中的一个“私人空间”，你可以在这里管理自己的资源，不会与其他同学的资源冲突。

#### 步骤 4：在自己的 Namespace 中创建 Harbor 登录 Secret（在 Windows 或 Mac 电脑上操作）

在 Kubernetes 中，Secret 是一种用于存储敏感信息（如用户名、密码等）的资源。我们需要创建一个 Secret 来存储 Harbor 私库的登录凭据，以便 Kubernetes 在拉取镜像时使用这些凭据进行身份验证。以下是具体操作步骤。

##### 4.1 使用 YAML 文件和 `kubectl` 命令创建 Secret

1. 打开 VS Code，在之前存放 Kubernetes 配置文件的文件夹中新建一个文件，命名为 `secret-harbor-login.yml`。
2. 将以下内容复制到文件中，并确保 Namespace 字段替换为你自己的 Namespace 名称（拼音全拼）。这里提供两种方式：明文方式和已编码方式，你可以根据需要选择。

   **选项 1：以明文形式编写（使用 `stringData` 字段）**  
   如果你希望在 YAML 文件中直接以明文形式编写用户名和密码，可以使用 `stringData` 字段，Kubernetes 会自动将明文转换为 Base64 编码存储在 Secret 中：
   ```yaml
   apiVersion: v1  # 指定 Kubernetes API 的版本
   kind: Secret  # 资源类型，这里是 Secret
   metadata:
     name: secret-harbor-login  # Secret 的名称
     namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
   type: kubernetes.io/dockerconfigjson  # Secret 类型，用于存储 Docker 镜像仓库登录信息
   stringData:  # 使用 stringData 字段直接以明文形式输入数据
     .dockerconfigjson: '{"auths":{"harbor.labworlds.cc":{"username":"admin","password":"admin123","auth":"YWRtaW46YWRtaW4xMjM="}}}'  # 明文 JSON 格式的 Docker 配置信息
   ```
   **注意**：
   - 将 `namespace` 字段替换为你的 Namespace 名称（拼音全拼，例如 `zhangwei`）。
   - `stringData` 字段中的内容是明文，Kubernetes 在创建 Secret 时会自动将这些内容编码为 Base64 并存储到 `data` 字段中。
   - 虽然这种方式便于编写和阅读，但不建议在生产环境中使用，因为 YAML 文件可能会被意外共享或存储在版本控制系统中，导致敏感信息泄露。

   **选项 2：以 Base64 编码形式编写（使用 `data` 字段）**  
   如果你希望更安全地处理敏感信息，可以先对数据进行 Base64 编码，然后写入 `data` 字段：
   ```yaml
   apiVersion: v1  # 指定 Kubernetes API 的版本
   kind: Secret  # 资源类型，这里是 Secret
   metadata:
     name: secret-harbor-login  # Secret 的名称
     namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
   type: kubernetes.io/dockerconfigjson  # Secret 类型，用于存储 Docker 镜像仓库登录信息
   data:
     .dockerconfigjson: eyJhdXRocyI6eyJoYXJib3IubGFid29ybGRzLmNjIjogeyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbjEyMyIsImF1dGgiOiJZV1J0YVc0NmFXTnNhV05vYldWdWRDST0ifX19  # Base64 编码后的 Docker 配置信息
   ```
   **注意**：
   - `data` 字段中的 `.dockerconfigjson` 值是已经对 Harbor 登录信息（地址：`http://harbor.labworlds.cc`，账号：`admin`，密码：`admin123`）进行 Base64 编码后的结果。你可以直接使用上述值，无需手动编码。如果需要自行生成，可以使用以下命令：
     ```bash
     echo -n '{"auths":{"harbor.labworlds.cc":{"username":"admin","password":"admin123","auth":"'"$(echo -n 'admin:admin123' | base64)"'"}}}' | base64
     ```

3. 保存文件。
4. 在终端中，进入 `secret-harbor-login.yml` 文件所在的目录，执行以下命令创建 Secret：
   ```bash
   kubectl apply -f secret-harbor-login.yml
   ```
5. 验证 Secret 是否创建成功：
   ```bash
   kubectl get secrets -n your-pinyin-name
   ```
   替换 `your-pinyin-name` 为你的 Namespace 名称。输出中应该能看到 `secret-harbor-login`。

**小贴士**：Secret 中的数据最终都会以 Base64 编码形式存储在 Kubernetes 中。虽然 Base64 编码不是加密，但可以防止直接明文查看敏感信息。创建 Secret 后，Kubernetes 会自动使用其中的凭据来访问 Harbor 私库拉取镜像（需要在 Pod 配置中引用此 Secret，后续步骤会介绍）。建议尽量避免在 YAML 文件中直接使用明文，尤其是在文件可能被共享或提交到版本控制系统的情况下。

##### 4.2 使用 Kuboard 界面创建 Secret（可选）

如果你不习惯使用命令行，也可以通过 Kuboard 界面创建 Secret。以下是具体步骤：

1. **访问 Kuboard 界面**：
   - 打开浏览器，输入老师提供的 Kuboard 访问地址（例如 `http://kuboard.your-cluster-domain.com`）。
   - 使用老师提供的用户名和密码登录 Kuboard。
2. **选择 Namespace**：
   - 登录后，在页面顶部或左侧导航栏中找到 Namespace 选择框。
   - 从下拉列表中选择你创建的 Namespace（例如 `your-pinyin-name`）。
3. **进入 Secret 创建页面**：
   - 在 Namespace 页面中，点击左侧导航栏中的“配置（Config）”或“Secret”选项。
   - 点击页面右上角的“创建（Create）”或“添加（Add）”按钮，进入 Secret 创建页面。
4. **填写 Secret 信息**：
   - **名称（Name）**：输入 `secret-harbor-login`。
   - **类型（Type）**：选择 `kubernetes.io/dockerconfigjson`（用于 Docker 镜像仓库登录）。
   - **数据（Data）**：在数据字段中，点击添加键值对，键为 `.dockerconfigjson`，值粘贴以下内容：
     ```
     {"auths":{"harbor.labworlds.cc":{"username":"admin","password":"admin123","auth":"YWRtaW46YWRtaW4xMjM="}}}
     ```
     上述内容是未编码的 JSON 格式，部分 Kuboard 版本会自动进行 Base64 编码。如果需要手动编码，可以参考 3.1 中的命令。
   - 确认无误后，点击“保存（Save）”或“创建（Create）”按钮。
5. **验证 Secret 创建**：
   - 创建完成后，回到 Secret 列表页面，你应该能看到 `secret-harbor-login` 出现在列表中。

**小贴士**：使用 Kuboard 界面创建 Secret 更加直观，适合初学者。如果界面中没有看到刚创建的 Secret，可以刷新页面或确认 Namespace 是否选择正确。

##### 4.3 使用 Kuboard 界面查看 Secret

创建 Secret 后，你可以通过 Kuboard 界面查看其基本信息（注意，敏感数据通常会被隐藏或以星号显示）。

1. **进入 Secret 列表**：
   - 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
   - 点击左侧导航栏中的“配置（Config）”或“Secret”选项。
2. **查看 Secret 详情**：
   - 在 Secret 列表中找到 `secret-harbor-login`，点击其名称进入详情页面。
   - 你可以看到 Secret 的基本信息，如名称、类型、创建时间等。
   - 数据字段中的具体内容（如 `.dockerconfigjson`）通常会以星号（***）显示，以保护敏感信息。如果你需要确认数据是否正确，可以通过 `kubectl` 命令查看编码后的值：
     ```bash
     kubectl get secret secret-harbor-login -n your-pinyin-name -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d
     ```


#### 步骤 5：创建 Pod YAML 文件（在 Windows 或 Mac 电脑上操作）

现在，我们将使用 VS Code 创建一个 Kubernetes Pod 的配置文件，并指定 Pod 运行在自己创建的 Namespace 中。

1. 打开 VS Code，选择一个文件夹用于存放 Kubernetes 配置文件。
2. 新建一个文件，命名为 `pod-stars-emmision.yml`。
3. 将以下内容复制到文件中，并根据自己的 Namespace 和镜像标签进行修改：
   ```yaml
   apiVersion: v1  # 指定 Kubernetes API 的版本
   kind: Pod  # 资源类型，这里是 Pod
   metadata:
     name: pod-stars-emmision  # Pod 的名称，符合企业标准
     namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
   spec:
     containers:  # 定义 Pod 中的容器
       - name: stars-emmision  # 容器的名称
         image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
         ports:  # 指定容器暴露的端口
           - containerPort: 80  # 容器内部使用的端口号，这里是 80
         livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
           httpGet:  # 使用 HTTP GET 请求进行探测
             path: /  # 请求的路径，这里是根路径
             port: 80  # 请求的端口，这里是 80
           initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
           periodSeconds: 10  # 每 10 秒进行一次探测
         readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
           httpGet:  # 使用 HTTP GET 请求进行探测
             path: /  # 请求的路径，这里是根路径
             port: 80  # 请求的端口，这里是 80
           initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
           periodSeconds: 10  # 每 10 秒进行一次探测
     imagePullSecrets:  # 指定用于拉取镜像的 Secret
       - name: secret-harbor-login  # 引用之前创建的 Secret 名称
   ```
   **注意**：
   - 将 `namespace` 字段替换为你的 Namespace 名称（拼音全拼）。
   - 将 `image` 字段替换为你在步骤 2 中构建并上传的镜像标签。

4. 保存文件。

**小贴士**：
- **livenessProbe（活性探测）**：用来检查容器是否还“活着”，如果探测失败，Kubernetes 会重启容器。
- **readinessProbe（就绪探测）**：用来检查容器是否准备好接收流量，如果探测失败，Kubernetes 不会将流量发送到这个容器。

#### 步骤 6：部署 Pod 到 Kubernetes 集群并查看状态（在 Windows 或 Mac 电脑上操作）

YAML 文件准备好后，使用 `kubectl` 命令将 Pod 部署到 Kubernetes 集群中，并通过命令行和 Kuboard 界面查看 Pod 状态。

##### 6.1 使用 `kubectl` 命令部署和查看 Pod

1. 在终端中，进入 `pod-stars-emmision.yml` 文件所在的目录。
2. 执行以下命令部署 Pod：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   ```
3. 检查 Pod 是否创建成功：
   ```bash
   kubectl get pods -n your-pinyin-name
   ```
   替换 `your-pinyin-name` 为你的 Namespace 名称。输出中应该能看到 `pod-stars-emmision` 的状态为 `Running`。
4. 查看 Pod 的详细状态和日志（可选）：
   - 查看 Pod 详细信息：
     ```bash
     kubectl describe pod pod-stars-emmision -n your-pinyin-name
     ```
   - 查看 Pod 内容器的日志：
     ```bash
     kubectl logs pod-stars-emmision -n your-pinyin-name
     ```

**小贴士**：如果 Pod 状态显示为 `ImagePullBackOff` 或其他错误，可能是镜像地址有误或未上传成功，请检查镜像标签和 Harbor 登录状态。

##### 5.2 使用 Kuboard 界面查看 Pod

除了命令行工具 `kubectl`，我们还可以使用 Kuboard 界面来查看和管理 Kubernetes 资源。Kuboard 是一个可视化管理工具，可以更直观地展示集群中的资源状态。以下是具体操作步骤：

1. **访问 Kuboard 界面**：
   - 打开浏览器，输入老师提供的 Kuboard 访问地址（例如 `http://kuboard.your-cluster-domain.com`）。
   - 使用老师提供的用户名和密码登录 Kuboard。
2. **选择 Namespace**：
   - 登录后，在页面顶部或左侧导航栏中找到 Namespace 选择框。
   - 从下拉列表中选择你创建的 Namespace（例如 `your-pinyin-name`）。
   - 如果没有看到你的 Namespace，可能需要刷新页面或确认登录账户是否有权限查看该 Namespace。
3. **查看 Pod 列表**：
   - 在 Namespace 页面中，点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项。
   - 你会看到当前 Namespace 下的 Pod 列表，找到名为 `pod-stars-emmision` 的 Pod。
   - Pod 列表会显示状态（例如 `Running` 或 `Pending`）、创建时间等信息。如果状态为绿色，表示 Pod 运行正常；如果为红色或黄色，可能存在问题。
4. **查看 Pod 详细信息**：
   - 点击 `pod-stars-emmision` 的名称，进入 Pod 详情页面。
   - 在详情页面中，你可以看到 Pod 的基本信息（如镜像、端口）、容器状态、事件（Events）等。
   - 如果需要查看日志，找到“日志（Logs）”选项卡，选择容器名称 `stars-emmision`，即可查看容器运行日志。
5. **排查问题（可选）**：
   - 如果 Pod 状态异常，可以在“事件（Events）”选项卡中查看详细错误信息，例如镜像拉取失败或资源不足。
   - 根据错误信息，回到命令行工具或 Harbor 私库进行排查和修复。

**小贴士**：
- Kuboard 界面操作直观，适合初学者快速了解集群资源状态，但某些复杂操作（如修改配置）仍需使用 `kubectl` 命令。
- 如果 Kuboard 中看不到 Pod 或 Namespace，可能需要检查你的权限设置或询问老师是否已分配正确的访问权限。

### 总结与检查

完成以上步骤后，你应该已经：
- 在 VMware 环境中准备好 Harbor 镜像相关工作。
- 创建了一个属于自己的 Namespace（以名字拼音全拼命名）。
- 在 Windows 或 Mac 电脑上构建并上传了 Docker 镜像到 Harbor 私库。
- 在自己的 Namespace 中成功部署了一个 Pod，并运行了 `stars-emmision` 应用。
- 使用 `kubectl` 命令行工具和 Kuboard 界面查看了 Pod 的状态和详细信息。


## 第三部分：基本命令学习——Pod 管理（结合 Kuboard 界面）

### 前期准备
在开始本部分的学习之前，确保你已经完成了以下准备工作：
- 完成了第二部分的实践练习，已经在自己的 Namespace 中创建并部署了一个 Pod（例如 `pod-stars-emmision`）。
- 确保 `kubectl` 工具已正确配置，可以与 Kubernetes 集群通信。
- 确保你有权限访问 Kuboard 管理界面，并已知晓登录地址、用户名和密码（由老师提供）。
- 熟悉基本的终端操作（Windows 使用 PowerShell 或 CMD，Mac 使用 Terminal）。

### 学习内容

我们将通过命令行工具 `kubectl` 和 Kuboard 图形化界面两种方式学习 Pod 的基本管理操作。以下内容会逐一介绍每个操作，并提供命令行和界面对应的步骤，方便同学们对比学习。

**Pod 管理操作总结表格**：
以下表格总结了 Pod 管理的常用操作，方便同学们日后快速参考 `kubectl` 命令和 Kuboard 界面操作步骤。注意：以下命令中需将 `your-pinyin-name` 替换为你的 Namespace 名称，Pod 名称以 `pod-stars-emmision` 为例。

| **操作内容**         | **kubectl 命令行操作**                                                                 | **Kuboard 界面操作步骤**                                                                                     |
|----------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 查看 Pod 列表        | `kubectl get pods -n your-pinyin-name`                                               | 选择 Namespace → 点击“工作负载”或“Pod” → 查看列表                                                          |
| 查看 Pod 详情        | `kubectl describe pod pod-stars-emmision -n your-pinyin-name`                       | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 查看详情                                         |
| 查看 Pod 日志        | `kubectl logs pod-stars-emmision -n your-pinyin-name`                               | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 选择“日志”选项卡                                 |
| 进入 Pod 内部        | `kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash`              | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 选择“终端”选项卡                                 |
| 创建 Pod             | `kubectl apply -f pod-stars-emmision.yml`                                           | 选择 Namespace → 点击“工作负载”或“Pod” → 点击“创建” → 上传 YAML 或填写表单 → 保存                        |
| 删除 Pod             | `kubectl delete -f pod-stars-emmision.yml` 或<br>`kubectl delete pod pod-stars-emmision -n your-pinyin-name` | 选择 Namespace → 点击“工作负载”或“Pod” → 勾选 Pod → 点击“删除” → 确认                                    |
| 重启 Pod（单独 Pod） | `kubectl delete pod pod-stars-emmision -n your-pinyin-name` 后重新 `apply`          | 选择 Namespace → 点击“工作负载”或“Pod” → 勾选 Pod → 点击“删除” → 重新创建                                |
| 重启 Pod（Deployment）| `kubectl rollout restart deployment <deployment-name> -n your-pinyin-name`          | 选择 Namespace → 点击“工作负载”或“Deployment” → 选择 Deployment → 点击“重启”或“滚动更新”                 |
| 查看健康检查状态     | `kubectl describe pod pod-stars-emmision -n your-pinyin-name` （查看 Events）       | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 查看“事件（Events）”选项卡                      |

#### 1. 查看 Pod 列表

了解当前 Namespace 中运行的 Pod 是管理的第一步。我们可以通过命令行和 Kuboard 界面查看 Pod 列表及其状态。

- **命令行操作（使用 `kubectl`）**：
  打开终端，输入以下命令查看当前 Namespace 中的 Pod 列表（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl get pods -n your-pinyin-name
  ```
  输出结果会显示 Pod 的名称、状态（例如 `Running`）、重启次数和运行时间等信息。如果不指定 Namespace，可以使用以下命令查看所有 Namespace 中的 Pod：
  ```bash
  kubectl get pods --all-namespaces
  ```
  **小贴士**：如果列表中没有看到你的 Pod，可能是 Namespace 名称输入错误或 Pod 尚未创建成功。

- **Kuboard 界面操作**：
  1. 打开浏览器，访问老师提供的 Kuboard 登录地址（例如 `http://kuboard.your-cluster-domain.com`）。
  2. 使用提供的用户名和密码登录 Kuboard。
  3. 在页面顶部或左侧导航栏中找到 Namespace 选择框，选择你的 Namespace（例如 `your-pinyin-name`）。
  4. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项。
  5. 在 Pod 列表页面，你可以看到当前 Namespace 中所有 Pod 的名称、状态（例如绿色表示 `Running`）、所属节点和创建时间等信息。
  **小贴士**：如果列表中没有看到你的 Pod，可以刷新页面或确认是否选择了正确的 Namespace。

#### 2. 查看 Pod 详情

当需要了解 Pod 的详细信息（例如镜像、端口、事件等）时，可以查看 Pod 的详细描述。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，查看特定 Pod 的详细信息（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl describe pod pod-stars-emmision -n your-pinyin-name
  ```
  输出结果会显示 Pod 的基本信息、容器配置、状态以及相关事件（Events），例如镜像拉取是否成功或容器启动是否正常。
  **小贴士**：通过 `describe` 命令可以快速排查 Pod 异常问题，例如 `ImagePullBackOff` 错误通常表示镜像拉取失败。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，你可以看到 Pod 的基本信息（如镜像、端口）、容器状态以及事件（Events）等详细信息。
  **小贴士**：如果 Pod 状态异常，可以在“事件（Events）”选项卡中查看具体错误信息，帮助排查问题。

#### 3. 查看 Pod 日志

查看 Pod 中容器的日志是调试和监控的重要手段，可以帮助了解应用运行情况。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，查看特定 Pod 的日志（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl logs pod-stars-emmision -n your-pinyin-name
  ```
  输出结果会显示 Pod 中容器的运行日志。如果 Pod 中有多个容器，可以指定容器名称，例如：
  ```bash
  kubectl logs pod-stars-emmision -c stars-emmision -n your-pinyin-name
  ```
  **小贴士**：如果需要实时查看日志，可以添加 `--follow` 参数，例如 `kubectl logs --follow pod-stars-emmision -n your-pinyin-name`。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，找到“日志（Logs）”选项卡，选择容器名称（例如 `stars-emmision`）。
  5. 日志内容会显示在页面中，你可以滚动查看或刷新以获取最新日志。
  **小贴士**：Kuboard 界面支持实时日志查看，点击“刷新”按钮或勾选“自动刷新”选项即可。

#### 4. 进入 Pod 内部

有时需要进入 Pod 内部的容器进行调试或查看文件，可以通过命令行或 Kuboard 界面进入容器。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，进入特定 Pod 的容器内部（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash
  ```
  如果容器中没有 `/bin/bash`，可以尝试使用 `/bin/sh`：
  ```bash
  kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/sh
  ```
  进入容器后，你可以执行命令查看文件或环境变量等，输入 `exit` 退出容器。
  **小贴士**：如果 Pod 中有多个容器，需要指定容器名称，例如 `kubectl exec -it pod-stars-emmision -c stars-emmision -n your-pinyin-name -- /bin/bash`。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，找到“终端（Terminal）”选项卡，选择容器名称（例如 `stars-emmision`）。
  5. 终端窗口会打开，你可以在其中输入命令进行操作，操作完成后关闭窗口即可退出。
  **小贴士**：Kuboard 的终端功能类似 `kubectl exec`，但更直观，适合不熟悉命令行的同学使用。

#### 5. 创建 Pod

如果你需要重新创建或部署一个新的 Pod，可以通过 YAML 文件或 Kuboard 界面完成。

- **命令行操作（使用 `kubectl`）**：
  假设你已经准备好 Pod 的 YAML 文件（例如 `pod-stars-emmision.yml`），在终端中进入文件所在目录，执行以下命令创建 Pod：
  ```bash
  kubectl apply -f pod-stars-emmision.yml
  ```
  创建完成后，可以使用 `kubectl get pods` 命令查看 Pod 状态。
  **小贴士**：如果 YAML 文件有误，命令会报错，请仔细检查文件内容。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 点击页面右上角的“创建（Create）”或“添加（Add）”按钮。
  4. 在创建页面中，你可以选择上传 YAML 文件（直接上传 `pod-stars-emmision.yml`），或者通过表单填写 Pod 的基本信息（如名称、镜像、端口等）。
  5. 填写或上传完成后，点击“保存（Save）”或“创建（Create）”按钮。
  6. 创建完成后，回到 Pod 列表页面查看新创建的 Pod 状态。
  **小贴士**：Kuboard 界面支持表单和 YAML 两种方式创建 Pod，表单方式更适合初学者。

#### 6. 删除 Pod

当不再需要某个 Pod 时，可以将其删除。

- **命令行操作（使用 `kubectl`）**：
  有两种方式删除 Pod：
  - 如果有 YAML 文件，可以使用以下命令删除：
    ```bash
    kubectl delete -f pod-stars-emmision.yml
    ```
  - 或者直接指定 Pod 名称删除（替换 `your-pinyin-name` 为你的 Namespace 名称）：
    ```bash
    kubectl delete pod pod-stars-emmision -n your-pinyin-name
    ```
  删除后，可以使用 `kubectl get pods` 命令确认 Pod 是否已删除。
  **小贴士**：如果 Pod 由控制器（如 Deployment）管理，删除 Pod 后控制器可能会自动重建 Pod。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），勾选该 Pod 或点击右侧操作按钮。
  4. 选择“删除（Delete）”选项，确认删除操作。
  5. 删除完成后，刷新页面确认 Pod 已从列表中消失。
  **小贴士**：Kuboard 界面删除操作简单直观，但同样需要注意是否由控制器管理 Pod。

#### 7. 重启 Pod - 只有未来学习了Deployment才行
Kubernetes 没有直接的重启 Pod 命令，但可以通过删除 Pod 让控制器（如 Deployment）自动重建，或者手动触发重启。


#### 8. 健康检查（通过配置实现）

健康检查是确保 Pod 和容器正常运行的重要机制，Kubernetes 提供了 `livenessProbe`（活性探测）和 `readinessProbe`（就绪探测）两种方式。这部分已在第二部分的 YAML 示例中介绍过，同学们可以回顾 `pod-stars-emmision.yml` 文件中的配置：
- `livenessProbe`：检查容器是否存活，如果探测失败，Kubernetes 会重启容器。
- `readinessProbe`：检查容器是否准备好接收流量，如果探测失败，Kubernetes 不会将流量发送到该容器。

- **命令行操作（使用 `kubectl`）**：
  使用 `describe` 命令查看 Pod 的健康检查状态：
  ```bash
  kubectl describe pod pod-stars-emmision -n your-pinyin-name
  ```
  在输出中的“Events”部分，可以看到健康检查的结果。

- **Kuboard 界面操作**：
  在 Pod 详情页面中，查看“事件（Events）”选项卡，了解健康检查的探测情况。

**小贴士**：健康检查配置需要根据应用特点调整，例如探测路径、频率和延迟时间等。

#### 总结与对比

通过本部分的学习，同学们应该已经掌握了以下内容：
- 使用 `kubectl` 命令行工具管理 Pod 的基本操作，包括查看列表、详情、日志，进入容器，创建、删除和重启 Pod。
- 使用 Kuboard 图形化界面完成相同的 Pod 管理操作，理解图形化工具与命令行的对应关系。
- 初步了解健康检查的概念及其在 Pod 配置中的作用。

**命令行与 Kuboard 界面对比**：
- **命令行（`kubectl`）**：操作灵活，适合自动化脚本和复杂任务，但需要记忆命令和参数，对初学者有一定学习曲线。
- **Kuboard 界面**：直观易用，适合初学者快速上手，降低了学习难度，但某些高级功能可能不如命令行灵活。

建议同学们在学习初期结合两种方式操作，先通过 Kuboard 界面熟悉资源管理流程，再逐步掌握 `kubectl` 命令，提升效率和深度理解。

## 第四部分：健康检查机制——livenessProbe、readinessProbe 和 startupProbe

### 健康检查机制概述

在 Kubernetes 中，健康检查（Health Check）是用来确保容器正常运行的“体检工具”。Kubernetes 会通过不同的“检查方式”来判断容器是否健康，并决定是否需要重启容器或调整流量分配。简单来说，健康检查就像给容器做定期体检，发现问题就及时处理，避免影响服务。

Kubernetes 提供了三种检查方式，我们可以把它们想象成三种不同的“体检项目”：
- **livenessProbe（活性探测）**：检查容器是否“活着”。如果检查失败，Kubernetes 会认为容器“生病了”，会重启它来尝试恢复。
- **readinessProbe（就绪探测）**：检查容器是否“准备好工作”。如果检查失败，Kubernetes 不会把用户请求发到这个容器，直到它“恢复健康”。
- **startupProbe（启动探测）**：检查容器是否“启动完成”。专门针对启动慢的应用，确保容器有足够时间准备好，不会因为还没启动完就被误判为不健康。

**为什么要用健康检查？**
想象一下，如果你的容器崩溃了，或者还没准备好就接收用户请求，结果会怎样？健康检查就是帮你避免这些问题，让服务更稳定。

### 健康检查原理详解（简单版）

我们用生活中的例子来解释这三种检查的原理和作用：

1. **livenessProbe（活性探测）**
   - **原理**：就像医生定期检查病人的心跳，如果心跳停止（检查失败），医生会尝试“抢救”（重启容器）。Kubernetes 会根据检查结果决定是否需要重启容器。
   - **作用**：确保容器不会“卡死”或“崩溃”，如果有问题就重启它。
   - **例子**：检查一个 Web 服务是否还能响应请求，如果不响应就重启。

2. **readinessProbe（就绪探测）**
   - **原理**：就像检查一个员工是否准备好上班，如果员工还在“喝咖啡”（检查失败），老板不会给他分配任务。Kubernetes 不会把流量发到还没准备好的容器。
   - **作用**：确保用户请求只发到准备好的容器，避免出错或延迟。
   - **例子**：检查应用是否连接上数据库，只有连接好了才接收请求。

3. **startupProbe（启动探测）**
   - **原理**：就像检查一个新员工是否完成了入职培训，如果还没完成（检查失败），老板会给他更多时间，不会急着安排工作。Kubernetes 会等容器启动完成再进行其他检查。
   - **作用**：给启动慢的应用更多时间，避免被误判为不健康。
   - **例子**：检查一个需要加载大文件的应用是否启动完成。

**三种检查的关系（Mermaid 流程图）**：
以下是一个简单的流程图，展示三种探测如何配合工作：

```mermaid
graph TD
    A[容器启动] --> B{startupProbe 检查}
    B -->|失败| C[等待重试, 延迟其他检查]
    B -->|成功| D{livenessProbe 检查}
    D -->|失败| E[重启容器]
    D -->|成功| F{readinessProbe 检查}
    F -->|失败| G[不分配流量]
    F -->|成功| H[分配流量]
```

**解释**：容器启动后，先用 `startupProbe` 检查是否启动完成；完成后用 `livenessProbe` 检查是否存活，如果存活再用 `readinessProbe` 检查是否可以接收流量。三者分工明确，确保容器从启动到运行都处于最佳状态。

### 健康检查语法与配置参数

健康检查是在 Pod 的 YAML 文件中配置的，写在容器（`containers`）下面。我们用最简单的方式解释语法和参数。

#### 基本语法结构

健康检查写在 `livenessProbe`、`readinessProbe` 或 `startupProbe` 字段下，支持三种检查方式：HTTP、TCP 和命令（Exec）。下面是一个简单的例子：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
  namespace: your-pinyin-name
spec:
  containers:
  - name: example-container
    image: nginx:1.14.2
    livenessProbe:  # 活性探测：检查是否存活
      httpGet:      # 用 HTTP 请求检查
        path: /     # 检查路径
        port: 80    # 检查端口
      initialDelaySeconds: 15  # 启动后等多久开始检查
      periodSeconds: 10        # 多久检查一次
      timeoutSeconds: 1        # 检查超时时间
      successThreshold: 1      # 成功几次算健康
      failureThreshold: 3      # 失败几次算不健康
```

#### 通用配置参数（详细解释）

不管用哪种检查方式，下面这些参数都会用到，决定了检查的“节奏”和“规则”：
- **`initialDelaySeconds`**：容器启动后等待多久才开始第一次检查（单位：秒）。比如设为 15，意思是容器启动 15 秒后才开始检查，避免容器还没准备好就被检查。默认是 0。
- **`periodSeconds`**：检查的频率（单位：秒）。比如设为 10，意思是每 10 秒检查一次。默认是 10。
- **`timeoutSeconds`**：每次检查的超时时间（单位：秒）。比如设为 1，意思是如果 1 秒内没返回结果，就算检查失败。默认是 1。
- **`successThreshold`**：连续成功几次才算“健康”或“就绪”。比如设为 1，意思是只要成功 1 次就通过。默认是 1。
- **`failureThreshold`**：连续失败几次才算“不健康”或“未就绪”。比如设为 3，意思是失败 3 次后 Kubernetes 会采取行动（重启或移除流量）。默认是 3。

**小贴士**：这些参数要根据你的应用特点调整。比如启动慢的应用，可以把 `initialDelaySeconds` 设长一点；`failureThreshold` 在 `startupProbe` 中可以设大一点，给更多时间。

#### 实践练习：基于 pod-stars-emmision 的健康检查配置

以下练习会逐步修改 `pod-stars-emmision.yml`，覆盖 HTTP、TCP、命令探测以及参数调整，每次修改后都会提供观察方法。

##### 练习 1：HTTP 探测（调整 livenessProbe 参数）
**目标**：修改 `livenessProbe` 参数，观察参数变化对检查的影响。
1. 修改 `pod-stars-emmision.yml`，将 `livenessProbe` 的参数调整为更短的延迟和频率：
   ```yaml
   livenessProbe:
     httpGet:
       path: /
       port: 80
     initialDelaySeconds: 5  # 缩短首次检查延迟
     periodSeconds: 5        # 缩短检查频率
     timeoutSeconds: 1
     successThreshold: 1
     failureThreshold: 3
   ```
2. 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
3. **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看 `livenessProbe` 检查是否更快触发，是否有失败记录。
4. **思考**：如果 `initialDelaySeconds` 设为 0，会发生什么？尝试修改并观察。

##### 练习 2：TCP 探测（替换 readinessProbe）
**目标**：将 `readinessProbe` 改为 TCP 探测，检查端口是否可用。
1. 修改 `pod-stars-emmision.yml`，将 `readinessProbe` 改为 TCP 探测：
   ```yaml
   readinessProbe:
     tcpSocket:
       port: 80
     initialDelaySeconds: 5
     periodSeconds: 5
     timeoutSeconds: 1
     successThreshold: 1
     failureThreshold: 3
   ```
2. 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
3. **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看 `readinessProbe` 是否成功。如果失败，可能是端口配置错误。
4. **思考**：如果把端口改为不存在的（如 8080），会怎样？尝试修改并观察事件变化。

##### 练习 3：命令探测（新增 startupProbe）
**目标**：添加 `startupProbe`，用命令探测检查进程是否存在。
1. 修改 `pod-stars-emmision.yml`，添加 `startupProbe`，检查是否存在特定进程（假设检查 `nginx` 进程，如果镜像不是 nginx，可改为其他命令）：
   ```yaml
   startupProbe:
     exec:
       command:
       - sh
       - -c
       - ps aux | grep nginx || ps aux | grep stars  # 检查 nginx 或 stars 相关进程
     initialDelaySeconds: 10
     periodSeconds: 5
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 30  # 给足够时间启动
   ```
2. 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
3. **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看 `startupProbe` 是否成功。如果失败，可能是命令不适合你的镜像，尝试调整命令。
4. **思考**：如果你的应用启动需要 2 分钟，怎么调整 `failureThreshold` 和 `initialDelaySeconds`？


#### 探测方式（三种方式+简单练习）

Kubernetes 支持三种检查方式，下面分别介绍，并附上简单的练习 YAML 文件，让你动手试试。

##### 1. **HTTP 探测（`httpGet`）**
- **作用**：通过 HTTP 请求检查某个路径，如果返回状态码是 200-399，就算成功。
- **适用**：Web 应用，比如检查 `/health` 路径是否正常。
- **参数**：
    - `path`：请求的路径，比如 `/health`。
    - `port`：请求的端口，比如 `80`。

- 修改 `pod-stars-emmision.yml`，同时配置三种探测：
   ```yaml
   livenessProbe:
     httpGet:
       path: /
       port: 80
     initialDelaySeconds: 15
     periodSeconds: 10
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 3
   readinessProbe:
     tcpSocket:
       port: 80
     initialDelaySeconds: 5
     periodSeconds: 5
     timeoutSeconds: 1
     successThreshold: 1
     failureThreshold: 3
   startupProbe:
     exec:
       command:
       - sh
       - -c
       - ps aux | grep nginx || ps aux | grep stars
     initialDelaySeconds: 10
     periodSeconds: 5
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 30
   ```
- 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl get pods -n your-pinyin-name
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
- **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看三种探测的检查结果，注意 `startupProbe` 是否先完成，`livenessProbe` 和 `readinessProbe` 是否随后生效。
- **思考**：如果 `startupProbe` 失败，会影响其他探测吗？观察事件日志分析原因。

##### 2. **TCP 探测（`tcpSocket`）**
- **作用**：检查某个端口是否能连接上，如果能连接就算成功。
- **适用**：非 HTTP 服务，比如数据库端口。
- **参数**：
- `port`：检查的端口，比如 `80`。
- 修改 `pod-stars-emmision.yml`，将 `readinessProbe` 改为 TCP 探测：
   ```yaml
   readinessProbe:
     tcpSocket:
       port: 80
     initialDelaySeconds: 5
     periodSeconds: 5
     timeoutSeconds: 1
     successThreshold: 1
     failureThreshold: 3
   ```
- 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
- **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看 `readinessProbe` 是否成功。如果失败，可能是端口配置错误。
- **思考**：如果把端口改为不存在的（如 8080），会怎样？尝试修改并观察事件变化。

##### 3. **命令探测（`exec`）**

- **作用**：在容器里跑一个命令，如果命令返回 0，就算成功。
- **适用**：自定义检查，比如检查某个进程是否存在。
- **参数**：
- `command`：要执行的命令，比如 `["ps", "aux"]`。
- **练习**：检查 nginx 进程是否存在。
- 修改 `pod-stars-emmision.yml`，添加 `startupProbe`，检查是否存在特定进程（假设检查 `nginx` 进程，如果镜像不是 nginx，可改为其他命令）：
   ```yaml
   startupProbe:
     exec:
       command:
       - sh
       - -c
       - ps aux | grep nginx || ps aux | grep stars  # 检查 nginx 或 stars 相关进程
     initialDelaySeconds: 10
     periodSeconds: 5
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 30  # 给足够时间启动
   ```
- 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
- **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看 `startupProbe` 是否成功。如果失败，可能是命令不适合你的镜像，尝试调整命令。
- **思考**：如果你的应用启动需要 2 分钟，怎么调整 `failureThreshold` 和 `initialDelaySeconds`？


#### 综合实践：三种探测一起用

下面是一个完整的例子，把三种探测都用上，模拟一个 Web 应用。创建文件 `pod-all-probes.yml`：
**目标**：结合 HTTP、TCP 和命令探测，观察三种探测的协同效果。
1. 修改 `pod-stars-emmision.yml`，同时配置三种探测：
   ```yaml
   livenessProbe:
     httpGet:
       path: /
       port: 80
     initialDelaySeconds: 15
     periodSeconds: 10
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 3
   readinessProbe:
     tcpSocket:
       port: 80
     initialDelaySeconds: 5
     periodSeconds: 5
     timeoutSeconds: 1
     successThreshold: 1
     failureThreshold: 3
   startupProbe:
     exec:
       command:
       - sh
       - -c
       - ps aux | grep nginx || ps aux | grep stars
     initialDelaySeconds: 10
     periodSeconds: 5
     timeoutSeconds: 2
     successThreshold: 1
     failureThreshold: 30
   ```
2. 重新部署并观察：
   ```bash
   kubectl apply -f pod-stars-emmision.yml
   kubectl get pods -n your-pinyin-name
   kubectl describe pod pod-stars-emmision -n your-pinyin-name
   ```
3. **Kuboard 观察**：在 Kuboard 的 Pod 详情页“事件（Events）”中，查看三种探测的检查结果，注意 `startupProbe` 是否先完成，`livenessProbe` 和 `readinessProbe` 是否随后生效。
4. **思考**：如果 `startupProbe` 失败，会影响其他探测吗？观察事件日志分析原因。

#### 常见问题与解决方法

- **容器频繁重启**：可能是 `livenessProbe` 的 `initialDelaySeconds` 太短或 `failureThreshold` 太小，增加这两个值试试。
- **流量未到达**：可能是 `readinessProbe` 失败，检查路径或端口是否正确。
- **启动探测失败**：确保 `startupProbe` 的命令或参数适合你的镜像，增加 `failureThreshold` 给更多时间。

**Kuboard 界面查看**：
登录 Kuboard，选择你的 Namespace，找到 `pod-all-probes`，点击进入详情页，在“事件（Events）”里查看检查结果。

#### 常见问题与小技巧

- **容器老是重启**：可能是 `livenessProbe` 检查太严格，把 `initialDelaySeconds` 设长点，`failureThreshold` 设大点。
- **流量不来**：可能是 `readinessProbe` 失败，检查路径和端口对不对。
- **启动慢被误判**：加个 `startupProbe`，给更多启动时间。
- **小技巧**：检查路径尽量用应用的健康接口（比如 `/health`），返回准确状态。

#### 总结

健康检查是 Kubernetes 确保容器正常运行的“体检工具”。通过 `livenessProbe` 检查容器是否存活，`readinessProbe` 检查是否可以接收流量，`startupProbe` 检查是否启动完成，三者配合让服务更稳定。配置时要根据应用特点调整检查参数，比如启动时间、频率等。


## 第五部分：ConfigMap 和 Secret——管理配置和敏感信息

### 1. ConfigMap 和 Secret 概述

#### 1.1 什么是 ConfigMap 和 Secret？
在 Kubernetes 中，应用的配置信息（如数据库地址、端口号）和敏感信息（如密码、密钥）不适合直接写在镜像或 Pod 定义中，因为这样不灵活也不安全。Kubernetes 提供了两种资源来解决这个问题：
- **ConfigMap**：用来存储非敏感的配置数据，比如应用的配置文件、环境变量等。想象它是一个“配置文件的收纳盒”，可以把配置信息集中管理，方便修改和复用。
- **Secret**：用来存储敏感信息，比如密码、API 密钥、证书等。想象它是一个“保险箱”，专门保护重要数据，避免泄露。

#### 1.2 为什么需要 ConfigMap 和 Secret？
- **解耦配置与代码**：如果把配置直接写在镜像里，每次改配置就要重新构建镜像，太麻烦。ConfigMap 和 Secret 让配置和代码分开，修改配置只需更新资源，不用动镜像。
- **安全性**：敏感信息（如密码）直接写在 Pod YAML 文件里容易泄露，Secret 提供了加密存储（Base64 编码，默认情况下），并可以通过权限控制限制访问。
- **复用性**：一个 ConfigMap 或 Secret 可以被多个 Pod 使用，方便统一管理配置。
- **灵活性**：支持多种方式加载配置，比如环境变量、文件挂载等，适应不同应用需求。

#### 1.3 ConfigMap 和 Secret 的区别与使用场景
- **ConfigMap 场景**：
  - 存储应用的配置文件，比如 Nginx 的 `nginx.conf`。
  - 设置环境变量，比如数据库连接地址 `DB_HOST=localhost`。
  - 统一管理多个 Pod 的公共配置，比如日志级别 `LOG_LEVEL=debug`。
- **Secret 场景**：
  - 存储数据库密码，比如 `DB_PASSWORD=admin123`。
  - 保存 API 密钥或令牌，比如 `API_KEY=xyz123`。
  - 提供 TLS 证书文件，用于 HTTPS 加密通信。

- **ConfigMap 和 Secret 的区别与使用场景**

  | 特性              | ConfigMap                       | Secret                          |
  |-------------------|---------------------------------|---------------------------------|
  | 存储内容          | 非敏感配置数据（如配置文件、环境变量） | 敏感信息（如密码、密钥、证书） |
  | 编码方式          | 明文存储                       | Base64 编码存储                |
  | 加密支持          | 不加密                         | 可配置加密（视集群配置）       |
  | 使用场景          | 应用程序配置、参数设置         | 数据库凭据、API 密钥、TLS 证书 |

#### 1.4 YAML 语法对齐说明（初学者必读）

在编写 Kubernetes 的 YAML 配置文件时，**缩进和对齐**非常重要，因为 YAML 是一种对缩进敏感的格式。以下是初学者需要注意的几点：

- **缩进层级：** 通常使用 2 个空格作为一级缩进（不要使用 Tab 键，因为 Tab 键在 YAML 中不被支持）。
- **对齐原则：** 同一层级的字段必须保持相同的缩进。例如，在 `spec` 下定义的 `containers` 和 `imagePullSecrets` 应该对齐；在 `containers` 下定义的 `name`、`image` 等字段也应该对齐。
- **嵌套结构：** 子字段比父字段多缩进一级。例如，`env` 是 `containers` 的子字段，所以 `env` 比 `containers` 多缩进 2 个空格。
- **示例对齐说明：** 在以下练习中，我会用注释标注对齐关系，确保您能看懂每个字段的位置。

如果缩进不对，Kubernetes 将无法解析 YAML 文件，导致应用失败。因此，编写时请仔细检查缩进，或者使用支持 YAML 语法高亮的编辑器（如 VSCode）来辅助编写。

**小贴士**：ConfigMap 适合存普通配置，Secret 适合存敏感数据。如果不确定用哪个，记住“涉及密码或密钥就用 Secret”。

### 2. ConfigMap 和 Secret 的创建与引入/挂载教学

ConfigMap 和 Secret 是 Kubernetes 中用于管理配置和敏感信息的两种资源。以下将分别对 ConfigMap 的两种用法（环境变量配置和文件配置）以及 Secret 的三种用法（环境变量配置、Harbor 登录配置和 HTTPS 证书配置）进行详细教学，每种用法都会包含创建方法（统一使用 YAML 和命令行方式）和引入/挂载到 Pod 的方式。

**注意**：文件命名规范要求外部文件名与内部 `metadata.name` 保持一致，例如 ConfigMap 的名称是 `configmap-app-env`，则文件名应为 `configmap-app-env.yml`。

#### 2.1 ConfigMap - 环境变量配置（env 配置）

- **用途**：将配置数据以环境变量的形式注入到 Pod 中，适合简单的键值对配置。
- **创建方法 - 语法说明**：
  ConfigMap 可以通过 YAML 文件定义，基本结构如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: ConfigMap  # 资源类型，这里是 ConfigMap
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: configmap-app-env  # ConfigMap 的名称，与文件名保持一致
  data:  # 配置数据以键值对形式存储
    key1: value1  # 键值对形式，环境变量名和值
    key2: value2
  ```

- **创建方法 - 具体示例**：
  创建一个名为 `configmap-app-env.yml` 的文件，内容如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: ConfigMap  # 资源类型，这里是 ConfigMap
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: configmap-app-env  # ConfigMap 的名称，与文件名保持一致
  data:  # 配置数据以键值对形式存储
    DB_HOST: mysql-service
    DB_PORT: "3306"
    LOG_LEVEL: info
  ```
  使用以下命令应用该文件：
  ```bash
  kubectl apply -f configmap-app-env.yml
  ```

- **引入到 Pod - 语法说明**：
  在 Pod 的 YAML 文件中，可以使用 `envFrom` 引用整个 ConfigMap 中的所有键值对作为环境变量，基本结构如下：
  ```yaml
  envFrom:  # 定义环境变量，从 ConfigMap 中引入所有键值对
  - configMapRef:
      name: configmap-app-env  # ConfigMap 名称
  ```
  **关于 `configMapKeyRef` 的说明**：除了 `envFrom` 一次性引入所有环境变量外，也可以使用 `configMapKeyRef` 单独引用 ConfigMap 中的某个键值对，语法如下：
  ```yaml
  env:  # 定义环境变量，从 ConfigMap 中引入
  - name: DB_HOST  # 环境变量名
    valueFrom:  # 使用 valueFrom 引用外部资源
      configMapKeyRef:
        name: configmap-app-env  # ConfigMap 名称
        key: DB_HOST  # ConfigMap 中的键
  ```
  由于 `configMapKeyRef` 需要逐个指定键值对，操作较为繁琐，因此本教程主要推荐使用 `--from-env-file` 和 `envFrom` 的方式一次性导入所有环境变量。

- **引入到 Pod - 具体示例**：
  引用位置在 Pod 的 `spec.containers.envFrom` 字段中，完整 Pod 配置如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      envFrom:  # 定义环境变量，从 ConfigMap 中引入所有键值对
      - configMapRef:
          name: configmap-app-env  # ConfigMap 名称
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```

- **查看信息 - 具体示例**：
  1. 列出命名空间中的所有 ConfigMap：
     ```bash
     kubectl get configmaps -n your-pinyin-name
     ```
  2. 查看 `configmap-app-env` 的详细信息：
     ```bash
     kubectl describe configmap configmap-app-env -n your-pinyin-name
     ```
  3. 查看 `configmap-app-env` 的内容：
     ```bash
     kubectl get configmap configmap-app-env -o yaml -n your-pinyin-name
     ```

#### 2.2 ConfigMap - 文件配置（文件挂载）

- **用途**：将配置数据以文件的形式挂载到 Pod 中，适合复杂的配置文件内容。
- **创建方法 - 语法说明**：
  ConfigMap 可以通过 YAML 文件定义，基本结构如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: ConfigMap  # 资源类型，这里是 ConfigMap
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: configmap-app-file  # ConfigMap 的名称，与文件名保持一致
  data:  # 配置数据以键值对形式存储
    filename: |  # 使用 | 表示多行文本，模拟一个配置文件
      content line 1
      content line 2
  ```
  使用 `kubectl apply -f` 命令应用 YAML 文件创建 ConfigMap。

- **创建方法 - 具体示例**：
  创建一个名为 `configmap-app-file.yml` 的文件，内容如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: ConfigMap  # 资源类型，这里是 ConfigMap
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: configmap-app-file  # ConfigMap 的名称，与文件名保持一致
  data:  # 配置数据以键值对形式存储
    config.txt: |  # 使用 | 表示多行文本，模拟一个配置文件
      server {
        host: localhost
        port: 8080
      }
  ```
  使用以下命令应用该文件：
  ```bash
  kubectl apply -f configmap-app-file.yml
  ```

- **挂载到 Pod - 语法说明**：
  在 Pod 的 YAML 文件中，使用 `volumes` 和 `volumeMounts` 挂载 ConfigMap，基本结构如下：
  ```yaml
  volumeMounts:  # 定义挂载点
  - name: volume-configmap-app-file
    mountPath: /etc/config  # 挂载路径，容器内可访问的目录
  volumes:  # 定义卷，引用 ConfigMap
  - name: volume-configmap-app-file
    configMap:
      name: configmap-app-file  # ConfigMap 名称
  ```

- **挂载到 Pod - 具体示例**：
  引用位置在 Pod 的 `spec.containers.volumeMounts` 和 `spec.volumes` 字段中，完整 Pod 配置如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      volumeMounts:  # 定义挂载点，将 ConfigMap 挂载为文件
      - name: volume-configmap-app-file  # 挂载 ConfigMap 文件配置
        mountPath: /etc/config
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    volumes:  # 定义卷，引用 ConfigMap
    - name: volume-configmap-app-file  # 卷名称，与 container 中的 volumeMounts 对应
      configMap:
        name: configmap-app-file  # ConfigMap 名称
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```

- **查看信息 - 具体示例**：
  1. 列出命名空间中的所有 ConfigMap：
     ```bash
     kubectl get configmaps -n your-pinyin-name
     ```
  2. 查看 `configmap-app-file` 的详细信息：
     ```bash
     kubectl describe configmap configmap-app-file -n your-pinyin-name
     ```
  3. 查看 `configmap-app-file` 的内容：
     ```bash
     kubectl get configmap configmap-app-file -o yaml -n your-pinyin-name
     ```

#### 2.3 Secret - 环境变量配置（env 配置）

- **用途**：将敏感数据以环境变量的形式注入到 Pod 中，适合简单的密码或密钥。
- **创建方法 - 语法说明**：
  Secret 可以通过 YAML 文件定义，使用 `stringData` 字段以明文方式输入数据，Kubernetes 会自动转换为 Base64 编码。基本结构如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-app-env  # Secret 的名称，与文件名保持一致
  type: Opaque  # Secret 类型，Opaque 表示通用类型
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    key1: value1
    key2: value2
  ```
  或者使用命令行方式通过 `--from-env-file` 创建 Secret，适合从环境变量文件快速导入配置。

- **创建方法 - 具体示例**：
  创建一个名为 `secret-app-env.yml` 的文件，内容如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-app-env  # Secret 的名称，与文件名保持一致
  type: Opaque  # Secret 类型，Opaque 表示通用类型
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    DB_PASSWORD: admin123
    API_KEY: xyz789
  ```
  使用以下命令应用该文件：
  ```bash
  kubectl apply -f secret-app-env.yml
  ```

- **引入到 Pod - 语法说明**：
  在 Pod 的 YAML 文件中，使用 `envFrom` 引用 Secret 中的所有键值对作为环境变量，基本结构如下：
  ```yaml
  envFrom:  # 定义环境变量，从 Secret 中引入所有键值对
  - secretRef:
      name: secret-app-env  # Secret 名称
  ```

- **引入到 Pod - 具体示例**：
  引用位置在 Pod 的 `spec.containers.envFrom` 字段中，完整 Pod 配置如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      envFrom:  # 定义环境变量，从 Secret 中引入所有键值对
      - secretRef:
          name: secret-app-env  # Secret 名称
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```

- **查看信息 - 具体示例**：
  1. 列出命名空间中的所有 Secret：
     ```bash
     kubectl get secrets -n your-pinyin-name
     ```
  2. 查看 `secret-app-env` 的详细信息：
     ```bash
     kubectl describe secret secret-app-env -n your-pinyin-name
     ```
  3. 查看 `secret-app-env` 的内容（Base64 编码）：
     ```bash
     kubectl get secret secret-app-env -o yaml -n your-pinyin-name
     ```
  4. 解码 `DB_PASSWORD` 以查看明文：
     ```bash
     kubectl get secret secret-app-env -o jsonpath='{.data.DB_PASSWORD}' -n your-pinyin-name | base64 -d


#### 2.4 Secret - Harbor 登录配置（镜像拉取）

- **用途**：用于存储镜像仓库的登录凭据，以便 Pod 拉取私有镜像。
- **创建方法 - 语法说明**：
  Secret 可以通过 YAML 文件定义，用于 Docker 镜像仓库登录的 Secret 类型为 `kubernetes.io/dockerconfigjson`，基本结构如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-harbor-login  # Secret 的名称，与文件名保持一致
  type: kubernetes.io/dockerconfigjson  # Secret 类型，用于镜像仓库登录
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    .dockerconfigjson: |  # Docker 配置 JSON 格式，包含镜像仓库登录信息
      {
        "auths": {
          "harbor.labworlds.cc": {
            "username": "your-username",
            "password": "your-password",
            "email": "your-email@example.com",
            "auth": "base64-encoded-auth-string"  # 可选，Kubernetes 会自动生成
          }
        }
      }
  ```
  使用 `kubectl apply -f` 命令应用 YAML 文件创建 Secret。

- **创建方法 - 具体示例**：
  创建一个名为 `secret-harbor-login.yml` 的文件，内容如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-harbor-login  # Secret 的名称，与文件名保持一致
  type: kubernetes.io/dockerconfigjson  # Secret 类型，用于镜像仓库登录
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    .dockerconfigjson: |  # Docker 配置 JSON 格式，包含镜像仓库登录信息
      {
        "auths": {
          "harbor.labworlds.cc": {
            "username": "your-username",  # 替换为你的 Harbor 用户名
            "password": "your-password",  # 替换为你的 Harbor 密码
          }
        }
      }
  ```
  使用以下命令应用该文件：
  ```bash
  kubectl apply -f secret-harbor-login.yml
  ```

- **引入到 Pod - 语法说明**：
  在 Pod 的 YAML 文件中，使用 `imagePullSecrets` 引用 Secret，基本结构如下：
  ```yaml
  imagePullSecrets:  # 指定用于拉取镜像的 Secret
  - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```

- **引入到 Pod - 具体示例**：
  引用位置在 Pod 的 `spec.imagePullSecrets` 字段中，完整 Pod 配置如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```

- **查看信息 - 具体示例**：
  1. 列出命名空间中的所有 Secret：
     ```bash
     kubectl get secrets -n your-pinyin-name
     ```
  2. 查看 `secret-harbor-login` 的详细信息：
     ```bash
     kubectl describe secret secret-harbor-login -n your-pinyin-name
     ```
  3. 查看 `secret-harbor-login` 的内容（Base64 编码）：
     ```bash
     kubectl get secret secret-harbor-login -o yaml -n your-pinyin-name
     ```

#### 2.5 Secret - HTTPS 证书配置（证书挂载）

- **用途**：将 HTTPS 证书以文件形式挂载到 Pod 中，适合需要 TLS 加密的场景。
- **创建方法 - 语法说明**：
  Secret 可以通过 YAML 文件定义，用于 TLS 证书的 Secret 类型为 `kubernetes.io/tls`，基本结构如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-domain  # Secret 的名称，与文件名保持一致
  type: kubernetes.io/tls  # Secret 类型，专门用于 TLS 证书
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    tls.crt: |  # 证书文件内容
      certificate content
    tls.key: |  # 私钥文件内容
      private key content
  ```
  使用 `kubectl apply -f` 命令应用 YAML 文件创建 Secret。

- **创建方法 - 具体示例**：
  创建一个名为 `secret-domain.yml` 的文件，内容如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Secret  # 资源类型，这里是 Secret
  metadata:
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
    name: secret-domain  # Secret 的名称，与文件名保持一致
  type: kubernetes.io/tls  # Secret 类型，专门用于 TLS 证书
  stringData:  # 使用 stringData 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64
    tls.crt: |  # 证书文件内容（示例，实际替换为真实证书）
      -----BEGIN CERTIFICATE-----
      MIID... (证书内容)
      -----END CERTIFICATE-----
    tls.key: |  # 私钥文件内容（示例，实际替换为真实私钥）
      -----BEGIN PRIVATE KEY-----
      MIIE... (私钥内容)
      -----END PRIVATE KEY-----
  ```
  使用以下命令应用该文件：
  ```bash
  kubectl apply -f secret-domain.yml
  ```

- **挂载到 Pod - 语法说明**：
  在 Pod 的 YAML 文件中，使用 `volumes` 和 `volumeMounts` 挂载 Secret，基本结构如下：
  ```yaml
  volumeMounts:  # 定义挂载点
  - name: volume-secret-domain
    mountPath: /etc/ssl  # 挂载路径，容器内可访问的目录
  volumes:  # 定义卷，引用 Secret
  - name: volume-secret-domain
    secret:
      secretName: secret-domain  # Secret 名称
  ```

- **挂载到 Pod - 具体示例**：
  引用位置在 Pod 的 `spec.containers.volumeMounts` 和 `spec.volumes` 字段中，完整 Pod 配置如下：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      volumeMounts:  # 定义挂载点，将 Secret 挂载为文件
      - name: volume-secret-domain  # 挂载 Secret HTTPS 证书
        mountPath: /etc/ssl
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    volumes:  # 定义卷，引用 Secret
    - name: volume-secret-domain  # 卷名称，与 container 中的 volumeMounts 对应
      secret:
        secretName: secret-domain  # Secret 名称
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称
  ```
- **查看信息 - 具体示例**：
  1. 列出命名空间中的所有 Secret：
     ```bash
     kubectl get secrets -n your-pinyin-name
     ```
  2. 查看 `secret-domain` 的详细信息：
     ```bash
     kubectl describe secret secret-domain -n your-pinyin-name
     ```
  3. 查看 `secret-domain` 的内容（Base64 编码）：
     ```bash
     kubectl get secret secret-domain -o yaml -n your-pinyin-name


### 3. 总结表格：ConfigMap 和 Secret 常用命令

以下是 ConfigMap 和 Secret 的常用命令总结表格，方便日后快速参考：

| **资源类型**          | **操作**                          | **命令**                                                                                     | **示例（假设命名空间为 `your-pinyin-name`）**                                      |
|-----------------------|----------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **ConfigMap**         | 列出所有 ConfigMap              | `kubectl get configmaps -n <namespace>`                                                    | `kubectl get configmaps -n your-pinyin-name`                              |
|                       | 查看详细信息                    | `kubectl describe configmap <configmap-name> -n <namespace>`                               | `kubectl describe configmap configmap-app-env -n your-pinyin-name`       |
|                       | 查看内容（YAML 格式）           | `kubectl get configmap <configmap-name> -o yaml -n <namespace>`                            | `kubectl get configmap configmap-app-env -o yaml -n your-pinyin-name`    |
| **Secret**            | 列出所有 Secret                 | `kubectl get secrets -n <namespace>`                                                       | `kubectl get secrets -n your-pinyin-name`                                 |
|                       | 查看详细信息                    | `kubectl describe secret <secret-name> -n <namespace>`                                     | `kubectl describe secret secret-app-env -n your-pinyin-name`             |
|                       | 查看内容（YAML 格式，Base64）   | `kubectl get secret <secret-name> -o yaml -n <namespace>`                                  | `kubectl get secret secret-app-env -o yaml -n your-pinyin-name`          |
|                       | 解码数据查看明文                | `kubectl get secret <secret-name> -o jsonpath='{.data.<key>}' -n <namespace> | base64 -d` | `kubectl get secret secret-app-env -o jsonpath='{.data.DB_PASSWORD}' -n your-pinyin-name | base64 -d` |
| **Pod**               | 列出所有 Pod                    | `kubectl get pods -n <namespace>`                                                          | `kubectl get pods -n your-pinyin-name`                                    |
|                       | 查看详细信息                    | `kubectl describe pod <pod-name> -n <namespace>`                                           | `kubectl describe pod pod-stars-emmision -n your-pinyin-name`            |
|                       | 查看日志                        | `kubectl logs <pod-name> -n <namespace>`                                                   | `kubectl logs pod-stars-emmision -n your-pinyin-name`                    |
|                       | 进入容器                        | `kubectl exec -it <pod-name> -n <namespace> -- /bin/bash` 或 `/bin/sh`                     | `kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash`   |

### 4. 综合练习：将 5 种配置全部挂载到 Pod 并验证

以下是一个完整的 Pod 配置示例，将上述 5 种配置（2 种 ConfigMap 和 3 种 Secret）全部引入或挂载到一个 Pod 中，并说明如何进入容器验证以及使用 Kuboard 查看资源。

- **Pod YAML 配置示例**：
  创建一个名为 `pod-stars-emmision.yml` 的文件，内容如下（文件名与 `metadata.name` 保持一致）：
  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
    - name: stars-emmision  # 容器的名称
      image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
      ports:  # 指定容器暴露的端口
      - containerPort: 80  # 容器内部使用的端口号，这里是 80
      envFrom:  # 定义环境变量，从 ConfigMap 和 Secret 中引入所有键值对
      - configMapRef:
          name: configmap-app-env  # ConfigMap 名称，来自 configmap-app-env.yml
      - secretRef:
          name: secret-app-env  # Secret 名称，来自 secret-app-env.yml
      volumeMounts:  # 定义挂载点，将 ConfigMap 和 Secret 挂载为文件
      - name: volume-configmap-app-file  # 挂载 ConfigMap 文件配置，来自 configmap-app-file.yml
        mountPath: /etc/config
      - name: volume-secret-domain  # 挂载 Secret HTTPS 证书，来自 secret-domain.yml
        mountPath: /etc/ssl
      livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
      readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
        httpGet:  # 使用 HTTP GET 请求进行探测
          path: /  # 请求的路径，这里是根路径
          port: 80  # 请求的端口，这里是 80
        initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
        periodSeconds: 10  # 每 10 秒进行一次探测
    volumes:  # 定义卷，引用 ConfigMap 和 Secret
    - name: volume-configmap-app-file  # 卷名称，与 container 中的 volumeMounts 对应，来自 configmap-app-file.yml
      configMap:
        name: configmap-app-file  # ConfigMap 名称
    - name: volume-secret-domain  # 卷名称，与 container 中的 volumeMounts 对应，来自 secret-domain.yml
      secret:
        secretName: secret-domain  # Secret 名称
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
    - name: secret-harbor-login  # 引用之前创建的 Secret 名称，来自 secret-harbor-login.yml
  ```
  使用命令应用该文件：
  ```bash
  kubectl apply -f pod-stars-emmision.yml
  ```

- **进入容器验证配置是否生效**：
  1. 获取 Pod 名称和状态，确保 Pod 运行正常：
     ```bash
     kubectl get pods -n your-pinyin-name
     ```
  2. 进入 Pod 的容器：
     ```bash
     kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash
     ```
     如果镜像不支持 `/bin/bash`，可以尝试 `/bin/sh`：
     ```bash
     kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/sh
     ```
  3. 验证环境变量是否注入：
     检查 `DB_HOST` 和 `DB_PASSWORD` 是否存在：
     ```bash
     echo $DB_HOST  # 应输出 mysql-service，来自 configmap-app-env.yml
     echo $DB_PASSWORD  # 应输出 admin123，来自 secret-app-env.yml
     ```
     如果输出对应值，说明环境变量引入成功。
  4. 验证文件挂载是否生效：
     检查 ConfigMap 文件配置：
     ```bash
     ls /etc/config  # 应看到 config.txt 文件，来自 configmap-app-file.yml
     cat /etc/config/config.txt  # 应输出配置文件内容
     ```
     检查 Secret HTTPS 证书：
     ```bash
     ls /etc/ssl  # 应看到 tls.crt 和 tls.key 文件，来自 secret-domain.yml
     cat /etc/ssl/tls.crt  # 应输出证书内容
     cat /etc/ssl/tls.key  # 应输出私钥内容
     ```
     如果能看到对应文件内容，说明挂载成功。
  5. 退出容器：
     ```bash
     exit
     ```

- **使用 Kuboard 查看资源**：
  1. 登录 Kuboard 界面（假设你已安装 Kuboard，通常通过浏览器访问集群的 Kuboard 服务地址）。
  2. 在左侧导航栏选择你的 Namespace（例如 `your-pinyin-name`）。
  3. 查看 Pod：
     - 进入“工作负载” -> “Pod”，找到 `pod-stars-emmision`，点击查看详情，确认 Pod 状态为 Running。
  4. 查看 ConfigMap：
     - 进入“配置” -> “ConfigMap”，找到 `configmap-app-env` 和 `configmap-app-file`，点击查看数据内容。
  5. 查看 Secret：
     - 进入“配置” -> “Secret”，找到 `secret-app-env`、`secret-harbor-login` 和 `secret-domain`，点击查看数据（注意 Secret 数据会以掩码形式显示，需解码查看明文）。
  6. 确认 Pod 配置：
     - 在 Pod 详情页中，查看“环境变量”和“挂载点”，确认是否引用了对应的 ConfigMap 和 Secret。

### 4. 总结与注意事项

- **文件命名规范**：外部文件名必须与内部 `metadata.name` 保持一致，例如 ConfigMap 名称是 `configmap-app-env`，则文件名为 `configmap-app-env.yml`。
- **YAML 缩进检查**：编写 YAML 文件时务必注意缩进，建议使用支持语法高亮的编辑器（如 VSCode）辅助编写。
- **Secret 明文编写**：Secret 可以使用 `stringData` 字段以明文方式定义数据，Kubernetes 会自动编码为 Base64。
- **Secret 安全性**：Secret 默认仅 Base64 编码，不等于加密，敏感数据需结合集群加密机制或权限控制保护。
- **验证配置**：创建 Pod 后，务必进入容器验证环境变量和文件挂载是否生效；同时可借助 Kuboard 等可视化工具查看资源状态。
- **环境变量导入方式**：本教程推荐使用 `--from-env-file` 创建 ConfigMap 和 Secret，并通过 `envFrom` 一次性引入所有环境变量，简化操作流程。

**小贴士**：ConfigMap 和 Secret 是 Kubernetes 配置管理的核心工具，掌握它们的创建和使用方式，能大大提升应用的灵活性和安全性。通过本练习，逐步熟悉各种配置的引入和挂载方式，确保在实际场景中能够灵活应用。


## 第六部分 Pod 资源限制与配置示例

### 1. Pod 资源限制的理论介绍
在 Kubernetes 中，为 Pod 设置资源限制是确保集群资源合理分配和应用稳定运行的重要手段。资源限制主要通过 `requests` 和 `limits` 两个字段来定义，分别表示容器运行所需的最低资源量和最大资源量。合理设置这些参数可以防止某个 Pod 占用过多资源，同时保证关键应用获得足够的资源支持。关于资源限制的详细理论介绍，请参考前文内容，这里不再赘述。

### 2. 为什么要使用 `requests` 和 `limits` 以及两者的含义
- **为什么要使用 `requests` 和 `limits`**：
  - **资源公平分配**：通过设置 `requests` 和 `limits`，可以确保集群资源合理分配，避免某个 Pod 占用过多资源导致其他 Pod 无法正常运行。
  - **应用稳定性**：合理设置资源限制可以防止容器因资源不足而崩溃，或因资源过剩而浪费。
  - **集群稳定性**：资源限制有助于保护集群整体稳定性，避免某个 Pod 的异常行为（如内存泄漏）影响其他 Pod 或节点。
- **`requests` 的含义**：资源请求，表示容器运行所需的最低资源量（CPU 和内存）。Kubernetes 在调度 Pod 时，会根据 `requests` 值选择合适的节点，确保节点有足够的资源满足 Pod 的最低需求。如果集群资源不足，Pod 将处于 `Pending` 状态。
- **`limits` 的含义**：资源限制，表示容器可以使用的最大资源量（CPU 和内存）。当容器尝试使用超出 `limits` 定义的资源时，Kubernetes 会采取限制措施，例如对 CPU 进行节流（throttling），或在内存超限时终止容器（OOMKilled）。


### 3. Pod 资源限制语法
在 Kubernetes 中，Pod 的资源限制通过 `spec.containers[].resources` 字段定义，主要包含 `requests` 和 `limits` 两个子字段，用于指定容器运行所需的最低资源量和最大资源量。以下是资源限制的 YAML 语法结构：

```yaml
spec:
  containers:
  - name: <容器名称>
    image: <镜像名称>
    resources:
      requests:  # 资源请求，表示容器运行所需的最低资源量
        cpu: "<CPU 核心数或毫核数>"  # 例如 "0.2" 或 "200m"
        memory: "<内存大小>"  # 例如 "256Mi" 或 "1Gi"
      limits:  # 资源限制，表示容器可使用的最大资源量
        cpu: "<CPU 核心数或毫核数>"  # 例如 "0.5" 或 "500m"
        memory: "<内存大小>"  # 例如 "512Mi" 或 "2Gi"
```

- **CPU 单位**：可以是小数（如 `0.5` 表示半个核心）或毫核（如 `500m` 表示 0.5 核心）。
- **内存单位**：支持 `Mi`（兆字节）、`Gi`（吉字节）等单位，例如 `512Mi` 表示 512 兆字节。


### 2. 练习 Pod YAML 文件
以下是一个完整的 Pod YAML 配置示例，包含了资源限制、探针配置以及镜像拉取秘钥等内容，供学员参考和学习。此示例严格遵循企业命名规范，并添加了详细注释以便理解：

- 创建一个名为 `pod-stars-emmision.yml` 的文件，内容如下（文件名与 `metadata.name` 保持一致）：

  ```yaml
  apiVersion: v1  # 指定 Kubernetes API 的版本
  kind: Pod  # 资源类型，这里是 Pod
  metadata:
    name: pod-stars-emmision  # Pod 的名称，符合企业标准，文件名应为 pod-stars-emmision.yml
    namespace: your-pinyin-name  # 替换为你的 Namespace 名称，例如 zhangwei
  spec:
    containers:  # 定义 Pod 中的容器
      - name: stars-emmision  # 容器的名称，与应用名保持一致
        image: harbor.labworlds.cc/stars-emmision/master:08061743-shiqi  # 替换为你的镜像标签
        ports:  # 指定容器暴露的端口
          - containerPort: 80  # 容器内部使用的端口号，这里是 80
        resources:  # 定义容器的资源限制
          requests:  # 资源请求，表示容器运行所需的最低资源量
            cpu: "0.2"  # 最低需要 0.2 个 CPU 核心
            memory: "256Mi"  # 最低需要 256Mi 内存
          limits:  # 资源限制，表示容器可使用的最大资源量
            cpu: "0.5"  # 最多可以使用 0.5 个 CPU 核心
            memory: "512Mi"  # 最多可以使用 512Mi 内存
        livenessProbe:  # 活性探测配置，用于检查容器是否正常运行
          httpGet:  # 使用 HTTP GET 请求进行探测
            path: /  # 请求的路径，这里是根路径
            port: 80  # 请求的端口，这里是 80
          initialDelaySeconds: 30  # 在容器启动后，等待 30 秒再进行第一次探测
          periodSeconds: 10  # 每 10 秒进行一次探测
        readinessProbe:  # 就绪探测配置，用于检查容器是否可以接收流量
          httpGet:  # 使用 HTTP GET 请求进行探测
            path: /  # 请求的路径，这里是根路径
            port: 80  # 请求的端口，这里是 80
          initialDelaySeconds: 5  # 在容器启动后，等待 5 秒再进行第一次探测
          periodSeconds: 10  # 每 10 秒进行一次探测
    imagePullSecrets:  # 指定用于拉取镜像的 Secret
      - name: secret-harbor-login  # 引用之前创建的 Secret 名称，用于私有镜像仓库登录
  ```

- 使用以下命令应用该文件：
  ```bash
  kubectl apply -f pod-stars-emmision.yml
  ```

- 查看pod-stars-emmision的状态
  ```bash
  kubectl get pod pod-stars-emmision -n your-pinyin-name
  ```

- 查看pod-stars-emmision的详情
  ```bash
  kubectl describe pod pod-stars-emmision -n your-pinyin-name
  ```

### 4. Mermaid 图表示 Pod 资源限制结构
由于当前环境不支持直接渲染 Mermaid 图表，我以代码形式提供 Pod 资源限制的层级结构图，学员可使用支持 Mermaid 的工具（如 Markdown 编辑器）查看：

```mermaid
graph TD
    Pod --> Spec
    Spec --> Containers
    Containers --> Container1[Container 1]
    Container1 --> Resources
    Resources --> Requests
    Resources --> Limits
    Requests --> CPU_Requests[CPU]
    Requests --> Memory_Requests[Memory]
    Limits --> CPU_Limits[CPU]
    Limits --> Memory_Limits[Memory]
    Container1 --> LivenessProbe
    Container1 --> ReadinessProbe
    Container1 --> Ports
    Spec --> ImagePullSecrets
```

此图展示了 Pod 中与资源限制相关的层级结构，包括 `requests` 和 `limits` 的 CPU 和内存配置，以及探针和镜像拉取秘钥等相关字段。


## 第七部分 Pod YAML 结构与规范

### 1. 完整 Pod 结构与理论介绍
Pod 是 Kubernetes 中最小的可调度单位，代表一个或多个容器的集合，这些容器共享网络、存储和生命周期。Pod 的设计目的是运行一个单一的应用程序实例，通常一个 Pod 包含一个主容器，偶尔也可能包含辅助容器（例如日志收集或代理服务）。Pod 的配置通过 YAML 文件定义，YAML 文件以键值对的形式描述 Pod 的属性和行为，具有严格的语法要求（缩进一致，通常为 2 个空格，不允许使用制表符）。

#### 理论介绍
Pod 的 YAML 文件主要由以下几个核心部分组成：
- **apiVersion**：指定 Kubernetes API 的版本，例如 `v1`，用于定义 Pod。
- **kind**：指定资源类型，这里为 `Pod`。
- **metadata**：包含 Pod 的元数据，例如名称（name）、命名空间（namespace）、标签（labels）、注解（annotations）等，用于标识和管理 Pod。
- **spec**：定义 Pod 的具体配置，是 YAML 文件的核心部分，包含容器（containers）、镜像（image）、端口（ports）、资源限制（resources）、环境变量（env）、挂载（volumes）、重启策略（restartPolicy）等。
- **status**：Pod 的运行状态信息，通常由 Kubernetes 自动生成，不需要在 YAML 文件中手动定义。

Pod 的生命周期由 Kubernetes 管理，从创建、运行到销毁，Pod 内的所有容器作为一个整体被调度到同一节点上，共享 IP 地址和端口空间。Pod 的设计简单而灵活，但也因此存在局限性（后文会提及）。

以下是一个完整的 Pod YAML 示例，包含常见配置字段：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-my-app
  namespace: default
  labels:
    app: my-app
  annotations:
    description: "This is a sample pod"
spec:
  restartPolicy: Always
  containers:
  - name: my-container
    image: nginx:1.14.2
    ports:
    - containerPort: 80
      protocol: TCP
    env:
    - name: ENV_VAR
      value: "value1"
    resources:
      limits:
        cpu: "0.5"
        memory: "512Mi"
      requests:
        cpu: "0.2"
        memory: "256Mi"
    livenessProbe:
      httpGet:
        path: /health
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 10
    volumeMounts:
    - name: temp-data
      mountPath: /tmp/data
  volumes:
  - name: temp-data
    emptyDir: {}
```

### 2. Pod 结构图或表格
为了帮助学员更好地理解如何编写一个 Pod YAML 文件，我以表格形式展示其关键字段和说明，方便快速掌握结构：

| 字段路径                              | 示例值                          | 说明                                      |
|---------------------------------------|---------------------------------|-------------------------------------------|
| `apiVersion`                          | `v1`                           | 指定 API 版本                            |
| `kind`                                | `Pod`                          | 资源类型为 Pod                           |
| `metadata.name`                       | `pod-my-app`                   | Pod 的名称，需符合命名规范               |
| `metadata.namespace`                  | `default`                      | Pod 所在的命名空间                       |
| `metadata.labels`                     | `app: my-app`                  | Pod 的标签，用于筛选和管理               |
| `metadata.annotations`                | `description: "Sample pod"`    | Pod 的注解，用于添加额外描述信息         |
| `spec.restartPolicy`                  | `Always`                       | 重启策略（Always, OnFailure, Never）     |
| `spec.containers[].name`              | `my-container`                 | 容器名称                                 |
| `spec.containers[].image`             | `nginx:1.14.2`                | 容器使用的镜像及其标签                   |
| `spec.containers[].ports[].containerPort` | `80`                       | 容器暴露的端口                           |
| `spec.containers[].env[].name`        | `ENV_VAR`                      | 环境变量名称                             |
| `spec.containers[].env[].value`       | `value1`                       | 环境变量值                               |
| `spec.containers[].resources.limits`  | `cpu: "0.5", memory: "512Mi"`  | 容器资源限制（CPU 和内存）               |
| `spec.containers[].resources.requests`| `cpu: "0.2", memory: "256Mi"`  | 容器资源请求（最低需求）                 |
| `spec.containers[].livenessProbe`     | `httpGet: {path: /health, port: 80}` | 存活探针，检查容器是否健康       |
| `spec.containers[].volumeMounts[].name`| `temp-data`                   | 引用卷的名称                             |
| `spec.containers[].volumeMounts[].mountPath`| `/tmp/data`             | 容器内的挂载路径                         |
| `spec.volumes[].name`                 | `temp-data`                    | 卷的名称                                 |
| `spec.volumes[].emptyDir`             | `{}`                           | 定义一个临时目录卷，Pod 销毁后数据丢失   |

如果需要更直观的结构图，可以使用 Mermaid 流程图来表示 Pod 的层级结构（由于当前环境不支持直接渲染 Mermaid，我以代码形式提供，学员可使用支持 Mermaid 的工具查看）：
```mermaid
graph TD
    Pod --> Metadata
    Pod --> Spec
    Metadata --> Name
    Metadata --> Namespace
    Metadata --> Labels
    Metadata --> Annotations
    Spec --> RestartPolicy
    Spec --> Containers
    Spec --> Volumes
    Containers --> Container1[Container 1]
    Container1 --> Image
    Container1 --> Ports
    Container1 --> Env
    Container1 --> Resources
    Container1 --> Probes
    Container1 --> VolumeMounts
    Resources --> Limits
    Resources --> Requests
    Volumes --> Volume1[Volume 1]
    Volume1 --> EmptyDir
```

### 3. 命名定义规范
在 Kubernetes 中，YAML 文件的命名和文件中定义的资源名称必须严格保持一致，以提高可读性和管理效率。具体规范如下：
- YAML 文件名应采用 `类型-应用名.yml` 的格式，例如：
  - 创建 Pod 配置时，文件名为 `pod-my-app.yml`，其中 `pod` 表示资源类型，`my-app` 是应用名。
  - 创建 ConfigMap 配置时，文件名为 `configmap-my-app.yml`，其中 `configmap` 表示资源类型，`my-app` 是应用名。
- YAML 文件中 `metadata.name` 字段的值必须与文件名中的完整名称一致，例如：
  - 文件名为 `pod-my-app.yml`，则 `metadata.name` 必须是 `pod-my-app`。
  - 文件名为 `configmap-my-app.yml`，则 `metadata.name` 必须是 `configmap-my-app`。
- 文件扩展名统一使用 `.yml`，团队内需保持一致。

这一规范确保了文件系统中的资源文件与 Kubernetes 集群中的资源对象一一对应，便于管理和排查问题。所有资源类型（Pod、ConfigMap、Deployment 等）均需遵循此命名规则，方便查看和管理，这是团队协作和运维的最佳实践。

### 4. Pod 的缺陷及未来部署方式
Pod 作为 Kubernetes 的基本单位，虽然简单易用，但存在一些局限性，导致在生产环境中通常不直接使用 Pod，而是通过更高级的控制器来管理。Pod 的主要缺陷包括：
- **缺乏自我修复能力**：Pod 不会自动重启或重新调度，节点宕机或 Pod 崩溃时需要手动干预。
- **无法滚动更新**：Pod 不支持镜像更新或配置变更后的滚动更新，无法实现零停机部署。
- **不适合有状态应用**：Pod 不具备状态管理能力，无法保证数据持久性或 Pod 身份的唯一性。
- **资源管理有限**：Pod 无法定义副本数量，无法动态扩展或缩容。

因此，在实际生产环境中，建议使用以下控制器替代直接管理 Pod：
- **Deployment**：适用于无状态应用，支持滚动更新、回滚、副本管理。
- **DaemonSet**：适用于需要在每个节点上运行一个 Pod 的场景，例如日志收集。
- **StatefulSet**：适用于有状态应用，提供稳定的网络标识和存储。

通过这些控制器，Kubernetes 能够更好地管理应用的生命周期和稳定性，弥补 Pod 自身的不足。