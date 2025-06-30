# Linux后端服务部署实践

## 课程回顾

在上一节课中，我们学习了Web服务的基础知识和Nginx的基本配置。今天我们将深入学习如何在Linux环境下部署前后端项目。

## 课程目标

1. 了解不同编程语言的包管理工具
2. 学习Node.js环境的安装和配置
3. 掌握Vue前端项目的部署流程
4. 掌握后端项目的部署流程
5. 深入理解Nginx的反向代理和负载均衡

## 包管理工具介绍

在开始部署之前，我们需要先了解不同编程语言的包管理工具。这些工具帮助我们管理项目依赖，使项目能够正常运行。

### 常见的包管理工具

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

### 为什么需要包管理工具？

1. **依赖管理**：自动处理项目所需的所有依赖包
2. **版本控制**：确保团队使用相同版本的依赖
3. **构建工具**：提供项目构建、测试等功能
4. **镜像源**：支持配置国内镜像源加速下载

## Node.js环境部署

### 基础概念

**Node.js**是一个基于Chrome V8引擎的JavaScript运行环境，它让我们可以使用JavaScript来编写服务器端程序。

**npm（Node Package Manager）**是Node.js默认的包管理工具，用于安装和管理项目依赖。

### 安装步骤

```bash
# 1. 下载Node.js 18.x版本
wget https://registry.npmmirror.com/-/binary/node/v18.17.0/node-v18.17.0-linux-x64.tar.gz

# 2. 解压安装包
tar -zxvf node-v18.17.0-linux-x64.tar.gz

# 3. 移动到指定目录
mv node-v18.17.0-linux-x64 /usr/local/

# 4. 配置环境变量
vim /etc/profile
export NODE_HOME=/usr/local/node-v18.17.0-linux-x64
export PATH=$NODE_HOME/bin:$PATH

# 5. 配置npm镜像源（加速下载）
npm config set registry https://registry.npmmirror.com
```

### 验证安装

```bash
# 查看Node.js版本
node -v

# 查看npm版本
npm -v
```

## Vue项目部署流程

### 什么是Vue？

Vue是一个用于构建用户界面的渐进式JavaScript框架。它主要用于构建单页面应用（SPA）。

### 部署前的准备工作

1. **确保环境已安装**
   - Node.js环境（上面已经安装）
   - Vue CLI（用于构建Vue项目）
   ```bash
   npm install -g @vue/cli
   ```

2. **了解项目结构**
   ```
   my-vue-project/
   ├── src/          # 源代码目录
   ├── public/       # 静态资源
   ├── package.json  # 项目配置文件
   └── dist/         # 构建后的文件（部署这个）
   ```

### 部署步骤详解

1. **拉取代码**
   ```bash
   # 从Git仓库克隆项目
   git clone <项目地址>
   cd my-vue-project
   ```

2. **安装依赖**
   ```bash
   # 安装项目依赖
   npm install
   ```

3. **项目构建**
   ```bash
   # 构建生产环境代码
   npm run build
   ```

4. **部署到Nginx**
   ```bash
   # 将构建后的文件复制到Nginx目录
   cp -r dist/* /var/www/html/
   ```

### 常见问题解决

1. **依赖安装失败**
   - 检查npm镜像源设置
   - 清除npm缓存：`npm cache clean --force`
   - 删除node_modules重新安装

2. **构建错误**
   - 检查Node.js版本兼容性
   - 查看项目配置文件
   - 检查语法错误

3. **跨域问题**
   - 配置开发环境代理
   - 配置Nginx反向代理（见下文）

4. **路由刷新404**
   - 配置Nginx try_files指令
   - 使用history模式需要特殊配置

## Nginx配置详解

### 什么是反向代理？

反向代理是指服务器接收客户端请求，然后将请求转发给内部网络上的其他服务器，并将结果返回给客户端。客户端只知道代理服务器，而不知道实际处理请求的服务器。

### Nginx配置文件结构

```nginx
# 前端项目配置
server {
    listen 80;                # 监听80端口
    server_name example.com;   # 域名配置
    
    # 前端文件目录
    root /var/www/html/dist;  # Vue项目构建文件目录
    index index.html;         # 默认首页
    
    # 处理Vue路由
    location / {
        # 尝试寻找文件，如果不存在则返回index.html
        try_files $uri $uri/ /index.html;
    }
    
    # API代理配置
    location /api/ {
        # 将请求转发到后端服务器
        proxy_pass http://backend_servers/;
        
        # 设置请求头信息
        proxy_set_header Host $host;  # 保持原始域名
        proxy_set_header X-Real-IP $remote_addr;  # 记录真实IP
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # 记录代理路径
        proxy_set_header X-Forwarded-Proto $scheme;  # 记录协议类型
        
        # 超时设置
        proxy_connect_timeout 60s;  # 连接超时
        proxy_send_timeout 60s;     # 发送超时
        proxy_read_timeout 60s;     # 读取超时
    }
}

# 后端服务器组配置
upstream backend_servers {
    # 1. 轮询策略：按顺序分配请求
    server 127.0.0.1:8001;  # 后端服务器1
    server 127.0.0.1:8002;  # 后端服务器2
    
    # 2. 加权轮询：根据权重分配请求
    server 127.0.0.1:8003 weight=3;  # 权重为3
    server 127.0.0.1:8004 weight=1;  # 权重为1
    
    # 3. IP哈希：根据IP地址固定分配到特定服务器
    # ip_hash;
    
    # 4. 最少连接：优先分配给连接数最少的服务器
    # least_conn;
    
    # 保持连接配置
    keepalive 32;  # 保持32个空闲连接
}
```

### 负载均衡策略详解

1. **轮询（Round Robin）**
   - 原理：按顺序将请求分配给不同服务器
   - 优点：配置简单，适合所有服务器性能相近的情况
   - 缺点：不考虑服务器实际负载情况

2. **加权轮询（Weighted Round Robin）**
   - 原理：根据服务器权重分配请求
   - 优点：可以根据服务器性能分配不同权重
   - 适用：服务器性能不均衡的情况

3. **IP哈希（IP Hash）**
   - 原理：根据客户端IP计算哈希值分配服务器
   - 优点：同一用户固定访问同一服务器
   - 适用：需要会话保持的场景

4. **最少连接（Least Connections）**
   - 原理：优先分配给当前连接数最少的服务器
   - 优点：能够动态适应服务器负载变化
   - 适用：请求处理时间差异大的场景

5. **URL哈希（URL Hash）**
    - 原理：根据请求的URL进行哈希分配
    - 优点：相同URL的请求总是发送到同一服务器
    - 适用：缓存服务器的场景

## 后端项目部署实践

### 后端服务部署流程

1. **环境依赖安装**
   - 根据项目需求安装对应的运行环境
   - 安装项目依赖包
   ```bash
   # Python项目示例
   pip install -r requirements.txt
   
   # Node.js项目示例
   npm install
   
   # Java项目示例
   mvn install
   ```

2. **配置文件管理**
   - 区分开发和生产环境配置
   - 敏感信息使用环境变量
   - 日志配置
   ```bash
   # 设置环境变量
   export DB_HOST=localhost
   export DB_USER=admin
   export DB_PASS=secure_password
   ```

3. **服务启动和守护**

   a. **Node.js项目使用PM2**
   ```bash
   # 安装PM2
   npm install -g pm2
   
   # 启动服务
   pm2 start app.js --name "my-app"
   
   # 查看运行状态
   pm2 status
   
   # 查看日志
   pm2 logs
   ```

   b. **Python项目使用Supervisor**
   ```bash
   # 安装Supervisor
   pip install supervisor
   
   # 配置文件
   [program:myapp]
   command=python app.py
   directory=/path/to/project
   autostart=true
   autorestart=true
   ```

   c. **使用Systemd服务**
   ```bash
   # 创建服务文件
   vim /etc/systemd/system/myapp.service
   
   [Unit]
   Description=My Application
   After=network.target
   
   [Service]
   Type=simple
   User=myapp
   WorkingDirectory=/path/to/app
   ExecStart=/usr/bin/node app.js
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   ```

4. **日志管理**
   - 配置日志轮转
   - 设置日志级别
   - 定期清理旧日志
   ```bash
   # 使用logrotate配置日志轮转
   vim /etc/logrotate.d/myapp
   
   /var/log/myapp/*.log {
       daily
       rotate 7
       compress
       delaycompress
       missingok
       notifempty
       create 644 myapp myapp
   }
   ```

### 进程管理工具比较

1. **PM2（Node.js）**
   - 优点：
     * 内建负载均衡
     * 自动重启
     * 日志管理
     * 监控面板
   - 适用场景：Node.js应用

2. **Supervisor（Python）**
   - 优点：
     * 配置简单
     * 进程管理
     * 日志处理
   - 适用场景：Python应用

3. **Systemd**
   - 优点：
     * 系统级服务管理
     * 开机自启
     * 依赖管理
   - 适用场景：所有类型应用

### 部署检查清单

1. **服务器准备**
   - [ ] 检查系统资源（CPU、内存、硬盘）
   - [ ] 确认防火墙配置
   - [ ] 检查必要端口是否开放

2. **应用部署**
   - [ ] 安装所需环境和依赖
   - [ ] 配置文件正确设置
   - [ ] 服务正常启动
   - [ ] 日志正常输出

3. **监控和维护**
   - [ ] 配置性能监控
   - [ ] 设置告警机制
   - [ ] 准备备份策略
   - [ ] 制定更新计划