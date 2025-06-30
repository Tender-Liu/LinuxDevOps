# Web应用发布与部署实践

## 课程目标

1. 掌握Web应用发布流程
   - 理解开发、测试、生产环境的区别
   - 掌握代码版本控制和分支管理
   - 学习自动化构建和部署流程

2. 掌握后端服务部署与管理
   - 学会部署Node.js/Express后端服务
   - 掌握Python/Flask后端环境配置
   - 了解Go/Gin框架的基本使用
   - 理解RESTful API的设计原则
   - 掌握多后端服务的管理和监控

3. 掌握前端项目部署
   - 理解前端构建流程
   - 掌握静态资源部署和优化
   - 学会配置CDN和缓存策略

4. 掌握运维管理技能
   - 掌握日志收集和分析
   - 了解性能监控和调优
   - 学习常见问题排查方法

## Web应用发布流程

### 1. 开发环境配置

#### 1.1 版本控制
```bash
# Git基本配置
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 分支管理
git checkout -b feature/user-auth  # 创建功能分支
git checkout -b hotfix/login-bug   # 创建修复分支
git checkout main                  # 切换到主分支

# 代码提交
git add .
git commit -m "feat: implement user authentication"
git push origin feature/user-auth
```

#### 1.2 环境变量管理
```bash
# 开发环境配置
cat > .env.development << EOF
API_URL=http://localhost:3000
DB_HOST=localhost
DB_PORT=5432
DEBUG=true
EOF

# 测试环境配置
cat > .env.test << EOF
API_URL=http://test-api.example.com
DB_HOST=test-db.example.com
DB_PORT=5432
DEBUG=false
EOF

# 生产环境配置
cat > .env.production << EOF
API_URL=https://api.example.com
DB_HOST=prod-db.example.com
DB_PORT=5432
DEBUG=false
EOF
```

### 2. 自动化构建与部署

#### 2.1 CI/CD配置
```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm install
    - npm run test
  only:
    - merge_requests

build:
  stage: build
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - dist/
  only:
    - main
    - release/*

deploy_staging:
  stage: deploy
  script:
    - rsync -avz --delete dist/ user@staging:/var/www/html/
  environment:
    name: staging
  only:
    - main

deploy_production:
  stage: deploy
  script:
    - rsync -avz --delete dist/ user@production:/var/www/html/
  environment:
    name: production
  when: manual
  only:
    - tags
```

#### 2.2 部署脚本
```bash
#!/bin/bash
# deploy.sh

# 配置
APP_NAME="my-web-app"
DEPLOY_USER="deploy"
DEPLOY_HOST="production.example.com"
DEPLOY_PATH="/var/www/${APP_NAME}"
BACKUP_PATH="/var/www/backups"

# 创建备份
echo "Creating backup..."
ssh ${DEPLOY_USER}@${DEPLOY_HOST} \
  "cd ${DEPLOY_PATH} && \
   tar -czf ${BACKUP_PATH}/${APP_NAME}-$(date +%Y%m%d_%H%M%S).tar.gz ."

# 部署新版本
echo "Deploying new version..."
rsync -avz --delete dist/ \
  ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}/

# 更新依赖
echo "Updating dependencies..."
ssh ${DEPLOY_USER}@${DEPLOY_HOST} \
  "cd ${DEPLOY_PATH} && \
   npm install --production"

# 重启服务
echo "Restarting service..."
ssh ${DEPLOY_USER}@${DEPLOY_HOST} \
  "cd ${DEPLOY_PATH} && \
   pm2 restart ${APP_NAME}"
```

## 后端服务部署

### 1. Node.js后端服务

#### 1.1 Node.js环境安装
```bash
# 使用nvm安装Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 16.14.0
nvm use 16.14.0

# 验证安装
node --version
npm --version
```

#### 1.2 项目初始化与依赖管理
```bash
# 创建项目目录
mkdir express-demo
cd express-demo

# 初始化项目
npm init -y

# 安装依赖
npm install express cors body-parser dotenv

# 创建环境配置文件
cat > .env << EOF
PORT=3000
NODE_ENV=development
EOF
```

#### 1.3 Express框架示例
```javascript
// app.js
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// 用户管理API路由
const users = [];

// 获取用户列表
app.get('/api/v1/users', (req, res) => {
    const { page = 1, limit = 10, status } = req.query;
    const start = (page - 1) * limit;
    const end = start + parseInt(limit);
    
    let filteredUsers = users;
    if (status) {
        filteredUsers = users.filter(user => user.status === status);
    }
    
    res.json({
        data: filteredUsers.slice(start, end),
        total: filteredUsers.length,
        page: parseInt(page),
        limit: parseInt(limit)
    });
});

// 创建用户
app.post('/api/v1/users', (req, res) => {
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).json({
            error: {
                code: 'INVALID_PARAMS',
                message: 'Name and email are required',
                details: {
                    missing: !name ? 'name' : 'email'
                }
            }
        });
    }
    
    const user = {
        id: users.length + 1,
        name,
        email,
        status: 'active',
        created_at: new Date().toISOString()
    };
    users.push(user);
    
    res.status(201).json({ data: user });
});

app.listen(port, () => {
    console.log(`Backend server running on port ${port}`);
});
```

### 2. Python后端服务

#### 2.1 Python环境安装
```bash
# 安装Python 3.8
yum install python38 python38-pip

# 创建虚拟环境
python3.8 -m venv venv
source venv/bin/activate

# 安装依赖
pip install flask flask-cors
```

#### 2.2 项目初始化与依赖管理
```bash
# 创建项目目录
mkdir flask-demo
cd flask-demo

# 创建requirements.txt
cat > requirements.txt << EOF
flask==2.0.1
flask-cors==3.0.10
python-dotenv==0.19.0
EOF

# 创建环境配置文件
cat > .env << EOF
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
EOF

# 安装依赖
pip install -r requirements.txt
```

#### 2.3 Flask框架示例
```python
# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# 配置日志
app.logger.setLevel(os.getenv('FLASK_DEBUG') and 'DEBUG' or 'INFO')

# 模拟数据存储
orders = []

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    status = request.args.get('status')
    
    start = (page - 1) * limit
    end = start + limit
    
    filtered_orders = [order for order in orders if not status or order['status'] == status]
    
    return jsonify({
        'data': filtered_orders[start:end],
        'total': len(filtered_orders),
        'page': page,
        'limit': limit
    })

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    if not data.get('items'):
        return jsonify({
            'error': {
                'code': 'INVALID_PARAMS',
                'message': 'Order items are required',
                'details': {
                    'field': 'items',
                    'value': None
                }
            }
        }), 400
    
    order = {
        'id': len(orders) + 1,
        'items': data['items'],
        'status': 'pending',
        'created_at': datetime.now().isoformat()
    }
    orders.append(order)
    
    return jsonify({'data': order}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 3. RESTful API设计原则

#### 3.1 API设计基础
- 使用HTTP动词表示操作
  * GET：获取资源
  * POST：创建资源
  * PUT：更新资源
  * DELETE：删除资源

- URL路径设计
  * 使用名词表示资源：`/users`、`/orders`
  * 资源关系表示：`/users/{id}/orders`
  * 避免动词：`/get-users`（不推荐）

- 状态码使用
  * 2xx：成功
    - 200：OK
    - 201：Created
    - 204：No Content
  * 4xx：客户端错误
    - 400：Bad Request
    - 401：Unauthorized
    - 404：Not Found
  * 5xx：服务器错误
    - 500：Internal Server Error

#### 3.2 最佳实践
- 版本控制
  ```
  /api/v1/users
  /api/v2/users
  ```

- 分页处理
  ```
  /api/users?page=2&limit=10
  ```

- 过滤和排序
  ```
  /api/users?status=active&sort=name
  ```

- 错误响应格式
  ```json
  {
    "error": {
      "code": "INVALID_PARAM",
      "message": "Invalid user ID format",
      "details": {
        "field": "user_id",
        "value": "abc"
      }
    }
  }
  ```

### 4. 服务启动脚本

#### 4.1 服务管理脚本
```bash
# start-services.sh
#!/bin/bash

# 配置服务目录
EXPRESS_DIR="./express-demo"
FLASK_DIR="./flask-demo"
GIN_DIR="./gin-demo"

# 启动Express服务
start_express() {
    echo "Starting Express service..."
    cd "$EXPRESS_DIR" && npm install && npm start &
    echo "Express service started on port 3000"
}

# 启动Flask服务
start_flask() {
    echo "Starting Flask service..."
    cd "$FLASK_DIR" && \
    source venv/bin/activate && \
    pip install -r requirements.txt && \
    flask run --host=0.0.0.0 --port=5000 &
    echo "Flask service started on port 5000"
}

# 启动Gin服务
start_gin() {
    echo "Starting Gin service..."
    cd "$GIN_DIR" && \
    go mod tidy && \
    go run main.go &
    echo "Gin service started on port 8080"
}

# 停止所有服务
stop_services() {
    echo "Stopping all services..."
    pkill -f "node.*express"
    pkill -f "python.*flask"
    pkill -f "go.*gin"
    echo "All services stopped"
}

# 根据参数执行操作
case "$1" in
    "start")
        start_express
        start_flask
        start_gin
        ;;
    "stop")
        stop_services
        ;;
    "restart")
        stop_services
        sleep 2
        start_express
        start_flask
        start_gin
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

#### 4.2 服务健康检查
```bash
# check-services.sh
#!/bin/bash

# 检查服务状态
check_service() {
    local name=$1
    local url=$2
    echo -n "Checking $name service... "
    if curl -s "$url" > /dev/null; then
        echo "OK"
    else
        echo "FAILED"
    fi
}

# 检查所有服务
check_service "Express" "http://localhost:3000/api/v1/users"
check_service "Flask" "http://localhost:5000/api/v1/orders"
check_service "Go" "http://localhost:8080/api/v1/products"
```

### 5. Go后端服务

#### 5.1 Go环境安装
```bash
# 下载并安装Go
wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.17.linux-amd64.tar.gz

# 配置环境变量
export PATH=$PATH:/usr/local/go/bin
source ~/.bashrc

# 验证安装
go version
```

#### 4.2 项目初始化与依赖管理
```bash
# 创建项目目录
mkdir gin-demo
cd gin-demo

# 初始化Go模块
go mod init gin-demo

# 安装依赖
go get -u github.com/gin-gonic/gin
go get -u github.com/joho/godotenv

# 创建环境配置文件
cat > .env << EOF
PORT=8080
GIN_MODE=debug
EOF
```

#### 4.3 Gin框架示例
```go
// main.go
package main

import (
    "github.com/gin-gonic/gin"
    "github.com/joho/godotenv"
    "log"
    "net/http"
    "os"
    "time"
    "strconv"
)

func init() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }
    
    if mode := os.Getenv("GIN_MODE"); mode != "" {
        gin.SetMode(mode)
    }
}

type Product struct {
    ID        int       `json:"id"`
    Name      string    `json:"name"`
    Price     float64   `json:"price"`
    Status    string    `json:"status"`
    CreatedAt time.Time `json:"created_at"`
}

var products []Product

func main() {
    r := gin.Default()

    // 获取产品列表
    r.GET("/api/v1/products", func(c *gin.Context) {
        page, _ := strconv.Atoi(c.DefaultQuery("page", "1"))
        limit, _ := strconv.Atoi(c.DefaultQuery("limit", "10"))
        status := c.Query("status")

        start := (page - 1) * limit
        end := start + limit

        var filteredProducts []Product
        if status != "" {
            for _, p := range products {
                if p.Status == status {
                    filteredProducts = append(filteredProducts, p)
                }
            }
        } else {
            filteredProducts = products
        }

        if end > len(filteredProducts) {
            end = len(filteredProducts)
        }

        c.JSON(http.StatusOK, gin.H{
            "data":  filteredProducts[start:end],
            "total": len(filteredProducts),
            "page":  page,
            "limit": limit,
        })
    })

    // 创建产品
    r.POST("/api/v1/products", func(c *gin.Context) {
        var product Product
        if err := c.ShouldBindJSON(&product); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{
                "error": gin.H{
                    "code":    "INVALID_PARAMS",
                    "message": "Invalid product data",
                    "details": gin.H{
                        "error": err.Error(),
                    },
                },
            })
            return
        }

        product.ID = len(products) + 1
        product.CreatedAt = time.Now()
        product.Status = "active"
        products = append(products, product)

        c.JSON(http.StatusCreated, gin.H{
            "data": product,
        })
    })

    r.Run(":8080")
}
```

## Nginx高级特性

### 1. 反向代理与负载均衡

#### 1.1 反向代理配置
```nginx
# 定义后端服务器组
upstream backend {
    # 轮询策略（默认）
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;

    # 加权轮询
    server 192.168.1.12:8080 weight=3;
    server 192.168.1.13:8080 weight=1;

    # IP哈希
    ip_hash;
    server 192.168.1.14:8080;
    server 192.168.1.15:8080;

    # 最少连接
    least_conn;
    server 192.168.1.16:8080;
    server 192.168.1.17:8080;
}

# 反向代理服务器配置
server {
    listen 80;
    server_name proxy.example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 1.2 TCP/UDP负载均衡
```nginx
# TCP/UDP调度器配置
stream {
    # MySQL负载均衡
    upstream mysql {
        server 192.168.1.20:3306 weight=2;
        server 192.168.1.21:3306 weight=1;
    }

    # DNS负载均衡
    upstream dns {
        server 192.168.1.30:53;
        server 192.168.1.31:53;
    }

    # TCP服务
    server {
        listen 3306;
        proxy_pass mysql;
    }

    # UDP服务
    server {
        listen 53 udp;
        proxy_pass dns;
    }
}
```

### 2. 链路追踪与监控

#### 2.1 OpenTracing配置
```nginx
# 加载OpenTracing模块
load_module modules/ngx_http_opentracing_module.so;

# HTTP模块配置
http {
    # OpenTracing设置
    opentracing on;
    opentracing_trace_locations off;
    opentracing_propagate_context;

    # Jaeger配置
    opentracing_load_tracer /usr/local/lib/libjaegertracing_plugin.so /etc/jaeger-config.json;

    server {
        location / {
            opentracing_operation_name $uri;
            opentracing_tag http_method $request_method;
            proxy_pass http://backend;
        }
    }
}
```

#### 2.2 Prometheus监控集成
```nginx
# 状态监控配置
location /nginx_status {
    stub_status on;
    access_log off;
    allow 127.0.0.1;
    deny all;
}

# Prometheus metrics导出
location /metrics {
    prometheus_metrics;
    allow 127.0.0.1;
    deny all;
}
```

### 3. 性能优化最佳实践

#### 3.1 系统层面优化
- 调整系统限制
  * 文件描述符限制
  * 进程数限制
  * TCP参数优化

#### 3.2 Nginx配置优化
- worker进程优化
  * worker_processes设置
  * worker_connections调整
  * worker_rlimit_nofile配置

- 缓冲区优化
  * client_body_buffer_size
  * client_max_body_size
  * client_header_buffer_size

- 超时设置
  * keepalive_timeout
  * client_header_timeout
  * client_body_timeout
  * send_timeout

#### 3.3 缓存策略优化
- 开启压缩
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml;
gzip_min_length 1000;
gzip_comp_level 6;
```

- 配置缓存
```nginx
# 浏览器缓存
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 30d;
    add_header Cache-Control "public, no-transform";
}

# 代理缓存
proxy_cache_path /path/to/cache levels=1:2 keys_zone=my_cache:10m;

location / {
    proxy_cache my_cache;
    proxy_cache_use_stale error timeout http_500 http_502 http_503 http_504;
    proxy_cache_valid 200 60m;
}
```