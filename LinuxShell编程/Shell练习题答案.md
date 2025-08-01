## Linux Shell 编程练习题答案（50 道）

### 一、基础知识与环境设置（1-10）
1. **什么是 Shell？简述 Bash 与其他 Shell（如 sh、zsh）的区别。**
   - **答案**：Shell 是用户与操作系统内核之间的接口，用于解释用户命令并执行。Bash（Bourne Again Shell）是 GNU 项目开发的 Shell，支持更多的功能（如命令补全、历史记录）且兼容 sh。sh（Bourne Shell）是较早的 Shell，功能较少；zsh 是一个功能强大的 Shell，支持更高级的补全和定制，但配置复杂。
   - **说明**：此题为理论题，旨在帮助学员理解 Shell 的概念和种类。

2. **如何查看当前使用的 Shell 类型？请写出命令。**
   - **答案**：`echo $SHELL` 或 `ps $$`
   - **说明**：`$SHELL` 显示环境变量中设置的 Shell 路径，`ps $$` 显示当前进程的 Shell 类型。

3. **如何在 Bash 中设置环境变量？请写出设置 PATH 变量的命令，并使其在重启后依然有效。**
   - **答案**：
     ```bash
     export PATH=$PATH:/new/path  # 临时设置
     echo 'export PATH=$PATH:/new/path' >> ~/.bashrc  # 持久化到 .bashrc 文件
     source ~/.bashrc  # 立即生效
     ```
   - **说明**：`export` 设置环境变量，追加到 `~/.bashrc` 确保重启后有效，`source` 重新加载配置文件。

4. **解释 Shell 脚本文件的首行 `#!/bin/bash` 的作用。**
   - **答案**：`#!/bin/bash` 是 Shebang 行，指定脚本使用 Bash 解释器执行。若无此行，系统可能使用默认 Shell（如 sh）运行，可能导致兼容性问题。
   - **说明**：Shebang 行指明解释器路径，确保脚本按预期运行。

5. **如何为 Shell 脚本文件添加可执行权限？请写出命令。**
   - **答案**：`chmod +x script.sh`
   - **说明**：`chmod +x` 为文件添加可执行权限，之后可通过 `./script.sh` 运行。

6. **写出三种运行 Shell 脚本的方式。**
   - **答案**：
     1. `./script.sh` （需可执行权限）
     2. `bash script.sh` （直接用 Bash 解释器运行）
     3. `source script.sh` 或 `. script.sh` （在当前 Shell 环境中执行）
   - **说明**：三种方式适用不同场景，`source` 会影响当前环境变量。

7. **什么是 Shell 中的 `$?` 变量？如何使用它判断命令执行是否成功？**
   - **答案**：`$?` 存储上一个命令的退出状态码，0 表示成功，非 0 表示失败。
     ```bash
     ls /tmp
     if [ $? -eq 0 ]; then
         echo "命令执行成功"
     else
         echo "命令执行失败"
     fi
     ```
   - **说明**：通过 `$?` 判断命令执行结果，常用于错误处理。

8. **解释 Shell 中的 `$$` 和 `$!` 变量的含义，并举例说明。**
   - **答案**：
     - `$$`：当前 Shell 进程的 PID（进程 ID）。
     - `$!`：最近后台运行进程的 PID。
     ```bash
     echo "当前进程 ID: $$"
     sleep 10 &
     echo "后台进程 ID: $!"
     ```
   - **说明**：`$$` 用于标识当前脚本进程，`$!` 用于管理后台任务。

9. **如何在 Shell 中查看所有内置命令？请写出命令。**
   - **答案**：`help` 或 `man bash`
   - **说明**：`help` 列出内置命令，`man bash` 提供 Bash 手册，包含内置命令说明。

10. **什么是 Shell 的别名（alias）？如何设置一个别名将 `ll` 定义为 `ls -l`？**
    - **答案**：
      ```bash
      alias ll='ls -l'
      ```
    - **说明**：`alias` 定义命令别名，简化常用命令输入，可添加到 `~/.bashrc` 持久化。

---

### 二、变量与参数处理（11-20）
11. **写一个 Shell 脚本，定义一个变量 `name` 为你的名字，并输出 “Hello, $name!”。**
    - **答案**：
      ```bash
      #!/bin/bash
      name="小明"
      echo "Hello, $name!"
      ```
    - **说明**：变量定义无需类型声明，用 `$` 引用变量值。

12. **如何在 Shell 脚本中读取用户输入并存储到变量中？请写出代码。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "请输入你的名字："
      read name
      echo "你好，$name！"
      ```
    - **说明**：`read` 命令从标准输入读取数据并赋值给变量。

13. **解释 Shell 中单引号 `''` 和双引号 `""` 的区别，并举例说明变量展开的行为。**
    - **答案**：
      - 单引号 `''`：不解析变量和特殊字符，输出原样。
      - 双引号 `""`：解析变量和部分特殊字符（如 `$`）。
      ```bash
      name="小明"
      echo 'Hello, $name'  # 输出：Hello, $name
      echo "Hello, $name"  # 输出：Hello, 小明
      ```
    - **说明**：双引号支持变量展开，单引号则保持原始字符串。

14. **写一个 Shell 脚本，输出脚本接收的第一个参数和所有参数。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "第一个参数：$1"
      echo "所有参数：$@"
      ```
    - **说明**：`$1` 表示第一个参数，`$@` 表示所有参数列表。

15. **如何在 Shell 脚本中检查是否提供了命令行参数？请写出代码。**
    - **答案**：
      ```bash
      #!/bin/bash
      if [ $# -eq 0 ]; then
          echo "未提供参数"
      else
          echo "提供了 $# 个参数"
      fi
      ```
    - **说明**：`$#` 表示参数数量，用于判断是否有参数输入。

16. **写一个 Shell 脚本，将变量 `count` 初始化为 0，并进行自增操作后输出结果。**
    - **答案**：
      ```bash
      #!/bin/bash
      count=0
      ((count++))
      echo "count = $count"
      ```
    - **说明**：`(())` 用于算术运算，`count++` 实现自增。

17. **如何在 Shell 中将命令的输出赋值给变量？请写出两种方法。**
    - **答案**：
      ```bash
      # 方法1：使用 $()
      date_str=$(date)
      echo "当前时间：$date_str"
      # 方法2：使用反引号
      date_str=`date`
      echo "当前时间：$date_str"
      ```
    - **说明**：`$()` 是现代写法，反引号 `` ` `` 是旧式写法，功能相同。

18. **写一个 Shell 脚本，定义只读变量 `VERSION=1.0`，并尝试修改它，观察结果。**
    - **答案**：
      ```bash
      #!/bin/bash
      readonly VERSION=1.0
      echo "版本：$VERSION"
      VERSION=2.0  # 会报错
      ```
    - **说明**：`readonly` 定义只读变量，修改会报错。

19. **解释 Shell 中 `export` 命令的作用，并写一个示例将变量导出到子进程。**
    - **答案**：
      ```bash
      #!/bin/bash
      export MY_VAR="Hello"
      bash -c 'echo $MY_VAR'  # 子进程中可访问 MY_VAR
      ```
    - **说明**：`export` 将变量导出到子进程环境，否则子进程无法访问。

20. **写一个 Shell 脚本，使用 `shift` 命令处理参数，并输出每次处理后的参数列表。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "初始参数：$@"
      shift
      echo "shift 后参数：$@"
      ```
    - **说明**：`shift` 移除第一个参数，后续参数前移。

---

### 三、流程控制（21-30）
21. **写一个 Shell 脚本，使用 `if` 语句判断一个文件是否存在，并输出相应信息。**
    - **答案**：
      ```bash
      #!/bin/bash
      file="test.txt"
      if [ -f "$file" ]; then
          echo "$file 存在"
      else
          echo "$file 不存在"
      fi
      ```
    - **说明**：`-f` 测试文件是否存在，`if` 进行条件判断。

22. **写一个 Shell 脚本，使用 `if-else` 判断输入的数字是正数、负数还是零。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "请输入一个数字："
      read num
      if [ $num -gt 0 ]; then
          echo "正数"
      elif [ $num -lt 0 ]; then
          echo "负数"
      else
          echo "零"
      fi
      ```
    - **说明**：使用 `-gt` 和 `-lt` 比较数字大小。

23. **如何在 Shell 中使用 `test` 命令比较两个字符串是否相等？请写出代码。**
    - **答案**：
      ```bash
      #!/bin/bash
      str1="hello"
      str2="hello"
      if test "$str1" = "$str2"; then
          echo "字符串相等"
      else
          echo "字符串不相等"
      fi
      ```
    - **说明**：`test` 或 `[` 用于字符串比较，`=` 表示相等。

24. **写一个 Shell 脚本，使用 `for` 循环遍历 1 到 10 并输出每个数字。**
    - **答案**：
      ```bash
      #!/bin/bash
      for i in {1..10}
      do
          echo $i
      done
      ```
    - **说明**：`{1..10}` 生成 1 到 10 的序列，`for` 循环遍历。

25. **写一个 Shell 脚本，使用 `while` 循环实现从 1 累加到 100 的和。**
    - **答案**：
      ```bash
      #!/bin/bash
      sum=0
      i=1
      while [ $i -le 100 ]
      do
          sum=$((sum + i))
          ((i++))
      done
      echo "1 到 100 的和：$sum"
      ```
    - **说明**：`while` 循环累加，`$(( ))` 用于算术运算。

26. **写一个 Shell 脚本，使用 `until` 循环输出从 10 倒数到 1 的数字。**
    - **答案**：
      ```bash
      #!/bin/bash
      i=10
      until [ $i -lt 1 ]
      do
          echo $i
          ((i--))
      done
      ```
    - **说明**：`until` 在条件为假时循环，适合倒计数。

27. **写一个 Shell 脚本，使用 `case` 语句根据用户输入的数字（1-3）输出对应的星期几。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "请输入 1-3 的数字："
      read num
      case $num in
          1)
              echo "星期一"
              ;;
          2)
              echo "星期二"
              ;;
          3)
              echo "星期三"
              ;;
          *)
              echo "无效输入"
              ;;
      esac
      ```
    - **说明**：`case` 实现多分支选择，`*` 匹配其他情况。

28. **如何在 Shell 脚本中使用 `break` 跳出循环？请写一个示例。**
    - **答案**：
      ```bash
      #!/bin/bash
      for i in {1..10}
      do
          if [ $i -eq 5 ]; then
              break
          fi
          echo $i
      done
      ```
    - **说明**：`break` 在 `i=5` 时终止循环，仅输出 1-4。

29. **如何在 Shell 脚本中使用 `continue` 跳过当前循环迭代？请写一个示例。**
    - **答案**：
      ```bash
      #!/bin/bash
      for i in {1..5}
      do
          if [ $i -eq 3 ]; then
              continue
          fi
          echo $i
      done
      ```
    - **说明**：`continue` 跳过 `i=3` 的迭代，输出 1,2,4,5。

30. **写一个 Shell 脚本，结合 `if` 和 `for` 循环，找出 1 到 50 之间的所有偶数。**
    - **答案**：
      ```bash
      #!/bin/bash
      for i in {1..50}
      do
          if [ $((i % 2)) -eq 0 ]; then
              echo $i
          fi
      done
      ```
    - **说明**：使用取模 `%` 判断偶数，结合循环和条件输出。

---

### 四、函数与模块化（31-35）
31. **写一个 Shell 脚本，定义一个函数 `say_hello`，接受一个参数并输出问候语。**
    - **答案**：
      ```bash
      #!/bin/bash
      say_hello() {
          echo "Hello, $1!"
      }
      say_hello "小明"
      ```
    - **说明**：函数定义用 `()`，参数通过 `$1` 访问。

32. **如何在 Shell 函数中返回一个值？写一个函数计算两个数的和并返回结果。**
    - **答案**：
      ```bash
      #!/bin/bash
      add() {
          sum=$(( $1 + $2 ))
          echo $sum  # 通过 echo 返回
      }
      result=$(add 3 5)
      echo "和为：$result"
      ```
    - **说明**：Shell 函数通常通过 `echo` 输出返回值，用 `$()` 捕获。

33. **写一个 Shell 脚本，定义一个函数检查文件是否存在，并在主程序中调用该函数。**
    - **答案**：
      ```bash
      #!/bin/bash
      check_file() {
          if [ -f "$1" ]; then
              echo "$1 存在"
          else
              echo "$1 不存在"
          fi
      }
      check_file "test.txt"
      ```
    - **说明**：函数封装文件检查逻辑，主程序调用。

34. **如何在 Shell 中定义局部变量以避免污染全局变量？请写一个示例。**
    - **答案**：
      ```bash
      #!/bin/bash
      my_func() {
          local var="局部变量"
          echo $var
      }
      my_func
      echo $var  # 为空，未定义
      ```
    - **说明**：`local` 限制变量作用域，仅在函数内有效。

35. **写一个 Shell 脚本，将多个常用函数整理到一个文件中，并通过 `source` 引入到另一个脚本中使用。**
    - **答案**：
      - 文件 `utils.sh`：
        ```bash
        check_file() {
            if [ -f "$1" ]; then
                echo "$1 存在"
            else
                echo "$1 不存在"
            fi
        }
        ```
      - 文件 `main.sh`：
        ```bash
        #!/bin/bash
        source utils.sh
        check_file "test.txt"
        ```
    - **说明**：`source` 引入外部脚本，复用函数。

---

### 五、文件与文本处理（36-45）
36. **写一个 Shell 脚本，读取文件 `data.txt` 的内容并输出到终端。**
    - **答案**：
      ```bash
      #!/bin/bash
      cat data.txt
      ```
    - **说明**：`cat` 直接输出文件内容。

37. **写一个 Shell 脚本，向文件 `log.txt` 追加一行当前时间戳。**
    - **答案**：
      ```bash
      #!/bin/bash
      echo "$(date)" >> log.txt
      ```
    - **说明**：`>>` 追加内容，`date` 获取时间戳。

38. **如何在 Shell 中使用 `grep` 查找文件中包含特定关键字的行？请写出命令。**
    - **答案**：`grep "keyword" file.txt`
    - **说明**：`grep` 搜索文件内容，匹配指定关键字。

39. **写一个 Shell 脚本，使用 `awk` 提取文件 `users.txt` 的第一列数据（假设以空格分隔）。**
    - **答案**：
      ```bash
      #!/bin/bash
      awk '{print $1}' users.txt
      ```
    - **说明**：`awk` 默认以空格分隔，`$1` 提取第一列。

40. **写一个 Shell 脚本，使用 `sed` 将文件中的所有 “error” 替换为 “warning”。**
    - **答案**：
      ```bash
      #!/bin/bash
      sed -i 's/error/warning/g' file.txt
      ```
    - **说明**：`sed` 替换文本，`-i` 直接修改文件，`g` 全局替换。

41. **如何在 Shell 中统计文件的行数、字数和字符数？请写出命令。**
    - **答案**：`wc file.txt`
    - **说明**：`wc` 输出行数、字数和字符数。

42. **写一个 Shell 脚本，查找当前目录下所有 `.txt` 文件并输出它们的名称。**
    - **答案**：
      ```bash
      #!/bin/bash
      find . -name "*.txt"
      ```
    - **说明**：`find` 搜索文件，`-name` 匹配文件名模式。

43. **写一个 Shell 脚本，使用管道将 `ls -l` 的输出传递给 `grep`，筛选包含 “root” 的行。**
    - **答案**：
      ```bash
      #!/bin/bash
      ls -l | grep "root"
      ```
    - **说明**：管道 `|` 将左侧命令输出作为右侧命令输入。

44. **写一个 Shell 脚本，读取文件内容并按行逆序输出。**
    - **答案**：
      ```bash
      #!/bin/bash
      tac file.txt
      ```
    - **说明**：`tac` 逆序输出文件内容（与 `cat` 相反）。

45. **写一个 Shell 脚本，使用 `cut` 命令提取 `/etc/passwd` 文件的用户名（第一字段）。**
    - **答案**：
      ```bash
      #!/bin/bash
      cut -d: -f1 /etc/passwd
      ```
    - **说明**：`cut` 按分隔符 `:` 提取第一字段 `-f1`。

---

### 六、实际应用与综合练习（46-50）
46. **写一个 Shell 脚本，监控系统内存使用情况，当内存使用率超过 80% 时输出警告。**
    - **答案**：
      ```bash
      #!/bin/bash
      mem_usage=$(free | awk '/Mem/{printf("%.2f", $3/$2*100)}')
      if [ $(echo "$mem_usage > 80" | bc) -eq 1 ]; then
          echo "警告：内存使用率 $mem_usage% 超过 80%！"
      else
          echo "内存使用率：$mem_usage%"
      fi
      ```
    - **说明**：`free` 获取内存信息，`awk` 计算使用率，`bc` 比较浮点数。

47. **写一个 Shell 脚本，自动备份指定目录到 `/backup` 文件夹，并以当前日期命名备份文件。**
    - **答案**：
      ```bash
      #!/bin/bash
      src_dir="/path/to/source"
      backup_dir="/backup"
      date_str=$(date +%Y%m%d)
      tar -czvf "$backup_dir/backup_$date_str.tar.gz" "$src_dir"
      echo "备份完成：$backup_dir/backup_$date_str.tar.gz"
      ```
    - **说明**：`tar` 压缩备份，`date` 生成日期字符串。

48. **写一个 Shell 脚本，检查指定进程是否正在运行，若未运行则启动该进程。**
    - **答案**：
      ```bash
      #!/bin/bash
      process_name="nginx"
      if ! ps aux | grep -v grep | grep "$process_name" > /dev/null; then
          echo "$process_name 未运行，启动中..."
          systemctl start nginx
      else
          echo "$process_name 正在运行"
      fi
      ```
    - **说明**：`ps` 和 `grep` 检查进程，`systemctl` 启动服务。

49. **写一个 Shell 脚本，批量重命名当前目录下所有 `.txt` 文件，添加前缀 “backup_”。**
    - **答案**：
      ```bash
      #!/bin/bash
      for file in *.txt
      do
          mv "$file" "backup_$file"
      done
      echo "重命名完成"
      ```
    - **说明**：`for` 循环遍历文件，`mv` 重命名。

50. **写一个 Shell 脚本，模拟一个简单的用户管理系统，支持添加用户、删除用户和列出用户功能。**
    - **答案**：
      ```bash
      #!/bin/bash
      user_file="users.txt"
      add_user() {
          echo "$1" >> "$user_file"
          echo "用户 $1 已添加"
      }
      delete_user() {
          sed -i "/^$1$/d" "$user_file"
          echo "用户 $1 已删除"
      }
      list_users() {
          cat "$user_file"
      }
      case "$1" in
          "add")
              add_user "$2"
              ;;
          "delete")
              delete_user "$2"
              ;;
          "list")
              list_users
              ;;
          *)
              echo "用法：$0 {add|delete|list} [username]"
              ;;
      esac
      ```
    - **说明**：使用文件存储用户，函数实现功能，`case` 处理命令。
