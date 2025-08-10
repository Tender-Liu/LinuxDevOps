# Kubernetes 工作负载控制器（Deployment）与 服务（Service）

## 学习目标
- 深入理解 Deployment 的使用，掌握无状态应用的部署方式。
- 学习 Service 为应用提供网络访问的原理和配置方法。


## 第一部分：Deployment 详解

### 1.1 Deployment 的概念与理论
- **定义**：Deployment 是 Kubernetes 中用于管理无状态应用的控制器。它通过声明式配置，定义了应用的期望状态（比如运行几个副本、使用哪个镜像），并由 Kubernetes 自动确保实际状态与期望状态一致。
- **通俗理解**：想象 Deployment 是一个“智能工厂经理”，它负责监督一群工人（Pod），确保工人数量正确、工作正常。如果某个工人“生病”或“离职”（Pod 宕机或被删除），经理会立刻安排一个新工人顶上（自动创建新的 Pod）。它还能在不影响工厂生产的情况下，逐步更换工人的工具（滚动更新镜像或配置）。
- **核心功能**：
  - 管理 Pod 的生命周期（创建、销毁、重启）。
  - 维持指定数量的 Pod 副本（高可用性）。
  - 支持滚动更新（逐步替换 Pod，减少停机时间）和回滚（恢复到之前的版本）。

### 1.2 Pod 与 Deployment 的调度过程
- **Pod 的调度过程**：
  - Pod 是 Kubernetes 的最小调度单位，直接运行你的应用容器。
  - 当你创建一个 Pod 时，Kubernetes 的调度器（kube-scheduler）会根据节点的资源情况（CPU、内存等）和 Pod 的资源需求（requests 和 limits），选择一个合适的节点运行 Pod。
  - **问题**：Pod 本身不具备“自我修复”能力。如果 Pod 所在的节点宕机或 Pod 因故障被删除，Kubernetes 不会自动重建 Pod，需要手动重新创建。
  - **通俗比喻**：Pod 就像一个独立的手艺人，接到任务后自己去干活，但如果手艺人病了或工具坏了，没人会自动找替补，必须老板（你自己）亲自安排。

- **Deployment 的调度过程**：
  - Deployment 是一个更高层次的控制器，它不直接运行应用，而是通过管理一组 Pod 来实现应用的部署。
  - 你在 Deployment 中定义期望状态（比如运行 3 个 Pod 副本），Kubernetes 会自动创建和管理这些 Pod。
  - Deployment 背后依赖 ReplicaSet（副本集）来维持 Pod 的数量。ReplicaSet 会不断监控 Pod 的状态，如果发现实际 Pod 数量少于期望数量（比如某个 Pod 宕机），它会立即创建一个新的 Pod；如果多于期望数量，则会删除多余的 Pod。
  - **详细调度流程（包含 Kubernetes 核心组件）**：
    1. **用户发送命令**：你通过 `kubectl apply -f deployment.yml` 提交 Deployment 配置。
    2. **API Server 接收指令**：Kubernetes 的 API Server（集群的“前台接待”）接收到你的请求，验证配置是否合法，并将配置记录到 etcd（集群的“数据库”）中，作为系统的“期望状态”。
    3. **Controller Manager 安排 Deployment**：Controller Manager（集群的“管理者”）中的 Deployment Controller 检测到 etcd 中有新的 Deployment 配置，它会根据配置创建一个 ReplicaSet（副本集），并记录到 etcd 中。
    4. **ReplicaSet 创建 Pod**：ReplicaSet Controller（也是 Controller Manager 的一部分）根据 Deployment 中定义的 `replicas` 数量，创建对应的 Pod 配置，并记录到 etcd 中。
    5. **Scheduler 寻找合适机器**：Scheduler（集群的“调度员”）检测到 etcd 中有未分配节点的 Pod，它会根据节点的资源情况、Pod 的资源需求以及调度策略（如节点亲和性），为每个 Pod 选择一个合适的节点，并将分配结果更新到 etcd 中。
    6. **Kubelet 运行 Pod**：每个节点上的 Kubelet（节点的“执行者”）检测到 etcd 中有分配到本节点的 Pod 配置后，会在本地启动 Pod 中的容器，确保 Pod 正常运行。
    7. **持续监控与修复**：ReplicaSet Controller 持续监控 Pod 的状态（通过 API Server 查询 etcd），如果发现 Pod 数量或状态与期望不符（例如 Pod 宕机），会再次创建或删除 Pod，重复上述调度流程。
  - **通俗比喻**：Deployment 的调度就像一个工厂的生产流程：你（用户）向工厂前台（API Server）提交订单（Deployment 配置），前台记录订单到账本（etcd），工厂经理（Controller Manager）看到订单后安排生产计划（创建 ReplicaSet 和 Pod），调度员（Scheduler）决定每个产品在哪个车间生产（分配节点），最后车间工人（Kubelet）执行具体生产任务（运行 Pod）。如果产品损坏，经理会立刻安排补货（重建 Pod）。
  - **复习核心组件的作用**：
    - **API Server**：集群的入口，接收用户请求并更新状态。
    - **etcd**：集群数据库，存储所有配置和状态信息。
    - **Controller Manager**：运行各种控制器（如 Deployment Controller 和 ReplicaSet Controller），确保资源状态符合期望。
    - **Scheduler**：负责 Pod 的调度，选择合适的节点。
    - **Kubelet**：节点上的代理，负责启动和管理 Pod。

- **Mermaid 图：Deployment 调度流程（包含 Kubernetes 组件）**：
  ```mermaid
  graph TD
    User[用户] -->|提交 Deployment 配置| APIServer[API Server]
    APIServer -->|记录配置| etcd[etcd 数据库]
    etcd -->|通知| ControllerManager[Controller Manager]
    ControllerManager -->|创建 ReplicaSet| etcd
    ControllerManager -->|创建 Pod 配置| etcd
    etcd -->|通知| Scheduler[Scheduler]
    Scheduler -->|分配节点| etcd
    etcd -->|通知| Kubelet[Kubelet]
    Kubelet -->|运行 Pod| Node[节点]
    ControllerManager -->|监控 Pod 状态| etcd
  ```
  **解释**：用户通过 API Server 提交 Deployment 配置，记录到 etcd 中，Controller Manager 创建 ReplicaSet 和 Pod，Scheduler 分配节点，Kubelet 在节点上运行 Pod，整个过程由 Controller Manager 持续监控。

### 1.3 为什么 Pod 不好，需要引入 Deployment？
- **Pod 的局限性**：
  - **缺乏自我修复能力**：Pod 不会自动重启或重新调度。如果节点宕机或 Pod 因故障被删除，需要手动重新创建，非常麻烦。
  - **无法管理副本**：Pod 本身不具备副本概念。如果需要运行多个相同应用的实例以提高可用性，必须手动创建多个 Pod，且无法动态调整数量。
  - **不支持滚动更新**：如果要更新 Pod 的镜像或配置，必须手动删除旧 Pod 并创建新 Pod，容易导致服务中断。
  - **不适合生产环境**：Pod 的管理方式过于原始，难以应对复杂的运维需求（如高可用性、版本管理）。
  - **通俗比喻**：Pod 就像一个单打独斗的手艺人，虽然能干活，但如果生病或任务量增加，老板（你）必须亲自找替补或加人，非常费力。

- **Deployment 的必要性**：
  - **自我修复**：Deployment 通过 ReplicaSet 监控 Pod 状态，自动重建宕机的 Pod，确保服务不中断。
  - **副本管理**：通过 `replicas` 字段，轻松指定 Pod 数量，实现高可用性和负载均衡。
  - **滚动更新与回滚**：Deployment 支持逐步替换 Pod（滚动更新），避免服务中断；如果更新出错，可以快速回滚到上一个版本。
  - **声明式管理**：只需定义期望状态，Kubernetes 自动完成所有操作，减少手动干预。
  - **通俗比喻**：Deployment 就像一个智能工厂经理，不仅能自动安排工人（Pod）数量，还能在不影响生产的情况下逐步更换设备（滚动更新），如果新设备有问题还能立刻换回旧设备（回滚），大大减轻老板（你）的负担。

- **Mermaid 图：Pod 与 Deployment 的管理对比**：
  ```mermaid
  graph TD
    subgraph Pod 管理
      User1[用户] -->|手动创建| PodA[Pod 1]
      User1 -->|手动创建| PodB[Pod 2]
      User1 -->|手动重建| PodC[Pod 3 宕机]
    end
    subgraph Deployment 管理
      User2[用户] -->|定义期望状态| Deployment[Deployment]
      Deployment -->|自动管理| ReplicaSet[ReplicaSet]
      ReplicaSet -->|自动维持| PodX[Pod 1]
      ReplicaSet -->|自动维持| PodY[Pod 2]
      ReplicaSet -->|自动重建| PodZ[Pod 3]
    end
  ```
  **解释**：Pod 管理需要用户手动操作每个 Pod 的创建和重建，而 Deployment 通过声明式配置自动完成所有管理工作，效率更高。

### 1.4 Deployment 的 YAML 语法
- **基本结构**：以下是一个简单的 Deployment YAML 示例，包含常见字段。
  ```yaml
  apiVersion: apps/v1  # 指定 API 版本，Deployment 使用 apps/v1
  kind: Deployment     # 资源类型为 Deployment
  metadata:
    name: my-app       # Deployment 的名称
    namespace: your-pinyin-name  # 所在的命名空间
  spec:
    replicas: 3        # 期望运行的 Pod 副本数
    selector:          # 选择器，用于关联 Deployment 和 Pod
      matchLabels:     # 通过标签匹配 Pod
        app: pod-my-app
    template:          # Pod 模板，定义 Pod 的结构
      metadata:
        labels:        # Pod 的标签，必须与 selector.matchLabels 一致
          app: pod-my-app
      spec:            # Pod 的具体配置
        containers:    # 容器定义
        - name: my-container  # 容器名称
          image: nginx:1.14.2  # 使用的镜像
          ports:       # 容器暴露的端口
          - containerPort: 80  # 容器内部端口号
  ```

- **关键字段说明**：
  - `apiVersion: apps/v1`：Deployment 属于 `apps` 组，版本为 `v1`，与 Pod 的 `v1` 不同。
  - `replicas`：指定 Pod 副本数量，Kubernetes 会自动维持这个数量。
  - `selector.matchLabels`：用于关联 Deployment 和 Pod，必须与 `template.metadata.labels` 一致，否则 Deployment 无法管理 Pod。
  - `template`：定义 Pod 的模板，包含 Pod 的所有配置（相当于一个嵌入的 Pod 定义）。

### 1.5 与之前的 Pod YAML 对比，新增语法的意义
- **之前的 Pod YAML 示例**（保留所有注释，供学员复习）：
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-light-year-admin-template  # Pod 的名称
      namespace: shiqi  # 所在的命名空间
    spec:
      containers:  # 容器配置列表
      - name: light-year-admin-template  # 容器名称
        image: harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi  # 容器镜像地址
        ports:  # 容器暴露的端口
        - containerPort: 80  # 容器内部端口
          name: http  # 端口名称
        resources:  # 资源限制和请求
          requests:  # 资源请求（最低需求）
            cpu: "100m"  # 请求 100 毫核 CPU
            memory: "64Mi"  # 请求 64MB 内存
          limits:  # 资源限制（最大使用）
            cpu: "200m"  # 限制 200 毫核 CPU
            memory: "128Mi"  # 限制 128MB 内存
        livenessProbe:  # 存活探针，检测容器是否存活
          httpGet:  # 使用 HTTP GET 请求检测
            path: /  # 检测路径
            port: 80  # 检测端口
          initialDelaySeconds: 15  # 首次检测延迟 15 秒
          periodSeconds: 10  # 每 10 秒检测一次
        readinessProbe:  # 就绪探针，检测容器是否准备好提供服务
          httpGet:  # 使用 HTTP GET 请求检测
            path: /  # 检测路径
            port: 80  # 检测端口
          initialDelaySeconds: 5  # 首次检测延迟 5 秒
          periodSeconds: 5  # 每 5 秒检测一次
        volumeMounts:  # 挂载卷
        - name: volumes-nginx-conf  # 卷名称
          mountPath: /etc/nginx/nginx.conf  # 挂载到容器内的路径
          subPath: nginx.conf  # 卷中的子路径
      volumes:  # 卷定义
      - name: volumes-nginx-conf  # 卷名称
        configMap:  # 使用 ConfigMap 作为卷来源
          name: configmap-nginx-conf  # ConfigMap 名称
      imagePullSecrets:  # 镜像拉取凭据
      - name: secret-harbor-login  # 镜像仓库登录密钥名称
    ```

- **实践步骤：从 Pod 切换到 Deployment**：
  1. **删除之前的 Pod**：由于我们现在开始使用 Deployment 管理应用，需要先删除之前手动创建的 Pod。
     ```bash
     kubectl delete pod pod-light-year-admin-template -n shiqi
     ```
     **说明**：删除旧 Pod 是为了避免资源冲突，Deployment 会自动创建和管理新的 Pod。
  2. **创建 Deployment YAML 文件**：我们将之前的 Pod 配置转换为 Deployment 配置，并保存为文件。
     - 文件名：`deployment-light-year-admin-template.yml`
     - 内容如下（新增了 `strategy.type: RollingUpdate` 配置）：
        ```yaml
        apiVersion: apps/v1  # 变更：从 v1 改为 apps/v1，因为 Deployment 属于 apps 组
        kind: Deployment     # 变更：从 Pod 改为 Deployment
        metadata:
          name: deployment-light-year-admin-template  # 名称调整，体现资源类型
          namespace: shiqi  # 所在的命名空间
        spec:
          replicas: 2        # 新增：指定 Pod 副本数，实现高可用性
          selector:          # 新增：选择器，用于关联 Deployment 和 Pod
            matchLabels:
              app: pod-light-year-admin-template  # 新增：定义标签，用于匹配 Pod
          strategy:          # 新增：定义更新策略
            type: RollingUpdate  # 设置为滚动更新，确保更新时服务不中断
            rollingUpdate:
              maxSurge: 1      # 最多允许 1 个额外 Pod
              maxUnavailable: 0  # 不允许有不可用 Pod，确保服务始终可用
          template:          # 新增：Pod 模板，包含 Pod 的完整定义
            metadata:
              labels:        # 新增：Pod 标签，必须与 selector.matchLabels 一致
                app: pod-light-year-admin-template
            spec:            # 以下为原 Pod 的 spec 内容，基本保持不变
              containers:  # 容器配置列表
              - name: light-year-admin-template  # 容器名称
                image: harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi  # 容器镜像地址
                ports:  # 容器暴露的端口
                - containerPort: 80  # 容器内部端口
                  name: http  # 端口名称
                resources:  # 资源限制和请求
                  requests:  # 资源请求（最低需求）
                    cpu: "100m"  # 请求 100 毫核 CPU
                    memory: "64Mi"  # 请求 64MB 内存
                  limits:  # 资源限制（最大使用）
                    cpu: "200m"  # 限制 200 毫核 CPU
                    memory: "128Mi"  # 限制 128MB 内存
                livenessProbe:  # 存活探针，检测容器是否存活
                  httpGet:  # 使用 HTTP GET 请求检测
                    path: /  # 检测路径
                    port: 80  # 检测端口
                  initialDelaySeconds: 15  # 首次检测延迟 15 秒
                  periodSeconds: 10  # 每 10 秒检测一次
                readinessProbe:  # 就绪探针，检测容器是否准备好提供服务
                  httpGet:  # 使用 HTTP GET 请求检测
                    path: /  # 检测路径
                    port: 80  # 检测端口
                  initialDelaySeconds: 5  # 首次检测延迟 5 秒
                  periodSeconds: 5  # 每 5 秒检测一次
                volumeMounts:  # 挂载卷
                - name: volumes-nginx-conf  # 卷名称
                  mountPath: /etc/nginx/nginx.conf  # 挂载到容器内的路径
                  subPath: nginx.conf  # 卷中的子路径
              volumes:  # 卷定义
              - name: volumes-nginx-conf  # 卷名称
                configMap:  # 使用 ConfigMap 作为卷来源
                  name: configmap-nginx-conf  # ConfigMap 名称
              imagePullSecrets:  # 镜像拉取凭据
              - name: secret-harbor-login  # 镜像仓库登录密钥名称
        ```
  3. **部署 Deployment**：使用 `kubectl apply` 命令部署文件。
     ```bash
     kubectl apply -f deployment-light-year-admin-template.yml
     ```
     **说明**：此命令会将配置提交到 Kubernetes 集群，Deployment 控制器会自动创建 2 个 Pod 副本。
  4. **通过 Kuboard 界面观察**：登录 Kuboard 管理界面（假设已安装 Kuboard），在 `shiqi` 命名空间下查看 `deployment-light-year-admin-template`，可以看到 Deployment 的状态和 Pod 副本数量。
     - 路径：Kuboard > 命名空间 > shiqi > 工作负载 > Deployment
     - 观察点：Deployment 详情页面会显示 Pod 数量、状态以及更新历史。
  5. **通过命令行验证**：使用以下命令查看 Deployment 和 Pod 状态。
     ```bash
     kubectl get deployment -n shiqi
     kubectl get pod -n shiqi -o wide
     ```
     **说明**：`get deployment` 显示 Deployment 的期望副本数和实际副本数，`get pod` 显示每个 Pod 的状态和所在节点。

- **新增语法及其作用**：
  1. **`apiVersion: apps/v1`**：
     - **变更原因**：Pod 使用 `v1`，而 Deployment 属于 `apps` 组，使用 `apps/v1`。
     - **作用**：确保 Kubernetes 正确识别资源类型和版本。
  2. **`kind: Deployment`**：
     - **变更原因**：从 `Pod` 改为 `Deployment`，表示这是一个控制器资源。
     - **作用**：告诉 Kubernetes 使用 Deployment 控制器管理资源。
  3. **`spec.replicas: 2`**：
     - **作用**：指定运行 2 个 Pod 副本，Kubernetes 会自动维持这个数量。如果某个 Pod 宕机，会自动重建一个新的，确保高可用性。
  4. **`spec.selector.matchLabels`**：
     - **作用**：定义 Deployment 如何找到它管理的 Pod。通过标签匹配，确保 Deployment 能正确识别和控制 Pod。
  5. **`spec.strategy.type: RollingUpdate`**：
     - **作用**：设置更新策略为滚动更新，确保在更新镜像或配置时，Pod 逐步替换，服务不中断。
  6. **`spec.strategy.rollingUpdate.maxSurge: 1`**：
     - **作用**：更新时最多允许 1 个额外 Pod，确保更新速度可控。
  7. **`spec.strategy.rollingUpdate.maxUnavailable: 0`**：
     - **作用**：更新时不允许有不可用 Pod，确保服务始终可用。
  8. **`spec.template`**：
     - **作用**：定义 Pod 的模板，包含 Pod 的完整配置（相当于把 Pod 的 `metadata` 和 `spec` 嵌入到 Deployment 中）。Deployment 根据这个模板创建和管理 Pod。
  9. **`template.metadata.labels`**：
     - **作用**：为 Pod 打上标签，必须与 `selector.matchLabels` 一致，否则 Deployment 无法管理这些 Pod。

- **通俗解释**：从 Pod 到 Deployment，就像从“单人作业”升级到“团队管理”。Pod 是一个人干活，出了问题自己解决不了；而 Deployment 是一个团队经理，定下团队人数（replicas）、工作模式（template），并通过名牌（labels 和 selector）认出自己的团队成员，随时调整和补充人员。

### 1.6 Deployment 的优势（结合实践操作）
以下内容结合实际操作，帮助学员通过命令和 Kuboard 界面直观感受 Deployment 的强大功能。

- **1. 自动管理 Pod 副本**：
  - **优势**：通过 `replicas` 字段，确保指定数量的 Pod 始终运行，实现高可用性和负载均衡。
  - **实践操作与观察**：
    1. 查看当前 Pod 副本数量（应为 3 个）。
       ```bash
       kubectl get pod -n shiqi -o wide
       ```
    2. 手动删除一个 Pod，模拟故障。
       ```bash
       kubectl delete pod <pod-name> -n shiqi
       ```
    3. 再次查看 Pod 列表，观察 Deployment 自动重建 Pod。
       ```bash
       kubectl get pod -n shiqi -o wide
       ```
    4. 登录 Kuboard 界面，在 `shiqi` 命名空间的 Deployment 详情页，查看 Pod 状态变化，确认副本数始终保持为 2。
  - **学习命令**：
    - `kubectl get deployment -n <namespace>`：查看 Deployment 状态。
    - `kubectl describe deployment <deployment-name> -n <namespace>`：查看 Deployment 详细信息，包括事件日志。
    - **通俗比喻**：Deployment 就像一个工厂经理，定下 2 个工人的目标，如果有工人“离职”，经理会立刻招聘新人补上，始终保持人数不变。

- **2. 滚动更新（类型与配置）**：
  - **优势**：更新镜像或配置时，Deployment 会逐步替换 Pod（一个接一个），避免服务中断。
  - **滚动更新的基本原理**：Deployment 在更新时会创建一个新的 ReplicaSet，逐步增加新版本 Pod 的数量，同时减少旧版本 Pod 的数量，直到完全替换完成。
  - **滚动更新的类型**：
    1. **Recreate（重建更新）**：
       - **定义**：先删除所有旧版本 Pod，再创建新版本 Pod。
       - **特点**：会导致服务短暂中断，适合对可用性要求不高的场景。
       - **通俗比喻**：就像工厂停工换设备，先把旧设备全拆掉，再装上新设备，中间生产会暂停。
    2. **RollingUpdate（滚动更新，默认类型）**：
       - **定义**：逐步替换 Pod，保持一定数量的 Pod 始终可用。
       - **特点**：不会导致服务中断，适合生产环境。
       - **配置参数**：
         - `maxSurge`：更新期间最多可以超出 `replicas` 的 Pod 数量（默认 25%），控制更新速度。
         - `maxUnavailable`：更新期间最多不可用的 Pod 数量（默认 25%），确保服务可用性。
       - **通俗比喻**：就像工厂换设备时，一个车间一个车间地换，始终保证大部分车间在生产，不会完全停工。
  - **实践操作与观察**：
    1. 修改滚动更新配置，调整 `maxSurge` 和 `maxUnavailable` 参数，观察更新速度和可用性。
        - 编辑 `deployment-light-year-admin-template.yml`，将 `maxSurge` 改为 2，`maxUnavailable` 改为 1。
          ```yaml
          spec:
            strategy:
              type: RollingUpdate
              rollingUpdate:
                maxSurge: 2  # 最多允许 2 个额外 Pod，加速更新
                maxUnavailable: 1  # 允许 1 个 Pod 不可用，观察服务影响
          ```
        - 或者百分比，调整 `maxSurge` 和 `maxUnavailable` 参数，观察更新速度和可用性。
        ```yaml
          spec:
            strategy:
              type: RollingUpdate
              rollingUpdate:
                maxSurge: 50%  # 最多允许 2 个额外 Pod，加速更新
                maxUnavailable: 50%  # 允许 1 个 Pod 不可用，观察服务影响
          ```
        - 应用更改：
          ```bash
          kubectl apply -f deployment-light-year-admin-template.yml
          ```
    2. 在 Kuboard 界面观察更新过程，查看 Pod 数量变化，确认更新期间服务是否可用。
    3. 使用命令查看更新状态：
       ```bash
       kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
       ```
  - **学习点**：通过调整 `maxSurge` 和 `maxUnavailable`，可以控制更新的速度和服务的可用性，适合不同场景需求。

- **3. 编辑 Deployment 镜像（发布新版本）**：
  - **优势**：发布新版本只需要修改 `template.spec.containers.image` 字段，Deployment 会自动完成滚动更新，操作非常方便。
  - **实践操作与观察（第一次发版）**：
    以下提供三种方式来更新镜像版本，学员可以根据习惯选择最适合自己的方式。建议初学者优先尝试 Kuboard 界面操作，简单直观；有一定基础的学员可以尝试配置文件或命令行操作，深入理解 Kubernetes 的工作原理。
    1. **方式一：通过 Kuboard 界面修改镜像（最简单）**：
       - 登录 Kuboard 管理界面，进入 `shiqi` 命名空间下的 `deployment-light-year-admin-template` 详情页面。
       - 点击“编辑”或“更新镜像”按钮（具体按钮名称根据 Kuboard 版本可能不同），在容器配置中将镜像字段修改为：
         ```
         harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v2
         ```
       - 保存并提交更改，Kuboard 会自动触发滚动更新。
       - 在 Kuboard 界面观察 Pod 逐步替换的过程，查看新旧版本 Pod 的镜像字段变化。
       **说明**：Kuboard 提供了图形化界面，操作直观，无需记住复杂命令，适合初学者。
    2. **方式二：通过修改配置文件更新镜像（推荐）**：
       - 编辑 `deployment-light-year-admin-template.yml` 文件，将 `image` 字段修改为新版本：
         ```yaml
         spec:
           template:
             spec:
               containers:
               - name: light-year-admin-template
                 image: harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v2  # 更新为 v2 版本
         ```
       - 应用更改：
         ```bash
         kubectl apply -f deployment-light-year-admin-template.yml
         ```
       - 查看更新状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
       **说明**：通过配置文件更新镜像，清晰记录了每次变更，便于版本管理和团队协作。
    3. **方式三：通过命令行直接更新镜像（快速但需熟悉命令）**：
       - 使用 `kubectl set image` 命令直接修改镜像版本：
         ```bash
         kubectl set image deployment/deployment-light-year-admin-template light-year-admin-template=harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v2 -n shiqi
         ```
       - 查看更新状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
       **说明**：命令行操作高效，适合自动化脚本或有经验的用户，但容易出错，需谨慎使用。
    - **观察结果**：无论使用哪种方式，Deployment 都会自动触发滚动更新。在 Kuboard 界面或通过命令行观察 Pod 逐步替换的过程，确认新版本镜像已应用。
  - **实践操作与观察（第二次发版）**：
    同样提供三种方式，模拟第二次发版，学员可选择任意一种方式操作。
    1. **方式一：通过 Kuboard 界面修改镜像**：
       - 在 Kuboard 界面中，将镜像字段更新为：
         ```
         harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v3
         ```
       - 保存并提交更改，观察更新历史和 Pod 状态。
    2. **方式二：通过修改配置文件更新镜像**：
       - 编辑 `deployment-light-year-admin-template.yml`，将 `image` 字段更新为：
         ```yaml
         spec:
           template:
             spec:
               containers:
               - name: light-year-admin-template
                 image: harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v3  # 更新为 v3 版本
         ```
       - 应用更改：
         ```bash
         kubectl apply -f deployment-light-year-admin-template.yml
         ```
       - 查看更新状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
    3. **方式三：通过命令行直接更新镜像**：
       - 使用命令更新镜像：
         ```bash
         kubectl set image deployment/deployment-light-year-admin-template light-year-admin-template=harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v3 -n shiqi
         ```
       - 查看更新状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
    - **观察结果**：在 Kuboard 界面查看更新历史和 Pod 状态，确认第二次发版完成。
  - **学习点**：
    - 只需要修改 `image` 字段，Deployment 就会自动完成新版本发布，无需手动删除或创建 Pod，操作简便且无服务中断。
    - 三种操作方式各有优势：Kuboard 界面最直观，适合初学者；配置文件便于管理和追溯；命令行高效但需熟悉语法。建议学员三种方式都尝试，找到最适合自己的操作方式。
  - **通俗比喻**：就像工厂更换设备型号，你可以通过车间管理软件（Kuboard）、书面计划（配置文件）或直接口头指令（命令行）通知经理（Deployment），经理会自动安排工人逐步使用新设备，确保生产不中断。

- **4. 回滚功能**：
  - **优势**：如果更新出错，可以快速回滚到上一个版本。
  - **实践操作与观察**：
    同样提供三种方式来执行回滚操作，学员可根据习惯选择。
    1. **方式一：通过 Kuboard 界面回滚（最简单）**：
       - 登录 Kuboard 界面，进入 `shiqi` 命名空间下的 `deployment-light-year-admin-template` 详情页面。
       - 在“更新历史”或“修订版本”选项中，找到之前的版本（如 v2），点击“回滚”按钮。
       - 确认回滚操作，Kuboard 会自动将 Deployment 恢复到 v2 版本。
       - 观察 Pod 镜像版本回滚到 v2，确认服务恢复正常。
       **说明**：Kuboard 界面操作直观，无需记住命令，适合快速回滚。
    2. **方式二：通过命令行回滚（快速但需熟悉命令）**：
       - 假设第二次发版（v3）有问题，需要回滚到第一次发版（v2）。
         ```bash
         kubectl rollout undo deployment/deployment-light-year-admin-template -n shiqi
         ```
       - 查看回滚状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
       **说明**：命令行回滚高效，适合有经验的用户或自动化场景。
    3. **方式三：通过修改配置文件回滚（记录清晰）**：
       - 编辑 `deployment-light-year-admin-template.yml` 文件，将 `image` 字段改回之前的版本：
         ```yaml
         spec:
           template:
             spec:
               containers:
               - name: light-year-admin-template
                 image: harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v2  # 回滚到 v2 版本
         ```
       - 应用更改：
         ```bash
         kubectl apply -f deployment-light-year-admin-template.yml
         ```
       - 查看回滚状态：
         ```bash
         kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi
         ```
       **说明**：通过配置文件回滚，可以清晰记录每次版本变更，便于管理和追溯。
    - **观察结果**：无论使用哪种方式，在 Kuboard 界面或通过命令行观察 Pod 镜像版本回滚到 v2，确认服务恢复正常。
  - **学习点**：
    - Deployment 自动保存每次更新的历史（Revision），可以通过多种方式快速回滚，降低发版风险。
    - Kuboard 界面回滚最直观，适合初学者；命令行操作高效；配置文件方式便于记录和团队协作。建议学员尝试不同方式，熟悉回滚流程。
  - **通俗比喻**：就像在工厂更换设备后发现新设备有问题，Deployment 能立刻换回旧设备，你可以通过管理软件（Kuboard）、书面计划（配置文件）或口头指令（命令行）通知经理，经理会确保生产恢复正常。

- **5. 声明式配置**：
  - **优势**：只需定义期望状态，Kubernetes 自动完成创建、监控和修复，减少手动操作。声明式配置可以通过配置文件、Kuboard 界面或命令行实现，灵活性高。
  - **实践操作与观察**：
    - **配置文件方式**：通过 `kubectl apply -f` 应用 YAML 文件，定义 Deployment 的期望状态（如副本数、镜像版本），Kubernetes 自动维护。
    - **Kuboard 界面方式**：通过图形化界面编辑 Deployment 配置，修改副本数或镜像版本，提交后 Kubernetes 自动执行。
    - **命令行方式**：通过 `kubectl set image` 或 `kubectl edit` 修改配置，Kubernetes 同样会自动调整到期望状态。
    - **观察结果**：无论使用哪种方式，Kubernetes 都会持续监控并确保实际状态与期望状态一致。例如，若 Pod 数量不足，自动重建；若镜像版本不符，自动更新。
  - **学习点**：
    - 声明式配置的核心是“告诉 Kubernetes 你想要什么”，而无需关心“如何实现”。这大大降低了运维复杂度，尤其适合大规模集群管理。
    - 建议优先使用配置文件方式，便于版本控制和团队协作；Kuboard 界面适合快速调整；命令行适合临时修改或脚本自动化。
  - **通俗比喻**：Deployment 就像一个智能管家，你只需通过手机 App（Kuboard）、书面清单（配置文件）或口头指令（命令行）告诉它“家里要保持 3 个清洁工，用的工具是最新款”，管家会自动招聘、监督和更换清洁工（滚动更新），甚至在出错时恢复到旧工具（回滚），完全不用你操心具体细节。

### 1.7 Deployment 总结命令表格
以下是 Deployment 常用命令的总结表格，方便学员快速上手和复习：

| **命令**                                                                 | **作用**                                   | **示例**                                                                                   |
|-------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------|
| `kubectl apply -f <file>.yml`                                           | 应用 Deployment 配置文件，创建或更新资源       | `kubectl apply -f deployment-light-year-admin-template.yml`                              |
| `kubectl get deployment -n <namespace>`                                 | 查看指定命名空间下的 Deployment 列表          | `kubectl get deployment -n shiqi`                                                       |
| `kubectl describe deployment <name> -n <namespace>`                     | 查看指定 Deployment 的详细信息（包括事件日志） | `kubectl describe deployment deployment-light-year-admin-template -n shiqi`            |
| `kubectl get pod -n <namespace> -o wide`                                | 查看 Pod 列表，包含状态和节点信息             | `kubectl get pod -n shiqi -o wide`                                                      |
| `kubectl delete pod <pod-name> -n <namespace>`                          | 删除指定 Pod（测试自动重建）                  | `kubectl delete pod <pod-name> -n shiqi`                                                |
| `kubectl set image deployment/<name> <container>=<image> -n <namespace>`| 更新 Deployment 的容器镜像，触发滚动更新      | `kubectl set image deployment/deployment-light-year-admin-template light-year-admin-template=harbor.labworlds.cc/light-year-admin-template/master:08061743-shiqi-v2 -n shiqi` |
| `kubectl rollout status deployment/<name> -n <namespace>`               | 查看滚动更新状态                              | `kubectl rollout status deployment/deployment-light-year-admin-template -n shiqi`       |
| `kubectl rollout undo deployment/<name> -n <namespace>`                 | 回滚到上一个版本                              | `kubectl rollout undo deployment/deployment-light-year-admin-template -n shiqi`         |
| `kubectl edit deployment <name> -n <namespace>`                         | 编辑 Deployment 配置（可修改 replicas 等）     | `kubectl edit deployment deployment-light-year-admin-template -n shiqi`                |

**学习建议**：将以上命令结合 Kuboard 界面操作，反复练习 Deployment 的创建、更新和回滚流程，加深对 Deployment 优势的理解。


## 作业 Admin3前后端项目部署 （最佳企业的项目部署）

### 2. 部署介绍
**部署** 是将开发好的代码和程序放到服务器上运行的过程，使得用户可以通过网络访问到这个系统。我们使用 Kubernetes（简称 K8s）作为容器编排工具来管理我们的应用。Kubernetes 是一个强大的系统，可以帮助我们自动管理应用的运行、扩展和故障恢复。

- **部署工具**：我们使用 Docker 将应用打包成镜像（就像一个轻量级的虚拟机），然后通过 Kubernetes 的 Deployment 资源在服务器上运行这些镜像。
- **部署目标**：
  - 将前端和后端分别打包成 Docker 镜像，上传到 Harbor 镜像仓库（一个存储 Docker 镜像的地方）。
  - 在 Kubernetes 集群中部署前端和后端，确保它们可以正常运行并相互通信。
  - 配置资源限制、更新策略和健康检查，确保系统稳定运行。
- **部署顺序**：按照您的要求，我们会先完成前端的部署和测试，确保前端可以正常访问，再进行后端的部署和测试。
- **Deployment 要求**：
  1. **命名规范**：所有资源必须按照规范命名，例如 Deployment、Pod、ConfigMap 等名称需清晰反映其作用和所属项目。
  2. **前端资源限制**：
     - 最小：CPU 50m，内存 64Mi
     - 最大：CPU 100m，内存 128Mi
  3. **后端资源限制**：
     - 最小：CPU 100m，内存 256Mi
     - 最大：CPU 200m，内存 256Mi
  4. **更新策略**：前端和后端均采用滚动更新策略，可以使用数字（如 maxSurge: 1）或百分比（如 maxSurge: 25%）。
  5. **后端 ConfigMap**：合理创建 `configmap-admin3-server.yml`，用于存储后端配置文件（如 `application.yml`），并挂载到后端容器中。


### 实现步骤列表（面向小白用户）

#### 前言：什么是 Kubernetes 和 Docker？
- **Docker**：想象 Docker 是一个打包工具，它把你的程序和程序运行所需的所有东西（比如依赖库、配置文件等）打包成一个“镜像”，就像一个便携的盒子。这个盒子可以在任何支持 Docker 的服务器上运行。
- **Kubernetes (K8s)**：Kubernetes 是一个“管家”，它负责管理很多 Docker 容器（从镜像运行出来的程序实例），确保它们正常运行、自动重启故障容器、分配资源等。我们通过写配置文件（比如 Deployment）告诉 Kubernetes 如何运行和管理我们的程序。

#### 步骤列表：前端部署（先完成并测试）
1. **拉取前端源码**
   - **命令**：`git clone https://gitee.com/Tender-Liu/admin3.git`
   - **解释**：使用 `git clone` 命令从 Gitee（一个代码托管平台）下载 Admin3 项目的源码到本地服务器。这就像从网上下载一个压缩包，只不过这里是代码。
2. **修改前端配置文件**
   - **命令**：
     ```bash
     cd admin3/admin3-ui
     # 编辑 .env 文件，确保 VITE_BASE_URI 设置为指定域名
     echo "VITE_BASE_URI=https://shiqi.admin.labworlds.cc:1443/admin3" > .env
     ```
   - **解释**：进入前端代码目录，修改 `.env` 文件（环境配置文件），设置前端请求后端的域名和路径。就像告诉前端程序“你的后台服务在这个地址，去找它吧”。
3. **构建前端 Docker 镜像**
   - **命令**：`docker build -t harbor.labworlds.cc/admin3-ui/master:081003-shiqi .`
   - **解释**：在当前目录下执行 `docker build` 命令，将前端代码打包成一个 Docker 镜像。`-t` 参数是给镜像起一个名字，包含了仓库地址、项目名、分支和版本号（类似一个标签）。这就像把程序装进一个盒子并贴上标签。
4. **推送前端镜像到 Harbor**
   - **命令**：`docker push harbor.labworlds.cc/admin3-ui/master:081003-shiqi`
   - **解释**：将本地构建好的镜像上传到 Harbor 镜像仓库（一个存储镜像的云端仓库）。这就像把盒子送到一个公共仓库，供其他人或服务器使用。
5. **部署前端到 Kubernetes**
   - **操作**：将之前整理好的 `deployment-admin3-ui.yml` 文件应用到 Kubernetes 集群。
   - **命令**：`kubectl apply -f deployment-admin3-ui.yml`
   - **解释**：`kubectl apply` 命令会读取配置文件，告诉 Kubernetes 按照文件内容创建资源。`Deployment` 是 Kubernetes 中的一种资源类型，它会启动一个或多个 Pod（容器实例）运行你的程序。配置文件中指定了镜像、资源限制、端口等信息。
6. **测试前端是否正常访问**
   - **操作**：通过浏览器访问前端地址 `https://shiqi.admin.labworlds.cc:1443/admin3`，检查页面是否可以正常加载。
   - **命令**（检查 Pod 状态）：`kubectl get pod -n shiqi`
   - **解释**：Pod 是 Kubernetes 中运行容器的最小单位，检查 Pod 状态可以确认前端容器是否正常运行。如果状态显示为 `Running`，说明容器启动成功。如果页面无法访问，可能需要检查日志：`kubectl logs -l app=pod-admin3-ui -n shiqi`。
   - **重要**：只有前端测试通过后（页面能正常打开），我们才会进入后端部署步骤。如果测试失败，需要排查问题（如镜像是否正确、配置文件是否有误等）。

#### 步骤列表：后端部署（前端测试通过后进行）
7. **拉取后端源码**
   - **命令**：`git clone https://gitee.com/Tender-Liu/admin3.git`
   - **解释**：与前端类似，从 Gitee 下载后端代码。
8. **构建后端 Docker 镜像**
   - **命令**：
     ```bash
     cd admin3/admin3-server
     docker build -t harbor.labworlds.cc/admin3-server/master:081003-shiqi .
     ```
   - **解释**：进入后端代码目录，构建后端镜像。注意镜像名称已更正为 `admin3-server`，以区分前端和后端。
9. **推送后端镜像到 Harbor**
   - **命令**：`docker push harbor.labworlds.cc/admin3-server/master:081003-shiqi`
   - **解释**：将后端镜像上传到 Harbor 仓库。
10. **创建后端 ConfigMap**
    - **操作**：将之前整理好的 `configmap-admin3-server.yml` 文件应用到 Kubernetes。
    - **命令**：`kubectl apply -f configmap-admin3-server.yml`
    - **解释**：ConfigMap 是一种 Kubernetes 资源，用于存储配置数据（比如后端的数据库连接信息）。我们通过 ConfigMap 将 `application.yml` 文件内容挂载到后端容器中，供程序读取。
11. **部署后端到 Kubernetes**
    - **操作**：将之前整理好的 `deployment-admin3-server.yml` 文件应用到 Kubernetes。
    - **命令**：`kubectl apply -f deployment-admin3-server.yml`
    - **解释**：与前端类似，通过 Deployment 启动后端容器。配置文件中指定了镜像、资源限制、端口、ConfigMap 挂载等信息。
12. **测试后端是否正常运行**
    - **操作**：检查后端 Pod 状态，并通过前端页面测试是否能正常调用后端接口。
    - **命令**：
      ```bash
      kubectl get pod -n shiqi
      kubectl logs -l app=pod-admin3-server -n shiqi
      ```
    - **解释**：确认后端 Pod 状态为 `Running`，并通过日志检查是否有错误。如果前端页面可以正常登录或加载数据，说明后端接口调用成功。


### 前端和后端配置文件（已整理）
#### 前端 Deployment 配置 (`deployment-admin3-ui.yml`)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-admin3-ui
  namespace: shiqi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-admin3-ui
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: pod-admin3-ui
    spec:
      containers:
      - name: admin3-ui
        image: harbor.labworlds.cc/admin3-ui/master:081003-shiqi
        ports:
        - containerPort: 80
          name: http
        resources:
          requests:
            cpu: "50m"
            memory: "64Mi"
          limits:
            cpu: "100m"
            memory: "128Mi"
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 15
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
      imagePullSecrets:
      - name: secret-harbor-login
```

#### 后端 ConfigMap 配置 (`configmap-admin3-server.yml`)
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: configmap-admin3-server
  namespace: shiqi
data:
  application.yml: |
    spring:
      jpa:
        generate-ddl: true
        defer-datasource-initialization: true
        show-sql: true
        hibernate:
          ddl-auto: update
        properties:
          hibernate.auto_quote_keyword: true
      application:
        name: admin3
      datasource:
        driver-class-name: com.mysql.cj.jdbc.Driver
        url: jdbc:mysql://192.168.110.167:3306/admin3?characterEncoding=utf8
        username: admin
        password: admin123
      sql:
        init:
          encoding: utf8
          data-locations: classpath:data.sql
          mode: always
          continue-on-error: true
      data:
        web:
          pageable:
            one-indexed-parameters: true
      profiles:
        include: biz
    server:
      servlet:
        context-path: /admin3
```

#### 后端 Deployment 配置 (`deployment-admin3-server.yml`)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-admin3-server
  namespace: shiqi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-admin3-server
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: pod-admin3-server
    spec:
      containers:
      - name: admin3-server
        image: harbor.labworlds.cc/admin3-server/master:081003-shiqi
        ports:
        - containerPort: 8080
          name: http
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
        livenessProbe:
          httpGet:
            path: /
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: volumes-admin3-server
          mountPath: /app/application.yml
          subPath: application.yml
      volumes:
      - name: volumes-admin3-server
        configMap:
          name: configmap-admin3-server
      imagePullSecrets:
      - name: secret-harbor-login
```

### 检查命令（必须做）
这些命令用于检查你的程序是否正常运行，类似“医生检查病人”的工具。

1. **查看所有资源状态**：
   - 命令：`kubectl get all -n shiqi`
   - 解释：列出 `shiqi` 命名空间下的所有资源（Deployment、Pod 等），看看它们是否正常。
2. **查看 Deployment 状态**：
   - 命令：`kubectl get deployment -n shiqi`
   - 解释：专门查看 Deployment 是否创建成功，是否所有副本都就绪。
3. **查看 Pod 状态**：
   - 命令：`kubectl get pod -n shiqi`
   - 解释：Pod 是程序运行的地方，状态为 `Running` 说明程序启动了。如果是 `CrashLoopBackOff` 或 `Error`，说明有问题。
4. **查看日志（程序运行记录）**：
   - 前端：`kubectl logs -l app=pod-admin3-ui -n shiqi`
   - 后端：`kubectl logs -l app=pod-admin3-server -n shiqi`
   - 解释：日志就像程序的日记，记录了程序运行中遇到的问题。查看日志可以帮助你找到错误原因。
5. **详细描述资源（排查问题）**：
   - 前端：`kubectl describe deployment deployment-admin3-ui -n shiqi`
   - 后端：`kubectl describe deployment deployment-admin3-server -n shiqi`
   - 解释：如果程序有问题，这个命令会提供更详细的信息，比如为什么 Pod 启动失败。

### Kuboard 界面查看步骤（必须做）
Kuboard 是一个图形化界面，就像 Windows 桌面，比命令行更直观。

1. **登录 Kuboard**：
   - 打开浏览器，输入 Kuboard 的网址（问你的管理员要），输入用户名和密码登录。
2. **选择命名空间**：
   - 登录后，左侧有个菜单，找到“命名空间”，点击 `shiqi`（就像选择一个文件夹）。
3. **查看程序（Deployment 和 Pod）**：
   - 在 `shiqi` 命名空间下，点击“工作负载” -> “Deployment”，你会看到 `deployment-admin3-ui` 和 `deployment-admin3-server`。
   - 点击某个 Deployment，里面有“Pod”选项卡，显示程序是否运行（状态应为绿色或 `Running`）。
4. **查看配置（ConfigMap）**：
   - 左侧菜单选“配置” -> “ConfigMap”，找到 `configmap-admin3-server`，点开可以看到后端配置内容。
5. **查看日志**：
   - 在 Pod 页面，点击某个 Pod，再点“日志”，选择容器名（比如 `admin3-ui`），就能看到程序运行记录。
6. **监控资源**：
   - 在 Deployment 或 Pod 页面，有 CPU 和内存使用图表，确保没有超出限制（就像检查电脑内存是否不够用）。
