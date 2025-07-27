# MySQL 考试卷

这份是最完整的版本，基于您的教学内容（Day1到Day5，包含基础操作、查询、优化、权限、主从、备份等）。我扩展了选择题到40道（每题1分，共40分），简答题到15道（每题2分，共30分），理论总分70分；实操部分扩展到6大题（总30分）。这覆盖了所有关键知识点，帮助学员全面巩固。

考试总分：100分。建议时长：3小时。学员需准备MySQL环境、Navicat和employees数据库。

## 理论部分（70分）

### 一、选择题（每题1分，共40分）
1. MySQL的默认存储引擎是什么？
   A. MyISAM
   B. InnoDB
   C. MEMORY
   D. ARCHIVE

2. 在创建表时，哪个约束确保字段值唯一且非空？
   A. UNIQUE
   B. PRIMARY KEY
   C. NOT NULL
   D. DEFAULT

3. SELECT语句中，哪个子句用于排序结果？
   A. WHERE
   B. ORDER BY
   C. LIMIT
   D. GROUP BY

4. 主从同步中，哪个日志记录主库变更？
   A. Redo Log
   B. Undo Log
   C. Binary Log (Binlog)
   D. Slow Query Log

5. 哪个索引类型适合范围查询？
   A. 哈希索引
   B. B+树索引
   C. 全文索引
   D. 唯一索引

6. 慢查询日志的默认阈值是多少秒？
   A. 1
   B. 5
   C. 10
   D. 60

7. mysqldump命令用于什么类型备份？
   A. 物理备份
   B. 逻辑备份
   C. 增量备份
   D. 热备份

8. Buffer Pool的作用是什么？
   A. 存储查询日志
   B. 缓存数据页
   C. 管理用户权限
   D. 处理子查询

9. 哪个命令授予用户权限？
   A. CREATE USER
   B. GRANT
   C. REVOKE
   D. ALTER USER

10. INNER JOIN返回什么结果？
    A. 所有匹配记录
    B. 左表所有 + 匹配
    C. 右表所有 + 匹配
    D. 所有记录

11. MySQL中，哪个数据类型用于存储日期和时间？
    A. INT
    B. VARCHAR
    C. DATETIME
    D. FLOAT

12. AUTO_INCREMENT用于什么？
    A. 设置默认值
    B. 自增主键
    C. 唯一约束
    D. 外键

13. WHERE子句不支持什么操作？
    A. =
    B. >
    C. LIKE
    D. JOIN

14. GROUP BY常与哪个函数搭配？
    A. COUNT()
    B. INSERT
    C. DELETE
    D. UPDATE

15. 外键约束的作用是？
    A. 确保数据完整性
    B. 加速查询
    C. 存储日志
    D. 缓存数据

16. 慢查询日志用于记录什么？
    A. 错误操作
    B. 执行时间长的查询
    C. 用户登录
    D. 备份记录

17. Redo Log用于什么？
    A. 回滚事务
    B. 崩溃恢复
    C. 查询优化
    D. 权限管理

18. 主从复制的优点不包括？
    A. 读写分离
    B. 数据备份
    C. 自动索引
    D. 高可用

19. EXPLAIN命令用于？
    A. 执行查询
    B. 分析查询计划
    C. 创建表
    D. 删除数据

20. 哪个不是MySQL数据类型？
    A. TEXT
    B. BLOB
    C. ARRAY
    D. ENUM

21. LIMIT用于？
    A. 过滤条件
    B. 分页查询
    C. 排序
    D. 分组

22. UNION操作符用于？
    A. 合并查询结果
    B. 连接表
    C. 更新数据
    D. 删除记录

23. 子查询位于哪里？
    A. FROM子句
    B. WHERE子句
    C. 两者均可
    D. 无

24. 复合索引的顺序重要吗？
    A. 是
    B. 否
    C. 只在唯一索引
    D. 只在全文索引

25. ProxySQL用于什么？
   A. 数据库代理与负载均衡
   B. 备份
   C. 日志分析
   D. 索引创建

26. Shell脚本备份常用于？
    A. 全量备份
    B. 增量备份
    C. 两者
    D. 无

27. InnoDB支持什么？
    A. 行级锁
    B. 表级锁
    C. 两者
    D. 无

28. MyISAM适合什么场景？
    A. 读多写少
    B. 事务密集
    C. 外键多
    D. 崩溃恢复

29. GRANT ALL PRIVILEGES授予什么？
    A. 所有权限
    B. 只读
    C. 只写
    D. 执行

30. 读写分离通过什么实现？
    A. 主从同步
    B. 索引
    C. 缓存
    D. 分区

31. CREATE TABLE语句中，ENGINE指定什么？
    A. 字符集
    B. 存储引擎
    C. 索引
    D. 约束

32. VARCHAR和CHAR的区别是？
    A. VARCHAR变长
    B. CHAR变长
    C. 无区别
    D. VARCHAR用于数字

33. HAVING子句用于？
    A. 过滤分组结果
    B. 过滤行
    C. 排序
    D. 分页

34. 哪个不是聚合函数？
    A. SUM
    B. AVG
    C. LIKE
    D. MAX

35. 主键索引是？
    A.  clustered
    B. non-clustered
    C. 全文
    D. 哈希

36. Binlog格式有几种？
    A. 1
    B. 2
    C. 3
    D. 4

37. 热备份是什么？
    A. 服务运行中备份
    B. 服务停止备份
    C. 增量备份
    D. 逻辑备份

38. Undo Log用于？
    A. 崩溃恢复
    B. 事务回滚
    C. 查询优化
    D. 权限

39. LEFT JOIN返回什么？
    A. 左表所有
    B. 右表所有
    C. 匹配
    D. 所有

40. 哪个命令查看索引？
    A. SHOW INDEX
    B. SHOW TABLES
    C. DESCRIBE
    D. EXPLAIN

### 二、简答题（每题2分，共30分）
1. 简述InnoDB和MyISAM的区别（至少3点）。
2. 解释PRIMARY KEY和AUTO_INCREMENT的用法。
3. 描述SELECT语句语法，解释WHERE、ORDER BY、LIMIT。
4. 什么是主从同步？说明原理和读写分离优势。
5. 解释索引原理（B+树），创建注意事项。
6. 简述MySQL备份类型（全量、增量），Shell脚本应用。
7. 解释Buffer Pool和Redo Log的作用。
8. 描述用户权限管理命令（GRANT、REVOKE）。
9. 说明JOIN类型（INNER、LEFT、RIGHT）的区别。
10. 简述ProxySQL在MySQL中的作用和优势。
11. 解释慢查询优化的步骤，包括EXPLAIN的使用。
12. 描述数据类型选择原则（数值、字符串、日期）。
13. 什么是事务？说明ACID属性。
14. 简述主从延迟的原因和解决方法。
15. 解释B+树与B树的区别。

## 实操部分（30分）

**准备：** 使用MySQL命令行或Navicat，基于employees数据库。

### 一、数据库和表操作（5分）
1. 创建名为test_db的数据库（utf8mb4）。（1分）
2. 创建students表（id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT DEFAULT 18）。（2分）
3. 插入3条记录，SELECT查询。（2分）

### 二、数据查询（10分）
1. 查询employees中female员工，按hire_date降序，前10条。（3分）
2. INNER JOIN employees和salaries，显示emp_no、first_name、salary>50000。（4分）
3. GROUP BY查询departments中每个部门员工数（联dept_emp）。（3分）

### 三、数据修改（5分）
1. 更新emp_no=10001的last_name为'Smith'。（2分）
2. 删除salaries中salary<30000的记录。（3分）

### 四、权限管理（3分）
创建test_user@localhost，授予test_db的SELECT、INSERT权限。（3分）

### 五、优化（4分）
在salaries创建复合索引idx_emp_salary (emp_no, salary)，EXPLAIN检查查询。（4分）

### 六、备份和主从（3分）
1. mysqldump备份employees到backup.sql。（2分）
2. 概述主从同步配置步骤。（1分）


        