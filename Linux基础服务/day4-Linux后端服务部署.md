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