# Linux运维岗位面试能力锻炼试卷

**试卷说明**：  
- 本试卷旨在锻炼Linux运维岗位的面试能力，题目基于职场实际场景，涵盖基础操作、日常任务、故障排查和系统管理等方面。  
- 总题数：45题，总分：100分，建议完成时间：90分钟。  
- 题目类型：选择题（单选）、判断题、主观题（操作题、案例分析题）。  
- 选择题和判断题请在答题纸上写出选项或判断结果，主观题需清晰书写答案，操作题需写出具体命令或脚本，案例题需阐述思路。

---

## 一、基础操作类（共20分，适合初级岗位）
### 1.1 选择题（每题2分，共10分）
1. 你需要查看服务器日志文件的最后20行内容，以下哪个命令最合适？  
   A. `cat logfile`  
   B. `head -n 20 logfile`  
   C. `tail -n 20 logfile`  
   D. `less logfile`  


2. 在检查服务器磁盘空间时，以下哪个命令可以显示挂载点和文件系统类型？  
   A. `df`  
   B. `df -h`  
   C. `df -T`  
   D. `du -h`  


3. 你需要快速查找当前目录下所有以`.conf`结尾的文件并显示详细信息，以下哪个命令正确？  
   A. `ls *.conf`  
   B. `ls -l *.conf`  
   C. `find *.conf`  
   D. `grep *.conf`  


4. 如果需要为一个脚本文件添加执行权限并确保只有所有者可读写，以下哪个命令是正确的？  
   A. `chmod 644 script.sh`  
   B. `chmod 755 script.sh`  
   C. `chmod 700 script.sh`  
   D. `chmod 777 script.sh`  


5. 你需要查看当前服务器的所有网络接口和IP地址，以下哪个命令可以实现？  
   A. `netstat -i`  
   B. `ip addr show`  
   C. `df -h`  
   D. `ps aux`  


### 1.2 判断题（每题2分，共10分）
6. 使用`cp -a`命令复制文件时，可以保留文件的权限和时间戳等属性。  

7. `tail -f logfile`可以实时监控日志文件的新增内容，但无法指定行数。  

8. 在Linux中，修改文件所有者只能使用`chown`命令，无法通过其他工具实现。  

9. 创建新用户后，如果不设置密码，用户可以通过SSH密钥登录。  

10. `grep -i`参数会忽略大小写进行搜索。  



## 二、日常任务类（共30分，适合中级岗位）
### 2.1 选择题（每题2分，共12分）
11. 你需要将`/data`目录打包成一个压缩文件`data.tar.gz`并显示详细过程，以下哪个命令正确？  
    A. `tar -cvf data.tar.gz /data`  
    B. `tar -zcvf data.tar.gz /data`  
    C. `tar -xvf data.tar.gz /data`  
    D. `tar -cv data.tar.gz /data`  

12. 如果你需要查看当前服务器的所有TCP监听端口，以下哪个命令是正确的？  
    A. `netstat -lnp`  
    B. `netstat -lnpt`  
    C. `netstat -tunap`  
    D. `netstat -i`  

13. 你需要启动一个服务（如`nginx`）并查看其启动日志，以下哪个命令组合最合适？  
    A. `systemctl start nginx && systemctl status nginx`  
    B. `systemctl start nginx && systemctl enable nginx`  
    C. `systemctl restart nginx && systemctl reload nginx`  
    D. `systemctl enable nginx && systemctl status nginx`  

14. 在排查日志时，你需要查找包含“error”的行并显示前后3行上下文，以下哪个命令正确？  
    A. `grep "error" logfile`  
    B. `grep -n "error" logfile`  
    C. `grep -C 3 "error" logfile`  
    D. `grep -l "error" logfile`  

15. 你需要查看当前系统运行了多长时间以及平均负载，以下哪个命令最合适？  
    A. `who`  
    B. `uptime`  
    C. `top`  
    D. `df`  

16. 你需要将一个大文件分割成多个小文件进行传输，以下哪个命令最合适？  
    A. `split`  
    B. `cut`  
    C. `tar`  
    D. `zip`  

### 2.2 判断题（每题2分，共8分）
17. 使用`rsync -avz`命令同步文件时，可以保留权限并启用压缩传输。  

18. 设置定时任务时，`cron`配置中`0 0 * * 0`表示任务每周日凌晨执行。  

19. 使用`ss -tunap`命令可以查看端口对应的进程信息，比`netstat`更快。  

20. `history | grep ssh`可以快速查找历史命令中包含“ssh”的记录。  


### 2.3 主观题（每题5分，共10分）
21. 你需要创建一个定时任务，每周一凌晨3点自动清理`/tmp`目录下的所有文件，写出`crontab`配置行。  
    
22. 写出命令，查找当前目录下所有大于100MB的文件并列出详细信息。  



## 三、故障排查类（共25分，适合高级岗位）
### 3.1 选择题（每题2分，共6分）
23. 服务器响应缓慢，你需要查看CPU和内存占用情况并按CPU排序，以下哪个命令最合适？  
    A. `top`  
    B. `htop`  
    C. `ps aux --sort=-%cpu`  
    D. `free -m`  


24. SSH无法连接到远程服务器，以下哪个命令可以检查目标服务器的SSH端口是否开放？  
    A. `ping remote_ip`  
    B. `telnet remote_ip 22`  
    C. `traceroute remote_ip`  
    D. `ifconfig`  

25. 你需要查看某个服务（如`nginx`）的错误日志以排查问题，以下哪个命令最合适？  
    A. `systemctl status nginx`  
    B. `journalctl -u nginx -p 3`  
    C. `systemctl enable nginx`  
    D. `systemctl reload nginx`  

26. 你需要检查服务器是否存在僵尸进程，以下哪个命令最合适？  
    A. `ps aux | grep Z`  
    B. `top | grep zombie`  
    C. `free -m`  
    D. `df -h`  

### 3.2 判断题（每题2分，共4分）
27. 磁盘空间不足时，使用`ncdu`工具可以更直观地分析目录空间占用。  

28. `netstat -tunap | grep 80`可以查看占用80端口的进程信息。  

29. 系统负载过高时，检查swap分区使用情况无关紧要。  

30. 使用`dmesg | grep error`可以查看内核日志中的错误信息。  


### 3.3 主观题（每题5分，共15分）
31. 服务器磁盘空间不足，某个分区已满，写出排查占用空间最大的文件或目录的具体命令和步骤。  

32. 一个Web服务（如`apache`）突然无法访问，写出你的排查步骤和相关命令。  

33. 服务器响应延迟高，怀疑是网络问题，写出你会使用的命令和分析方法。  



## 四、综合应用类（共25分，适合运维工程师）
### 4.1 主观题（每题5分，共25分）
**注意**：本部分题目需详细阐述思路或编写完整脚本，建议在面试中安排上机操作。  
34. 编写一个Shell脚本，检查某个服务的进程是否存在（如`nginx`），如果不存在则尝试启动。  



35. 你的服务器需要限制SSH访问，只允许特定IP（如`192.168.1.100`）连接，写出配置步骤和命令。  
      
36. 设计一个监控策略，定期检查服务器的磁盘使用率，如果超过80%则发送告警邮件，写出脚本思路和命令。  

37. 你需要为一个开发团队配置一个共享目录`/data/share`，确保团队成员有读写权限但不能删除他人文件，写出配置步骤。  
   
38. 服务器被怀疑存在异常流量，可能是DDoS攻击，写出你会采取的排查和应急措施，包括命令和步骤。  
    


## 评分标准
- **选择题（28分）**：每题2分，正确得满分，错误或未答得0分。  
- **判断题（22分）**：每题2分，正确得满分，错误或未答得0分。  
- **主观题（50分）**：每题5分，答案准确、逻辑清晰得满分，部分正确得3-4分，思路正确但不完整得1-2分，无效回答得0分。  
- **总分计算**：总分100分，建议根据岗位级别调整题目权重（如初级岗位重点考核前两部分，中高级岗位全面考核）。

