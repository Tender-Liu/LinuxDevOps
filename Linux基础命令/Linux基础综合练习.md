# Linux基础综合练习

## 课程目标

1. 巩固文件操作技能
   * 熟练掌握文件和目录管理
   * 深入理解文件权限概念
   * 掌握文件查找和过滤方法

2. 提升文本处理能力
   * 熟练使用vim编辑器
   * 掌握grep的高级应用
   * 学会使用管道组合命令

3. 培养综合实践能力
   * 能够解决实际运维问题
   * 掌握故障排查方法
   * 提升Shell脚本编写技能

## 练习内容

### 任务一：文件与目录管理
1. 创建以下目录结构：
```bash
linux_practice/
├── docs/
├── logs/
└── scripts/
```

2. 在各目录中创建以下文件：
- docs/readme.txt
- logs/system.log
- scripts/backup.sh

### 任务二：文本编辑与处理
1. 使用vim编辑 docs/readme.txt，添加以下内容：
```
# Linux系统管理指南

## 1. 系统监控
- 使用top命令监控系统资源
- 使用df命令查看磁盘使用情况
- 使用free命令查看内存使用情况

## 2. 日志管理
- 系统日志位于/var/log目录
- 使用tail命令实时查看日志
- 使用grep命令过滤日志信息

## 3. 文件操作
- 使用cp命令复制文件
- 使用mv命令移动文件
- 使用rm命令删除文件
```

2. 在 logs/system.log 中添加以下示例日志：
```
2024-01-01 10:00:00 INFO: System startup completed
2024-01-01 10:01:15 WARNING: High CPU usage detected
2024-01-01 10:02:30 ERROR: Failed to connect to database
2024-01-01 10:03:45 INFO: Backup process started
2024-01-01 10:04:00 ERROR: Disk space low
2024-01-01 10:05:30 INFO: Cache cleared successfully
```

### 任务三：文本搜索与处理
1. 使用grep命令完成以下操作：
- 在system.log中查找所有ERROR级别的日志
- 在system.log中统计各种日志级别(INFO/WARNING/ERROR)的出现次数
- 在readme.txt中查找包含"命令"的行

2. 使用vim的查找替换功能：
- 在readme.txt中将所有的"命令"替换为"command"

### 任务四：文件操作进阶
1. 文件备份：
- 将docs目录复制一份为docs_backup
- 将system.log重命名为system_old.log，并创建新的system.log

2. 权限设置：
- 将scripts目录设置为755权限
- 将backup.sh设置为可执行权限

### 任务五：管道符综合应用
1. 日志分析任务：
```bash
# 查找ERROR日志并保存到文件
grep "ERROR" system.log > error.log

# 同时查看多种级别的日志
grep -E "ERROR|WARNING" system.log

# 统计日志级别出现次数并保存
grep -c "ERROR" system.log > error_count.txt
grep -c "WARNING" system.log > warning_count.txt
grep -c "INFO" system.log > info_count.txt
```

2. 文件查找任务：
```bash
# 查找所有txt文件
find . -name "*.txt"

# 查找并列出文件详细信息
find . -name "*.log" -ls
```

## 解题思路

### 任务一解题思路
1. 使用mkdir命令创建目录结构：
```bash
mkdir -p linux_practice/{docs,logs,scripts}
```

2. 使用touch命令创建文件：
```bash
touch linux_practice/docs/readme.txt
touch linux_practice/logs/system.log
touch linux_practice/scripts/backup.sh
```

### 任务二解题思路
1. 编辑readme.txt：
```bash
vim linux_practice/docs/readme.txt
# 进入vim后按i进入插入模式
# 粘贴内容
# 按Esc退出插入模式
# 输入:wq保存并退出
```

2. 编辑system.log：
```bash
vim linux_practice/logs/system.log
# 按i进入插入模式
# 粘贴日志内容
# Esc后:wq保存退出
```

### 任务三解题思路
1. grep命令操作：
```bash
# 查找ERROR日志
grep "ERROR" linux_practice/logs/system.log

# 统计日志级别
grep -c "INFO" linux_practice/logs/system.log
grep -c "WARNING" linux_practice/logs/system.log
grep -c "ERROR" linux_practice/logs/system.log

# 查找包含"命令"的行
grep "命令" linux_practice/docs/readme.txt
```

2. vim替换操作：
```bash
vim linux_practice/docs/readme.txt
# 进入命令模式后输入
:%s/命令/command/g
# :wq保存退出
```

### 任务四解题思路
1. 文件备份操作：
```bash
# 复制目录
cp -r linux_practice/docs linux_practice/docs_backup

# 重命名日志文件
mv linux_practice/logs/system.log linux_practice/logs/system_old.log
touch linux_practice/logs/system.log
```

2. 设置权限：
```bash
chmod 755 linux_practice/scripts
chmod +x linux_practice/scripts/backup.sh
```

### 任务五解题思路
1. 日志分析：
```bash
# 使用grep搜索并重定向到文件
grep "ERROR" system.log > error.log

# 使用grep -E处理多个模式
grep -E "ERROR|WARNING" system.log
```

2. 文件查找：
```bash
# 使用find命令基本功能
find . -name "*.txt"
find . -name "*.log" -ls
```

## 考核要点
1. 目录和文件操作的准确性
2. vim编辑器的熟练程度
3. grep命令的使用熟练度
4. 文件权限概念的理解
5. 命令组合的灵活运用
6. 管道符和重定向的正确使用

## 扩展思考
1. 如何使用find命令在目录中查找特定文件？
2. 如何使用grep的正则表达式进行更复杂的搜索？
3. 如何使用tar命令对练习文件进行打包备份？
4. 如何结合多个基础命令完成更复杂的任务？