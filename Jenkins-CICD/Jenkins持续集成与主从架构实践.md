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
       - 登录 Jenkins UI，进入“Manage Jenkins > Manage Credentials > Stores scoped to Jenkins里面有个System > Global credentials (unrestricted) ”。
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
         - Remote root directory：`/home/ubuntu/jenkins/agent`（Agent 工作目录，就像给助手安排一个办公桌）。
         - Labels：`node-192.168.110.6-shiqi`（标签，就像给助手贴上“擅长构建”的标记）。
         - Launch method：选择“Launch via SSH”（通过 SSH 连接）。
         - Host：Agent 的 IP 地址（例如 `192.168.110.6`，Docker 模拟时为宿主机 IP）。
         - Credentials：选择之前添加的凭据 `agent-ssh-key`。
       - 保存并启动 Agent，Jenkins 会通过 SSH 连接到 Agent 主机，并自动下载和安装 Agent 程序，检查状态是否为“在线”。
     - **命名规范**：学员课后配置自己的 Agent 时，节点名称必须遵循 `node-ip-拼音名字` 的格式，例如 `node-192.168.110.6-shiqi`，便于管理和识别。
  4. **测试 Agent 功能**
     - **理论解释**：测试就像试着让助手做一件小事，看看他能不能听懂指令并完成。在企业环境中，Agent 节点通常安装在跳板机上，为了确保任务运行在特定机器上，我们需要直接指定 Node 名称。如果指定的 Node 有问题（例如离线），任务会报错，运维人员需要介入排查。
     - **实践演示**：创建一个简单 Pipeline，通过指定 Node 名称让任务在特定 Agent 上运行：
     - **job创建**: `training-agent-label-liujun`
        ```groovy
        properties([
            parameters([
                booleanParam(name: 'rendering', defaultValue: false, description: '是否要渲染页面'),
                string(name: 'git_branch', defaultValue: 'master', description: '请输入代码分支', trim: true),
                string(name: 'git_tag', defaultValue: '', description: '请输入代码TAG', trim: true),
                string(name: 'image', defaultValue: '', description: '请输入完整的镜像地址', trim: true),
                hidden(name: 'project_name', defaultValue: 'go-starter', description: '隐藏参数不给修改'),
                extendedChoice(
                    name: 'hosts', 
                    type: 'PT_CHECKBOX', 
                    value: '192.168.110.8,192.168.110.171,192.168.110.172', 
                    description: '请选择主机',
                    multiSelectDelimiter: ','
                ),
                string(name: 'docker_run', defaultValue: 'docker run -d -p 9006:8080 --restart=always', description: '请输入Docker运行命令', trim: true),
            ])
        ])
        pipeline {
            // 在指定标签的节点上运行
            agent { label 'node-192.168.110.6-shiqi' }
            stages {
                stage('Print String Param') {
                    when {
                      expression { params.rendering == false }
                    }
                    steps {
                        echo "String 参数值为: ${params.MY_STRING}"
                        sh "ifconfig"
                        sh "hostname"
                    }
                } 
            }
        }
        ```
     - **语法解释**：
       - 在 Pipeline 中，使用 `agent { label 'node-192.168.110.6-shiqi' }` 可以指定任务运行在具有特定标签的节点上，Jenkins 会动态选择符合条件的在线 Agent。
       - 创建job名为:  `training-agent-node-liujun`
       - 在企业环境中，如果需要确保任务运行在特定跳板机上，可以直接指定 Node 名称，使用 `agent { node 'node-192.168.110.6-shiqi' }` 语法。这样可以明确任务运行位置，但如果该 Node 离线或有问题，任务会报错，运维人员需要介入排查：
          ```groovy
          properties([
              parameters([
                  booleanParam(name: 'rendering', defaultValue: false, description: '是否要渲染页面'),
                  string(name: 'git_branch', defaultValue: 'master', description: '请输入代码分支', trim: true),
                  string(name: 'git_tag', defaultValue: '', description: '请输入代码TAG', trim: true),
                  string(name: 'image', defaultValue: '', description: '请输入完整的镜像地址', trim: true),
                  hidden(name: 'project_name', defaultValue: 'go-starter', description: '隐藏参数不给修改'),
                  extendedChoice(
                      name: 'hosts', 
                      type: 'PT_CHECKBOX', 
                      value: '192.168.110.8,192.168.110.171,192.168.110.172', 
                      description: '请选择主机',
                      multiSelectDelimiter: ','
                  ),
                  string(name: 'docker_run', defaultValue: 'docker run -d -p 9006:8080 --restart=always', description: '请输入Docker运行命令', trim: true),
              ])
          ])
          pipeline {
              // 在指定节点名上运行
              agent { node 'node-192.168.110.6-shiqi' }
              stages {
                  stage('Print String Param') {
                      when {
                        expression { params.rendering == false }
                      }
                      steps {
                          echo "String 参数值为: ${params.MY_STRING}"
                          sh "ifconfig"
                          sh "hostname"
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

好的，我会根据你的要求编写第二部分内容，移除时间和教学目标，专注于“Git 获取代码与私钥配置”，并结合你提供的案例代码，为每一行代码添加详细注释以方便学习。同时，我会确保内容面向小白，使用通俗易懂的语言和比喻解释概念。以下是第二部分的完整内容。

---

## 第二部分：Git 获取代码与私钥配置

### Git 基础与代码拉取概念简介（面向小白，通俗理论解释）
- **什么是 Git？**：
  - Git 就像一个“超级笔记本”，帮你记录和管理代码的每一次修改。你可以把代码存到“笔记本”里（仓库），随时拿出来看或者改。
  - 在 Jenkins 中，我们用 Git 把代码从远程仓库（如 Gitee 或 GitHub）拉到本地，就像从云端下载文件到你的电脑。
- **为何需要私钥配置？**：
  - 远程仓库不是随便就能访问的，就像你家门有锁，需要钥匙才能进去。SSH 私钥就是这把“钥匙”，Jenkins 要用它来证明身份，才能拉取代码。
  - 配置好私钥后，Jenkins 就可以通过 SSH 协议访问仓库，比如从 `https://gitee.com/Tender-Liu/go-starter` 克隆代码，而不需要每次手动输入密码。
- **Git 分支（Branch）和标签（Tag）是什么？**：
  - 分支（Branch）就像一本书的不同章节，比如 `master` 是主章节，`dev` 是开发中的草稿，你可以选择拉取哪个章节的代码。
  - 标签（Tag）就像书里的书签，标记某个特定版本，比如 `v1.0`，通常用于发布稳定版本。
  - 在 Jenkins 中，我们可以让用户选择拉取某个分支或某个标签的代码，非常灵活。
- **Jenkins 如何拉取代码？**：
  - Jenkins 通过 Pipeline 脚本执行 Git 命令，就像告诉一个助手：“去仓库拿代码，拿哪个分支或标签由用户决定。”
  - 下面是一个简单的图，展示 Jenkins 拉取代码的流程：
    ```mermaid
    graph TD
        User[用户] -->|选择分支或标签| Jenkins[Jenkins Master]
        Jenkins -->|使用私钥认证| GitRepo[Git 仓库]
        Jenkins -->|分配任务| Agent[Agent 节点]
        GitRepo -->|返回代码| Agent
        Agent -->|执行构建| Jenkins
    ```
  - 图解说明：用户通过 Jenkins 界面选择要拉取的分支或标签，Jenkins 使用私钥连接到 Git 仓库，将代码拉到指定 Agent 节点上执行任务。
- **互动问题**：
  - “大家有没有用过 Git 拉取代码？如果要拉取特定版本的代码，你会选择分支还是标签？”

### 实践操作：配置 Git 私钥与代码拉取
- **场景说明**：
  - 我们将通过 Jenkins 配置 SSH 私钥，用于访问 Git 仓库（以 `https://gitee.com/Tender-Liu/go-starter` 为例）。
  - 然后编写 Pipeline 脚本，让用户可以选择分支（Branch）或标签（Tag）来拉取代码，并在特定 Agent 节点上执行任务。
  - 本节提供完整代码案例，并为每一行添加详细注释，方便学员学习和课后实践。
- **操作步骤（结合流程图）**：
  - 配置和拉取代码流程图（用 Mermaid 表示，方便学员理解步骤）：
    ```mermaid
    flowchart TD
        A[生成 SSH 公私钥对] --> B[将公钥添加到 Git 仓库]
        B --> C[将私钥存储到 Jenkins 凭据]
        C --> D[编写 Pipeline 拉取代码]
        D --> E[运行 Pipeline 测试拉取]
    ```
  1. **生成 SSH 公私钥对**：
     - **理论解释**：SSH 密钥就像一对门锁和钥匙，公钥（锁）放在 Git 仓库，私钥（钥匙）给 Jenkins，用来打开仓库大门。
     - **实践步骤**：
       - 在本地或服务器上生成密钥对，命令如下（供学员参考，现场可使用预生成的密钥）：
         ```bash
         ssh-keygen -t rsa -b 4096 -C "Jenkins Git Access" -N "" -f ~/.ssh/jenkins-git-key
         ```
       - 说明：`-t rsa` 指定加密类型，`-b 4096` 设置密钥强度，`-C` 是注释，`-N ""` 表示无密码，`-f` 指定文件路径。
       - 生成后，公钥文件是 `~/.ssh/jenkins-git-key.pub`，私钥文件是 `~/.ssh/jenkins-git-key`。
  2. **将公钥添加到 Git 仓库（如 Gitee）**：
     - **理论解释**：公钥就像你告诉仓库：“这是我的身份证明，允许持有对应私钥的人进来。”
     - **实践步骤**：
       - 登录 Gitee 账户，进入“设置 > SSH 公钥”。
       - 复制公钥内容（`cat ~/.ssh/jenkins-git-key.pub`），粘贴到 Gitee 的公钥输入框，保存。
       - 说明：每个仓库或平台（如 GitHub、GitLab）都需要添加公钥，确保 Jenkins 能访问目标仓库。
  3. **将私钥存储到 Jenkins 凭据管理**：
     - **理论解释**：私钥是访问仓库的钥匙，必须安全存放在 Jenkins 里，就像把钥匙锁在保险箱，只有需要时拿出来用。
     - **实践演示**：
       - 登录 Jenkins UI，进入“Manage Jenkins > Manage Credentials”。
       - 点击“Add Credentials”，选择类型为“SSH Username with private key”。
       - 设置参数：
         - ID：`git-ssh-key`（凭据的唯一标识，供 Pipeline 使用）。
         - Description：`SSH Key for Git Access`（描述，方便识别）。
         - Username：`git`（或你的 Git 用户名）。
         - Private Key：选择“Enter directly”，粘贴你的私钥内容（`cat ~/.ssh/jenkins-git-key` 获取）。
       - 保存凭据，确保私钥安全存储在 Jenkins 中。
     - **注意**：私钥非常重要，不要泄露，Jenkins 会加密存储，防止被盗用。
  4. **编写 Pipeline 脚本拉取代码**：
     - **理论解释**：Pipeline 就像一份任务清单，告诉 Jenkins 去哪个仓库拿代码，拿哪个分支或标签，拿完后做什么。
     - **实践演示**：以下是一个完整的 Pipeline 脚本案例，包含用户参数选择（如分支、标签）和 Git 代码拉取逻辑，每行代码都有详细注释，方便学习。
       ```groovy
       // docker镜像标签，按照时间-构建编号命名
       def getBuildTag(){
           return new Date().format('MMddHH') + "-${env.BUILD_ID}"
       }
       // 定义 Pipeline 参数，允许用户在运行时选择拉取代码的分支、标签等信息
       properties([
           parameters([
               // 布尔参数：是否要渲染页面，默认值为 false，勾选为 true
               booleanParam(name: 'rendering', defaultValue: false, description: '是否要渲染页面'),
               // 字符串参数：输入 Git 分支名称，默认值为 'master'，trim 去除首尾空格
               string(name: 'git_branch', defaultValue: 'master', description: '请输入代码分支', trim: true),
               // 字符串参数：输入 Git 标签名称，默认值为空，trim 去除首尾空格
               string(name: 'git_tag', defaultValue: '', description: '请输入代码TAG', trim: true),
               // 字符串参数：输入镜像地址，默认值为空，trim 去除首尾空格
               string(name: 'image', defaultValue: '', description: '请输入完整的镜像地址', trim: true),
               // 隐藏参数：项目名称，默认值为 'go-starter'，用户不可见也不可修改
               hidden(name: 'project_name', defaultValue: 'go-starter', description: '隐藏参数不给修改'),
               // 扩展选择参数：多选主机 IP，支持勾选多个选项，用逗号分隔
               extendedChoice(
                   name: 'hosts', 
                   type: 'PT_CHECKBOX', 
                   value: '192.168.110.8,192.168.110.171,192.168.110.172', 
                   description: '请选择主机',
                   multiSelectDelimiter: ','
               ),
               // 字符串参数：输入 Docker 运行命令，默认值已提供，trim 去除首尾空格
               string(name: 'docker_run', defaultValue: 'docker run -d -p 9006:8080 --restart=always', description: '请输入Docker运行命令', trim: true),
           ])
       ])

       // 定义 Pipeline 主结构
       pipeline {
           // 指定运行节点：任务在特定 Agent 节点上执行，企业中常指定跳板机
           agent { node 'node-192.168.110.6-shiqi' }
           // 设置 Pipeline 选项
           options {
               // 保留最近 30 个构建记录，防止日志过多占用空间
               buildDiscarder(logRotator(numToKeepStr: '30'))
               // 启用 ANSI 颜色输出，日志显示更美观
               ansiColor('xterm')
           }
           // 定义环境变量，在整个 Pipeline 中都可以使用
           environment {
               // 自定义变量：获取构建标签（通常是时间戳或版本号），具体实现可由函数定义
               images_tag = getBuildTag()
               // 自定义变量：初始化分支变量，稍后根据参数赋值
               branch = ""
           }
           // 定义 Pipeline 阶段
           stages {
               // 阶段 1：Git 克隆代码，只有当分支或标签参数不为空时才执行
               stage('Git Clone') {
                   when {
                       // 条件表达式：如果 git_branch 或 git_tag 参数有一个不为空，则执行此阶段
                       expression { params.rendering == false && (params.git_branch != "" || params.git_tag != "") }
                   }
                   steps {
                       // 使用脚本块，允许更复杂的逻辑处理
                       script {
                           // 判断逻辑：如果用户输入了标签（Tag），则拉取指定 Tag 的代码
                           if (params.git_tag != "") {
                               // 使用 GitSCM 插件拉取代码，指定 Tag 引用
                               checkout([$class: 'GitSCM',
                                   // 指定 Tag 路径，格式为 refs/tags/标签名
                                   branches: [[name: "refs/tags/${params.git_tag}"]],
                                   // 不生成子模块配置
                                   doGenerateSubmoduleConfigurations: false,
                                   // 无额外扩展配置
                                   extensions: [],
                                   // 指定 Git 远程仓库信息和凭据
                                   userRemoteConfigs: [[
                                       // 使用之前配置的私钥凭据 ID
                                       credentialsId: '4c4463c8-1c2b-480d-91f1-46ca481f08ab',
                                       // 仓库地址，指向 Gitee 上的 go-starter 项目
                                       url: 'git@gitee.com:Tender-Liu/go-starter.git'
                                   ]]
                               ])
                               // 将 branch 变量赋值为选择的 Tag，便于后续使用
                               branch = git_tag
                           } else {
                               // 如果未输入 Tag，则拉取指定分支（Branch）的代码
                               git branch: params.git_branch, 
                                   // 使用之前配置的私钥凭据 ID
                                   credentialsId: '4c4463c8-1c2b-480d-91f1-46ca481f08ab', 
                                   // 仓库地址，指向 Gitee 上的 go-starter 项目
                                   url: 'git@gitee.com:Tender-Liu/go-starter.git'
                               // 将 branch 变量赋值为选择的分支，便于后续使用
                               branch = git_branch
                           }
                       }
                   }
               }
               // 阶段 2：打印参数信息和测试环境，只有当 rendering 参数为 false 时执行
               stage('Print String Param') {
                   when {
                       // 条件表达式：如果 rendering 参数为 false，则执行此阶段
                       expression { params.rendering == false }
                   }
                   steps {
                       // 打印用户输入的参数值（假设有 MY_STRING 参数，实际案例中需替换）
                       echo "String 参数值为: ${branch}"
                       // 执行 shell 命令：显示网络配置信息，用于调试
                       sh "ifconfig"
                       // 执行 shell 命令：显示主机名，确认任务运行在哪个节点
                       sh "hostname"
                   }
               } 
           }
       }
       ```
     - **代码说明**：
       - 上面的 Pipeline 脚本非常灵活，允许用户通过参数选择分支（`git_branch`）或标签（`git_tag`）来拉取代码。
       - 使用了 `credentialsId` 调用之前存储的私钥，确保 Jenkins 能安全访问 Git 仓库（如 `git@gitee.com:Tender-Liu/go-starter.git`）。
       - 指定了具体节点 `node-192.168.110.6-shiqi` 运行任务，符合企业中跳板机场景需求。
       - 包含多种参数类型（布尔、字符串、隐藏、多选等），展示了 Jenkins 参数化的强大功能。
  5. **运行 Pipeline 测试代码拉取**：
     - **理论解释**：运行 Pipeline 就像让 Jenkins 按照清单做事，看看它能不能顺利拿到代码并执行任务。
     - **实践演示**：
       - 在 Jenkins UI 中创建或编辑一个 Pipeline 项目，粘贴上述脚本。
       - 点击“Build with Parameters”，输入参数（如分支 `master` 或标签 `v1.0`）。
       - 运行构建，查看日志确认代码是否成功拉取，是否在指定节点上执行。
     - **注意**：如果拉取失败，常见原因是私钥配置错误或网络问题，需检查凭据 ID 和仓库 URL 是否正确。
  6. **互动与答疑**：
     - 鼓励学员记录 Pipeline 脚本，课后尝试修改参数（如分支或标签）运行。
     - 提问：“如果代码拉取失败，你会检查哪些地方？分支和标签有什么区别？”


## 第三部分：Jenkins Pipeline 语法学习（理论篇）

### Pipeline 语法简介（面向小白，通俗理论解释）
- **什么是 Jenkins Pipeline？**：
  - Pipeline 就像一份“任务清单”，告诉 Jenkins 要做什么事，按什么顺序做。比如，先拉代码，再编译，就像做菜的步骤：先洗菜，再切菜。
  - 在 Jenkins 中，Pipeline 用代码（基于 Groovy 语言）编写，可以自动化整个构建和发布流程，非常灵活。不用手动点击界面配置任务，而是把所有步骤都写成代码，方便管理和重复使用。
- **为何使用 Pipeline？**：
  - 传统的 Jenkins 任务靠手动点界面配置，就像手写菜单，复杂又容易出错。Pipeline 把步骤写成代码，就像用电脑程序控制整个厨房，效率高还能重复使用。
  - Pipeline 支持条件判断、循环、参数选择、多个阶段，可以轻松实现复杂的自动化流程，比如只在特定条件下部署，或者同时处理多个任务。
- **Pipeline 的基本结构**：
  - Pipeline 就像一本书，分为几个大章节：全局设置、用户输入、执行流程。每个章节有具体内容，比如“在哪台机器上做”、“保留多少日志”、“有哪些步骤”等。
  - 下面是一个简单的图，展示 Pipeline 的结构：
    ```mermaid
    graph TD
        Pipeline[Pipeline 脚本] -->|全局设置| Settings[全局设置]
        Pipeline -->|用户输入| Parameters[参数配置 Parameters]
        Pipeline -->|执行流程| MainPipeline[Pipeline 主结构]
        MainPipeline --> Agent[Agent: 指定运行节点]
        MainPipeline --> Options[Options: 构建选项]
        MainPipeline --> Environment[Environment: 环境变量]
        MainPipeline --> Stages[Stages: 执行阶段]
        Stages --> Stage1[Stage 1]
        Stages --> Stage2[Stage 2]
        Stage1 --> Steps[Steps: 具体步骤]
    ```
  - 图解说明：Pipeline 脚本包含全局设置、参数配置和主结构，主结构又分为运行节点、构建选项、环境变量和多个阶段，每个阶段有具体步骤。
- **Pipeline 的两种类型**：
  - **声明式 Pipeline（Declarative Pipeline）**：就像填表格，语法固定，结构清晰，适合大多数场景，容易上手。我们本节主要讲这种类型。
  - **脚本式 Pipeline（Scripted Pipeline）**：就像写自由作文，语法更灵活，但更复杂，适合高级用户定制特殊逻辑。
- **互动问题**：
  - “大家有没有手动配置过 Jenkins 任务？如果可以用代码自动化整个流程，你觉得会带来什么好处？”


### Pipeline 语法核心概念（一步步理解）
下面我们逐步讲解 Pipeline 语法的主要组成部分，用通俗的语言解释每个概念的作用，帮助大家打好理论基础。

#### **1. pipeline 块：任务清单的起点**
- **是什么**：`pipeline` 是整个脚本的根节点，就像“任务清单”的标题，告诉 Jenkins 这是一个 Pipeline 任务，所有内容都写在这个大括号 `{}` 里面。
- **通俗解释**：就像做菜前先写下“今日菜单”这个标题，后面所有步骤都围绕这个菜单展开。
- **作用**：定义整个自动化流程的开始和结束，包含所有设置和步骤。

#### **2. agent：指定任务在哪里运行**
- **是什么**：`agent` 定义了任务在哪台机器上执行，比如 `agent any` 表示在任意可用节点上运行。
- **通俗解释**：就像指定“在哪个厨房做菜”，可以是随便哪个厨房（`any`），也可以是特定的厨房（某个节点标签）。
- **作用**：确保任务有地方运行，Jenkins 会根据 `agent` 分配资源。

#### **3. stages 和 stage：任务的阶段划分**
- **是什么**：`stages` 是任务的主要阶段集合，里面包含多个 `stage`，每个 `stage` 是一个具体的阶段，比如“拉代码”、“构建”。
- **通俗解释**：`stages` 就像做菜的“步骤列表”，而每个 `stage` 是一个步骤，比如“洗菜”、“切菜”。Jenkins 会按顺序执行每个阶段。
- **作用**：把大任务拆分成小步骤，方便管理和查看进度，每个阶段可以独立成功或失败。

#### **4. steps：阶段内的具体操作**
- **是什么**：`steps` 是每个 `stage` 里面的具体操作，比如执行命令、打印日志。
- **通俗解释**：就像“洗菜”这个阶段的具体动作是“打开水龙头、冲洗蔬菜”，`steps` 就是告诉 Jenkins 每个阶段到底要做什么。
- **作用**：定义每个阶段的具体任务内容，是 Pipeline 的核心执行部分。

#### **5. environment：定义环境变量**
- **是什么**：`environment` 用来定义一些固定值（变量），比如应用名称、服务器地址，在整个任务中都可以用。
- **通俗解释**：就像做菜前的“配料表”，提前准备好盐、酱油的量（变量值），在做菜的任何步骤都能拿来用，省得每次都重新写。
- **作用**：简化脚本编写，统一管理常用值，避免重复硬编码。

#### **6. options：设置全局选项**
- **是什么**：`options` 用来设置流水线的全局规则，比如保留多少次构建记录、超时时间等。
- **通俗解释**：就像设定做菜的规则：“菜单只保留最近 10 份，超过 30 分钟没做完就别做了。”用来控制任务的行为。
- **作用**：优化任务运行，防止资源浪费，比如清理旧日志、避免任务卡死。

#### **7. parameters：用户输入参数**
- **是什么**：`parameters` 允许用户在运行任务时输入参数，比如选择部署环境（开发、测试、生产）。
- **通俗解释**：就像问顾客：“你要辣的还是不辣的？” 让任务更灵活，用户可以根据需求选择不同的设置。
- **作用**：增加任务的交互性和可定制性，满足不同场景需求。

#### **8. triggers：触发任务的方式**
- **是什么**：`triggers` 定义任务如何被触发，比如定时运行、代码提交时自动运行。
- **通俗解释**：就像设定闹钟：“每天早上 8 点自动开始做菜。” 让任务不需要手动点击就能运行。
- **作用**：实现自动化触发，节省人工操作时间。

#### **9. post：任务后的善后工作**
- **是什么**：`post` 定义任务或阶段结束后要做什么，比如成功时发通知，失败时报警。
- **通俗解释**：就像做完菜后的“收拾桌子”，成功就告诉大家“菜做好了”，失败就喊“菜烧糊了，快来看看”。
- **作用**：处理任务结果，通知团队或记录日志，方便后续跟进。

#### **10. when：条件判断**
- **是什么**：`when` 用来设置条件，只有满足条件时才执行某个阶段。
- **通俗解释**：就像说“只有下雨天才带伞”，在 Pipeline 中可以设置“只有选择生产环境才部署”。
- **作用**：让流程更智能，根据不同情况执行不同步骤。

### 注意事项（小白常见问题解答）
- **Q：Pipeline 语法难学吗？**  
  - A：不难！尤其是声明式 Pipeline，结构很固定，就像填表格，只要记住几个关键部分（比如 `stages`、`steps`），就能写出基本脚本。咱们会一步步学，慢慢加深。
- **Q：我需要学 Groovy 语言吗？**  
  - A：不需要特别学！声明式 Pipeline 的语法很简单，基本就是几个固定关键词，日常用到的 Groovy 知识很少，后续如果有复杂需求再学也不迟。
- **Q：Pipeline 能做什么？**  
  - A：几乎所有自动化任务都可以，比如拉代码、编译、测试、部署、发通知，甚至跨团队协作。只要是重复性工作，Pipeline 都能帮你省时间。

### 互动思考题
- **思考 1**：如果你的项目需要每天自动构建一次，应该用哪个语法部分来实现？（提示：想想“触发”相关的概念）
- **思考 2**：如果一个任务有多个步骤，某个步骤失败了，你希望收到通知，应该用哪个语法部分？（提示：想想“善后工作”）
- **思考 3**：如果想让用户选择是构建“开发环境”还是“测试环境”，应该用哪个语法部分？（提示：想想“用户输入”）

### 总结
- 本节我们详细介绍了 Jenkins Pipeline 的理论基础，讲解了声明式 Pipeline 的核心语法概念，包括 `pipeline`、`agent`、`stages`、`steps` 等。
- 通过通俗的比喻（比如“做菜步骤”），希望大家对 Pipeline 的结构和作用有了初步认识，理解了每个语法部分的用途。
- 下一部分我们会结合具体的代码示例，逐步实践这些语法，从最简单的脚本开始，一点一点加深，真正掌握 Pipeline 的用法。基础要打牢，慢慢来，不着急！

## 第三部分：Jenkins Pipeline 语法学习（实践篇）

### 实践学习目标
- 本节通过一系列小实验，逐步学习 Jenkins Pipeline 的核心语法，包括 `parameters`、`options`、`environment`、`stages`、`when` 条件判断等。
- 每个实验聚焦 1-2 个语法点，配合通俗解释和简单代码，确保大家能理解并动手实践。
- 最后通过一个综合实验，将所有语法点整合到一个脚本中，并基于实际代码进行练习，复习和巩固所学内容。
- 实验任务名称统一格式为 `training-类型-姓名拼音`，比如 `training-parameters-shiqi`。
- **注意**：所有实验均指定运行在特定节点 `node-192.168.110.6-shiqi` 上。

### 实验环境准备
- **前提**：确保你的 Jenkins 环境已搭建好，能正常创建和运行 Pipeline 任务，且节点 `node-192.168.110.6-shiqi` 已配置并可用。
- **操作步骤**：
  1. 登录 Jenkins，点击“新建 Item”。
  2. 输入任务名称（按 `training-类型-姓名拼音` 格式），选择“Pipeline”类型，点击“OK”。
  3. 在“Pipeline”配置中，选择“Pipeline script”，将实验代码粘贴进去，保存并运行。
- **注意事项**：如果运行报错，检查代码拼写或节点是否可用，或查看“控制台输出”（Console Output）日志，常见问题是语法格式错误或节点不可用。

### 实验 1：学习 `parameters` 语法（用户输入参数）
- **目标**：理解 `parameters` 的作用，学习如何让用户在运行任务时输入参数。
- **通俗解释**：`parameters` 就像点餐时问顾客：“你要辣的还是不辣的？” 让任务更灵活，用户可以根据需求选择不同的设置。
- **代码示例**：
  ```groovy
  properties([
      parameters([
          booleanParam(name: 'isGreeting', defaultValue: true, description: '是否要打招呼'),
          string(name: 'userName', defaultValue: '小白', description: '请输入你的名字', trim: true)
      ])
  ])

  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      stages {
          stage('Say Hello') {
              steps {
                  echo "嗨，${params.userName}！欢迎学习 Jenkins Pipeline！"
                  script {
                      if (params.isGreeting) {
                          echo "很高兴见到你！"
                      } else {
                          echo "不打招呼，直接进入学习吧！"
                      }
                  }
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-parameters-shiqi`
  - 这里只是介绍 `parameters` 语法哦！运行任务前，Jenkins 会显示参数输入框，你可以勾选是否打招呼，输入名字。
  - 运行后，查看日志，观察是否打印了你的名字和对应的招呼语。
- **语法重点**：
  - `booleanParam`：布尔类型参数，勾选或不勾选，比如 `isGreeting`。
  - `string`：字符串类型参数，输入文本，比如 `userName`。
  - `params.参数名`：引用参数值，比如 `${params.userName}`。
- **互动问题**：
  - “运行任务时，改一下名字和勾选选项，看看日志输出有何变化？”
  - “试着添加一个新参数，比如 `hobby`，并在 `echo` 中输出。”

### 实验 2：学习 `options` 语法（全局选项设置）
- **目标**：理解 `options` 的作用，学习如何设置构建规则。
- **通俗解释**：`options` 就像设定做菜的规则：“菜单只保留最近 10 份，超过 30 分钟没做完就别做了。” 用来控制任务的行为。
- **代码示例**：
  ```groovy
  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      options {
          buildDiscarder(logRotator(numToKeepStr: '5'))
          timeout(time: 10, unit: 'MINUTES')
      }
      stages {
          stage('Test Options') {
              steps {
                  echo "这是一个测试任务，设置了只保留 5 次构建记录。"
                  echo "如果任务超过 10 分钟，会自动超时停止。"
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-options-shiqi`
  - 这里只是介绍 `options` 语法哦！运行任务后，查看 Jenkins 界面，观察构建历史是否只保留 5 次。
  - 注意 `timeout` 设置了 10 分钟超时，实际任务很短，不会触发，但你可以后续测试长任务时观察效果。
- **语法重点**：
  - `buildDiscarder(logRotator(numToKeepStr: '5'))`：只保留最近 5 次构建记录，节省空间。
  - `timeout(time: 10, unit: 'MINUTES')`：设置超时时间，防止任务卡死。
- **互动问题**：
  - “运行几次任务后，检查构建历史，是否只保留了 5 次记录？”
  - “试着把 `numToKeepStr` 改成 '3'，看看效果如何？”

### 实验 3：学习 `environment` 和自定义函数
- **目标**：理解 `environment` 的作用，学习定义环境变量和简单函数。
- **通俗解释**：`environment` 就像做菜前的“配料表”，提前准备好固定值（变量），随时用。自定义函数就像自己写个小工具，方便重复计算或处理。
- **代码示例**：
  ```groovy
  // 定义一个函数，返回当前时间加构建编号的标签
  def getBuildTag() {
      return new Date().format('MMddHH') + "-${env.BUILD_ID}"
  }

  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      environment {
          image_tag = getBuildTag()
          project_name = "MyApp"
      }
      stages {
          stage('Show Environment') {
              steps {
                  echo "当前构建标签是：${image_tag}"
                  echo "项目名称是：${project_name}"
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-environment-shiqi`
  - 这里只是介绍 `environment` 和函数语法哦！运行任务后，查看日志，观察构建标签是否包含时间和构建编号。
- **语法重点**：
  - `environment`：定义全局环境变量，比如 `image_tag`。
  - `def 函数名()`：定义函数，比如 `getBuildTag()`，可以重复调用。
  - `变量名`：引用环境变量，比如 `${image_tag}`。
- **互动问题**：
  - “运行任务后，构建标签是什么格式？多次运行是否会变？”
  - “试着修改函数 `getBuildTag()`，比如只返回日期不加构建编号，看看效果如何？”

### 实验 4：学习 `when` 语法（条件判断）
- **目标**：理解 `when` 的作用，学习如何根据条件执行阶段。
- **通俗解释**：`when` 就像说“只有下雨天才带伞”，在 Pipeline 中可以设置“只有特定条件才执行某个步骤”。
- **代码示例**：
  ```groovy
  properties([
      parameters([
          booleanParam(name: 'runTest', defaultValue: false, description: '是否运行测试')
      ])
  ])

  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      stages {
          stage('Normal Step') {
              steps {
                  echo "这是普通步骤，总是会执行。"
              }
          }
          stage('Conditional Test') {
              when {
                  expression { params.runTest == true }
              }
              steps {
                  echo "只有勾选了运行测试，才会执行这一步！"
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-when-shiqi`
  - 这里只是介绍 `when` 语法哦！运行任务时，可以选择是否勾选“运行测试”，观察日志中是否执行了条件步骤。
- **语法重点**：
  - `when { expression { 条件 } }`：条件判断，只有条件为真时执行该阶段。
- **互动问题**：
  - “不勾选‘运行测试’时，日志里打印了什么？勾选后呢？”
  - “试着把条件改成 `params.runTest == false`，看看效果如何？”

### 实验 5：学习 `script` 语法（动态逻辑处理）
- **目标**：理解 `script` 的作用，学习如何在声明式 Pipeline 中嵌入脚本逻辑。
- **通俗解释**：`script` 就像在固定菜单中加点“自由发挥”，可以在声明式 Pipeline 中写更灵活的逻辑，比如根据参数选择不同操作。
- **代码示例**：
  ```groovy
  properties([
      parameters([
          string(name: 'gitBranch', defaultValue: 'master', description: '请输入分支名', trim: true)
      ])
  ])

  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      environment {
          branch = ""
      }
      stages {
          stage('Set Branch') {
              steps {
                  script {
                      if (params.gitBranch != "") {
                          branch = params.gitBranch
                          echo "设置分支为：${branch}"
                      } else {
                          branch = "default"
                          echo "分支为空，使用默认值：${branch}"
                      }
                  }
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-script-shiqi`
  - 这里只是介绍 `script` 语法哦！运行任务时，输入分支名或留空，观察日志中分支值是否正确设置。
- **语法重点**：
  - `script { ... }`：嵌入脚本逻辑，处理复杂判断或动态赋值。
- **互动问题**：
  - “输入一个分支名后，日志显示了什么？留空呢？”
  - “试着在 `script` 中加一个 `else if`，比如分支是 'dev' 时输出特别提示。”

### 综合实验：整合所有语法（基于实际代码的构建流程）
- **目标**：将之前学习的语法点整合到一个 Pipeline 脚本中，基于你提供的实际代码，模拟一个完整的构建流程，复习和巩固所学内容。
- **通俗解释**：之前每个实验就像学做菜的单个步骤（洗菜、切菜），现在我们把所有步骤组合起来，基于你的代码做一道完整的“菜”，感受整个流程的自动化。
- **代码示例**：
  ```groovy
  // Docker 镜像标签，按照时间-构建编号命名
  def getBuildTag() {
      return new Date().format('MMddHH') + "-${env.BUILD_ID}"
  }

  properties([
      parameters([
          booleanParam(name: 'rendering', defaultValue: false, description: '是否要渲染页面'),
          string(name: 'git_branch', defaultValue: 'master', description: '请输入代码分支', trim: true),
          string(name: 'git_tag', defaultValue: '', description: '请输入代码TAG', trim: true),
          string(name: 'image', defaultValue: '', description: '请输入完整的镜像地址', trim: true),
          hidden(name: 'project_name', defaultValue: 'go-starter', description: '隐藏参数不给修改'),
          extendedChoice(
              name: 'hosts', 
              type: 'PT_CHECKBOX', 
              value: '192.168.110.8,192.168.110.171,192.168.110.172', 
              description: '请选择主机',
              multiSelectDelimiter: ','
          ),
          string(name: 'docker_run', defaultValue: 'docker run -d -p 9006:8080 --restart=always', description: '请输入Docker运行命令', trim: true),
      ])
  ])

  pipeline {
      agent { node 'node-192.168.110.6-shiqi' }
      options {
          buildDiscarder(logRotator(numToKeepStr: '30'))
          ansiColor('xterm')
      }
      environment {
          image_tag = getBuildTag()
          branch = ""
      }
      stages {
          stage('Git Clone') {
              when {
                  expression { params.rendering == false && (params.git_branch != "" || params.git_tag != "") }
              }
              steps {
                  script {
                      if (params.git_tag != "") {
                          checkout([$class: 'GitSCM',
                              branches: [[name: "refs/tags/${params.git_tag}"]],
                              doGenerateSubmoduleConfigurations: false,
                              extensions: [],
                              userRemoteConfigs: [[
                                  credentialsId: '4c4463c8-1c2b-480d-91f1-46ca481f08ab',
                                  url: 'git@gitee.com:Tender-Liu/go-starter.git'
                              ]]
                          ])
                          branch = params.git_tag
                          echo "已克隆 TAG：${params.git_tag}，分支设置为：${branch}"
                      } else {
                          git branch: params.git_branch, credentialsId: '4c4463c8-1c2b-480d-91f1-46ca481f08ab', url: 'git@gitee.com:Tender-Liu/go-starter.git'
                          branch = params.git_branch
                          echo "已克隆分支：${params.git_branch}，分支设置为：${branch}"
                      }
                  }
              }
          }
          stage('Print String Param') {
              when {
                  expression { params.rendering == false }
              }
              steps {
                  echo "当前项目：${params.project_name}"
                  echo "构建标签：${image_tag}"
                  sh "ifconfig"
                  sh "hostname"
              }
          }
          stage('Summary') {
              steps {
                  echo "任务总结：构建完成！"
                  echo "分支/TAG：${branch}"
                  echo "Docker 运行命令：${params.docker_run}"
                  echo "目标主机：${params.hosts}"
              }
          }
      }
  }
  ```
- **实验说明**：
  - 任务名称：`training-comprehensive-shiqi`
  - 这里是综合实验哦！运行任务时，输入参数（分支名、TAG、镜像地址、主机等），观察日志中每个阶段是否按预期执行。
  - 这个实验整合了 `parameters`（用户输入多种参数）、`options`（构建规则）、`environment`（环境变量）、自定义函数（构建标签）、`when`（条件判断）、`script`（动态逻辑）。
  - 代码基于你提供的实际脚本，增加了额外的日志输出和总结阶段，便于观察和学习。
- **语法复习**：
  - `parameters`：用户输入分支、TAG、镜像地址、主机等。
  - `options`：限制构建记录和设置颜色输出。
  - `environment` 和函数：动态生成构建标签，定义分支变量。
  - `script`：根据输入动态设置分支或 TAG。
  - `when`：根据参数决定是否执行克隆和打印阶段。
- **互动问题**：
  - “运行任务时，输入分支名和 TAG，观察日志中分支设置是否正确？”
  - “不勾选‘是否渲染页面’时，哪些阶段会执行？勾选后呢？”
  - “试着添加一个新阶段，只有当镜像地址不为空时输出‘准备构建镜像：${params.image}’。”

### 注意事项（小白常见问题解答）
- **Q：运行任务时没有参数输入框怎么办？**  
  - A：确保代码中正确定义了 `properties([parameters([...])])`，并且保存后重新运行任务，参数会在界面上显示。
- **Q：条件 `when` 不生效怎么办？**  
  - A：检查条件表达式是否正确，比如 `params.rendering == false`，确保参数名和逻辑无误，查看日志确认。
- **Q：节点运行报错怎么办？**  
  - A：确保节点 `node-192.168.110.6-shiqi` 在 Jenkins 中已正确配置且在线，检查“控制台输出”日志确认错误原因。

### 互动练习
- **练习 1**：基于综合实验，添加一个新阶段 `Check Image`，只有当 `image` 参数不为空时执行，输出“准备构建镜像：${params.image}”。
- **练习 2**：基于综合实验，添加一个新参数 `buildVersion`，默认值为空，并在 `Summary` 阶段输出版本信息。
- **思考题**：如果想让综合实验每天自动运行一次，应该添加哪个语法部分？（提示：搜索 `triggers` 关键字）