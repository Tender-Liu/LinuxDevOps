#  containerd 配置文件重置
containerd config default > /etc/containerd/config.toml

# 创建或修改 crictl 配置文件
cat <<EOF | sudo tee /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF
# 这个配置确保 crictl 能够正确连接到 containerd 服务

# 重启 containerd 服务：
sudo systemctl daemon-reload
sudo systemctl restart containerd




以下是优化后的教案，内容更加清晰地解释了 VIP 的概念，并补充了在没有 VIP 地址时如何直接使用 Nginx 的 IP 作为 `control-plane-endpoint` 的方案。同时，明确了 Nginx 配置需要使用 `stream` 模块来处理 TCP 流量，而不是 `server` 块中的 HTTP 代理。Keepalived 的高可用方案在此不做赘述，专注于核心步骤和注意事项。

---

## Kubernetes 高可用集群部署教案

### 第一部分：3 台 Master 节点高可用部署
- **内容目标：** 使用 `kubeadm` 工具初始化第一台 Master 节点，并将其他两台 Master 节点加入，形成高可用集群。
- **VIP 概念说明：**
  - **什么是 VIP？** VIP（Virtual IP，虚拟 IP 地址）是一个虚拟的 IP 地址，通常不直接绑定到某台具体的物理机器上，而是由负载均衡器（如 Nginx、HAProxy）或高可用工具（如 Keepalived）管理。在 Kubernetes 高可用集群中，VIP 作为控制平面的统一入口，客户端（如 `kubectl`）通过这个地址访问集群的 API Server。
  - **VIP 作用：** 通过 VIP 和负载均衡器，即使某个 Master 节点宕机，请求仍会被转发到其他可用的 Master 节点，从而保证控制平面的高可用性。
  - **VIP 配置说明：** 在本教案中，我们将 VIP 设置为 `192.168.1.100`（可根据实际环境调整）。如果没有独立的 VIP 地址，可以直接使用负载均衡器（如 Nginx）服务器的 IP 地址作为 `control-plane-endpoint`，但这会导致单点故障风险（即负载均衡器宕机时控制平面不可用）。
- **详细步骤：**
  1. **初始化第一台 Master 节点（Master 1）：**
     - 在 `k8s-master1` 上执行初始化命令，生成集群配置文件。
     - 命令（根据您的环境 IP 和配置调整）：
       ```bash
       sudo kubeadm init \
       --pod-network-cidr=10.244.0.0/16 \
       --service-cidr=10.96.0.0/12 \
       --apiserver-advertise-address=192.168.1.101 \
       --control-plane-endpoint=192.168.1.100 \
       --image-repository=registry.aliyuncs.com/google_containers \
       --cri-socket=unix:///var/run/containerd/containerd.sock \
       --upload-certs
       ```
       - **参数说明：**
         - `--pod-network-cidr=10.244.0.0/16`：指定 Pod 网络范围，供后续网络插件（如 Calico）使用。
         - `--service-cidr=10.96.0.0/12`：指定 Service 网络范围，用于集群内部服务通信。
         - `--apiserver-advertise-address=192.168.1.101`：指定当前 Master 的 IP 地址（即 `k8s-master1` 的 IP）。
         - `--control-plane-endpoint=192.168.1.100`：指定统一的控制平面入口地址（通常为 VIP，由负载均衡器监听）。如果没有独立的 VIP，可以直接使用负载均衡器（如 Nginx）服务器的 IP 地址，详见后续说明。
         - `--image-repository=registry.aliyuncs.com/google_containers`：使用阿里云镜像源加速镜像下载。
         - `--cri-socket=unix:///var/run/containerd/containerd.sock`：指定容器运行时为 Containerd。
         - `--upload-certs`：上传证书，方便其他 Master 节点加入。
     - **重要提示：保存初始化输出内容：**
       - 初始化完成后，终端会输出大量信息，包括 `kubeadm join` 命令等关键内容。
       - 必须保存这些输出内容，否则后续加入节点时需要重新生成，非常麻烦。
       - 命令：
         ```bash
         # 将输出内容保存到文件中
         vim kubeadm-init.txt
         # 或者在初始化时重定向输出：
         sudo kubeadm init [参数列表] | tee kubeadm-init.txt
         ```
       - **kubeadm-init.txt 文件中的三个重要部分：**
         1. **kubectl 命令配置部分：** 用于配置本地 kubectl 工具，使其能连接到集群。
            - 示例内容：
              ```bash
              mkdir -p $HOME/.kube
              sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
              sudo chown $(id -u):$(id -g) $HOME/.kube/config
              ```
            - 作用：将集群配置文件复制到用户目录下，kubectl 工具会读取该文件与集群通信。
         2. **Master 节点加入命令：** 用于将其他 Master 节点加入集群，形成高可用控制平面。
            - 示例内容（以实际初始化输出为准）：
              ```bash
              kubeadm join 192.168.1.100:6443 --token dg7bkm.77u82668vm6qon11 \
              --discovery-token-ca-cert-hash sha256:48f573d1fd60a667775206855e31220897bf018b6f0b9b07912d73a72e77e954 \
              --control-plane --certificate-key 6c5fd8bee32be7e14b600a61d8bc189298f587a46b1f8adbd8eb6c6b5eaea0cd
              ```
            - 注意：`--control-plane` 表示作为控制平面节点加入，`--certificate-key` 用于下载证书，需妥善保存。
         3. **Node 节点加入命令：** 用于将工作节点（Worker Node）加入集群，运行实际工作负载。
            - 示例内容（以实际初始化输出为准）：
              ```bash
              kubeadm join 192.168.1.100:6443 --token dg7bkm.77u82668vm6qon11 \
              --discovery-token-ca-cert-hash sha256:48f573d1fd60a667775206855e31220897bf018b6f0b9b07912d73a72e77e954
              ```
     - **配置 kubectl 工具：**
       - 根据初始化输出中的 kubectl 配置命令，设置本地环境。
       - 命令：
         ```bash
         mkdir -p $HOME/.kube
         sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
         sudo chown $(id -u):$(id -g) $HOME/.kube/config
         ```
       - 验证：`kubectl get nodes` 查看当前节点状态（暂时只有 Master 1）。
  2. **配置负载均衡器（Nginx）以支持控制平面高可用：**
     - **前提说明：** Kubernetes 高可用集群需要一个负载均衡器来将请求分发到多个 Master 节点。以下使用 Nginx 作为负载均衡器，监听 `control-plane-endpoint` 指定的地址（即 `192.168.1.100:6443`）。
     - **情况 1：有独立 VIP 地址（如 `192.168.1.100`）：**
       - 选择一台独立服务器（推荐）或暂时使用一台 Master 节点安装 Nginx。
       - 安装 Nginx：
         ```bash
         sudo apt update
         sudo apt install nginx -y  # Ubuntu/Debian
         sudo yum install nginx -y  # CentOS/RHEL
         ```
       - 配置 Nginx（使用 `stream` 模块处理 TCP 流量）：
         - 编辑或创建配置文件 `/etc/nginx/conf.d/kubernetes.conf`：
           ```nginx
           stream {
               upstream kubernetes {
                   server 192.168.1.101:6443;
                   server 192.168.1.102:6443;
                   server 192.168.1.103:6443;
               }
               server {
                   listen 192.168.1.100:6443;
                   proxy_pass kubernetes;
               }
           }
           ```
         - **说明：**
           - `stream` 模块用于处理 TCP/UDP 流量，Kubernetes API Server 使用的是 TCP 协议（端口 6443），因此不能使用 HTTP 模块的 `server` 块。
           - `upstream kubernetes` 定义了后端 Master 节点的 IP 和端口（根据实际 Master IP 调整）。
           - `listen 192.168.1.100:6443` 表示监听 VIP 地址和端口。
         - 如果 `192.168.1.100` 不是 Nginx 服务器的物理 IP，需要手动绑定：
           ```bash
           sudo ip addr add 192.168.1.100/24 dev eth0
           ```
           （将 `eth0` 替换为实际网卡名称）
       - 重启 Nginx：
         ```bash
         sudo systemctl restart nginx
         sudo systemctl enable nginx
         ```
       - 验证：使用 `curl https://192.168.1.100:6443` 测试是否有响应（会提示证书错误，但应有返回）。
     - **情况 2：没有独立 VIP 地址，直接使用 Nginx 服务器的 IP：**
       - 如果没有独立的 VIP 地址，可以直接将 Nginx 服务器的 IP 地址（如 `192.168.1.100`）用作 `control-plane-endpoint`。
       - **代价：** 这会导致单点故障风险，如果 Nginx 服务器宕机，控制平面将不可用。但作为学习或测试环境，这是一个简化的方案。
       - 配置步骤：
         - 假设 Nginx 服务器的 IP 就是 `192.168.1.100`，则 `kubeadm init` 命令中的 `--control-plane-endpoint` 已经设置为 `192.168.1.100`。
         - 配置 Nginx（同样使用 `stream` 模块）：
           ```nginx
           stream {
               upstream kubernetes {
                   server 192.168.1.101:6443;
                   server 192.168.1.102:6443;
                   server 192.168.1.103:6443;
               }
               server {
                   listen 192.168.1.100:6443;
                   proxy_pass kubernetes;
               }
           }
           ```
         - 重启 Nginx：
           ```bash
           sudo systemctl restart nginx
           sudo systemctl enable nginx
           ```
         - 验证：使用 `curl https://192.168.1.100:6443` 测试是否有响应。
  3. **加入第二台和第三台 Master 节点：**
     - 在 `k8s-master2` 和 `k8s-master3` 上执行 `kubeadm join` 命令（从 `kubeadm-init.txt` 文件中获取 Master 加入命令）。
     - 示例命令（根据实际输出调整）：
       ```bash
       sudo kubeadm join 192.168.1.100:6443 --token dg7bkm.77u82668vm6qon11 \
       --discovery-token-ca-cert-hash sha256:48f573d1fd60a667775206855e31220897bf018b6f0b9b07912d73a72e77e954 \
       --control-plane --certificate-key 6c5fd8bee32be7e14b600a61d8bc189298f587a46b1f8adbd8eb6c6b5eaea0cd
       ```
     - 重复以上步骤在 `k8s-master3` 上执行相同命令。
     - 配置 kubectl 工具（每台 Master 都需要）：
       ```bash
       mkdir -p $HOME/.kube
       sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
       sudo chown $(id -u):$(id -g) $HOME/.kube/config
       ```
     - 验证：在任意 Master 上执行 `kubectl get nodes`，应看到 3 台 Master 节点，状态为 `NotReady`（因未安装网络插件）。
  4. **安装 CNI 网络插件（Calico）：**
     - 在任意一台 Master 节点上安装 Calico 网络插件，确保 Pod 间通信。
     - 命令（考虑到网络限制，建议提前下载文件）：
       ```bash
       # 下载 Calico YAML 文件（若无法直接下载，可在本地下载后传输到 Linux）
       curl https://raw.githubusercontent.com/projectcalico/calico/v3.28.2/manifests/calico.yaml -O
       
       # 更新镜像源为国内源（华为云镜像源示例）
       sed -i 's|docker.io/|swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/|g' calico.yaml

       # 编辑 calico.yaml 文件，修改 Pod 网络 CIDR
       vim calico.yaml
       # 找到以下行并取消注释，确保与初始化时的 --pod-network-cidr 一致
       # - name: CALICO_IPV4POOL_CIDR
       #   value: "10.244.0.0/16"
       
       # 安装 Calico 至 Kubernetes 集群
       kubectl apply -f calico.yaml
       ```
     - 验证：等待几分钟后，执行 `kubectl get nodes`，状态应变为 `Ready`。
     - 验证 Pod 网络：`kubectl get pods -n kube-system`，确保 Calico 相关 Pod 运行正常（如 `calico-node`、`calico-kube-controllers` 等）。
- **互动与检查：** 每完成一步，检查节点状态，鼓励学员互相确认 3 台 Master 是否都显示 `Ready`。特别强调保存 `kubeadm-init.txt` 的重要性，教师或助教解答问题。

### 第二部分：2 台 Node 节点加入集群
- **内容目标：** 将 2 台 Node 节点加入 Kubernetes 集群，扩展工作负载能力。
- **详细步骤：**
  1. **获取加入命令：**
     - 从 `kubeadm-init.txt` 文件中获取 Node 节点加入命令。
     - 如果文件丢失或 Token 过期，可在任意 Master 节点上重新生成：
       ```bash
       kubeadm token create --print-join-command
       ```
  2. **加入 Node 节点：**
     - 在 `k8s-node1` 和 `k8s-node2` 上执行从 `kubeadm-init.txt` 中获取的 `kubeadm join` 命令。
     - 示例命令（根据实际输出调整）：
       ```bash
       sudo kubeadm join 192.168.1.100:6443 --token dg7bkm.77u82668vm6qon11 \
       --discovery-token-ca-cert-hash sha256:48f573d1fd60a667775206855e31220897bf018b6f0b9b07912d73a72e77e954
       ```
  3. **验证：**
     - 在任意 Master 节点上执行 `kubectl get nodes`，应看到 5 个节点（3 Master + 2 Node），状态为 `Ready`。
     - 检查 Calico 网络插件是否在 Node 节点上运行：
       ```bash
       kubectl get pods -n kube-system -o wide
       ```
       - 确认每个节点上都有 `calico-node` Pod 运行。
- **互动与检查：** 确认所有节点加入成功，解答学员关于节点状态或加入失败的疑问。
