# Ubuntu 系统下的综合 Linux 命令练习题及解析（增强 find 与 grep 版）

## 练习题 1：简单难度（基础操作与 `vim` 入门，结合 `grep` 进阶）

### 题目
你需要在当前目录下完成以下任务：
1. 创建一个名为 `test_logs` 的目录。
2. 在该目录下创建一个文件 `app.log`，并复制以下内容粘贴到文件中（使用 `vim` 编辑器完成）：
   [INFO] 2023-10-01 10:00:01 Log entry 1
   [INFO] 2023-10-01 10:01:02 Log entry 2
   [INFO] 2023-10-01 10:02:03 Log entry 3
   [INFO] 2023-10-01 10:03:04 Log entry 4
   [WARNING] 2023-10-01 10:04:05 Log entry 5 error
   [INFO] 2023-10-01 10:05:06 Log entry 6
   [INFO] 2023-10-01 10:06:07 Log entry 7
   [WARNING] 2023-10-01 10:07:08 Log entry 8 issue
   [INFO] 2023-10-01 10:08:09 Log entry 9
   [INFO] 2023-10-01 10:09:10 Log entry 10
3. 使用 `grep` 查找 `app.log` 中包含 `WARNING` 的行，并显示行号，同时将结果保存到 `warnings.txt`。
4. 使用 `vim` 再次打开 `app.log`，完成以下编辑：
   - 在文件第一行前添加一行 `[START] Log begins here`。
   - 在文件最后一行后添加一行 `[END] Log ends here`。
   - 将所有包含 `WARNING` 的行中的 `error` 或 `issue` 替换为 `PROBLEM`。

### 解题思路
1. **分析需求**：
   - 创建目录和文件。
   - 写入预定义内容。
   - 使用 `grep` 进行带行号的搜索并保存结果。
   - 使用 `vim` 进行多步编辑。
2. **选择命令**：
   - 使用 `mkdir` 创建目录。
   - 使用 `vim` 创建并编辑文件。
   - 使用 `grep` 搜索内容并输出行号。
3. **构建步骤**：
   - `mkdir test_logs` 创建目录。
   - 使用 `vim test_logs/app.log` 创建文件，进入插入模式粘贴内容。
   - `grep -n` 查找包含 `WARNING` 的行并保存。
   - 再次使用 `vim` 打开文件，进行插入和替换操作。
4. **注意事项**：
   - 确保当前目录有写入权限。
   - 熟悉 `grep -n` 的用法以显示行号。
   - 熟悉 `vim` 基本操作：`i` 进入插入模式，`Esc` 退出插入模式，`:wq` 保存退出，`:s` 替换等。

### 参考答案
#### 步骤 1：创建目录
mkdir test_logs

#### 步骤 2：创建文件并粘贴内容
vim test_logs/app.log
- 在 `vim` 中：
  1. 按 `i` 进入插入模式。
  2. 复制以下内容并粘贴到编辑器中：
     [INFO] 2023-10-01 10:00:01 Log entry 1
     [INFO] 2023-10-01 10:01:02 Log entry 2
     [INFO] 2023-10-01 10:02:03 Log entry 3
     [INFO] 2023-10-01 10:03:04 Log entry 4
     [WARNING] 2023-10-01 10:04:05 Log entry 5 error
     [INFO] 2023-10-01 10:05:06 Log entry 6
     [INFO] 2023-10-01 10:06:07 Log entry 7
     [WARNING] 2023-10-01 10:07:08 Log entry 8 issue
     [INFO] 2023-10-01 10:08:09 Log entry 9
     [INFO] 2023-10-01 10:09:10 Log entry 10
  3. 按 `Esc` 退出插入模式。
  4. 输入 `:wq` 保存并退出。

#### 步骤 3：查找包含 `WARNING` 的行并保存
grep -n "WARNING" test_logs/app.log > warnings.txt
- 输出结果（保存到 `warnings.txt`）：
  5:[WARNING] 2023-10-01 10:04:05 Log entry 5 error
  8:[WARNING] 2023-10-01 10:07:08 Log entry 8 issue

#### 步骤 4：使用 `vim` 编辑文件
vim test_logs/app.log
- 在 `vim` 中：
  1. 按 `gg` 跳转到文件第一行。
  2. 按 `O`（大写）在当前行上方插入新行，输入 `[START] Log begins here`，按 `Esc`。
  3. 按 `G` 跳转到文件最后一行。
  4. 按 `o`（小写）在当前行下方插入新行，输入 `[END] Log ends here`，按 `Esc`。
  5. 输入 `:%s/\(WARNING.*\)\(error\|issue\)/\1PROBLEM/g` 并回车，将所有包含 `WARNING` 的行中的 `error` 或 `issue` 替换为 `PROBLEM`。
  6. 输入 `:wq` 保存并退出。
- 编辑后的文件内容为：
  [START] Log begins here
  [INFO] 2023-10-01 10:00:01 Log entry 1
  [INFO] 2023-10-01 10:01:02 Log entry 2
  [INFO] 2023-10-01 10:02:03 Log entry 3
  [INFO] 2023-10-01 10:03:04 Log entry 4
  [WARNING] 2023-10-01 10:04:05 Log entry 5 PROBLEM
  [INFO] 2023-10-01 10:05:06 Log entry 6
  [INFO] 2023-10-01 10:06:07 Log entry 7
  [WARNING] 2023-10-01 10:07:08 Log entry 8 PROBLEM
  [INFO] 2023-10-01 10:08:09 Log entry 9
  [INFO] 2023-10-01 10:09:10 Log entry 10
  [END] Log ends here

---

## 练习题 2：一般难度（多命令协作与 `find` 和 `grep` 进阶）

### 题目
你需要在当前目录下完成以下任务：
1. 使用 `echo` 创建三个文件 `report1.txt`、`report2.txt` 和 `report3.txt`，内容分别为：
   - `report1.txt`:
     Project: Alpha
     Status: In Progress
     Issues: 3
   - `report2.txt`:
     Project: Beta
     Status: Completed
     Issues: 0
   - `report3.txt`:
     Project: Gamma
     Status: In Progress
     Issues: 5
2. 使用 `find` 查找当前目录下所有以 `report` 开头的文件，并将文件名列表通过管道传递给 `grep`，只显示包含 `Issues` 且值大于 0 的文件内容。
3. 使用 `vim` 编辑 `report1.txt`，完成以下操作：
   - 在文件末尾添加一行 `Updated: 2023-10-01`。
   - 将 `Issues: 3` 替换为 `Issues: 4`。
   - 查找包含 `Status` 的行，并将光标定位到该行。
4. 使用 `head` 查看 `report1.txt` 的前 4 行。

### 解题思路
1. **分析需求**：
   - 创建多个文件并写入内容。
   - 使用 `find` 和 `grep` 结合管道符进行复杂搜索。
   - 使用 `vim` 进行编辑。
   - 查看文件内容。
2. **选择命令**：
   - 使用 `echo` 创建文件。
   - 使用 `find` 查找文件并结合 `grep` 过滤内容。
   - 使用 `vim` 进行编辑。
   - 使用 `head` 查看内容。
3. **构建步骤**：
   - 使用 `echo` 和重定向创建文件。
   - 使用 `find` 和 `xargs` 结合 `grep` 查找并过滤内容。
   - 使用 `vim` 打开文件进行编辑。
   - 使用 `head -n 4` 查看前 4 行。
4. **注意事项**：
   - `find` 结合 `xargs` 可以处理多个文件。
   - `grep` 使用正则或条件过滤非零值。
   - 确保 `vim` 编辑时保存文件。

### 参考答案
#### 步骤 1：创建文件
echo -e "Project: Alpha\nStatus: In Progress\nIssues: 3" > report1.txt
echo -e "Project: Beta\nStatus: Completed\nIssues: 0" > report2.txt
echo -e "Project: Gamma\nStatus: In Progress\nIssues: 5" > report3.txt

#### 步骤 2：使用 `find` 和 `grep` 查找文件并过滤内容
find . -name "report*.txt" -type f -exec grep -l "Issues: [1-9]" {} \;
- 输出结果（仅显示符合条件的文件名）：
  ./report1.txt
  ./report3.txt
- 或者查看具体内容：
find . -name "report*.txt" -type f -exec grep "Issues: [1-9]" {} \;
- 输出结果：
  ./report1.txt:Issues: 3
  ./report3.txt:Issues: 5

#### 步骤 3：使用 `vim` 编辑文件
vim report1.txt
- 在 `vim` 中：
  1. 按 `G` 跳转到文件末尾。
  2. 按 `o` 在当前行下方插入新行，输入 `Updated: 2023-10-01`，按 `Esc`。
  3. 输入 `:%s/Issues: 3/Issues: 4/g` 并回车，将 `Issues: 3` 替换为 `Issues: 4`。
  4. 输入 `/Status` 并按回车，查找包含 `Status` 的行，光标会定位到该行。
  5. 输入 `:wq` 保存并退出。
- 编辑后的文件内容为：
  Project: Alpha
  Status: In Progress
  Issues: 4
  Updated: 2023-10-01

#### 步骤 4：查看前 4 行
head -n 4 report1.txt
- 输出结果：
  Project: Alpha
  Status: In Progress
  Issues: 4
  Updated: 2023-10-01

---

## 练习题 3：困难难度（复杂任务与 `find` 和 `grep` 综合应用）

### 题目
你需要在 Ubuntu 系统中完成以下任务：
1. 在当前目录下创建子目录 `logs`、`docs` 和 `backups`，并在每个目录中创建一些测试文件：
   - `logs/error1.log`、`logs/error2.log`、`logs/info.log`
   - `docs/report1.txt`、`docs/report2.txt`
   - `backups/backup1.tar`、`backups/backup2.tar`
   每个文件内容可随意填写，例如使用 `echo` 输入简单文本。
2. 使用 `find` 查找当前目录及其子目录中所有以 `.log` 结尾的文件，并结合 `grep` 查找其中包含 `error` 的文件名（假设文件内容或文件名中可能包含 `error`），将结果保存到 `error_logs.txt`。
3. 使用 `vim` 编辑 `error_logs.txt`，完成以下操作：
   - 在文件第一行添加标题 `List of Error Logs:`。
   - 在文件末尾添加一行 `Total files: `，并手动统计文件数量后填入（假设有 2 个文件，则为 `Total files: 2`）。
   - 将文件内容按字母顺序排序（假设 `vim` 中使用命令）。
4. 使用 `tail` 查看 `error_logs.txt` 的最后 3 行。
5. 使用 `find` 查找所有以 `.tar` 结尾的文件，并打包成一个新的压缩文件 `all_backups.tar.gz`。

### 解题思路
1. **分析需求**：
   - 创建目录结构和测试文件。
   - 使用 `find` 和 `grep` 进行复杂搜索并保存结果。
   - 使用 `vim` 进行编辑。
   - 查看文件内容。
   - 使用 `find` 查找并打包文件。
2. **选择命令**：
   - 使用 `mkdir` 和 `echo` 创建目录和文件。
   - 使用 `find` 和 `grep` 结合查找特定文件。
   - 使用 `vim` 进行编辑。
   - 使用 `tail` 查看内容。
   - 使用 `find` 和 `tar` 打包文件。
3. **构建步骤**：
   - 创建目录和文件。
   - 使用 `find` 查找 `.log` 文件并用 `grep` 过滤包含 `error` 的文件。
   - 使用 `vim` 编辑结果文件。
   - 使用 `tail -n 3` 查看最后 3 行。
   - 使用 `find` 和 `tar` 打包 `.tar` 文件。
4. **注意事项**：
   - `find` 可以结合 `-name` 和 `-exec` 进行复杂搜索。
   - `grep -l` 只输出文件名，适合过滤。
   - `vim` 中排序使用 `:sort` 命令。

### 参考答案
#### 步骤 1：创建目录和测试文件
mkdir -p logs docs backups
echo "Error occurred" > logs/error1.log
echo "Another error" > logs/error2.log
echo "Just info" > logs/info.log
echo "Report content 1" > docs/report1.txt
echo "Report content 2" > docs/report2.txt
echo "Backup data 1" > backups/backup1.tar
echo "Backup data 2" > backups/backup2.tar

#### 步骤 2：使用 `find` 和 `grep` 查找包含 `error` 的 `.log` 文件
find . -name "*.log" -type f | grep "error" > error_logs.txt
- 输出结果（保存到 `error_logs.txt`）：
  ./logs/error1.log
  ./logs/error2.log

#### 步骤 3：使用 `vim` 编辑文件
vim error_logs.txt
- 在 `vim` 中：
  1. 按 `gg` 跳转到文件第一行，按 `O` 在上方插入新行，输入 `List of Error Logs:`，按 `Esc`。
  2. 按 `G` 跳转到文件末尾，按 `o` 在下方插入新行，输入 `Total files: 2`，按 `Esc`。
  3. 输入 `:2,$sort` 并回车，对文件内容从第二行到最后一行按字母顺序排序（避免标题行被排序）。
  4. 输入 `:wq` 保存并退出。
- 编辑后内容为：
  List of Error Logs:
  ./logs/error1.log
  ./logs/error2.log
  Total files: 2

#### 步骤 4：查看最后 3 行
tail -n 3 error_logs.txt
- 输出结果：
  ./logs/error1.log
  ./logs/error2.log
  Total files: 2

#### 步骤 5：使用 `find` 查找 `.tar` 文件并打包
tar -czvf all_backups.tar.gz $(find . -name "*.tar")
- 打包 `./backups/backup1.tar` 和 `./backups/backup2.tar` 到 `all_backups.tar.gz`。

---

## 总结
- **简单题**：结合 `mkdir`、`grep` 和 `vim`，增强了 `grep` 的使用（如显示行号、正则替换），完成日志文件的搜索和编辑。
- **一般题**：结合 `echo`、`find`、`grep` 和 `vim`，通过 `find` 和 `grep` 的管道操作实现多文件内容过滤，体现文件搜索的实用性。
- **困难题**：综合使用 `find`、`grep`、`tail`、`tar` 和 `vim`，通过复杂的文件查找和内容过滤，完成多目录文件的处理和打包。

这些题目增强了 `find` 和 `grep` 的应用场景，涵盖了文件名和内容搜索、条件过滤等进阶用法，同时保留了 `vim` 的练习比例。如果你觉得还需要更多相关练习或有其他需求，欢迎继续反馈！