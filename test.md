我们开始写第三部分：kubeconfig 文件管理多个集群或多个集群
1. windwos：本地C:\Users\用户\.kube\config linux：家目录 ~/.kube/config
如何配置多个账户在一个



好的，我明白您的需求。以下是关于如何在 Kuboard 界面中查看 RBAC 相关内容（例如 ServiceAccount、ClusterRole、ClusterRoleBinding、Secret 等）的补充说明。Kuboard 是一个基于 Web 的 Kubernetes 管理界面，提供直观的方式来查看和管理集群资源。以下内容将帮助您在 Kuboard 中查看作业二中创建的普通运维人员账号及其相关权限配置。

---

#### 8. 在 Kuboard 界面中查看 RBAC 相关内容
Kuboard 提供了一个用户友好的图形化界面，允许您浏览和管理 Kubernetes 集群中的资源。以下是在 Kuboard 中查看作业二中创建的资源（如 ServiceAccount、ClusterRole、ClusterRoleBinding、Secret 等）的具体步骤。假设您已经安装并登录了 Kuboard，并且有权限访问集群。

##### 8.1 登录 Kuboard 并选择集群
1. 打开浏览器，访问 Kuboard 的 Web 界面（通常是您部署 Kuboard 的 IP 地址和端口，例如 `http://<IP>:32567`）。
2. 使用您的凭据登录 Kuboard。
3. 在顶部导航栏或集群列表中，选择您正在操作的 Kubernetes 集群（即通过 `Kubeadm` 部署的集群）。

**解释**：  
- Kuboard 支持管理多个 Kubernetes 集群，登录后需要选择正确的集群以查看相应的资源。

##### 8.2 查看 ServiceAccount
要查看在 `kube-system` 命名空间中创建的 `ops-user` 服务账户：
1. 在左侧导航栏中，点击 **命名空间**（Namespaces）。
2. 在命名空间列表中，找到并点击 `kube-system` 命名空间。
3. 在 `kube-system` 命名空间的页面中，点击顶部菜单的 **服务账户**（Service Accounts）选项卡。
4. 在服务账户列表中，找到 `ops-user`，点击其名称可以查看详细信息。

**预期结果**：  
- 您将看到 `ops-user` 服务账户的基本信息，例如创建时间、命名空间等。
- 如果有关联的 Secret（例如 Token），可能会在详细信息中显示相关链接。

**解释**：  
- Kuboard 的界面允许您直观地浏览服务账户列表及其关联资源。

##### 8.3 查看 ClusterRole
要查看创建的 `ops-read-write-no-delete` 集群角色：
1. 在左侧导航栏中，点击 **集群角色**（Cluster Roles）。
2. 在集群角色列表中，使用搜索框输入 `ops-read-write-no-delete` 以快速定位。
3. 点击 `ops-read-write-no-delete` 的名称，查看其详细信息，包括权限规则（`rules`）。

**预期结果**：  
- 详细信息页面会展示该 `ClusterRole` 的权限配置，例如允许的操作（`verbs`）包括 `get`、`list`、`create` 等，但不包括 `delete`。
- 您可以看到该角色适用于所有 API 组和资源类型（`apiGroups` 和 `resources` 为 `*`）。

**解释**：  
- Kuboard 将 `ClusterRole` 作为全局资源单独列出，方便查看和管理集群级别的角色。

##### 8.4 查看 ClusterRoleBinding
要查看创建的 `ops-read-write-no-delete-binding` 集群角色绑定：
1. 在左侧导航栏中，点击 **集群角色绑定**（Cluster Role Bindings）。
2. 在集群角色绑定列表中，使用搜索框输入 `ops-read-write-no-delete-binding` 以快速定位。
3. 点击 `ops-read-write-no-delete-binding` 的名称，查看其详细信息，包括绑定的主体（`subjects`）和角色引用（`roleRef`）。

**预期结果**：  
- 详细信息页面会展示该绑定将 `ops-read-write-no-delete` 角色关联到 `ops-user` 服务账户（位于 `kube-system` 命名空间）。
- 您可以确认权限是集群级别的，适用于所有命名空间。

**解释**：  
- `ClusterRoleBinding` 在 Kuboard 中作为全局资源列出，用于查看角色与主体之间的绑定关系。

##### 8.5 查看 Secret
要查看在 `kube-system` 命名空间中创建的 `ops-user-token` Secret（如果手动创建）：
1. 在左侧导航栏中，点击 **命名空间**（Namespaces）。
2. 在命名空间列表中，找到并点击 `kube-system` 命名空间。
3. 在 `kube-system` 命名空间的页面中，点击顶部菜单的 **密钥**（Secrets）选项卡。
4. 在密钥列表中，找到 `ops-user-token`，点击其名称可以查看详细信息。

**预期结果**：  
- 您将看到 `ops-user-token` 的基本信息，例如类型（`kubernetes.io/service-account-token`）和关联的服务账户（通过注解）。
- **注意**：Kuboard 不会直接显示 Secret 的明文内容（如 Token），这是出于安全考虑。如果需要使用 Token，可能需要通过其他方式提取。

**解释**：  
- Secret 在 Kuboard 中按命名空间组织，方便查看与特定服务账户关联的密钥。

##### 8.6 测试权限（可选）
虽然 Kuboard 本身不直接支持模拟服务账户权限进行测试，但您可以通过查看资源的方式间接确认权限范围：
1. 在 Kuboard 中，浏览不同的命名空间（例如 `default` 或 `shiqi`）。
2. 确认您可以看到资源列表（例如 Pods、Deployments 等），这表明 `ops-user` 的查看权限已生效。
3. 注意 Kuboard 界面中是否提供删除按钮或操作选项（取决于 Kuboard 版本和权限配置），但由于权限限制，实际删除操作无法执行。

**解释**：  
- 如果您希望在 Kuboard 中以 `ops-user` 身份登录并测试权限，需要为该服务账户生成 Token，并配置 Kuboard 的访问凭据（这通常涉及更复杂的设置，超出本文范围）。
- 更简单的测试方式是使用 `kubectl` 命令行工具模拟权限（如作业二第 6 步所述）。

##### 8.7 查看集群整体状态
Kuboard 还提供集群整体状态的概览，帮助您确认环境是否正常：
1. 在左侧导航栏中，点击 **概览**（Overview）或 **节点**（Nodes）。
2. 查看集群节点的状态、资源使用情况等，确保集群运行正常。

**解释**：  
- 集群状态概览有助于确认 RBAC 配置是否影响了集群的整体运行。
- Kuboard 的图形化界面使查看节点和资源状态变得直观。

##### 8.8 注意事项
- **权限限制**：如果您在 Kuboard 中以管理员身份登录，您将看到所有资源和操作选项。但如果以 `ops-user` 身份登录（需要额外配置），界面可能会根据权限限制某些操作（例如隐藏删除按钮）。
- **版本差异**：Kuboard 的界面和功能可能因版本不同而有所差异，上述步骤基于常见版本（如 Kuboard v3）。如果界面不同，请参考您使用的版本的官方文档。
- **日志和事件**：如果遇到权限相关问题，可以在 Kuboard 中查看资源的 **事件**（Events）或日志，以帮助排查问题。
