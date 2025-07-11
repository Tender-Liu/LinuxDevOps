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