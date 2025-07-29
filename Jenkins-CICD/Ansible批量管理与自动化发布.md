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
    ```bash
    [web_servers]
    192.168.1.101 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.102 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.103 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.104 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.105 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root

    [app_servers]
    192.168.1.201 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.202 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    ```
  - **参数解释**：
    - `ansible_user`：指定 SSH 登录用户名。
    - `ansible_port`：指定 SSH 端口，默认 22。
    - `ansible_ssh_private_key_file`：指定 SSH 私钥路径。
    - `ansible_become` : 是否启用权限提升
    - `ansible_become_method` : 权限提升方式（使用 sudo）
    - `ansible_become_user` : 提升为哪个用户（root）
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

- **常用模块汇总表格**

| **模块名**      | **用途**                          | **语法**                                              | **主要参数**                              | **示例**                                                                 | **解释**                                              |
|------------------|-----------------------------------|------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------|
| `command`       | 执行简单命令（不支持管道、重定向） | `ansible <主机> -m command -a "命令"`               | 无特定参数，直接传入命令                 | `ansible all -m command -a "lsb_release -a"`                           | 显示 Ubuntu 系统版本信息。                           |
| `shell`         | 执行复杂命令（支持管道、重定向）   | `ansible <主机> -m shell -a "命令"`                 | 无特定参数，直接传入命令                 | `ansible all -m shell -a "df -h \| grep /dev"`                         | 显示磁盘使用情况，过滤设备相关行。                   |
| `file`          | 管理文件和目录（创建、删除、权限） | `ansible <主机> -m file -a "path=路径 state=状态 mode=权限"` | `path`, `state`, `mode`                  | `ansible all -m file -a "path=/tmp/test_dir state=directory mode=0755"`| 创建目录 `/tmp/test_dir`，权限为 `0755`。            |
| `copy`          | 复制文件到目标主机               | `ansible <主机> -m copy -a "src=源文件 dest=目标路径 mode=权限"` | `src`, `dest`, `mode`                    | `ansible all -m copy -a "src=/local/path/test.txt dest=/tmp/test.txt mode=0644"` | 将本地文件复制到目标主机，权限为 `0644`。            |
| `apt`           | 管理 Ubuntu/Debian 软件包        | `ansible <主机> -m apt -a "name=包名 state=状态 update_cache=是否更新" -b` | `name`, `state`, `update_cache`          | `ansible all -m apt -a "name=vim state=present" -b`                    | 确保 `vim` 已安装，若未安装则自动安装。              |
| `service`       | 管理服务（启动、停止、重启）      | `ansible <主机> -m service -a "name=服务名 state=状态" -b` | `name`, `state`                          | `ansible web_servers -m service -a "name=nginx state=started" -b`      | 确保 `nginx` 服务启动。                              |
| `user`          | 管理用户（创建、删除、修改）      | `ansible <主机> -m user -a "name=用户名 state=状态" -b` | `name`, `state`                          | `ansible all -m user -a "name=testuser state=present" -b`              | 创建用户 `testuser`，若已存在则无操作。              |

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


## 第二部分：批量操作主机
### 1. Inventory 文件高级用法
Inventory 文件是 Ansible 管理主机的基础，支持静态文件和动态生成两种方式。通过高级用法，可以实现主机分组和变量定义，适应企业中复杂的角色划分和配置需求。

- **主机分组**
  - **用途**：根据企业中服务器的角色或功能进行分组，便于针对性管理。
  - **实现方式**：在 Inventory 文件中以 INI 或 YAML 格式定义主机组。
  - **INI 格式示例**（简单且常用）：
    ```bash
    [web_servers]
    192.168.1.101 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.102 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.103 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.104 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.105 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root

    [app_servers]
    192.168.1.201 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.202 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.203 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.204 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root
    192.168.1.205 ansible_user=ubuntu ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes ansible_become_method=sudo ansible_become_user=root

    [all_servers:children]
    web_servers
    app_servers
    ```
  - **解释**：
    - `web_servers` 组包含 5 台运行 Web 服务的服务器。
    - `app_servers` 组包含 5 台运行应用服务的服务器。
    - `all_servers` 是一个父组，包含 `web_servers` 和 `app_servers` 两个子组，方便对所有服务器统一操作。
    - `ansible_ssh_private_key_file`：指定 SSH 私钥路径。
    - `ansible_become` : 是否启用权限提升
    - `ansible_become_method` : 权限提升方式（使用 sudo）
    - `ansible_become_user` : 提升为哪个用户（root）
  - **测试分组**：执行 `ansible web_servers --list` 查看 `web_servers` 组的主机列表，确认分组正确。
  - **Mermaid 分组结构图**：
    ```mermaid
    graph TD
        A[Inventory] --> B[all_servers]
        B --> C[web_servers]
        B --> D[app_servers]
        C --> E[192.168.1.101]
        C --> F[192.168.1.102]
        C --> G[192.168.1.103]
        C --> H[192.168.1.104]
        C --> I[192.168.1.105]
        D --> J[192.168.1.201]
        D --> K[192.168.1.202]
        D --> L[192.168.1.203]
        D --> M[192.168.1.204]
        D --> N[192.168.1.205]
    ```

- **定义变量**
  - **用途**：通过主机变量和组变量，定义特定主机的配置信息或组内通用配置，增加灵活性。
  - **主机变量**：针对单个主机设置特定参数，如 SSH 端口、用户名等。
  - **组变量**：针对整个主机组设置通用参数，如系统版本、服务端口等。
  - **实现方式**：
    - 在 Inventory 文件中直接定义。
    - 或通过单独的变量文件定义（如 `group_vars/web_servers.yml`）。
  - **示例 1：直接在 Inventory 文件中定义变量**：
    ```bash
    [web_servers]
    192.168.1.101 ansible_user=ubuntu ansible_port=22 nginx_port=80
    192.168.1.102 ansible_user=ubuntu ansible_port=2222 nginx_port=8080

    [app_servers]
    192.168.1.201 ansible_user=appuser ansible_port=22 java_version=11
    192.168.1.202 ansible_user=appuser ansible_port=22 java_version=11
    ```
    - 解释：`192.168.1.102` 的 SSH 端口为 `2222`，Nginx 端口为 `8080`；`app_servers` 组主机使用 `appuser` 用户登录，Java 版本为 `11`。
  - **示例 2：通过 `group_vars` 定义组变量**：
    - Ansible项目文件夹
      ```bash
      在 Ansible 项目根目录下（与 inventory 文件同级）创建如下目录结构：
      ./ansible_project/           # 项目根目录
      ├── inventory               # 主机清单文件
      ├── ansible.cfg            # Ansible 配置文件
      ├── hosts                  # 远程主机 配置文件
      └── group_vars/            # 组变量目录
          ├── web_servers.yml    # web_servers 组的变量
          └── app_servers.yml    # app_servers 组的变量
      ```
    - 创建文件 `group_vars/web_servers.yml`：
      ```yaml
      ---
      nginx_version: "1.18.0"
      default_port: 80
      ```
    - 创建文件 `group_vars/app_servers.yml`：
      ```yaml
      ---
      java_version: "11"
      app_port: 8080
      ```
    - 解释：为 `web_servers` 组定义 Nginx 版本和默认端口；为 `app_servers` 组定义 Java 版本和应用端口。
  - **测试变量**：执行 `ansible web_servers -m debug -a "var=nginx_version"`，查看 `web_servers` 组的变量值是否正确加载。
  - **注意**：变量可以在 Ad-hoc 命令或 Playbook 中引用，增强任务的灵活性，后续课程中会深入讲解 Playbook 中的变量用法。

好的，我会根据你的请求优化这份教案，重点放在批量操作、错误处理和企业场景实践上，并删除与变量和 Playbook 相关的高级内容（仅保留必要的基本用法）。以下是优化后的教案，内容更加精炼，逻辑更清晰，适合初学者循序渐进学习 Ansible 的批量操作部分。

---

### 2. 批量操作实践
Ansible 支持对多台主机同时执行任务，通过主机组或模式匹配选择目标主机，极大提升运维效率。

- **对多台主机同时执行命令**
  - **目标**：对所有主机或特定组执行相同任务。
  - **示例**：
    - 检查所有主机系统版本：`ansible all -m command -a "lsb_release -a"`  
      *解释*：对 Inventory 文件中所有主机执行 `lsb_release -a`，返回 Ubuntu 系统版本信息。
    - 检查 `web_servers` 组磁盘使用情况：`ansible web_servers -m shell -a "df -h | grep /dev"`  
      *解释*：对 `web_servers` 组主机执行磁盘使用检查，过滤设备相关信息。
  - **验证**：检查命令输出，确保所有目标主机返回了正确结果。

- **使用模式匹配选择目标主机**
  - **用途**：通过模式匹配灵活选择目标主机，支持通配符和逻辑组合。
  - **常用模式**：
    - `all`：匹配所有主机。
    - `web_servers`：匹配特定组。
    - `192.168.1.*`：使用通配符匹配 IP 地址范围。
    - `web_servers:app_servers`：匹配多个组（并集）。
    - `web_servers:&app_servers`：匹配多个组的交集。
    - `web_servers:!192.168.1.101`：排除特定主机。
  - **示例**：
    - 对 `web_servers` 和 `app_servers` 执行 ping 测试：`ansible "web_servers:app_servers" -m ping`  
      *解释*：对两个组的所有主机执行连通性测试。
    - 对 `web_servers` 组中除 `192.168.1.101` 外的其他主机检查版本：`ansible "web_servers:!192.168.1.101" -m command -a "lsb_release -a"`  
      *解释*：排除特定主机，检查其余主机的系统版本。
  - **验证**：检查输出，确保只对匹配的主机执行了任务。

### 3. 错误处理与日志
在批量操作中，部分主机可能因网络、权限或配置问题导致任务失败，Ansible 提供了错误处理和日志功能帮助排查问题。

- **忽略错误的基本说明**
  - **用途**：当部分主机任务失败时，允许任务继续执行，不影响其他主机。
  - **注意**：Ad-hoc 命令中无法直接忽略错误，建议对重要任务后续学习更高级方法。

- **查看执行日志与调试**
  - **用途**：通过详细日志输出排查任务执行过程中的问题。
  - **方法**：
    - 使用 `-v`、`-vv` 或 `-vvv` 参数增加输出详细程度。
    - 配置 `ansible.cfg` 中的 `log_path` 记录日志到文件。
  - **示例**：
    - 检查所有主机连通性并显示详细输出：`ansible all -m ping -vvv`  
      *解释*：`-vvv` 显示最详细的调试信息，包括 SSH 连接过程和模块执行细节。
    - 检查配置文件中的日志路径：确保 `ansible.cfg` 中设置了 `log_path = /var/log/ansible.log`  
      *解释*：执行任务后，可查看 `/var/log/ansible.log` 文件，分析历史记录。
  - **验证**：执行命令后，检查屏幕输出或日志文件，定位失败主机的具体错误（如 SSH 连接超时、权限不足）。

### 4. 企业操作场景：批量检查和配置 Ubuntu 服务器的安全策略
通过一个真实的企业场景，实践 Ansible 的批量管理能力，确保服务器符合安全和运维规范。

- **场景描述**：
  - 企业有 10 台 Ubuntu 服务器，分为 `web_servers`（5 台，运行 Web 服务）和 `app_servers`（5 台，运行应用服务）。
  - 需要通过 Ansible 批量完成以下任务，确保服务器符合企业安全和运维规范：
    1. 检查所有服务器的 SSH 配置，确保禁用 root 登录（检查 `/etc/ssh/sshd_config` 中的 `PermitRootLogin` 设置）。
    2. 在所有服务器上设置统一的系统时区（如 `Asia/Shanghai`），确保日志时间一致。
    3. 在 `web_servers` 组检查 Nginx 服务状态，确保服务正常运行。
    4. 在 `app_servers` 组检查 Java 进程是否存在，确保应用服务可用。

- **实践步骤**：
  1. **编写 Inventory 文件，定义主机组**：
     - 确保 `web_servers` 和 `app_servers` 组正确定义。
     - 测试分组：`ansible all --list`，确认主机列表正确。
  2. **检查 SSH 配置（禁用 root 登录）**：
     - 命令：`ansible all -m shell -a "grep PermitRootLogin /etc/ssh/sshd_config"`  
       *解释*：检查所有主机的 SSH 配置文件，输出 `PermitRootLogin` 的设置值（应为 `no` 表示禁用）。  
       *验证*：检查输出，确认所有主机返回了 `PermitRootLogin no`，若有异常（如值为 `yes` 或未配置），记录主机 IP 后续处理。
  3. **批量设置系统时区**：
     - 命令：`ansible all -m shell -a "timedatectl set-timezone Asia/Shanghai" -b`  
       *解释*：以 root 权限设置所有主机的时区为 `Asia/Shanghai`。  
       *验证*：执行 `ansible all -m command -a "timedatectl | grep 'Time zone'"`，确认时区已设置为 `Asia/Shanghai`。
  4. **针对 `web_servers` 检查 Nginx 状态**：
     - 命令：`ansible web_servers -m shell -a "systemctl is-active nginx" -b`  
       *解释*：检查 `web_servers` 组中 Nginx 服务是否处于 `active` 状态。  
       *验证*：检查输出，正常情况下返回 `active`，若返回 `inactive` 或 `failed`，记录异常主机 IP 并分析原因。
  5. **针对 `app_servers` 检查 Java 进程**：
     - 命令：`ansible app_servers -m shell -a "ps aux | grep java"`  
       *解释*：检查 `app_servers` 组是否存在 Java 进程。  
       *验证*：检查输出，若返回包含 `java` 的进程信息，说明应用服务运行正常；若无相关输出，记录异常主机 IP 后续排查。

- **验证与调试**：
  - 检查每个任务的输出结果，确认是否符合预期（如 SSH 配置正确、时区一致、服务状态正常）。
  - 对异常主机记录 IP 和具体问题（如 `192.168.1.101` Nginx 未运行），并使用 `ansible <主机 IP> -m ping -vvv` 或查看日志文件进一步调试。
  - 常见问题及解决：
    - SSH 连接失败：检查 Inventory 文件中的 `ansible_user` 和 `ansible_port`，确保 SSH 免密登录配置正确。
    - 权限不足：确保使用 `-b` 参数以 root 权限执行需要 sudo 的命令。
    - 服务未安装：若 Nginx 或 Java 未安装，需后续处理。

- **Mermaid 任务流程图**：
  ```mermaid
  graph TD
      A[开始: 批量管理任务] --> B[检查所有主机 SSH 配置]
      B --> C[设置所有主机时区为 Asia/Shanghai]
      C --> D{主机组划分}
      D -->|web_servers| E[检查 Nginx 服务状态]
      D -->|app_servers| F[检查 Java 进程是否存在]
      E --> G[记录异常主机]
      F --> G
      G --> H[调试与排查问题]
      H --> I[结束: 任务完成]
  ```


## 第三部分：Ansible 跳板机（A-B-C）远程操作

### 2. 跳板机概念与场景
- **什么是跳板机？为什么需要跳板机？**  
  跳板机是一种中间服务器，用于连接无法直接访问的目标主机。在企业环境中，内网服务器往往由于安全策略（如防火墙限制或网络隔离）无法从外部直接访问，必须通过一个位于外网或边界网络的跳板机作为中转站来访问这些内网主机。  
  *小白类比*：跳板机就像一个“中转站”，你想去一个不允许直接进入的房间（内网主机），必须先通过一个前台登记（跳板机），才能进去。

- **典型场景**：  
  企业内网主机无法直接连接，需要通过跳板机访问。比如，你在公司外网的笔记本上，通过跳板机连接到内网的服务器进行运维操作。

- **跳板机连接结构图**  
  以下是跳板机在 A-B-C 场景中的连接关系图，直观展示控制节点、跳板机和内网主机之间的关系：  
  ```mermaid
  graph TD
      A[控制节点 A<br>（你的电脑）] -->|SSH 连接<br>使用私钥登录| B[跳板机 B<br>（外网服务器<br>192.168.110.171）]
      B -->|中转连接| C1[内网主机 C1<br>（192.168.110.172）]
      B -->|中转连接| C2[内网主机 C2<br>（192.168.110.173）]
      B -->|中转连接| C3[内网主机 C3<br>（192.168.110.174）]
      style A fill:#f9f,stroke:#333,stroke-width:2px
      style B fill:#bbf,stroke:#333,stroke-width:2px
      style C1 fill:#bfb,stroke:#333,stroke-width:2px
      style C2 fill:#bfb,stroke:#333,stroke-width:2px
      style C3 fill:#bfb,stroke:#333,stroke-width:2px
  ```
  *解释*：从图中可以看出，控制节点 A 无法直接访问内网主机 C1、C2、C3，必须先连接到跳板机 B，再通过 B 中转到内网主机。这就像你必须先通过“门卫室”（跳板机）才能进入内网的“办公室”（内网主机）。

### 3. 配置跳板机
- **配置 SSH 代理（基于 Ubuntu 环境）**  
  为了通过跳板机访问目标主机，可以在 SSH 配置中使用 `ProxyCommand` 来实现跳板功能。对于小白同学，我们以 `ProxyCommand` 为例，详细讲解如何配置：  
  1. 编辑 SSH 配置文件：`~/.ssh/config`（如果没有此文件，可以手动创建）。  
  2. 添加以下内容（假设跳板机 IP 为 `192.168.110.171`，目标主机 IP 为 `192.168.110.172`，端口为 `5423`）：  
     ```
     Host jump-server
         HostName 192.168.110.171
         User ubuntu
         Port 5423
         IdentityFile /home/ubuntu/.ssh/id_rsa

     Host inner-server
         HostName 192.168.110.172
         User ubuntu
         Port 5423
         ProxyCommand ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa
         IdentityFile /home/ubuntu/.ssh/id_rsa
     ```
  3. 保存后，设置文件权限：`chmod 600 ~/.ssh/config`。  
  *解释*：  
  - `ProxyCommand ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa` 告诉 SSH，通过跳板机 `192.168.110.171` 去连接目标主机 `%h`（即 `192.168.110.172`），`%p` 表示目标主机的端口（即 `5423`）。  
  - `IdentityFile /home/ubuntu/.ssh/id_rsa` 是用于登录跳板机 `192.168.110.171` 的私钥文件，确保你能无密码登录跳板机。  
  - *小白类比*：`ProxyCommand` 就像告诉 SSH，“你先用这把钥匙（id_rsa）打开跳板机的大门（171），然后通过跳板机再去敲目标主机（172）的门。” 这样你就不用手动先登录跳板机，SSH 会自动帮你完成中转。

- **在 Ansible 中使用跳板机**  
  Ansible 支持通过 `ansible_ssh_common_args` 参数配置跳板机，可以直接在 Inventory 文件中指定 `ProxyCommand`，实现通过跳板机连接内网主机。  
  *简单方法*（适合小白）：在 Inventory 文件中为目标主机添加跳板机参数：  
  ```
  [test]
  192.168.110.172 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
  ```
  *解释*：  
  - `ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"'`：这一部分告诉 Ansible，通过跳板机 `192.168.110.171` 去连接目标主机 `192.168.110.172`，并指定跳板机的端口为 `5423`，使用指定的私钥文件登录跳板机。  
  - `ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa`：这是用于登录跳板机 `192.168.110.171` 的私钥文件。注意，这里并不是目标主机（172）的密钥，而是跳板机（171）的密钥，因为 Ansible 需要先登录到跳板机，再通过跳板机去操作目标主机。  
  - *小白类比*：想象你是一个快递员（Ansible），要送包裹给目标主机（172），但必须先通过一个门卫（跳板机 171）。你需要门卫的钥匙（id_rsa）才能进去，然后门卫会带你到目标主机。你不需要目标主机的钥匙，因为跳板机会帮你搞定后面的路。

### 4. 实践案例
- **配置 A-B-C 跳板机环境**  
  假设你有一台控制节点 A（你的电脑），跳板机 B（外网服务器，IP 为 `192.168.110.171`），和内网主机 C（目标服务器，IP 为 `192.168.110.172`）。目标是通过 B 访问 C。  
  1. 配置 Inventory 文件（参考上面方法），指定跳板机 B 的参数和密钥文件。  
  2. 测试连接：`ansible test -m ping`  
     *解释*：使用 `ping` 模块测试是否能通过跳板机连接到内网主机 C。这一步是为了验证网络是否通畅，确认跳板机配置是否正确。  
     *验证*：检查输出结果，确保返回了目标主机的响应信息（如 `pong`），表示跳板机网络配置成功。

- **通过跳板机执行命令**  
  示例：检查系统版本：`ansible test -m shell -a "uname -a"`  
  *解释*：通过跳板机 B，对内网主机 C 执行 `uname -a` 命令，查看系统内核信息。  
  *验证*：检查命令输出，确保返回了目标主机的系统信息。

- **操作流程图**  
  以下是 Ansible 通过跳板机执行命令的流程图，帮助理解整个操作步骤：  
  ```mermaid
  flowchart TD
    A[控制节点 A<br>运行 Ansible 命令] -->|1. 使用私钥连接跳板机| B[跳板机 B<br>192.168.110.171]
    B -->|2. 中转到内网主机| C[内网主机 C<br>192.168.110.172]
    C -->|3. 执行命令<br>如 uname -a| D[返回结果]
    D -->|4. 结果通过跳板机返回| B
    B -->|5. 结果返回控制节点| A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
  ```
  *解释*：从图中可以看出，Ansible 命令从控制节点 A 发出，先通过跳板机 B 中转到内网主机 C，执行命令后，结果再通过跳板机 B 返回到控制节点 A。整个过程就像“快递员通过门卫送包裹，再把回执带回来”。

### 5. 企业操作场景：通过跳板机收集企业内网 Ubuntu 服务器的日志和性能数据
- **场景描述**  
  企业有一个外网跳板机（Ubuntu，IP 为 `192.168.110.171`），需要通过该跳板机访问内网的 5 台 Ubuntu 服务器（定义为 `inner_servers` 组）。目标是为后续运维分析提供数据支持，完成以下任务：  
  1. 检查内网服务器的磁盘使用情况（`df -h`），识别磁盘空间不足的风险。  
  2. 收集内网服务器的系统日志（`/var/log/syslog` 最近 100 行），并传输回控制节点进行分析。  
  3. 检查内网服务器的 CPU 和内存使用情况（`free -m`），记录性能数据。  
  *小白提示*：这是一个典型的运维场景，你就像一个“远程医生”，通过跳板机这个“通道”去检查内网服务器的“健康状况”。

- **实践步骤**  
  1. **配置 Inventory 文件，定义 `inner_servers` 组并指定跳板机参数**  
     示例：
     ```
     [inner_servers]
     192.168.110.172 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
     192.168.110.173 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
     192.168.110.174 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
     192.168.110.175 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
     192.168.110.176 ansible_user=ubuntu ansible_port=5423 ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -p 5423 ubuntu@192.168.110.171 -i /home/ubuntu/.ssh/id_rsa"' ansible_ssh_private_key_file=/home/ubuntu/.ssh/id_rsa
     ```
     *解释*：为每台内网服务器指定跳板机参数，确保 Ansible 通过跳板机 `192.168.110.171` 访问这些主机。`ansible_ssh_private_key_file` 指定的是跳板机的私钥文件，用于登录跳板机。  
     *验证*：执行 `ansible inner_servers -m ping`，确认所有主机都能通过跳板机连接成功。

  2. **通过跳板机检查磁盘使用情况**  
     命令：`ansible inner_servers -m shell -a "df -h"`  
     *解释*：对 `inner_servers` 组的所有主机执行 `df -h` 命令，查看磁盘空间使用情况。  
     *验证*：检查输出结果，确保每台主机返回了磁盘使用数据，特别关注使用率高的分区（如超过 80%），记录可能存在空间不足风险的主机 IP。

  3. **收集系统日志并取回**  
     - 第一步，提取日志：`ansible inner_servers -m shell -a "tail -n 100 /var/log/syslog > /tmp/syslog_tail.log" -b`  
       *解释*：在每台内网主机上执行命令，将 `/var/log/syslog` 的最后 100 行日志保存到临时文件 `/tmp/syslog_tail.log` 中，使用 `-b` 参数以 root 权限执行（读取日志可能需要权限）。  
       *验证*：执行 `ansible inner_servers -m shell -a "ls -l /tmp/syslog_tail.log"`，确认临时文件已生成。  
     - 第二步，取回日志：`ansible inner_servers -m fetch -a "src=/tmp/syslog_tail.log dest=./logs/{{ inventory_hostname }}_syslog.log flat=yes"`  
       *解释*：使用 `fetch` 模块将每台主机的日志文件取回到控制节点的 `./logs/` 目录，并以主机名命名文件。  
       *验证*：在控制节点检查 `./logs/` 目录，确认每个主机的日志文件（如 `192.168.110.172_syslog.log`）已成功取回。

  4. **检查性能数据（CPU 和内存使用情况）**  
     命令：`ansible inner_servers -m shell -a "free -m"`  
     *解释*：对 `inner_servers` 组的所有主机执行 `free -m` 命令，查看内存使用情况（以 MB 为单位）。  
     *验证*：检查输出结果，确保每台主机返回了内存和 CPU 相关数据，记录内存使用率较高的主机（例如，空闲内存过低），为后续优化提供依据。

- **验证与调试**  
  - 确认每个任务的输出结果是否符合预期（如磁盘数据、日志文件、性能数据是否正确收集）。  
  - 如果遇到问题（如连接失败或命令执行错误），可以尝试以下方法：  
    1. 检查跳板机连接：`ansible inner_servers -m ping -vvv`，使用详细输出查看 SSH 连接是否通过跳板机成功建立。  
    2. 确认权限：如果日志读取或命令执行失败，检查是否需要 `-b` 参数以 root 权限运行。  
    3. 检查网络：如果跳板机到内网主机连接超时，确认跳板机的 SSH 配置和网络策略是否允许访问内网。  
    4. 检查密钥文件：确保 `ansible_ssh_private_key_file` 指定的私钥文件正确且有权限访问，并且该密钥能成功登录跳板机。  
  - *小白提示*：调试就像“查水管漏水”，一步步检查从控制节点到跳板机（171），再到内网主机（172 等）的每一段连接，确保数据能顺利“流”过来。
