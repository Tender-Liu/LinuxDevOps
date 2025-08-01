# 运维相关Shell脚本练习题

## 练习题1：检查系统服务状态（简单）
**题目描述：**

编写一个Shell脚本，检查系统上某个服务（如sshd）是否正在运行，并输出其状态。

**运维场景：**

在服务器维护中，经常需要检查关键服务是否正常运行，以便及时处理问题。

**要求：**

1. 使用条件测试和if结构判断服务状态。
2. 使用systemctl命令检查服务状态（假设系统使用systemd）。
3. 输出格式为：服务 [服务名] 当前状态：运行中/未运行。

**环境准备（Ubuntu系统）：**

为了模拟服务状态检查的环境，需要确保Ubuntu系统中有一个可测试的服务（如sshd）。

1. 检查是否安装sshd：运行systemctl status ssh（Ubuntu上通常为ssh而非sshd）。
2. 如果未安装，安装openssh-server：sudo apt update && sudo apt install openssh-server -y。
3. 启动服务：sudo systemctl start ssh。
4. 如果不方便安装服务，可以将脚本中的SERVICE="sshd"改为系统中已存在的服务，如cron（通过systemctl list-units --type=service查看）。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：检查系统服务状态

SERVICE="sshd"

if systemctl is-active --quiet $SERVICE; then
    echo "服务 $SERVICE 当前状态：运行中"
else
    echo "服务 $SERVICE 当前状态：未运行"
fi

```

**操作步骤：**

1. 创建脚本文件：vim check_service.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x check_service.sh。
3. 运行脚本：./check_service.sh。
4. 查看输出结果，确认服务状态是否正确显示（可能需要以root权限运行：sudo ./check_service.sh）。

## 练习题2：批量检查文件是否存在（简单）

**题目描述：**

编写一个Shell脚本，检查当前目录下多个文件是否存在，并输出结果。

**运维场景：**

在备份或部署脚本中，需要检查关键配置文件是否存在，以确保任务顺利进行。

**要求：**

1. 使用for循环遍历文件列表。
2. 使用条件测试和if结构检查文件是否存在。
3. 输出格式为：文件 [文件名]：存在/不存在。

**环境准备（Ubuntu系统）：**

为了测试文件检查脚本，需要在当前目录下创建一些测试文件。

1. 在当前目录下创建测试文件：touch test1.txt test2.txt（创建两个文件）。
2. 确保至少有一个文件不存在（如脚本中的test3.txt），以便测试“不存在”的情况。
3. 如果需要更多文件，可以继续创建：touch test4.txt。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：批量检查文件是否存在

FILES=("test1.txt" "test2.txt" "test3.txt")

for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ]; then
        echo "文件 $FILE：存在"
    else
        echo "文件 $FILE：不存在"
    fi
done

```

**操作步骤：**

1. 创建脚本文件：vim check_files.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x check_files.sh。
3. 运行脚本：./check_files.sh。
4. 查看输出结果，确认文件状态是否正确显示（可先创建或删除部分文件进行测试）。

## 练习题3：监控磁盘使用率并报警（简单-一般）
**题目描述：**

编写一个Shell脚本，检查系统磁盘使用率是否超过阈值（例如80%），如果超过则输出报警信息。

**运维场景：**

磁盘空间不足可能导致系统故障，运维人员需要定期监控并及时清理或扩容。

**要求：**

1. 使用df命令获取磁盘使用率。
2. 使用条件测试和if结构判断是否超过阈值。
3. 输出格式为：磁盘使用率：xx%，状态：正常/警告：磁盘空间不足！。

**环境准备（Ubuntu系统）：**

磁盘使用率检查不需要特别的环境准备，但可以模拟高使用率场景以测试报警逻辑。

1. 检查当前磁盘使用率：运行df -h /查看根分区使用率。
2. 如果磁盘使用率较低（无法触发报警），可以临时创建一个大文件模拟高使用率：dd if=/dev/zero of=/tmp/bigfile bs=1M count=1000（创建1GB文件，注意磁盘空间）。
3. 测试完成后删除临时文件：rm -f /tmp/bigfile。
4. 或者调整脚本中的THRESHOLD值（如改为10%），以便在低使用率下也能触发报警。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：监控磁盘使用率并报警

THRESHOLD=80
USAGE=$(df / | grep '/' | awk '{print $5}' | sed 's/%//')

if [ $USAGE -gt $THRESHOLD ]; then
    echo "磁盘使用率：$USAGE%，状态：警告：磁盘空间不足！"
else
    echo "磁盘使用率：$USAGE%，状态：正常"
fi

```

**操作步骤：**

1. 创建脚本文件：vim check_disk.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x check_disk.sh。
3. 运行脚本：./check_disk.sh。
4. 查看输出结果，确认磁盘使用率和状态是否正确显示。


## 练习题4：批量重命名日志文件（一般）

**题目描述：**

编写一个Shell脚本，将当前目录下的所有.log文件重命名为backup_原文件名_日期.log格式。

**运维场景：**

在日志管理中，经常需要备份旧日志文件并加上日期标签，以便后续分析。

**要求：**

1. 使用for循环遍历所有.log文件。
2. 使用条件测试和if结构检查文件是否存在。
3. 使用日期命令date获取当前日期，格式为YYYYMMDD。
4. 输出格式为：重命名：原文件名 -> 新文件名。

**环境准备（Ubuntu系统）：**

为了测试日志文件重命名，需要在当前目录下创建一些.log文件。

1. 创建测试日志文件：touch test1.log test2.log test3.log。
2. 或者写入一些内容以模拟真实日志：echo "test log" > test1.log。
3. 确保当前目录有写入权限，以便重命名操作成功。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：批量重命名日志文件

DATE=$(date +%Y%m%d)

for FILE in *.log; do
    if [ -f "$FILE" ]; then
        NEW_NAME="backup_${FILE%.*}_$DATE.log"
        mv "$FILE" "$NEW_NAME"
        echo "重命名：$FILE -> $NEW_NAME"
    fi
done

```

**操作步骤：**

1. 创建脚本文件：vim rename_logs.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x rename_logs.sh。
3. 创建测试文件：touch test1.log test2.log。
4. 运行脚本：./rename_logs.sh。
5. 查看输出结果，确认文件是否成功重命名。


## 练习题5：定时检查进程并重启（一般）
**题目描述：**

编写一个Shell脚本，检查某个进程（如nginx）是否运行，如果未运行则尝试重启，并在指定次数内持续监控。

**运维场景：**

关键服务进程可能因故障停止，运维脚本需要自动检测并重启以保证服务可用性。

**要求：**

1. 使用while循环实现持续监控，限制检查次数（如5次）。
2. 使用条件测试和if结构判断进程状态（使用pgrep命令）。
3. 使用systemctl重启服务。
4. 输出格式为：第x次检查：进程 [进程名] 状态：运行中/未运行，正在重启...。

**环境准备（Ubuntu系统）：**

为了测试进程检查和重启脚本，需要安装一个可测试的服务（如nginx）。

1. 检查是否安装nginx：运行systemctl status nginx。
2. 如果未安装，安装nginx：sudo apt update && sudo apt install nginx -y。
3. 启动服务：sudo systemctl start nginx。
4. 如果不方便安装nginx，可以将脚本中的PROCESS="nginx"改为系统中已存在的服务进程，如ssh（通过ps aux查看进程名）。
5. 测试重启逻辑：手动停止服务sudo systemctl stop nginx，然后运行脚本观察是否重启。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：定时检查进程并重启
PROCESS="nginx"
MAX_CHECKS=5
COUNT=1

while [ $COUNT -le $MAX_CHECKS ]; do
    echo "第${COUNT}次检查："
    if pgrep -x "$PROCESS" > /dev/null; then
        echo "进程 $PROCESS 状态：运行中"
    else
        echo "进程 $PROCESS 状态：未运行，正在重启..."
        sudo systemctl restart $PROCESS
    fi
    ((COUNT++))
    sleep 2
done

```

**操作步骤：**

1. 创建脚本文件：vim check_process.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x check_process.sh。
3. 运行脚本：sudo ./check_process.sh（可能需要root权限）。
4. 查看输出结果，确认进程状态和重启操作是否正确执行。

## 练习题6：统计系统用户登录次数（一般）
**题目描述：**

编写一个Shell脚本，统计系统中所有用户的登录次数，并输出排名前3的用户。

**运维场景：**

编写一个Shell脚本，统计系统中所有用户的登录次数，并输出排名前3的用户。

**要求：**

1. 使用for循环遍历/etc/passwd中的用户。
2. 使用while循环读取命令输出。
3. 使用条件测试和if结构过滤无效用户。
4. 输出格式为：用户：用户名，登录次数：xx。

**环境准备（Ubuntu系统）：**

统计用户登录次数需要访问系统登录记录，通常不需要特别准备，但需要确保有权限。

1. 检查是否能访问登录记录：运行last命令，查看是否有输出。
2. 如果没有权限，使用sudo last测试，确保脚本运行时有足够权限。
3. 如果系统是全新安装，可能没有足够的登录记录，可以手动登录几次（或切换用户）以生成记录：su - 用户名。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：统计系统用户登录次数

echo "统计用户登录次数（前3名）："
for USER in $(cut -d: -f1 /etc/passwd); do
    if id "$USER" &>/dev/null; then
        LOGIN_COUNT=$(last -u "$USER" | grep -c "^$USER")
        echo "$USER:$LOGIN_COUNT"
    fi
done | sort -t: -k2 -nr | head -3 | while IFS=: read -r USER COUNT; do
    echo "用户：$USER，登录次数：$COUNT"
done

```

**操作步骤：**

1. 创建脚本文件：vim count_logins.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x count_logins.sh。
3. 运行脚本：sudo ./count_logins.sh（可能需要root权限查看登录记录）。
4. 查看输出结果，确认用户登录次数统计是否正确。

## 练习题7：自动化清理旧日志文件（一般）
**题目描述：**

编写一个Shell脚本，检查指定目录下的日志文件，删除超过指定天数（如7天）的文件，并记录清理操作。

**运维场景：**

编写一个Shell脚本，统计系统中所有用户的登录次数，并输出排名前3的用户。

**要求：**

1. 使用for循环遍历指定目录下的日志文件。
2. 使用while循环控制清理次数或条件。
3. 使用条件测试和if结构判断文件修改时间是否超过指定天数（使用find命令）。
4. 输出格式为：清理文件：文件名，修改时间：xx天前。
5. 将清理记录写入日志文件。

**环境准备（Ubuntu系统）：**

为了测试日志清理脚本，需要创建一个模拟日志目录并生成旧文件。

1. 创建测试目录：mkdir -p ~/mylogs。
2. 创建一些测试日志文件，并模拟旧文件：
    * `touch ~/mylogs/test1.log`
    * `touch ~/mylogs/test2.log`
    * 模拟旧文件（修改时间为10天前）：`touch -d "10 days ago" ~/mylogs/old1.log`
    * `touch -d "15 days ago" ~/mylogs/old2.log`
3. 确保脚本中的`LOG_DIR`指向测试目录（如`~/mylogs`），并有写入权限。
4. 确保`/var/log`目录有写入权限（用于记录清理日志），或者将`LOG_FILE`路径改为用户有权限的目录（如`~/cleanup.log`）。

**参考代码：**

```bash
#!/bin/bash
# 脚本目的：自动化清理旧日志文件

LOG_DIR="/var/log"
DAYS_OLD=7
LOG_FILE="/var/log/cleanup.log"
COUNT=1
MAX_CHECKS=10

echo "开始清理旧日志文件（超过 $DAYS_OLD 天）..."
while [ $COUNT -le $MAX_CHECKS ]; do
    for FILE in $(find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS_OLD); do
        if [ -f "$FILE" ]; then
            MOD_TIME=$(find "$FILE" -printf "%T@\n" | cut -d. -f1)
            DAYS_AGO=$(( ( $(date +%s) - $MOD_TIME ) / 86400 ))
            echo "清理文件：$FILE，修改时间：$DAYS_AGO 天前"
            echo "$(date '+%Y-%m-%d %H:%M:%S') - 清理文件：$FILE" >> "$LOG_FILE"
            rm -f "$FILE"
        fi
    done
    ((COUNT++))
    break  # 仅执行一次清理，防止死循环
done
echo "清理完成，记录已写入 $LOG_FILE"

```

**操作步骤：**

1. 创建脚本文件：vim cleanup_logs.sh，粘贴代码，保存退出（:wq）。
2. 赋予执行权限：chmod +x cleanup_logs.sh。
3. 运行脚本：sudo ./cleanup_logs.sh（可能需要root权限访问日志目录）。
4. 查看输出结果，确认旧日志文件是否被清理，并检查记录文件/var/log/cleanup.log。