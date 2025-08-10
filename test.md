# 第 2 天：工作负载控制器（Deployment）与服务（Service）

## 目标
- 深入理解 Deployment 的使用，掌握无状态应用的部署方式。
- 学习 Service 为应用提供网络访问的原理和配置方法。

## 内容规划

### 1. Deployment 详解
- **Deployment 的概念**
  - 定义：Deployment 是 Kubernetes 中用于管理无状态应用的控制器，能够自动管理 Pod 的副本，支持滚动更新和回滚。
  - 工作原理：通过声明式配置，Kubernetes 会自动确保 Pod 的期望状态与实际状态一致。

- **Pod 与 Deployment 的区别**
  - **Pod**：
    - 最小的调度单位，直接运行应用。
    - 不支持自我修复和副本管理，需手动处理 Pod 的创建、更新和删除。
  - **Deployment**：
    - 控制器，管理多个 Pod 的生命周期。
    - 支持滚动更新、回滚和副本管理，确保高可用性。
    - 通过声明式配置简化应用的管理。

- **Deployment 的 YAML 语法**
  - 介绍 Deployment 的基本结构和常见字段：
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - name: my-container
            image: my-image:latest
            ports:
            - containerPort: 80
    ```

- **Deployment 的优势**
  - 自动管理 Pod 的副本，确保高可用性。
  - 支持滚动更新，减少停机时间。
  - 简化应用的版本管理和回滚操作。

### 2. Service 详解
- **Service 的概念**
  - 定义：Service 是一种抽象，定义了一组 Pod 的访问策略，解决了 Pod 动态 IP 的问题，提供稳定的网络访问入口。

- **Service 类型**
  - **ClusterIP**：默认类型，提供集群内部访问。
  - **NodePort**：在每个节点上开放一个端口，外部可访问。
  - **LoadBalancer**：为 Service 提供外部负载均衡器，适合生产环境。

- **Service 的 YAML 语法**
  - 介绍 Service 的基本结构和常见字段：
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: my-app-service
      namespace: default
    spec:
      type: ClusterIP
      selector:
        app: my-app
      ports:
      - port: 80
        targetPort: 80
    ```

- **Service 的作用**
  - 提供稳定的访问入口，解决 Pod 动态 IP 的问题。
  - 支持流量负载均衡，确保应用的高可用性。

### 3. 互动讨论
- **Deployment 的优势是什么？**
  - 通过自动化管理 Pod，简化运维工作。
  - 滚动更新保证了应用的持续可用性。

- **Service 如何帮助 Pod 实现负载均衡和外部访问？**
  - 提供统一的访问入口，支持多种负载均衡策略。

### 4. 实践练习
- **创建 Deployment 和 Service**
  - 学员将根据提供的 YAML 模板，创建一个简单的无状态应用，并通过 Service 进行访问。

## 总结
通过本节内容，学员将深入理解 Deployment 和 Service 的概念、作用及其配置方法，掌握如何在 Kubernetes 中管理无状态应用，并为后续的应用部署打下坚实基础。