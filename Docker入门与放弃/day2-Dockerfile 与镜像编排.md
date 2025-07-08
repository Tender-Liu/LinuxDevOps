镜像编排理论讲解
什么是镜像编排？为什么需要 Dockerfile？
Docker 镜像构建过程与分层原理。
面试常见问题：Dockerfile 的构建过程是怎样的？如何优化镜像大小？
Dockerfile 详解
核心指令：FROM、RUN、CMD、ENTRYPOINT、COPY、ADD、WORKDIR、EXPOSE、ENV 等。
语法案例 1：构建一个简单的 Ubuntu + Vim 镜像。
语法案例 2：构建一个 Nginx 镜像，添加自定义网页。
语法案例 3：构建一个多阶段构建镜像（如 Node.js 应用）。
项目实践：Dockerfile 编写
Python 项目：构建 Flask 应用镜像。
Java 项目：构建 Spring Boot 应用镜像。
Node.js 项目：构建 Express 应用镜像。
前端页面：构建 React/Vue 应用镜像。
Go 项目：构建 Go Web 应用镜像，使用多阶段构建优化镜像大小。
镜像优化与最佳实践
减少镜像层级，清理缓存文件。
使用多阶段构建（Multi-stage Build）。
案例：优化一个 Python 应用镜像，减少大小。
总结与小测验
总结：Dockerfile 的核心指令与镜像构建优化。
小测验：编写一个简单的 Dockerfile，回答构建失败的可能原因。
思考题（面试准备）
什么是多阶段构建？如何减少镜像体积？
CMD 和 ENTRYPOINT 的区别是什么？