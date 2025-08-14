### StatefulSet 部署 Redis - 动态分配的PV

#### 1. 登录 NFS 主机并创建目录
- **目标**：在 NFS 服务器 `192.168.110.168` 上创建一个目录 `/nfs/shiqi-redis-not-exist-pvc`，用于 Redis 数据的持久化存储。
- **步骤**：
  1. **登录 NFS 主机**：使用 SSH 登录到 NFS 服务器（假设已配置好 NFS 服务）。
     ```
     ssh user@192.168.110.168
     ```
  2. **创建目录**：创建指定目录并设置权限。
     ```
     sudo mkdir -p /nfs/shiqi-redis-not-exist-pvc
     sudo chmod -R 777 /nfs/shiqi-redis-not-exist-pvc  # 教学环境使用，生产环境应设置更严格权限
     ```
  3. **验证目录**：确认目录已创建。
     ```
     ls -ld /nfs/shiqi-redis-not-exist-pvc
     ```
  4. **检查 NFS 共享配置**：确保 `/nfs` 已配置为共享目录。如果未配置，需编辑 `/etc/exports` 文件并重启 NFS 服务。
     ```
     sudo vi /etc/exports  # 添加或确认共享配置，例如：/nfs *(rw,sync,no_root_squash)
     sudo systemctl restart nfs  # 重启 NFS 服务
     ```

**优化说明**：增加了 NFS 共享配置的具体命令示例，便于初学者操作。


#### 2. 提前准备 PV
- **目标**：创建一个 PersistentVolume (PV)，为后续动态创建的 PVC 提供存储资源。
- **文件**：`pv-shiqi-redis-not-exist-pvc.yml`
- **YAML 定义**：
  ```yaml
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    name: pv-shiqi-redis-not-exist-pvc
  spec:
    capacity:
      storage: 64Mi
    accessModes:
      - ReadWriteOnce  # 支持多个 Pod 读写（注意：Redis 更适合 ReadWriteOnce）
    reclaimPolicy: Retain  # 数据保留策略，删除 PVC 后 PV 不会被自动删除
    nfs:
      path: /nfs/shiqi-redis-not-exist-pvc
      server: 192.168.110.168
  ```
- **创建命令**：
  ```
  kubectl apply -f pv-shiqi-redis-not-exist-pvc.yml
  ```

**优化说明**：对 `accessModes` 增加了说明，提醒用户 Redis 更适合 `ReadWriteOnce` 模式，避免误解。


#### 3. 创建 StatefulSet（使用模板动态创建 PVC）
- **目标**：通过 `volumeClaimTemplates` 让 Kubernetes 自动为每个 Pod 创建独立的 PVC，实现数据持久化。
- **文件**：`statefulset-redis-not-exist-pvc.yml`
- **YAML 定义**：
  ```yaml
  apiVersion: apps/v1
  kind: StatefulSet
  metadata:
    name: statefulset-redis-not-exist-pvc
    namespace: shiqi
    labels:
      app: redis-not-exist-pvc
      version: "7.4.4"
  spec:
    serviceName: "redis-not-exist-pvc"  # 关联 Headless Service，用于 Pod 间网络发现
    replicas: 1  # 单实例 Redis，生产环境可根据需求调整
    selector:
      matchLabels:
        app: redis-not-exist-pvc
    template:
      metadata:
        labels:
          app: redis-not-exist-pvc
          version: "7.4.4"
      spec:
        containers:
        - name: redis
          image: swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/redis:7.4.4
          ports:
          - containerPort: 6379
            name: redis
          resources:
            requests:
              memory: "64Mi"
              cpu: "100m"
            limits:
              memory: "128Mi"
              cpu: "100m"
          livenessProbe:
            tcpSocket:
              port: 6379
            initialDelaySeconds: 30
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
            successThreshold: 1
          readinessProbe:
            exec:
              command:
              - redis-cli
              - ping
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
            successThreshold: 1
          volumeMounts:
          - name: pvc-shiqi  # 与 volumeClaimTemplates 的名称一致
            mountPath: /data  # Redis 数据存储目录
        restartPolicy: Always
    volumeClaimTemplates:  # 动态创建 PVC 模板
    - metadata:
        name: pvc-shiqi  # PVC 名称前缀，实际名称会附加 Pod名 + 序号（如 redis-not-exist-pvc-0）
      spec:
        accessModes:
        - ReadWriteOnce  # 单个 Pod 读写，适合 Redis 单实例
        resources:
          requests:
            storage: 64Mi  # 请求存储空间
        storageClassName: ""  # 空字符串表示不使用动态供应，匹配静态 PV
  ```


#### 4. 部署与验证步骤
- **目标**：通过命令行或图形界面部署 StatefulSet，并验证其运行状态及数据持久化。
- **步骤**：
  1. **保存 YAML 文件**：将上述 StatefulSet YAML 内容保存为 `statefulset-redis-not-exist-pvc.yml`。
  2. **应用配置文件**：使用以下命令部署 StatefulSet。
     ```
     kubectl apply -f statefulset-redis-not-exist-pvc.yml
     ```
  3. **检查 StatefulSet 状态**：确认 StatefulSet 是否成功创建。
     ```
     kubectl get statefulsets -n shiqi
     ```
     预期输出类似：
     ```
     NAME                             READY   AGE
     statefulset-redis-not-exist-pvc  1/1     2m
     ```
  4. **检查 Pod 状态**：确认 Pod 是否正常运行。
     ```
     kubectl get pods -n shiqi
     ```
     预期输出类似：
     ```
     NAME                               READY   STATUS    RESTARTS   AGE
     statefulset-redis-not-exist-pvc-0  1/1     Running   0          2m
     ```
  5. **检查 PVC 状态**：确认动态创建的 PVC 是否绑定成功。
     ```
     kubectl get pvc -n shiqi
     ```
     预期输出类似：
     ```
     NAME                        STATUS   VOLUME                       CAPACITY   ACCESS MODES   STORAGECLASS   AGE
     redis-data-statefulset-redis-not-exist-pvc-0  Bound    pv-shiqi-redis-not-exist-pvc  64Mi       RWO                           2m
     ```
  6. **验证挂载情况**：进入 Pod 内部，确认 `/data` 目录是否已挂载。
     ```
     kubectl exec -it statefulset-redis-not-exist-pvc-0 -n shiqi -- /bin/bash
     ls -ld /data
     ```
     预期输出类似：
     ```
     drwxrwxrwx 2 redis redis 4096 Aug 14 21:03 /data
     ```

#### 5. 验证 Redis 数据持久化
- **目标**：确认 Redis 数据是否正确存储在动态创建的 PVC 挂载目录下。
- **步骤**：
  1. **进入 Redis 容器**：使用以下命令进入 Redis 容器。
     ```
     kubectl exec -it statefulset-redis-not-exist-pvc-0 -n shiqi -- /bin/bash
     ```
  2. **检查数据目录**：查看 `/data` 目录下的文件，确认 Redis 数据文件是否存在。
     ```
     ls -l /data
     ```
     预期输出类似：
     ```
     total 4
     -rw-r--r-- 1 redis redis 1024 Aug 14 21:03 dump.rdb
     ```
     **说明**：Redis 默认将数据持久化存储为 `dump.rdb` 文件。
  3. **写入测试数据**：使用 Redis CLI 写入一些测试数据。
     ```
     redis-cli
     SET testkey "Hello, Redis Dynamic PVC!"
     GET testkey
     SAVE
     ```
     预期输出：
     ```
     "Hello, Redis Dynamic PVC!"
     ```
     **说明**：`SAVE` 命令会强制将数据写入磁盘，更新 `/data/dump.rdb` 文件。
  4. **验证数据持久化**：删除 Pod，模拟 Pod 重启，确认数据是否依然存在。
     ```
     kubectl delete pod statefulset-redis-not-exist-pvc-0 -n shiqi
     kubectl get pods -n shiqi -w  # 等待 Pod 重新创建
     kubectl exec -it statefulset-redis-not-exist-pvc-0 -n shiqi -- redis-cli GET testkey
     ```
     预期输出：
     ```
     "Hello, Redis Dynamic PVC!"
     ```
     **说明**：由于 PVC 的持久化存储，即使 Pod 被删除重建，数据依然保留。

### 3. 作业：深入理解 Redis 与 StatefulSet

为了帮助你更深入地理解为什么 Redis 需要使用 StatefulSet 而不是 Deployment，请完成以下作业：

1. **思考与回答**：Redis 使用 StatefulSet 的原因是什么？请从以下几个方面分析并写下你的理解：
   - **持久化存储**：Redis 的数据需要持久化，以防止数据丢失。StatefulSet 如何通过 PVC 提供持久化存储的能力？
   - **稳定的网络标识**：StatefulSet 为每个 Pod 分配一个唯一的、稳定的网络标识，这对 Redis 集群模式中的节点间通信有何重要意义？
   - **有序部署与扩展**：StatefulSet 支持有序的部署和扩展，确保 Redis 实例按照特定顺序启动和停止，这对数据一致性有何帮助？

2. **实践扩展**：尝试将 StatefulSet 的副本数（`replicas`）从 1 增加到 3，观察 PVC 和 Pod 的创建情况。记录 Kubernetes 如何为每个 Pod 分配独立的 PVC（如果使用了 `volumeClaimTemplates`）。

**提示**：你可以通过修改 YAML 文件中的 `replicas` 字段，然后重新应用配置文件来完成扩展：
```bash
kubectl apply -f redis-dynamic-statefulset.yaml
```


