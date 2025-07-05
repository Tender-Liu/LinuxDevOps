# Linux基础知识考试卷

## 一、单项选择题（每题1分，共30分）

**注意：每题只有一个正确答案**

1. 在实际工作中，需要查看当前所在目录的绝对路径，应使用哪个命令：
   * A. ls -l
   * B. cd ~
   * C. pwd
   * D. dirname $PWD

2. 在部署项目时，需要创建多层嵌套目录结构（如/data/web/app/logs），最高效的命令是：
   * A. touch -p /data/web/app/logs
   * B. mkdir -p /data/web/app/logs
   * C. cp -r /data/web/app/logs
   * D. mkdir /data && mkdir /data/web && mkdir /data/web/app && mkdir /data/web/app/logs

3. 系统日志文件较大，需要查看最后100行并持续监控新增内容，应使用哪个命令：
   * A. ls -lh /var/log/syslog
   * B. cat /var/log/syslog
   * C. tail -n 100 -f /var/log/syslog
   * D. find /var/log -name "syslog" -exec cat {} \;

4. 需要在/etc目录下查找所有7天内修改过且大于1MB的配置文件，应使用哪个命令：
   * A. search -path "/etc" -mtime -7 -size +1M -name "*.conf"
   * B. locate -d /etc -mtime -7 -size +1M "*.conf"
   * C. find /etc -type f -mtime -7 -size +1M -name "*.conf"
   * D. grep -r -l --include="*.conf" "/etc" | xargs ls -lh | awk '$5 > 1000000'

5. 需要在多个日志文件中搜索包含"ERROR"的行（不区分大小写），并显示行号，应使用哪个命令：
   * A. find /var/log -name "*.log" -exec cat {} \; | grep "ERROR"
   * B. grep -n -i "ERROR" /var/log/*.log
   * C. cat /var/log/*.log | grep "ERROR"
   * D. ls -l /var/log/*.log | grep "ERROR"

6. 需要查看一个大型配置文件的前20行内容进行分析，最合适的命令是：
   * A. head -n 20 /etc/config.conf
   * B. tail -n 20 /etc/config.conf
   * C. cat /etc/config.conf | grep -A 20 "^"
   * D. less /etc/config.conf | sed -n '1,20p'

7. 服务器日志持续增长，需要实时监控最新的错误信息，最适合的命令是：
   * A. head -f /var/log/error.log
   * B. tail -f /var/log/error.log
   * C. cat -f /var/log/error.log
   * D. less +F /var/log/error.log

8. 需要递归复制一个目录及其所有内容到另一个位置，并保留文件权限和时间戳，应使用哪个命令：
   * A. cp -rp /source/dir /dest/dir
   * B. mv -r /source/dir /dest/dir
   * C. rsync -a /source/dir /dest/dir
   * D. tar -cf - /source/dir | tar -xf - -C /dest

9. 在不中断服务的情况下，需要将一个正在使用的日志文件重命名为带有日期的备份，应使用哪个命令：
   * A. cp access.log access.log.$(date +%Y%m%d) && echo > access.log
   * B. mv -f access.log access.log.$(date +%Y%m%d)
   * C. mv --no-clobber access.log access.log.$(date +%Y%m%d)
   * D. touch access.log.$(date +%Y%m%d) && cat access.log > access.log.$(date +%Y%m%d)

10. 需要安全地删除一个包含重要数据的目录及其所有内容，但在删除前需要确认，应使用哪个命令：
    * A. cp -r /important/data /dev/null
    * B. mv /important/data /tmp && rm -rf /tmp/data
    * C. rm -ri /important/data
    * D. touch -c /important/data/* && rm -f /important/data/*

11. 在编写脚本时，需要创建一个空文件并设置其访问和修改时间为当前时间，应使用哪个命令：
    * A. cp /dev/null newfile
    * B. mv /dev/null newfile
    * C. echo -n > newfile
    * D. touch -am newfile

12. 在排查环境问题时，需要确定系统使用的是哪个版本的Python解释器及其路径，最直接的命令是：
    * A. which python3
    * B. whereis -b python3
    * C. locate -b "\python3$"
    * D. find /usr -name python3 -type f -executable

13. 需要将整个项目目录打包并使用最高压缩率压缩，以节省存储空间，最合适的命令是：
    * A. zip -9r project.zip /path/to/project
    * B. tar -cJf project.tar.xz /path/to/project
    * C. gzip -9 < $(tar -cf - /path/to/project) > project.tar.gz
    * D. bzip2 -9 /path/to/project

14. 在脚本中需要将命令的标准输出和错误输出都重定向到同一个日志文件（覆盖原有内容），正确的语法是：
    * A. command > logfile 2>&1
    * B. command >> logfile 2>&1
    * C. command < logfile 2>&1
    * D. command | tee logfile

15. 在日志分析过程中，需要将grep命令的匹配结果追加到已有的报告文件末尾，正确的命令是：
    * A. grep "ERROR" /var/log/app.log > report.txt
    * B. grep "ERROR" /var/log/app.log >> report.txt
    * C. grep "ERROR" /var/log/app.log < report.txt
    * D. grep "ERROR" /var/log.app.log | report.txt

16. 需要统计一个大型日志文件中包含特定错误信息的行数，最高效的命令组合是：
    * A. grep "OutOfMemoryError" server.log > errors.txt && wc -l errors.txt
    * B. grep "OutOfMemoryError" server.log >> count.txt && cat count.txt
    * C. wc -l < grep "OutOfMemoryError" server.log
    * D. grep "OutOfMemoryError" server.log | wc -l

17. 在排查网络连接问题时，需要查看所有网络接口的IP地址、MAC地址和活动状态，最合适的命令是：
    * A. netstat -i
    * B. ip addr show
    * C. ping -I eth0 127.0.0.1
    * D. route -n

18. 系统负载过高，需要查看所有进程并按CPU使用率降序排列，以找出占用CPU最多的进程，应使用哪个命令：
    * A. ps aux --sort=-%cpu
    * B. top -o %CPU
    * C. jobs -l | sort -r
    * D. kill -l | grep CPU

19. 一个Java应用程序无响应，需要强制终止所有相关进程，最有效的命令是：
    * A. ps -ef | grep java
    * B. top -p $(pgrep java)
    * C. jobs | grep java
    * D. kill -9 $(pgrep java)

20. 需要挂载一个新的NFS共享存储到/mnt/data目录，并设置为读写权限，正确的命令是：
    * A. mount -t nfs -o rw server:/share /mnt/data
    * B. umount -t nfs server:/share /mnt/data
    * C. cd /mnt/data && mount server:/share
    * D. ls -la server:/share > /mnt/data

21. 在维护过程中，需要安全地卸载一个正在使用的USB设备(/dev/sdb1)，最安全的命令是：
    * A. mount -u /dev/sdb1
    * B. umount -l /dev/sdb1
    * C. cd / && eject /dev/sdb1
    * D. ls -la /dev/sdb1 && rm /dev/sdb1

22. 需要删除目录中所有以log开头的文件，但保留log目录，正确的命令是：
    * A. rm -f log?
    * B. rm -f log*
    * C. rm -f log[0-9]
    * D. rm -f log*.{txt,log} && rm -f log*.tmp

23. 需要查找当前目录下所有5个字符长度的文件名（如file1, test2等），正确的命令是：
    * A. ls ?????
    * B. ls *
    * C. ls [a-z][a-z][a-z][a-z][a-z]
    * D. ls {5}

24. 在服务器上需要编辑一个配置文件并保存修改，同时支持语法高亮和自动缩进，最适合的编辑器是：
    * A. cat > config.ini
    * B. less config.ini
    * C. vim -c "set syntax=on" config.ini
    * D. grep -v "^#" config.ini > new_config.ini

25. 在vim编辑器中修改完配置文件后，需要保存更改并退出，正确的命令是：
    * A. :q
    * B. :w
    * C. :wq 或 :x
    * D. :q!

26. 在vim中编辑系统配置文件时，发现做了错误修改，需要放弃所有更改并退出，应使用哪个命令：
    * A. :q
    * B. :w!
    * C. :wq!
    * D. :q!

27. 下载了一个未知文件，需要确定其文件类型（如文本、二进制、压缩包等），最准确的命令是：
    A. type -a unknown_file
    B. file -b unknown_file
    C. cat -A unknown_file | head
    D. ls -la unknown_file

28. 服务器存储空间不足，需要查看所有文件系统的使用情况并以人类可读的格式显示，最合适的命令是：
    A. df -h
    B. du -sh /*
    C. free -h
    D. top -o %MEM

29. 应用程序性能下降，怀疑是内存不足，需要查看系统内存使用详情（包括物理内存和交换空间），最直接的命令是：
    A. df -h /proc/meminfo
    B. du -sh /proc/kcore
    C. free -m
    D. top -bn1 | head -5

30. 在编写系统脚本时，需要获取当前执行脚本的用户名，以确保有足够的权限，最准确的命令是：
    A. who am i
    B. whoami
    C. users | head -1
    D. id -un

## 二、判断题（每题1分，共10分）

1. 在Linux中，`ls -l`命令用于以长格式列出目录内容。（   ）

2. 在Linux中，`cd ..`命令用于返回上一级目录。（   ）

3. 在Linux中，`rm -rf`命令可以递归删除目录及其内容，无需确认。（   ）

4. 在Linux中，`grep -i`命令用于忽略大小写进行搜索。（   ）

5. 在Linux中，`tar -czf`命令用于创建gzip压缩的tar归档文件。（   ）

6. 在Linux中，`find -name`命令用于按文件名查找文件，区分大小写。（   ）

7. 在Linux中，`head -n 5`命令用于显示文件的前5行内容。（   ）

8. 在Linux中，`echo $HOME`命令用于显示当前用户的主目录路径。（   ）

9. 在Linux中，`vim`编辑器默认启动在命令模式。（   ）

10. 在Linux中，管道符`|`可以将一个命令的输出作为另一个命令的输入。（   ）

## 三、解答题（每题5分，共50分）

1. 请写出查找/etc目录下所有以.conf结尾的文件，并统计数量的命令。

2. 请写出查看/var/log/syslog文件最后20行内容，并实时更新的命令。

3. 请写出将/home目录打包并使用gzip压缩成/root/home.tar.gz的命令。

4. 请写出在/etc/passwd文件中查找包含字符串"root"的行，并显示行号的命令。

5. 请写出查找/var目录下大于10MB的文件的命令。

6. 请写出创建目录/test/dir1/dir2（如果父目录不存在则创建）的命令。

7. 请写出在vim编辑器中，查找字符串"error"并将其全部替换为"warning"的命令。

8. 请写出查找/etc目录下最近7天内被修改过的文件的命令。

9. 请写出将/etc/passwd文件的内容按行排序后，只显示不重复的行的命令。

10. 请写出一个命令，查找/var/log目录下所有包含"error"字符串的文件，并将结果保存到/tmp/error_files.txt文件中。

