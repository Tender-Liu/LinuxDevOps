# Linux基础服务考试卷
## 一、选择题（1-20 每题1分，21-30 每题2分 共60分）
1. OSI七层模型中，负责数据加密和解密的是哪一层？
   - A. 会话层
   - B. 表示层
   - C. 传输层
   - D. 网络层

2. Nginx默认的主配置文件路径是？
   - A. /etc/nginx/nginx.conf
   - B. /usr/local/nginx/nginx.conf
   - C. /etc/nginx/conf.d/default.conf
   - D. /usr/nginx/nginx.conf

3. 下列哪个命令可以查看当前系统的时间同步状态？
   - A. top
   - B. chronyc sources
   - C. ps aux
   - D. free

4. Nginx中用于设置最大连接数的指令是？
   - A. worker_processes
   - B. worker_connections
   - C. keepalive_timeout
   - D. events

5. 在Nginx配置中，哪个指令用于开启GZIP压缩？
   - A. gzip_types
   - B. gzip
   - C. gzip_min_length
   - D. gzip_comp_level

6. 下列哪个不是Nginx的事件模型？
   - A. select
   - B. poll
   - C. epoll
   - D. fork

7. 通过哪个命令可以实时查看系统进程？
   - A. ps aux
   - B. netstat -an
   - C. df -h
   - D. free -m

8. Nginx中，哪个模块用于反向代理？
   - A. http_proxy_module
   - B. http_rewrite_module
   - C. http_ssl_module
   - D. http_gzip_module

9. 下列哪个命令可以查看系统内存使用情况？
   - A. free -m
   - B. ps aux
   - C. netstat -an
   - D. df -h

10. Nginx中，哪个指令用于设置日志级别？
    - A. error_log
    - B. access_log
    - C. log_format
    - D. log_level

11. 在Nginx配置文件中，哪个块用于定义全局参数？
    - A. http
    - B. server
    - C. location
    - D. events

12. 下列哪个命令可以查看磁盘空间？
    - A. df -h
    - B. free -m
    - C. ps aux
    - D. top

13. Nginx中，哪个指令用于设置服务器名称？
    - A. server_name
    - B. listen
    - C. root
    - D. index

14. 下列哪个不是Nginx的日志类型？
    - A. error_log
    - B. access_log
    - C. debug_log
    - D. warn_log

15. Nginx中，哪个指令用于设置默认首页？
    - A. index
    - B. root
    - C. server_name
    - D. listen

16. 下列哪个命令可以查看网络连接？
    - A. netstat -an
    - B. ps aux
    - C. free -m
    - D. df -h

17. Nginx中，哪个指令用于设置监听端口？
    - A. listen
    - B. server_name
    - C. root
    - D. index

18. 下列哪个不是Nginx的核心模块？
    - A. http_core_module
    - B. http_proxy_module
    - C. http_ssl_module
    - D. http_mysql_module

19. Nginx中，哪个指令用于设置连接超时时间？
    - A. keepalive_timeout
    - B. worker_connections
    - C. worker_processes
    - D. listen

20. 下列哪个命令可以查看系统负载？
    - A. top
    - B. free -m
    - C. df -h
    - D. ps aux

21. Nginx中，哪个指令用于设置网站根目录？
    - A. root
    - B. index
    - C. server_name
    - D. listen

22. 下列哪个不是Nginx的配置文件？
    - A. nginx.conf
    - B. default.conf
    - C. mime.types
    - D. httpd.conf

23. Nginx中，哪个指令用于设置SSL证书路径？
    - A. ssl_certificate
    - B. ssl_certificate_key
    - C. ssl_protocols
    - D. ssl_ciphers

24. 下列哪个命令可以查看系统日志？
    - A. tail -f /var/log/nginx/error.log
    - B. ps aux
    - C. free -m
    - D. df -h

25. Nginx中，哪个指令用于设置加密协议？
    - A. ssl_protocols
    - B. ssl_certificate
    - C. ssl_certificate_key
    - D. ssl_ciphers

26. 下列哪个不是Nginx的性能优化参数？
    - A. worker_processes
    - B. worker_connections
    - C. keepalive_timeout
    - D. server_name

27. Nginx中，哪个指令用于设置缓存时间？
    - A. expires
    - B. cache
    - C. cache_time
    - D. cache_control

28. 下列哪个命令可以查看Nginx编译参数？
    - A. nginx -V
    - B. nginx -t
    - C. nginx -s reload
    - D. nginx -c

29. Nginx中，哪个指令用于设置访问认证文件？
    - A. auth_basic_user_file
    - B. auth_basic
    - C. access_log
    - D. error_log

30. 下列哪个不是Nginx的安全加固措施？
    - A. 隐藏版本号
    - B. 添加安全响应头
    - C. 限制上传文件大小
    - D. 增加worker进程数


    
## 二、判断题（每题2分，共20分）
1. Nginx只能作为Web服务器，不能做反向代理。（ ）

2. OSI七层模型中，应用层负责数据的加密和解密。（ ）

3. 使用chronyc sources命令可以查看时间同步源状态。（ ）

4. Nginx的worker_processes越多，性能一定越好。（ ）

5. keepalive_timeout用于设置连接的超时时间。（ ）

6. Nginx支持多域名和多端口配置。（ ）

7. error_log用于记录访问日志。（ ）

8. GZIP压缩可以提升网页加载速度。（ ）

9. Nginx配置文件修改后需要重载服务才能生效。（ ）

10. LVS是一种四层负载均衡技术。（ ）


## 三、机试题（共30分）
1. 机试题一：Nginx静态页面发布（10分）
    * 创建项目目录（1分）
      - 创建目录: /opt/nginx/pear-admin-boot.{你的名字}.com
      - 确保目录权限正确

    * 项目部署（2分）
      - 克隆项目: git clone https://gitee.com/pear-admin/pear-admin-layui.git
      - 确保项目文件完整性

    * SSL证书配置（2分）
      - 创建证书目录: /opt/nginx/ssl/pear-admin-boot.{你的名字}.com/
      - 生成自签名证书
      - 配置证书权限

    * Nginx配置优化（3分）
      - 优化nginx.conf主配置文件
      - 配置worker进程数和连接数
      - 开启gzip压缩
      - SSL优化
      - 服务安全性

    * 站点配置（2分）
      - 创建并配置/etc/nginx/conf.d/pear-admin-boot.{你的名字}.com.conf
      - 配置SSL证书路径

    * 服务验证（1分）
      - 检查配置语法
      - 重载Nginx服务
      - 配置hosts文件
      - 浏览器访问验证

2. 机试题二：Nginx部署Vue前端项目（20分）
    * 环境准备（3分）
      - 安装Node.js环境
      - 安装yarn: npm install -g yarn
      - 验证环境配置

    * 项目部署（5分）
      - 创建目录: /opt/nginx/vue-admin.{你的名字}.com
      - 克隆项目: git clone https://gitee.com/nuoMis/vue-admin.git
      - 安装依赖: yarn install
      - 项目打包: yarn build

    * SSL证书配置（3分）
      - 创建证书目录: /opt/nginx/ssl/vue-admin.{你的名字}.com/
      - 生成自签名证书
      - 配置证书权限

    * Nginx配置（5分）
      - 创建并配置/etc/nginx/conf.d/vue-admin.{你的名字}.com.conf
      - 配置SSL证书
      - 配置静态文件目录
      - 配置SPA路由重写

    * 部署验证（4分）
      - 将dist目录部署到指定位置
      - 检查配置语法
      - 重载Nginx服务
      - 配置hosts文件
      - 浏览器访问验证

