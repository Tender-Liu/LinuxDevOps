好的，我会为第三部分“基本命令学习——Pod 管理（结合 Kuboard 界面）”添加一个总结表格，方便同学们日后快速参考 `kubectl` 命令和 Kuboard 界面操作的对应关系。以下是更新后的内容，将表格添加到“总结与对比”小节中，并确保整体逻辑连贯。

---

### 第三部分：基本命令学习——Pod 管理（结合 Kuboard 界面）

#### 学习目标

通过本部分的学习，同学们将掌握：
- 使用 `kubectl` 命令行工具管理 Pod，包括创建、删除、查看状态和日志等操作。
- 使用 Kuboard 界面管理 Pod，理解图形化工具与命令行操作的对应关系。
- 对比命令行和图形化界面的操作方式，降低学习曲线，提升对 Kubernetes 资源管理的理解。

#### 前期准备

在开始本部分的学习之前，确保你已经完成了以下准备工作：
- 完成了第二部分的实践练习，已经在自己的 Namespace 中创建并部署了一个 Pod（例如 `pod-stars-emmision`）。
- 确保 `kubectl` 工具已正确配置，可以与 Kubernetes 集群通信。
- 确保你有权限访问 Kuboard 管理界面，并已知晓登录地址、用户名和密码（由老师提供）。
- 熟悉基本的终端操作（Windows 使用 PowerShell 或 CMD，Mac 使用 Terminal）。

#### 学习内容

我们将通过命令行工具 `kubectl` 和 Kuboard 图形化界面两种方式学习 Pod 的基本管理操作。以下内容会逐一介绍每个操作，并提供命令行和界面对应的步骤，方便同学们对比学习。

##### 1. 查看 Pod 列表

了解当前 Namespace 中运行的 Pod 是管理的第一步。我们可以通过命令行和 Kuboard 界面查看 Pod 列表及其状态。

- **命令行操作（使用 `kubectl`）**：
  打开终端，输入以下命令查看当前 Namespace 中的 Pod 列表（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl get pods -n your-pinyin-name
  ```
  输出结果会显示 Pod 的名称、状态（例如 `Running`）、重启次数和运行时间等信息。如果不指定 Namespace，可以使用以下命令查看所有 Namespace 中的 Pod：
  ```bash
  kubectl get pods --all-namespaces
  ```
  **小贴士**：如果列表中没有看到你的 Pod，可能是 Namespace 名称输入错误或 Pod 尚未创建成功。

- **Kuboard 界面操作**：
  1. 打开浏览器，访问老师提供的 Kuboard 登录地址（例如 `http://kuboard.your-cluster-domain.com`）。
  2. 使用提供的用户名和密码登录 Kuboard。
  3. 在页面顶部或左侧导航栏中找到 Namespace 选择框，选择你的 Namespace（例如 `your-pinyin-name`）。
  4. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项。
  5. 在 Pod 列表页面，你可以看到当前 Namespace 中所有 Pod 的名称、状态（例如绿色表示 `Running`）、所属节点和创建时间等信息。
  **小贴士**：如果列表中没有看到你的 Pod，可以刷新页面或确认是否选择了正确的 Namespace。

##### 2. 查看 Pod 详情

当需要了解 Pod 的详细信息（例如镜像、端口、事件等）时，可以查看 Pod 的详细描述。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，查看特定 Pod 的详细信息（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl describe pod pod-stars-emmision -n your-pinyin-name
  ```
  输出结果会显示 Pod 的基本信息、容器配置、状态以及相关事件（Events），例如镜像拉取是否成功或容器启动是否正常。
  **小贴士**：通过 `describe` 命令可以快速排查 Pod 异常问题，例如 `ImagePullBackOff` 错误通常表示镜像拉取失败。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，你可以看到 Pod 的基本信息（如镜像、端口）、容器状态以及事件（Events）等详细信息。
  **小贴士**：如果 Pod 状态异常，可以在“事件（Events）”选项卡中查看具体错误信息，帮助排查问题。

##### 3. 查看 Pod 日志

查看 Pod 中容器的日志是调试和监控的重要手段，可以帮助了解应用运行情况。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，查看特定 Pod 的日志（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl logs pod-stars-emmision -n your-pinyin-name
  ```
  输出结果会显示 Pod 中容器的运行日志。如果 Pod 中有多个容器，可以指定容器名称，例如：
  ```bash
  kubectl logs pod-stars-emmision -c stars-emmision -n your-pinyin-name
  ```
  **小贴士**：如果需要实时查看日志，可以添加 `--follow` 参数，例如 `kubectl logs --follow pod-stars-emmision -n your-pinyin-name`。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，找到“日志（Logs）”选项卡，选择容器名称（例如 `stars-emmision`）。
  5. 日志内容会显示在页面中，你可以滚动查看或刷新以获取最新日志。
  **小贴士**：Kuboard 界面支持实时日志查看，点击“刷新”按钮或勾选“自动刷新”选项即可。

##### 4. 进入 Pod 内部

有时需要进入 Pod 内部的容器进行调试或查看文件，可以通过命令行或 Kuboard 界面进入容器。

- **命令行操作（使用 `kubectl`）**：
  在终端中输入以下命令，进入特定 Pod 的容器内部（替换 `your-pinyin-name` 为你的 Namespace 名称）：
  ```bash
  kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash
  ```
  如果容器中没有 `/bin/bash`，可以尝试使用 `/bin/sh`：
  ```bash
  kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/sh
  ```
  进入容器后，你可以执行命令查看文件或环境变量等，输入 `exit` 退出容器。
  **小贴士**：如果 Pod 中有多个容器，需要指定容器名称，例如 `kubectl exec -it pod-stars-emmision -c stars-emmision -n your-pinyin-name -- /bin/bash`。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击其名称进入详情页面。
  4. 在详情页面中，找到“终端（Terminal）”选项卡，选择容器名称（例如 `stars-emmision`）。
  5. 终端窗口会打开，你可以在其中输入命令进行操作，操作完成后关闭窗口即可退出。
  **小贴士**：Kuboard 的终端功能类似 `kubectl exec`，但更直观，适合不熟悉命令行的同学使用。

##### 5. 创建 Pod

如果你需要重新创建或部署一个新的 Pod，可以通过 YAML 文件或 Kuboard 界面完成。

- **命令行操作（使用 `kubectl`）**：
  假设你已经准备好 Pod 的 YAML 文件（例如 `pod-stars-emmision.yml`），在终端中进入文件所在目录，执行以下命令创建 Pod：
  ```bash
  kubectl apply -f pod-stars-emmision.yml
  ```
  创建完成后，可以使用 `kubectl get pods` 命令查看 Pod 状态。
  **小贴士**：如果 YAML 文件有误，命令会报错，请仔细检查文件内容。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 点击页面右上角的“创建（Create）”或“添加（Add）”按钮。
  4. 在创建页面中，你可以选择上传 YAML 文件（直接上传 `pod-stars-emmision.yml`），或者通过表单填写 Pod 的基本信息（如名称、镜像、端口等）。
  5. 填写或上传完成后，点击“保存（Save）”或“创建（Create）”按钮。
  6. 创建完成后，回到 Pod 列表页面查看新创建的 Pod 状态。
  **小贴士**：Kuboard 界面支持表单和 YAML 两种方式创建 Pod，表单方式更适合初学者。

##### 6. 删除 Pod

当不再需要某个 Pod 时，可以将其删除。

- **命令行操作（使用 `kubectl`）**：
  有两种方式删除 Pod：
  - 如果有 YAML 文件，可以使用以下命令删除：
    ```bash
    kubectl delete -f pod-stars-emmision.yml
    ```
  - 或者直接指定 Pod 名称删除（替换 `your-pinyin-name` 为你的 Namespace 名称）：
    ```bash
    kubectl delete pod pod-stars-emmision -n your-pinyin-name
    ```
  删除后，可以使用 `kubectl get pods` 命令确认 Pod 是否已删除。
  **小贴士**：如果 Pod 由控制器（如 Deployment）管理，删除 Pod 后控制器可能会自动重建 Pod。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），勾选该 Pod 或点击右侧操作按钮。
  4. 选择“删除（Delete）”选项，确认删除操作。
  5. 删除完成后，刷新页面确认 Pod 已从列表中消失。
  **小贴士**：Kuboard 界面删除操作简单直观，但同样需要注意是否由控制器管理 Pod。

##### 7. 重启 Pod

Kubernetes 没有直接的重启 Pod 命令，但可以通过删除 Pod 让控制器（如 Deployment）自动重建，或者手动触发重启。

- **命令行操作（使用 `kubectl`）**：
  如果你的 Pod 直接创建（而非通过 Deployment 等控制器），可以通过删除 Pod 后重新创建来实现重启：
  ```bash
  kubectl delete pod pod-stars-emmision -n your-pinyin-name
  kubectl apply -f pod-stars-emmision.yml
  ```
  如果 Pod 由 Deployment 管理，可以通过以下命令触发滚动重启（后续课程会详细讲解 Deployment）：
  ```bash
  kubectl rollout restart deployment <deployment-name> -n your-pinyin-name
  ```
  **小贴士**：直接删除 Pod 是一种简单重启方式，但建议使用控制器管理 Pod 以实现自动化。

- **Kuboard 界面操作**：
  1. 在 Kuboard 界面中，选择你的 Namespace（例如 `your-pinyin-name`）。
  2. 点击左侧导航栏中的“工作负载（Workloads）”或“Pod”选项，进入 Pod 列表页面。
  3. 在列表中找到你的 Pod（例如 `pod-stars-emmision`），点击右侧操作按钮。
  4. 如果 Pod 由 Deployment 管理，可能有“重启（Restart）”或“滚动更新”选项；否则，可以选择“删除（Delete）”，然后重新创建 Pod。
  **小贴士**：Kuboard 界面的重启功能依赖于资源类型，如果是单独的 Pod，需要手动删除并重新创建。

##### 8. 健康检查（通过配置实现）

健康检查是确保 Pod 和容器正常运行的重要机制，Kubernetes 提供了 `livenessProbe`（活性探测）和 `readinessProbe`（就绪探测）两种方式。这部分已在第二部分的 YAML 示例中介绍过，同学们可以回顾 `pod-stars-emmision.yml` 文件中的配置：
- `livenessProbe`：检查容器是否存活，如果探测失败，Kubernetes 会重启容器。
- `readinessProbe`：检查容器是否准备好接收流量，如果探测失败，Kubernetes 不会将流量发送到该容器。

在后续课程中，我们会详细讲解如何配置和优化健康检查参数。当前可以先通过命令行或 Kuboard 查看 Pod 状态，确认健康检查是否生效。

- **命令行操作（使用 `kubectl`）**：
  使用 `describe` 命令查看 Pod 的健康检查状态：
  ```bash
  kubectl describe pod pod-stars-emmision -n your-pinyin-name
  ```
  在输出中的“Events”部分，可以看到健康检查的结果。

- **Kuboard 界面操作**：
  在 Pod 详情页面中，查看“事件（Events）”选项卡，了解健康检查的探测情况。

**小贴士**：健康检查配置需要根据应用特点调整，例如探测路径、频率和延迟时间等。

#### 总结与对比

通过本部分的学习，同学们应该已经掌握了以下内容：
- 使用 `kubectl` 命令行工具管理 Pod 的基本操作，包括查看列表、详情、日志，进入容器，创建、删除和重启 Pod。
- 使用 Kuboard 图形化界面完成相同的 Pod 管理操作，理解图形化工具与命令行的对应关系。
- 初步了解健康检查的概念及其在 Pod 配置中的作用。

**命令行与 Kuboard 界面对比**：
- **命令行（`kubectl`）**：操作灵活，适合自动化脚本和复杂任务，但需要记忆命令和参数，对初学者有一定学习曲线。
- **Kuboard 界面**：直观易用，适合初学者快速上手，降低了学习难度，但某些高级功能可能不如命令行灵活。

建议同学们在学习初期结合两种方式操作，先通过 Kuboard 界面熟悉资源管理流程，再逐步掌握 `kubectl` 命令，提升效率和深度理解。

**Pod 管理操作总结表格**：
以下表格总结了 Pod 管理的常用操作，方便同学们日后快速参考 `kubectl` 命令和 Kuboard 界面操作步骤。注意：以下命令中需将 `your-pinyin-name` 替换为你的 Namespace 名称，Pod 名称以 `pod-stars-emmision` 为例。

| **操作内容**         | **kubectl 命令行操作**                                                                 | **Kuboard 界面操作步骤**                                                                                     |
|----------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 查看 Pod 列表        | `kubectl get pods -n your-pinyin-name`                                               | 选择 Namespace → 点击“工作负载”或“Pod” → 查看列表                                                          |
| 查看 Pod 详情        | `kubectl describe pod pod-stars-emmision -n your-pinyin-name`                       | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 查看详情                                         |
| 查看 Pod 日志        | `kubectl logs pod-stars-emmision -n your-pinyin-name`                               | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 选择“日志”选项卡                                 |
| 进入 Pod 内部        | `kubectl exec -it pod-stars-emmision -n your-pinyin-name -- /bin/bash`              | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 选择“终端”选项卡                                 |
| 创建 Pod             | `kubectl apply -f pod-stars-emmision.yml`                                           | 选择 Namespace → 点击“工作负载”或“Pod” → 点击“创建” → 上传 YAML 或填写表单 → 保存                        |
| 删除 Pod             | `kubectl delete -f pod-stars-emmision.yml` 或<br>`kubectl delete pod pod-stars-emmision -n your-pinyin-name` | 选择 Namespace → 点击“工作负载”或“Pod” → 勾选 Pod → 点击“删除” → 确认                                    |
| 重启 Pod（单独 Pod） | `kubectl delete pod pod-stars-emmision -n your-pinyin-name` 后重新 `apply`          | 选择 Namespace → 点击“工作负载”或“Pod” → 勾选 Pod → 点击“删除” → 重新创建                                |
| 重启 Pod（Deployment）| `kubectl rollout restart deployment <deployment-name> -n your-pinyin-name`          | 选择 Namespace → 点击“工作负载”或“Deployment” → 选择 Deployment → 点击“重启”或“滚动更新”                 |
| 查看健康检查状态     | `kubectl describe pod pod-stars-emmision -n your-pinyin-name` （查看 Events）       | 选择 Namespace → 点击“工作负载”或“Pod” → 点击 Pod 名称 → 查看“事件（Events）”选项卡                      |

**小贴士**：将此表格保存到笔记中，或打印出来作为快速参考手册，在日常操作中可以根据需求选择命令行或界面方式。

#### 课后练习

1. 使用 `kubectl` 命令查看你创建的 Pod 的日志和详细信息，记录关键信息（如状态、事件）。
2. 使用 Kuboard 界面进入你创建的 Pod 内部，尝试查看容器中的文件或环境变量。
3. 尝试删除你的 Pod，然后通过命令行或 Kuboard 界面重新创建，观察状态变化。
4. 复习健康检查的配置，思考如何调整 `livenessProbe` 和 `readinessProbe` 参数以适应不同的应用场景。

---

以上是更新后的第三部分内容，添加了“Pod 管理操作总结表格”，方便同学们日后快速查阅和使用。如果还有其他需要补充或调整的地方，请随时告诉我！