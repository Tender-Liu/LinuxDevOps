笔试题目

注意：未注明"写下命令"或"口头回答"的题目, 请您上机操作
     注明"写下命令"的题目, 请写下您的答案
     注明"口头回答"的题目, 口头作答即可

一、git部分

1. 用您的姓名缩写新建一个分支,并切换到该分支上

2. 在README.md中追加您的名字缩写，将当前分支合并到master分支，并推送远端
                  
3. 在master分支上，之前有一次commit误删了文件（描述为：Deleted error.log），想撤销这次操作找回文件，请问如何操作？
          
4. 请介绍您在DevOps实践中如下情况是如何设计或操作？
        a. 您的项目中git工作流是如何设计?分支策略如何设计？每个分支的作用是什么？软件的版本是如何规划的？
        b. 打算开发新功能时，会怎么做？
        c. 打算进行CI时，会怎么做？
        d. CI出错后，是否有提醒？如何补救？
        e. 您用哪个分支上的代码部署生产环境？为什么？
        f. 您是否使用预发布环境？如何使用？如果预发布环境中发现程序有bug，会如何做？
        g. 如果需要支持多环境部署，基于您现有的DevOps方式，该如何实现或需要做哪些改变？

        口头回答:


二、linux部分

1. 请使用top命令找到当前占用内存最多的进程

2. 请查询哪个进程占用了2222端口

3. 请用vi/vim打开time.txt, 将文件中的内容复制50遍并显示行数，然后将其中的time和Time全部替换为TIME

4. 请为linux/aaa.sh在output文件夹下建立名为bbb.sh的软连接

5. 请查询linux/doc目录下(包括子目录)共有多少个后缀名为md的文件

6. 请将linux/doc目录下按目录占用的空间大小倒序排列显示前十条记录

7. 请采用awk显示linux/doc目录下首层的目录，但不显示文件

8. 用EOF，向output/shutdown.service下写入如下内容：
        [Unit]
        Description=shutdown linux service

        [Service]
        Type=oneshot
        ExecStart=/usr/sbin/shutdown -h 20:00

        [Install]
        WantedBy=multi-user.target

9. 在output目录下创建一个名为print.sh，要求传入2个参数，在屏幕上显示（参数1内容：参数2内容），并将结果写入output/print.log

10. 请写出用journalctl命令查看nginx.service今天以来,错误级别在warning以上的日志
        写下命令：
11. 请找出用8.8.8.8域名解析服务器解析www.gitlab.com对应的IP
       
12. 请用curl找到https://www.gitlab.com最终展示的页面前经过的跳转过程

13. 请观察/home/workspace/test目录下的git项目，该项目无法执行git pull命令拉取代码，请尝试用strace命令排查问题。

三、gitlab CI/CD部分


1. 观察gitlab-runner/gitlab-ci.yml文件，请增加一个pre-deploy的stage, 并改变stage执行顺序为(test -> build -> pre-deploy -> deploy)

2. 因为在实际工作中，通常每次触发pipline时,要下载和编译依赖包,如果每次都这样操作会浪费很多时间,请问增加什么配置能改善这种情况?为什么？
        口头回答:

3. 观察gitlab-runner/gitlab-ci2.yml文件，请问.gem和.yarn这两个标签下的代码分别实现了什么功能？区别是什么？
        口头回答:

四、docker部分


1. 请运行一个docker容器,要求：
        a. 以守护进程方式启动nginx镜像
        b. 将宿主机的docker/content目录挂载到/usr/share/nginx/html目录
        c. 将容器的80端口暴露到宿主机的8080端口
        d. 设置环境变量NGINX_PORT=80

        写下命令： 

2. 请编写一个Dockfile，要求：
        a. 以ubuntu:16.04为基础镜像
        b. 安装一个vim(具体命令为：apt update && apt -y upgrade && apt install -y vim )
        c. 暴露一个12345端口
        d. 保证docker启动后不瞬间退出

        请写出：
            Dockfile:

            docker启动命令:


3. 有一个nginx的docker镜像要使用宿主机的网络,请问应当如何运行?
    
        写下命令：


五、k8s部分


1. 查看一个集群下的所有node
        写下命令：

2. 在web namespace下查看一个名为nginx-0的pod的详细信息，然后打印该pod的日志
        写下命令：

3. 将nginx-deployment.yaml文件部署到集群中
        写下命令：

4. 请观察k8s/demo1.yaml的内容，回答以下问题：
        a. 该配置会部署什么类型的实例？
        口头回答：
        b. 该配置会部署在哪台机器上？
        口头回答：
        c. 该配置会暴露什么类型的端口？
        口头回答：

5. 请观察k8s/demo2.yaml的内容，回答以下问题：
        a. 该配置会部署什么类型的实例？
        口头回答：
        b. 该配置会部署在哪台机器上？
        口头回答：
        c. 该配置会暴露什么类型的端口？
        口头回答：

6. 请简述Deployment，Service，Pod的关系？
    口头回答：
7. 请描述当k8s集群中部署出现下列状态时，您排查问题的思路。
    a. pod mysql 一直处于Pending状态。
        口头回答：
        b. pod nginx 出现CrashLoopBackOff状态。
    口头回答：

六、ansible部分


1. 请描述一下ansible文件夹下demo.yaml中playbook中notify的功能是什么？什么时候执行？
        口头回答：

2. 请指出该playbook作用在哪些主机上？
        口头回答：

3. 请将执行的并发数改为10

4. 请用命令查询apt_key模块validate_certs参数的含义和用法


七、Terraform部分


1. 请观察terraform/demo.tf文件，
    a. 请问该文件的功能是什么？
        口头回答：

    b. 什么情况下要用data关键字声明资源？
        口头回答：

2.      请问如何查询资源类型为alicloud_instance, 资源名称为default的资源配置信息
        写下命令：

八、工单实例部分

1. 请观察工单,并回答问题:

        a. 工单描述：
        
        Gitlab运行CI/CD时需要安装并注册gitlab-runner组件，客户在Windows平台下注册gitlab-runner时遇到以下错误：

        + .\gitlab-runner.exe register
        + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            + CategoryInfo          : NotSpecified: (Exception 0xc0000005 0x8 0x0       0x0:String) [], RemoteException
            + FullyQualifiedErrorId : NativeCommandError


        b. 辅助信息：

        gitlab-runner的问题通常在它的Issue列表中可以找到，地址是：https://gitlab.com/gitlab-org/gitlab-runner/-/issues

   请根据以上信息，请您协助客户找到该问题的原因并解决。
        口头回答:
