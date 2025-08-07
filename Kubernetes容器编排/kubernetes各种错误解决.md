# Kubernetes 清理脚本说明文档

## 1. 背景

在通过 `kubeadm` 安装 Kubernetes 集群时，如果遇到安装失败或需要重新初始化环境，残留的配置文件、数据目录和网络设置可能会导致后续安装失败。因此，需要一个全面的清理脚本，将所有与 Kubernetes 相关的配置、数据和服务移除。

本脚本 `clean.sh` 旨在帮助用户彻底清理 Kubernetes 环境，以便重新开始安装或解决相关问题。

## 2. 脚本内容

以下是 `clean.sh` 脚本的完整内容，并附带每部分功能的说明：

```bash
#!/bin/bash

# 重置 kubeadm
sudo kubeadm reset -f
# 说明：强制重置 kubeadm，移除所有 Kubernetes 集群配置。

# 停止相关服务
sudo systemctl stop kubelet
# 说明：停止 kubelet 服务，避免在清理过程中服务仍在运行。

# 清理所有相关目录
sudo rm -rf /etc/kubernetes/
sudo rm -rf /var/lib/kubelet/
sudo rm -rf /var/lib/etcd/
sudo rm -rf $HOME/.kube/
sudo rm -rf /etc/cni/net.d
# 说明：删除 Kubernetes 的配置文件、数据目录、用户配置和 CNI 网络配置。

# 删除所有 Kubernetes 容器和镜像（可选，如果想完全清理的话）
sudo crictl rm -f $(sudo crictl ps -a -q)
# 说明：强制删除所有 Kubernetes 相关的容器。

# 停止 containerd 服务
sudo systemctl stop containerd
# 说明：停止 containerd 容器运行时服务，以便清理相关数据。

# 清理所有容器运行时和 k8s 相关目录
sudo rm -rf /var/lib/containerd/*
sudo rm -rf /run/containerd/*
sudo rm -rf /var/run/containerd/*
sudo rm -rf /var/lib/cni/*
sudo rm -rf /var/run/cni/*
sudo rm -rf /etc/cni/*
sudo rm -rf /var/lib/kubelet/*
sudo rm -rf /var/run/kubernetes/*
sudo rm -rf /run/flannel/*
sudo rm -rf /var/lib/calico/*
sudo rm -rf /var/run/calico/*
sudo rm -rf /var/lib/etcd/*
sudo rm -rf /etc/kubernetes/*
# 说明：彻底删除容器运行时数据、CNI 网络数据、Kubernetes 数据以及常见网络插件（如 Flannel 和 Calico）的数据。

# 清理网络接口
sudo ip link delete cni0
sudo ip link delete flannel.1
sudo ip link delete calico*
# 说明：删除 Kubernetes 相关的网络接口，包括 CNI、Flannel 和 Calico 创建的接口。

# 清理 iptables 规则
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
# 说明：清除所有 iptables 规则，包括默认表和 NAT、mangle 表，确保网络规则被重置。

# 重启服务
sudo systemctl restart containerd
sudo systemctl restart kubelet
# 说明：重启 containerd 和 kubelet 服务，确保系统恢复到可用的初始状态。
```

## 3. 使用方法

### 3.1 前提条件
- 确保以 `root` 权限或通过 `sudo` 执行脚本。
- 确保系统中已安装 `kubeadm`、`kubelet` 和 `containerd` 等工具（如果未安装，部分命令可能报错，但不影响清理）。
- 建议在执行脚本前备份重要数据（如 `/etc/kubernetes/` 或 `/var/lib/etcd/` 中的数据），以防止误删关键文件。

### 3.2 执行步骤
1. 将上述脚本内容保存为 `clean.sh` 文件。
2. 赋予执行权限：
   ```bash
   chmod +x clean.sh
   ```
3. 执行脚本：
   ```bash
   sudo ./clean.sh
   ```
4. 检查清理结果，确保相关目录和网络接口已被删除。