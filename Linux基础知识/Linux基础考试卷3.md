# Linux基础知识考试卷2

## 一、单项选择题（每题1分，共30分）

**注意：每题只有一个正确答案**

1. 需要查看当前目录下的文件和目录列表，包括隐藏文件，应使用哪个命令：  
   * A. ls -l  
   * B. ls -a  
   * C. pwd  
   * D. cd .  

2. 在创建目录时，如果需要一次性创建多级目录（如`/data/logs/app/error`），最合适的命令是：  
   * A. mkdir /data/logs/app/error  
   * B. mkdir -p /data/logs/app/error  
   * C. touch -p /data/logs/app/error  
   * D. cp -r /data/logs/app/error  

3. 需要查看一个日志文件的最后50行内容，最合适的命令是：  
   * A. head -n 50 /var/log/messages  
   * B. tail -n 50 /var/log/messages  
   * C. cat /var/log/messages  
   * D. less /var/log/messages  

4. 需要在`/usr/local`目录下查找所有最近30天内被访问过的文件，应使用哪个命令：  
   * A. find /usr/local -type f -atime -30  
   * B. locate /usr/local -atime -30  
   * C. grep -r /usr/local -atime -30  
   * D. ls -l /usr/local | grep -30  

5. 需要在多个文本文件中查找包含“WARNING”字符串的行（忽略大小写），并显示文件名，应使用哪个命令：  
   * A. grep -i “WARNING” *.txt  
   * B. grep -l -i “WARNING” *.txt  
   * C. find . -name “*.txt” | grep “WARNING”  
   * D. cat *.txt | grep “WARNING”  

6. 需要查看一个配置文件的最后10行内容，最合适的命令是：  
   * A. head -n 10 /etc/config.conf  
   * B. tail -n 10 /etc/config.conf  
   * C. cat /etc/config.conf | grep -A 10  
   * D. less /etc/config.conf | tail -10  

7. 需要实时监控一个日志文件的新增内容，最合适的命令是：  
   * A. head -f /var/log/app.log  
   * B. tail -f /var/log/app.log  
   * C. cat -f /var/log/app.log  
   * D. vim /var/log/app.log  

8. 需要将一个目录及其内容递归复制到另一个位置，并保留文件的所有属性，应使用哪个命令：  
   * A. cp -r /source /dest  
   * B. cp -a /source /dest  
   * C. mv -r /source /dest  
   * D. tar -c /source | tar -x /dest  

9. 需要将一个正在写入的日志文件重命名为带有日期的备份文件，同时不中断服务，应使用哪个命令：  
   * A. mv access.log access.log.$(date +%Y%m%d)  
   * B. cp access.log access.log.$(date +%Y%m%d) && truncate -s 0 access.log  
   * C. touch access.log.$(date +%Y%m%d) && mv access.log  
   * D. cat access.log > access.log.$(date +%Y%m%d)  

10. 需要删除一个目录及其所有内容，但在删除前需要逐个文件确认，应使用哪个命令：  
    * A. rm -rf /data/dir  
    * B. rm -ri /data/dir  
    * C. mv /data/dir /dev/null  
    * D. cp -r /data/dir /tmp && rm /tmp/dir  

11. 需要创建一个空文件并更新其访问和修改时间为当前时间，应使用哪个命令：  
    * A. echo > newfile  
    * B. touch newfile  
    * C. cp /dev/null newfile  
    * D. mv /dev/null newfile  

12. 需要确定系统中bash shell的安装路径，最直接的命令是：  
    * A. which bash  
    * B. locate bash  
    * C. find / -name bash  
    * D. ls /bin/bash  

13. 需要将一个目录打包并以最高压缩率压缩为tar.bz2格式，最合适的命令是：  
    * A. tar -cjf project.tar.bz2 /path/to/project  
    * B. zip -9 project.zip /path/to/project  
    * C. gzip -9 /path/to/project  
    * D. tar -czf project.tar.gz /path/to/project  

14. 在脚本中需要将命令的标准输出和错误输出重定向到同一个文件（追加模式），正确的语法是：  
    * A. command > logfile 2>&1  
    * B. command >> logfile 2>&1  
    * C. command < logfile 2>&1  
    * D. command | logfile  

15. 需要将grep命令的输出结果追加到一个现有文件中，正确的命令是：  
    * A. grep “ERROR” log.txt > output.txt  
    * B. grep “ERROR” log.txt >> output.txt  
    * C. grep “ERROR” log.txt < output.txt  
    * D. grep “ERROR” log.txt | output.txt  

16. 需要统计一个日志文件中包含“Failed”字符串的行数，最有效的命令是：  
    * A. grep “Failed” log.txt | wc -l  
    * B. cat log.txt | grep “Failed” > count.txt  
    * C. wc -l log.txt | grep “Failed”  
    * D. grep “Failed” log.txt > count.txt && cat count.txt  

17. 需要查看系统中所有网络接口的详细信息，包括IP地址和状态，最合适的命令是：  
    * A. ifconfig  
    * B. ip link show  
    * C. netstat -r  
    * D. ping localhost  

18. 需要查看当前运行的进程，并按内存使用量降序排列，应使用哪个命令：  
    * A. ps aux --sort=-%mem  
    * B. top -o %MEM  
    * C. jobs | sort -r  
    * D. kill -l | grep MEM  

19. 需要强制终止所有与“nginx”相关的进程，最有效的命令是：  
    * A. kill -9 $(pgrep nginx)  
    * B. ps -ef | grep nginx  
    * C. top -p $(pgrep nginx)  
    * D. jobs | grep nginx  

20. 需要将一个远程服务器的共享目录挂载到本地`/mnt/share`目录，正确的命令是：  
    * A. mount -t nfs -o ro server:/share /mnt/share  
    * B. umount server:/share /mnt/share  
    * C. cd /mnt/share && mount server:/share  
    * D. ls server:/share > /mnt/share  

21. 需要安全卸载一个挂载在`/mnt/usb`的设备，最安全的命令是：  
    * A. umount /mnt/usb  
    * B. mount -u /mnt/usb  
    * C. eject /mnt/usb  
    * D. rm -rf /mnt/usb  

22. 需要删除当前目录下所有以“temp”开头的文件，但不删除“temp”目录，正确的命令是：  
    * A. rm -f temp*  
    * B. rm -f temp?  
    * C. rm -f temp[0-9]  
    * D. rm -f temp/*.txt  

23. 需要列出当前目录下所有文件名长度为6个字符的文件，正确的命令是：  
    * A. ls ??????  
    * B. ls *  
    * C. ls [a-z][a-z][a-z][a-z][a-z][a-z]  
    * D. ls {6}  

24. 需要编辑一个配置文件，并支持语法高亮和搜索功能，最合适的编辑器是：  
    * A. cat config.txt  
    * B. nano config.txt  
    * C. vim config.txt  
    * D. less config.txt  

25. 在vim编辑器中编辑完成后，需要保存并退出，正确的命令是：  
    * A. :q  
    * B. :w  
    * C. :wq  
    * D. :q!  

26. 在vim编辑器中，如果不想保存修改直接退出，正确的命令是：  
    * A. :q  
    * B. :w!  
    * C. :q!  
    * D. :wq!  

27. 需要确定一个文件的类型（如文本、图片、可执行文件等），最合适的命令是：  
    * A. ls -l file  
    * B. file file  
    * C. cat file  
    * D. type file  

28. 需要查看系统中所有文件系统的磁盘使用情况，并以人类可读格式显示，最合适的命令是：  
    * A. du -h  
    * B. df -h  
    * C. free -h  
    * D. top -o DISK  

29. 需要查看系统的内存使用情况，包括缓存和缓冲区，最合适的命令是：  
    * A. df -m  
    * B. free -m  
    * C. du -sh /proc  
    * D. top -bn1  

30. 需要在脚本中获取当前登录用户的用户名，最合适的命令是：  
    * A. whoami  
    * B. users  
    * C. who am i  
    * D. id -g  

## 二、判断题（每题1分，共10分）

1. 在Linux中，`ls -R`命令用于递归列出目录及其子目录内容。（   ）  

2. 在Linux中，`cd ~`命令用于切换到当前用户的主目录。（   ）  

3. 在Linux中，`rm -f`命令删除文件时会提示确认。（   ）  

4. 在Linux中，`grep -v`命令用于显示不匹配指定模式的行。（   ）  

5. 在Linux中，`tar -xzf`命令用于解压gzip压缩的tar归档文件。（   ）  

6. 在Linux中，`find -iname`命令用于按文件名查找文件，不区分大小写。（   ）  

7. 在Linux中，`tail -n 10`命令用于显示文件的最后10行内容。（   ）  

8. 在Linux中，`echo $PATH`命令用于显示当前用户的环境变量路径。（   ）  

9. 在Linux中，`vim`编辑器启动时默认处于插入模式。（   ）  

10. 在Linux中，重定向符号`>`会覆盖目标文件的内容。（   ）  

## 三、解答题（每题5分，共50分）

1. 请写出查找`/usr`目录下所有以`.txt`结尾的文件，并统计其数量的命令。  

2. 请写出查看`/var/log/messages`文件最后30行内容，并实时更新的命令。  

3. 请写出将`/data`目录打包并使用bzip2压缩为`/root/data.tar.bz2`的命令。  

4. 请写出在`/etc/hosts`文件中查找包含字符串“localhost”的行，并显示行号的命令。  

5. 请写出查找`/tmp`目录下大于5MB的文件的命令。  

6. 请写出创建目录`/test/folder1/folder2`（如果父目录不存在则创建）的命令。  

7. 请写出在vim编辑器中查找字符串“failed”并将其全部替换为“error”的命令。  

8. 请写出查找`/var`目录下最近3天内被修改过的文件的命令。  

9. 请写出将`/etc/group`文件的内容按行排序后，去除重复行的命令。  

10. 请写出一个命令，查找`/var/log`目录下所有包含“warning”字符串的文件，并将结果保存到`/tmp/warning_files.txt`文件中。  



