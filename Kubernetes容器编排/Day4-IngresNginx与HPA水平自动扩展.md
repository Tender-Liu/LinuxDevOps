# IngresNginx 与 HPA(水平自动扩展)

## 学习目标
1. 理解 Ingress 和 Ingress-Nginx 的核心概念与作用，掌握其作为 Kubernetes 高级流量管理资源的功能，区分 Ingress 与 Service 的使用场景，并了解 Ingress-Nginx 支持域名路由、路径匹配和 SSL 终止等特性。
2. 掌握 Ingress-Nginx 的基本配置与应用，能够编写简单的 Ingress 资源配置文件，为应用配置基于域名的访问入口，并通过 kubectl 或 Kuboard 验证配置效果，确保外部流量正确路由到目标服务。
3. 理解水平自动扩展（HPA）的原理与价值，能够描述 HPA 基于资源指标（如 CPU、内存）或自定义指标动态调整 Pod 副本数的工作机制，并解释其在流量高峰场景下的作用及与 Deployment 静态副本管理的区别。
4. 掌握 HPA 的基本配置与验证，能够为 Deployment 配置 HPA 资源，设置基于 CPU 利用率的扩展规则，并通过 kubectl 或 Kuboard 观察 Pod 副本数量变化，验证自动扩展效果。
5. 具备综合应用能力，能够在 Kubernetes 集群中结合 Ingress-Nginx 和 HPA 部署一个简单的无状态应用（如 Web 服务器），实现外部访问与动态扩展，并分析流量管理与资源扩展如何提升应用的高可用性。