# Prometheus 监控与 Grafana 告警：构建云原生监控系统

## 学习目标
1. 理解 Prometheus 监控系统的基本概念、架构及其在云原生环境中的重要性。
2. 掌握 Prometheus 的核心组件功能（Prometheus Server、Exporters、Alertmanager）以及 PromQL 查询语言的基础使用。
3. 能够对比 Prometheus 与其他监控系统（如 Zabbix、Nagios）的优劣，明确适用场景。
4. 学会在本地或 Kubernetes 环境中部署 Prometheus 监控系统，并配置常见 Exporter（如 Node Exporter、MySQL Exporter、Redis Exporter）进行数据采集。
5. 理解 Grafana Alerting 的功能与配置方式，掌握通过可视化界面设置告警规则和通知渠道的方法。
6. 掌握 Prometheus 和 Grafana 在生产环境中的应用策略，学会配置监控仪表盘、设置告警规则，并通过模拟场景应对企业级监控与告警需求。

##  第一部分：Prometheus 理论

### **1. 什么是 Prometheus？**
- **定义**：Prometheus 是一个开源的监控工具和时间序列数据库（TSDB），专门用来收集、存储和分析系统的运行数据，特别适合动态变化的环境，比如云服务或容器化应用。
- **起源与背景**：
  - 由 SoundCloud 公司开发，2016 年加入 CNCF（云原生计算基金会），是 Kubernetes 生态中监控领域的“明星工具”。
  - **比喻**：想象 Prometheus 是一个“24小时值班的系统保安”，它时刻盯着你的服务器、应用和数据库，一旦发现异常（比如服务器快要“累垮”），就会记录下来并准备发出警告。
- **核心特点**（用通俗语言解释）：
  - **指标监控**：它关注系统的“健康数据”，比如 CPU 使用率、内存占用、请求数量，就像医生检查你的心跳和血压。
  - **动态适应**：能自动发现新加入的服务器或服务，尤其适合 Kubernetes 这种经常变化的环境，不需要你手动一个个添加。
  - **强大查询**：自带一种查询语言叫 PromQL，就像一个“数据侦探”，能帮你从海量数据中找出问题根源。
- **适用场景**（结合生活化例子）：
  - 监控服务器是否“过载”，比如 CPU 使用率过高，就像监控家里电器的用电量，防止跳闸。
  - 检查网站或应用的“健康”，比如页面加载慢不慢，就像检查餐厅服务员是否及时响应顾客。
  - 关注数据库“压力”，比如连接数是否过多，就像监控水管是否快要爆裂。

### **2. Prometheus 架构与核心组件**
- **架构概述**：
  - Prometheus 是一个“主动型”监控工具，它会自己去“问”各个系统：“你还好吗？给我看看你的状态数据！”然后把这些数据存下来，供你查询或用来设置警告。
  - **通俗流程**：它先去“收集”数据，然后“保存”起来，最后让你“查看”或“报警”。
- **核心组件**（逐个解释，配合比喻）：
  - **Prometheus Server**：
    - 这是“大脑”，负责主动收集数据、保存数据（像一个时间日记本），还能让你查询历史状态。
    - 它通过一个配置文件（比如 `prometheus.yml`）知道去哪里找数据，就像保安有份巡逻清单，知道要检查哪些区域。
  - **Exporters**：
    - 这些是“小探子”，专门负责把某个系统的状态翻译成 Prometheus 能懂的数据格式，放在一个公开的地方（通常是网页地址 `/metrics`）等待被收集。
    - 举例：Node Exporter 就像一个“服务器体检仪”，告诉你 CPU、内存、硬盘的使用情况；MySQL Exporter 就像“数据库心电图”，告诉你数据库的查询速度和连接数。
  - **Pushgateway**（可选，简要提及）：
    - 有些系统没办法被“问”，只能主动“汇报”，Pushgateway 就像一个“中转站”，接收这些汇报再转给 Prometheus。
    - 就像一个临时工只能通过中介报告工作情况，我们课程暂时不深入讨论。
  - **Alertmanager**（简要提及）：
    - 专门处理警告信息，决定怎么通知你（比如发邮件或微信）。
    - 就像保安发现问题后决定是打 110 还是直接通知物业，我们课程会用更简单的方式（Grafana Alerting）来做告警。
- **数据流转**（用生活场景描述）：
  - 想象一个小区保安系统：各个房子装了传感器（Exporters）报告状态，保安队长（Prometheus Server）定时巡逻收集信息，存到日志本里。如果发现某户门窗异常，就通过广播（告警）通知大家。
- **Mermaid 架构图**（帮助可视化）：
````mermaid
  graph TD
    A[Prometheus Server] -->|拉取数据| B[Node Exporter]
    A -->|拉取数据| C[MySQL Exporter]
    A -->|拉取数据| D[Redis Exporter]
    E[Pushgateway] -->|推送数据| A
    A -->|触发告警| F[Alertmanager]
    F -->|发送通知| G[邮件/Slack]
    A -->|查询数据| H[用户界面/Grafana]
  style A fill:#f9f,stroke:#333,stroke-width:2px
  style F fill:#ff9,stroke:#333,stroke-width:2px
````
**图表说明**：上图展示了 Prometheus 的核心组件和数据流动方向。Prometheus Server 是中心，主动从各个 Exporter 拉取数据，必要时通过 Alertmanager 发送告警，用户可以通过界面查看数据。

### **3. 工作原理**
- **Pull 模型**（拉取模式）：
  - Prometheus 像一个“巡逻员”，每隔一段时间（比如 30 秒）主动去访问 Exporter 的“窗口”（HTTP 地址 `/metrics`），询问：“你的最新状态是什么？”然后把答案记下来。
  - **对比 Push 模型**：不像有些工具等着系统主动汇报，Pull 模型让 Prometheus 掌握主动权，特别适合管理一大堆动态变化的服务（比如 Kubernetes 容器），因为它不需要每个服务都记住“汇报地址”。
- **时间序列数据**（用表格比喻）：
  - 收集来的数据像一本“时间日记”，每一行是一个时间点的记录，每一列是不同的“健康指标”。
  - 每个指标有名字和“标签”（labels），标签就像备注，帮你细分数据。比如 `http_requests_total{method="GET", status="200"}` 这条记录的意思是：“GET 请求中，返回状态码 200 的总数”。
  - **生活例子**：就像你每天记录体温，备注是“早上”还是“晚上”，方便你分析趋势。
- **PromQL 查询语言**（简单介绍）：
  - PromQL 是一个“数据搜索工具”，让你能问：“过去 5 分钟我的网站请求速度是多少？”或者“哪些服务器的 CPU 使用率超过 80%？”
  - **简单例子**：`rate(http_requests_total[5m])` 就像问：“最近 5 分钟，每秒有多少请求进来？”
  - **教学说明**：我们不会写复杂代码，通过 Grafana 的图形界面也能完成类似查询，不用担心记不住语法。

### **4. 优势与适用场景对比**
- **优势**（用小白能懂的方式）：
  - **自动发现**：新加一台服务器或服务，它能自己找到，不用你手动设置，就像手机自动连上新 Wi-Fi。
  - **高效查询**：能快速分析海量数据，找出问题，就像在超市里用扫码枪快速找到商品信息。
  - **团队友好**：开源免费，社区支持多，遇到问题网上教程一大堆。
- **与其他监控系统的对比**（通俗化）：
  - **Prometheus vs Zabbix**：
    - Zabbix 像一个“老式保安”，适合固定不变的服务器，手动配置多；Prometheus 像“智能摄像头”，自动适应新设备，数据分析更灵活。
  - **Prometheus vs Nagios**：
    - Nagios 像“基础警铃”，只能告诉你“有问题”，不擅长分析原因；Prometheus 像“智能诊断仪”，能告诉你问题细节。
  - **结论**：Prometheus 是现代监控的“好帮手”，尤其适合变化多端、设备众多的环境。


# 第二部分：Prometheus 本地安装


### **1. 前置准备**
- **目标环境**：我们将在 Linux 系统（以 Ubuntu 或 CentOS 为例）上安装 Prometheus，确保您有一台可以 SSH 登录的服务器或本地虚拟机。
- **工具需求**：需要有基本的 Linux 命令行操作知识（如 `cd`、`tar`、`sudo`），以及文本编辑器（如 `vim` 或 `nano`）。
- **比喻**：安装 Prometheus 就像在家里装一个“智能监控摄像头”，我们需要先下载设备（软件包），然后按照说明书（步骤）一步步安装，最后通电（启动服务）让它工作。
- **下载地址**：
  - 官方网站：https://prometheus.io/download/
  - 具体版本下载链接：https://github.com/prometheus/prometheus/releases/download/v3.5.0/prometheus-3.5.0.linux-amd64.tar.gz
  - 官方文档：https://prometheus.io/docs/prometheus/latest/getting_started/
  - **说明**：我们选择的是 v3.5.0 版本，适合 Linux 系统的 64 位架构（amd64）。如果您的系统架构不同（如 ARM），需要下载对应版本。

### **2. 安装步骤（详细解释）**
以下是安装 Prometheus 的具体步骤，每一步都会用通俗语言和比喻解释其作用。

- **步骤 1：下载并解压安装包**
  ```bash
  wget https://github.com/prometheus/prometheus/releases/download/v3.5.0/prometheus-3.5.0.linux-amd64.tar.gz
  tar -zxvf prometheus-3.5.0.linux-amd64.tar.gz
  ```
  - **解释**：`wget` 命令就像去商店拿回一个包裹，下载 Prometheus 的安装文件。`tar -zxvf` 就像打开包裹，把里面的零件（文件）取出来。
  - **输出结果**：解压后会生成一个文件夹 `prometheus-3.5.0.linux-amd64`，里面包含 Prometheus 的可执行文件和配置文件。
  - **比喻**：这就像把“监控摄像头”的零件从包装盒里拿出来，准备组装。

- **步骤 2：进入解压后的目录**
  ```bash
  cd prometheus-3.5.0.linux-amd64/
  ```
  - **解释**：`cd` 命令就像走进一个房间，进入解压后的文件夹，以便后续操作里面的文件。
  - **比喻**：这就像走进工作间，准备开始组装“摄像头”。

- **步骤 3：移动文件到系统目录**
  ```bash
  sudo mv prometheus /usr/local/bin
  sudo mv promtool /usr/local/bin
  sudo mv consoles /etc/prometheus
  mkdir -p /etc/prometheus
  sudo mv console_libraries /etc/prometheus
  sudo mv prometheus.yml /etc/prometheus
  ```
  - **解释**：
    - `sudo mv` 命令就像把东西搬到合适的位置，`sudo` 表示以管理员权限操作（因为普通用户不能随便改系统文件）。
    - `prometheus` 和 `promtool` 是主要程序文件，放到 `/usr/local/bin` 目录下，就像把“摄像头主机”和“调试工具”放到容易启动的地方。
    - `consoles` 和 `console_libraries` 是 Prometheus 自带的网页界面模板和库文件，放到 `/etc/prometheus` 目录下，就像把“显示屏”和“说明书”放到固定的抽屉里。
    - `prometheus.yml` 是配置文件，就像“摄像头的设置手册”，告诉它去监控哪些地方。
    - `mkdir -p /etc/prometheus` 是创建一个文件夹，确保 `/etc/prometheus` 存在，就像确保抽屉已经准备好。
  - **比喻**：这就像把“摄像头”的零件放到家里合适的位置，比如主机放客厅，说明书放书柜。

- **步骤 4：创建并编辑系统服务配置文件**
  ```bash
  vim /etc/systemd/system/prometheus.service
  ```
  - **解释**：这一步是用 `vim` 编辑器创建一个服务文件，告诉系统如何运行 Prometheus。`systemd` 是 Linux 系统管理服务的工具，就像一个“家政管家”，帮你自动启动和管理程序。
  - **比喻**：这就像写一份“定时任务清单”，告诉家政机器人每天几点开摄像头、怎么运行。
  - **文件内容**（逐行解释）：
    ```bash
    [Unit]
    Description=Prometheus
    Wants=network-online.target
    After=network-online.target

    [Service]
    User=root
    Group=root
    Type=simple
    ExecStart=/usr/local/bin/prometheus \
        --config.file=/etc/prometheus/prometheus.yml \
        --storage.tsdb.path=/var/prometheus/data \
        --web.listen-address=0.0.0.0:9090 \
        --storage.tsdb.retention.time=7d \
        --storage.tsdb.retention.size=30GB
    Restart=always
    RestartSec=5
    
    [Install]
    WantedBy=multi-user.target
    ```
    - **解释**：`[Unit]` 部分描述服务的属性。`Description` 是服务名称，`Wants` 和 `After` 确保 Prometheus 在网络连接好之后再启动，就像说“只有家里网络通了，摄像头才能联网工作”。

    - **解释**：
      - `[Service]` 部分定义服务如何运行。
      - `User=root` 和 `Group=root` 表示以 root 用户和组运行，就像让“最高管理员”来操作摄像头。
      - `Type=simple` 表示服务类型是最简单的启动方式。
      - `ExecStart` 是启动命令，后面是 Prometheus 的运行参数，就像告诉摄像头“用这个设置手册，存数据到这个硬盘，监听这个端口”。
        - `--config.file=/etc/prometheus/prometheus.yml`：指定配置文件路径，就像“按照这份设置手册工作”。
        - `--storage.tsdb.path=/var/prometheus/data`：指定数据存储路径，就像“把监控录像存到这个硬盘”。
        - `--web.listen-address=0.0.0.0:9090`：指定网页界面监听地址和端口，`0.0.0.0` 表示任何设备都能访问，`9090` 是端口，就像“在家里任何设备都能通过 9090 这个门看监控画面”。
        - `--storage.tsdb.retention.time=7d`：数据保留 7 天，就像“只保存最近 7 天的录像，旧的自动删掉”。
        - `--storage.tsdb.retention.size=30GB`：数据存储上限 30GB，就像“硬盘最多用 30GB 存录像，满了就覆盖老数据”。
      - `Restart=always` 和 `RestartSec=5` 表示如果服务崩溃，5 秒后自动重启，就像“如果摄像头断线，5 秒后自动重连”。

    - **解释**：`[Install]` 部分定义服务安装后如何启动，`multi-user.target` 表示开机时自动运行，就像“每次开机，摄像头都自动启动”。
  - **操作提示**：在 `vim` 中，输入 `i` 进入编辑模式，粘贴以上内容，编辑完成后按 `Esc`，输入 `:wq` 保存并退出。如果不熟悉 `vim`，可以用 `nano` 编辑器，操作更简单。

- **步骤 5：启用并启动 Prometheus 服务**
  ```bash
  sudo systemctl enable prometheus
  sudo systemctl start prometheus
  ```
  - **解释**：
    - `sudo systemctl enable prometheus` 表示设置 Prometheus 开机自启，就像告诉家政机器人“以后每次开机都自动打开摄像头”。
    - `sudo systemctl start prometheus` 表示立即启动 Prometheus 服务，就像现在按下“开机按钮”让摄像头开始工作。
  - **验证启动**：
    - 使用命令 `sudo systemctl status prometheus` 检查服务状态，如果显示 `active (running)`，说明启动成功，就像检查摄像头指示灯是否亮了。
    - 打开浏览器，访问 `http://你的服务器IP:9090`，如果看到 Prometheus 的网页界面，说明安装成功，就像通过手机 App 看到监控画面。
  - **比喻**：这就像装好摄像头后，插上电源，按下开关，然后用手机检查是否能看到画面。

### **3. 配置文件 `prometheus.yml` 解释**
- **位置**：`/etc/prometheus/prometheus.yml`
- **作用**：这是 Prometheus 的核心配置文件，告诉它去哪里收集数据、怎么收集、收集的频率等，就像“监控摄像头的巡逻计划书”。
- **默认内容**（简要解释，假设是默认配置文件）：
  ```
  global:
    scrape_interval: 30s
    evaluation_interval: 30s

  scrape_configs:
    - job_name: 'prometheus'
      static_configs:
        - targets: ['localhost:9090']
  ```
  - **逐部分解释**：
    - `global`：全局设置，适用于所有任务。
      - `scrape_interval: 30s`：每 30 秒收集一次数据，就像“每 30 秒巡逻一次，看看系统状态”。
      - `evaluation_interval: 30s`：每 30 秒评估一次告警规则，就像“每 30 秒检查一次有没有异常情况要报警”。
    - `scrape_configs`：定义具体的数据收集任务。
      - `job_name: 'prometheus'`：任务名称，就像给巡逻任务取个名字叫“监控自己”。
      - `static_configs`：静态配置目标，不需要自动发现。
        - `targets: ['localhost:9090']`：监控目标是本机的 9090 端口，也就是 Prometheus 自己，就像“摄像头先监控自己的状态”。
  - **教学说明**：目前是默认配置，监控的是 Prometheus 自身。在后续课程中，我们会修改这个文件，添加更多目标（如 Node Exporter），就像“告诉摄像头不仅看自己，还要看服务器其他房间”。
  - **比喻**：配置文件就像一份“巡逻清单”，告诉摄像头每隔多久检查一次，检查哪些地方。

### **4. 常见问题与排查**
- **问题 1：启动失败**
  - 检查命令：`sudo systemctl status prometheus`
  - 可能原因：配置文件路径错误或数据目录没有权限。
  - 解决方法：确保 `/var/prometheus/data` 目录存在并有写入权限，可以用 `sudo mkdir -p /var/prometheus/data` 和 `sudo chmod 777 /var/prometheus/data` 创建并授权。
  - 比喻：就像摄像头启动不了，可能是电源线没插好，检查一下“插座”（目录权限）是否正常。
- **问题 2：网页界面打不开**
  - 检查命令：`netstat -lnpt | grep 9090` 查看端口是否监听。
  - 可能原因：防火墙阻挡或 IP 地址错误。
  - 解决方法：确保防火墙允许 9090 端口（`sudo ufw allow 9090`），或检查是否用正确的服务器 IP 访问。
  - 比喻：就像手机连不上摄像头，可能是“Wi-Fi 信号被墙挡住”（防火墙），需要调整设置。


好的，我将根据您的要求和提供的配置文件，详细解答您的问题，并对 `prometheus.yml` 配置文件进行完整解析。内容将以通俗易懂的方式呈现，适合小白学员，并通过比喻和步骤拆解帮助理解。

---

# 第三部分：使用 Helm 在 Kubernetes 中安装 Node Exporter（包含详细配置和外部 Prometheus 权限）

### **目标**
- 掌握使用 Helm 在 Kubernetes 集群中部署 `kube-state-metrics` 和 Node Exporter 的方法，命名空间为 `prometheus`。
- 理解为什么 ClusterRole 不能对所有类型资源直接赋予 `get`、`list`、`watch` 权限。
- 学习如何为 ServiceAccount 创建 Secret 并将其放到 `kube-system` 命名空间。
- 详细解析提供的 `prometheus.yml` 配置文件，解释每个部分的作用。

### **内容结构**

#### **1. 使用 Helm 安装 kube-state-metrics 和 Node Exporter（命名空间为 prometheus）**
- **步骤 1：添加 Helm 仓库**
  ```bash
  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  helm repo update
  ```
  - **解释**：添加 Helm 仓库就像在“应用商店”里添加一个新的软件来源，更新列表确保拿到最新版本。
  - **验证**：运行 `helm search repo prometheus` 查看是否能找到相关 Chart。

- **步骤 2：安装 kube-state-metrics**
  ```bash
  helm install kube-state-metrics prometheus-community/kube-state-metrics \
    --namespace prometheus --create-namespace
  ```
  - **解释**：安装 `kube-state-metrics` 到 `prometheus` 命名空间，就像把“房间管理员”放到指定的监控房间。
  - **验证**：运行 `kubectl get pods -n prometheus` 查看 Pod 状态，确保 `kube-state-metrics` Pod 状态为 `Running`。

- **步骤 3：安装 prometheus-node-exporter**
  ```bash
  helm install node-exporter prometheus-community/prometheus-node-exporter \
    --namespace prometheus
  ```
  - **解释**：安装 Node Exporter 到 `prometheus` 命名空间，就像把“传感器”装到监控房间。
  - **验证**：运行 `kubectl get pods -n prometheus` 查看 Pod 状态，确保 `node-exporter` Pod 状态为 `Running`。

- **替代方案：直接安装 kube-prometheus-stack** （以后可能你去公司用得到）
  ```bash
  helm install prometheus-stack prometheus-community/kube-prometheus-stack \
    --namespace prometheus --create-namespace
  ```
  - **解释**：这就像买一个“监控全家桶”，包含所有组件，一次性装好。
  - **验证**：运行 `kubectl get pods -n prometheus` 确保所有 Pod 正常运行。

#### **2. 为什么 ClusterRole 不能对所有类型资源直接赋予 "get", "list", "watch" 权限**
- **原因**：
  - **安全原则 - 最小权限原则**：Kubernetes 的 RBAC（基于角色的访问控制）遵循最小权限原则，即只授予必要的权限。如果对所有资源类型（`*`）都赋予 `get`、`list`、`watch` 权限，可能会导致权限过大，增加安全风险。例如，Prometheus 可能访问到敏感资源（如 Secret 或 ConfigMap 中的密码），或对某些资源执行不必要的操作，增加被攻击的风险。
    - **比喻**：这就像给一个保安“万能钥匙”，让他能打开家里所有房间的门，甚至包括保险柜（敏感资源）。如果钥匙被偷，家里所有东西都可能被盗。所以最好只给他能巡查房间状态的钥匙，而不是所有门的钥匙。
  - **资源分组（apiGroups）差异**：Kubernetes 资源分为不同的 `apiGroups`（如核心资源 `""`、应用资源 `apps`、批处理资源 `batch` 等）。不同组的资源可能有不同的访问需求，Prometheus 只需要访问与监控相关的资源（如 Node、Pod、Service），而不需要访问所有组的所有资源。
    - **比喻**：这就像家里有不同区域（客厅、卧室、厨房），保安只需要查看客厅和卧室的状态（监控相关资源），不需要进入厨房（无关资源）。
  - **性能考虑**：对所有资源执行 `watch` 操作会增加 API Server 的负载，尤其是大规模集群中，资源数量庞大，Prometheus 频繁查询会影响集群性能。
    - **比喻**：这就像保安每分钟检查家里所有东西（包括不重要的抽屉、柜子），浪费时间和精力，只需检查关键区域（监控相关资源）就够了。
- **解决方法**：在实际配置中，通常会明确指定 Prometheus 需要的资源类型和 `apiGroups`，例如：
  - 核心资源：`nodes`、`pods`、`services`、`endpoints` 等。
  - 应用资源：`deployments`、`statefulsets` 等。
  - 自定义资源：如 `kube-state-metrics` 暴露的服务。
  - 示例 ClusterRole（精简版）：
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: prometheus
    rules:
    - apiGroups: [""]
      resources: ["nodes", "pods", "services", "endpoints"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["apps"]
      resources: ["deployments", "statefulsets"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["batch"]
      resources: ["jobs", "cronjobs"]
      verbs: ["get", "list", "watch"]
    ```
  - **比喻**：这就像只给保安客厅和卧室的钥匙，让他能查看这些区域的状态，而不是家里所有地方都能进。

#### **3. 创建 ServiceAccount 的 Secret 并放到 kube-system 命名空间**
- **步骤：创建 ServiceAccount 和 Secret**
  - 默认情况下，创建 ServiceAccount 后，Kubernetes 会自动生成一个关联的 Secret（包含 Token），但我们可以手动指定将其放到 `kube-system` 命名空间（通常用于系统组件）。
  - 创建 YAML 文件 `prometheus-sa.yaml`：
    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: prometheus
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: prometheus
    rules:
    - apiGroups: [""]
      resources: ["nodes", "pods", "services", "endpoints"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["apps"]
      resources: ["deployments", "statefulsets"]
      verbs: ["get", "list", "watch"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: prometheus
    subjects:
    - kind: ServiceAccount
      name: prometheus
      namespace: kube-system
    roleRef:
      kind: ClusterRole
      name: prometheus
      apiGroup: rbac.authorization.k8s.io
    ```
  - 应用配置：
    ```bash
    kubectl apply -f prometheus-sa.yaml
    ```
  - **获取自动生成的 Secret**：
    ```bash
    kubectl get secret -n kube-system | grep prometheus
    ```
    输出类似 `prometheus-token-xxxx`，这是自动生成的 Secret。
  - **手动创建 Secret 并放到 kube-system**（如果需要自定义）：
    - 手动提取 Token 或创建自定义 Secret（不推荐，因为 Kubernetes 1.24+ 已移除自动挂载 Token，需手动管理）。
    - 创建 Secret YAML 文件 `prometheus-secret.yaml`：
      ```yaml
      apiVersion: v1
      kind: Secret
      metadata:
        name: prometheus-token
        namespace: kube-system
        annotations:
          kubernetes.io/service-account.name: prometheus
      type: kubernetes.io/service-account-token
      ```
    - 应用配置：
      ```bash
      kubectl apply -f prometheus-secret.yaml
      ```
    - **解释**：将 Secret 放到 `kube-system` 命名空间，可能是因为外部 Prometheus 的部署环境或策略要求系统级 Secret 存储在 `kube-system`。但通常建议直接使用 ServiceAccount 关联的 Secret，无需手动移动。
    - **比喻**：这就像把保安的钥匙（Token）从监控房间（`prometheus` 命名空间）拿到前台（`kube-system` 命名空间），方便外部监控中心直接在前台取用。
  - **验证**：运行 `kubectl get secret -n kube-system | grep prometheus` 确保 Secret 已创建。

#### **4. 完整解析 prometheus.yml 配置文件**
以下是对您提供的 `prometheus.yml` 配置文件的详细解析，用通俗语言和比喻解释每个部分的作用。

- **文件概述**：
  - `prometheus.yml` 是 Prometheus 的主配置文件，定义了如何抓取监控数据、设置告警、加载规则等。
  - **比喻**：这就像监控中心的“任务清单”，告诉监控中心“去哪里收集数据”、“多久查一次”、“发现问题怎么报警”。

- **global 部分**：
  ```yaml
  global:
    scrape_interval: 30s
    evaluation_interval: 30s
    external_labels:
      cluster: 'kubernetes-cluster'
      replica: 'prometheus-166'
  ```
  - **解释**：
    - `scrape_interval: 30s`：设置全局抓取间隔为 30 秒，即 Prometheus 每 30 秒从目标收集一次数据。
      - **比喻**：这就像监控中心每 30 秒巡查一次家里情况。
    - `evaluation_interval: 30s`：设置规则评估间隔为 30 秒，即 Prometheus 每 30 秒检查一次告警规则是否触发。
      - **比喻**：这就像监控中心每 30 秒分析一次数据，看看有没有异常需要报警。
    - `external_labels`：为所有收集的数据添加额外标签，这里指定集群名称为 `kubernetes-cluster`，实例名称为 `prometheus-166`，便于多集群或多实例区分。
      - **比喻**：这就像在每个传感器数据上贴个标签，写明“来自哪个家（集群）”、“哪个监控中心（实例）”，避免混淆。

- **alerting 部分**：
  ```yaml
  alerting:
    alertmanagers:
      - static_configs:
          - targets:
            - localhost:9093
  ```
  - **解释**：
    - `alertmanagers`：指定告警管理器的地址，这里是 `localhost:9093`，即 Prometheus 会将告警发送到本地运行的 Alertmanager（端口 9093）。
    - **比喻**：这就像监控中心发现问题后，通知本地的“报警器”（Alertmanager），由它决定怎么处理报警（发邮件、发短信等）。

- **rule_files 部分**：
  ```yaml
  rule_files:
    - "rules/*.yml"
  ```
  - **解释**：
    - `rule_files`：指定告警规则文件路径，这里加载 `rules` 目录下的所有 `.yml` 文件。这些文件定义了告警条件，如 CPU 使用率超过 90% 则报警。
    - **比喻**：这就像监控中心的“报警手册”，里面写着“如果温度超过 30 度，就拉响警报”，规则文件就是这样的手册。

- **scrape_configs 部分**：
  - 这是配置文件的核心部分，定义了 Prometheus 从哪里抓取数据。每个 `job_name` 代表一个监控任务，下面详细解析每个任务。
  - **比喻**：这就像监控中心的“巡查计划表”，列出要检查的所有地方（目标）和检查方式。

  - **1. Prometheus 自身监控 (job_name: 'prometheus')**
    ```yaml
    - job_name: 'prometheus'
      static_configs:
        - targets: ['192.168.110.166:9090']
          labels:
            app: "prometheus"
      scrape_interval: 30s
      metrics_path: /metrics
    ```
    - **解释**：
      - `job_name: 'prometheus'`：任务名称，表示监控 Prometheus 自身。
      - `static_configs`：静态配置目标，这里指定 Prometheus 运行在 `192.168.110.166:9090`。
      - `labels`：为目标添加标签 `app: "prometheus"`，便于区分。
      - `scrape_interval: 30s`：抓取间隔 30 秒。
      - `metrics_path: /metrics`：指定抓取数据的路径为 `/metrics`。
      - **比喻**：这就像监控中心先检查自己的状态（是否正常运行），就像人先看看自己有没有生病。

  - **2. Kubernetes API Server 监控 (job_name: 'kubernetes-apiservers')**
    ```yaml
    # 1. Kubernetes API Server 监控
    - job_name: 'kubernetes-apiservers'
      kubernetes_sd_configs:
      - role: endpoints
      api_server: https://192.168.110.167:6443
      tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
      action: keep
      regex: default;kubernetes;https
      - action: labelmap
      regex: __meta_kubernetes_service_label_(.+)
    ```
    - **解释**：
      - `job_name: 'kubernetes-apiservers'`：任务名称，表示监控 Kubernetes API Server。
      - `kubernetes_sd_configs`：使用 Kubernetes 服务发现机制，`role: endpoints` 表示发现服务端点。
      - `api_server: https://192.168.110.167:6443`：指定 Kubernetes API Server 地址。
      - `tls_config` 和 `bearer_token_file`：配置 TLS 证书和认证 Token，`ca_file: /etc/prometheus/k8s-ca.crt` 是 CA 证书路径，用于验证 API Server 身份；`bearer_token_file: /etc/prometheus/k8s-token` 是认证 Token 文件路径，用于证明 Prometheus 的访问权限；`insecure_skip_verify: true` 表示跳过证书验证（不安全，仅用于测试）。
        - **比喻**：这就像用“身份证”（Token）和“通行证”（证书）进入 Kubernetes 总部（API Server），但暂时不检查通行证真假（跳过验证）。
      - `relabel_configs`：重新标记配置，筛选和修改标签：
        - 筛选 `default` 命名空间的 `kubernetes` 服务，端口名为 `https`。
        - 将服务标签映射为 Prometheus 标签。
        - 替换目标标签为 `kubernetes_namespace` 和 `kubernetes_name`。
        - **比喻**：这就像从一大堆房间中挑出“总部办公室”（default 下的 kubernetes 服务），并在数据上贴上房间名和用途的标签，方便查看。

  - **3. Node Exporter 监控 (job_name: 'kubernetes-nodes')**
    ```yaml
    - job_name: 'kubernetes-nodes'
      kubernetes_sd_configs:
      - role: node
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: http
      relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
      - target_label: __address__
        replacement: ${1}:9100
        source_labels: [__meta_kubernetes_node_address_InternalIP]
      - target_label: __metrics_path__
        replacement: /metrics
      - source_labels: [__meta_kubernetes_node_name]
        action: replace
        target_label: node
      metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'node_(cpu_seconds_total|memory_MemTotal_bytes|memory_MemFree_bytes|memory_MemAvailable_bytes|memory_Buffers_bytes|memory_Cached_bytes|filesystem_size_bytes|filesystem_free_bytes|filesystem_avail_bytes|network_receive_bytes_total|network_transmit_bytes_total|load1|load5|load15|disk_read_bytes_total|disk_written_bytes_total)'
        action: keep
    ```
    - **解释**：
      - `job_name: 'kubernetes-nodes'`：任务名称，监控 Kubernetes 节点（通过 Node Exporter）。
      - `role: node`：服务发现角色为节点，发现集群中所有节点。
      - `scheme: http`：使用 HTTP 协议访问 Node Exporter。
      - `relabel_configs`：
        - 将节点标签映射为 Prometheus 标签。
        - 将节点内部 IP 加上端口 `9100`（Node Exporter 默认端口）作为目标地址。
        - 设置指标路径为 `/metrics`。
        - 将节点名称设置为 `node` 标签。
      - `metric_relabel_configs`：只保留关键指标，如 CPU、内存、磁盘、网络等，丢弃不必要的指标，减少数据量。
      - **比喻**：这就像监控中心找到家里每个房间的“传感器”（Node Exporter），用房间的 IP 地址和端口联系上，只记录重要的温度、湿度数据（关键指标），忽略无关信息。

  - **4. Kubelet 监控 (job_name: 'kubernetes-kubelet')**
    ```yaml
    - job_name: 'kubernetes-kubelet'
      kubernetes_sd_configs:
      - role: node
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
      - target_label: __metrics_path__
        replacement: /metrics
      - source_labels: [__meta_kubernetes_node_name]
        action: replace
        target_label: node
    ```
    - **解释**：
      - `job_name: 'kubernetes-kubelet'`：任务名称，监控 Kubernetes 节点的 Kubelet（负责节点上 Pod 管理的组件）。
      - `role: node`：发现所有节点。
      - `scheme: https`：使用 HTTPS 访问 Kubelet。
      - `relabel_configs`：设置指标路径为 `/metrics`，将节点名称设置为 `node` 标签。
      - **比喻**：这就像监控中心联系每个房间的“管家”（Kubelet），询问房间里每个人的状态（Pod 状态）。

  - **5. cAdvisor 监控 (job_name: 'kubernetes-cadvisor')**
    ```yaml
    - job_name: 'kubernetes-cadvisor'
      kubernetes_sd_configs:
      - role: node
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      metrics_path: /metrics/cadvisor
      relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
      - source_labels: [__meta_kubernetes_node_name]
        action: replace
        target_label: node
      metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'container_(cpu_usage_seconds_total|memory_usage_bytes|memory_working_set_bytes|fs_usage_bytes|fs_limit_bytes|network_receive_bytes_total|network_transmit_bytes_total|spec_cpu_quota|spec_memory_limit_bytes)'
        action: keep
      - source_labels: [container]
        regex: 'POD'
        action: drop
      - source_labels: [container]
        regex: '^$'
        action: drop
    ```
    - **解释**：
      - `job_name: 'kubernetes-cadvisor'`：任务名称，监控 cAdvisor（容器监控工具，集成在 Kubelet 中）。
      - `metrics_path: /metrics/cadvisor`：指定 cAdvisor 指标路径。
      - `metric_relabel_configs`：只保留关键容器指标（如 CPU、内存、网络），丢弃暂停容器（`POD`）和空容器名的指标。
      - **比喻**：这就像监控中心询问每个房间的“智能摄像头”（cAdvisor），了解每个人的活动量（容器资源使用），但忽略无关的人（暂停容器）。

  - **6. kube-state-metrics 监控 (job_name: 'kube-state-metrics')**
    ```yaml
    - job_name: 'kube-state-metrics'
      kubernetes_sd_configs:
      - role: service
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      # 只抓取 kube-state-metrics 服务
      - source_labels: [__meta_kubernetes_service_name]
        action: keep
        regex: kube-state-metrics
      # 构建代理路径
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name]
        action: replace
        target_label: __metrics_path__
        regex: (.+);(.+)
        replacement: /api/v1/namespaces/${1}/services/${2}:8080/proxy/metrics
      # 设置 API Server 地址
      - action: replace
        target_label: __address__
        replacement: 192.168.110.167:6443
      # 添加标签
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_service_name]
        action: replace
        target_label: kubernetes_service_name
    ```
    - **解释**：
      - `job_name: 'kube-state-metrics'`：任务名称，监控 `kube-state-metrics` 服务。
      - `role: service`：发现服务。
      - `relabel_configs`：只保留名为 `kube-state-metrics` 的服务，端口名为 `http-metrics`，并设置命名空间和服务名称标签。
      - **比喻**：这就像监控中心联系“房间管理员”（kube-state-metrics），获取每个房间的使用情况（资源状态）。

  - **7. Pod 监控 (job_name: 'kubernetes-pods')**
    ```yaml
    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      # 只抓取有注解的 Pod
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      # 获取自定义端口
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __tmp_port
        regex: (.+)
      # 如果没有自定义端口，跳过
      - source_labels: [__tmp_port]
        action: keep
        regex: .+
      # 构建地址
      - source_labels: [__address__, __tmp_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      # 获取自定义路径
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      # 设置默认路径
      - target_label: __metrics_path__
        replacement: /metrics
        regex: ^$
      # 添加标签
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name
      - source_labels: [__meta_kubernetes_pod_node_name]
        action: replace
        target_label: kubernetes_node
      # 清理临时标签
      - regex: __tmp_.*
        action: labeldrop
    ```
    - **解释**：
      - `job_name: 'kubernetes-pods'`：任务名称，监控 Kubernetes Pod。
      - `role: pod`：发现所有 Pod。
      - `relabel_configs`：只抓取带有注解 `prometheus.io/scrape: true` 的 Pod，获取自定义端口和路径，构建目标地址，添加标签，清理临时标签。
      - **比喻**：这就像监控中心只关注有“监控标志”的房间（有注解的 Pod），记录他们的位置和状态，忽略其他房间。

  - **8. Service 监控 (job_name: 'kubernetes-services')**
    ```yaml
    - job_name: 'kubernetes-services'
      kubernetes_sd_configs:
      - role: service
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      # 只抓取有 prometheus.io/scrape: "true" 注解的 Service
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      
      # 排除不需要的服务（包括 kube-state-metrics 避免重复）
      - source_labels: [__meta_kubernetes_service_name]
        action: drop
        regex: (.*node-exporter.*|kubernetes|kube-dns|kube-state-metrics)
      
      # 获取自定义 scheme，默认 http
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        action: replace
        target_label: __scheme__
        regex: (https?)
        replacement: ${1}
      
      # 获取自定义 metrics 路径，默认 /metrics
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
        replacement: ${1}
      
      # 设置默认 metrics 路径（如果没有自定义路径）
      - source_labels: [__metrics_path__]
        action: replace
        target_label: __metrics_path__
        regex: ^$
        replacement: /metrics
      
      # 获取自定义端口
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __tmp_port
        regex: (.+)
        replacement: ${1}
      
      # 如果没有自定义端口，使用服务的第一个端口
      - source_labels: [__tmp_port, __meta_kubernetes_service_port_number]
        action: replace
        target_label: __tmp_port
        regex: ^;(.+)
        replacement: ${1}
      
      # 构建代理地址 - 通过 API Server 访问
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __tmp_port, __metrics_path__]
        action: replace
        target_label: __metrics_path__
        regex: (.+);(.+);(.+);(.+)
        replacement: /api/v1/namespaces/${1}/services/${2}:${3}/proxy${4}
      
      # 设置 API Server 地址
      - action: replace
        target_label: __address__
        replacement: 192.168.110.167:6443
      
      # 强制使用 https（通过 API Server）
      - action: replace
        target_label: __scheme__
        replacement: https
      
      # 添加 Service 标签映射
      - action: labelmap
        regex: __meta_kubernetes_service_label_(.+)
        replacement: service_${1}
      
      # 添加标准标签
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      
      - source_labels: [__meta_kubernetes_service_name]
        action: replace
        target_label: kubernetes_service_name
      
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name]
        action: replace
        target_label: kubernetes_name
        regex: (.+);(.+)
        replacement: ${1}/${2}
      
      # 清理临时标签
      - regex: __tmp_.*
        action: labeldrop
    ```
    - **解释**：
      - `job_name: 'kubernetes-services'`：任务名称，监控 Kubernetes Service。
      - `role: endpoints`：发现服务端点。
      - `relabel_configs`：只抓取带有注解 `prometheus.io/scrape: true` 的服务，排除系统服务，构建目标地址和路径，添加标签。
      - **比喻**：这就像监控中心只关注有“监控标志”的公共区域（Service），忽略系统区域（如监控工具本身）。

  - **9. Ingress 监控 (job_name: 'kubernetes-ingress-nginx')**
    ```yaml
    - job_name: 'kubernetes-ingress-nginx'
      kubernetes_sd_configs:
      - role: pod
        api_server: https://192.168.110.167:6443
        tls_config:
          ca_file: /etc/prometheus/k8s-ca.crt
          insecure_skip_verify: true
        bearer_token_file: /etc/prometheus/k8s-token
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
        action: keep
        regex: ingress-nginx
      - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_component]
        action: keep
        regex: controller
      # 通过 API Server 代理访问
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_pod_name]
        action: replace
        target_label: __metrics_path__
        regex: (.+);(.+)
        replacement: /api/v1/namespaces/${1}/pods/${2}:10254/proxy/metrics
      - action: replace
        target_label: __address__
        replacement: 192.168.110.167:6443
      - action: replace
        target_label: __scheme__
        replacement: https
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name
      scheme: https
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    ```
    - **解释**：
      - `job_name: 'kubernetes-ingress-nginx'`：任务名称，监控 Ingress（使用 NGINX Ingress Controller）。
      - `role: pod`：发现 Pod。
      - `relabel_configs`：只保留标签为 `ingress-nginx` 且组件为 `controller` 的 Pod，设置目标地址为 Pod IP 加端口 `10254`（NGINX 指标端口）。
      - **比喻**：这就像监控中心关注家门口的“门卫”（Ingress Controller），了解进出流量情况。

#### **1. 获取并保存 CA 证书到 /etc/prometheus/k8s-ca.crt**
- **背景**：
  - CA 证书用于验证 Kubernetes API Server 的身份，确保 Prometheus 与 API Server 通信的安全性。我们可以从 `kubeconfig` 文件中提取 CA 证书数据，并保存到指定路径。
  - **比喻**：CA 证书就像一个“官方印章”，监控中心（Prometheus）用它确认联系的总部（API Server）是不是真的。我们需要从文件柜（kubeconfig）中拿出印章的副本，放到监控中心的抽屉里（`/etc/prometheus/k8s-ca.crt`）。
- **步骤：获取并保存 CA 证书**
  - **步骤 1：提取 CA 证书数据**
    ```bash
    kubectl config view --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}' | base64 -d
    ```
    - **解释**：
      - `kubectl config view --raw`：查看当前的 `kubeconfig` 配置，`--raw` 确保输出原始数据。
      - `-o jsonpath='{.clusters[0].cluster.certificate-authority-data}'`：从配置中提取第一个集群的 `certificate-authority-data` 字段（Base64 编码的 CA 证书）。
      - `base64 -d`：将 Base64 编码的数据解码为明文证书内容。
    - **输出示例**：
      ```
      -----BEGIN CERTIFICATE-----
      MIICyDCCAbCgAwIBAgIBADANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwprdWJl
      ...
      -----END CERTIFICATE-----
      ```
    - **比喻**：这就像从文件柜中找到印章的加密副本，解开密码（Base64 解码），看到印章的真实内容。
  - **步骤 2：保存 CA 证书到文件**
    ```bash
    vim /etc/prometheus/k8s-ca.crt
    ```
    - **解释**：将解码后的证书内容保存到 `/etc/prometheus/k8s-ca.crt` 文件中，供 Prometheus 使用。
    - **注意**：
      - 确保 `/etc/prometheus/` 目录存在，如果没有，需要先创建：`mkdir -p /etc/prometheus`。
      - 确保当前用户有权限写入该路径，如果没有，可以用 `sudo` 执行命令或调整权限：`sudo chmod 755 /etc/prometheus`。
    - **比喻**：这就像把印章副本放进监控中心的抽屉（指定文件路径），方便随时使用。
  - **步骤 3：验证保存的文件**
    ```bash
    cat /etc/prometheus/k8s-ca.crt
    ```
    - **解释**：查看文件内容，确保证书已正确保存。输出应以 `-----BEGIN CERTIFICATE-----` 开头，以 `-----END CERTIFICATE-----` 结尾。

#### **2. 获取并保存 Token 到 /etc/prometheus/k8s-token**
- **背景**：
  - ServiceAccount 的 Token 用于身份认证，外部 Prometheus 需要使用它访问 Kubernetes API Server。这个 Token 存储在与 ServiceAccount 关联的 Secret 中，我们可以提取并保存到指定路径。
  - **比喻**：Token 就像保安的“通行证”，监控中心（Prometheus）需要用它证明身份。我们需要从家里保险箱（Secret）中拿出通行证，放到监控中心的抽屉里（`/etc/prometheus/k8s-token`）。
- **步骤：获取并保存 Token**
  - **步骤 1：查看 ServiceAccount 关联的 Secret**
    ```bash
    kubectl get secret -n kube-system | grep prometheus-token
    ```
    - **解释**：假设 Secret 名称包含 `prometheus-token`，位于 `kube-system` 命名空间。运行此命令会列出匹配的 Secret，例如 `prometheus-token`。
    - **输出示例**：
      ```
      prometheus-token   kubernetes.io/service-account-token   3      1h
      ```
  - **步骤 2：提取 Token 值并保存到文件**
    ```bash
    # 在你windwos或者macos本地执行的命令
    kubectl get secret prometheus-token -n kube-system -o jsonpath='{.data.token}' | base64 -d
    # 登录你自己的prometheus主机,把内容保存起来
    vim /etc/prometheus/k8s-token
    ```
    - **解释**：
      - `kubectl get secret ... -o jsonpath='{.data.token}'`：从指定 Secret 中提取 `token` 字段的值（Base64 编码）。
      - `base64 -d`：将 Base64 编码的 Token 解码为明文。
      - `vim /etc/prometheus/k8s-token`：将解码后的 Token 保存到文件 `/etc/prometheus/k8s-token` 中，供 Prometheus 使用。
    - **注意**：
      - 确保 `/etc/prometheus/` 目录存在，如果没有，需要先创建：`mkdir -p /etc/prometheus`。
      - 确保当前用户有权限写入该路径，如果没有，可以用 `sudo` 执行命令或调整权限：`sudo chmod 755 /etc/prometheus`。
  - **步骤 3：验证保存的 Token 文件**
    ```bash
    cat /etc/prometheus/k8s-token
    ```
    - **解释**：查看文件内容，确保 Token 已正确保存。输出应该是一长串字符（类似 JWT 格式），例如 `eyJhbGciOiJSUzI1NiIsImtpZCI6...`。


#### **完成配置内容**
```bash
# prometheus.yml
global:
  scrape_interval: 30s
  evaluation_interval: 30s
  external_labels:
    cluster: 'kubernetes-cluster'
    replica: 'prometheus-166'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - localhost:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  - "rules/*.yml"

# A scrape configuration containing exactly one endpoint to scrape:
scrape_configs:
  # Prometheus 自身监控
  - job_name: 'prometheus'
    static_configs:
      - targets: ['192.168.110.166:9090']
        labels:
          app: "prometheus"
    scrape_interval: 30s
    metrics_path: /metrics

  # 1. Kubernetes API Server 监控
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
    - role: endpoints
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
      action: keep
      regex: default;kubernetes;https
    - action: labelmap
      regex: __meta_kubernetes_service_label_(.+)

  # 2. Node Exporter (节点系统指标)
  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
    - role: node
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: http
    relabel_configs:
    - action: labelmap
      regex: __meta_kubernetes_node_label_(.+)
    - target_label: __address__
      replacement: ${1}:9100
      source_labels: [__meta_kubernetes_node_address_InternalIP]
    - target_label: __metrics_path__
      replacement: /metrics
    - source_labels: [__meta_kubernetes_node_name]
      action: replace
      target_label: node
    metric_relabel_configs:
    - source_labels: [__name__]
      regex: 'node_(cpu_seconds_total|memory_MemTotal_bytes|memory_MemFree_bytes|memory_MemAvailable_bytes|memory_Buffers_bytes|memory_Cached_bytes|filesystem_size_bytes|filesystem_free_bytes|filesystem_avail_bytes|network_receive_bytes_total|network_transmit_bytes_total|load1|load5|load15|disk_read_bytes_total|disk_written_bytes_total)'
      action: keep

  # 3. Kubelet 监控 (节点和Pod的基础指标)
  - job_name: 'kubernetes-kubelet'
    kubernetes_sd_configs:
    - role: node
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    - action: labelmap
      regex: __meta_kubernetes_node_label_(.+)
    - target_label: __metrics_path__
      replacement: /metrics
    - source_labels: [__meta_kubernetes_node_name]
      action: replace
      target_label: node

  # 4. cAdvisor 监控 (容器资源使用情况)
  - job_name: 'kubernetes-cadvisor'
    kubernetes_sd_configs:
    - role: node
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    metrics_path: /metrics/cadvisor
    relabel_configs:
    - action: labelmap
      regex: __meta_kubernetes_node_label_(.+)
    - source_labels: [__meta_kubernetes_node_name]
      action: replace
      target_label: node
    metric_relabel_configs:
    - source_labels: [__name__]
      regex: 'container_(cpu_usage_seconds_total|memory_usage_bytes|memory_working_set_bytes|fs_usage_bytes|fs_limit_bytes|network_receive_bytes_total|network_transmit_bytes_total|spec_cpu_quota|spec_memory_limit_bytes)'
      action: keep
    - source_labels: [container]
      regex: 'POD'
      action: drop
    - source_labels: [container]
      regex: '^$'
      action: drop

  # 5. Pod 监控
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
    - role: pod
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    # 只抓取有注解的 Pod
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    # 获取自定义端口
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      target_label: __tmp_port
      regex: (.+)
    # 如果没有自定义端口，跳过
    - source_labels: [__tmp_port]
      action: keep
      regex: .+
    # 构建地址
    - source_labels: [__address__, __tmp_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: $1:$2
      target_label: __address__
    # 获取自定义路径
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
    # 设置默认路径
    - target_label: __metrics_path__
      replacement: /metrics
      regex: ^$
    # 添加标签
    - action: labelmap
      regex: __meta_kubernetes_pod_label_(.+)
    - source_labels: [__meta_kubernetes_namespace]
      action: replace
      target_label: kubernetes_namespace
    - source_labels: [__meta_kubernetes_pod_name]
      action: replace
      target_label: kubernetes_pod_name
    - source_labels: [__meta_kubernetes_pod_node_name]
      action: replace
      target_label: kubernetes_node
    # 清理临时标签
    - regex: __tmp_.*
      action: labeldrop

  # 6. Service 监控 (服务级别指标)
  - job_name: 'kubernetes-services'
    kubernetes_sd_configs:
    - role: service
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    # 只抓取有 prometheus.io/scrape: "true" 注解的 Service
    - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    
    # 排除不需要的服务（包括 kube-state-metrics 避免重复）
    - source_labels: [__meta_kubernetes_service_name]
      action: drop
      regex: (.*node-exporter.*|kubernetes|kube-dns|kube-state-metrics)
    
    # 获取自定义 scheme，默认 http
    - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
      action: replace
      target_label: __scheme__
      regex: (https?)
      replacement: ${1}
    
    # 获取自定义 metrics 路径，默认 /metrics
    - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
      replacement: ${1}
    
    # 设置默认 metrics 路径（如果没有自定义路径）
    - source_labels: [__metrics_path__]
      action: replace
      target_label: __metrics_path__
      regex: ^$
      replacement: /metrics
    
    # 获取自定义端口
    - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_port]
      action: replace
      target_label: __tmp_port
      regex: (.+)
      replacement: ${1}
    
    # 如果没有自定义端口，使用服务的第一个端口
    - source_labels: [__tmp_port, __meta_kubernetes_service_port_number]
      action: replace
      target_label: __tmp_port
      regex: ^;(.+)
      replacement: ${1}
    
    # 构建代理地址 - 通过 API Server 访问
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __tmp_port, __metrics_path__]
      action: replace
      target_label: __metrics_path__
      regex: (.+);(.+);(.+);(.+)
      replacement: /api/v1/namespaces/${1}/services/${2}:${3}/proxy${4}
    
    # 设置 API Server 地址
    - action: replace
      target_label: __address__
      replacement: 192.168.110.167:6443
    
    # 强制使用 https（通过 API Server）
    - action: replace
      target_label: __scheme__
      replacement: https
    
    # 添加 Service 标签映射
    - action: labelmap
      regex: __meta_kubernetes_service_label_(.+)
      replacement: service_${1}
    
    # 添加标准标签
    - source_labels: [__meta_kubernetes_namespace]
      action: replace
      target_label: kubernetes_namespace
    
    - source_labels: [__meta_kubernetes_service_name]
      action: replace
      target_label: kubernetes_service_name
    
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name]
      action: replace
      target_label: kubernetes_name
      regex: (.+);(.+)
      replacement: ${1}/${2}
    
    # 清理临时标签
    - regex: __tmp_.*
      action: labeldrop

  # 7. 专门为 kube-state-metrics 添加一个独立的 job
  - job_name: 'kube-state-metrics'
    kubernetes_sd_configs:
    - role: service
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    # 只抓取 kube-state-metrics 服务
    - source_labels: [__meta_kubernetes_service_name]
      action: keep
      regex: kube-state-metrics
    
    # 构建代理路径
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name]
      action: replace
      target_label: __metrics_path__
      regex: (.+);(.+)
      replacement: /api/v1/namespaces/${1}/services/${2}:8080/proxy/metrics
    
    # 设置 API Server 地址
    - action: replace
      target_label: __address__
      replacement: 192.168.110.167:6443
    
    # 添加标签
    - source_labels: [__meta_kubernetes_namespace]
      action: replace
      target_label: kubernetes_namespace
    
    - source_labels: [__meta_kubernetes_service_name]
      action: replace
      target_label: kubernetes_service_name


  # 8. Ingress 监控 (nginx-ingress controller)
  - job_name: 'kubernetes-ingress-nginx'
    kubernetes_sd_configs:
    - role: pod
      api_server: https://192.168.110.167:6443
      tls_config:
        ca_file: /etc/prometheus/k8s-ca.crt
        insecure_skip_verify: true
      bearer_token_file: /etc/prometheus/k8s-token
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
      action: keep
      regex: ingress-nginx
    - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_component]
      action: keep
      regex: controller
    # 通过 API Server 代理访问
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_pod_name]
      action: replace
      target_label: __metrics_path__
      regex: (.+);(.+)
      replacement: /api/v1/namespaces/${1}/pods/${2}:10254/proxy/metrics
    - action: replace
      target_label: __address__
      replacement: 192.168.110.167:6443
    - action: replace
      target_label: __scheme__
      replacement: https
    - source_labels: [__meta_kubernetes_namespace]
      action: replace
      target_label: kubernetes_namespace
    - source_labels: [__meta_kubernetes_pod_name]
      action: replace
      target_label: kubernetes_pod_name
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/k8s-ca.crt
      insecure_skip_verify: true
    bearer_token_file: /etc/prometheus/k8s-token

```

### **总结**
通过以上内容，我们完成了以下任务：
1. 使用 Helm 在 `prometheus` 命名空间安装了 `kube-state-metrics` 和 Node Exporter。
2. 解释了为什么 ClusterRole 不能对所有资源类型直接赋予 `get`、`list`、`watch` 权限，强调了最小权限原则和性能考虑。
3. 提供了创建 ServiceAccount 和 Secret 的步骤，并说明如何将其放到 `kube-system` 命名空间。
4. 详细解析了 `prometheus.yml` 配置文件，解释了每个监控任务的作用和配置细节，特别是 `ca_file` 和 `bearer_token_file` 的认证机制。









## 第二部分：Grafana Alerting 理论

### **1. 什么是 Grafana Alerting？**
- **定义**：Grafana Alerting 是 Grafana 平台自带的一个告警功能，可以根据监控数据（比如从 Prometheus 拿来的指标）设置规则，一旦数据异常就发出警告。
- **背景**：
  - Grafana 是一个“数据看板工具”，就像一个大屏幕显示器，能把各种数据画成图表，方便你一眼看出系统状态。
  - Alerting 是它的“报警升级版”，不仅能“看”，还能“提醒”，让你不需要一直盯着屏幕。
  - **比喻**：Grafana Alerting 就像家里的“智能烟雾报警器”，不仅能检测到烟雾（数据异常），还能自动拨打消防电话（发送通知）。
- **核心特点**（通俗解释）：
  - **图形化操作**：不需要写代码，鼠标点一点就能设置“如果 CPU 超过 80%，就报警”。
  - **多来源支持**：能监控不同工具的数据，比如 Prometheus 的指标、Loki 的日志，就像一个报警器能同时检查烟雾和燃气。
  - **和看板结合**：告警直接显示在你的监控图表上，哪里出问题一目了然。

### **2. Grafana Alerting 核心功能**
- **告警规则配置**（用步骤描述）：
  - 你在 Grafana 界面上选一个数据（比如 CPU 使用率），设定一个条件（比如“超过 80% 持续 5 分钟”），然后决定怎么报警（比如发邮件）。
  - **例子**：就像设置手机闹钟，“如果时间到 7:00，就响铃”，只不过这里是“如果数据异常，就报警”。
- **通知渠道**：
  - 可以选择报警方式：发邮件、发 Slack 消息、甚至推送手机通知，就像报警器能打不同人的电话。
  - 还能自定义消息内容，比如“服务器 A 的 CPU 超载了，请检查！”让通知更清晰。
- **告警状态管理**：
  - Grafana 界面会显示告警是“正常”还是“已触发”，就像报警器面板上的绿灯和红灯。
  - 还能看到历史记录，方便你事后分析“上次报警是什么时候，为什么”。
- **与仪表盘结合**：
  - 告警规则可以绑到你的监控图表上，数据一超标，图表就变色或闪烁，帮你快速找到问题点。
  - **比喻**：就像车速表，超速时不仅数字变红，还会发出“滴滴”声。

### **3. 与 Prometheus 的关系**
- **数据集成**：
  - Grafana 像一个“显示屏”，连接到 Prometheus 这个“数据仓库”，直接读取里面的指标数据（比如 CPU、内存）。
  - 告警规则基于这些数据设置，就像根据体温计读数决定是否要吃药。
- **分工与优势**：
  - Prometheus 负责“采集和存数据”，就像一个勤劳的记录员；Grafana 负责“展示和报警”，就像一个会说话的播报员。
  - **对比 Prometheus Alertmanager**：
    - Alertmanager 是 Prometheus 自带的“专业报警员”，功能强大但设置复杂，适合大公司用。
    - Grafana Alerting 是“简易报警员”，界面友好，点几下鼠标就搞定，适合我们学习和小团队。
  - **课程重点**：我们用 Grafana Alerting，因为它简单直观，学起来更快。
- **Mermaid 流程图**（帮助可视化）：
````mermaid
  graph LR
    A[Prometheus Server] -->|提供数据| B[Grafana]
    C[Exporters] -->|暴露指标| A
    B -->|配置告警规则| D[Grafana Alerting]
    D -->|发送通知| E[邮件/Slack/手机]
    B -->|显示数据| F[仪表盘]
  style A fill:#f9f,stroke:#333,stroke-width:2px
  style B fill:#ff9,stroke:#333,stroke-width:2px
  style D fill:#9ff,stroke:#333,stroke-width:2px
````
**图表说明**：上图展示了 Prometheus 如何采集数据并传递给 Grafana，Grafana 再通过 Alerting 功能设置告警并发送通知，同时在仪表盘上直观显示数据。

### **4. 优势与适用场景**
- **优势**（通俗化）：
  - **简单易用**：不需要懂编程，界面像玩游戏一样点几下就设置好了。
  - **直观显示**：告警和图表在一起，哪里有问题点哪里，就像导航地图上直接标出堵车点。
  - **灵活扩展**：能接不同数据工具，未来加新监控对象也很方便。
- **适用场景**（生活化）：
  - 小团队快速搭建监控报警，就像家里装个简单摄像头，不需要专业安保系统。
  - 学习阶段练手，界面友好不吓人，就像用简单计算器而不是专业软件。
  - 需要“看”和“报警”一起解决的场景，就像车上仪表盘既显示速度又提醒超速。


