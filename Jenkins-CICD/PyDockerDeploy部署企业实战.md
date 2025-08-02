# 从零开始学习 CI/CD 与 PyDockerDeploy 项目实践

## 一、课程目标
1. **掌握 CI/CD 基础知识**：理解持续集成（CI）和持续交付/部署（CD）的基本概念及其在现代软件开发中的重要性。
2. **深入了解 PyDockerDeploy**：熟悉 PyDockerDeploy 的功能、应用场景及其核心代码结构，以便在实际项目中有效使用。
3. **环境搭建与实践操作**：学习如何搭建开发环境，掌握 Docker 容器的创建、管理和部署。
4. **CI/CD 工具集成能力**：掌握如何将 PyDockerDeploy 与 CI/CD 工具（如 Jenkins 和 GitLab Runner）进行集成，实现自动化部署。
5. **企业级应用理解**：通过实际案例分析，理解 CI/CD 在企业级项目中的应用及其面临的挑战和解决方案。
6. **容器生命周期管理**：学习如何有效管理 Docker 容器的生命周期，包括启动、停止和清理操作。
7. **安全性与流量管理**：理解如何将 PyDockerDeploy 与 Cloudflare 等工具结合，确保容器部署的安全性和流量管理。



## 1. CI/CD 概念介绍（通俗易懂，形象类比）

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


## 2. PyDockerDeploy 项目介绍

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


## 3. PyDockerDeploy 项目结构与逻辑（Mermaid 图与解释）

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

- **脚本执行参数解释：**
  - 以下是 `deployer.py` 和 `config_manager.py` 脚本中常用的参数及其作用，以表格形式展示，方便理解：
  
  **deployer.py 参数表格：**
  | 参数名             | 完整形式            | 作用与通俗解释                                                                 |
  |--------------------|---------------------|------------------------------------------------------------------------------|
  | `-p`              | `--project`         | 指定要部署的软件名称，就像告诉快递员你要送哪个包裹（例如：go-starter）。      |
  | `-b`              | `--git_branch`      | 指定软件的代码分支，就像告诉快递员这个包裹是哪个版本（例如：master 分支）。  |
  | `-t`              | `--image_tag`       | 指定软件的具体版本号，就像包裹上的标签（例如：liujun-v1.0）。                |
  | `-h`              | `--hosts`           | 指定目标服务器地址，就像快递员的送货地址（例如：192.168.110.8）。            |
  | `-r`              | `--harbor_registry` | 指定软件镜像仓库地址，就像包裹的发货仓库（例如：harbor.labworlds.cc）。      |
  | `-d`              | `--docker_run`      | 指定启动软件的命令，就像告诉快递员如何摆放包裹（例如：`docker run -d -p 9006:8080`）。 |

  **config_manager.py 参数表格（修正版）：**
  | 参数名             | 完整形式            | 作用与通俗解释                                                                 |
  |--------------------|---------------------|------------------------------------------------------------------------------|
  | `--data`          | 无短形式            | 指定配置文件内容，就像告诉管理员你要上传的具体文件内容。                      |
  | `--filepath`      | 无短形式            | 指定远程配置文件路径，就像告诉管理员文件要放在服务器的哪个位置（例如：`/opt/项目名称/config.yml`）。 |
  | `--hosts`         | 无短形式            | 指定目标主机地址列表，就像告诉管理员要将文件送到哪些地址（多个主机用逗号分隔，例如：`192.168.110.8,192.168.110.171`）。 |

- **命令参数详细解释（以 deployer.py 示例命令为例）：**
  - `python3 deployer.py`：运行部署脚本，就像启动快递系统。
  - `-p go-starter`：指定软件名称为 go-starter，就像告诉系统你要送 go-starter 这个包裹。
  - `--git_branch master`：指定代码分支为 master，就像告诉系统这个包裹是 master 版本。
  - `--image_tag liujun-v1.0`：指定版本号为 liujun-v1.0，就像在包裹上贴上具体标签。
  - `--hosts 192.168.110.8`：指定目标服务器为 192.168.110.8，就像告诉快递员送货地址。
  - `--harbor_registry harbor.labworlds.cc`：指定镜像仓库地址为 harbor.labworlds.cc，就像告诉快递员从哪个仓库取货。
  - `--docker_run "docker run -d -p 9006:8080"`：指定启动命令，就像告诉快递员如何安装或摆放包裹（`-d` 表示后台运行，`-p 9006:8080` 表示将服务器的 9006 端口映射到软件的 8080 端口）。

- **命令参数详细解释（以 config_manager.py 示例命令为例）：**
  - `python3 config_manager.py`：运行配置文件上传工具脚本，就像启动文件管理系统。
  - `--data "配置文件内容"`：指定要上传的配置文件内容，就像告诉系统你要上传的具体文件数据。
  - `--filepath "/opt/go-starter/config.yml"`：指定远程服务器上的文件路径，就像告诉系统文件要放在服务器的哪个位置。
  - `--hosts "192.168.110.8,192.168.110.171"`：指定目标主机地址列表，就像告诉系统要将文件上传到哪些服务器。

- **互动环节：**
  - 提问：如果骑手（DockerManager）送餐时地址错了，会发生什么？（引导学生思考 Docker 命令执行错误的影响）

### 5. 安装依赖说明（环境准备）

**目标：指导小白群体如何准备 PyDockerDeploy 的运行环境。**

- **为什么需要准备环境？**
  - 就像你要骑自行车送外卖，得先有自行车和头盔，PyDockerDeploy 也需要一些“工具”才能正常工作。

- **每台服务器需要安装的依赖：**
  1. 安装 Python 的 SSH 工具： (给自己的主机安装的)
     ```bash
     sudo apt install python3-paramiko
     sudo apt install python3-bcrypt
     ```
     - 作用：`paramiko` 是一个 Python 库，让 PyDockerDeploy 能远程控制服务器，就像“遥控器”。
  2. 配置 Docker 使用权限：(给控制的主机安装的)
     - 记得自己要配置harbor私库支持以及使用ubuntu用户登录`docker login harbor.labworlds.cc`
     ```bash
     sudo usermod -aG docker ubuntu
     ```
     - 作用：让 `ubuntu` 用户有权限操作 Docker，就像给骑手发放通行证。**配置后需要重新登录服务器让权限生效**。

- **提前准备项目镜像：**
  - 就像外卖平台要先有餐品库存，PyDockerDeploy 需要有软件版本（Docker 镜像）才能部署。
  - 建议提前在镜像仓库（如 Harbor）准备好镜像，示例：`harbor.labworlds.cc/go-starter/master:liujun-v1.0`。
  - 说明：这些镜像通常由 CI 流程（比如 Jenkins）自动生成并上传。



### 6. 实践操作：部署测试，无需构建

**目标：通过实际操作让小白群体掌握 PyDockerDeploy 的基本使用，并解决代码推送中的常见问题。**

- **测试场景：**
  - 这是个例子，给你们看的，练习在下面呐
  - 我们用 PyDockerDeploy 把一个软件（Docker 镜像）部署到一台服务器上。
  - 命令示例（基于 Git 分支部署）：
    ```bash
    python3 deployer.py -p go-starter \
        --git_branch master \
        --image_tag liujun-v1.0 \
        --hosts 192.168.110.8 \
        --harbor_registry harbor.labworlds.cc \
        --docker_run "docker run -d -p 9006:8080"
    ```
  - 通俗解释：这段命令就像告诉快递员：“把 go-starter 这个软件的 master 分支、liujun-v1.0 版本，送到 192.168.110.8 这台服务器，启动时用指定的方式运行。”每个参数的作用下面会详细解释。

- **操作步骤：**
  1. 下载 PyDockerDeploy 项目代码到本地（就像拿到快递工具）。
     - 命令示例：
       ```bash
       git clone https://gitee.com/Tender-Liu/PyDockerDeploy.git
       cd PyDockerDeploy
       ```
     - 通俗解释：就像从网上下载一个快递工具包，并打开它准备使用。
  2. 修改 `deployer.py` 文件中的 SSH 配置（比如用户名、私钥路径），就像设置快递员的导航地址。
     - 通俗解释：你需要在代码中填入服务器的登录信息，就像告诉快递员用哪个账号和密码进入送货地点。
     - 示例修改内容（在 `deployer.py` 中找到相关配置）：
       ```python
       SSH_USERNAME = "ubuntu"  # 服务器登录用户名
       SSH_PRIVATE_KEY_PATH = "/home/user/.ssh/id_rsa"  # 本地私钥路径
       ```
  3. 在终端运行上面的部署命令，观察部署过程（就像看着快递员送货）。
     - 使用 `\` 换行的命令示例：
       ```bash
       python deployer.py -p go-starter \
           --git_branch master \
           --image_tag liujun-v1.0 \
           --hosts 192.168.110.8,192.168.110.171 \
           --harbor_registry harbor.labworlds.cc \
           --docker_run "docker run -d -p 9006:8080"
       ```
     - 通俗解释：运行这个命令就像下达送货指令，系统会自动完成从取货到送货的全过程。
  4. 登录目标服务器，用 `docker ps` 命令检查软件是否正常运行（就像确认客户收到货）。
     - 命令示例：
       ```bash
       ssh ubuntu@192.168.110.8
       docker ps
       ```
     - 通俗解释：登录服务器就像去送货地点查看，`docker ps` 就像检查包裹是否已经正确摆放并在使用中。


### 6. 实践操作：部署测试 - CI手动/CD半自动 - 前端

**目标：通过实际操作让小白群体掌握 PyDockerDeploy 的基本使用，结合 CI/CD 流程完成前后端分离项目的前端部署，并配置后端域名以适配教室环境。**

- **项目背景介绍：**
  - 本次实践操作基于一个前后端分离的项目 `admin3`，前端部分是 `admin3-ui`，使用 Vue.js 框架（具体是 vue-manage-system），依赖 Node.js 18+ 环境开发。
  - 通俗解释：前后端分离就像把一个大任务拆成两部分，前端负责页面显示（好看的外表），后端负责数据处理（内在逻辑）。我们今天主要处理前端部分，把页面打包成一个可以运行的“包裹”，然后送到服务器上，同时需要配置前端如何找到后端（通过域名和端口）。
  - 项目代码地址：`https://gitee.com/Tender-Liu/admin3.git`

- **操作步骤：**

#### 步骤 1：获取项目代码
- 命令示例：
  ```bash
  git clone https://gitee.com/Tender-Liu/admin3.git
  cd admin3/admin3-ui
  ```
- 通俗解释：就像从网上下载一个包裹（项目代码），然后打开包裹中的前端部分，准备加工。

#### 步骤 2：配置后端域名（修改 .env 文件）
- **背景说明：**
  - 在前后端分离项目中，前端需要知道后端的地址（域名和端口），才能发送请求获取数据。这个地址通常配置在前端项目的 `.env` 文件中。
  - 在教室环境中，常规的 80 和 443 端口可能无法正常使用，因此我们需要使用特殊端口 1443。
  - 为了区分每个学生的部署环境，域名中需要加入个人名字，并由老师通过 Cloudflare 进行授权。
- **操作步骤：**
  1. 打开 `admin3-ui/.env` 文件，使用文本编辑器（如 `vim` 或 `nano`）进行修改。
     - 命令示例：
       ```bash
       vim .env
       ```
  2. 找到 `VITE_BASE_URI` 配置项，修改为以下格式（将 `你的名字` 替换为自己的名字，例如 `zhang-san`）：
     ```env
     VITE_BASE_URI=https://你的名字.admin.labworlds.cc:1443/admin3
     ```
     - 示例（假设名字为 `zhang-san`）：
       ```env
       VITE_BASE_URI=https://zhang-san.admin.labworlds.cc:1443/admin3
       ```
  3. 保存并退出编辑器（如 `vim` 中按 `ESC`，输入 `:wq` 并回车）。
- **通俗解释：**
  - `.env` 文件就像一个地址簿，告诉前端页面“如果你需要数据，就去这个地址找后端”。
  - `VITE_BASE_URI` 是后端的地址，`https://zhang-san.admin.labworlds.cc:1443/admin3` 就像告诉前端“去 zhang-san 的门牌号，敲 1443 号窗口，找 admin3 房间要数据”。
  - 使用个人名字（如 `zhang-san`）是为了避免大家用同一个地址，就像每个人有自己的门牌号，方便区分。
- **重要提醒：**
  - 修改域名后，请向老师申请 Cloudflare 授权，老师会帮你配置域名解析，确保 `你的名字.admin.labworlds.cc` 可以正常访问。
  - 通俗解释：就像你告诉快递公司你的新地址，但需要公司批准并更新导航系统（Cloudflare 授权），这样快递员才能找到你。

#### 步骤 3：理解 Dockerfile 和 Nginx 配置
- **Dockerfile 介绍：**
  - Dockerfile 是一个“制作说明书”，告诉系统如何把前端代码打包成一个可以运行的 Docker 镜像。
  - 内容解析（简化版）：
    ```dockerfile
    # 第一阶段：构建 Vue 项目
    FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/node:18.20.8-alpine3.20 AS build
    WORKDIR /app
    COPY . .
    RUN npm config set registry https://registry.npmmirror.com && \
        yarn config set registry https://registry.npmmirror.com && \
        yarn install && \
        yarn build
    # 第二阶段：使用 Nginx 发布静态文件
    FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/nginx:alpine3.20
    WORKDIR /app
    COPY --from=build /app/dist /app
    COPY nginx.conf /etc/nginx/nginx.conf
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    ```
  - 通俗解释：
    - 第一阶段：就像用一个专门的厨房（Node.js 环境）把原材料（Vue 代码）加工成成品（静态页面文件），用 `yarn install` 和 `yarn build` 命令完成。
    - 第二阶段：把加工好的成品（静态文件）装到一个展示柜（Nginx 服务器）里，Nginx 就像一个服务员，把页面展示给用户看。`EXPOSE 80` 表示服务员在 80 号窗口接待用户，`CMD` 是启动服务员工作的指令。

- **Nginx 配置介绍（nginx.conf）：**
  - Nginx 是一个高效的网页服务器，这里用来展示 Vue 项目打包后的静态页面。
  - 核心配置解析（简化版）：
    ```nginx
    http {
        server {
            listen 80;  # 在 80 端口监听用户请求
            server_name localhost;
            root /app;  # 页面文件放在 /app 目录下
            index index.html;  # 默认页面是 index.html
            location / {
                try_files $uri $uri/ /index.html;  # 支持 Vue 的 history 模式
                add_header Cache-Control "no-store, no-cache, must-revalidate";  # 不缓存页面
            }
            # 静态资源缓存配置
            location /assets {
                expires 1y;  # 缓存 1 年
                add_header Cache-Control "public";
            }
        }
    }
    ```
  - 通俗解释：Nginx 就像一个服务员，接到用户请求后（通过 80 端口），会从 `/app` 文件夹里找到页面文件给用户看。`location /` 确保用户访问任何路径都能看到页面（支持 Vue 的路由模式），而 `location /assets` 则让图片、CSS 等静态文件可以缓存很久，加快用户访问速度。

#### 步骤 4：构建 Docker 镜像
- 命令示例（个人实验用，带名字区分）：
  ```bash
  docker build -t harbor.labworlds.cc/admin3-ui/分支名:名字-版本 .
  ```
- 示例（假设分支名为 `dev`，名字为 `zhang-san`，版本为 `v1.0`）：
  ```bash
  docker build -t harbor.labworlds.cc/admin3-ui/dev:zhang-san-v1.0 .
  ```
- 命令示例（企业环境用，带构建时间）：
  ```bash
  docker build -t harbor.labworlds.cc/admin3-ui/分支名:$(date +%Y%m%d-%H%M%S) .
  ```
- 示例（假设分支名为 `dev`，当前时间为 2025-08-01 20:33）：
  ```bash
  docker build -t harbor.labworlds.cc/admin3-ui/dev:20250801-2033 .
  ```
- 通俗解释：
  - `docker build` 就像按照说明书（Dockerfile）把代码加工成一个包裹（Docker 镜像）。
  - `-t` 参数是给包裹贴标签，格式是 `仓库地址/项目名/分支名:版本号`，方便区分不同人的镜像（实验用）或不同时间的构建（企业用）。
  - `.` 表示在当前目录执行构建，就像告诉系统“就在这里加工”。

#### 步骤 5：推送 Docker 镜像到仓库
- 命令示例（个人实验用）：
  ```bash
  docker push harbor.labworlds.cc/admin3-ui/dev:zhang-san-v1.0
  ```
- 命令示例（企业环境用）：
  ```bash
  docker push harbor.labworlds.cc/admin3-ui/dev:20250801-2033
  ```
- 通俗解释：
  - `docker push` 就像把加工好的包裹送到仓库（Harbor 镜像仓库），这样其他地方的服务器可以从仓库取货。
  - 注意：首次推送前可能需要登录仓库，命令如下（替换用户名和密码）：
    ```bash
    docker login harbor.labworlds.cc -u 用户名 -p 密码
    ```

#### 步骤 6：使用 deployer.py 部署
- 命令示例（使用 Python 3，带 `\` 换行）：
  ```bash
  python3 deployer.py -p admin3-ui \
      --git_branch dev \
      --image_tag zhang-san-v1.0 \
      --hosts 192.168.110.8 \
      --harbor_registry harbor.labworlds.cc \
      --docker_run "docker run -d -p 8000:80"
  ```
- 通俗解释：
  - `python3 deployer.py`：启动部署工具，就像叫来一个快递员。
  - `-p admin3-ui`：指定要部署的软件名称（前端项目）。
  - `--git_branch dev`：指定分支为 dev，就像告诉快递员这是 dev 版本的包裹。
  - `--image_tag zhang-san-v1.0`：指定版本号，就像包裹上的具体标签。
  - `--hosts 192.168.110.8`：指定目标服务器地址，就像告诉快递员送货地点。
  - `--harbor_registry harbor.labworlds.cc`：指定镜像仓库地址，就像告诉快递员从哪里取货。
  - `--docker_run "docker run -d -p 8000:80 --restart=always --cpus=\"1.0\" --memory=\"512m\""`：指定启动命令，就像告诉快递员如何摆放包裹（`-d` 后台运行，`-p 80:80` 将服务器的 8000 端口映射到容器的 80 端口，让用户可以访问页面）。

#### 步骤 7：验证部署结果
- 登录目标服务器检查是否正常运行：
  ```bash
  ssh 用户名@192.168.110.8
  docker ps
  ```
- 通俗解释：就像去送货地点确认包裹是否正确摆放，`docker ps` 会显示运行中的容器，如果看到 `admin3-ui` 相关容器，说明部署成功。
- 进一步验证：通过浏览器访问 `http://192.168.110.8`，看看前端页面是否正常显示。如果页面能正常加载并与后端交互（需要后端已部署），说明配置成功。

- **常见问题解决：**
  1. **构建镜像时网络问题**：
     - 如果 `yarn install` 阶段报错，可能是网络问题，Dockerfile 中已设置镜像源（`registry.npmmirror.com`），如仍失败，可尝试手动设置代理或更换网络。
     - 通俗解释：就像厨房买不到原料，可以换个市场（镜像源）或者修好网络。
  2. **推送镜像时权限问题**：
     - 如果 `docker push` 报错，可能是未登录仓库，执行 `docker login` 命令。
     - 通俗解释：就像快递员没通行证进不了仓库，先登录获取权限。
  3. **部署时端口冲突**：
     - 如果 `docker run` 报错端口已被占用，可修改 `--docker_run` 参数中的端口，例如 `-p 8080:80`。
     - 通俗解释：就像送货地点窗口（端口）被占用了，换个窗口摆放包裹。
  4. **后端域名无法访问**：
     - 如果前端页面加载后无法与后端交互，可能是域名未授权或后端未部署。请确认是否已向老师申请 Cloudflare 授权，并检查后端服务是否在目标服务器上运行。
     - 通俗解释：就像前端敲错了门（域名不对）或者后端房间没人（服务未启动），需要确认地址和后端状态。

- **互动环节：**
  - 学生分组实践，教师巡回指导，解决常见问题（如网络问题、权限问题、端口冲突、域名配置）。
  - 提问：如果快递员送货时发现地址簿上的地址（`VITE_BASE_URI`）写错了，会发生什么？（引导学生思考域名配置的重要性）


## Cloudflare 介绍与结构图解析

### 1. Cloudflare 整体工作原理
- **通俗解释：**
  - Cloudflare 就像一个“网络中间人”，站在用户和你的网站之间，帮你加速访问、保护安全、解析域名。用户访问你的网站时，不是直接找你的服务器，而是先经过 Cloudflare 的处理。
- **Mermaid 结构图：Cloudflare 的基本工作流程**
  ```mermaid
  graph TD
      A[用户] -->|访问网站| B[Cloudflare]
      B -->|加速、安全、解析| C[你的网站服务器]
      C -->|返回内容| B
      B -->|快速、安全地返回| A
  ```
- **图解说明：**
  - 用户（你用浏览器访问网站的人）发起请求，先到 Cloudflare。
  - Cloudflare 像一个“保安+快递员”，检查请求是否安全（防止黑客），加速内容分发（通过 CDN），然后把请求转给你的网站服务器。
  - 服务器返回内容后，Cloudflare 再优化内容（比如压缩图片），快速送回给用户。

### 2. CDN 和边缘节点的作用
- **通俗解释：**
  - CDN（内容分发网络）是 Cloudflare 的核心功能之一，它通过全球分布的边缘节点（小服务器）存储网站内容，用户访问时从最近的节点获取数据，速度更快。
- **Mermaid 结构图：CDN 边缘节点如何工作**
  ```mermaid
  graph TD
      A[用户 - 北京] -->|访问网站| B[Cloudflare CDN 系统]
      C[用户 - 纽约] -->|访问网站| B
      D[用户 - 悉尼] -->|访问网站| B
      
      B -->|选择最近节点| E[边缘节点 - 北京]
      B -->|选择最近节点| F[边缘节点 - 纽约]
      B -->|选择最近节点| G[边缘节点 - 悉尼]
      
      E -->|快速返回内容| A
      F -->|快速返回内容| C
      G -->|快速返回内容| D
      
      H[源服务器 - 上海] -->|同步内容| E
      H -->|同步内容| F
      H -->|同步内容| G
  ```
- **图解说明：**
  - 用户在不同地方（北京、纽约、悉尼）访问网站，请求都先到 Cloudflare CDN 系统。
  - Cloudflare 根据用户位置，智能选择最近的边缘节点（北京节点、纽约节点、悉尼节点）来响应请求，速度快。
  - 边缘节点的内容是从源服务器（比如在上海）同步过来的，就像总店把商品提前送到各地仓库。
  - 通俗解释：就像你在北京买东西，不用从上海发货，直接从北京仓库拿，省时间。

### 3. 边缘节点与源服务器的关系
- **通俗解释：**
  - 边缘节点是离用户近的小仓库，存储网站的副本内容；源服务器是你的主服务器，存储原始内容。边缘节点减轻了源服务器的压力，只有特殊请求才会直接找源服务器。
- **Mermaid 结构图：边缘节点与源服务器的分工**
  ```mermaid
  graph LR
      A[用户1] -->|普通请求| B[边缘节点]
      A2[用户2] -->|普通请求| B
      A3[用户3] -->|特殊请求| B
      B -->|无法处理时转发| C[源服务器]
      C -->|返回内容| B
      B -->|返回内容| A
      B -->|返回内容| A2
      B -->|返回内容| A3
      C -.->|定期同步内容| B
  ```
- **图解说明：**
  - 大部分用户请求（比如看图片、页面）直接由边缘节点处理，快速返回内容。
  - 少数特殊请求（比如登录、提交表单）如果边缘节点处理不了，会转发到源服务器。
  - 源服务器定期把最新内容同步到边缘节点，保持内容一致。
  - 通俗解释：就像大部分顾客在小仓库买东西，只有特殊订单才送到总店处理，总店还定期给仓库补货。

### 4. 域名授权流程
- **通俗解释：**
  - 域名授权是把你的网站地址（比如 `zhang-san.admin.labworlds.cc`）交给 Cloudflare 管理，让它帮你解析地址、加速访问和保护安全。没有授权，用户可能找不到你的网站。
- **Mermaid 结构图：域名授权流程（教室环境）**
  ```mermaid
  sequenceDiagram
      participant S as 学生
      participant T as 老师
      participant C as Cloudflare
      participant U as 用户
      S->>T: 提交域名申请<br>（如 zhang-san.admin.labworlds.cc）
      T->>C: 配置域名授权<br>（添加解析记录）
      C->>T: 授权完成通知
      T->>S: 告知授权成功
      S->>S: 配置前端项目<br>（修改 .env 文件）
      U->>C: 访问网站<br>（输入域名）
      C->>U: 解析域名并返回内容<br>（通过边缘节点加速）
  ```
- **图解说明：**
  - 学生把自己的域名（比如 `zhang-san.admin.labworlds.cc`）告诉老师，申请授权。
  - 老师在 Cloudflare 平台上配置域名解析，完成授权。
  - 授权成功后，学生在项目中配置域名（比如修改 `.env` 文件中的 `VITE_BASE_URI`）。
  - 用户访问网站时，Cloudflare 解析域名，快速返回内容（通过边缘节点）。
  - 通俗解释：就像你把新店地址告诉队长（老师），队长帮你登记到导航系统（Cloudflare），顾客才能通过导航找到你。

### 5. Cloudflare 的安全保护机制
- **通俗解释：**
  - Cloudflare 像一个保安，帮你挡住黑客攻击（比如 DDoS 攻击），只让正常用户访问你的网站。
- **Mermaid 结构图：Cloudflare 安全保护流程**
  ```mermaid
  graph TD
      A[正常用户] -->|访问网站| B[Cloudflare 安全层]
      A2[黑客攻击] -->|恶意请求| B
      B -->|允许通过| C[你的网站服务器]
      B -->|拦截| A2
      C -->|返回内容| B
      B -->|返回内容| A
  ```
- **图解说明：**
  - 正常用户的请求通过 Cloudflare 安全检查，顺利到达你的服务器。
  - 黑客的恶意请求（比如 DDoS 攻击）被 Cloudflare 拦截，无法到达服务器。
  - 通俗解释：就像保安检查来访者，顾客可以进店，捣乱的人被赶走。

### 6. 常见问题解答（结合图解）
- **问题 1：为什么需要边缘节点？**
  - 答：边缘节点离用户近，加速内容加载，减轻源服务器压力。参考“CDN 边缘节点如何工作”图，全球用户都能从最近节点获取内容。
  - 通俗解释：就像小仓库离顾客近，买东西快，总店也不用忙坏了。
- **问题 2：域名授权有什么用？**
  - 答：授权让 Cloudflare 管理你的域名，用户才能找到你的网站，还能享受加速和安全保护。参考“域名授权流程”图，授权后用户访问顺畅。
  - 通俗解释：就像把地址登记到导航系统，顾客才能找到你，导航还帮你优化路线。

### 7. 互动环节
- 提问：看“CDN 边缘节点如何工作”图，如果你在北京访问网站，Cloudflare 会选哪个节点？为什么？（引导学生理解位置优化的概念）
- 讨论：看“域名授权流程”图，如果不授权会怎样？用户能找到你的网站吗？（引导学生思考授权的重要性）

### 8. 总结：为什么要用 Cloudflare？
- Cloudflare 提供加速（CDN 边缘节点）、安全保护、域名解析等功能，让你的网站更快、更安全，用户体验更好。
- 通俗解释：Cloudflare 就像一个超级帮手，帮你开分店（边缘节点）、当保安（防攻击）、做导航（域名解析），让你的小店生意更好。

你好！感谢你的提醒，我会根据正确的流程重新整理实验环节的内容，确保包含学生注册 Cloudflare 账号、使用 Google 邮箱发送给老师、老师授权域名的步骤，以及学生自行配置 DNS 解析的详细指导。以下是修订后的内容，依然面向小白群体，用通俗易懂的语言，并结合 Mermaid 图直观展示流程。


### Cloudflare 实验环节：详细步骤指导（面向小白群体）

**目标：帮助同学们完成 Cloudflare 注册、域名授权申请、DNS 解析配置、CDN 开启、Nginx 配置，并验证结果。**

#### 1. 学生注册 Cloudflare 账号
- **步骤：**
  1. 打开浏览器，访问 Cloudflare 官网（`https://www.cloudflare.com/`）。
  2. 点击“Sign Up”或“注册”按钮，输入邮箱地址和密码，完成注册。
     - 建议使用 Google 邮箱（如 `yourname@gmail.com`）注册，方便后续与老师沟通。
  3. 注册后，登录 Cloudflare 账号，进入管理控制台（Dashboard）。
- **通俗解释：**
  - 就像你去开一个淘宝店，先要注册一个账号，才能管理你的店铺。Cloudflare 账号就是你管理网站加速和安全的“后台”。
- **注意：**
  - 使用常用的邮箱，确保能收到验证邮件。如果注册遇到问题，及时告诉老师。

#### 2. 学生将 Google 邮箱发送给老师，申请域名授权
- **步骤：**
  1. 注册 Cloudflare 账号后，将你的 Google 邮箱地址（比如 `yourname@gmail.com`）通过微信、邮件或其他方式发送给老师。
  2. 同时告知老师你希望使用的子域名（比如 `shiqi.admin.labworlds.cc`）。
  3. 等待老师完成域名授权，并通知你授权结果。
- **通俗解释：**
  - 就像你告诉老师“我要开店，地址是 `labworlds.cc`”，然后把你的联系方式（邮箱）给老师，老师会帮你登记到导航系统。
- **注意：**
  - 确保邮箱和子域名信息准确无误，方便老师快速处理。如果长时间未收到老师回复，主动询问进度。

#### 3. 老师授权域名（labworlds.cc）步骤
- **老师操作流程：**
  1. 收到学生发送的 Google 邮箱和子域名信息后，登录 Cloudflare 管理控制台。
  2. 在 Cloudflare 团队账号中，添加学生邮箱（`yourname@gmail.com`）为团队成员，并分配对应子域名（比如 `labworlds.cc`）的管理权限。
  3. 通知学生授权已完成，学生可以登录自己的 Cloudflare 账号查看授权的域名。
- **通俗解释：**
  - 就像老师在导航系统（Cloudflare）上为每个学生登记一个地址（子域名），并授权学生自己管理这个地址。
- **Mermaid 结构图：域名授权流程（老师与学生）**
  ```mermaid
  sequenceDiagram
      participant S as 学生
      participant T as 老师
      participant C as Cloudflare
      S->>T: 发送 Google 邮箱和域名<br>（如 labworlds.cc）
      T->>C: 添加学生邮箱到团队<br>分配子域名权限
      C->>T: 授权完成
      T->>S: 通知授权成功
      S->>C: 登录账号查看授权域名
  ```
- **老师注意：**
  - 确保学生邮箱正确添加，避免权限分配错误。
- **学生注意：**
  - 收到老师通知后，登录 Cloudflare 账号确认是否能看到授权的域名。

#### 4. 学生配置 DNS 解析
- **背景说明：**
  - 由于教室的公网 IP 是临时的，且教室环境全面翻墙，无法直接获取固定 IP，需要通过百度搜索“IP 查询”来获取当前公网 IP，并配置 DNS 解析。
- **步骤：**
  1. 打开浏览器，访问百度（`https://www.baidu.com/`）。
  2. 在搜索框输入“IP 查询”或“我的 IP”，百度会显示当前公网 IP 地址（比如 `114.114.114.114`），记下这个 IP。
  3. 登录 Cloudflare 账号，进入管理控制台（Dashboard）。
  4. 在左侧菜单选择“DNS”选项，找到你的域名（比如 `labworlds.cc`）。
  5. 点击“添加记录”（Add Record），配置如下：
     - 类型（Type）：选择 `A`（表示指向 IP 地址）。
     - 名称（Name）：输入你的子域名（比如 `shiqi.admin.labworlds.cc`）。
     - IPv4 地址（IPv4 Address）：输入刚才查询到的公网 IP（比如 `114.114.114.114`）。
     - TTL：选择“自动”（Auto）。
     - 代理状态（Proxy Status）：确保云朵图标为橙色（表示开启 CDN）。
  6. 点击“保存”（Save），等待 DNS 解析生效（通常几分钟）。
- **通俗解释：**
  - 就像你告诉导航系统（Cloudflare）：“我的店在 `114.114.114.114` 这个位置，请帮我登记。”橙色云朵图标就像“分店已开”，会加速顾客访问。
- **Mermaid 结构图：DNS 解析配置流程**
  ```mermaid
  sequenceDiagram
      participant S as 学生
      participant B as 百度
      participant C as Cloudflare
      S->>B: 搜索“IP 查询”
      B->>S: 返回公网 IP（如 114.114.114.114）
      S->>C: 登录账号，进入 DNS 设置
      S->>C: 添加 A 记录<br>（域名: shiqi.admin.labworlds.cc<br>IP: 114.114.114.114）
      C->>S: 保存成功，等待生效
  ```
- **注意：**
  - 公网 IP 是临时的，可能随时变化。如果访问网站时发现域名解析不对，及时重新查询 IP 并更新 DNS 记录。
  - DNS 解析生效需要时间，如果访问网站提示找不到地址，稍等片刻或问老师确认。

#### 5. 开启 Cloudflare CDN
- **步骤：**
  1. 在 Cloudflare DNS 设置页面，找到你刚添加的记录（比如 `shiqi.admin.labworlds.cc`）。
  2. 确保右侧的“云朵图标”是橙色（表示 CDN 已开启）。如果不是橙色，点击图标切换到橙色状态。
- **通俗解释：**
  - 就像你告诉 Cloudflare：“请帮我开分店（边缘节点），让顾客能快速买到东西。”橙色云朵图标就是“分店已开”的标志。
- **Mermaid 结构图：CDN 开启效果**
  ```mermaid
  graph TD
      A[用户] -->|访问 shiqi.admin.labworlds.cc| B[Cloudflare CDN]
      B -->|选择最近边缘节点| C[边缘节点]
      C -->|快速返回内容| A
      D[源服务器] -.->|同步内容| C
  ```
- **注意：**
  - CDN 开启后，需要几分钟生效。如果访问网站时速度慢，稍等片刻或问老师确认。

#### 6. 配置 Nginx 域名解析到 Docker 前端服务
- **背景说明：**
  - Nginx 是一个反向代理服务器，负责把用户的请求转发到你的 Docker 前端服务（比如运行在 `192.168.110.8:8000` 的服务）。
- **步骤：**
  1. 登录服务器 `192.168.110.167`（老师提供的虚拟机或容器环境），进入 Nginx 配置文件目录：
     ```bash
     cd /etc/nginx/conf.d/
     ```
  2. 创建或编辑配置文件（以 `shiqi.admin.labworlds.cc.conf` 为例），内容如下（老师已提供模板，直接复制粘贴）：
     ```nginx
     # HTTPS server
     server {
         listen 1443 ssl;
         server_name shiqi.admin.labworlds.cc;
         access_log /var/log/nginx/shiqi.admin.labworlds.cc.access.log json_combined;
         error_log /var/log/nginx/shiqi.admin.labworlds.cc.error.log warn;
         
         # 证书文件路径
         ssl_certificate /etc/nginx/ssl/shiqi.admin.labworlds.cc/certificate.crt;
         ssl_certificate_key /etc/nginx/ssl/shiqi.admin.labworlds.cc/private.key;
         
         # SSL优化配置
         ssl_protocols TLSv1.2 TLSv1.3;
         ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
         ssl_prefer_server_ciphers on;
         ssl_session_cache shared:SSL:10m;
         ssl_session_timeout 10m;
         ssl_stapling on;
         ssl_stapling_verify on;
         
         # 添加location配置
         location / {
             proxy_pass http://admin_fronend;
             proxy_http_version 1.1;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
             proxy_connect_timeout 60s;
             proxy_send_timeout 60s;
             proxy_read_timeout 60s;
         }
     }

     # 将HTTP请求重定向到HTTPS
     server {
         listen 180;
         server_name shiqi.admin.labworlds.cc;
         return 301 https://$server_name:1443$request_uri;
     }

     upstream admin_fronend {
         server 192.168.110.8:8000 max_fails=3 fail_timeout=30s;
     }
     ```
  3. 生成 SSL 证书（用于 HTTPS 加密访问）：
     ```bash
     mkdir -p /etc/nginx/ssl/shiqi.admin.labworlds.cc/
     openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/shiqi.admin.labworlds.cc/private.key -out /etc/nginx/ssl/shiqi.admin.labworlds.cc/certificate.crt -subj "/C=CN/ST=Beijing/L=Beijing/O=liujun/CN=shiqi.admin.labworlds.cc"
     ```
  4. 检查 Nginx 配置是否正确：
     ```bash
     nginx -t
     ```
  5. 重启 Nginx 使配置生效：
     ```bash
     systemctl reload nginx
     ```

- **通俗解释：**
  - Nginx 就像一个“门卫”，用户的请求（访问 `shiqi.admin.labworlds.cc:1443`）先到门卫这里，门卫再把请求转给里面的 Docker 前端服务（`192.168.110.8:80`）。
  - SSL 证书就像“安全锁”，保证用户和网站之间的通信是加密的，不会被偷看。
- **Mermaid 结构图：Nginx 转发流程**
  ```mermaid
  graph TD
      A[用户] -->|访问 https://shiqi.admin.labworlds.cc:1443| B[Nginx 反向代理]
      B -->|转发请求| C[Docker 前端服务<br>192.168.110.8:80]
      C -->|返回内容| B
      B -->|返回内容| A
  ```
- **注意：**
  - 确保 Docker 前端服务已启动（`192.168.110.8:80`），否则 Nginx 转发会失败。
  - 如果 `nginx -t` 报错，检查配置文件是否有语法错误，及时问老师。

#### 6. 验证 Cloudflare CDN 是否开启
- **步骤：**
  1. 打开 Google Chrome 浏览器，访问你的网站：
     ```
     https://shiqi.admin.labworlds.cc:1443
     ```
  2. 按 `F12` 打开开发者工具，选择“Network”选项卡，刷新页面。
  3. 查看请求的响应头（Response Headers），寻找类似 `CF-Cache-Status: HIT` 的字段：
     - 如果有 `HIT`，说明内容是从 Cloudflare 边缘节点获取的，CDN 已开启。
     - 如果是 `MISS` 或没有相关字段，可能 CDN 未生效，稍等几分钟或问老师确认。
- **通俗解释：**
  - 就像你买东西时，包裹上写着“本地仓库发货”（HIT），说明是从 Cloudflare 的小仓库拿的，速度快。如果写“总店发货”（MISS），说明还没用上 CDN。
- **注意：**
  - 首次访问可能是 `MISS`，因为内容还没缓存到边缘节点，多刷新几次可能变成 `HIT`。

#### 7. 检查页面访问后端服务
- **步骤：**
  1. 在浏览器中访问网站（`https://shiqi.admin.labworlds.cc:1443`），按 `F12` 打开开发者工具，选择“Network”选项卡。
  2. 查看页面发出的后端请求 URL，确认是否以 `/admin3/` 开头（比如 `/admin3/userinfo`）。
  3. 如果后端服务未部署，请求会返回 `500` 错误（服务器内部错误），这是正常现象，后续会学习配置后端服务。
- **通俗解释：**
  - 就像你点了外卖，但餐厅（后端服务）还没开张，订单会失败（返回 500）。现在先记住后端 URL 的前缀（`/admin3/`），等会开张餐厅时要用。
- **注意：**
  - 记录下后端 URL 前缀（`/admin3/`），后续配置后端服务时会用到。
  - 如果页面无法加载，确认 Nginx 和 Docker 前端服务是否正常运行。

#### 8. 常见问题解答
- **问题 1：访问网站时提示证书错误怎么办？**
  - 答：因为我们用的是自签名证书（`openssl` 生成），浏览器会提示不安全。点击“继续访问”或“接受风险”即可，实验环境不影响使用。
  - 通俗解释：就像你用了一个临时门锁，保安（浏览器）不认识，提醒你小心，但你可以放心进门。
- **问题 2：CDN 一直显示 MISS 怎么办？**
  - 答：可能是 CDN 缓存未生效，等待几分钟或多刷新几次。如果仍无效，确认 Cloudflare DNS 记录的云朵图标是否为橙色。
  - 通俗解释：就像小仓库刚开张，东西还没送来，多等一会或问店长（老师）。

#### 9. 互动环节
- 提问：访问网站后，开发者工具显示 `CF-Cache-Status: HIT` 了吗？如果没有，可能是什么原因？（引导学生理解 CDN 缓存机制）
- 讨论：后端 URL 以 `/admin3/` 开头，为什么现在访问会返回 500？（引导学生思考前后端分离的概念）


### 部署测试 - CI手动/CD半自动 - 后端

#### 一、实验目标
1. 掌握 Docker 镜像构建与推送的基本操作。
2. 理解 `admin3-server` 服务的 Dockerfile 和配置文件内容。
3. 使用 `config_manager.py` 和 `deployer.py` 脚本完成配置文件的上传和服务的部署。
4. 配置 Nginx 反向代理，理解跨域概念并完成前后端联调。
5. 测试系统登录功能，验证后端服务是否正常运行。

#### 二、实验环境
- **顶级域名**：labworlds.cc（由老师授权）
- **数据库**：由老师提供，已学习过 MySQL 主从与 ProxySQL 读写代理，无需自行部署。
- **目标服务器**：192.168.110.8
- **镜像仓库**：harbor.labworlds.cc
- **Harbor 仓库查看地址**：192.168.110.164（账号：admin，密码：admin123）

#### 三、实验步骤与内容解释

##### 1. 构建 admin3-server 镜像
- **进入项目目录**：
  ```bash
  cd admin3/admin3-server
  ```
  说明：进入 `admin3-server` 项目目录，准备构建 Docker 镜像。

- **Dockerfile 内容解释**：
  Dockerfile 是一个用于构建 Docker 镜像的脚本文件，类似于一份“制作说明书”，告诉 Docker 如何一步步构建一个可以运行的服务镜像。以下是 `admin3-server` 的 Dockerfile 内容及逐行解释：
  ```dockerfile
  # 第一阶段：构建阶段
  FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/maven:3.9.9-eclipse-temurin-21-alpine AS builder
  # 使用 Maven 镜像作为基础镜像，包含 Java 21 和 Maven 工具，用于编译代码。AS builder 表示这是一个临时阶段，命名为 builder。

  WORKDIR /build
  # 设置工作目录为 /build，所有后续操作都在这个目录下进行，就像设置一个临时工作台。

  COPY pom.xml .
  COPY src src/
  # 将项目中的 pom.xml 和 src 目录复制到工作目录，pom.xml 是项目依赖文件，src 是源代码目录。

  RUN mkdir -p /usr/share/maven/conf/ && \
      sed -i '/<mirrors>/a\    <mirror>\n      <id>aliyun-public</id>\n      <mirrorOf>*</mirrorOf>\n      <name>Aliyun Public</name>\n      <url>https://maven.aliyun.com/nexus/content/groups/public/</url>\n    </mirror>' /usr/share/maven/conf/settings.xml
  # 配置 Maven 镜像源为阿里云镜像，加快依赖包下载速度，就像告诉系统“去这个更快的仓库拿材料”。

  RUN mvn clean package -DskipTests
  # 执行 Maven 构建命令，清理旧文件并打包项目，-DskipTests 表示跳过测试环节，生成可执行的 jar 文件。

  # 第二阶段：运行阶段
  FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/eclipse-temurin:21-jdk-alpine
  # 使用一个更小的 Java 21 运行时镜像作为基础镜像，用于运行打包好的程序，减少镜像体积。

  WORKDIR /app
  # 设置工作目录为 /app，所有运行时操作都在这个目录下进行。

  COPY --from=builder /build/target/admin3-server-*-SNAPSHOT.jar admin3-server.jar
  # 从第一阶段（builder）中复制生成的 jar 文件到当前镜像的 /app 目录，并重命名为 admin3-server.jar。

  ENV JAVA_OPTS="-Xms256m -Xmx512m"
  # 设置 Java 虚拟机参数，-Xms256m 表示初始内存为 256MB，-Xmx512m 表示最大内存为 512MB，防止程序占用过多内存。

  EXPOSE 8080
  # 暴露 8080 端口，表示程序会通过这个端口对外提供服务，就像打开一扇门让外界访问。

  ENTRYPOINT ["sh", "-c", "java ${JAVA_OPTS} -jar admin3-server.jar --spring.config.location=file:/app/application.yml"]
  # 设置容器启动命令，使用 java 运行 jar 文件，并指定配置文件位置为 /app/application.yml，就像告诉系统“启动时用这个配置运行程序”。
  ```

- **构建镜像命令**：
  ```bash
  docker build -t harbor.labworlds.cc/admin3-server/分支名:名字-版本 .
  ```
  命令解释：
  - `docker build`：构建 Docker 镜像，就像按照说明书制作一个产品。
  - `-t harbor.labworlds.cc/admin3-server/分支名:名字-版本`：为镜像指定一个标签，格式为“仓库地址/项目名/分支名:版本名”，例如 `harbor.labworlds.cc/admin3-server/master:liujun-v1.0`，就像给产品贴上名称和版本号。
  - `.`：表示在当前目录查找 Dockerfile 文件。

- **推送镜像到仓库**：
  构建完成后，使用以下命令推送镜像到 Harbor 仓库：
  ```bash
  docker push harbor.labworlds.cc/admin3-server/分支名:名字-版本
  ```
  说明：推送镜像到 `harbor.labworlds.cc` 仓库，完成后可登录 192.168.110.164（账号：admin，密码：admin123）查看镜像是否上传成功。

##### 2. 配置文件 application.yml 解释
配置文件 `application.yml` 是 Spring Boot 应用程序的配置文件，定义了程序运行时的各种参数，类似于一份“设置清单”。以下是内容及解释：
```yaml
spring:
  jpa:
    generate-ddl: true
    defer-datasource-initialization: true
    show-sql: true
    hibernate:
      ddl-auto: update
    properties:
      hibernate.auto_quote_keyword: true
  # JPA 配置，用于与数据库交互。generate-ddl 和 ddl-auto: update 表示自动生成和更新数据库表结构；show-sql: true 表示打印 SQL 语句，方便调试。

  application:
    name: admin3
  # 设置应用名称为 admin3，就像给程序取个名字。

  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://192.168.110.163:3306/admin3?characterEncoding=utf8
    username: admin
    password: admin123
  # 数据库连接配置，指定 MySQL 驱动、连接地址（192.168.110.163:3306）、数据库名称（admin3）、用户名和密码。characterEncoding=utf8 确保中文字符不乱码。

  sql:
    init:
      encoding: utf8
      data-locations: classpath:data.sql
      mode: always
      continue-on-error: true
  # 初始化 SQL 脚本配置，data-locations 指定初始化数据脚本位置，mode: always 表示每次启动都执行，continue-on-error: true 表示出错时继续执行。

  data:
    web:
      pageable:
        one-indexed-parameters: true
  # 分页参数配置，设置为从 1 开始计数（而不是默认的 0）。

  profiles:
    include: biz
  # 加载额外的配置文件 biz.yml，用于业务逻辑配置。

server:
  servlet:
    context-path: /admin3
  # 设置服务的前缀路径为 /admin3，例如访问接口时需加上 /admin3 前缀（如：http://域名/admin3/接口名）。
```

##### 3. 上传配置文件到目标服务器
使用 `config_manager.py` 脚本将配置文件上传到目标服务器：
```bash
python3 /root/PyDockerDeploy/config_manager.py \
--data """$(cat application.yml)""" \
--filepath "/opt/admin3-server/application.yml" \
--hosts "192.168.110.8"
```
命令解释：
- `python3 /root/PyDockerDeploy/config_manager.py`：运行配置文件上传工具。
- `--data """$(cat application.yml)"""`：指定配置文件内容，通过 `cat` 命令读取 `application.yml` 文件内容。
- `--filepath "/opt/admin3-server/application.yml"`：指定配置文件在目标服务器上的路径。
- `--hosts "192.168.110.8"`：指定目标服务器地址为 192.168.110.8。

##### 4. 部署 admin3-server 服务
使用 `deployer.py` 脚本部署服务：
```bash
python3 deployer.py -p admin3-server \
  --git_branch master \
  --image_tag liujun-v1.0 \
  --hosts 192.168.110.8 \
  --harbor_registry harbor.labworlds.cc \
  --docker_run "docker run -d -p 8080:8080 -v /opt/admin3-server/application.yml:/app/application.yml"
```
命令解释：
- `python3 deployer.py`：运行部署脚本。
- `-p admin3-server`：指定项目名称为 admin3-server。
- `--git_branch master`：指定代码分支为 master。
- `--image_tag liujun-v1.0`：指定镜像版本为 liujun-v1.0。
- `--hosts 192.168.110.8`：指定目标服务器为 192.168.110.8。
- `--harbor_registry harbor.labworlds.cc`：指定镜像仓库地址。
- `--docker_run "docker run -d -p 8080:8080 -v /opt/admin3-server/application.yml:/app/application.yml"`：
  - `-d`：表示后台运行容器。
  - `-p 8080:8080`：表示将服务器的 8080 端口映射到容器的 8080 端口。
  - `-v /opt/admin3-server/application.yml:/app/application.yml`：表示将目标服务器上的 `/opt/admin3-server/application.yml` 文件挂载到容器内的 `/app/application.yml` 路径。挂载就像“借用”主机上的文件，容器可以直接读取主机上的配置文件，确保服务启动时能加载正确的配置（例如数据库连接信息）。

##### 5. 配置 Nginx 反向代理
Nginx 配置文件 `shiqi.admin.labworlds.cc.conf` 内容如下，用于配置 HTTPS 访问和反向代理：
```nginx
# HTTPS server
server {
    listen 1443 ssl;
    server_name shiqi.admin.labworlds.cc;
    # 监听 1443 端口并启用 SSL，支持 HTTPS 访问，server_name 指定子域名。

    access_log /var/log/nginx/shiqi.admin.labworlds.cc.access.log json_combined;
    error_log /var/log/nginx/shiqi.admin.labworlds.cc.error.log warn;
    # 设置访问日志和错误日志路径，方便排查问题。

    ssl_certificate /etc/nginx/ssl/shiqi.admin.labworlds.cc/certificate.crt;
    ssl_certificate_key /etc/nginx/ssl/shiqi.admin.labworlds.cc/private.key;
    # 指定 SSL 证书和私钥路径，用于 HTTPS 加密通信。

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_stapling on;
    ssl_stapling_verify on;
    # SSL 优化配置，设置支持的协议和加密套件，提高安全性和性能。

    location / {
        proxy_pass http://admin_fronend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    # 配置前端代理，/ 路径下的请求转发到 admin_fronend（前端服务）。

    location /admin3/ {
        proxy_pass http://admin_backend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    # 配置后端代理，/admin3/ 路径下的请求转发到 admin_backend（后端服务）。
}

# HTTP 重定向到 HTTPS
server {
    listen 180;
    server_name shiqi.admin.labworlds.cc;
    return 301 https://$server_name:1443$request_uri;
}
# 将 180 端口的 HTTP 请求重定向到 HTTPS 1443 端口。

upstream admin_backend {
    server 192.168.110.8:8080 max_fails=3 fail_timeout=30s;
}
# 定义后端服务地址为 192.168.110.8:8080，设置健康检查参数。

upstream admin_fronend {
    server 192.168.110.8:8000 max_fails=3 fail_timeout=30s;
}
# 定义前端服务地址为 192.168.110.8:8000，设置健康检查参数。
```

- **跨域概念解释**：
  跨域（Cross-Origin Resource Sharing, CORS）是指浏览器在访问一个网站的资源时，如果资源的域名、协议或端口与当前网站的域名、协议或端口不同，浏览器会限制这种访问，这就是“同源策略”。例如，前端运行在 `https://shiqi.admin.labworlds.cc:1443`，后端接口在 `http://192.168.110.8:8080/admin3/`，由于域名和端口不同，浏览器会认为这是跨域请求，默认会阻止。
  - **解决方法**：在后端配置 CORS 允许跨域，或者通过 Nginx 反向代理将前后端请求统一到同一个域名下（如上配置，通过 `proxy_pass` 将请求转发到后端服务，浏览器认为请求是同源的）。
  - **通俗比喻**：就像你在家（前端）想点外卖（后端数据），但外卖店（后端）只送给附近的人（同源），这时你请一个中间人（Nginx）帮忙，外卖店以为中间人是附近的人，就把外卖送来了。

##### 6. 测试系统登录功能
- 访问前端地址：`https://shiqi.admin.labworlds.cc:1443`，尝试登录系统。
- 检查是否能正常调用后端接口（路径为 `/admin3/` 的请求），验证后端服务是否正常运行。
- 如果登录成功，说明后端发布完成；如果失败，检查日志（Nginx 日志或后端服务日志）定位问题。
