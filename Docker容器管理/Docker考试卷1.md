# Docker综合考试卷

## 一、选择题(每题1分,共30分)

### 理论知识部分(1-15题):

1. 关于Docker和虚拟机的区别,下列说法正确的是:
    * A. Docker比虚拟机占用更多系统资源
    * B. Docker启动速度比虚拟机慢
    * C. Docker共享主机内核,而虚拟机需要独立的操作系统
    * D. Docker的隔离性比虚拟机更强

2. 一个电商公司想部署微服务架构,选择Docker的主要原因是:
    * A. Docker可以完全取代数据库
    * B. Docker能实现环境一致性和快速部署
    * C. Docker只能运行在Linux系统上
    * D. Docker适合存储大量数据

3. 关于Docker镜像层,以下说法正确的是:
    * A. 每个镜像只有一层
    * B. 镜像层是可读可写的
    * C. 基础镜像位于最上层
    * D. 镜像层采用分层存储,共享相同的层

4. Docker容器在企业生产环境中的最佳实践是:
    * A. 在容器内运行多个应用
    * B. 一个容器运行一个主进程
    * C. 使用root用户运行所有容器
    * D. 存储数据到容器内部

5. 在构建Docker镜像时,哪种做法可以有效减小镜像体积:
    * A. 使用最新版本的基础镜像
    * B. 将所有命令合并为一层
    * C. 使用多阶段构建
    * D. 把所有依赖都打包进去

6. 关于Docker网络模式,以下哪种最适合多容器通信:
    * A. host模式
    * B. none模式
    * C. 用户自定义桥接网络
    * D. 默认桥接网络

7. Docker数据持久化最推荐的方式是:
    * A. 将数据直接存储在容器里
    * B. 使用Docker Volume
    * C. 使用bind mount
    * D. 不进行持久化存储

8. 企业中使用私有镜像仓库的主要原因是:
    * A. 提高镜像下载速度
    * B. 确保镜像安全性
    * C. 节省存储空间
    * D. 减少构建时间

9. Docker容器在运行Web应用时,最佳的端口映射方式是:
    * A. 使用host网络模式
    * B. 映射到随机端口
    * C. 指定固定端口映射
    * D. 不进行端口映射

10. 关于Docker Compose,以下说法正确的是:
    * A. 只能用于单机部署
    * B. 替代了Dockerfile的功能
    * C. 用于定义和运行多容器应用
    * D. 主要用于镜像构建

11. Docker镜像的最佳存储策略是:
    * A. 总是使用latest标签
    * B. 使用具体的版本标签
    * C. 不使用标签
    * D. 随机生成标签

12. 容器编排时,关于服务发现正确的是:
    * A. 手动配置IP地址
    * B. 使用容器名称通信
    * C. 使用服务发现机制
    * D. 直接使用localhost

13. 企业使用Docker的安全策略应该包括:
    * A. 只使用官方镜像
    * B. 定期更新基础镜像
    * C. 扫描镜像漏洞
    * D. 以上都是

14. Docker容器日志管理最佳实践是:
    * A. 禁用所有日志
    * B. 使用日志驱动收集
    * C. 存储在容器内部
    * D. 只在测试环境记录

15. 关于容器资源限制,正确的做法是:
    * A. 不限制资源使用
    * B. 只限制内存使用
    * C. 根据应用需求合理限制
    * D. 统一限制所有容器

### 命令操作部分(16-30题):

16. 查看当前运行的容器命令是:
    * A. docker ps
    * B. docker container ls
    * C. docker images
    * D. A和B都对

17. 删除所有未使用的镜像,正确的命令是:
    * A. docker rmi $(docker images)
    * B. docker image prune -a
    * C. docker rm -f
    * D. docker delete images

18. 进入正在运行容器的命令是:
    * A. docker attach
    * B. docker exec -it
    * C. docker run -it
    * D. docker start -i

19. 查看容器日志的命令是:
    * A. docker log
    * B. docker logs
    * C. docker inspect
    * D. docker info

20. 停止所有运行容器的命令是:
    * A. docker stop all
    * B. docker stop $(docker ps -q)
    * C. docker kill all
    * D. docker rm all

21. 构建Docker镜像的命令是:
    * A. docker create
    * B. docker build
    * C. docker commit
    * D. docker make

22. 将容器保存为新镜像的命令是:
    * A. docker save
    * B. docker export
    * C. docker commit
    * D. docker cp

23. 查看镜像构建历史的命令是:
    * A. docker info
    * B. docker logs
    * C. docker history
    * D. docker inspect

24. 从容器拷贝文件到主机的命令是:
    * A. docker cp
    * B. docker copy
    * C. docker export
    * D. docker save

25. 查看容器资源使用情况的命令是:
    * A. docker ps
    * B. docker top
    * C. docker stats
    * D. docker info

26. 创建Docker网络的命令是:
    * A. docker network add
    * B. docker network create
    * C. docker network new
    * D. docker network make

27. 查看容器详细信息的命令是:
    * A. docker info
    * B. docker inspect
    * C. docker show
    * D. docker view

28. 给正在运行的容器添加数据卷的命令是:
    * A. docker volume add
    * B. docker update --volume
    * C. docker modify
    * D. 无法添加,必须重建容器

29. 查看Docker系统信息的命令是:
    * A. docker version
    * B. docker info
    * C. docker system
    * D. docker about

30. 清理Docker系统的命令是:
    * A. docker clean
    * B. docker system prune
    * C. docker remove
    * D. docker clear

## 二、判断题(每题2分,共20分)
1. Docker容器在停止后会自动删除容器数据 ( )
2. Docker镜像可以同时拥有多个标签 ( )
3. 容器内的进程可以直接访问宿主机的文件系统 ( )
4. Docker镜像是分层存储的 ( )
5. 使用volume方式挂载的数据会随容器删除而删除 ( )
6. Docker容器默认会限制资源使用 ( )
7. 一个容器可以加入多个用户自定义网络 ( )
8. Dockerfile中的CMD指令在容器运行时可以被覆盖 ( )
9. Docker Hub上的官方镜像都是安全的 ( )
10. 容器重启后IP地址会改变 ( )

## 三、解答题(每题3分,共15分)
1. 简述Docker容器和虚拟机的区别,并说明各自的应用场景。

2. 解释什么是Docker的数据持久化?有哪些方式?各有什么特点?

3. 描述Docker的网络模式有哪些?分别适用于什么场景?

4. 如何优化Docker镜像大小?请列举几种方法。

5. 简述Docker的常见安全问题及解决方案。

## 机试题，构建发布Vue 静态页面
