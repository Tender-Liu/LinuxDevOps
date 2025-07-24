# MySQL 异地备份与PythonORM

## 学习目标
1. 掌握 MySQL 异地备份的基本概念和重要性。
2. 学习 binlog 增量备份与恢复（高频、小数据量）。
3. 学习 mysqldump 全量备份与恢复（低频、大数据量）。
4. 熟悉常用工具的参数（`scp`、`mysqldump`、`mysqlbinlog`）。
5. 使用 `crontab` 设置定时任务，实现自动化备份。
6. 结合企业项目实战，应用主从数据库环境进行备份与恢复。
7. 了解恢复时的业务影响及应对措施。

---

## 第一部分：基础工具与参数表格（含语法解释和示例）

在开始具体备份操作前，我们先深入了解三个核心工具的基本用法和参数，确保大家对命令有清晰认识。以下是 `scp`、`mysqldump` 和 `mysqlbinlog` 的常用参数表格，附带语法解释和简单示例，方便查询和学习。

### 1. scp（文件传输工具）
`scp` 用于通过 SSH 协议安全传输文件，类似“远程复制粘贴”，是异地备份中传输文件的重要工具。

#### 参数表格
| 参数          | 说明                                   | 示例                                      |
|--------------|---------------------------------------|------------------------------------------|
| `-P`         | 指定 SSH 端口（默认 22），当目标服务器使用非默认端口时使用 | `scp -P 2222 file.txt user@host:/path`   |
| `-r`         | 递归传输目录及其内容，适用于传输整个文件夹 | `scp -r /local/dir user@host:/remote/dir`|
| `-C`         | 启用压缩，加速传输，适合大文件或慢网络 | `scp -C file.txt user@host:/path`        |
| `-i`         | 指定私钥文件，用于身份验证，替代密码登录 | `scp -i ~/.ssh/key file.txt user@host:/path` |

#### 语法解释
- **基本语法**：`scp [选项] 源文件 目标地址`
  - `源文件`：可以是本地文件/目录，也可以是远程服务器上的文件/目录。
  - `目标地址`：格式为 `用户名@目标IP:目标目录`，表示文件要传输到的位置。
  - `选项`：如 `-P`、`-r` 等，用于调整传输行为。
- **上传文件**：`scp 本地文件 用户名@目标IP:目标目录`
  - 表示将本地文件上传到远程服务器的指定目录。
- **下载文件**：`scp 用户名@目标IP:远程文件 本地目录`
  - 表示从远程服务器下载文件到本地指定目录。

#### 简单示例
1. **上传单个文件到远程服务器**：
   ```bash
   scp /home/user/test.txt root@192.168.110.5:/tmp/
   # 将本地 /home/user/test.txt 上传到远程服务器 192.168.110.5 的 /tmp/ 目录
   ```
2. **下载文件从远程服务器到本地**：
   ```bash
   scp root@192.168.110.5:/tmp/test.txt /home/user/downloads/
   # 从远程服务器 192.168.110.5 的 /tmp/test.txt 下载到本地 /home/user/downloads/ 目录
   ```
3. **使用非默认端口上传文件**：
   ```bash
   scp -P 2222 /home/user/test.txt root@192.168.110.5:/tmp/
   # 指定 SSH 端口为 2222，上传文件到远程服务器
   ```
4. **递归上传整个目录**：
   ```bash
   scp -r /home/user/backup root@192.168.110.5:/backup/remote/
   # 将本地 /home/user/backup 目录及其内容递归上传到远程服务器的 /backup/remote/ 目录
   ```

### 2. mysqldump（全量备份工具）
`mysqldump` 是 MySQL 官方提供的备份工具，用于生成数据库的 SQL 脚本文件，常用于全量备份。

#### 参数表格
| 参数                  | 说明                                   | 示例                                      |
|----------------------|---------------------------------------|------------------------------------------|
| `-u`                 | 指定用户名，用于连接 MySQL 数据库      | `mysqldump -u root`                      |
| `-p`                 | 指定密码（无空格），用于连接数据库      | `mysqldump -u root -p'yourpassword'`     |
| `--databases`        | 备份指定数据库，可以指定多个数据库      | `mysqldump --databases mydb`             |
| `--single-transaction` | 减少锁表影响（适用于 InnoDB 引擎），避免备份时阻塞业务 | `mysqldump --single-transaction`         |
| `--all-databases`    | 备份所有数据库，适用于多数据库环境      | `mysqldump --all-databases`              |
| `-R`                 | 备份存储过程和函数，适合复杂数据库      | `mysqldump -R`                           |
| `--triggers`         | 备份触发器，确保完整性                 | `mysqldump --triggers`                   |

#### 语法解释
- **基本语法**：`mysqldump [选项] [数据库名] > 输出文件.sql`
  - `[选项]`：如 `-u`、`-p` 等，用于指定连接信息和备份行为。
  - `[数据库名]`：指定要备份的数据库，若使用 `--all-databases` 则无需指定。
  - `> 输出文件.sql`：将备份内容重定向到指定文件，通常是 `.sql` 格式。
- **备份数据库**：`mysqldump -u 用户 -p'密码' --databases 数据库名 > 备份文件.sql`
  - 表示备份指定数据库，并将结果保存到本地文件。



#### 案例：MySQL 数据库备份与恢复（针对 employees 数据库）

##### 重要提示
- 确保您有足够的权限（如 root 用户）。
- 操作前建议在测试环境验证。
- 替换命令中的 `yourpassword` 和路径 `/backup/local/full/` 为实际值。


##### 1. 全量备份（不影响线上使用）
为了减少对线上数据库的影响，使用 `--single-transaction` 参数（适用于 InnoDB 存储引擎），确保备份过程中尽量不锁表。

**命令**：
```bash
mysqldump -u root -p'yourpassword' --single-transaction --all-databases > /backup/local/full/all_backup.sql
# 备份所有数据库，保存为 all_backup.sql，减少锁表影响
```

**说明**：
- `--single-transaction`：确保备份时不锁表，适合线上环境（InnoDB 表）。
- 备份文件保存到 `/backup/local/full/all_backup.sql`，请确保目录存在并有写入权限。

**验证备份**：
```bash
ls -lh /backup/local/full/
# 检查备份文件是否生成
```


##### 2. 全量恢复
全量恢复会将备份文件中的所有数据库恢复到当前 MySQL 实例，可能会覆盖现有数据，操作前务必备份当前数据。

**操作前备份当前数据**：
```bash
mysqldump -u root -p'yourpassword' --all-databases > /backup/local/full/current_backup.sql
# 备份当前数据库状态，防止数据丢失
```

**恢复命令**：
```bash
mysql -u root -p'yourpassword' < /backup/local/full/all_backup.sql
# 将备份文件导入，恢复所有数据库
```

**验证恢复**：
```sql
mysql -u root -p'yourpassword' -e "SHOW DATABASES;"
# 检查所有数据库是否恢复
```

##### 3. 指定 employees 数据库恢复
如果只想恢复 `employees` 数据库，可以使用单独备份的 `employees` 数据库文件。

###### 3.1 先备份 employees 数据库（可选）
如果没有单独的 `employees` 备份文件，可以先创建：
```bash
mysqldump -u root -p'yourpassword' --single-transaction --databases employees > /backup/local/full/employees_backup.sql
# 单独备份 employees 数据库
```

###### 3.2 恢复 employees 数据库
**命令**：
```bash
mysql -u root -p'yourpassword' < /backup/local/full/employees_backup.sql
# 将备份文件导入，恢复 employees 数据库
```

**说明**：
- 如果 `employees` 数据库已存在，可能会报错，需先删除（谨慎操作）：
  ```sql
  mysql -u root -p'yourpassword' -e "DROP DATABASE IF EXISTS employees;"
  # 删除现有数据库，注意会丢失当前数据
  ```
  然后再执行恢复：
  ```bash
  mysql -u root -p'yourpassword' < /backup/local/full/employees_backup.sql
  ```

**验证恢复**：
```sql
mysql -u root -p'yourpassword' -e "USE employees; SHOW TABLES;"
# 检查 employees 数据库的表是否恢复
```

#### 总结
- **全量备份**：使用 `--single-transaction` 参数，减少对线上影响，备份所有数据库到 `all_backup.sql`。
- **全量恢复**：直接导入 `all_backup.sql`，恢复所有数据库（操作前备份当前数据到 `current_backup.sql`）。
- **指定 employees 恢复**：单独备份或使用 `employees_backup.sql` 文件，导入恢复 `employees` 数据库。


### 3. mysqlbinlog（处理 binlog 文件工具）
`mysqlbinlog` 用于读取和回放 MySQL 的二进制日志文件（binlog），常用于增量恢复或查看数据库操作历史。

#### 参数表格
| 参数                  | 说明                                   | 示例                                      |
|----------------------|---------------------------------------|------------------------------------------|
| `--start-datetime`   | 从指定时间点开始读取日志，精确到秒      | `mysqlbinlog --start-datetime="2025-07-20 10:00:00"` |
| `--stop-datetime`    | 读取日志到指定时间点结束，精确到秒      | `mysqlbinlog --stop-datetime="2025-07-20 11:00:00"` |
| `--start-position`   | 从指定位置开始读取日志，精确到事件位置  | `mysqlbinlog --start-position=123`       |
| `--stop-position`    | 读取日志到指定位置结束，精确到事件位置  | `mysqlbinlog --stop-position=456`        |
| `-d`                 | 指定数据库，仅读取该数据库的相关日志    | `mysqlbinlog -d mydb`                    |

#### 语法解释
- **基本语法**：`mysqlbinlog [选项] binlog文件`
  - `[选项]`：如 `--start-datetime` 等，用于过滤日志内容。
  - `binlog文件`：指定要读取的二进制日志文件路径。
- **读取并回放 binlog**：`mysqlbinlog binlog文件 | mysql -u 用户 -p'密码'`
  - 表示将 binlog 文件内容转换为 SQL 语句，并通过 `mysql` 命令执行，恢复数据。
- **查看 binlog 内容**：`mysqlbinlog binlog文件 > 输出文件.txt`
  - 表示将 binlog 文件内容输出为可读文本，方便排查问题。

#### MySQL Binlog 数据恢复教案
**场景描述**
你是一名数据库管理员，在一次日常维护过程中，同事误执行了一条删除命令，导致`employees.departments`表中的部分重要数据被删除。现在需要通过binlog恢复这些数据。

##### 当前表状态
执行`SELECT * FROM employees.departments`查询，当前表中仅剩以下数据：

```
dept_no | dept_name
--------|------------
d011    | 123
d014    | 123123
d009    | Customer Service
d005    | Development
d002    | Finance
d003    | Human Resources
d001    | Marketing
d010    | mysql
d004    | Production
d006    | Quality Management
xx      | 测试123
```

##### 误删操作
同事执行的误删命令为：

```sql
DELETE FROM employees.departments WHERE dept_no IN ('d007', 'd008', 'd012', 'd013');
```

##### 误删数据
这条命令删除了以下部门数据：
- d007 (Sales)
- d008 (Research)
- d012 (Data Analytics)
- d013 (Legal)

##### 数据恢复步骤

* 步骤1：找到包含删除操作的binlog文件

   ```bash
   # 登录MySQL查看当前使用的binlog文件
   mysql -u root -p -e "SHOW MASTER STATUS;"

   # 或查看所有binlog文件列表
   mysql -u root -p -e "SHOW BINARY LOGS;"
   ```

   假设我们确定删除操作记录在`mysql-bin.000003`文件中。

* 步骤2：确定删除操作的时间范围

   ```bash
   # 查看binlog文件的大致内容和时间戳
   mysqlbinlog --base64-output=decode-rows -v /var/log/mysql/mysql-bin.000003 | head -n 100
   mysqlbinlog --base64-output=decode-rows -v /var/log/mysql/mysql-bin.000003 | tail -n 100
   ```

   假设我们确定删除操作发生在2025-07-24 15:30:00左右。

* 步骤3：提取相关时间段的binlog内容

   ```bash
   # 提取删除操作前后一段时间的binlog
   mysqlbinlog --base64-output=decode-rows -v --start-datetime="2025-07-24 21:00:00" --stop-datetime="2025-07-24 21:35:00" /var/log/mysql/mysql-bin.000003 > /tmp/delete_operation.txt
   ```

* 步骤4：在提取的binlog中找到删除操作

   ```bash
   # 在提取的文件中查找删除操作
   grep -A 10 -B 3 "DELETE FROM.*departments" /tmp/delete_operation.txt
   ```

   我们可能会看到类似以下内容：

   ```
   # at 4567
   #250724 15:30:12 server id 1  end_log_pos 4620 CRC32 0xa1b2c3d4     Delete_rows: table id 123 flags: STMT_END_F
   ### DELETE FROM `employees`.`departments`
   ### WHERE
   ###   @1='d007'
   ###   @2='Sales'

   # at 4620
   #250724 15:30:12 server id 1  end_log_pos 4673 CRC32 0xd4c3b2a1     Delete_rows: table id 123 flags: STMT_END_F
   ### DELETE FROM `employees`.`departments`
   ### WHERE
   ###   @1='d008'
   ###   @2='Research'

   # 以此类推...
   #250724 21:01:31 server id 1  end_log_pos 8654 CRC32 0xa40c1d11         Xid = 11714
   # 如果你用我的命令查到了最后的at，这个就是结束的位置
   # 你的删除是在8654 这里提交到数据库的
   COMMIT/*!*/;
   # at 8654
   ```

* 步骤5：确定准确的position范围
   通过上述输出，确定删除操作的准确position范围，例如从4567到8654。

   ```bash
   # 根据确定的position范围再次提取
   mysqlbinlog --base64-output=decode-rows -v --start-position=4567 --stop-position=8654 /var/log/mysql/mysql-bin.000789 > /tmp/exact_delete_operation.txt
   ```

* 步骤6：手动编写恢复SQL（CHAGPT）

   根据提取的Delete_rows事件，手动编写INSERT语句：哈哈，把你的日志cat一下，给chagpt绝对稳稳的
   # AI给我的，注意，注意，生成的SQL，到公司里面你记得给领导看，别傻乎乎的执行，想死抓紧离职
   ```sql
   # AI给我的，注意，注意，生成的SQL，到公司里面你记得给领导看，别傻乎乎的执行，想死抓紧离职
   INSERT INTO employees.departments VALUES ('d007', 'Sales');
   INSERT INTO employees.departments VALUES ('d008', 'Research');
   INSERT INTO employees.departments VALUES ('d012', 'Data Analytics');
   INSERT INTO employees.departments VALUES ('d013', 'Legal');
   ```

---