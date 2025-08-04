# Jenkins 持续集成与主从架构实践

## 学习目标
1. **掌握 Jenkins 主从架构配置**：理解主从架构的基本概念，学会配置 Agent（从节点），将学员的机器或模拟节点加入到 Jenkins Master 中，分担构建压力，解决单台服务器（4 核 8G）无法支持 30 多人同时构建的问题。
2. **熟悉 Git 代码拉取与凭据管理**：学习如何在 Jenkins 中配置 Git 私钥凭据，并通过 Pipeline 实现代码拉取，支持动态分支和 Tag。
3. **精通 Jenkins Pipeline 语法及发布流程**：掌握 Pipeline 基本语法，包括参数定义、条件判断、函数定义、全局变量及流程控制，并整合完整发布流程（构建、推送镜像、配置修改、部署等）。
4. **了解代码质量扫描（扩展）**：通过 SonarQube 集成学习代码扫描的基本方法，作为扩展内容供有兴趣的学员深入探索。
5. **实践与应用**：通过动手操作，学员能够将所学内容应用到实际环境中，课后可配置自己的 Agent 加入 Jenkins 系统，提升构建能力。


## 第一部分：Jenkins 主从架构配置

### 主从架构概念简介（面向小白，通俗理论解释）
- **什么是 Jenkins 主从架构？**：
  - 想象 Jenkins 是一个“大厨”（Master），负责安排菜单（任务调度）和接待顾客（用户界面），但它不亲自炒菜，因为厨房太小（服务器资源有限）。
  - Agent（Slave）就像是“助手”，专门负责炒菜（执行构建任务），可以有很多个助手在不同厨房工作（多台机器并行处理）。
  - Master 和 Agent 一起合作：Master 告诉助手做什么，助手完成任务后把结果汇报给 Master。
- **为何需要主从架构？**：
  - 现在我们只有一台服务器（4 核 8G），就像只有一个厨房，30 多人同时下单（构建任务），大厨忙不过来，顾客要排长队（任务排队）。
  - 主从架构的作用：增加“助手”（Agent），让任务分到多个厨房（机器）去做，这样大家不用等太久，效率大大提升。
- **主从架构如何工作？（结合 Mermaid 图）**：
  - 下面是一个简单的图，展示 Master 和 Agent 的关系：
    ```mermaid
    graph TD
        Master[Jenkins Master] -->|调度任务| Agent1[Agent 1]
        Master -->|调度任务| Agent2[Agent 2]
        Master -->|调度任务| Agent3[Agent 3]
        Agent1 -->|返回结果| Master
        Agent2 -->|返回结果| Master
        Agent3 -->|返回结果| Master
        subgraph 任务执行
            Agent1 --- Build1[构建任务 1]
            Agent2 --- Build2[构建任务 2]
            Agent3 --- Build3[构建任务 3]
        end
        subgraph 用户交互
            Master --- UI[用户界面]
            Master --- Config[配置管理]
        end
    ```
  - 图解说明：Master 负责用户交互和任务分配，Agent 负责具体执行任务，每个 Agent 可以处理不同的构建任务，互不干扰。
- **企业实践场景（简单举例）**：
  - 比如一个公司有 100 个开发人员，每天有几十个构建任务，如果只有一台机器，大家都要排队，可能一个任务要等几小时。
  - 配置 5 台 Agent 后，任务可以同时在 5 台机器上跑，等待时间大大缩短。
- **互动问题**：
  - “大家有没有遇到过任务排队的情况？如果只有一台机器忙不过来，你会怎么解决？想象自己是 Master，如何安排助手工作？”

### Agent 配置前的理论基础（面向小白）
- **Agent 是什么？**：
  - Agent 就像你家里的另一台电脑，告诉 Jenkins Master：“我可以帮忙干活！”然后 Master 就把任务发给它。
- **怎么连接 Master 和 Agent？**：
  - 最常见的方式是 SSH（就像用微信和朋友聊天，需要先加好友），我们要在 Master 上存好“私钥”，这样它可以直接和 Agent 沟通，不用每次输入密码。
- **Jenkins 可以自动安装 Agent**：
  - 好消息是，你不需要在 Agent 机器上手动安装任何 Jenkins 软件，只要装好 OpenJDK（一种运行 Java 的工具），Jenkins Master 会自动帮你安装 Agent 程序。
- **什么是 Label（标签）和 Node 指定？**：
  - 标签（Label）就像给 Agent 贴个小纸条，比如“擅长前端”或“擅长后端”，Master 看到标签就知道可以把任务分给符合条件的节点。
  - 在企业环境中，Agent 节点通常安装在跳板机上，为了确保任务运行在特定机器上（例如特定的跳板机），往往需要直接指定 Node 名称。如果指定节点有问题（例如离线），任务会报错，运维人员需要介入排查。
- **互动问题**：
  - “如果你有两台电脑，一台擅长跑大程序，一台适合跑小任务，你会怎么给它们贴标签？”

### 实践操作：配置 Agent（从节点）
- **场景说明**：
  - 由于现场可能无法为每位学员提供独立机器，我们将使用 VMware 启动 Ubuntu 系统后，配置 Agent 节点，或使用一台备用机器（如果有）。
  - 学员课后可参考步骤，在自己的机器上配置真实 Agent，加入到 Jenkins Master。
- **操作步骤（结合流程图）**：
  - 配置流程图（用 Mermaid 表示，方便学员理解步骤）：
    ```mermaid
    flowchart TD
        A[准备 Agent 环境: 安装 OpenJDK] --> B[配置 SSH 私钥到 Jenkins]
        B --> C[在 Master 上添加 Agent]
        C --> D[设置 Label 标签]
        D --> E[测试 Agent 可用性]
    ```
  1. **准备 Agent 环境（现场模拟）**（建议时间：10 分钟）
     - **理论解释**：Agent 节点只需要安装 OpenJDK，因为 Jenkins 的任务是用 Java 跑的，就像你要玩游戏必须装游戏软件。Jenkins Master 会自动安装 Agent 程序。
     - **实践演示**：在模拟 Agent 节点上安装 OpenJDK。
       - 真实环境中的安装命令（供学员课后参考）：
         ```bash
         sudo apt update
         sudo apt install fontconfig openjdk-21-jre -y
         java -version
         ```
       - 说明：运行 `java -version` 确认 OpenJDK 安装成功，输出应包含类似 `openjdk 21` 的信息。
  2. **配置 SSH 私钥到 Jenkins 凭据管理**
     - **理论解释**：我们所有主机都有公共密钥（公钥），现在需要把对应的私钥存到 Jenkins 里，就像把家门钥匙交给管家，让它能打开所有房间。
     - **OpenSSH转换**: `如果你的私钥以 -----BEGIN OPENSSH PRIVATE KEY-----` 开头，说明它是 OpenSSH 格式的私钥，需要转换为 PEM 格式。
       - 转换命令：
         ```bash
         ssh-keygen -p -m PEM -f ~/.ssh/id_rsa
         ```
     - **实践演示**：
       - 登录 Jenkins UI，进入“Manage Jenkins > Manage Credentials”。
       - 点击“Add Credentials”，选择类型为“SSH Username with private key”。
       - 设置参数：
         - ID：`agent-ssh-key`（凭据的唯一标识，供后续使用）。
         - Description：`SSH Key for Agents`（描述，方便识别）。
         - Username：`jenkins`（或你的 SSH 用户名）。
         - Private Key：选择“Enter directly”，粘贴你的私钥内容（确保私钥与主机公钥匹配）。
       - 保存凭据，确保私钥安全存储在 Jenkins 中。
     - **注意**：私钥非常重要，不要泄露，Jenkins 会加密存储，防止被盗用。
  3. **在 Jenkins Master 上添加 Agent**
     - **理论解释**：这就像在 Jenkins 里登记一个新员工，告诉它这个员工在哪、叫什么名字、擅长什么，Jenkins 会自动安装 Agent 程序。
     - **实践演示**：
       - 登录 Jenkins UI，进入“Manage Jenkins > Manage Nodes and Clouds > New Node”。
       - 输入节点名称（如 `node-192.168.110.6-shiqi`），选择“Permanent Agent”。
       - 配置参数：
         - Remote root directory：`/home/jenkins/agent`（Agent 工作目录，就像给助手安排一个办公桌）。
         - Labels：`node-192.168.110.6-shiqi`（标签，就像给助手贴上“擅长构建”的标记）。
         - Launch method：选择“Launch via SSH”（通过 SSH 连接）。
         - Host：Agent 的 IP 地址（例如 `192.168.110.6`，Docker 模拟时为宿主机 IP）。
         - Credentials：选择之前添加的凭据 `agent-ssh-key`。
       - 保存并启动 Agent，Jenkins 会通过 SSH 连接到 Agent 主机，并自动下载和安装 Agent 程序，检查状态是否为“在线”。
     - **命名规范**：学员课后配置自己的 Agent 时，节点名称必须遵循 `node-ip-拼音名字` 的格式，例如 `node-192.168.110.6-shiqi`，便于管理和识别。
  4. **测试 Agent 功能**
     - **理论解释**：测试就像试着让助手做一件小事，看看他能不能听懂指令并完成。在企业环境中，Agent 节点通常安装在跳板机上，为了确保任务运行在特定机器上，我们需要直接指定 Node 名称。如果指定的 Node 有问题（例如离线），任务会报错，运维人员需要介入排查。
     - **实践演示**：创建一个简单 Pipeline，通过指定 Node 名称让任务在特定 Agent 上运行：
       ```groovy
       pipeline {
           // 在指定标签的节点上运行
           agent { label 'node-192.168.110.6-shiqi' } 
           stages {
               stage('Build') {
                   steps {
                       echo 'Building on a specific node...'
                       sh 'hostname'
                   }
               }
           }
       }
       ```
     - **语法解释**：
       - 在 Pipeline 中，使用 `agent { label 'node-192.168.110.6-shiqi' }` 可以指定任务运行在具有特定标签的节点上，Jenkins 会动态选择符合条件的在线 Agent。
       - 在企业环境中，如果需要确保任务运行在特定跳板机上，可以直接指定 Node 名称，使用 `agent { node 'node-192.168.110.6-shiqi' }` 语法。这样可以明确任务运行位置，但如果该 Node 离线或有问题，任务会报错，运维人员需要介入排查：
         ```groovy
         pipeline {
             agent { node 'node-192.168.110.6-shiqi' } // 指定具体节点名称运行
             stages {
                 stage('Build') {
                     steps {
                         echo 'Building on a specific node...'
                         sh 'hostname'
                     }
                 }
             }
         }
         ```
     - 运行 Pipeline，查看日志确认任务是否在指定标签或具体 Node 上执行。
  5. **互动与答疑**
     - 鼓励学员记录配置步骤，课后在自己的机器上尝试加入 Agent。
     - 提问：“如果你的 Agent 显示离线，可能是什么原因？如何解决？在企业中指定具体 Node 名称和使用 Label 有什么不同？”

### 教学资源与准备
- **环境准备**：
  - Jenkins Master 服务器（已安装并运行）。
  - VMware主机 添加 Agent。
  - SSH 私钥（与主机公钥匹配，提前准备好用于演示）。
- **文档支持**：
  - 配置步骤文档（包括 OpenJDK 安装、SSH 私钥配置、Agent 添加步骤，面向小白，带图文说明）。
  - 命令参考（如 `apt install`、`java -version`）。
- **演示脚本**：
  - 简单 Pipeline 示例（通过 Label 或指定 Node 运行）。
- **可视化工具**：
  - Mermaid 图（架构图和流程图）已嵌入教学内容，课件中可提供图片或在线工具链接供学员查看。

### 学员练习与课后任务
- **现场练习**：
  - 观察 Agent 配置过程，记录关键步骤。
  - 若有条件，可尝试运行提供的 Pipeline，查看任务是否分配到 Agent。
- **课后任务**：
  - 在自己的机器上安装 OpenJDK，命令参考：
    ```bash
    sudo apt update
    sudo apt install fontconfig openjdk-21-jre -y
    java -version
    ```
  - 严格按照 `node-ip-拼音名字` 格式命名自己的 Agent 节点，例如 `node-192.168.110.6-shiqi`。
  - 参考文档完成 Agent 配置，确保 Agent 状态为“在线”。
  - 提交简单 Pipeline，通过 Label 或指定 Node 名称在自己的 Agent 上运行，查看运行结果。


