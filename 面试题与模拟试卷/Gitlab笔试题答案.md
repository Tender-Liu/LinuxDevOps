好的，以下是您提供的笔试题目中所有需要“写下命令”或“请写出”部分的详细答案。对于未注明“写下命令”或“口头回答”的题目，我会提供操作指导。对于“口头回答”的部分，我会标注清楚，以便您准备口头表述。

---

# 笔试题目答案

## 注意事项
- 未注明"写下命令"或"口头回答"的题目，请上机操作。
- 注明"写下命令"的题目，以下提供书面答案。
- 注明"口头回答"的题目，标注为口头作答准备。

---

## 一、Git 部分
1. **用您的姓名缩写新建一个分支，并切换到该分支上**  
   操作：  
   ````bash
   git checkout -b <您的姓名缩写>
   ````

2. **在 README.md 中追加您的名字缩写，将当前分支合并到 master 分支，并推送远端**  
   操作：  
   - 编辑 README.md 文件，追加您的名字缩写并保存。  
   - 提交更改：  
     ````bash
     git add README.md
     git commit -m "Add <您的姓名缩写> to README.md"
     ````
   - 切换到 master 分支并合并：  
     ````bash
     git checkout master
     git merge <您的姓名缩写>
     ````
   - 推送远端：  
     ````bash
     git push origin master
     ````

3. **在 master 分支上，之前有一次 commit 误删了文件（描述为：Deleted error.log），想撤销这次操作找回文件，请问如何操作？**  
   操作：  
   - 找到误删文件的 commit ID：  
     ````bash
     git log --oneline
     ````
   - 撤销该 commit，但保留更改：  
     ````bash
     git revert <commit-id>
     ````
   - 或者直接回退到上一个 commit：  
     ````bash
     git checkout <commit-id>^ -- error.log
     git commit -m "Restore error.log"
     ````

4. **请介绍您在 DevOps 实践中如下情况是如何设计或操作？**  
   **口头回答**：请准备以下内容的口头表述，涵盖 git 工作流设计、分支策略、新功能开发、CI/CD 流程、环境部署等。

---

## 二、Linux 部分
1. **请使用 top 命令找到当前占用内存最多的进程**  
   操作：  
   ````bash
   top
   ````
   说明：运行后按 `Shift + P` 按 CPU 排序，或观察 `RES` 列查看内存占用，按 `q` 退出。

2. **请查询哪个进程占用了 2222 端口**  
   操作：  
   ````bash
   netstat -tuln | grep 2222
   ````
   或  
   ````bash
   lsof -i :2222
   ````

3. **请用 vi/vim 打开 time.txt，将文件中的内容复制 50 遍并显示行数，然后将其中的 time 和 Time 全部替换为 TIME**  
   操作：  
   - 打开文件：  
     ````bash
     vim time.txt
     ````
   - 复制内容 50 遍（在 vim 中）：  
     输入命令模式下：  
     ``:1,$yank`` （复制所有内容）  
     然后输入：  
     ``:1,$put`` （粘贴一次）  
     重复粘贴操作 49 次（可以用宏或循环，简单方法是多次 `:put`）。  
   - 显示行数：  
     ``:set number`` 或退出 vim 后运行：  
     ````bash
     wc -l time.txt
     ````
   - 替换 time 和 Time 为 TIME：  
     在 vim 命令模式下：  
     ``:%s/\(time\|Time\)/TIME/g``

4. **请为 linux/aaa.sh 在 output 文件夹下建立名为 bbb.sh 的软连接**  
   操作：  
   ````bash
   ln -s ../linux/aaa.sh output/bbb.sh
   ````

5. **请查询 linux/doc 目录下（包括子目录）共有多少个后缀名为 md 的文件**  
   操作：  
   ````bash
   find linux/doc -type f -name "*.md" | wc -l
   ````

6. **请将 linux/doc 目录下按目录占用的空间大小倒序排列显示前十条记录**  
   操作：  
   ````bash
   du -h linux/doc | sort -rh | head -n 10
   ````

7. **请采用 awk 显示 linux/doc 目录下首层的目录，但不显示文件**  
   操作：  
   ````bash
   ls -l linux/doc | awk '$1 ~ /^d/ {print $9}'
   ````

8. **用 EOF，向 output/shutdown.service 下写入如下内容**  
   操作：  
   ````bash
   cat << EOF > output/shutdown.service
   [Unit]
   Description=shutdown linux service

   [Service]
   Type=oneshot
   ExecStart=/usr/sbin/shutdown -h 20:00

   [Install]
   WantedBy=multi-user.target
   EOF
   ````

9. **在 output 目录下创建一个名为 print.sh，要求传入 2 个参数，在屏幕上显示（参数 1 内容：参数 2 内容），并将结果写入 output/print.log**  
   操作：  
   ````bash
   cat << EOF > output/print.sh
   #!/bin/bash
   echo "\$1内容：\$2内容"
   echo "\$1内容：\$2内容" >> output/print.log
   EOF
   chmod +x output/print.sh
   ````

10. **请写出用 journalctl 命令查看 nginx.service 今天以来，错误级别在 warning 以上的日志**  
    **写下命令：**  
    ````bash
    journalctl -u nginx.service --since "today" -p 4 -xb
    ````

11. **请找出用 8.8.8.8 域名解析服务器解析 www.gitlab.com 对应的 IP**  
    操作：  
    ````bash
    dig @8.8.8.8 www.gitlab.com
    ````
    或  
    ````bash
    nslookup www.gitlab.com 8.8.8.8
    ````

12. **请用 curl 找到 https://www.gitlab.com 最终展示的页面前经过的跳转过程**  
    操作：  
    ````bash
    curl -s -L -o /dev/null -w '%{url_effective}\n' https://www.gitlab.com --trace-ascii -
    ````

13. **请观察 /home/workspace/test 目录下的 git 项目，该项目无法执行 git pull 命令拉取代码，请尝试用 strace 命令排查问题**  
    操作：  
    ````bash
    strace -o trace.log git pull
    ````
    说明：查看 trace.log 文件，分析错误原因。

---

## 三、GitLab CI/CD 部分
1. **观察 gitlab-runner/gitlab-ci.yml 文件，请增加一个 pre-deploy 的 stage，并改变 stage 执行顺序为 (test -> build -> pre-deploy -> deploy)**  
   操作：  
   编辑 gitlab-ci.yml 文件，添加 pre-deploy stage：  
   ````yaml
   stages:
     - test
     - build
     - pre-deploy
     - deploy
   ````
   并在适当位置添加 pre-deploy 阶段的 job 定义。

2. **因为在实际工作中，通常每次触发 pipeline 时，要下载和编译依赖包，如果每次都这样操作会浪费很多时间，请问增加什么配置能改善这种情况？为什么？**  
   **口头回答**：请准备关于缓存依赖（如使用 `cache` 配置）的说明。

3. **观察 gitlab-runner/gitlab-ci2.yml 文件，请问 .gem 和 .yarn 这两个标签下的代码分别实现了什么功能？区别是什么？**  
   **口头回答**：请准备关于 Ruby（.gem）和 Node.js（.yarn）依赖管理的区别说明。

---

## 四、Docker 部分
1. **请运行一个 docker 容器，要求：**  
   - a. 以守护进程方式启动 nginx 镜像  
   - b. 将宿主机的 docker/content 目录挂载到 /usr/share/nginx/html 目录  
   - c. 将容器的 80 端口暴露到宿主机的 8080 端口  
   - d. 设置环境变量 NGINX_PORT=80  
   **写下命令：**  
   ````bash
   docker run -d -v $(pwd)/docker/content:/usr/share/nginx/html -p 8080:80 -e NGINX_PORT=80 nginx
   ````

2. **请编写一个 Dockerfile，要求：**  
   - a. 以 ubuntu:16.04 为基础镜像  
   - b. 安装一个 vim（具体命令为：apt update && apt -y upgrade && apt install -y vim）  
   - c. 暴露一个 12345 端口  
   - d. 保证 docker 启动后不瞬间退出  
   **请写出：**  
   **Dockerfile：**  
   ````dockerfile
   FROM ubuntu:16.04
   RUN apt update && apt -y upgrade && apt install -y vim
   EXPOSE 12345
   CMD ["tail", "-f", "/dev/null"]
   ````
   **docker 启动命令：**  
   ````bash
   docker run -d -p 12345:12345 <image-name>
   ````

3. **有一个 nginx 的 docker 镜像要使用宿主机的网络，请问应当如何运行？**  
   **写下命令：**  
   ````bash
   docker run --network host nginx
   ````

---

## 五、K8s 部分
1. **查看一个集群下的所有 node**  
   **写下命令：**  
   ````bash
   kubectl get nodes
   ````

2. **在 web namespace 下查看一个名为 nginx-0 的 pod 的详细信息，然后打印该 pod 的日志**  
   **写下命令：**  
   ````bash
   kubectl get pod nginx-0 -n web -o wide
   kubectl logs nginx-0 -n web
   ````

3. **将 nginx-deployment.yaml 文件部署到集群中**  
   **写下命令：**  
   ````bash
   kubectl apply -f nginx-deployment.yaml
   ````

4. **请观察 k8s/demo1.yaml 的内容，回答以下问题：**  
   **口头回答**：请准备关于实例类型、部署机器和端口类型的说明。

5. **请观察 k8s/demo2.yaml 的内容，回答以下问题：**  
   **口头回答**：请准备关于实例类型、部署机器和端口类型的说明。

6. **请简述 Deployment，Service，Pod 的关系？**  
   **口头回答**：请准备关于三者关系的说明。

7. **请描述当 k8s 集群中部署出现下列状态时，您排查问题的思路：**  
   **口头回答**：请准备关于 Pending 和 CrashLoopBackOff 状态的排查思路。

---

## 六、Ansible 部分
1. **请描述一下 ansible 文件夹下 demo.yaml 中 playbook 中 notify 的功能是什么？什么时候执行？**  
   **口头回答**：请准备关于 notify 功能的说明。

2. **请指出该 playbook 作用在哪些主机上？**  
   **口头回答**：请准备关于主机范围的说明。

3. **请将执行的并发数改为 10**  
   操作：  
   编辑 playbook 文件或运行命令时指定：  
   ````bash
   ansible-playbook demo.yaml -f 10
   ````

4. **请用命令查询 apt_key 模块 validate_certs 参数的含义和用法**  
   操作：  
   ````bash
   ansible-doc apt_key
   ````
   说明：查找 `validate_certs` 参数的描述，通常表示是否验证证书。

---

## 七、Terraform 部分
1. **请观察 terraform/demo.tf 文件：**  
   **口头回答**：请准备关于文件功能和 data 关键字的说明。

2. **请问如何查询资源类型为 alicloud_instance，资源名称为 default 的资源配置信息**  
   **写下命令：**  
   ````bash
   terraform show | grep -A 10 "alicloud_instance.default"
   ````

---

## 八、工单实例部分
1. **请观察工单，并回答问题：**  
   **口头回答**：请准备关于 GitLab Runner 在 Windows 平台注册错误的解决思路，参考 GitLab 官方 issue 列表。