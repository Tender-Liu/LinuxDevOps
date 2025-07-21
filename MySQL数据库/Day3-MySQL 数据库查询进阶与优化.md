# 第三天教案：MySQL 数据库进阶

## 第一部分：高级查询（1.5 小时）
- **目标：** 掌握 MySQL 高级查询语法，包括子查询、连接查询、分组聚合和窗口函数。
- **时间分配：** 理论讲解（0.8 小时），案例演示与实践（0.7 小时）。
- **数据源：** 使用 MySQL 官方提供的 `employees` 数据库（一个模拟公司员工数据的练习库）。

### 1.1 `employees` 数据库表结构介绍
为了方便学员在学习 SQL 时有直观的对照，我先列出 `employees` 数据库的主要表结构和字段说明。以下是核心表的结构，数据量较大（约 30 万员工记录），适合用来演示复杂查询。

| 表名            | 主要字段                                      | 字段说明                          | 数据量（约）       |
|----------------|----------------------------------------------|----------------------------------|-------------------|
| `employees`    | `emp_no`, `birth_date`, `first_name`, `last_name`, `gender`, `hire_date` | 员工基本信息：编号、出生日期、姓名、性别、入职日期 | 30 万条          |
| `salaries`     | `emp_no`, `salary`, `from_date`, `to_date`   | 员工薪资历史：员工编号、薪资、起止日期 | 280 万条         |
| `titles`       | `emp_no`, `title`, `from_date`, `to_date`    | 员工职位历史：员工编号、职位、起止日期 | 44 万条          |
| `departments`  | `dept_no`, `dept_name`                      | 部门信息：部门编号、部门名称      | 9 条             |
| `dept_emp`     | `emp_no`, `dept_no`, `from_date`, `to_date`  | 员工部门关系：员工编号、部门编号、起止日期 | 33 万条          |
| `dept_manager` | `emp_no`, `dept_no`, `from_date`, `to_date`  | 部门经理关系：经理编号、部门编号、起止日期 | 24 条            |

- **说明：** `employees` 数据库模拟了一个公司的员工管理场景，包含员工信息、薪资、职位、部门等多维度数据，非常适合练习复杂查询。
- **小白提示：** 可以把 `employees` 想象成一个大公司的 HR 系统，里面存了员工档案、工资单、部门分配等信息，我们通过 SQL 从中提取想要的数据。

### 1.2 高级查询语法总览与学习用途
在开始具体学习之前，我先总结一下本部分将要学习的高级查询语法，以及学习它们的实际用途和应用场景，帮助你理解“学了有什么用”。

| 语法名称         | 功能简介                                      | 实际应用场景                          | 学了有什么用                          |
|------------------|----------------------------------------------|--------------------------------------|--------------------------------------|
| 子查询（Subquery） | 在查询中嵌套另一个查询，用于分步获取中间结果 | 筛选复杂条件，如“找到薪资高于某人的人” | 解决多步骤数据筛选问题，提升逻辑拆解能力 |
| 连接查询（JOIN）  | 合并多个表的数据，基于共同字段关联          | 关联员工和部门，查出员工所属部门     | 掌握多表数据整合，常见于报表生成       |
| 分组聚合（GROUP BY 与 HAVING） | 按某字段分组，结合统计函数（如 COUNT、AVG），可用 HAVING 筛选分组结果 | 统计每个部门的员工人数或平均薪资，筛选高薪部门 | 用于数据统计分析，常见于商业报表       |
| 窗口函数（Window Function） | 对数据排名、累加等操作，不改变原始数据 | 按薪资排名，或计算部门内排名         | 高级分析工具，适合数据分析岗位         |

- **学习这些语法的意义：**
  - **职场需求：** 这些高级语法是数据分析、数据库管理、后端开发等岗位的核心技能，掌握它们能让你在处理复杂数据需求时游刃有余。
  - **实际场景：** 比如在电商公司，你可以用 JOIN 查询用户订单和商品信息；用 GROUP BY 统计各品类销量；用子查询筛选高价值用户。
  - **思维提升：** 学习高级 SQL 能锻炼结构化思维，帮助你将复杂问题拆解为小步骤，逐步解决。
- **小白提示：** 想象自己是公司数据管理员，这些工具就像“数据挖掘机”，能帮你从海量信息中挖出有用的东西，做出聪明决策。

### 1.3 高级查询语法详细讲解与分步拆解
以下是 MySQL 中常用的高级查询语法，我会先逐一介绍每个语法的用途、基本规则和应用场景，然后针对每个语法提供至少 3 个基于 `employees` 数据库的示例 SQL 语句，并分步骤拆解代码逻辑，确保你能看懂每个部分的作用。所有语法都会用通俗语言和比喻解释，帮助小白理解。

#### 1.3.1 子查询（Subquery）
- **介绍：**
  - 子查询是嵌套在另一个查询中的查询，通常用于 WHERE 或 FROM 子句中，返回一个中间结果供外层查询使用。
  - 比喻：子查询就像“先问一个小问题，得到答案后再回答大问题”，比如先查出某个部门的员工编号，再用这些编号查薪资。
  - 分类：单行子查询（返回一行）、多行子查询（返回多行）、相关子查询（与外层查询相关）。
  - **应用场景：** 当你需要分步筛选数据时，比如“找到薪资高于某个特定员工的所有人”，子查询能帮你先找到参照值，再做比较。
- **示例与分步拆解：**
  1. **单行子查询 - 查找薪资高于某个员工的员工信息**
     - **需求：** 查找薪资高于员工编号 10001 当前薪资的所有员工信息。
     - **思考步骤：**
       - 第一步：先找到 10001 号员工的当前薪资是多少。
       - 第二步：用这个薪资值去筛选其他员工，找出薪资更高的人。
       - 第三步：显示这些员工的编号、姓名等信息。
     - **SQL 代码与拆解：**
       ```sql
       SELECT emp_no, first_name, last_name  -- 第三步：显示员工编号、姓名
       FROM employees
       WHERE emp_no IN (
           SELECT emp_no  -- 第二步：找出薪资高于 10001 号员工的员工编号
           FROM salaries
           WHERE salary > (
               SELECT salary  -- 第一步：找到 10001 号员工的当前薪资
               FROM salaries
               WHERE emp_no = 10001 AND to_date = '9999-01-01'  -- to_date 为最大值表示当前有效
           )
           AND to_date = '9999-01-01'  -- 只查当前薪资
       );
       ```
       - **结果解释：** 最内层查询先得到 10001 号员工的薪资，中间层查询找出薪资高于这个值的所有员工编号，最外层查询显示这些员工的详细信息。
  2. **多行子查询 - 查找在某个部门工作过的员工**
     - **需求：** 查找曾在 'd001' 部门（市场部）工作过的所有员工信息。
     - **思考步骤：**
       - 第一步：从部门关系表中找到所有在 'd001' 部门工作过的员工编号。
       - 第二步：用这些编号去员工表中查找对应的姓名等信息。
     - **SQL 代码与拆解：**
       ```sql
       SELECT emp_no, first_name, last_name  -- 第二步：根据员工编号显示详细信息
       FROM employees
       WHERE emp_no IN (
           SELECT emp_no  -- 第一步：找到所有在 'd001' 部门工作过的员工编号
           FROM dept_emp
           WHERE dept_no = 'd001'  -- 市场部编号
       );
       ```
       - **结果解释：** 内层查询返回一个员工编号列表，外层查询根据列表显示对应的员工信息。
  3. **相关子查询 - 查找每个员工的最新薪资**
     - **需求：** 查找每个员工的最新薪资记录。
     - **思考步骤：**
       - 第一步：遍历员工表中的每个员工。
       - 第二步：对每个员工，检查薪资表中是否存在当前有效的薪资记录。
       - 第三步：如果存在，显示员工信息和薪资。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, s.salary  -- 第三步：显示员工信息和薪资
       FROM employees e
       WHERE EXISTS (
           SELECT 1  -- 第二步：检查是否存在当前薪资记录
           FROM salaries s
           WHERE s.emp_no = e.emp_no  -- 第一步：与外层员工编号关联
           AND s.to_date = '9999-01-01'  -- 只取当前有效的薪资
       );
       ```
       - **结果解释：** EXISTS 检查每个员工是否有当前薪资记录，比直接 JOIN 效率更高。

#### 1.3.2 连接查询（JOIN）
- **介绍：**
  - JOIN 用于连接多个表，基于共同字段（如员工编号）合并数据，常见类型有 INNER JOIN、LEFT JOIN、RIGHT JOIN。
  - 比喻：JOIN 就像“把两张表格拼在一起”，比如把员工表和薪资表通过员工编号对齐，查出每个人的工资。
  - 注意：JOIN 性能消耗较大，需合理选择连接条件。
  - **应用场景：** 当你需要从多个表中整合信息时，比如查询员工姓名和所在部门名称，JOIN 是必备工具。
- **示例与分步拆解：**
  1. **INNER JOIN - 查询员工当前薪资**
     - **需求：** 查询员工基本信息及其当前薪资。
     - **思考步骤：**
       - 第一步：从员工表（employees）获取员工基本信息。
       - 第二步：从薪资表（salaries）获取薪资信息，通过员工编号关联两表。
       - 第三步：筛选出当前有效的薪资记录。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, s.salary  -- 第三步：显示员工信息和薪资
       FROM employees e
       INNER JOIN salaries s ON e.emp_no = s.emp_no  -- 第二步：通过 emp_no 连接两表
       WHERE s.to_date = '9999-01-01';  -- 第一步：只取当前有效薪资
       ```
       - **结果解释：** INNER JOIN 只返回两表都匹配的记录，查出员工信息和当前薪资。
  2. **LEFT JOIN - 查询所有员工及其部门（包括无部门员工）**
     - **需求：** 查询所有员工及其所属部门，即使某些员工未分配部门。
     - **思考步骤：**
       - 第一步：从员工表获取所有员工信息。
       - 第二步：通过员工编号连接部门关系表（dept_emp）。
       - 第三步：再连接部门信息表（departments）获取部门名称。
       - 第四步：使用 LEFT JOIN 保留所有员工，即使没有部门。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, d.dept_name  -- 第四步：显示员工信息和部门名称
       FROM employees e
       LEFT JOIN dept_emp de ON e.emp_no = de.emp_no  -- 第二步：连接员工和部门关系表
       LEFT JOIN departments d ON de.dept_no = d.dept_no;  -- 第三步：再连接部门信息表
       ```
       - **结果解释：** LEFT JOIN 保留 employees 表所有记录，即使没有部门也显示（dept_name 为 NULL）。
  3. **RIGHT JOIN - 查询所有部门及其经理（包括无经理部门）**
     - **需求：** 查询所有部门及其经理信息，即使某些部门无经理。
     - **思考步骤：**
       - 第一步：从部门表（departments）获取所有部门信息。
       - 第二步：通过部门编号连接经理关系表（dept_manager）。
       - 第三步：再通过员工编号连接员工表（employees）获取经理姓名。
       - 第四步：使用 RIGHT JOIN 保留所有部门，即使无经理。
     - **SQL 代码与拆解：**
       ```sql
       SELECT d.dept_no, d.dept_name, e.first_name, e.last_name  -- 第四步：显示部门和经理信息
       FROM departments d
       RIGHT JOIN dept_manager dm ON d.dept_no = dm.dept_no  -- 第二步：连接部门和经理关系表
       RIGHT JOIN employees e ON dm.emp_no = e.emp_no;  -- 第三步：再连接员工表
       ```
       - **结果解释：** RIGHT JOIN 保留 departments 表所有记录，即使无经理也显示部门信息。

#### 1.3.3 分组聚合（GROUP BY 与 HAVING）
- **介绍：**
  - GROUP BY 用于按某字段分组，结合聚合函数（如 COUNT、SUM、AVG）计算每组的结果。
  - HAVING 是 GROUP BY 的筛选条件，用于在分组后对聚合结果进行过滤，类似于 WHERE 但作用于分组后的数据。
  - 比喻：GROUP BY 就像“把数据按类别打包统计”，比如按部门统计员工人数；HAVING 就像“从统计结果中挑出符合条件的类别”，比如只看人数超过 100 的部门。
  - 注意：WHERE 在分组前过滤原始数据，HAVING 在分组后过滤聚合结果，两者不可混淆。
  - **应用场景：** 用于数据统计，比如公司想知道每个部门的员工人数或平均薪资，并筛选出人数较多或薪资较高的部门，GROUP BY 和 HAVING 是最佳选择。
- **示例与分步拆解：**
  1. **按部门统计员工人数（使用 GROUP BY）**
     - **需求：** 统计每个部门当前员工人数。
     - **思考步骤：**
       - 第一步：连接部门表（departments）和部门关系表（dept_emp）。
       - 第二步：筛选当前在职员工（to_date 为 '9999-01-01'）。
       - 第三步：按部门名称分组，统计每组人数。
     - **SQL 代码与拆解：**
       ```sql
       SELECT d.dept_name, COUNT(*) AS emp_count  -- 第三步：按部门显示员工人数
       FROM departments d
       JOIN dept_emp de ON d.dept_no = de.dept_no  -- 第一步：连接部门和员工关系表
       WHERE de.to_date = '9999-01-01'  -- 第二步：只统计当前在职员工
       GROUP BY d.dept_name;  -- 按部门名称分组
       ```
       - **结果解释：** 按部门分组，计算每个部门当前员工数量。
  2. **按职位统计平均薪资（使用 GROUP BY）**
     - **需求：** 统计每个职位的平均薪资（当前有效）。
     - **思考步骤：**
       - 第一步：连接职位表（titles）和薪资表（salaries）。
       - 第二步：筛选当前有效的职位和薪资记录。
       - 第三步：按职位分组，计算每组平均薪资。
     - **SQL 代码与拆解：**
       ```sql
       SELECT t.title, AVG(s.salary) AS avg_salary  -- 第三步：按职位显示平均薪资
       FROM titles t
       JOIN salaries s ON t.emp_no = s.emp_no  -- 第一步：连接职位和薪资表
       WHERE t.to_date = '9999-01-01'  -- 第二步：只取当前职位
       AND s.to_date = '9999-01-01'  -- 第二步：只取当前薪资
       GROUP BY t.title;  -- 按职位分组
       ```
       - **结果解释：** 按职位分组，计算每个职位的平均薪资。
  3. **按部门筛选高薪资部门（使用 GROUP BY 与 HAVING）**
     - **需求：** 统计当前每个部门的平均薪资，筛选平均薪资大于 60000 的部门。
     - **思考步骤：**
       - 第一步：连接部门表、部门关系表和薪资表。
       - 第二步：筛选当前有效的部门分配和薪资记录。
       - 第三步：按部门分组，计算平均薪资。
       - 第四步：用 HAVING 筛选平均薪资大于 60000 的部门。
     - **SQL 代码与拆解：**
       ```sql
       SELECT d.dept_name, AVG(s.salary) AS avg_salary  -- 第四步：显示高薪资部门及其平均薪资
       FROM departments d
       JOIN dept_emp de ON d.dept_no = de.dept_no  -- 第一步：连接部门和员工关系表
       JOIN salaries s ON de.emp_no = s.emp_no  -- 第一步：连接薪资表
       WHERE de.to_date = '9999-01-01'  -- 第二步：当前部门分配
       AND s.to_date = '9999-01-01'  -- 第二步：当前薪资
       GROUP BY d.dept_name  -- 第三步：按部门分组
       HAVING avg_salary > 60000;  -- 第四步：筛选平均薪资大于 60000 的部门
       ```
       - **结果解释：** HAVING 在分组后对聚合结果进行筛选，找出平均薪资高于 60000 的部门，区别于 WHERE 的原始数据过滤。

#### 1.3.4 窗口函数（Window Function）
- **介绍：**
  - 窗口函数在 MySQL 8.0+ 中支持，用于在查询中对数据进行排名、累加等操作，而不影响原始数据。
  - 比喻：窗口函数就像“在表格每行旁边加一列计算结果”，比如给每个员工按薪资排名。
  - 常见函数：RANK()、ROW_NUMBER()、SUM() OVER() 等。
  - **应用场景：** 用于高级数据分析，比如给员工薪资排名，或计算部门内排名，常用于数据分析岗位。
- **示例与分步拆解：**
  1. **按薪资排名**
     - **需求：** 给当前薪资按降序排名。
     - **思考步骤：**
       - 第一步：连接员工表和薪资表，获取当前薪资。
       - 第二步：使用 RANK() 函数按薪资降序排名。
       - 第三步：显示员工信息、薪资和排名。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, s.salary,  -- 第三步：显示员工信息、薪资和排名
              RANK() OVER (ORDER BY s.salary DESC) AS salary_rank  -- 第二步：薪资排名，相同值同名次
       FROM employees e
       JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接获取当前薪资
       WHERE s.to_date = '9999-01-01';  -- 第一步：只取当前薪资
       ```
       - **结果解释：** RANK() 按薪资降序排名，相同薪资同名次。
  2. **按部门内薪资排名**
     - **需求：** 按部门内薪资降序排名。
     - **思考步骤：**
       - 第一步：连接员工表、薪资表、部门关系表和部门表，获取当前薪资和部门信息。
       - 第二步：使用 ROW_NUMBER() 函数，在每个部门内按薪资降序排名。
       - 第三步：显示员工信息、部门、薪资和排名。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, d.dept_name, s.salary,  -- 第三步：显示信息和排名
              ROW_NUMBER() OVER (PARTITION BY d.dept_name ORDER BY s.salary DESC) AS dept_salary_rank  -- 第二步：部门内排名
       FROM employees e
       JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接薪资表
       JOIN dept_emp de ON e.emp_no = de.emp_no  -- 第一步：连接部门关系表
       JOIN departments d ON de.dept_no = d.dept_no  -- 第一步：连接部门表
       WHERE s.to_date = '9999-01-01'  -- 第一步：当前薪资
       AND de.to_date = '9999-01-01';  -- 第一步：当前部门
       ```
       - **结果解释：** PARTITION BY 按部门分组，ROW_NUMBER() 在每个部门内按薪资排名。
  3. **计算累计薪资**
     - **需求：** 按薪资升序计算累计薪资总和。
     - **思考步骤：**
       - 第一步：连接员工表和薪资表，获取当前薪资。
       - 第二步：使用 SUM() OVER() 函数计算累计薪资。
       - 第三步：显示员工信息、薪资和累计薪资。
     - **SQL 代码与拆解：**
       ```sql
       SELECT e.emp_no, e.first_name, e.last_name, s.salary,  -- 第三步：显示信息和累计薪资
              SUM(s.salary) OVER (ORDER BY s.salary) AS cumulative_salary  -- 第二步：累计薪资
       FROM employees e
       JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接获取当前薪资
       WHERE s.to_date = '9999-01-01';  -- 第一步：当前薪资
       ```
       - **结果解释：** SUM() OVER() 计算从最低薪资到当前行的累计总和。

## 第二部分：高级查询作业题（自学与实践）
为了帮助学员巩固所学内容，以下是 12 个基于 `employees` 数据库的作业题，涵盖子查询、JOIN、分组聚合和窗口函数。每个题目包含需求描述、思考步骤拆解、SQL 实现代码及详细注释，供学员练习和参考。

### 作业题 1：查找薪资高于员工编号 10002 的员工信息（子查询）
- **需求：** 查找薪资高于员工编号 10002 当前薪资的所有员工信息。
- **思考步骤：**
  - 第一步：找到 10002 号员工的当前薪资。
  - 第二步：用这个薪资值筛选其他员工，找出薪资更高的人。
  - 第三步：显示这些员工的编号、姓名。
- **SQL 实现：**
  ```sql
  SELECT emp_no, first_name, last_name  -- 第三步：显示员工编号、姓名
  FROM employees
  WHERE emp_no IN (
      SELECT emp_no  -- 第二步：找出薪资高于 10002 号员工的员工编号
      FROM salaries
      WHERE salary > (
          SELECT salary  -- 第一步：找到 10002 号员工的当前薪资
          FROM salaries
          WHERE emp_no = 10002 AND to_date = '9999-01-01'  -- 当前有效薪资
      )
      AND to_date = '9999-01-01'  -- 只查当前薪资
  );
  ```

### 作业题 2：查找曾在 'd002' 部门工作过的员工（子查询）
- **需求：** 查找曾在 'd002' 部门（财务部）工作过的所有员工信息。
- **思考步骤：**
  - 第一步：从部门关系表中找到所有在 'd002' 部门工作过的员工编号。
  - 第二步：用这些编号去员工表中查找对应的姓名等信息。
- **SQL 实现：**
  ```sql
  SELECT emp_no, first_name, last_name  -- 第二步：根据员工编号显示详细信息
  FROM employees
  WHERE emp_no IN (
      SELECT emp_no  -- 第一步：找到所有在 'd002' 部门工作过的员工编号
      FROM dept_emp
      WHERE dept_no = 'd002'  -- 财务部编号
  );
  ```

### 作业题 3：查找有当前薪资记录的员工（子查询）
- **需求：** 查找所有有当前薪资记录的员工信息。
- **思考步骤：**
  - 第一步：遍历员工表中的每个员工。
  - 第二步：检查每个员工在薪资表中是否有当前有效薪资记录。
  - 第三步：显示符合条件的员工信息。
- **SQL 实现：**
  ```sql
  SELECT e.emp_no, e.first_name, e.last_name  -- 第三步：显示员工信息
  FROM employees e
  WHERE EXISTS (
      SELECT 1  -- 第二步：检查是否存在当前薪资记录
      FROM salaries s
      WHERE s.emp_no = e.emp_no  -- 第一步：与外层员工编号关联
      AND s.to_date = '9999-01-01'  -- 只取当前有效的薪资
  );
  ```

### 作业题 4：查询员工及其当前职位（INNER JOIN）
- **需求：** 查询员工基本信息及其当前职位。
- **思考步骤：**
  - 第一步：从员工表获取员工基本信息。
  - 第二步：通过员工编号连接职位表（titles）。
  - 第三步：筛选当前有效的职位记录。
- **SQL 实现：**
  ```sql
  SELECT e.emp_no, e.first_name, e.last_name, t.title  -- 第三步：显示员工信息和职位
  FROM employees e
  INNER JOIN titles t ON e.emp_no = t.emp_no  -- 第二步：通过 emp_no 连接两表
  WHERE t.to_date = '9999-01-01';  -- 第一步：只取当前有效职位
  ```

### 作业题 5：查询所有员工及其部门信息（LEFT JOIN）
- **需求：** 查询所有员工及其所属部门信息，即使某些员工未分配部门。
- **思考步骤：**
  - 第一步：从员工表获取所有员工信息。
  - 第二步：通过员工编号连接部门关系表（dept_emp）。
  - 第三步：再连接部门信息表（departments）获取部门名称。
  - 第四步：使用 LEFT JOIN 保留所有员工。
- **SQL 实现：**
  ```sql
  SELECT e.emp_no, e.first_name, e.last_name, d.dept_name  -- 第四步：显示员工信息和部门名称
  FROM employees e
  LEFT JOIN dept_emp de ON e.emp_no = de.emp_no  -- 第二步：连接员工和部门关系表
  LEFT JOIN departments d ON de.dept_no = d.dept_no;  -- 第三步：再连接部门信息表
  ```

### 作业题 6：查询所有部门及其当前经理（RIGHT JOIN）
- **需求：** 查询所有部门及其当前经理信息，即使某些部门无经理。
- **思考步骤：**
  - 第一步：从部门表获取所有部门信息。
  - 第二步：通过部门编号连接经理关系表（dept_manager）。
  - 第三步：再通过员工编号连接员工表获取经理姓名。
  - 第四步：使用 RIGHT JOIN 保留所有部门。
- **SQL 实现：**
  ```sql
  SELECT d.dept_no, d.dept_name, e.first_name, e.last_name  -- 第四步：显示部门和经理信息
  FROM departments d
  RIGHT JOIN dept_manager dm ON d.dept_no = dm.dept_no  -- 第二步：连接部门和经理关系表
  RIGHT JOIN employees e ON dm.emp_no = e.emp_no;  -- 第三步：再连接员工表
  ```

### 作业题 7：统计每个部门的当前员工人数（GROUP BY）
- **需求：** 统计每个部门当前员工人数。
- **思考步骤：**
  - 第一步：连接部门表和部门关系表。
  - 第二步：筛选当前在职员工。
  - 第三步：按部门编号分组，统计人数。
- **SQL 实现：**
  ```sql
  SELECT d.dept_no, d.dept_name, COUNT(*) AS emp_count  -- 第三步：按部门显示员工人数
  FROM departments d
  JOIN dept_emp de ON d.dept_no = de.dept_no  -- 第一步：连接部门和员工关系表
  WHERE de.to_date = '9999-01-01'  -- 第二步：只统计当前在职员工
  GROUP BY d.dept_no, d.dept_name;  -- 按部门分组
  ```

### 作业题 8：统计每个职位的员工人数（GROUP BY）
- **需求：** 统计每个职位的当前员工人数。
- **思考步骤：**
  - 第一步：从职位表获取职位信息。
  - 第二步：筛选当前有效的职位记录。
  - 第三步：按职位分组，统计人数。
- **SQL 实现：**
  ```sql
  SELECT t.title, COUNT(*) AS emp_count  -- 第三步：按职位显示员工人数
  FROM titles t
  WHERE t.to_date = '9999-01-01'  -- 第二步：只取当前职位
  GROUP BY t.title;  -- 第一步：按职位分组
  ```

### 作业题 9：筛选平均薪资大于 70000 的部门（GROUP BY + HAVING）
- **需求：** 统计当前每个部门的平均薪资，筛选平均薪资大于 70000 的部门。
- **思考步骤：**
  - 第一步：连接部门表、部门关系表和薪资表。
  - 第二步：筛选当前有效的部门分配和薪资记录。
  - 第三步：按部门分组，计算平均薪资。
  - 第四步：用 HAVING 筛选平均薪资大于 70000 的部门。
- **SQL 实现：**
  ```sql
  SELECT d.dept_name, AVG(s.salary) AS avg_salary  -- 第四步：显示高薪资部门及其平均薪资
  FROM departments d
  JOIN dept_emp de ON d.dept_no = de.dept_no  -- 第一步：连接部门和员工关系表
  JOIN salaries s ON de.emp_no = s.emp_no  -- 第一步：连接薪资表
  WHERE de.to_date = '9999-01-01'  -- 第二步：当前部门分配
  AND s.to_date = '9999-01-01'  -- 第二步：当前薪资
  GROUP BY d.dept_name  -- 第三步：按部门分组
  HAVING avg_salary > 70000;  -- 第四步：筛选平均薪资大于 70000 的部门
  ```

### 作业题 10：按薪资降序排名前 10 名（窗口函数）
- **需求：** 给当前薪资按降序排名，显示前 10 名员工信息。
- **思考步骤：**
  - 第一步：连接员工表和薪资表，获取当前薪资。
  - 第二步：使用 RANK() 函数按薪资降序排名。
  - 第三步：显示员工信息、薪资和排名，限制前 10 名。
- **SQL 实现：**
  ```sql
  SELECT e.emp_no, e.first_name, e.last_name, s.salary,  -- 第三步：显示员工信息、薪资和排名
         RANK() OVER (ORDER BY s.salary DESC) AS salary_rank  -- 第二步：薪资排名
  FROM employees e
  JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接获取当前薪资
  WHERE s.to_date = '9999-01-01'  -- 第一步：只取当前薪资
  LIMIT 10;  -- 第三步：限制前 10 名
  ```

### 作业题 11：按部门内薪资排名前 3 名（窗口函数）
- **需求：** 按部门内薪资降序排名，显示每个部门薪资前 3 名的员工信息。
- **思考步骤：**
  - 第一步：连接员工表、薪资表、部门关系表和部门表，获取当前薪资和部门信息。
  - 第二步：使用 ROW_NUMBER() 函数，在每个部门内按薪资降序排名。
  - 第三步：筛选排名前 3 的员工，显示信息。
- **SQL 实现：**
  ```sql
  SELECT emp_no, first_name, last_name, dept_name, salary, dept_salary_rank  -- 第三步：显示信息和排名
  FROM (
      SELECT e.emp_no, e.first_name, e.last_name, d.dept_name, s.salary,
             ROW_NUMBER() OVER (PARTITION BY d.dept_name ORDER BY s.salary DESC) AS dept_salary_rank  -- 第二步：部门内排名
      FROM employees e
      JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接薪资表
      JOIN dept_emp de ON e.emp_no = de.emp_no  -- 第一步：连接部门关系表
      JOIN departments d ON de.dept_no = d.dept_no  -- 第一步：连接部门表
      WHERE s.to_date = '9999-01-01'  -- 第一步：当前薪资
      AND de.to_date = '9999-01-01'  -- 第一步：当前部门
  ) ranked
  WHERE dept_salary_rank <= 3;  -- 第三步：筛选每个部门前 3 名
  ```

### 作业题 12：计算薪资升序累计总和（窗口函数）
- **需求：** 按薪资升序计算累计薪资总和，显示前 20 条记录。
- **思考步骤：**
  - 第一步：连接员工表和薪资表，获取当前薪资。
  - 第二步：使用 SUM() OVER() 函数计算累计薪资。
  - 第三步：显示员工信息、薪资和累计薪资，限制前 20 条。
- **SQL 实现：**
  ```sql
  SELECT e.emp_no, e.first_name, e.last_name, s.salary,  -- 第三步：显示信息和累计薪资
         SUM(s.salary) OVER (ORDER BY s.salary) AS cumulative_salary  -- 第二步：累计薪资
  FROM employees e
  JOIN salaries s ON e.emp_no = s.emp_no  -- 第一步：连接获取当前薪资
  WHERE s.to_date = '9999-01-01'  -- 第一步：当前薪资
  LIMIT 20;  -- 第三步：限制前 20 条记录
  ```

---

好的，我会根据你的要求，编写第二阶段的教案，专注于索引的相关内容。在教案中，我会先详细介绍索引的类型、作用和特点，用通俗的比喻和描述帮助理解；然后提到索引会增加数据库的存储空间和内存使用；接着说明如何删除 `employees` 数据库中已有的索引（因为官方表确实默认有索引），并提供查看索引的命令；最后通过案例演示索引的创建和效果，并提供相应的观察命令。

---

## 第二部分：索引基础与应用（1.5 小时）
- **目标：** 理解索引的作用、类型及其在查询优化中的应用，掌握如何创建、查看和删除索引。
- **时间分配：** 理论讲解（0.7 小时），案例演示与实践（0.8 小时）。
- **数据源：** 继续使用 MySQL 官方提供的 `employees` 数据库。

### 2.1 索引的基本概念与作用
- **什么是索引？**
  - 索引（Index）是数据库中一种特殊的数据结构，用于加速数据查询操作。它就像一本书的目录，通过目录你可以快速找到特定章节，而不需要一页页翻书。
  - 比喻：没有索引的数据库就像一本没有目录的书，查找内容时需要从头到尾扫描（全表扫描）；而有了索引，数据库可以直接“跳”到目标数据，查询速度大幅提升。
- **索引的作用：**
  - **加速查询：** 特别是在 WHERE 条件、JOIN 连接、ORDER BY 排序等操作中，索引能显著减少扫描的数据量。
  - **减少资源消耗：** 降低 CPU 和磁盘 I/O 的使用，尤其在大表（比如 `employees` 表的 30 万条记录）中效果明显。
- **索引的代价：**
  - **增加存储空间和内存使用：** 索引本身是额外的数据结构，存储在磁盘上，会占用额外的空间；同时，数据库运行时可能会将部分索引加载到内存中，增加内存使用。
  - **写入性能下降：** 每次插入、更新或删除数据时，数据库需要同步更新索引，这会增加写入操作的时间。
  - 比喻：索引就像书的目录，虽然查找快，但每增加或修改内容时，目录也需要更新，增加了额外工作量。
- **应用场景：**
  - 索引适用于频繁查询的字段，比如员工编号、日期、部门编号等；但不适合频繁写入的场景，因为更新成本高。

### 2.2 索引的类型与特点
以下是 MySQL 中常见的索引类型，我会用通俗的语言和比喻描述每种类型的作用和适用场景。

#### 2.2.1 主键索引（Primary Key Index）
- **描述：** 主键索引是一种特殊的唯一索引，每个表只能有一个主键，通常用于唯一标识记录的字段（如 `emp_no`）。它确保每条记录都有唯一的“身份证号”。
- **比喻：** 就像每个人的身份证号，独一无二，数据库通过它快速定位到具体记录。
- **特点：**
  - 自动创建：定义主键时，数据库会自动为主键字段创建索引。
  - 唯一性：不允许重复值，且不能为 NULL。
- **适用场景：** 适合用在唯一标识字段上，比如员工编号、订单 ID 等。

#### 2.2.2 唯一索引（Unique Index）
- **描述：** 唯一索引保证字段值不重复，但允许 NULL 值（与主键不同），一个表可以有多个唯一索引。
- **比喻：** 就像一个班级的学号，虽然不是身份证，但也要求每个人不同，确保不重名。
- **特点：**
  - 确保唯一性：字段值不能重复，但可以为 NULL。
  - 可多个：一个表可以有多个唯一索引。
- **适用场景：** 适合用于邮箱、用户名等需要唯一但不一定是主键的字段。

#### 2.2.3 普通索引（Normal Index）
- **描述：** 普通索引是最常见的索引类型，没有唯一性限制，单纯用于加速查询。
- **比喻：** 就像书中的普通目录，指向内容位置，但不限制内容是否重复。
- **特点：**
  - 无限制：值可以重复，也可以为 NULL。
  - 灵活性高：可以根据查询需求创建多个普通索引。
- **适用场景：** 适合用于经常查询但不需要唯一性的字段，如日期、性别等。

#### 2.2.4 全文索引（Full-Text Index）
- **描述：** 全文索引用于文本搜索，适合在长文本中查找关键词，MySQL 的 InnoDB 引擎在较新版本中支持。
- **比喻：** 就像搜索引擎的关键词索引，能快速找到包含某个词的文章。
- **特点：**
  - 针对文本：主要用于 CHAR、VARCHAR、TEXT 类型字段。
  - 搜索效率高：支持 LIKE 模糊查询和全文搜索。
- **适用场景：** 适合搜索文章内容、产品描述等文本字段。

#### 2.2.5 复合索引（Composite Index）
- **描述：** 复合索引是由多个字段组合创建的索引，按字段顺序匹配查询条件。
- **比喻：** 就像一个多层目录，先按章节找，再按小节找，顺序很重要。
- **特点：**
  - 多字段：基于多个字段创建，查询时需遵循“最左前缀原则”（即查询条件需包含索引的最左字段）。
  - 节省空间：一个复合索引可替代多个单字段索引。
- **适用场景：** 适合多条件查询，比如按部门和入职日期同时筛选员工。

### 2.3 索引对存储和内存的影响
- **存储空间增加：**
  - 索引是独立的数据结构，存储在磁盘上，创建索引会增加数据库文件的大小。例如，在 `employees` 表（30 万条记录）上为 `hire_date` 创建索引，可能增加几 MB 的存储空间。
- **内存使用增加：**
  - 数据库运行时，可能会将常用索引加载到内存中以加速查询，这会占用额外的内存资源。特别是大数据量表，索引越多，内存占用越明显。
- **小白提示：** 想象索引像一个大字典，放在桌子上（磁盘）占地方，拿起来查（加载到内存）也占手（内存资源），所以索引不是越多越好，需要根据实际需求创建。

### 2.4 查看和删除现有索引
- **背景说明：** `employees` 数据库是 MySQL 官方提供的练习库，默认情况下，部分字段（如主键字段 `emp_no`）已经创建了索引。为了更好地演示索引的创建和效果，我们需要先查看并删除这些默认索引。
- **查看索引的命令：**
  - 使用 `SHOW INDEXES FROM 表名` 可以查看指定表上的所有索引信息。
  - 示例：
    ```sql
    -- 查看 employees 表上的所有索引
    SHOW INDEXES FROM employees;
    ```
    - **结果说明：** 会显示索引名称（Key_name）、字段（Column_name）、是否唯一（Non_unique）等信息。比如，主键索引会显示为 `PRIMARY`。
  - 使用 `EXPLAIN` 命令可以查看查询是否使用了索引。
    ```sql
    -- 检查某个查询是否使用索引
    EXPLAIN SELECT * FROM employees WHERE emp_no = 10001;
    ```
    - **结果说明：** 在结果的 `key` 列中，如果显示索引名称，说明查询使用了索引；如果为 NULL，说明未使用索引。
- **删除索引的命令：**
  - 使用 `DROP INDEX 索引名 ON 表名` 可以删除指定索引（主键索引需先删除主键约束）。
  - 示例：
    ```sql
    -- 删除 employees 表上的非主键索引（假设有一个名为 idx_hire_date 的索引）
    DROP INDEX idx_hire_date ON employees;
    -- 如果需要删除主键索引，先删除主键约束（谨慎操作）
    ALTER TABLE employees DROP PRIMARY KEY;
    ```
  - **注意：** 删除主键索引需谨慎，因为它可能影响表结构完整性。在教学演示中，我们可以选择删除非主键索引，或者在测试环境操作。
- **小白提示：** 查看索引就像“检查书有没有目录”，删除索引就像“把目录撕掉”，之后查询会变慢，但写入会变快。

### 2.5 索引的创建与效果演示
以下通过案例演示如何在 `employees` 数据库中创建索引，并观察其效果。我们假设已删除部分默认索引（或在测试环境操作），以便清晰展示创建前后差异。

#### 2.5.1 案例 1：创建普通索引并观察效果
- **需求：** 在 `employees` 表的 `hire_date` 字段上创建普通索引，加速入职日期范围查询。
- **思考步骤：**
  - 第一步：检查当前查询性能，用 EXPLAIN 分析是否使用索引。
  - 第二步：创建普通索引。
  - 第三步：再次执行查询，用 EXPLAIN 观察是否使用索引，比较性能变化。
- **SQL 实现与观察：**
  ```sql
  -- 第一步：检查当前查询性能
  EXPLAIN SELECT emp_no, first_name, last_name
  FROM employees
  WHERE hire_date BETWEEN '1990-01-01' AND '1990-12-31';
  -- 结果观察：查看 'key' 列是否为 NULL，若为 NULL 说明未使用索引，'rows' 列显示扫描行数可能很大（如 30 万）

  -- 第二步：创建普通索引
  CREATE INDEX idx_hire_date ON employees(hire_date);
  -- 结果观察：创建后无直接输出，但可以用以下命令查看索引是否创建成功
  SHOW INDEXES FROM employees;
  -- 结果中应看到 Key_name 为 'idx_hire_date' 的记录

  -- 第三步：再次检查查询性能
  EXPLAIN SELECT emp_no, first_name, last_name
  FROM employees
  WHERE hire_date BETWEEN '1990-01-01' AND '1990-12-31';
  -- 结果观察：查看 'key' 列是否显示 'idx_hire_date'，若显示说明查询使用了索引，'rows' 列扫描行数应大幅减少
  ```
- **解释：** 创建索引后，数据库可以直接定位到符合日期范围的记录，减少扫描行数，查询速度提升。

#### 2.5.2 案例 2：创建复合索引并观察效果
- **需求：** 在 `dept_emp` 表的 `dept_no` 和 `from_date` 字段上创建复合索引，加速部门和日期的联合查询。
- **思考步骤：**
  - 第一步：检查当前查询性能，用 EXPLAIN 分析是否使用索引。
  - 第二步：创建复合索引。
  - 第三步：再次执行查询，用 EXPLAIN 观察是否使用索引。
- **SQL 实现与观察：**
  ```sql
  -- 第一步：检查当前查询性能
  EXPLAIN SELECT emp_no
  FROM dept_emp
  WHERE dept_no = 'd001' AND from_date >= '1990-01-01';
  -- 结果观察：查看 'key' 列是否为 NULL，若为 NULL 说明未使用索引，扫描行数可能较多

  -- 第二步：创建复合索引
  CREATE INDEX idx_dept_from_date ON dept_emp(dept_no, from_date);
  -- 结果观察：用以下命令查看索引是否创建成功
  SHOW INDEXES FROM dept_emp;
  -- 结果中应看到 Key_name 为 'idx_dept_from_date' 的记录

  -- 第三步：再次检查查询性能
  EXPLAIN SELECT emp_no
  FROM dept_emp
  WHERE dept_no = 'd001' AND from_date >= '1990-01-01';
  -- 结果观察：查看 'key' 列是否显示 'idx_dept_from_date'，若显示说明查询使用了索引，扫描行数应减少
  ```
- **解释：** 复合索引按字段顺序匹配条件，`dept_no` 是最左字段，查询时优先匹配，效率更高。

#### 2.5.3 案例 3：创建唯一索引并观察效果
- **需求：** 在 `employees` 表的 `first_name` 和 `last_name` 上创建唯一索引（假设需要姓名唯一，仅为演示）。
- **思考步骤：**
  - 第一步：检查当前是否有重复数据（唯一索引要求值不重复）。
  - 第二步：创建唯一索引（若有重复数据会失败）。
  - 第三步：查看索引是否创建成功。
- **SQL 实现与观察：**
  ```sql
  -- 第一步：检查是否有重复数据
  SELECT first_name, last_name, COUNT(*) AS count
  FROM employees
  GROUP BY first_name, last_name
  HAVING count > 1;
  -- 结果观察：如果有重复数据，创建唯一索引会失败，需先处理重复数据（这里仅演示语法）

  -- 第二步：创建唯一索引（假设无重复数据）
  CREATE UNIQUE INDEX idx_name_unique ON employees(first_name, last_name);
  -- 结果观察：若创建失败，可能是数据重复；若成功，可用以下命令查看
  SHOW INDEXES FROM employees;
  -- 结果中应看到 Key_name 为 'idx_name_unique' 的记录，且 Non_unique 值为 0（表示唯一）

  -- 第三步：测试唯一性约束
  -- 尝试插入重复数据（假设可以插入，仅演示）
  -- INSERT INTO employees (first_name, last_name) VALUES ('已有名字', '已有姓氏');
  -- 结果观察：插入应失败，提示 Duplicate entry 错误
  ```
- **解释：** 唯一索引确保数据不重复，适合需要唯一约束的场景，但 `employees` 表实际数据可能有重复姓名，创建时需注意。

### 2.6 索引相关的观察命令总结
以下是常用的索引观察命令，方便学员随时检查索引状态和查询效果：
- **查看表上所有索引：**
  ```sql
  SHOW INDEXES FROM 表名;
  -- 示例：SHOW INDEXES FROM employees;
  -- 结果字段说明：Key_name（索引名）、Column_name（字段名）、Non_unique（是否唯一，0 为唯一）
  ```
- **查看查询是否使用索引：**
  ```sql
  EXPLAIN SELECT ... FROM 表名 WHERE 条件;
  -- 示例：EXPLAIN SELECT * FROM employees WHERE hire_date = '1990-01-01';
  -- 结果字段说明：key（使用的索引名，若为 NULL 则未使用）、rows（扫描行数）
  ```
- **查看数据库存储空间变化（间接观察索引占用）：**
  ```sql
  -- 查看表的大小（包括索引）
  SELECT table_name, data_length, index_length
  FROM information_schema.tables
  WHERE table_schema = 'employees' AND table_name = 'employees';
  -- 结果字段说明：data_length（数据大小，字节）、index_length（索引大小，字节）
  ```
- **小白提示：** 这些命令就像“体检工具”，能帮你看到索引是否生效、占用了多少空间，方便调试和优化。

### 2.7 索引应用作业题
以下是 6 个基于 `employees` 数据库的作业题，帮助学员练习索引的创建和观察。每个题目包含需求、思考步骤和 SQL 代码，供学员实践。

#### 作业题 1：为 `salaries` 表的 `salary` 字段创建普通索引
- **需求：** 在 `salaries` 表的 `salary` 字段上创建普通索引，加速薪资范围查询。
- **思考步骤：**
  - 第一步：检查当前查询是否使用索引。
  - 第二步：创建普通索引。
  - 第三步：查看索引是否创建成功，并检查查询效果。
- **SQL 实现：**
  ```sql
  -- 第一步：检查查询性能
  EXPLAIN SELECT emp_no, salary FROM salaries WHERE salary > 80000;
  -- 观察 'key' 列是否为 NULL

  -- 第二步：创建普通索引
  CREATE INDEX idx_salary ON salaries(salary);
  
  -- 第三步：查看索引并检查效果
  SHOW INDEXES FROM salaries;  -- 应看到 idx_salary
  EXPLAIN SELECT emp_no, salary FROM salaries WHERE salary > 80000;  -- 观察 'key' 是否为 idx_salary
  ```

#### 作业题 2：为 `titles` 表的 `title` 字段创建普通索引
- **需求：** 在 `titles` 表的 `title` 字段上创建普通索引，加速职位查询。
- **思考步骤：**
  - 第一步：检查当前查询是否使用索引。
  - 第二步：创建普通索引。
  - 第三步：查看索引是否创建成功，并检查查询效果。
- **SQL 实现：**
  ```sql
  -- 第一步：检查查询性能
  EXPLAIN SELECT emp_no, title FROM titles WHERE title = 'Engineer';
  -- 观察 'key' 列是否为 NULL

  -- 第二步：创建普通索引
  CREATE INDEX idx_title ON titles(title);
  
  -- 第三步：查看索引并检查效果
  SHOW INDEXES FROM titles;  -- 应看到 idx_title
  EXPLAIN SELECT emp_no, title FROM titles WHERE title = 'Engineer';  -- 观察 'key' 是否为 idx_title
  ```

#### 作业题 3：为 `dept_emp` 表创建复合索引
- **需求：** 在 `dept_emp` 表的 `emp_no` 和 `dept_no` 字段上创建复合索引，加速员工和部门联合查询。
- **思考步骤：**
  - 第一步：检查当前查询是否使用索引。
  - 第二步：创建复合索引。
  - 第三步：查看索引是否创建成功，并检查查询效果。
- **SQL 实现：**
  ```sql
  -- 第一步：检查查询性能
  EXPLAIN SELECT emp_no, dept_no FROM dept_emp WHERE emp_no = 10001 AND dept_no = 'd001';
  -- 观察 'key' 列是否为 NULL

  -- 第二步：创建复合索引
  CREATE INDEX idx_emp_dept ON dept_emp(emp_no, dept_no);
  
  -- 第三步：查看索引并检查效果
  SHOW INDEXES FROM dept_emp;  -- 应看到 idx_emp_dept
  EXPLAIN SELECT emp_no, dept_no FROM dept_emp WHERE emp_no = 10001 AND dept_no = 'd001';  -- 观察 'key' 是否为 idx_emp_dept
  ```

#### 作业题 4：查看 `employees` 表索引并尝试删除一个非主键索引
- **需求：** 查看 `employees` 表的所有索引，删除一个非主键索引（若有）。
- **思考步骤：**
  - 第一步：查看当前索引。
  - 第二步：选择一个非主键索引并删除。
  - 第三步：再次查看索引，确认删除效果。
- **SQL 实现：**
  ```sql
  -- 第一步：查看当前索引
  SHOW INDEXES FROM employees;
  -- 观察 Key_name，找到非 PRIMARY 的索引名（如 idx_hire_date，若有）

  -- 第二步：删除一个非主键索引（假设索引名为 idx_hire_date）
  DROP INDEX idx_hire_date ON employees;
  
  -- 第三步：再次查看索引
  SHOW INDEXES FROM employees;  -- 确认 idx_hire_date 已消失
  ```

#### 作业题 5：观察索引对存储空间的影响
- **需求：** 在创建索引前后，观察 `employees` 表存储空间的变化。
- **思考步骤：**
  - 第一步：查看当前表和索引的大小。
  - 第二步：创建一个新索引。
  - 第三步：再次查看表和索引的大小，比较变化。
- **SQL 实现：**
  ```sql
  -- 第一步：查看当前表和索引大小
  SELECT table_name, data_length, index_length
  FROM information_schema.tables
  WHERE table_schema = 'employees' AND table_name = 'employees';
  -- 记录 index_length 值（索引大小，字节）

  -- 第二步：创建新索引
  CREATE INDEX idx_birth_date ON employees(birth_date);
  
  -- 第三步：再次查看表和索引大小
  SELECT table_name, data_length, index_length
  FROM information_schema.tables
  WHERE table_schema = 'employees' AND table_name = 'employees';
  -- 比较 index_length 值，应有所增加
  ```

#### 作业题 6：为 `salaries` 表创建复合索引并观察效果
- **需求：** 在 `salaries` 表的 `emp_no` 和 `from_date` 字段上创建复合索引，加速查询。
- **思考步骤：**
  - 第一步：检查当前查询是否使用索引。
  - 第二步：创建复合索引。
  - 第三步：查看索引是否创建成功，并检查查询效果。
- **SQL 实现：**
  ```sql
  -- 第一步：检查查询性能
  EXPLAIN SELECT salary FROM salaries WHERE emp_no = 10001 AND from_date >= '1990-01-01';
  -- 观察 'key' 列是否为 NULL

  -- 第二步：创建复合索引
  CREATE INDEX idx_emp_from_date ON salaries(emp_no, from_date);
  
  -- 第三步：查看索引并检查效果
  SHOW INDEXES FROM salaries;  -- 应看到 idx_emp_from_date
  EXPLAIN SELECT salary FROM salaries WHERE emp_no = 10001 AND from_date >= '1990-01-01';  -- 观察 'key' 是否为 idx_emp_from_date
  ```

---

### 总结与备注
- **本部分成果：** 学员掌握了索引的基本概念、类型（主键、唯一、普通、全文、复合索引）及其作用，学会了如何创建、查看和删除索引，并通过案例和作业题理解了索引对查询性能的提升以及对存储和内存的占用。
- **小白适应性：** 通过比喻（如“索引像书目录”）和分步拆解，确保内容易懂；提供多种观察命令，帮助直观感受索引效果。
- **学习用途回顾：**
  - 索引是数据库优化的核心工具，能显著提升查询效率，特别适合大数据量场景。
  - 了解索引的代价（如存储和内存占用）有助于合理设计数据库结构。
- **后续衔接：** 索引带来的写入压力和数据一致性问题，将在下一部分（如 Redo Log 原理）中探讨。

---
