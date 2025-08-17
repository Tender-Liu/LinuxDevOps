### 最终 6 天 Kubernetes 学习计划大纲
以下大纲涵盖了 Kubernetes 的核心概念，实验部分由您自行准备。

#### 第 1 天：Pod 与配置管理（ConfigMap 和 Secret）
- **目标**：掌握 Pod 基本操作以及配置管理的基础知识，为部署案例做准备。
- **内容**：
  - Pod 的创建、生命周期、资源限制、健康检查。
  - ConfigMap：管理非敏感配置数据，供 Pod 使用。
  - Secret：管理敏感数据（如密码、密钥），确保安全。
- **互动讨论**：Pod 资源限制如何影响调度？ConfigMap 和 Secret 在部署中如何提高配置灵活性？

#### 第 2 天：工作负载控制器（Deployment）与服务（Service）
- **目标**：掌握 Deployment 的使用，理解无状态应用的部署方式，并学习 Service 为应用提供网络访问。
- **内容**：
  - Deployment：滚动更新和副本管理，适用于无状态应用。
  - Service 类型（ClusterIP、NodePort、LoadBalancer）及其应用场景。
- **互动讨论**：Deployment 在无状态应用管理中的优势是什么？Service 如何帮助 Pod 实现负载均衡和外部访问？

#### 第 3 天：存储与工作负载控制器（StatefulSet、PV、PVC）
- **目标**：掌握存储管理方法和 StatefulSet 的使用，理解有状态应用的部署方式。
- **内容**：
  - Volume：Pod 中的临时存储。
  - PersistentVolume（PV）和 PersistentVolumeClaim（PVC）：持久化存储资源管理。
  - StorageClass：动态存储分配。
  - StatefulSet：管理有状态应用，适用于数据库等需要稳定身份和持久化存储的应用。
- **互动讨论**：StatefulSet 和 Deployment 的主要区别是什么？PV 和 PVC 如何配合 StatefulSet 实现数据持久化？

#### 第 4 天：网络与 Ingress-Nginx 及工作负载控制器（DaemonSet）
- **目标**：理解 Ingress 的使用，掌握高级网络通信机制，并学习 DaemonSet 的应用场景。
- **内容**：
  - Ingress 资源配置外部访问和域名路由。
  - Ingress-Nginx：作为常用的 Ingress Controller，处理 HTTP/HTTPS 流量，支持高级路由规则、SSL 终止等功能。
  - DaemonSet：确保每个节点运行一个 Pod 副本，适用于日志收集、监控代理等场景。
- **互动讨论**：Service 和 Ingress 的区别是什么？Ingress-Nginx 在流量管理中有哪些优势？DaemonSet 的典型应用场景有哪些？

#### 第 5 天：调度策略与工作负载控制器对比（Deployment、StatefulSet，DaemonSet）
- **目标**：学习 Kubernetes 调度策略，并通过对比复习三大工作负载控制器（Deployment、StatefulSet、DaemonSet）。
- **内容**：
  - 标签（Labels）：为资源添加元数据，用于筛选和组织。
  - 亲和力（Affinity）：Pod 亲和性与反亲和性，控制 Pod 调度。
  - 污点（Taints）与容忍（Tolerations）：限制节点调度 Pod。
  - 对比复习 Deployment、StatefulSet、DaemonSet 的特点和应用场景。
- **互动讨论**：三大工作负载控制器的适用场景有何不同？亲和力和污点如何配合优化调度？

#### 第 6 天：权限管理、与故障排查及综合复习
- **目标**：学习权限控制和 HPA 配置，掌握故障排查技巧，复习核心内容。
- **内容**：
  - RBAC 权限管理，创建角色和绑定。
  - 查看 Pod 日志、事件（Events），排查问题。合理使用kuboard查看日志、事件、指标等
  - 复习 Pod, ConfigMap、Secret、Deployment、StatefulSet、DaemonSet、service、Ingress-Nginx、调度策略等核心概念。面试题各类详情
- **互动讨论**：如何通过日志和事件快速定位问题？

### 说明
- **内容覆盖**：大纲涵盖了 Kubernetes 的核心资源和工作负载控制器（Deployment、StatefulSet、DaemonSet）、网络管理（Service、Ingress-Nginx）、调度策略（标签、亲和力、污点）、自动扩展（HPA）以及配置管理（ConfigMap、Secret）等关键内容。
- **时间安排**：课程内容分布均衡，逐步递进，从基础到高级，从单个资源到综合应用，确保学习逻辑清晰。
- **实验自主性**：实验部分由您自行准备，如果在教学或实验过程中需要具体的命令、YAML 示例或其他支持，随时可以告诉我，我会提供帮助。
