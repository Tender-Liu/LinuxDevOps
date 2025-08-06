#### 创建或修改 crictl 配置文件
cat <<EOF | sudo tee /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF

#### 配置文件位置
Containerd 的主配置文件通常位于 `/etc/containerd/config.toml`。如果文件不存在，可以通过以下命令生成默认配置：

```bash
sudo containerd config default > /etc/containerd/config.toml
```

使用文本编辑器打开配置文件：

```bash
sudo vim /etc/containerd/config.toml
```

### 修改配置镜像加速与私有仓库配置

```toml
[plugins."io.containerd.grpc.v1.cri".registry]
  # 我在162行
  config_path = "/etc/containerd/certs.d"

  # mirrors 部分用于配置镜像源，加速公共镜像仓库（如 docker.io）的下载。
  # 以下是为 docker.io 配置国内镜像源的示例。
  # 我在170行
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
    [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
      endpoint = [
        "https://dockerproxy.com",
        "https://docker.m.daocloud.io",
        "https://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.sjtug.sjtu.edu.cn",
        "https://ccr.ccs.tencentyun.com"
      ]
    
    [plugins."io.containerd.grpc.v1.cri".registry.mirrors."quay.io"]
    # 可选：为其他公共镜像仓库（如 quay.io）配置镜像源
      endpoint = ["https://dockerproxy.com", "https://hub-mirror.c.163.com"]
```

### 配置 `sandbox_image`
```bash
# 我在67行
sandbox_image = "registry.aliyuncs.com/google_containers/pause:3.8"
```

#### 保存主配置文件

#### 步骤 2：配置 Harbor 仓库（单独文件）
为了支持私有 Harbor 仓库，推荐使用单独的配置文件，路径为 `/etc/containerd/certs.d/你的仓库域名/`。

1. **创建目录和文件**：
   ```bash
   sudo mkdir -p /etc/containerd/certs.d/harbor.labworlds.cc
   sudo vim /etc/containerd/certs.d/harbor.labworlds.cc/hosts.toml
   ```

2. **写入 Harbor 配置内容**：
   在 `hosts.toml` 文件中添加以下内容，适用于 HTTP 协议或需要跳过 TLS 验证的 Harbor 仓库：

   ```toml
   server = "http://harbor.labworlds.cc"
   [host."http://harbor.labworlds.cc"]
     capabilities = ["pull", "resolve", "push"]
     skip_verify = true
   ```

3. **设置文件权限**：
   限制访问权限以保护认证信息：
   ```bash
   sudo chmod 600 /etc/containerd/certs.d/harbor.labworlds.cc/hosts.toml
   ```

#### 步骤 3：重启 Containerd 服务
使配置生效：

```bash
sudo systemctl daemon-reload
sudo systemctl restart containerd
sudo systemctl enable containerd
```

#### 步骤 4：验证配置
1. **检查镜像源配置**：
   查看 Containerd 配置是否包含镜像源：
   ```bash
   crictl info | grep -A 10 registry
   ```

2. **测试拉取 Docker Hub 镜像**：
   验证国内镜像源是否生效：
   ```bash
   crictl pull docker.io/library/busybox:latest
   ```

3. **测试拉取 Harbor 镜像**：
   验证 Harbor 仓库配置是否正确：
   ```bash
   crictl pull harbor.labworlds.cc/go-starter/dev:lbw-v1.0
   ```

4. **查看日志（如果有问题）**：
   如果拉取镜像失败，检查日志：
   ```bash
   journalctl -u containerd | grep -i harbor
   ```

好的，我会将你提供的内容整合到标题为“9. 修改 Docker 配置与 Containerd 下载镜像使用国内源：”的格式中，并确保内容结构清晰、易于理解。以下是优化后的文档内容：

---

## 9. 修改 Docker 配置与 Containerd 下载镜像使用国内源

本文档将指导你如何配置 Containerd 使用国内镜像源以加速镜像下载，并设置私有 Harbor 仓库支持。

### 9.1 创建或修改 crictl 配置文件

配置 `crictl` 工具的运行时和镜像端点：

```bash
cat <<EOF | sudo tee /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF
```

### 9.2 Containerd 配置文件位置

Containerd 的主配置文件通常位于 `/etc/containerd/config.toml`。如果该文件不存在，可以通过以下命令生成默认配置：

```bash
sudo containerd config default > /etc/containerd/config.toml
```

使用文本编辑器打开配置文件进行编辑：

```bash
sudo vim /etc/containerd/config.toml
```

### 9.3 修改配置镜像加速与私有仓库配置

在配置文件中找到 `[plugins."io.containerd.grpc.v1.cri".registry]` 部分（通常在第 162 行附近），并按以下内容修改或添加：

```toml
[plugins."io.containerd.grpc.v1.cri".registry]
  # 我在162行
  config_path = "/etc/containerd/certs.d"

  # mirrors 部分用于配置镜像源，加速公共镜像仓库（如 docker.io）的下载。
  # 以下是为 docker.io 配置国内镜像源的示例。
  # 我在170行
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
    [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
      endpoint = [
        "https://dockerproxy.com",
        "https://docker.m.daocloud.io",
        "https://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.sjtug.sjtu.edu.cn",
        "https://ccr.ccs.tencentyun.com"
      ]
    
    [plugins."io.containerd.grpc.v1.cri".registry.mirrors."quay.io"]
    # 可选：为其他公共镜像仓库（如 quay.io）配置镜像源
      endpoint = ["https://dockerproxy.com", "https://hub-mirror.c.163.com"]
```

### 9.4 配置 `sandbox_image`

在配置文件中找到 `sandbox_image` 字段（通常在第 67 行附近），并修改为以下内容：

```toml
# 我在67行
sandbox_image = "registry.aliyuncs.com/google_containers/pause:3.8"
```

### 9.5 保存主配置文件

编辑完成后，保存 `/etc/containerd/config.toml` 文件。

### 9.6 配置 Harbor 仓库（单独文件）

为了支持私有 Harbor 仓库，推荐使用单独的配置文件，路径为 `/etc/containerd/certs.d/你的仓库域名/`。

1. **创建目录和文件**：
   ```bash
   sudo mkdir -p /etc/containerd/certs.d/harbor.labworlds.cc
   sudo vim /etc/containerd/certs.d/harbor.labworlds.cc/hosts.toml
   ```

2. **写入 Harbor 配置内容**：
   在 `hosts.toml` 文件中添加以下内容，适用于 HTTP 协议或需要跳过 TLS 验证的 Harbor 仓库：

   ```toml
   server = "http://harbor.labworlds.cc"
   [host."http://harbor.labworlds.cc"]
     capabilities = ["pull", "resolve", "push"]
     skip_verify = true
   ```

3. **设置文件权限**：
   限制访问权限以保护认证信息：
   ```bash
   sudo chmod 600 /etc/containerd/certs.d/harbor.labworlds.cc/hosts.toml
   ```

### 9.7 重启 Containerd 服务

使配置生效，需要重启 Containerd 服务：

```bash
sudo systemctl daemon-reload
sudo systemctl restart containerd
sudo systemctl enable containerd
```

---

### 优化说明

1. **标题编号统一**：将内容整合到“9. 修改 Docker 配置与 Containerd 下载镜像使用国内源”下，并为每个小节添加子编号（如 9.1、9.2），保持结构一致性。
2. **内容清晰**：每个小节专注于一个具体步骤，方便用户按顺序操作。
3. **格式规范**：代码块和说明文字分开，确保配置内容易于复制和理解。

如果你有其他调整需求或希望进一步优化某些部分，请随时告诉我！
