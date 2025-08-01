# 从零开始学习 CI/CD 与 PyDockerDeploy 项目实践

## 一、课程目标
1. 让零基础学员理解 CI/CD 的基本概念及其在软件开发中的作用，认识常见 CI/CD 工具。
2. 熟悉 PyDockerDeploy 项目的功能和使用场景，掌握其核心代码逻辑。
3. 学会如何准备环境并实践 Docker 容器部署。


## 二、课程内容

### 1. CI/CD 概念介绍（通俗易懂，形象类比）

**目标：通过生活化的比喻让小白群体理解 CI/CD 的重要性，并认识常见的 CI/CD 工具及其作用。**

- **什么是 CI/CD？**
  - **CI（持续集成）**：想象你在和朋友一起准备一顿大餐，每个人负责不同的菜（比如炒菜、煮汤、做甜点）。为了确保最后能顺利开饭，每当一个人做好一道菜，就会马上放到餐桌上，和其他已经完成的菜一起试着搭配，看看味道是否协调。如果有问题（比如太咸或太甜），马上调整。这就是持续集成——在软件开发中，开发人员经常把自己的代码合并到主代码库（就像餐桌），并通过自动化测试检查代码是否有问题（就像试味道），确保整体项目不会因为某个人的代码而出错。
  - **CD（持续交付/持续部署）**：继续大餐的例子，当一道菜做好并确认没问题后，我们不是等所有菜都做好才上桌，而是立刻端给客人品尝。这就是持续交付/持续部署——通过自动化工具快速把代码更新送到用户手中（生产环境，就像餐厅的餐桌），让用户能尽早用上新功能。持续交付（Continuous Delivery）是指确保代码随时可以部署，而持续部署（Continuous Deployment）是指代码通过测试后自动部署到生产环境。

- **CI/CD 的好处：**
  - **CI 的好处**：就像试菜能及时发现味道问题，持续集成让团队早发现代码中的 Bug，减少后期修复成本。如果不及时测试，问题可能堆积到最后，导致项目延期或失败。
  - **CD 的好处**：就像及时上菜能让客人满意，持续部署让用户更快体验到新功能，同时减少手动部署出错的风险。手动部署就像手忙脚乱地上菜，容易出错，而自动化部署就像有服务员机器人帮忙，省力又准确。

- **没有 CI/CD 会怎样？**
  - 没有 CI：就像所有人做完菜才发现搭配不好，代码问题可能堆积到最后，比如一个人的代码和其他人的代码冲突，或者某个功能有 Bug 导致整个项目崩溃，修复成本非常高。
  - 没有 CD：就像等所有菜都做好才上桌，用户要等很久才能看到新功能，体验很差。而且手动部署还可能因为人为失误（如配置错误）导致服务宕机。

- **CI/CD 工具的作用与常见工具介绍：**
  - CI/CD 就像餐厅里的分工体系，需要不同的工具（就像不同的厨具和服务员）来完成从做菜到上菜的全流程。下面是一些常见的 CI/CD 工具，各自有不同的“专长”：
    1. **Jenkins（CI 工具）**：
       - 作用：Jenkins 是一个非常流行的持续集成工具，就像餐厅里的“总厨”，负责协调大家做菜。它可以自动运行测试、构建软件（把代码变成可运行的程序或镜像），确保每道菜（代码）都没问题。
       - 例子：当你提交代码后，Jenkins 会自动运行测试脚本，如果测试通过，它会把代码打包成 Docker 镜像（就像把菜装盘），为后续部署做好准备。
    2. **GitLab Runner（CI/CD 工具）**：
       - 作用：GitLab Runner 是 GitLab 平台自带的 CI/CD 工具，就像餐厅里的“多面手服务员”，既能帮忙做菜（运行测试、构建），也能帮忙上菜（部署）。它通过 GitLab 的配置文件（`.gitlab-ci.yml`）来定义整个流程。
       - 例子：你可以在 GitLab 上设置，当代码提交到某个分支时，GitLab Runner 自动运行测试、构建镜像，并推送到镜像仓库。
    3. **ArgoCD（CD 工具）**：
       - 作用：ArgoCD 是一个专注于持续部署的工具，特别适合 Kubernetes 环境（一种管理容器化应用的系统）。它就像餐厅里的“智能上菜机器人”，会持续监控目标环境，确保部署的软件版本和期望的一致，如果不一致就自动调整。
       - 例子：ArgoCD 可以自动检测代码仓库中的配置文件变化，然后把最新的应用部署到 Kubernetes 集群中。
    4. **PyDockerDeploy（我们自己的 CD 工具）**：
       - 作用：PyDockerDeploy 是我们今天要学习的工具，专注于 Docker 容器的持续部署。它就像一个“专职送菜员”，负责把 Jenkins 或 GitLab Runner 构建好的 Docker 镜像（已经做好的菜）快速送到目标服务器（餐桌），并确保软件正常运行。
       - 例子：PyDockerDeploy 可以连接多台服务器，自动下载指定镜像并启动容器，完成从镜像到运行服务的最后一步。

- **CI/CD 工具如何协同工作？**
  - 就像餐厅里总厨（Jenkins）负责做菜，多面手服务员（GitLab Runner）帮忙做菜和送菜，智能机器人（ArgoCD）和专职送菜员（PyDockerDeploy）负责把菜送到客人面前，这些工具可以组合使用，形成一个完整的 CI/CD 流水线。
  - 典型流程：开发人员提交代码 → Jenkins/GitLab Runner 运行测试并构建镜像 → 镜像推送到仓库（如 Harbor）→ PyDockerDeploy/ArgoCD 拉取镜像并部署到服务器。
  - 通俗解释：就像做菜（CI）完成后，有人负责把菜送到餐桌（CD），PyDockerDeploy 就是我们自己打造的“送菜工具”，简单好用，专注于 Docker 部署。

- **互动环节：**
  - 提问：如果做菜时不试味道、不及时上菜，会发生什么问题？（引导学生类比到软件开发中的代码冲突、部署延迟等问题）
  - 提问：如果餐厅里没有总厨（Jenkins）或送菜员（PyDockerDeploy），会怎样影响效率？（引导学生思考 CI/CD 工具在自动化和分工中的作用）


### 2. PyDockerDeploy 项目介绍

**目标：让小白群体了解 PyDockerDeploy 项目的用途和功能。**

- **项目是什么？**
  - PyDockerDeploy 是一个用 Python 写的小工具，专门用来帮助我们把 Docker 容器（可以理解为一个轻量化的软件运行环境）快速部署到服务器上。
  - 它就像一个“快递员”，负责把开发好的软件（Docker 镜像）送到目标地点（服务器），并确保软件能正常运行。
  - 项目地址：https://gitee.com/Tender-Liu/PyDockerDeploy.git

- **项目能做什么？**
  1. 支持一次性把软件部署到多台服务器。
  2. 提供三种部署方式：可以根据代码分支部署、直接指定软件版本部署，或者用服务器上已有的最新版本重新启动。
  3. 还能管理软件的运行状态（启动、停止、删除）和清理不需要的老版本。

- **项目在 CI/CD 中的位置：**
  - 它主要负责 CD（持续部署）部分，是 CI/CD 流程的“最后一站”，把 CI 阶段构建好的软件（Docker 镜像）部署到服务器上。
  - 简单来说，CI 负责“做菜”（代码测试和构建），CD 负责“上菜”（部署到用户环境），而 PyDockerDeploy 就是“上菜的工具”。

- **互动环节：**
  - 提问：如果你是餐厅服务员，有什么工具能帮你更快、更准确地上菜？（引导学生类比到 PyDockerDeploy 的自动化部署功能）


### 3. PyDockerDeploy 项目结构与逻辑（Mermaid 图与解释）
**时间：20 分钟**

**目标：通过结构图和简单解释让小白群体了解项目的组成和逻辑。**

- **项目结构图展示：**
  ```mermaid
  classDiagram
      class DeployConfig {
          +str project_name
          +str git_branch
          +str image_tag
          +List[str] hosts
      }
      class DockerDeployer {
          +deploy()
          +deploy_to_host()
      }
      class DockerManager {
          +pull_image()
          +start_container()
          +stop_container()
      }
      DockerDeployer --> DeployConfig
      DockerDeployer --> DockerManager
  ```

- **结构图解释（通俗版）：**
  1. **DeployConfig（部署配置）**：
     - 就像一个“任务清单”，记录了我们要部署什么软件（`project_name`）、用哪个版本（`git_branch` 和 `image_tag`）、送到哪些服务器（`hosts`）。
     - 作用：告诉其他部分该做什么。
  2. **DockerDeployer（部署执行者）**：
     - 就像一个“总指挥”，负责看任务清单，然后安排部署工作。
     - 主要任务：`deploy()` 是总部署计划，指挥所有服务器完成部署；`deploy_to_host()` 是单台服务器的部署步骤。
  3. **DockerManager（Docker 工具箱）**：
     - 就像一个“具体干活的工人”，专门负责和服务器上的 Docker 打交道。
     - 主要任务：`pull_image()` 是下载软件版本，`start_container()` 是启动软件，`stop_container()` 是停止软件运行。
  4. **关系箭头**：
     - `DockerDeployer --> DeployConfig`：总指挥要看任务清单才能知道做什么。
     - `DockerDeployer --> DockerManager`：总指挥指挥工人去干具体的活。

- **互动环节：**
  - 提问：如果任务清单（DeployConfig）写错了，会发生什么？（引导学生思考配置错误会导致部署失败）

---

### 4. 核心代码讲解（简单易懂）
**时间：25 分钟**

**目标：通过核心代码片段让小白群体理解 PyDockerDeploy 的工作原理。**

- **代码文件总览：**
  - `deployer.py`：主程序，负责接收命令和整体部署流程。
  - `utils/docker_manager.py`：负责 Docker 的具体操作（如下载、启动软件）。
  - `utils/ssh_client.py`：负责连接服务器，就像一个“远程遥控器”。
  - `config_manager.py`：负责上传配置文件，就像“送材料到工地”。

- **核心代码片段讲解：**
  1. **DeployConfig 类（任务清单）**：
     - 代码作用：保存部署需要的各种信息，比如软件名字、版本、目标服务器。
     - 通俗解释：就像你点外卖时填写的订单信息（收货地址、餐品名称），没有这个清单，后面就不知道送哪里、送什么。
     - 示例代码（简化版）：
       ```python
       class DeployConfig:
           def __init__(self, project_name, docker_run, hosts, harbor_registry):
               self.project_name = project_name  # 软件名称
               self.docker_run = docker_run      # 启动软件的命令
               self.hosts = hosts                # 目标服务器列表
               self.harbor_registry = harbor_registry  # 软件仓库地址
       ```

  2. **DockerDeployer 类（总指挥）**：
     - 代码作用：读取任务清单，安排部署步骤。
     - 通俗解释：就像外卖配送中心，接到订单后安排骑手送餐，确保每个地址都送到。
     - 示例代码（简化版）：
       ```python
       class DockerDeployer:
           def __init__(self, config):
               self.config = config  # 保存任务清单
           
           def deploy(self, ssh_clients):
               print("开始部署...")
               for ssh_client in ssh_clients:  # 遍历每个服务器
                   self.deploy_to_host(ssh_client)  # 部署到单台服务器
               print("部署完成！")
       ```

  3. **DockerManager 类（具体工人）**：
     - 代码作用：执行具体的 Docker 操作，比如下载软件、启动软件。
     - 通俗解释：就像外卖骑手，具体负责把餐送到客户手上。
     - 示例代码（简化版）：
       ```python
       class DockerManager:
           def pull_image(self, image_name):
               print(f"下载软件版本: {image_name}")
               # 通过 SSH 远程执行 Docker 命令下载
           
           def start_container(self, container_name, docker_run):
               print(f"启动软件: {container_name}")
               # 通过 SSH 远程启动 Docker 容器
       ```

- **互动环节：**
  - 提问：如果骑手（DockerManager）送餐时地址错了，会发生什么？（引导学生思考 Docker 命令执行错误的影响）

### 5. 安装依赖说明（环境准备）
**时间：15 分钟**

**目标：指导小白群体如何准备 PyDockerDeploy 的运行环境。**

- **为什么需要准备环境？**
  - 就像你要骑自行车送外卖，得先有自行车和头盔，PyDockerDeploy 也需要一些“工具”才能正常工作。

- **每台服务器需要安装的依赖：**
  1. 安装 Python 的 SSH 工具：
     ```bash
     sudo apt install python3-paramiko
     ```
     - 作用：`paramiko` 是一个 Python 库，让 PyDockerDeploy 能远程控制服务器，就像“遥控器”。
  2. 配置 Docker 使用权限：
     ```bash
     sudo usermod -aG docker ubuntu
     ```
     - 作用：让 `ubuntu` 用户有权限操作 Docker，就像给骑手发放通行证。配置后需要重新登录服务器让权限生效。

- **提前准备项目镜像：**
  - 就像外卖平台要先有餐品库存，PyDockerDeploy 需要有软件版本（Docker 镜像）才能部署。
  - 建议提前在镜像仓库（如 Harbor）准备好镜像，示例：`harbor.labworlds.cc/go-starter/master:liujun-v1.0`。
  - 说明：这些镜像通常由 CI 流程（比如 Jenkins）自动生成并上传。


### 6. 实践操作：部署测试
**时间：30 分钟**

**目标：通过实际操作让小白群体掌握 PyDockerDeploy 的基本使用。**

- **测试场景：**
  - 我们用 PyDockerDeploy 把一个软件（Docker 镜像）部署到一台服务器上。
  - 命令示例（基于 Git 分支部署）：
    ```bash
    python deployer.py -p go-starter --git_branch master --image_tag liujun-v1.0 \
        --hosts 192.168.110.8 --harbor_registry harbor.labworlds.cc \
        --docker_run "docker run -d -p 9006:8080"
    ```
  - 通俗解释：这段命令就像告诉快递员：“把 go-starter 这个软件的 master 分支、liujun-v1.0 版本，送到 192.168.110.8 这台服务器，启动时用指定方式运行。”

- **操作步骤：**
  1. 下载 PyDockerDeploy 项目代码到本地（就像拿到快递工具）。
  2. 修改 `deployer.py` 文件中的 SSH 配置（比如用户名、私钥路径），就像设置快递员的导航地址。
  3. 在终端运行上面的命令，观察部署过程（就像看着快递员送货）。
  4. 登录目标服务器，用 `docker ps` 命令检查软件是否正常运行（就像确认客户收到货）。

- **互动环节：**
  - 学生分组实践，教师巡回指导，解决常见问题（如 SSH 连接不上、命令参数错误）。
