# ProxySQL 配置命令总结表格

| 命令 | 作用对象 | 功能描述 | 应用场景 |
|------|---------|---------|---------|
| `LOAD MYSQL USERS TO RUNTIME;` | 用户配置 | 将内存表中的用户配置应用到运行环境 | 修改用户账号、权限、密码后 |
| `SAVE MYSQL USERS TO DISK;` | 用户配置 | 将内存表中的用户配置持久化到磁盘 | 确保用户配置在重启后不丢失 |
| `LOAD MYSQL VARIABLES TO RUNTIME;` | 系统变量 | 将内存表中的系统变量应用到运行环境 | 修改连接池大小、超时设置等参数后 |
| `SAVE MYSQL VARIABLES TO DISK;` | 系统变量 | 将内存表中的系统变量持久化到磁盘 | 确保系统变量配置在重启后不丢失 |
| `LOAD MYSQL QUERY RULES TO RUNTIME;` | 查询规则 | 将内存表中的查询规则应用到运行环境 | 修改查询路由、缓存、重写规则后 |
| `SAVE MYSQL QUERY RULES TO DISK;` | 查询规则 | 将内存表中的查询规则持久化到磁盘 | 确保查询规则在重启后不丢失 |
| `LOAD MYSQL SERVERS TO RUNTIME;` | 服务器配置 | 将内存表中的服务器配置应用到运行环境 | 添加/删除服务器、修改主机组后 |
| `SAVE MYSQL SERVERS TO DISK;` | 服务器配置 | 将内存表中的服务器配置持久化到磁盘 | 确保服务器配置在重启后不丢失 |

## 配置流程

所有 ProxySQL 配置遵循相同的三层架构流程：

1. **修改配置**：在内存表中修改配置 (`mysql_users`, `mysql_variables`, `mysql_query_rules`, `mysql_servers`)
2. **应用到运行时**：执行 `LOAD ... TO RUNTIME;` 命令使配置生效
3. **持久化到磁盘**：执行 `SAVE ... TO DISK;` 命令确保配置在重启后保留

这种设计允许安全地测试配置更改，并在需要时轻松回滚。