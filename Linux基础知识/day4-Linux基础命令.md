# Linux基础命令实用教案
## 一、课程目标
1. 掌握常用的Linux命令，包括 echo、tail、head、ifconfig、tar、find 等。
2. 理解并学会重定向、管道操作。
3. 能够独立进行文件查找、打包、解包及网络配置等操作。
4. 具备实际动手能力，通过案例操作巩固命令用法。

## 1. echo命令 —— 输出字符串或变量值
echo 用于在终端输出指定的字符串、变量值或表达式结果。常用于脚本和命令行输出信息。

| 参数       | 作用说明                       | 示例                      |
|------------|-------------------------------|---------------------------|
| 无         | 直接输出内容                  | `echo hello`             |
| `-n`       | 输出时不换行                  | `echo -n "hello"`        |
| `-e`       | 解析转义字符（如 `\n`、`\t` 等） | `echo -e "hello\nworld"` |
| `$变量名`  | 输出变量的值                  | `echo $HOME`             |

echo命令: 用于切换目录.  [教学链接](https://www.linuxcool.com/echo)

### 常见用法举例
```bash
head /etc/passwd                 # 显示前10行
head -n 3 /etc/passwd            # 显示前3行
head -n 20 filename.txt          # 显示前20行

```

### 课后练习
* 用 echo 输出你的名字和年龄。
* 用 echo -e 输出两行内容，第二行内容为“Hello Linux”。
* 用 echo 输出当前用户（提示：$USER）。

```bash
# 用 echo 输出你的名字和年龄。
echo "姓名：张三，年龄：20"
# 用 echo -e 输出两行内容，第二行内容为“Hello Linux”。
echo -e "第一行内容\nHello Linux"
# 用 echo 输出当前用户（提示：$USER）。
echo $USER
```

## 2. head命令 —— 查看文件开头内容

head 用于显示文件的前若干行内容，默认显示前10行。

| 参数       | 作用说明                       | 示例                      |
|------------|-------------------------------|---------------------------|
| `-n 数字`  | 指定显示前多少行              | `head -n 5 filename.txt` |
| `-q`       | 多文件时不输出文件名头部      | `head -q file1 file2`    |
| `-v`       | 总是输出文件名头部            | `head -v file1 file2`    |

### 常见用法举例
```bash
head /etc/passwd                 # 显示前10行
head -n 3 /etc/passwd            # 显示前3行
head -n 20 filename.txt          # 显示前20行

```

### 课后练习
1. 创建一个包含10行内容的文本文件，用 head 查看前5行内容。
    * 创建 `vim   practise.txt`, 请将内容复制到文本中
    ```bash

    sed命令 – 批量编辑文本文件
    sdiff命令 – 以并排方式合并文件之间的差异
    gedit命令 – GNOME桌面的文本编辑器
    cat命令 – 在终端设备上显示文件内容
    let命令 – 执行一个或多个表达式
    fold命令 – 限制文件列宽 genisoimage命令 – 创建ISO镜像文件
    echo命令 – 输出字符串或提取后的变量值
    ed命令 – 文本编辑 ispell命令 – 用于拼写检查程序
    原文链接：https://www.linuxcool.com/tail
    ```
    * 使用命令`head -n 5 test.txt` 查看
2. 用 head -n 15 查看 /etc/passwd 的前15行。
    *  `head -n 15 /etc/passwd`
3. 用 head 查看两个文件的前3行，要求不显示文件名头部。
    * head -n 3 -q /var/log/apt/history.log /etc/passwd

## 3. tail命令 —— 查看文件结尾内容
tail 用于显示文件的最后若干行内容，默认显示最后10行。

| 参数       | 作用说明                           | 示例                         |
|------------|-----------------------------------|------------------------------|
| `-n 数字`  | 指定显示最后多少行                | `tail -n 5 filename.txt`    |
| `-f`       | 动态实时输出文件新增内容（如日志） | `tail -f /var/log/syslog`   |
| `-q`       | 多文件时不输出文件名头部          | `tail -q file1 file2`       |
| `-v`       | 总是输出文件名头部                | `tail -v file1 file2`       |

### 常见用法举例
```bash
tail /var/log/syslog                  # 显示最后10行
tail -n 20 filename.txt               # 显示最后20行
tail -f /var/log/syslog               # 实时输出日志文件内容

```

### 课后练习
1. 用 tail 查看 /etc/passwd 文件的最后8行。
    * `tail -n 8 /etc/passwd`
2. 用 tail -f 实时查看 /var/log/syslog 文件内容，并观察变化。
    * `tail -f /var/log/syslog`
    * 在打开一个终端使用echo 命令，为`/var/log/syslog` 添加内容
    * `echo "你能看见我的实时更新吗？" >> /var/log/syslog`
    * 观察`tail -f /var/log/syslog` 是否有数据在刷新
3. 用 tail 查看两个文件的最后2行，要求不显示文件名头部。
    * tail -n 2 -q /var/log/apt/history.log /etc/passwd


## 4. tar 命令教学
tar（tape archive）是 Linux 下最常用的归档和压缩工具之一，常用于文件或目录的打包、压缩、解压、查看等操作。

| 参数  | 作用说明                       | 备注/示例                        |
|-------|-------------------------------|----------------------------------|
| `-c`  | 创建归档（打包）              | `tar -cf file.tar dir/`         |
| `-x`  | 解包（释放归档）              | `tar -xf file.tar`             |
| `-t`  | 列出归档内容                  | `tar -tf file.tar`             |
| `-f`  | 指定归档文件名（必须最后写）  | `tar -cf file.tar dir/`        |
| `-z`  | 用 gzip 压缩/解压 (.gz)       | `tar -czf file.tar.gz dir/`    |
| `-j`  | 用 bzip2 压缩/解压 (.bz2)     | `tar -cjf file.tar.bz2 dir/`   |
| `-J`  | 用 xz 压缩/解压 (.xz)         | `tar -cJf file.tar.xz dir/`    |
| `-v`  | 显示详细过程（可选）          | `tar -cvf file.tar dir/`       |
| `-C`  | 切换到指定目录再操作          | `tar -C /etc -czf etc.tar.gz .`|

### tar常见压缩格式及区别
#### 为什么tar包有多种压缩格式？
* tar 本身只是“打包”工具，把多个文件或目录合成一个归档文件（.tar）。
* 但 tar 本身不压缩数据，所以常和压缩工具配合用。
* 常见的三种压缩工具分别是：gzip、bzip2、xz。

### 三种压缩方式对比
| 格式   | 参数  | 文件扩展名          | 速度   | 压缩率（压缩后体积） | 兼容性/用途                          |
|--------|-------|---------------------|--------|---------------------|--------------------------------------|
| gzip   | `-z`  | `.tar.gz` 或 `.tgz` | 快     | 一般                | 最常用，兼容性最好                   |
| bzip2  | `-j`  | `.tar.bz2`          | 较慢   | 高                  | 适合对压缩率要求高                   |
| xz     | `-J`  | `.tar.xz`           | 最慢   | 最高                | 新一代，体积最小，但速度慢           |

**说明**
* `gzip`：压缩速度最快，解压也快，适合日常备份和传输，默认推荐。
* `bzip2`：压缩速度稍慢，但压缩得更小，适合对体积要求高但速度不是第一需求的场合。
* `xz`：压缩率最高，压缩和解压都最慢，适合极限压缩（如软件发行包），但不适合大批量频繁操作。

### 图示总结
* 压缩速度：gzip > bzip2 > xz
* 压缩体积：xz < bzip2 < gzip

### 常见文件名后缀
* `.tar.gz` 或 `.tgz` ：tar打包 + gzip压缩
* `.tar.bz2` ：tar打包 + bzip2压缩
* `.tar.xz` ：tar打包 + xz压缩

### 基本语法
```bash
tar [选项] [归档文件名] [文件或目录名...]
```

### 选择建议
* 日常备份、传输：用 .tar.gz（速度快，兼容性好）
* 追求更小体积：用 .tar.bz2 或 .tar.xz
* 极限压缩：用 .tar.xz


### 常用打包与解包示例
```bash
# 1.1 打包为 .tar
tar -cf /root/test.tar /etc/passwd /home
mkdir /root/test_tar

# 1.2 打包为 .tar.gz（gzip压缩）
tar -zcf /root/test.tar.gz /etc/passwd /home
mkdir /root/test_gz

# 1.3 打包为 .tar.bz2（bzip2压缩）
tar -jcf /root/test.tar.bz2 /etc/passwd /home
mkdir /root/test_bz2

# 1.4 打包为 .tar.xz（xz压缩）
tar -Jcf /root/test.tar.xz /etc/passwd /home
mkdir /root/test_xz

```

### 查看归档内容
```bash
tar -tf /root/test.tar
tar -tf /root/test.tar.gz
tar -tf /root/test.tar.bz2
tar -tf /root/test.tar.xz
```

### 解包（释放归档）
```bash
# 3.1 解包到当前目录 -- 这个不练习
tar -xf /root/test.tar -C /root/test_tar

# 3.2 解包到指定目录 .tar.gz（gzip压缩）
tar -zxvf /root/test.tar.gz -C /root/test_gz/

# 3.2 解包到指定目录 .tar.gz（gzip压缩）
tar -jxvf /root/test.tar.bz2 -C /root/test_bz2/

# 3.2 解包到指定目录 .tar.gz（gzip压缩）
tar -Jxvf /root/test.tar.xz -C /root/test_xz/


```

### 高级用法
#### 1. -C 切换目录打包
```bash
# 只打包 /etc 目录下的 passwd 文件和 /etc/sysconfig/network-scripts/ 下的 ifcfg-lo 文件
tar -zcf /root/passwd.tar.gz -C /etc passwd -C /etc/sysconfig/network-scripts ifcfg-lo

# 创建解压缩文件夹
mkdir /root/passwd_gz

# 查看压缩文件
tar -tf /root/passwd_gz

# 指定位置，解压文件
tar -zxf /root/passwd.tar.gz -C /root/passwd_gz

```

#### 2. 多文件/多目录打包
```bash
# 指定压缩内容 passwd shells hosts fstab
tar -zcf /root/hosts.tar.gz -C /etc passwd shells hosts fstab

# 创建解压目录
mkdir /root/hosts_gz

# 查看压缩文件
tar -tf hosts_gz.tar.gz

# 解压文件到指定目录
tar -zxvf /root/hosts.tar.gz -C /root/hosts_gz

```

### 典型案例与作业
案例1：备份 /usr/local 目录为 bzip2 压缩包

**步骤**

1. 用 tar 把 /usr/local 目录打包为 /root/backup.tar.bz2，使用 bzip2 压缩。
2. 查看压缩包内容。
3. 解包到 /tmp/testbak 目录。

**标准答案**

```bash
# 1. 打包
tar -jcf /root/backup.tar.bz2 /usr/local

# 2. 查看内容
tar -tf /root/backup.tar.bz2

# 3. 解包到 /tmp/testbak
mkdir -p /tmp/testbak
tar -jxf /root/backup.tar.bz2 -C /tmp/testbak

```

### 清单式综合作业
**题目**

* 用 tar 把 /home 下所有内容打包为 /root/homebak.tar.xz，并用 xz 压缩。
* 查看该压缩包的内容。
* 解包到 /opt/homerestore 目录。
* 只解包 home 目录下的某个文件（比如 /home/youruser/.bashrc）到 /tmp/onlybashrc。

**参考答案**

```bash
# 1. 打包
tar -Jcf /root/homebak.tar.xz /home

# 2. 查看内容
tar -tf /root/homebak.tar.xz

# 3. 解包
mkdir -p /opt/homerestore
tar -Jxf /root/homebak.tar.xz -C /opt/homerestore

# 4. 只解包某个文件  shiqi 是我自己的用户名
mkdir -p /tmp/onlybashrc
tar -Jxf /root/homebak.tar.xz -C /tmp/onlybashrc home/shiqi/.bashrc

```

## 5. 文件查询命令find
find是Linux中非常强大的文件查找命令，可以根据文件名、类型、大小、时间、所有者等多种条件查找文件或目录，并可对查找到的结果进行后续处理。

### 常用参数表格
| 参数/格式                          | 作用说明                              | 示例及解释                                      |
|------------------------------------|--------------------------------------|------------------------------------------------|
| `find [目录]`                      | 查找指定目录下所有内容                | `find /etc` # 查找/etc下所有文件和目录         |
| `-type f`                          | 查找普通文件                         | `find /boot -type f`                          |
| `-type d`                          | 查找目录                             | `find /boot -type d`                          |
| `-type l`                          | 查找符号链接（快捷方式）             | `find /etc -type l`                           |
| `-name "文件名"`                   | 按名称查找（区分大小写）             | `find /etc -name "passwd"`                    |
| `-iname "文件名"`                  | 按名称查找（不区分大小写）           | `find /etc -iname "HOSTS"`                    |
| `-name "*.conf"`                   | 按后缀查找                           | `find /etc -name "*.conf"`                    |
| `-size +100k`                      | 查找大于100KB的文件                  | `find /boot -size +100k`                      |
| `-size -10M`                       | 查找小于10MB的文件                   | `find /boot -size -10M`                       |
| `-user 用户名`                     | 查找属于指定用户的文件               | `find /home -user natasha`                    |
| `-mtime +10`                       | 查找10天前修改过的文件               | `find /var -mtime +10`                        |
| `-mtime -7`                        | 查找最近7天内修改的文件              | `find /root -mtime -7`                        |
| `-exec 命令 {} \;`                 | 对查找到的每个文件执行命令           | `find /boot -size +10M -exec cp {} /mnt \;`   |
| `-o`                               | 或条件（满足任一条件）               | `find /mnt -name "cbd*" -o -type f`          |
| `wc -l`                            | 统计查找结果数量                     | （未提供具体示例）                            |
| `cat -n`                           | 给查找结果加行号                     | （未提供具体示例）                            |

### 重点命令讲解

#### 按类型查找
* 查找目录：find /usr -type d
* 查找文件：find /bin -type f
* 查找快捷方式：find /etc -type l

#### 按名称查找
* 精确查找：find /etc -name "passwd"
* 模糊查找：find /etc -name "*.conf"
* 忽略大小写：find /etc -iname "HOSTS"

#### 按大小查找
* 大于10M：find /boot -size +10M
* 小于1M：find /boot -size -1M
* 10M到50M之间：find /boot -size +10M -size -50M

#### 按用户查找
* find /home -user natasha

####  按修改时间查找
* 90天前：find /var -mtime +90
* 最近10天：find /root -mtime -10

#### 联合条件查找
* find /mnt -name "cbd*" -type d

#### 查找并处理（-exec）
* 查找大文件并复制：find /boot -size +10M -exec cp {} /mnt \;
* 查找所有者为student的文件并复制：
    * find / -user student -type f -exec cp {} /root/findfiles \;

### 课堂练习
1. 查找/etc目录下所有以.conf结尾的文件，并统计有多少个。
2. 查找/boot目录下大于1MB小于10MB的文件。
3. 查找/home目录下属于用户natasha的所有文件。
4. 查找/root目录下最近7天内修改过的文件。
5. 查找/opt目录下所有目录，并给结果加行号显示。
6. 查找/etc目录下所有符号链接文件。
7. 查找/mnt目录下所有以cbd开头的文件或目录。
8. 查找/boot下所有大于10M的文件，并将它们复制到/mnt目录。

**答案**

```bash
# 查找/etc目录下所有以.conf结尾的文件，并统计有多少个
find /etc -type f -name "*.conf" | wc -l

# 查找/boot目录下大于1MB小于10MB的文件
find /boot -type f -size +1M -size -10M

# 查找/home目录下属于用户natasha的所有文件
find /home -user natasha

# 查找/root目录下最近7天内修改过的文件
find /root -type f -mtime -7

# 查找/opt目录下所有目录，并给结果加行号显示
find /opt -type d | nl

# 查找/etc目录下所有符号链接文件
find /etc -type l

# 查找/mnt目录下所有以cbd开头的文件或目录
find /mnt -name "cbd*"

# 查找/boot下所有大于10M的文件，并将它们复制到/mnt目录
find /boot -type f -size +10M -exec cp {} /mnt/ \;

```

**说明：**

* 每条命令前都有注释，便于理解用途。
* 如需批量执行，可将内容保存为 .sh 文件并加上 #!/bin/bash 头部声明。
* 最后一条复制命令请确保 /mnt/ 目录存在且有写入权限。

## 6. Linux 重定向与管道操作

### 1. 重定向符号
#### （1）输出重定向 >
* 作用：将命令的标准输出写入到指定文件，覆盖原有内容。
* 例子：
    ```bash
    echo "Hello World" > hello.txt

    ```
    说明：把“Hello World”写入hello.txt文件（原内容会被覆盖）。

#### （2）追加重定向 >>
* 作用：将命令的标准输出追加到指定文件末尾，不覆盖原有内容。
* 例子：
    ```bash
    echo "Welcome" >> hello.txt

    ```
    说明：把“Welcome”添加到hello.txt文件末尾。

#### （3）输入重定向 <
* 作用：将文件内容作为命令的输入。
* 例子：
    ```bash
    wc -l < hello.txt
    ```
    说明：统计hello.txt文件的行数。

### 2. 管道符 |
* 作用：把前一个命令的输出，作为后一个命令的输入，实现多步处理。
* 例子：
    ```bash
    ls /etc | grep conf

    ```
    说明：列出/etc目录下所有文件，再筛选出包含“conf”的行。

### 3. 其他常用符号
#### （1）错误输出重定向 2>
* 作用：将命令的错误输出写入文件。
* 例子：
    ```bash
    ls /notexist 2> error.log

    ```
    说明：把ls命令的错误信息写入error.log。
  
#### （2）同时重定向标准输出和错误输出 &> (后面学哦)
* 例子：
```bash
command &> all.log

```
说明：标准输出和错误输出都写入all.log。


### 实例练习
#### 练习1：输出重定向与追加重定向
```bash
echo "This is a test." > test.txt      # 创建新文件
echo "Add another line." >> test.txt   # 追加内容

```

#### 练习2：输入重定向
```bash
wc -w < test.txt    # 统计test.txt文件的单词数

```

#### 练习3：管道符的使用
```bash
ls /etc | grep passwd       # 查找/etc目录下包含passwd的文件
ps aux | grep ssh           # 查找正在运行的ssh相关进程
find /etc -name "*.conf" | wc -l    # 统计以.conf结尾的文件数量

```

#### 练习4：错误输出重定向
```bash
ls /notexist 2> err.log
cat err.log

```

#### 练习5：结合find、grep、管道和重定向
```bash
find /etc -type f -name "*.conf" | grep network > network_conf.txt

```
说明：查找所有.conf文件名中包含network的文件，并保存到network_conf.txt。

## 8. 课后综合练习
1. 查找/etc目录下所有以.conf结尾的文件，把结果保存到conf_list.txt，并统计数量。
2. 查找/var/log下大于1M的文件，把文件名保存到logfiles.txt。
3. 查找/home下属于用户student的所有文件，并将结果追加到student_files.txt。
4. 查找/boot下所有大于10M的文件，并将它们复制到/mnt目录。
5. 使用管道将find命令的结果按行号显示（查找/opt下所有目录）。
6. 查找/etc目录下所有符号链接文件，并保存到symlinks.txt。
7. 查找/mnt目录下所有以cbd开头的文件或目录，并按行号显示。
8. 查找/root目录下最近7天内修改过的文件，并按行号显示。
9. 查找/etc下包含“root”关键字的.conf文件名，并保存到root_conf.txt。
10. 统计/etc目录下所有.conf文件中包含“network”关键字的行数。


## 9. ifconfig 与 ip addr 简介
### 1. ifconfig 工具
* 传统的网络配置和查看工具。
* 注意：Ubuntu 18.04及以后版本默认未安装，需要手动安装。
* 安装命令：
    ```bash
    sudo apt update
    sudo apt install net-tools
    ```
#### 常用参数
| 参数                     | 作用说明                     | 示例                                      |
|--------------------------|-----------------------------|-------------------------------------------|
| 无参数                   | 显示所有已激活网卡信息       | `ifconfig`                               |
| 网卡名                   | 显示指定网卡信息             | `ifconfig ens33`                         |
| `up`/`down`              | 启用/禁用指定网卡            | `ifconfig ens33 up`                      |
| `promisc`                | 设置混杂模式                 | `ifconfig ens33 promisc`                 |
| `hw ether XX:XX...`      | 修改 MAC 地址                | `ifconfig ens33 hw ether 00:11:22:33:44:55` |
| `mtu 数值`               | 修改 MTU                    | `ifconfig ens33 mtu 1400`                |

#### 输出内容解读
```bash
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::20c:29ff:fe16:1d3c  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:16:1d:3c  txqueuelen 1000  (Ethernet)
        RX packets 12345  bytes 1234567 (1.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 23456  bytes 2345678 (2.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

**主要字段说明：**

* `flags=...`：网卡状态（UP表示启用）
* `inet`：IPv4地址
* `netmask`：子网掩码
* `broadcast`：广播地址
* `inet6`：IPv6地址
* `ether`：MAC地址
* `RX/TX packets`：接收/发送的数据包数量
* `errors/dropped`：错误包和丢弃包计数


### 2. ip addr 工具
* 新一代网络管理工具，属于 iproute2 套件，Ubuntu默认已安装。
* 功能更强大，建议优先掌握。

#### 常用参数
| 参数/子命令              | 作用说明                     | 示例                                      |
|--------------------------|-----------------------------|-------------------------------------------|
| `addr` (或 `a`)          | 显示所有网卡 IP 地址信息     | `ip addr` 或 `ip a`                      |
| `addr show 网卡名`       | 显示指定网卡 IP 地址信息     | `ip addr show ens33`                     |
| `link`                   | 显示所有网卡的链路层信息     | `ip link`                                |
| `link set 网卡名 up`     | 启用指定网卡                 | `ip link set ens33 up`                   |
| `link set 网卡名 down`   | 禁用指定网卡                 | `ip link set ens33 down`                 |

#### 输出内容解读
以 ip addr show ens33 输出为例：

```bash
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:16:1d:3c brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic ens33
       valid_lft 86321sec preferred_lft 86321sec
    inet6 fe80::20c:29ff:fe16:1d3c/64 scope link 
       valid_lft forever preferred_lft forever

```

**主要字段说明：**

* `2`:：网卡编号
* `ens33:`：网卡名称
* `<...>`：网卡状态
* `mtu`：最大传输单元
* `link/ether`：MAC地址
* `inet`：IPv4地址（如 `192.168.1.100/24`，`/24`代表子网掩码）
* `brd`：广播地址
* `scope`：作用范围（global全局，link链路本地）
* `dynamic`：动态分配（DHCP获取）
* `inet6`：IPv6地址


### 3. 对比与建议
* ifconfig：命令简洁，输出直观，适合新手和老系统。
* ip addr：功能更强大，输出更详细，支持更多新特性，推荐优先掌握。

### 4. 实操举例
* 查看所有网卡信息
```bash
ifconfig
ip addr

```

* 查看指定网卡信息
```bash
ifconfig ens33
ip addr show ens33


```

* 启用/禁用网卡
```bash
sudo ifconfig ens33 up
sudo ifconfig ens33 down

sudo ip link set ens33 up
sudo ip link set ens33 down


```

### 重点来了 - 动态IP（DHCP）配置
#### 1. 确认网卡名称
常见的网卡名有：`eth0`、`ens33`、`enp0s3` 等。
```bash
ip link

```

#### 2. 配置文件位置
* Ubuntu 18.04 及以后默认使用 Netplan 管理网络配置，配置文件通常在 `/etc/netplan/` 目录下，如：
    ```bash
    /etc/netplan/01-netcfg.yaml
    ```
* `01-netcfg.yaml`: 这个名字是我随便起的，只要能保证 `.yaml` 结尾，你取什么名字无所谓

#### 3. 编辑Netplan配置文件为DHCP
假设网卡名为 ens33，编辑配置文件：
```bash
sudo vim /etc/netplan/01-netcfg.yaml

```

**内容示例（DHCP）：**

```bash
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:
      dhcp4: true

```

#### 4. 应用配置
```bash
sudo netplan apply

```

#### 5. 验证是否获取到IP
```bash
ip addr show ens33
ifconfig ens33
```


### 重点（必会）静态IP配置

#### 编辑Netplan配置文件为静态IP
假设要配置IP为 `192.168.1.100`，网关为 `192.168.1.1`，DNS为 `8.8.8.8`，子网掩码为 `/24`。

**文件内容解释**
| 字段                             | 作用说明                                                                                      | 示例                          |
|----------------------------------|---------------------------------------------------------------------------------------------|-------------------------------|
| `network:`                       | 网络配置文件的根节点，所有网络相关设置都写在这里                                             | `network:`                    |
| `version: 2`                     | Netplan 配置文件的版本号，目前一般固定写2                                                    | `version: 2`                  |
| `renderer: networkd`             | 指定网络管理的后端方式，`networkd`适合服务器，`NetworkManager`适合桌面环境                   | `renderer: networkd`          |
| `ethernets:`                     | 以太网（有线网卡）的配置块，下面写具体网卡名                                                 | `ethernets:`                  |
| `ens33:`                         | 具体要配置的网卡名，要和实际网卡名一致（用`ip link`查）                                      | `ens33:`                      |
| `dhcp4: true/false`              | 是否启用IPv4的DHCP自动分配（true=自动获取，false=手动指定）                                  | `dhcp4: false`                |
| `addresses:`                     | 要分配给网卡的静态IP地址，格式为`IP/掩码位数`，如`192.168.1.100/24`                         | `addresses: [192.168.1.100/24]`|
| `gateway4:`                      | 默认网关（路由器的IP地址）                                                                   | `gateway4: 192.168.1.1`       |
| `nameservers:`                   | DNS服务器配置块，下面用`addresses:`列出DNS服务器                                             | `nameservers:`                |
| `addresses: [8.8.8.8, ...]`      | DNS服务器IP地址列表，多个用逗号分隔                                                          | `addresses: [8.8.8.8, 114.114.114.114]` |

* 编辑 `vim  /etc/netplan/01-netcfg.yaml`
* 文本内容
    ```bash
    network:
      version: 2
      renderer: networkd
      ethernets:
        ens33:
          dhcp4: false
          addresses:
            - 192.168.1.100/24
          gateway4: 192.168.1.1
          nameservers:
            addresses: [8.8.8.8, 114.114.114.114]
    ```

* 应用配置
```bash
sudo netplan apply
```

* 验证
```bash
ip addr show ens33
# 或者
ifconfig ens33
```


### 常见问题与注意事项
* 编辑Netplan配置文件时注意缩进（用空格不用Tab），否则会报错！
* 配置静态IP时，dhcp4 一定要设为 false。
* 每次修改后都要用 sudo netplan apply 应用配置。
* 如果配置错误，网络可能中断，可用虚拟机快照或事先备份配置文件。

## 综合练习答案
```bash
# 课后综合练习（含答案）

1. 查找/etc目录下所有以.conf结尾的文件，把结果保存到conf_list.txt，并统计数量。
find /etc -type f -name "*.conf" | tee conf_list.txt | wc -l

2. 查找/var/log下大于1M的文件，把文件名保存到logfiles.txt。
find /var/log -type f -size +1M > logfiles.txt

3. 查找/home下属于用户student的所有文件，并将结果追加到student_files.txt。
find /home -user student >> student_files.txt

4. 查找/boot下所有大于10M的文件，并将它们复制到/mnt目录。
find /boot -type f -size +10M -exec cp {} /mnt/ \;

5. 使用管道将find命令的结果按行号显示（查找/opt下所有目录）。
find /opt -type d | nl

6. 查找/etc目录下所有符号链接文件，并保存到symlinks.txt。
find /etc -type l > symlinks.txt

7. 查找/mnt目录下所有以cbd开头的文件或目录，并按行号显示。
find /mnt -name "cbd*" | nl

8. 查找/root目录下最近7天内修改过的文件，并按行号显示。
find /root -type f -mtime -7 | nl

9. 查找/etc下包含“root”关键字的.conf文件名，并保存到root_conf.txt。
find /etc -type f -name "*.conf" | xargs grep -l "root" > root_conf.txt

10. 统计/etc目录下所有.conf文件中包含“network”关键字的行数。
find /etc -type f -name "*.conf" | xargs grep -c "network"

```