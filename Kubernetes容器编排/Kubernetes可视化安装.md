## 第一部分：Kubernetes 是什么？为什么需要它？

### **1.1 Kubernetes 简介**
- **Kubernetes（简称 K8s）** 是一个管理容器的工具。它可以帮助我们轻松管理成百上千个容器（比如 Docker 容器），让它们在多台服务器上运行，确保它们不会宕机，还能自动扩展或缩减。
- **通俗理解：** 想象你有一群小机器人（容器）在工厂里干活，Kubernetes 就是工厂的总管，它会安排每个机器人做什么活、监控它们是否正常工作，如果某个机器人坏了，它会立刻派一个新的顶上。
- **为什么需要 Kubernetes？**
  - 容器数量多时，手动管理很麻烦，Kubernetes 帮我们自动化管理。
  - 它能确保服务高可用（不会轻易宕机）。
  - 它支持负载均衡，让流量均匀分配到不同的容器。
- **你们的集群：** 3 个 Master 节点就像工厂的“总管办公室”，负责指挥；2 个 Node 节点就像“车间”，负责实际干活；HAProxy 就像“工厂大门”，负责把外部请求分发到不同的 Master 节点。

### **1.2 基本概念（用生活化的例子解释）**
- **Pod：** Kubernetes 里最小的单位，就像一个“工作小组”，里面有1个或多个容器（小机器人），它们共享同一个网络和存储。
- **Service：** 一个稳定的“服务窗口”，不管后面的 Pod（工作小组）怎么换，外部访问这个窗口总是能找到正确的 Pod。
- **Node：** 一台物理或虚拟服务器，就像工厂里的一个“工作站”，上面可以运行多个 Pod。你们有 2 个 Node 节点。
- **Cluster：** 整个 Kubernetes 集群，就像一个大工厂，包含多个 Node（工作站），由 Master 节点（总管办公室）控制。你们有 3 个 Master 节点。
- **HAProxy：** 负载均衡器，就像工厂的“门卫”，负责把外部请求均匀分发到 3 个 Master 节点。

---

## 第二部分：Kuboard 安装与使用（安装在 HAProxy 上）

### **2.1 在 HAProxy 主机中安装 Kuboard（可视化管理工具）**
- **什么是 Kuboard？** Kuboard 是一个 Kubernetes 的图形界面工具，就像一个“工厂监控大屏”，可以让我们通过网页管理集群，而不用总是敲命令。
- **安装步骤：**
  1. 在 HAProxy 主机上运行以下 Docker 命令来安装 Kuboard：
     ```bash
     # 注意：把下面的 IP 地址改成你 HAProxy 主机的实际 IP 地址
     sudo docker run -d \
         --restart=unless-stopped \
         --name=kuboard \
         -p 80:80/tcp \
         -p 10081:10081/tcp \
         -e KUBOARD_ENDPOINT="http://你的HAProxy_IP:80" \
         -e KUBOARD_AGENT_SERVER_TCP_PORT="10081" \
         -v /root/kuboard-data:/data \
         swr.cn-east-2.myhuaweicloud.com/kuboard/kuboard:v3
     ```
     **解释：** 这条命令会启动一个 Kuboard 容器，监听 80 和 10081 端口，并将数据存储在 `/root/kuboard-data` 目录下。
  2. 安装完成后，在浏览器中访问 `http://你的HAProxy_IP:80`，进入 Kuboard 登录界面。
- **默认账号密码：**
  - 用户名：admin
  - 密码：Kuboard123
- **登录界面示意图：** （保留原文描述）
  ```
  ![kuboard登录界面](/images/kuboard登录界面.png "kuboard登录界面")
  ```

### **2.2 将 Kubernetes 集群添加到 Kuboard 进行管理**
- **步骤：**
  1. 登录 Kuboard 后，点击“添加集群”。
     ```
     ![kuboard添加集群](/images/添加集群.png "kuboard添加集群")
     ```
  2. 按照界面提示，创建一个新的集群或导入现有集群。
     ```
     ![kuboard创建集群](/images/创建集群.png "kuboard创建集群")
     ```
  3. 在其中一个 Master 主机中运行以下命令，将 Kubernetes 集群与 Kuboard 连接：
     ```bash
     # 注意：这条命令需要从 Kuboard 界面复制，下面只是示例
     curl -k 'http://你的HAProxy_IP:80/kuboard-api/cluster/kubernetes-test/kind/KubernetesCluster/kubernetes-test/resource/installAgentToKubernetes?token=你的Token' > kuboard-agent.yaml
     kubectl apply -f ./kuboard-agent.yaml
     ```
     **解释：** 这条命令会下载一个配置文件，并通过 `kubectl` 命令将 Kuboard 的代理安装到 Kubernetes 集群中，让 Kuboard 能监控和管理集群。
  4. 完成后，在 Kuboard 界面中可以看到集群的 Node 信息（类似于工厂里每个工作站的状态）。
     ```
     ![kuboard Node信息](/images/查看node信息.png "kuboard Node信息")
     ```
