# HAProxy 教程

## 一、HAProxy概述

### 1.1 什么是HAProxy
HAProxy（High Availability Proxy）是一个开源的、高性能的负载均衡和代理服务器软件。它专门用于改善大型网站和应用的可用性、可靠性和性能。

### 1.2 HAProxy的主要特点
- **高性能**：单进程、事件驱动模型，支持数万并发连接
- **可靠性**：生产环境验证的稳定性，提供热备份功能
- **功能丰富**：支持多种负载均衡算法、会话保持、SSL终端等
- **监控友好**：详细的统计信息，支持多种监控方式

## 二、为什么需要HAProxy

### 2.1 业务场景演进

#### 场景一：小型餐厅（小型网站）
想象你开了一家小餐厅：
- 每天客流量：1000人（相当于网站1-10万访问量）
- 只需要一个服务员（相当于一个Nginx服务器）
- 服务员负责：
  - 接待客人（处理用户请求）
  - 点餐（处理动态内容）
  - 上菜（返回页面内容）
- 特点：人不多时，一个服务员就够用了

#### 场景二：餐厅生意火爆（业务快速增长）
餐厅太受欢迎，客人越来越多：
- 每天客流量：5000人（相当于10-100万访问量）
- 问题：
  - 一个服务员忙不过来了（Nginx服务器压力大）
  - 需要增加服务员（增加服务器）
  - 客人希望每次都由同一个服务员服务（会话保持）
- 解决方案：
  - 雇佣一个领班（HAProxy）专门负责分配客人给不同服务员
  - 服务员们（多个Nginx）可以专心服务客人

#### 场景三：开连锁餐厅（大型应用架构）
生意越做越大，开了连锁店：
- 每天客流量：2万人以上（相当于100万以上访问量）
- 架构：
  - 在商场门口安排迎宾（LVS）：专门负责快速指引客人到不同分店
  - 每个分店都有领班（HAProxy）：负责店内的精细化服务安排
  - 多名服务员（Nginx）：专注于服务客人

### 2.2 分层架构的优势

1. **性能最大化**
   - LVS：专注流量分发，性能最强
   - HAProxy：负责会话管理和SSL，性能适中
   - Nginx：处理具体业务，按需扩展

2. **职责明确**
   - LVS：流量调度员，分发快速高效
   - HAProxy：中层管理者，负责精细调控
   - Nginx：一线服务员，处理具体业务

3. **系统弹性**
   - 每层都可以独立扩展
   - 故障隔离，一层问题不影响整体
   - 便于针对性优化和监控

### 2.3 为什么选择HAProxy

1. **从小型项目角度**
   - 配置简单，易于上手
   - 监控界面直观
   - 支持健康检查，避免服务中断

2. **从中型项目角度**
   - 支持会话保持
   - 提供丰富的负载均衡算法
   - 可以根据URL、Cookie等进行智能分发

3. **从大型项目角度**
   - 可以与LVS、Nginx完美配合
   - 支持SSL卸载，减轻后端服务器压力
   - 提供细粒度的访问控制

## 三、HAProxy架构和工作原理

### 3.1 基本架构

```mermaid
graph TB
    subgraph 用户层
        Client[用户请求]
    end

    subgraph 四层负载均衡
        LVS1[LVS主节点]
        LVS2[LVS备节点]
        VIP[虚拟IP]
    end

    subgraph HAProxy层
        HA1[HAProxy-1]
        HA2[HAProxy-2]
    end

    subgraph Web服务器层
        N1[Nginx-1]
        N2[Nginx-2]
        N3[Nginx-3]
    end

    subgraph 应用服务器层
        A1[应用服务器-1]
        A2[应用服务器-2]
        A3[应用服务器-3]
    end

    Client --> VIP
    VIP --> LVS1
    VIP --> LVS2
    LVS1 --> |四层转发| HA1
    LVS1 --> |四层转发| HA2
    LVS2 --> |备用节点| HA1
    LVS2 --> |备用节点| HA2
    HA1 --> |七层转发| N1
    HA1 --> |七层转发| N2
    HA1 --> |七层转发| N3
    HA2 --> |七层转发| N1
    HA2 --> |七层转发| N2
    HA2 --> |七层转发| N3
    N1 --> |应用请求| A1
    N1 --> |应用请求| A2
    N2 --> |应用请求| A2
    N2 --> |应用请求| A3
    N3 --> |应用请求| A1
    N3 --> |应用请求| A3
```

### 3.2 工作流程说明
1. **用户请求流程**
   - 用户请求首先到达虚拟IP（VIP）
   - LVS主节点接收请求并进行四层转发
   - HAProxy节点进行七层负载均衡
   - Nginx处理具体的Web请求
   - 应用服务器处理业务逻辑

2. **HAProxy处理流程**
   - 前端监听：接收来自LVS的请求
   - ACL规则匹配：根据规则判断请求类型
   - 负载均衡：选择合适的后端服务器
   - 健康检查：定期检查服务器状态
   - 会话保持：确保用户请求的一致性
   - 监控统计：记录性能和状态指标

## 四、HAProxy与其他负载均衡方案对比

| 特性 | LVS | HAProxy | Nginx |
|------|-----|----------|--------|
| 工作层 | 网络层(L4) | 应用层(L7)/传输层(L4) | 应用层(L7) |
| 性能 | 最强，可达到10Gbps | 较强，可达到2-3Gbps | 中等，可达到1-2Gbps |
| CPU消耗 | 最低 | 中等 | 较高 |
| 并发连接 | 百万级 | 十万级 | 万级 |
| 配置复杂度 | 简单 | 中等 | 较复杂 |
| 健康检查 | 基础TCP检查 | 支持多种协议检查 | 基础HTTP/TCP检查 |
| 会话保持 | 支持 | 支持多种方式 | 需要第三方模块 |
| 安装难度 | 较难 | 简单 | 简单 |
| 维护成本 | 低 | 中 | 中 |
| 功能特点 | - 仅做转发<br>- 性能最强<br>- 资源占用最少<br>- 无流量修改能力 | - 丰富的负载均衡算法<br>- 强大的健康检查<br>- 详细的统计信息<br>- 可编程的ACL规则 | - 反向代理<br>- 静态文件处理<br>- URL重写<br>- 资源缓存 |
| 适用场景 | - 超大并发<br>- 电信级应用<br>- 纯四层转发 | - 七层应用负载均衡<br>- 需要精细控制<br>- 中等规模集群 | - Web服务器<br>- 反向代理<br>- 小规模负载均衡 |

## 五、HAProxy的核心功能

### 5.1 负载均衡算法

#### 5.1.1 轮询（Round Robin）
- 最简单的负载均衡算法
- 按顺序将请求分配给后端服务器
- 适用场景：后端服务器性能相近
- 配置示例：
```conf
backend web-backend
    balance roundrobin    # 使用轮询算法
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.2 加权轮询（Weighted Round Robin/static-rr）
- 可以为服务器设置权重，权重越大分配到的请求越多
- static-rr为静态加权轮询，权重运行时不可变
- 适用场景：服务器性能不同
- 配置示例：
```conf
backend web-backend
    balance static-rr
    server web1 192.168.1.101:80 weight 3 check
    server web2 192.168.1.102:80 weight 1 check
```

#### 5.1.3 最少连接（Least Connection）
- 将请求分配给当前连接数最少的服务器
- 动态计算服务器负载
- 适用场景：请求处理时间差异大
- 配置示例：
```conf
backend web-backend
    balance leastconn    # 使用最少连接算法
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.4 源地址哈希（Source Hash）
- 根据客户端IP地址计算哈希值分配服务器
- 同一客户端总是访问同一服务器
- 适用场景：需要会话保持
- 配置示例：
```conf
backend web-backend
    balance source    # 使用源地址哈希
    hash-type consistent    # 使用一致性哈希
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.5 URI哈希（URI Hash）
- 根据请求的URI进行哈希分配服务器
- 适用场景：代理缓存、提高缓存命中率
- 配置示例：
```conf
backend web-backend
    balance uri
    hash-type consistent
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.6 URL参数哈希（URL Parameter Hash）
- 根据HTTP GET请求的指定参数进行哈希分配服务器
- 适用场景：同一用户请求分配到同一服务器
- 配置示例：
```conf
backend web-backend
    balance url_param userid
    hash-type consistent
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.7 HTTP头哈希（Header Hash）
- 根据HTTP请求头的指定字段进行哈希分配服务器
- 适用场景：根据自定义头部实现粘性会话
- 配置示例：
```conf
backend web-backend
    balance hdr(User-Agent)
    hash-type consistent
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check
```

#### 5.1.8 RDP Cookie哈希（RDP Cookie Hash）
- 针对RDP协议，根据cookie进行哈希分配服务器
- 适用场景：RDP协议粘性会话
- 配置示例：
```conf
backend web-backend
    balance rdp-cookie(mstshash)
    server web1 192.168.1.101:3389 check
    server web2 192.168.1.102:3389 check
```

### 5.2 健康检查机制

#### 5.2.1 TCP 端口检查
- 最基本的健康检查方式
- 检查服务器端口是否可连接
- 配置示例：
```conf
backend web-backend
    option tcp-check    # 启用TCP检查
    server web1 192.168.1.101:80 check port 80    # 检查80端口
```

#### 5.2.2 HTTP 请求检查
- 发送HTTP请求检查服务是否正常
- 可以指定检查URL和期望的响应
- 配置示例：
```conf
backend web-backend
    option httpchk GET /health    # 检查/health路径
    http-check expect status 200    # 期望返回200状态码
    server web1 192.168.1.101:80 check
```

#### 5.2.3 SSL 证书检查
- 检查SSL证书是否有效
- 验证证书有效期
- 配置示例：
```conf
backend web-backend
    option ssl-hello-chk    # 启用SSL检查
    server web1 192.168.1.101:443 check
```

### 5.3 安全特性

#### 5.3.1 SSL/TLS 终端
- HAProxy处理SSL/TLS加密解密
- 减轻后端服务器负担
- 配置示例：
```conf
frontend https-in
    bind *:443 ssl crt /etc/ssl/certs/example.pem
    mode http
    default_backend web-backend
```

#### 5.3.2 ACL 访问控制
- 根据各种条件控制访问
- 可以基于IP、域名、路径等
- 配置示例：
```conf
frontend http-in
    acl is_admin path_beg /admin    # 定义管理路径
    acl allowed_ip src 192.168.1.0/24    # 定义允许的IP
    block if is_admin !allowed_ip    # 禁止非允许IP访问管理路径
```

#### 5.3.3 DDoS 防护
- 限制连接数和请求率
- 防止资源耗尽
- 配置示例：
```conf
frontend http-in
    stick-table type ip size 100k expire 30s store conn_rate(3s)
    tcp-request connection reject if { src_conn_rate gt 10 }
```

### 5.4 运维管理

#### 5.4.1 统计信息页面
- 查看服务器状态和性能指标
- 配置示例：
```conf
listen stats
    bind *:8080
    stats enable    # 启用统计页面
    stats uri /stats    # 统计页面URL
    stats auth admin:password    # 访问认证
```

#### 5.4.2 日志配置
- 记录详细的访问日志
- 便于问题排查
- 配置示例：
```conf
global
    log 127.0.0.1 local0 info

frontend http-in
    option httplog    # 启用HTTP日志
    log global    # 使用全局日志配置
```

### 5.5 基础配置模板
这是一个完整的基础配置模板，包含了常用的配置项：

```conf
global
    log 127.0.0.1 local0 info
    maxconn 4096    # 最大连接数
    user haproxy
    group haproxy
    daemon    # 后台运行

defaults
    log global
    mode http    # 默认HTTP模式
    option httplog
    option dontlognull
    timeout connect 5000ms    # 连接超时
    timeout client 50000ms    # 客户端超时
    timeout server 50000ms    # 服务器超时

frontend http-in
    bind *:80
    default_backend web-backend

backend web-backend
    balance roundrobin
    option httpchk GET /health
    server web1 192.168.1.101:80 check
    server web2 192.168.1.102:80 check

listen stats
    bind *:8080
    stats enable
    stats uri /stats
    stats auth admin:password
```

这个配置模板包含了：
1. 基本的全局设置
2. 默认的超时配置
3. 前端HTTP监听
4. 后端服务器配置
5. 统计页面设置

你可以根据实际需求修改IP地址、端口和其他参数。记得在修改配置后重启HAProxy服务使配置生效：
```bash
systemctl restart haproxy
```

## 六、HAProxy实验环境搭建

### 6.1 安装HAProxy

#### 6.1.1 Ubuntu系统安装
```bash
# 更新软件包索引
sudo apt update

# 安装HAProxy
sudo apt install -y haproxy

# 启动并设置开机自启
sudo systemctl enable --now haproxy

# 查看版本和状态
haproxy -v
sudo systemctl status haproxy
```

### 6.2 基础配置模板

创建一个包含日志和监控的基础配置：
```bash
# 给大家一个通用的配置文件
vim  /etc/haproxy/haproxy.cfg 
# 配置文件内容
global
    # 日志配置
    log /dev/log local0 info    # 系统日志
    log /dev/log local1 notice  # 管理日志
    
    # 进程配置
    chroot /var/lib/haproxy
    user haproxy
    group haproxy
    daemon
    
    # 性能优化
    maxconn 50000               # 最大连接数
    # 给大家留着学员自我修改，随意你有兴趣就去查
    # 系统的文件描述符限制（ulimit -n）太低
    # 只有绝对了系统的文件描述符限制，才能让这个配置生效哦
    # ulimit-n 65536             # 文件描述符限制
    
    # 监控配置
    stats socket /var/lib/haproxy/stats mode 660 level admin
    stats timeout 30s

defaults
    # 日志配置
    log global
    option httplog              # 启用HTTP日志
    option dontlognull         # 不记录空连接
    
    # 模式设置
    mode http
    
    # 超时配置
    timeout connect 5000ms     # 连接超时 毫秒的哈
    timeout client 50000ms     # 客户端超时
    timeout server 50000ms     # 服务器超时
    
    # 健康检查
    option redispatch          # 服务器挂掉后重新分发
    retries 3                  # 重试次数

# 监控页面
listen stats
    bind *:8404
    stats enable               # 启用统计页面
    stats uri /stats           # 统计页面URL
    stats refresh 10s          # 刷新间隔
    stats auth admin:StrongPassword123  # 访问认证
    stats admin if TRUE        # 启用管理功能
    
    # Prometheus监控接口 - 这个以后要用到滴，给我加上加上
    http-request use-service prometheus-exporter if { path /metrics }
    
    # 隐藏版本信息
    stats hide-version

```

### 6.3 配置说明

1. **日志配置**
   - 使用系统rsyslog服务
   - 分别记录系统日志和管理日志
   - 可通过local0和local1分类管理

2. **监控设置**
   - 提供Web统计界面（8404端口）
   - 支持Prometheus监控集成
   - 包含基本认证保护

3. **性能优化**
   - 最大连接数设置为50000
   - 调整文件描述符限制
   - 启用守护进程模式

4. **安全特性**
   - 请求速率限制
   - 隐藏版本信息
   - 访问认证保护

### 6.4 测试方法

1. **配置测试**
```bash
# 检查配置文件语法
haproxy -c -f /etc/haproxy/haproxy.cfg

# 检查服务状态
systemctl status haproxy

# 查看日志
tail -f /var/log/messages
```

2. **监控检查**
```bash
# 访问统计页面
curl -u admin:StrongPassword123 http://192.168.110.5:8404/stats

# 检查Prometheus指标
curl http://192.168.110.5:8404/metrics
```

### 实验二 配置

        

        