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
