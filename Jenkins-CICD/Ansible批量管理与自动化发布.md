# Ansible 批量管理与自动化发布

## 技能掌握目标
- 掌握 Ansible 的基本概念和常用模块，能够使用 Ad-hoc 命令完成基础操作。
- 学会通过 Ansible 批量管理多台 Ubuntu 主机，完成企业级安全检查和配置任务。
- 理解并实现 Ansible 跳板机（a-b-c）远程操作，解决企业复杂网络环境下的管理问题。
- 熟练编写 Ansible Playbook，重点掌握带参数和条件判断的用法，实现灵活的任务管理。
- 通过 Playbook 实现 Docker 环境下 Java 项目和前端项目的自动化部署，提升运维效率。

## 环境说明
- 所有主机均为 Ubuntu 系统。
- 必须配置 SSH 免密登录，自行配置。
- 学习环境需准备至少 3 台主机（虚拟机或云服务器），用于模拟控制节点、跳板机和目标主机。
- 部署实践需准备 Docker 环境及简单的 Docker 化 Java 项目（Spring Boot 或 JAR 文件）和前端项目（Vue/React 静态文件）。

## 第一部分：Ansible 基础与常用模块

### 1.1 什么是 Ansible？
- Ansible 是一种开源的自动化运维工具，用于配置管理、应用部署、任务自动化和编排。
- 核心特点：
  - **无代理（Agentless）**：不需要在被管主机上安装额外软件，仅依赖 SSH 和 Python。
  - **声明式配置**：通过 YAML 格式描述目标状态，Ansible 自动完成配置。
  - **模块化设计**：内置丰富模块，支持文件管理、包安装、服务控制等操作。
  - **跨平台支持**：适用于 Linux、Windows 等多种操作系统（本课程以 Ubuntu 为例）。
- 应用场景：
  - 批量服务器配置（如统一安装软件、修改配置文件）。
  - 自动化部署（如发布应用、更新代码）。
  - 基础设施即代码（IaC），管理云资源。

### 1.2 为什么选择 Ansible？
- **易用性**：相比其他工具（如 Puppet、Chef），Ansible 学习曲线平缓，配置文件简单易读。
- **轻量级**：无代理架构减少了维护成本，适合中小型团队。
- **灵活性**：支持 Ad-hoc 命令（临时任务）和 Playbook（复杂任务编排）。
- **社区支持**：拥有活跃的社区和丰富的文档资源，易于扩展。

- **Ansible 的应用场景**
  - 服务器配置管理：批量设置用户、文件权限、软件安装。
  - 应用部署：自动化部署 Web 应用、数据库、容器化项目。
  - 任务调度：定时执行系统检查、日志收集。
  - 企业场景：通过跳板机管理内网主机、Docker 环境下的 CI/CD 集成。

### 1.3 Ansible 的架构与工作原理
- **Ansible 的架构与工作原理**
  - **核心组件**：
    - **控制节点（Control Node）**：运行 Ansible 的主机，负责任务调度、执行和日志记录，通常是管理员的本地机器或服务器。
    - **被管节点（Managed Nodes）**：通过 SSH 接收和执行任务的目标主机，无需安装 Ansible 客户端。
    - **Inventory**：定义被管主机及其分组信息，可以是静态文件或动态脚本生成。
    - **Modules**：Ansible 的功能单元，用于执行具体任务（如 `file` 模块创建文件，`apt` 模块安装软件）。
    - **Playbooks**：定义自动化任务的配置文件，包含多个任务和逻辑，支持条件判断和循环。
  - **工作流程**：
    1. 管理员在控制节点编写 Inventory 和任务（Ad-hoc 命令或 Playbook）。
    2. Ansible 通过 SSH 连接到被管节点。
    3. 将任务分解为模块，传输到被管节点执行。
    4. 被管节点返回执行结果，控制节点记录日志。
- **Mermaid 架构图**：
    ```mermaid
    graph TD
        A[控制节点 Control Node] -->|SSH 连接| B[被管节点 Managed Node 1]
        A -->|SSH 连接| C[被管节点 Managed Node 2]
        A -->|SSH 连接| D[被管节点 Managed Node 3]
        A --> E[Inventory 文件]
        A --> F[Modules 模块]
        A --> G[Playbooks 任务文件]
        E -->|定义主机| B
        E -->|定义主机| C
        E -->|定义主机| D
        F -->|执行任务| B
        F -->|执行任务| C
        F -->|执行任务| D
        G -->|定义任务逻辑| F
    ```
  - 图解说明：控制节点通过 SSH 管理多个被管节点，依赖 Inventory 定义目标主机，使用 Modules 执行具体任务，并通过 Playbooks 实现复杂任务编排。

### 1.4 Ansible 与其他工具的对比
- **Ansible vs Puppet/Chef**：
  - Ansible：无代理，基于 SSH，配置简单，适合快速上手。
  - Puppet/Chef：有代理，需要安装客户端，配置复杂，适合大型复杂环境。
- **Ansible vs SaltStack**：
  - Ansible：无代理，速度稍慢，易于维护。
  - SaltStack：有代理，速度快，但部署复杂。
- 适用场景：Ansible 更适合中小型团队或对简单性和维护成本敏感的环境。


### 2. 环境搭建
#### 2.1 安装 Ansible（基于 Ubuntu 系统）
- **步骤**：
  1. 更新系统包列表：`sudo apt update`。
  2. 安装 Ansible：`sudo apt install ansible -y`。
  3. 验证安装：`ansible --version`，确认版本信息输出（如 `ansible 2.9.6`）。
- **注意**：确保控制节点和被管节点都安装了 Python（通常 Ubuntu 已预装），Ansible 依赖 Python 运行。

#### 2.2 Ansible 配置文件
- **配置文件位置**：默认配置文件为 `/etc/ansible/ansible.cfg`，可通过环境变量 `ANSIBLE_CONFIG` 指定自定义配置文件。
- **常用配置参数**：
  - `inventory`：指定 Inventory 文件路径，默认 `/etc/ansible/hosts`。
  - `remote_user`：指定 SSH 连接时使用的默认用户名，如 `remote_user = ubuntu`。
  - `private_key_file`：指定 SSH 私钥文件路径，如 `private_key_file = /home/ubuntu/.ssh/id_rsa`。
  - `remote_port`：指定 SSH 连接端口，默认 22，如 `remote_port = 2222`。
  - `host_key_checking`：是否检查主机密钥，默认 `True`，可设为 `False` 跳过首次连接警告（不推荐生产环境）。
- **示例配置**（`/etc/ansible/ansible.cfg` 或自定义文件）：
  ```
  [defaults]
  inventory = /etc/ansible/hosts  # 指定 Inventory 文件路径
  remote_user = ubuntu            # 指定 SSH 连接的默认用户名
  private_key_file = /home/ubuntu/.ssh/id_rsa  # 指定 SSH 私钥路径
  remote_port = 5423                # 指定 SSH 连接的默认端口
  host_key_checking = False       # 禁用主机密钥检查（初学时方便，生产环境慎用）
  log_path = /var/log/ansible.log  # 指定日志路径
  ```
- **说明**：
  - `remote_user`：连接目标主机时使用的用户名，需与 SSH 免密登录配置一致。
  - `private_key_file`：指定 SSH 私钥，确保控制节点能通过该密钥访问目标主机。
  - `remote_port`：如果目标主机 SSH 端口非默认 22，需明确指定。

#### 2.3 验证 SSH 免密登录
- **前提**：环境已配置 SSH 免密登录，仅需测试连接。
- **测试命令**：`ssh <用户名>@<目标主机IP> -p <端口> -i <私钥文件>`，确保能直接登录无密码提示。
- **注意**：若连接失败，需检查私钥文件权限（应为 `600`）和目标主机 `~/.ssh/authorized_keys` 是否包含对应公钥。

#### 2.4 编写 Inventory 文件
- **编写 Inventory 文件**
  - **定义方式**：Inventory 文件用于列出被管主机，可以是 INI 格式或 YAML 格式。
  - **INI 格式示例**（简单且常用）`vim /etc/ansible/hosts`：
    ```
    [web_servers]
    192.168.1.101 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa
    192.168.1.102 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa

    [app_servers]
    192.168.1.201 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa
    192.168.1.202 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa
    ```
  - **参数解释**：
    - `ansible_user`：指定 SSH 登录用户名。
    - `ansible_port`：指定 SSH 端口，默认 22。
    - `ansible_ssh_private_key_file`：指定 SSH 私钥路径。
  - **测试 Inventory 配置**：`ansible all --list`，查看主机列表是否正确加载。
  - **测试连接**：`ansible all -m ping`，确认所有主机返回 `pong` 响应，表示连接成功。
  - **Mermaid Inventory 分组结构图**：
    ```mermaid
    graph TD
        A[Inventory] --> B[web_servers]
        A --> C[app_servers]
        B --> D[192.168.1.101]
        B --> E[192.168.1.102]
        C --> F[192.168.1.201]
        C --> G[192.168.1.202]
    ```

### 3. Ansible 命令语法与常用模块
- **Ansible 命令基本语法**
  - **Ad-hoc 命令格式**：
    ```
    ansible [主机或组] [-m 模块名] [-a "模块参数"] [-u 用户名] [-b] [--private-key 密钥路径]
    ```
  - **参数解释**：
    - `[主机或组]`：指定目标主机或主机组，如 `all`（所有主机）、`web_servers`（某组）。
    - `-m`：指定模块名，默认是 `command` 模块。
    - `-a`：指定模块参数，通常是字符串格式。
    - `-u`：指定 SSH 用户名。
    - `-b`：以 root 权限执行（等同于 `become: yes`，在 Ubuntu 中通常调用 `sudo`）。
    - `--private-key`：指定 SSH 私钥路径。
    - `-i`：指定 Inventory 文件路径，如 `-i ./inventory`。
  - **示例**：
    - 检查所有主机连通性：`ansible all -m ping`。
    - 以 root 权限执行命令：`ansible web_servers -m shell -a "df -h" -b`。
    - 指定用户和密钥：`ansible app_servers -m ping -u custom_user --private-key=/path/to/key`。
- **常用模块详解**
  1. **`command` 和 `shell` 模块**
     - **用途**：用于在目标主机上执行命令。
     - **区别**：
       - `command`：执行简单命令，不支持管道（`|`）、重定向（`>`）和 shell 内置命令。
       - `shell`：支持完整 shell 环境，可以使用管道和重定向。
     - **语法与参数**：
       - `command`：`ansible <主机> -m command -a "命令"`。
       - `shell`：`ansible <主机> -m shell -a "命令"`。
     - **示例与解释**：
       - 使用 `command` 检查系统版本：`ansible all -m command -a "lsb_release -a"`。
         - 解释：`lsb_release -a` 显示 Ubuntu 系统版本信息，`command` 模块直接执行该命令并返回结果。
       - 使用 `shell` 检查磁盘使用：`ansible all -m shell -a "df -h | grep /dev"`。
         - 解释：`df -h` 显示磁盘使用情况，`| grep /dev` 过滤出设备相关行，`shell` 模块支持管道操作。
     - **注意**：优先使用 `command` 模块以提高安全性，需复杂操作时再用 `shell`。
  2. **`file` 模块**
     - **用途**：管理文件和目录（创建、删除、修改权限）。
     - **常用参数**：
       - `path`：文件或目录路径。
       - `state`：状态，`present`（存在，默认）、`absent`（删除）、`directory`（目录）、`file`（文件）。
       - `mode`：权限，如 `0755`（八进制表示）。
     - **语法**：`ansible <主机> -m file -a "path=路径 state=状态 mode=权限"`。
     - **示例与解释**：
       - 创建目录：`ansible all -m file -a "path=/tmp/test_dir state=directory mode=0755"`。
         - 解释：确保 `/tmp/test_dir` 目录存在，权限为 `0755`（rwxr-x）。
       - 删除文件：`ansible all -m file -a "path=/tmp/test_file state=absent"`。
         - 解释：删除 `/tmp/test_file` 文件，若不存在则无操作（幂等性）。
  3. **`copy` 模块**
     - **用途**：从控制节点复制文件到目标主机。
     - **常用参数**：
       - `src`：源文件路径（控制节点本地）。
       - `dest`：目标路径（目标主机）。
       - `mode`：目标文件权限。
     - **语法**：`ansible <主机> -m copy -a "src=源文件 dest=目标路径 mode=权限"`。
     - **示例与解释**：
       - 复制文件：`ansible all -m copy -a "src=/local/path/test.txt dest=/tmp/test.txt mode=0644"`。
         - 解释：将本地 `/local/path/test.txt` 复制到目标主机的 `/tmp/test.txt`，权限为 `0644`（rw-r--）。
  4. **`apt` 模块**
     - **用途**：管理 Ubuntu/Debian 系统软件包。
     - **常用参数**：
       - `name`：软件包名。
       - `state`：状态，`present`（安装）、`absent`（卸载）、`latest`（更新到最新）。
       - `update_cache`：是否更新包缓存，`yes` 或 `no`。
     - **语法**：`ansible <主机> -m apt -a "name=包名 state=状态 update_cache=是否更新" -b`。
     - **示例与解释**：
       - 更新包缓存：`ansible all -m apt -a "update_cache=yes" -b`。
         - 解释：等同于 `apt update`，更新软件包列表，`-b` 表示以 root 权限执行。
       - 安装软件：`ansible all -m apt -a "name=vim state=present" -b`。
         - 解释：确保 `vim` 已安装，若未安装则自动安装。
  5. **`service` 模块**
     - **用途**：管理服务（启动、停止、重启）。
     - **常用参数**：
       - `name`：服务名。
       - `state`：状态，`started`（启动）、`stopped`（停止）、`restarted`（重启）。
     - **语法**：`ansible <主机> -m service -a "name=服务名 state=状态" -b`。
     - **示例与解释**：
       - 启动服务：`ansible web_servers -m service -a "name=nginx state=started" -b`。
         - 解释：确保 `nginx` 服务处于启动状态，若未启动则启动。
       - 重启服务：`ansible web_servers -m service -a "name=nginx state=restarted" -b`。
         - 解释：重启 `nginx` 服务。
  6. **`user` 模块**
     - **用途**：管理用户（创建、删除、修改）。
     - **常用参数**：
       - `name`：用户名。
       - `state`：状态，`present`（创建）、`absent`（删除）。
     - **语法**：`ansible <主机> -m user -a "name=用户名 state=状态" -b`。
     - **示例与解释**：
       - 创建用户：`ansible all -m user -a "name=testuser state=present" -b`。
         - 解释：创建用户 `testuser`，若已存在则无操作。
       - 删除用户：`ansible all -m user -a "name=testuser state=absent" -b`。
         - 解释：删除用户 `testuser`，若不存在则无操作。

### 4. 实践练习（基于语法和命令解释）
- **任务 1：文件操作**
  - **目标**：熟悉 `file` 和 `copy` 模块的使用，掌握文件和目录管理。
  - **步骤**：
    1. 使用 `file` 模块创建目录：`ansible all -m file -a "path=/tmp/ansible_test state=directory mode=0755"`。
       - 解释：创建 `/tmp/ansible_test` 目录，权限为 `0755`（rwxr-x）。
    2. 使用 `copy` 模块复制文件：`ansible all -m copy -a "src=./test.txt dest=/tmp/ansible_test/test.txt mode=0644"`。
       - 解释：将本地 `./test.txt`（需提前创建）复制到目标主机的 `/tmp/ansible_test/test.txt`。
    3. 验证：登录目标主机，执行 `ls -ld /tmp/ansible_test` 和 `cat /tmp/ansible_test/test.txt`，确认目录和文件存在。
- **任务 2：系统信息收集**
  - **目标**：掌握 `command` 和 `shell` 模块，收集系统信息。
  - **步骤**：
    1. 使用 `command` 模块查看系统版本：`ansible all -m command -a "lsb_release -a"`。
       - 解释：`lsb_release -a` 显示 Ubuntu 系统版本信息。
    2. 使用 `shell` 模块查看磁盘使用：`ansible all -m shell -a "df -h | grep /dev"`。
       - 解释：`df -h` 显示磁盘使用情况，`| grep /dev` 过滤设备相关信息。
    3. 验证：检查命令输出，确认返回了系统版本和磁盘使用信息。
- **任务 3：服务状态检查**
  - **目标**：使用 `service` 模块检查和管理服务状态。
  - **步骤**：
    1. 检查 Nginx 服务状态：`ansible web_servers -m service -a "name=nginx state=started" -b`。
       - 解释：确保 `nginx` 服务启动，若未安装或未启动，可能报错（假设已安装）。
    2. 如果服务未启动，尝试启动：同上命令。
    3. 验证：检查输出中 `changed` 或 `state` 字段，确认服务状态为 `started`。


