# Linux后端服务部署实践

## 课程回顾

在上一节课中，我们学习了Nginx的反向代理与负载均衡配置，以及Node.js环境的安装和部署。我们详细讲解了如何部署Vue前端项目和Node.js后端服务，并通过Nginx实现了反向代理和负载均衡。今天我们将继续学习其他常见后端语言（Python、Java和Go）的部署方法。

## 课程目标

1. 掌握Python环境的安装和配置
2. 学习Python Web应用的部署流程
3. 掌握Java环境的安装和配置
4. 学习Java Web应用的部署方法
5. 掌握Go环境的安装和配置
6. 学习Go应用的部署流程
7. 了解不同语言部署的异同点


## 包管理工具介绍

在开始部署之前，我们需要先了解不同编程语言的包管理工具。这些工具帮助我们管理项目依赖，使项目能够正常运行。

###  常见的包管理工具

1. **Python - pip**
   - 用途：安装和管理Python包
   - 示例：`pip install requests`
   - 配置文件：requirements.txt

2. **Java - Maven**
   - 用途：项目构建和依赖管理
   - 示例：`mvn install`
   - 配置文件：pom.xml

3. **Node.js - npm/yarn**
   - 用途：安装和管理JavaScript包
   - 示例：`npm install express`
   - 配置文件：package.json

4. **Go - go mod**
   - 用途：Go语言依赖管理
   - 示例：`go mod tidy`
   - 配置文件：go.mod


## Python环境部署

### 基础概念

**Python**是一种解释型、高级编程语言，以简洁易读的语法和强大的生态系统而闻名。在Web开发领域，Python拥有多个流行的框架，如Django、Flask和FastAPI。

**pip**是Python的包管理工具，用于安装和管理Python包。它是Python的官方包管理器，类似于Node.js的npm。

**virtualenv**是Python的虚拟环境工具，用于创建隔离的Python环境，避免不同项目之间的依赖冲突。

### 安装步骤

```bash
# 1. 安装Python 3.x
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

# 2. 验证安装
python3 --version
pip3 --version

# 3. 配置pip镜像源（加速下载）
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip3 config set global.trusted-host mirrors.aliyun.com
```
### 部署FastAPI应用

FastAPI是一个现代、高性能的Python Web框架，专为API开发而设计，具有自动生成交互式API文档的特性。下面我们将部署一个简单的FastAPI应用。

### 创建虚拟环境

虚拟环境是Python项目的最佳实践，它可以为每个项目创建独立的Python环境，避免依赖冲突。

```bash
# 1. 创建项目目录
# 这个命令会创建一个多层级的目录结构，-p 参数确保父目录不存在时会自动创建
mkdir -p /opt/nginx/python-backend.liujun.com

# 进入刚刚创建的目录
cd /opt/nginx/python-backend.liujun.com

# 从码云(Gitee)克隆一个FastAPI项目模板
# 这会下载一个现成的FastAPI项目到当前目录
git clone https://gitee.com/Tender-Liu/fastapi-starter.git .

# 2. 为项目创建虚拟环境
# 虚拟环境是一个独立的Python环境，可以避免不同项目之间的依赖冲突
python3 -m venv venv

# 3. 激活虚拟环境
# 这个命令会启动虚拟环境，之后安装的所有Python包都会安装到这个环境中
source venv/bin/activate

# 成功激活虚拟环境后，命令提示符前会显示(venv)，如下所示：
(venv) root@ubuntu-virtual-machine:/opt/nginx/python-backend.liujun.com#

# 4. 退出虚拟环境（使用完毕后）
# 如果你想退出虚拟环境，可以使用以下命令
deactivate
```

> **虚拟环境是什么？为什么要用它？**
> 
> 虚拟环境就像是在你的电脑中创建了一个"小房间"，这个房间里有独立的Python解释器和包管理工具。使用虚拟环境的好处有：
> 
> 1. **隔离项目依赖**：不同项目可能需要不同版本的包，虚拟环境可以避免冲突
> 2. **不污染全局环境**：在虚拟环境中安装的包不会影响系统的Python环境
> 3. **方便部署**：可以轻松导出项目依赖列表，在其他环境中快速重建
> 4. **便于管理**：当项目不再需要时，只需删除虚拟环境文件夹即可
>
> **命令解释：**
> - `python3 -m venv venv`：第一个venv是Python的虚拟环境模块，第二个venv是我们创建的虚拟环境名称
> - `source venv/bin/activate`：激活虚拟环境，激活后命令提示符前会显示(venv)
> - `deactivate`：退出虚拟环境，回到系统全局Python环境

#### 1. 安装Python后端项目依赖包

```bash
# 进入项目目录
cd /opt/nginx/python-backend.liujun.com

# 激活虚拟环境 - 这一步很重要，确保我们在正确的环境中安装依赖
source venv/bin/activate

# 安装项目依赖
# requirements.txt文件包含了项目所需的所有Python包及其版本
# pip会自动读取这个文件并安装所有列出的依赖
pip install -r requirements.txt

# 启动项目进行测试
# 这个命令会运行FastAPI应用的入口文件main.py
python3 main.py

# 如果看到以下输出，说明你的Python后端服务启动正常：
启动服务器: http://localhost:8070
API文档地址: http://localhost:8070/api/docs
INFO:     Will watch for changes in these directories: ['E:\\fastapi-starter']
INFO:     Uvicorn running on http://0.0.0.0:8070 (Press CTRL+C to quit)
INFO:     Started reloader process [3048] using StatReload
INFO:     Started server process [7488]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

# 测试完成后，按Ctrl+C可以停止服务
# 如果想让服务在后台运行，可以使用nohup命令：
nohup python3 main.py > output.log 2>&1 &

# 解释：
# nohup: 让命令在终端关闭后继续运行
# > output.log: 将标准输出重定向到output.log文件
# 2>&1: 将标准错误也重定向到标准输出（即output.log）
# &: 在后台运行命令

# 检查端口是否启动正常
# 这个命令会显示8070端口的监听情况，如果有输出说明服务正在运行
netstat -nltp | grep 8070
```

#### 2. 测试应用

```bash
# 打开Windows浏览器访问后端服务的API文档
# 将IP地址替换为你的Linux服务器IP
http://192.168.110.203:8070/api/docs
```

> **提示：**
> 1. 确保你的Linux服务器防火墙允许8070端口的访问
> 2. 如果在虚拟机中部署，确保网络设置为"桥接模式"而非"NAT模式"
> 3. API文档页面是由FastAPI自动生成的，你可以在这里测试所有API接口
> 4. 如果无法访问，可以尝试以下排查步骤：
>    - 检查服务是否正在运行：`ps aux | grep python3`
>    - 检查端口是否正在监听：`netstat -nltp | grep 8070`
>    - 检查防火墙设置：`sudo ufw status`


#### 配置nginx反向代理，以及负载均衡

> **什么是反向代理？** 反向代理就像一个"前台接待员"，当用户访问网站时，实际上是先访问到这个"接待员"，然后由"接待员"将请求转发给后面的真正服务器。这样做的好处是：保护了真实服务器的安全、可以实现负载均衡、提供缓存加速等功能。

> **什么是负载均衡？** 负载均衡就像是一个"交通指挥员"，当有多个服务器可用时，它会根据规则（如轮询、权重、响应时间等）将用户请求分配到不同的服务器上，避免单个服务器压力过大，提高整体系统的稳定性和响应速度。

**配置SSL证书（实现HTTPS安全访问）**

> **为什么需要SSL证书？** SSL证书可以加密客户端和服务器之间的通信，防止数据被窃听或篡改，保护用户隐私和数据安全。在生产环境中，通常需要购买正规的SSL证书，但在学习阶段，我们可以使用自签名证书进行测试。

```bash
# 创建SSL证书目录（存放证书的专门文件夹）
mkdir -p /etc/nginx/ssl/python-backend.liujun.com

# 生成自签名SSL证书
# -x509：生成自签名证书
# -nodes：不加密私钥
# -days 365：证书有效期为365天
# -newkey rsa:2048：生成2048位的RSA密钥
# -keyout：指定私钥输出位置
# -out：指定证书输出位置
# -subj：指定证书主题信息，CN是Common Name，表示证书对应的域名
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/python-backend.liujun.com/private.key \
    -out /etc/nginx/ssl/python-backend.liujun.com/certificate.crt \
    -subj "/CN=python-backend.liujun.com"
```

**配置nginx反向代理**

> **为什么要配置Nginx？** Nginx作为反向代理服务器，可以帮助我们实现负载均衡、SSL终止、静态资源缓存等功能，提高应用的安全性、性能和可靠性。

```bash
# 编辑nginx配置文件（创建一个新的配置文件，以域名命名）
sudo vim /etc/nginx/conf.d/python-backend.liujun.com.conf

# 在配置文件中添加以下内容（替换IP和域名）
```

```nginx
# 后端服务器组（定义一组服务器，用于负载均衡）
upstream backend_servers {
    # 后端服务器列表
    # 内容请更换为你的Python后端服务地址与IP，另一个可以找你的同学合作
    server 192.168.110.203:8070 weight=1 max_fails=2 fail_timeout=30s;
    # server 192.168.110.203:8070 weight=1 max_fails=2 fail_timeout=30s;
    
    # 参数解释：
    # weight=1：权重为1，多个服务器时可以设置不同权重，权重越高分配的请求越多
    # max_fails=2：允许请求失败的次数，超过后标记为不可用
    # fail_timeout=30s：经过30秒后，会重新尝试连接已标记为不可用的服务器
}

# HTTPS server - Python项目配置
# 这个server块定义了一个HTTPS服务器，用于处理来自客户端的HTTPS请求
server {
    # 监听443端口（HTTPS的标准端口）并启用SSL
    listen 443 ssl;
    # 设置服务器名称，必须与证书中的CN匹配
    server_name python-backend.liujun.com;
    # 访问日志配置，记录所有访问请求
    access_log /var/log/nginx/python-backend.liujun.com.access.log json_combined;
    # 错误日志配置，记录警告级别以上的错误
    error_log /var/log/nginx/python-backend.liujun.com.error.log warn;
    
    # 证书文件路径（必须与之前生成的证书路径一致）
    ssl_certificate /etc/nginx/ssl/python-backend.liujun.com/certificate.crt;  # 公钥证书
    ssl_certificate_key /etc/nginx/ssl/python-backend.liujun.com/private.key;  # 私钥文件
    
    # SSL优化配置（提高安全性和性能）
    ssl_protocols TLSv1.2 TLSv1.3;                     # 只允许TLS1.2和1.3协议，禁用不安全的老版本
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;  # 使用强加密套件
    ssl_prefer_server_ciphers on;                      # 优先使用服务器的加密套件，提高安全性
    ssl_session_cache shared:SSL:10m;                  # SSL会话缓存，提高性能（10MB共享内存）
    ssl_session_timeout 10m;                           # 缓存会话的超时时间（10分钟）
    ssl_stapling on;                                   # 启用OCSP Stapling（提高性能和隐私）
    ssl_stapling_verify on;                           # 验证OCSP响应的有效性

    # API代理配置 - 处理所有以/api/开头的请求
    location /api/ {
        # 将请求转发到之前定义的后端服务器组
        proxy_pass http://backend_servers;
        
        # 配置代理协议版本（HTTP/1.1支持长连接，提高性能）
        proxy_http_version 1.1;
        
        # WebSocket支持（如果你的应用使用WebSocket，这些设置是必需的）
        # WebSocket是一种在单个TCP连接上进行全双工通信的协议
        proxy_set_header Upgrade $http_upgrade;        # 支持协议升级
        proxy_set_header Connection 'upgrade';         # 连接升级为WebSocket
        
        # 传递客户端信息到后端服务器（这样后端可以获取到真实的客户端信息）
        proxy_set_header Host $host;                  # 传递原始主机名
        proxy_set_header X-Real-IP $remote_addr;      # 传递客户端真实IP
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # 传递请求链路上的所有IP
        proxy_set_header X-Forwarded-Proto $scheme;   # 传递原始协议（http/https）
        
        # 超时设置（防止长时间运行的请求占用资源）
        proxy_connect_timeout 60s;  # 与后端服务器建立连接的超时时间
        proxy_send_timeout 60s;     # 向后端服务器传输请求的超时时间
        proxy_read_timeout 60s;     # 从后端服务器读取响应的超时时间
    }

    # 静态资源缓存配置 - 处理常见的静态文件类型
    # ~* 表示不区分大小写的正则匹配，匹配所有以这些扩展名结尾的文件
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;                                # 设置缓存过期时间为1年
        add_header Cache-Control "public, no-transform";  # 允许所有缓存服务器缓存，且不允许转换
        access_log off;                           # 关闭访问日志，减少磁盘IO
    }
    
} # 结束HTTPS server块

# HTTP重定向到HTTPS - 安全增强
# 这个server块处理所有HTTP请求，并将其重定向到HTTPS
server {
    listen 80;                                  # 监听80端口（HTTP标准端口）
    server_name python-backend.liujun.com;       # 注意：这里应该是python-backend.liujun.com而不是vue-web.liujun.com
    
    # 301是永久重定向状态码，告诉浏览器和搜索引擎这个页面已永久移动
    # $server_name是当前请求的域名，$request_uri是请求的URI部分
    return 301 https://$server_name$request_uri;  # 重定向到对应的HTTPS地址
}
```


5. **Windows系统配置域名解析**
。
   > **为什么需要配置hosts文件？** 在实际生产环境中，域名解析通常由DNS服务器完成。但在开发测试环境中，我们可以通过修改本地hosts文件，将域名直接映射到指定的IP地址，避免购买和配置真实域名。

   ```bash
   # 1. 以管理员身份打开记事本（右键点击记事本 -> 选择"以管理员身份运行"）
   # 2. 在记事本中，点击"文件" -> "打开"，导航到：C:\Windows\System32\drivers\etc\
   # 3. 在文件类型下拉框中选择"所有文件(*.*)"，然后选择并打开"hosts"文件
   # 4. 在文件末尾添加以下内容（替换IP为你的服务器IP）：
   192.168.110.你尾号多少 python-backend.liujun.com
   ```

   > **注意事项：**
   > - IP地址和域名之间使用空格分隔，不要使用制表符
   > - 确保没有多余的空格或特殊字符
   > - 保存文件时可能需要管理员权限
   > - 如果修改后不生效，可以尝试在命令提示符中运行 `ipconfig /flushdns` 刷新DNS缓存

6. **访问测试**

   > **如何验证配置是否成功？** 完成所有配置后，我们需要测试服务是否正常运行。FastAPI自带了一个交互式API文档页面，可以用来测试和了解API的功能。

   ```bash
   # 在浏览器中输入以下地址（注意是HTTPS协议）：
   https://python-backend.liujun.com/api/docs
   ```

   > **可能遇到的问题及解决方法：**
   > - 如果浏览器提示证书不受信任：这是因为我们使用了自签名证书，点击"高级" -> "继续前往"（不同浏览器提示可能不同）
   > - 如果无法访问：检查Nginx和后端服务是否正常运行，可以查看Nginx错误日志 `/var/log/nginx/python-backend.liujun.com.error.log`
   > - 如果API响应错误：检查后端服务日志，确保应用正确处理请求



## Java环境部署

### 基本概念

> **什么是Java？** Java是一种广泛使用的编程语言和计算平台，由Sun Microsystems（现已被Oracle收购）于1995年发布。Java以其"一次编写，到处运行"的特性而闻名，这意味着编译后的Java代码可以在所有支持Java的平台上运行，无需重新编译。

> **什么是JDK？** JDK（Java Development Kit）是Java开发工具包，包含了Java运行环境（JRE）、Java编译器、Java工具（如javadoc、jar）和Java基础类库。开发Java应用程序需要安装JDK。

> **什么是Maven？** Maven是一个项目管理和构建自动化工具，主要用于Java项目。它可以帮助开发者管理项目的构建、报告和文档，以及项目依赖。Maven使用一个名为POM（Project Object Model）的XML文件来描述项目结构和依赖关系。

> **什么是Spring Boot？** Spring Boot是基于Spring框架的一个子项目，旨在简化Spring应用的初始搭建和开发过程。它提供了一种快速创建独立的、生产级别的基于Spring的应用程序的方法，内置了许多常用的配置，减少了开发人员的配置工作。

### 安装JDK和Maven

#### 1. 安装JDK 11

```bash

# 下载JDK（如果下载缓慢，可以使用老师提供的安装包）
wget https://repo.huaweicloud.com/java/jdk/11.0.2+9/jdk-11.0.2_linux-x64_bin.tar.gz

# 如果使用老师提供的安装包，可以通过rz命令上传
# rz -y

# 解压JDK到指定目录
sudo tar -zxvf jdk-11.0.2_linux-x64_bin.tar.gz

# 移动JDK到指定目录
sudo mv jdk-11.0.2 /usr/local/

# 配置JDK环境变量
sudo vim /etc/profile

# 在文件末尾添加以下内容
# JDK 环境变量
export JAVA_HOME=/usr/local/jdk-11.0.2
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

# 保存并退出vim（按ESC，然后输入:wq回车）

# 使环境变量生效
source /etc/profile

# 验证JDK安装
java -version
```

> **环境变量说明：**
> - `JAVA_HOME`：指定JDK安装路径
> - `PATH`：添加JDK的bin目录到系统路径，使得可以直接运行java、javac等命令
> - `CLASSPATH`：指定Java类库的路径

#### 2. 安装Maven

```bash

# 下载Maven（如果下载缓慢，可以使用老师提供的安装包）
wget https://dlcdn.apache.org/maven/maven-3/3.9.10/binaries/apache-maven-3.9.10-bin.tar.gz

# 如果使用老师提供的安装包，可以通过rz命令上传
# rz -y

# 解压Maven到指定目录
sudo tar -zxvf apache-maven-3.9.10-bin.tar.gz

# 移动maven到指定目录
sudo mv apache-maven-3.9.10 /usr/local/


# 配置Maven环境变量（编辑之前已修改的/etc/profile文件）
sudo vim /etc/profile

# 在文件末尾添加以下内容（在JDK环境变量之后）
# Maven 环境变量
export MAVEN_HOME=/usr/local/apache-maven-3.9.10
export PATH=$PATH:$MAVEN_HOME/bin

# 保存并退出vim（按ESC，然后输入:wq回车）

# 使环境变量生效
source /etc/profile

# 验证Maven安装
mvn -version
```

> **环境变量说明：**
> - `MAVEN_HOME`：指定Maven安装路径
> - `PATH`：添加Maven的bin目录到系统路径，使得可以直接运行mvn命令

#### 3. 配置Maven镜像源（可选，但推荐）

由于默认的Maven中央仓库在国外，下载依赖可能较慢，建议配置国内镜像源。Maven配置有两种方式：用户级配置和全局配置。

**全局配置（推荐服务器环境使用）**

```bash
# 编辑Maven全局配置文件
sudo vim /usr/local/maven/conf/settings.xml
# 或者使用实际安装路径
# sudo vim /usr/local/apache-maven-3.9.10/conf/settings.xml
```

在`<mirrors>`标签中添加以下内容：
> /usr/local/apache-maven-3.9.10/conf/settings.xml 这个文件找到159行，添加到这个159行下面去
```xml
    <!-- 阿里云Maven镜像 -->
    <mirror>
    <id>aliyun</id>
    <mirrorOf>central</mirrorOf>
    <name>Aliyun Maven Repository</name>
    <url>https://maven.aliyun.com/repository/public</url>
    </mirror>

    <!-- 阿里云Maven中央仓库 -->
    <mirror>
    <id>aliyun-central</id>
    <mirrorOf>central</mirrorOf>
    <name>Aliyun Central</name>
    <url>https://maven.aliyun.com/repository/central</url>
    </mirror>

    <!-- 阿里云JCenter -->
    <mirror>
    <id>aliyun-jcenter</id>
    <mirrorOf>jcenter</mirrorOf>
    <name>Aliyun JCenter</name>
    <url>https://maven.aliyun.com/repository/jcenter</url>
    </mirror>


    # 这个是让你找位置的
    184 <mirror>
    185       <id>maven-default-http-blocker</id>
    186       <mirrorOf>external:http:*</mirrorOf>
    187       <name>Pseudo repository to mirror external repositories initially using HTTP.</name>
    188       <url>http://0.0.0.0/</url>
    189       <blocked>true</blocked>
    190 </mirror>

```

> **说明：** 
> - 配置Maven镜像源可以大幅提高依赖下载速度，特别是在国内网络环境下。
> - 全局配置：对所有用户有效，配置文件位于Maven安装目录下的`conf/settings.xml`
>
> **关于`mirrorOf`参数的说明：**
> - `<mirrorOf>central</mirrorOf>`：仅镜像中央仓库
> - `<mirrorOf>*</mirrorOf>`：镜像所有仓库（包括中央仓库、JCenter等）
> - `<mirrorOf>*,!repo1</mirrorOf>`：镜像除repo1外的所有仓库
>
> **使用`mirrorOf="*"`的优缺点：**
> - **优点**：简单方便，所有依赖都从配置的镜像下载
> - **缺点**：如果镜像仓库不包含某些特定的依赖，可能导致构建失败
> - **建议**：在大多数情况下，使用`<mirrorOf>central</mirrorOf>`就足够了；如果确定阿里云镜像包含你需要的所有依赖，可以使用`<mirrorOf>*</mirrorOf>`

### 部署Spring Boot应用

Spring Boot是目前最流行的Java Web框架之一，它简化了Spring应用的开发和部署过程。下面我们将学习如何部署一个简单的Spring Boot应用。

#### 1. 创建项目目录

```bash
# 创建项目目录
mkdir -p /opt/nginx/java-backend.liujun.com

# 进入项目目录
cd /opt/nginx/java-backend.liujun.com

# 克隆示例项目
git clone https://gitee.com/Tender-Liu/spring-boot-hello-world.git .
```

> **说明：** 我们创建了一个专门的目录来存放Spring Boot应用，并从Gitee克隆了一个示例项目。使用`.`作为git clone的目标路径，可以将代码直接克隆到当前目录，而不是创建一个新的子目录。

#### 2. 构建项目

```bash
# 使用Maven构建项目
mvn clean package
```

> **说明：** `mvn clean package`命令会清理之前的构建产物，然后重新编译和打包项目。构建成功后，会在`target`目录下生成可执行的JAR文件。

#### 3. 运行应用

```bash
# 运行Spring Boot应用
java -Xms128m -Xmx256m -jar -Dserver.port=8088 target/spring-boot-2-hello-world-1.0.2-SNAPSHOT.jar
```

> **参数说明：**
> - `-Xms128m`：设置JVM初始堆内存为256MB
> - `-Xmx256m`：设置JVM最大堆内存为256MB
> - `-Dserver.port=8088`：设置应用监听的端口为8088

当你看到以下输出时，说明应用已成功启动：

```
  .   ____          _            __ _ _
 /\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::               (v2.7.18)

2025-07-01 21:43:45.700  INFO 44795 --- [           main] c.e.helloworld.HelloWorldApplication
```

#### 4. 测试应用

```bash
# 在Linux服务器上使用curl测试
curl http://localhost:8088

# 或者在Windows浏览器中访问
# http://192.168.100.101:8088/hello
```

> **说明：** 测试成功后，按`Ctrl+C`退出应用。在生产环境中，我们需要让应用在后台运行，下面将介绍如何实现。

#### 5. 后台运行应用

```bash
# 使用nohup命令在后台运行应用
nohup java -Xms128m -Xmx256m -jar -Dserver.port=8088 target/spring-boot-2-hello-world-1.0.2-SNAPSHOT.jar > app.log 2>&1 &

# 查看应用是否成功启动
netstat -lnpt | grep java

# 查看日志
tail -f app.log
```

> **说明：** `nohup`命令可以让应用在用户退出登录后继续运行，`&`符号将进程放入后台。`> app.log 2>&1`将标准输出和错误输出重定向到app.log文件。

#### 7. 配置Nginx反向代理

为了通过域名访问应用，并支持HTTPS，我们需要配置Nginx反向代理。

```bash
# 创建SSL证书目录
sudo mkdir -p /etc/nginx/ssl/java-backend.liujun.com

# 生成自签名SSL证书
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/java-backend.liujun.com/private.key \
    -out /etc/nginx/ssl/java-backend.liujun.com/certificate.crt \
    -subj "/CN=java-backend.liujun.com"

# 创建Nginx配置文件
sudo vim /etc/nginx/conf.d/java-backend.liujun.com.conf
```

添加以下内容：

```nginx
# 后端服务器组
upstream java_backend {
    # 后端服务器列表
    # 内容请更换为你的Java后端服务地址与IP，另一个可以找你的同学合作
    server 192.168.110.203:8088 weight=1 max_fails=2 fail_timeout=30s;
    # server 192.168.110.203:8088 weight=1 max_fails=2 fail_timeout=30s;
}

# HTTPS server
server {
    listen 443 ssl;
    server_name java-backend.liujun.com;
    
    # 日志配置
    access_log /var/log/nginx/java-backend.liujun.com.access.log;
    error_log /var/log/nginx/java-backend.liujun.com.error.log;
    
    # SSL配置
    ssl_certificate /etc/nginx/ssl/java-backend.liujun.com/certificate.crt;
    ssl_certificate_key /etc/nginx/ssl/java-backend.liujun.com/private.key;
    
    # SSL优化配置（提高安全性和性能）
    ssl_protocols TLSv1.2 TLSv1.3;                     # 只允许TLS1.2和1.3协议，禁用不安全的老版本
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;  # 使用强加密套件
    ssl_prefer_server_ciphers on;                      # 优先使用服务器的加密套件，提高安全性
    ssl_session_cache shared:SSL:10m;                  # SSL会话缓存，提高性能（10MB共享内存）
    ssl_session_timeout 10m;                           # 缓存会话的超时时间（10分钟）
    ssl_stapling on;                                   # 启用OCSP Stapling（提高性能和隐私）
    ssl_stapling_verify on;                           # 验证OCSP响应的有效性
    
    # API代理（使用/api/前缀）
    location /api/ {
        # 将/api/前缀去除后转发到后端
        proxy_pass http://java_backend/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # URL重写说明
    # URL重写是指将客户端请求的URL转换为服务器内部不同的URL格式的过程
    # 在这个配置中，我们实现了以下URL重写：
    # 1. 外部访问：https://java-backend.liujun.com/api/hello
    # 2. 内部转发：http://java_backend/hello (去除了/api/前缀)
    #
    # 重写的关键点：
    # - location /api/ 匹配所有以/api/开头的请求
    # - proxy_pass http://java_backend/ 中的斜杠(/)很重要，它会自动去除location匹配的/api/前缀
    # - 如果写成 proxy_pass http://java_backend (没有斜杠)，则会将完整路径转发，变成 http://java_backend/api/hello
    #
    # 这种重写方式的好处：
    # 1. 前端统一使用/api/前缀访问后端服务，便于区分API请求和静态资源
    # 2. 后端应用不需要修改代码，仍然使用原来的路径处理请求
    # 3. 提高了系统的可维护性和安全性
}

# HTTP重定向到HTTPS
server {
    listen 80;
    server_name java-backend.liujun.com;
    return 301 https://$server_name$request_uri;
}
```


重新加载Nginx配置：

```bash
sudo nginx -t       # 测试配置是否有语法错误
sudo nginx -s reload  # 重新加载配置
```

#### 8. 配置本地域名解析（Windows）

在Windows系统上，编辑hosts文件（C:\Windows\System32\drivers\etc\hosts），添加以下内容：

```
192.168.110.xxx java-backend.liujun.com
```

其中，`192.168.110.xxx`是你的Linux服务器IP地址。


##### 测试访问

在浏览器中访问：

```
https://java-backend.liujun.com/api/hello
```

#### 9. URL重写与测试访问

##### 什么是URL重写

URL重写是一种将用户在浏览器中输入的URL转换为服务器内部不同URL的技术。在本例中，我们实现了以下URL重写：

* **原始URL**：`http://192.168.100.101:8088/hello`（直接访问Spring Boot应用）
* **新URL**：`https://java-backend.liujun.com/api/hello`（通过Nginx代理访问）

##### URL重写的实现方式

在Nginx配置中，URL重写主要通过以下方式实现：

1. **路径匹配**：`location /api/` 指令匹配所有以`/api/`开头的请求
2. **前缀去除**：`proxy_pass http://java_backend/` 中的尾部斜杠表示去除匹配的前缀
3. **请求转发**：将修改后的请求转发到后端服务器

##### URL重写的具体示例

以下是几个URL转换的具体示例：

| 客户端请求 | Nginx内部转发 | 说明 |
|------------|--------------|------|
| `/api/hello` | `/hello` | 基本前缀去除 |
| `/api/users/1` | `/users/1` | 保留路径参数 |
| `/api/search?q=test` | `/search?q=test` | 保留查询参数 |

##### 不同的重写规则

根据`proxy_pass`的配置方式，URL重写有不同的行为：

```nginx
# 情况1：带斜杠结尾 - 去除匹配的前缀
location /api/ {
    proxy_pass http://backend/;
    # /api/hello -> http://backend/hello
}

# 情况2：不带斜杠结尾 - 保留完整路径
location /api/ {
    proxy_pass http://backend;
    # /api/hello -> http://backend/api/hello
}

# 情况3：指定新路径 - 替换为新路径
location /api/ {
    proxy_pass http://backend/newpath/;
    # /api/hello -> http://backend/newpath/hello
}
```

##### URL重写的优势

1. **API路径规范化**：统一使用`/api`前缀标识API请求
2. **前后端分离**：便于区分API请求和静态资源
3. **安全性提升**：隐藏了后端服务的真实地址和端口
4. **灵活性**：可以在不修改后端代码的情况下调整URL结构
5. **便于维护**：可以轻松更改后端服务地址而不影响前端


