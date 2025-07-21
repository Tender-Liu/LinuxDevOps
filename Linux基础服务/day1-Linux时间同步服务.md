# Linux 时间同步与系统监控实战指南

## 课程目标

通过本课程您将掌握以下核心技能：

1. 掌握时间同步服务的部署和配置
   - 理解NTP服务的重要性
   - 能够验证时间同步状态
   - 熟练使用相关命令
2. 掌握系统资源监控的方法
   - 能够查看进程和网络状态
   - 学会分析系统性能指标

---

## Chrony时间同步服务简要指南

Chrony是一个开源的时间同步服务，用于通过网络同步系统时间，确保时钟准确性。在集群环境中，时间同步至关重要。如果服务器时间不一致，可能会导致以下问题：
- **任务调度混乱**：分布式系统中的定时任务（如CronJob）依赖统一时间，时间差异会导致任务执行顺序错乱。
- **日志分析困难**：不同服务器日志时间戳不一致，排查问题时难以准确追溯事件顺序。
- **安全认证失败**：许多安全协议（如Kerberos、SSL/TLS证书验证）要求时间同步，时间偏差可能导致认证失败或通信中断。

### 1. 企业场景举例
在企业中，假设一个由多台服务器组成的微服务架构集群，负责处理电商订单。如果各服务器时间不一致，可能出现以下问题：
- 订单生成时间与支付时间不匹配，导致交易记录混乱。
- 分布式锁或缓存失效时间计算错误，引发数据一致性问题。
- 安全令牌因时间偏差而被判定为过期，影响用户登录或API调用。

此外，默认的NTP服务器通常位于国外（如pool.ntp.org），对中国用户而言可能存在延迟高或连接不稳定的问题。配置国内NTP服务器（如阿里云、腾讯云）能显著提高同步效率和可靠性。

### 2. 核心命令一览

| 命令           | 作用                     | 常用示例                                  |
|----------------|--------------------------|------------------------------------------|
| `timedatectl`  | 管理系统时间和时区       | `sudo timedatectl set-timezone Asia/Shanghai` |
| `chronyc`      | Chrony客户端控制工具     | `sudo chronyc tracking`                 |
| `date`         | 显示/设置系统时间        | `date "+%Y-%m-%d %H:%M:%S"`            |

#### chronyc常用子命令
| 子命令         | 作用                      | 示例                      |
|----------------|--------------------------|---------------------------|
| `tracking`     | 显示时间同步状态         | `chronyc tracking`       |
| `sources`      | 显示配置的时间源         | `chronyc sources -v`     |

### 3. 基本配置步骤

#### 3.1 安装与配置
```bash
# 安装chrony
sudo apt update
sudo apt install -y chrony

# 编辑配置文件，指定国内NTP服务器以提高同步速度
sudo vim /etc/chrony/chrony.conf
# 添加或修改以下内容
server ntp.aliyun.com iburst
server time1.cloud.tencent.com iburst

# 启动并启用服务
sudo systemctl restart chrony
sudo systemctl enable chrony
```

#### 3.2 时区设置
```bash
# 查看当前时区
timedatectl

# 设置时区为上海
sudo timedatectl set-timezone Asia/Shanghai

# 验证时间
date
```

#### 3.3 同步状态检查
```bash
# 查看同步状态
chronyc tracking

# 查看时间源
chronyc sources -v
```

### 4. 核心要点总结
- **主要功能**：Chrony用于时间同步，确保系统时间与NTP服务器一致，解决集群时间差异问题。
- **企业应用**：配置完成后，通常无需频繁调整，但定期检查同步状态可避免潜在风险。
- **注意事项**：
  - 必须配置国内NTP服务器以降低延迟、提高可靠性，默认国外服务器不适合中国环境。
  - 确保网络连接正常，防火墙允许NTP端口（UDP 123）通信。

---


## 系统状态查看详解

### 1. 命令解释
| 命令       | 作用                        | 基本语法                       |
|------------|----------------------------|-------------------------------|
| `top`      | 实时显示系统资源使用状况    | `top [-d 延时 -p PID]`       |
| `ps`       | 显示进程状态               | `ps [aux -- sort]`           |
| `netstat`  | 显示网络连接信息           | `netstat [-tulpn]`           |
| `free`     | 显示内存使用情况           | `free [-h -s]`              |
| `df`       | 显示磁盘使用情况           | `df [-h -T]`                |

### 2. 参数详解

#### 2.1 top命令参数

| 参数   | 作用                | 示例                |
|--------|---------------------|---------------------|
| `-d`   | 指定刷新间隔        | `top -d 2`          |
| `-p`   | 监控指定进程        | `top -p 1234`       |
| `-u`   | 显示特定用户进程    | `top -u root`       |
| `-b`   | 批处理模式          | `top -b -n 1`       |

交互命令：

* P：按CPU使用率排序
* M：按内存使用率排序
* T：按运行时间排序
* k：终止进程
* r：重新设置优先级
* c: 显示模式-显示完整命令及参数
* z: 进入颜色模式

#### 2.2 ps命令参数
| 参数        | 作用            | 示例                       |
|-------------|-----------------|----------------------------|
| `aux`       | 显示所有进程    | `ps aux`                   |
| `-ef`       | 全格式显示      | `ps -ef`                   |
| `--sort`    | 排序显示        | `ps aux --sort=-pcpu`      |
| `-u`        | 指定用户进程    | `ps -u root`               |


#### 2.3 netstat命令参数
| 参数   | 作用            | 示例              |
|--------|-----------------|-------------------|
| `-t`   | 显示TCP连接     | `netstat -t`      |
| `-u`   | 显示UDP连接     | `netstat -u`      |
| `-l`   | 显示监听端口    | `netstat -l`      |
| `-n`   | 显示端口号      | `netstat -n`      |
| `-p`   | 显示进程信息    | `netstat -p`      |

#### 2.4 free命令参数
| 参数 | 作用     | 示例         |
| ---- | -------- | ------------ |
| -h   | 人性化显示 | `free -h`    |
| -s   | 持续显示   | `free -s 1`  |
| -t   | 显示总计   | `free -t`    |
| -w   | 宽输出     | `free -w`    |

#### 2.5 df命令参数
| 参数 | 作用               | 示例            |
| ---- | ------------------ | --------------- |
| -h   | 人性化显示         | `df -h`         |
| -T   | 显示文件系统类型   | `df -T`         |
| -i   | 显示 inode 信息    | `df -i`         |
| -x   | 排除特定文件系统   | `df -x tmpfs`   |


### 3. 命令输出详解

#### 3.1 系统负载监控
```bash
# 实时监控系统负载
top
```

输出示例：
```plaintext
top - 14:28:48 up 1 day, 2:35, 1 user, load average: 0.52, 0.58, 0.59
Tasks: 180 total,   1 running, 179 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.9 us,  3.1 sy,  0.0 ni, 90.6 id,  0.0 wa,  0.0 hi,  0.4 si,  0.0 st
MiB Mem :  7881.4 total,   361.0 free,  4876.1 used,  2644.3 buff/cache
MiB Swap:  2048.0 total,  1892.5 free,   155.5 used.  2522.8 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
 1520 www-data  20   0  357604  14056   8872 S   6.0   0.2   0:00.91 nginx
 1521 mysql     20   0 1795288 365272  37500 S   5.0   4.5   2:30.31 mysqld
```

**输出解释：**
- 第1行：系统运行时间、用户数、平均负载（1分钟、5分钟、15分钟）
- 第2行：进程总数及状态分布
- 第3行：CPU使用率分布（us用户态、sy系统态、id空闲等）
- 第4-5行：内存和交换分区使用情况
- 进程列表说明：
  - PID：进程ID
  - USER：进程所有者
  - %CPU：CPU使用率
  - %MEM：内存使用率
  - COMMAND：进程名称

```bash
# 按CPU使用率排序输出前5个进程
ps aux --sort=-pcpu | head -n 6
```

输出示例：
```plaintext
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
www-data  1520  6.0  0.2 357604 14056 ?        Ss   13:45   0:00 nginx: master process
mysql     1521  5.0  4.5 1795288 365272 ?      Sl   13:45   2:30 /usr/sbin/mysqld
```

#### 3.2 网络连接查看
```bash
# 查看所有TCP连接
netstat -tnp
```

输出示例：
```plaintext
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      1521/mysqld
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1520/nginx
tcp        0      0 192.168.1.100:80        192.168.1.10:52431      ESTABLISHED 1520/nginx
```

**输出解释：**
- Proto：协议类型（tcp/udp）
- Local Address：本地地址和端口
- Foreign Address：远程地址和端口
- State：连接状态（LISTEN监听、ESTABLISHED已连接等）
- PID/Program name：进程ID和名称

```bash
# 查看监听端口
netstat -tlnp
```

#### 3.3 内存使用监控
```bash
# 查看内存使用情况
free -h
```

输出示例：
```plaintext
              total        used        free      shared  buff/cache   available
Mem:          7.7Gi       4.8Gi       361Mi       386Mi       2.6Gi       2.5Gi
Swap:         2.0Gi       155Mi       1.9Gi
```

**输出解释：**
- total：总内存大小
- used：已使用内存
- free：空闲内存
- shared：共享内存
- buff/cache：缓冲/缓存使用的内存
- available：可用内存（包括可回收的缓存）

```bash
# 每2秒更新一次内存使用情况
free -h -s 2
```

#### 3.4 磁盘使用查看
```bash
# 查看磁盘使用情况
df -h
```

输出示例：
```plaintext
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        98G   48G   45G  52% /
/dev/sda2       459G  199G  237G  46% /home
tmpfs           7.8G     0  7.8G   0% /dev/shm
```

**输出解释：**
- Filesystem：文件系统设备
- Size：总容量
- Used：已使用空间
- Avail：可用空间
- Use%：使用率百分比
- Mounted on：挂载点

```bash
# 查看文件系统类型
df -T
```

输出示例：
```plaintext
Filesystem     Type     Size  Used Avail Use% Mounted on
/dev/sda1      ext4      98G   48G   45G  52% /
/dev/sda2      ext4     459G  199G  237G  46% /home
tmpfs          tmpfs    7.8G     0  7.8G   0% /dev/shm
```

```bash
# 查看inode使用情况
df -i
```

输出示例：
```plaintext
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      6553600 285873 6267727    5% /
/dev/sda2     30531584 524188 30007396    2% /home
tmpfs          2023936      1 2023935    1% /dev/shm
```

**输出解释：**
- Inodes：总inode数量
- IUsed：已使用的inode数量
- IFree：空闲的inode数量
- IUse%：inode使用率

### 4. 练习实验

#### 练习1：系统负载分析
```bash
# 任务：找出CPU使用率最高的前5个进程
步骤1: 使用top命令
top
# 按P键按CPU使用率排序

步骤2: 使用ps命令
ps aux --sort=-pcpu | head -n 6

# 答案分析：
# 1. 进程ID
# 2. CPU使用率
# 3. 内存使用率
# 4. 命令名称

```

#### 练习2：网络连接分析
```bash
# 任务：查看系统所有TCP监听端口
步骤1: 使用netstat命令
netstat -tlnp

# 答案应包含：
# - 协议类型
# - 本地地址
# - 监听端口
# - 进程名/PID

```

#### 练习3：内存使用分析
```bash
# 任务：监控系统内存使用变化
步骤1: 使用free命令持续监控
free -h -s 2

步骤2: 分析内存使用情况
# 关注点：
# - 总内存
# - 已用内存
# - 可用内存
# - 缓存使用

```

#### 练习4：磁盘空间分析  --选学高级用法
不会的哈，自己修养，我不强求

```bash
# 任务：找出磁盘使用率超过80%的分区
步骤1: 使用df命令
df -h | awk '{if(NR>1)if(+$5>80)print}'

# 答案分析：
# - 文件系统
# - 已用空间
# - 可用空间
# - 使用率

```


### 5. 常见问题处理
#### 5.1 系统负载高
```bash
# 检查CPU密集进程
top -c
# 或
ps aux --sort=-pcpu | head

# 检查内存使用
free -h
ps aux --sort=-rss | head

```

#### 5.2 网络连接问题
```bash
# 检查网络连接状态
netstat -ant | awk '{print $6}' | sort | uniq -c

# 检查特定端口
netstat -tlnp | grep :80

```

#### 5.3 内存不足
```bash
# 查看内存使用详情
free -h
# 查看大内存进程
ps aux --sort=-rss | head

```

#### 5.4 磁盘空间不足
```bash
# 查看大文件
find / -type f -size +100M -exec ls -lh {} \;

# 查看目录大小
du -sh /*

```

### 6. 监控要点
1. 系统负载监控
    * CPU使用率
    * 平均负载
    * 进程数量
    * 线程状态
2. 网络状态监控
    * 连接数量
    * 网络流量
    * 端口状态
    * 错误统计
3. 内存使用监控
    * 物理内存使用
    * 交换空间使用
    * 缓存使用
    * 共享内存
4. 磁盘使用监控
    * 空间使用率
    * I/O负载
    * inode使用
    * 读写速度