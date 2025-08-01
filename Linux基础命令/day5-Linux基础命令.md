# Linux常用命令与系统管理基础

## 课程目标

1. 掌握系统管理命令
   * 熟练使用man查看命令帮助
   * 掌握date和history命令的应用
   * 学会使用df、lsblk查看系统资源

2. 掌握文件管理技能
   * 熟练使用zip进行文件压缩管理
   * 掌握软链接和硬链接的创建与管理
   * 理解文件系统的基本概念

3. 掌握软件包管理
   * 熟练使用apt/rpm管理软件包
   * 掌握软件源的配置和优化
   * 培养系统维护的实践能力


## 第一部分：常用基础命令学习

### 1. man 命令
#### 命令解释
`man` 是 Linux 系统下的帮助查看工具，用于查看命令的使用手册。

#### 参数表格
```bash
| 参数      | 作用                      |
| --------- | ------------------------- |
| man 1     | 查看用户命令手册          |
| man 5     | 查看文件格式手册          |
| man -k    | 按关键字搜索命令手册      |
| man -f    | 显示命令的简短描述        |

```

#### 语法举例
```bash
man ls           # 查看ls命令的帮助文档
man -k copy      # 搜索所有与copy相关的命令
man 5 passwd     # 查看passwd文件的格式说明

```

#### 练习
1. 使用 man 命令查看 df 命令的帮助文档。
2. 使用 man -k 搜索与“disk”相关的命令。

### 2. date 命令

#### 命令解释
`date` 用于显示或设置系统的日期和时间。

#### 参数表格
```bash
| 参数        | 作用                          |
| ----------- | ----------------------------- |
| date        | 显示当前日期和时间            |
| date '+%Y-%m-%d %H:%M:%S' | 按指定格式显示时间 |
| date -s     | 设置系统日期和时间            |

```

#### 语法举例
```bash
date                   # 显示当前日期和时间
date '+%Y-%m-%d'       # 只显示年月日
date -s "2024-06-24 10:00:00"  # 设置系统时间

```

#### 练习
1. 使用 `date` 命令显示当前时间。
2. 用 `date` 命令只显示当前的小时和分钟。

### 3. history 命令
#### 命令解释
`history` 用于显示历史命令记录。

#### 参数表格
```bash
| 参数      | 作用                        |
| --------- | --------------------------- |
| history   | 显示历史命令列表            |
| history n | 显示最近的n条历史命令       |
| !n        | 执行第n条历史命令           |
| !!        | 执行上一条命令              |

```

#### 语法举例
```bash
history           # 显示所有历史命令
history 10        # 显示最近10条命令
!100              # 执行第100条命令
!!                # 再次执行上一条命令

```

#### 练习
1. 查看最近20条历史命令。
2. 尝试用 !! 快捷键执行上一条命令。

### 4. df 命令

#### 命令解释
`df` 用于显示文件系统的磁盘空间占用情况。

#### 参数表格
```bash
| 参数      | 说明                                         |
| --------- | -------------------------------------------- |
| -a        | 显示所有文件系统                             |
| -h        | 以更易读的方式显示（如GB、MB）               |
| -H        | 以1KB=1000B为换算单位                        |
| -i        | 显示索引字节信息                             |
| -k        | 设置显示时的块大小                           |
| -l        | 只显示本地文件系统                           |
| -t        | 只显示指定类型文件系统                       |
| -T        | 显示文件系统的类型                           |
| --sync    | 在获取磁盘使用信息前先执行sync同步命令        |


```

#### 语法举例
```bash
df -h            # 以人类可读方式显示磁盘使用情况
df -a            # 显示所有文件系统
df -i            # 显示索引节点信息
df -T            # 显示文件系统类型
df -l            # 只显示本地文件系统
df -t ext4       # 只显示ext4类型的文件系统
df --sync        # 先同步，再显示磁盘信息

```

#### df -Th 示例输出
假设你输入以下命令：

```bash
df -Th

```

你可能会看到类似如下的输出：

```bash
文件系统         类型      容量  已用  可用 已用% 挂载点
/dev/sda1       ext4      50G   20G   28G   42%  /
tmpfs           tmpfs     2.0G   0B   2.0G   0%  /dev/shm
/dev/sdb1       ntfs     100G   60G   40G   60%  /data

```

#### 每一列的详细解释

| 列名       | 英文名         | 说明                                           |
|------------|----------------|------------------------------------------------|
| 文件系统   | Filesystem     | 设备名称或挂载的分区名，比如 `/dev/sda1`, `tmpfs` 等。 |
| 类型       | Type           | 文件系统的类型，如 `ext4`、`ntfs`、`tmpfs` 等。      |
| 容量       | Size           | 分区或挂载点的总容量（以人类可读的方式显示，如 `G`、`M` 等）。 |
| 已用       | Used           | 已经被使用的空间。                              |
| 可用       | Avail          | 还可以使用的空间。                              |
| 已用%      | Use%           | 已用空间的百分比。                              |
| 挂载点     | Mounted on     | 该文件系统被挂载到的目录。                      |


### lsblk 命令

#### 命令解释

| 参数      | 说明                                     |
| --------- | ---------------------------------------- |
| -a        | 显示所有设备（包括空设备）               |
| -b        | 以字节为单位显示设备大小                 |
| -d        | 只显示磁盘设备，不显示分区               |
| -e <ID>   | 排除指定设备（以设备号或名称）           |
| -f        | 显示文件系统相关信息                     |
| -l        | 以列表（长列表）方式显示                 |
| -n        | 不显示表头                               |
| -o <列名> | 指定显示的列（如NAME,SIZE,TYPE,MOUNTPOINT）|
| -p        | 显示设备的完整路径（如/dev/sda）         |
| -r        | 以原始格式显示设备树                     |
| -t        | 显示拓扑结构                             |
| -J        | 以JSON格式输出                           |
| -P        | 以键值对（property）格式输出             |
| -h        | 显示帮助信息                             |

#### 常用命令示例
```bash
lsblk                # 默认以树状结构显示所有块设备
lsblk -f             # 显示文件系统类型、UUID等信息
lsblk -a             # 显示所有块设备，包括空设备
lsblk -d             # 只显示磁盘本身，不显示分区
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT  # 自定义显示列
lsblk -p             # 显示完整设备路径
lsblk -J             # 以JSON格式输出
lsblk -P             # 以键值对格式输出

```

#### 输出内容解释
默认输出一般包含以下列：

**假设命令：**

```bash
lsblk
```

**输出：**

```bash
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0  100G  0 disk
├─sda1   8:1    0   50G  0 part /
├─sda2   8:2    0   30G  0 part /data
└─sda3   8:3    0   20G  0 part [SWAP]
sdb      8:16   1   16G  0 disk
└─sdb1   8:17   1   16G  0 part /mnt/usb

```

* sda：第一个硬盘，100G
    * sda1：第一个分区，50G，挂载在根目录/
    * sda2：第二个分区，30G，挂载在/data
    * sda3：第三个分区，20G，作为交换分区[SWAP]
* sdb：第二块盘（比如U盘），16G
    * sdb1：分区，16G，挂载在/mnt/usb

### 综合练习
#### 1. 使用 lsblk 和 df 命令查看磁盘分区和空间使用情况，并保存到 disk_info.txt
**结题思路**

* lsblk 用于显示块设备信息（如磁盘分区结构）。
* df 用于显示文件系统的磁盘空间使用情况。
* 使用重定向或追加将输出保存到文件 disk_info.txt。

**答案（命令）**

```bash
lsblk > disk_info.txt
df -h >> disk_info.txt

```

**说明：**
* > 表示覆盖写入，>> 表示追加写入。
* df -h 以人类可读的方式显示磁盘使用情况。

#### 2. 使用 history 查找最近的 date 命令，并用 man 查阅 date 用法

**结题思路**

* history 显示历史命令记录，可以用 grep 筛选包含特定关键字的命令。
* man 查看命令的详细手册。

**答案（命令）**

```bash
history | grep date
man date

```

**说明：**

* history | grep date 查找历史中包含 date 的命令。
* man date 打开 date 命令的使用手册。

##### 3. 使用 date 输出当前时间，格式为“年-月-日 时:分:秒”

**结题思路**

* date 命令可以用 + 参数自定义输出格式。
* 格式字符串 %Y-%m-%d %H:%M:%S 分别对应年、月、日、时、分、秒。

**答案（命令）**

```bash
date "+%Y-%m-%d %H:%M:%S"

```

## 二 unzip命令 – 解压缩zip格式文件
* `unzip` 命令用于解压缩zip格式的文件
* `zip` 归档工具，跨平台（Windows与Linux）
* `lrzsz` 用于 Linux 下与 Windows 进行文件传输

### sudo apt update
#### Ubuntu/Debian 系统
```bash
sudo apt install unzip zip lrzsz -y
```

#### CentOS/RHEL 系统
```bash
sudo yum install unzip zip lrzsz -y
```

#### 检查安装情况
```bash
unzip -v
zip -v
sz --version
rz --version
```

#### zip 文件压缩与解压

| 命令   | 主要参数 | 含义说明                     |
|--------|----------|------------------------------|
| zip    | -r       | 递归压缩整个目录             |
| zip    | -q       | 安静模式，不显示压缩过程     |
| zip    | -e       | 压缩时加密，需要输入密码     |
| unzip  | -d       | 指定解压目标目录             |
| unzip  | -l       | 查看 zip 包内文件列表        |
| unzip  | -o       | 解压时自动覆盖已存在的文件   |

#### rz 与 sz 结合操作流程表

| 步骤 | 操作命令        | 作用说明                       | 交互内容/注意事项             |
|------|----------------|-------------------------------|-------------------------------|
| 1    | `rz`           | 从本地上传文件到Linux服务器    | 终端弹窗，选择要上传的文件    |
| 2    | `ls`           | 查看上传的文件是否存在         | 确认文件已上传                |
| 3    | `unzip xxx.zip`| （可选）解压上传的zip文件      | 解压后可进行后续操作          |
| 4    | `sz filename`  | 从Linux服务器下载文件到本地    | 终端弹窗，选择保存位置        |

#### 1. 在Linux上压缩目录或文件
假设要压缩目录 /home：

* -r：递归压缩整个目录

```bash
zip -r project.zip /home

```

#### 2. 用 sz 命令将压缩包下载到Windows
```bash
sz project.zip

```

此时终端会弹窗，选择保存位置，将 project.zip 下载到本地 Windows 电脑。

#### 3. 在Windows上重命名压缩包
在 Windows 文件管理器中，将 project.zip 改名为 myproject.zip（或其他你想要的名字）。

#### 4. 用 rz 命令上传压缩包到Linux
在Linux终端输入：

```bash
rz

```

弹窗后，选择刚刚重命名的 myproject.zip，上传到当前目录。

#### 5. 将压缩包解压到指定目录
假设你要解压到 /home/user/testdir，需要先确保目标目录存在：

```bash
mkdir -p /home/user/testdir

```

然后执行：

```bash
unzip myproject.zip -d /home/user/testdir

```

* -d 后面跟解压目标路径

#### 6. 检查解压结果
```bash
# 确认文件已正确解压到指定目录
ls /home/user/testdir

```

### ln 软硬链接
`ln` 命令用于为文件创建链接。

* 硬链接（Hard Link）：指向文件数据本身，删除原文件不会影响硬链接。
* 软链接（符号链接，Soft Link/Symbolic Link）：类似 Windows 的快捷方式，指向文件路径，原文件删除后软链接失效。

#### 参数表格
| 参数  | 含义说明                       |
|-------|--------------------------------|
| -s    | 创建软（符号）链接             |
| -f    | 强制创建（覆盖已有的目标文件） |
| -v    | 显示详细操作过程               |
| -n    | 把目标视为普通文件             |


#### 常用命令与案例

##### （1）创建硬链接
```bash
# 创建一个空文件
touch /root/main.txt
# 使用硬链接
ln /root/main.txt /tmp/main-hardlink.txt
# 查看文件
ls -l /tmp/main-hardlink.txt
# 删除文件
rm -rf /tmp/main-hardlink.txt
# 再次检查原来的文件还来吗？
ls -l /root/main.txt

```

* 作用：为 main.txt 创建一个名为 main-hardlink.txt 的硬链接。

##### （2）创建软链接
```bash
ln -s source.txt softlink.txt
# 创建一个空文件
touch /root/main.txt
# 使用软链接
ln /root/main.txt /tmp/main-softlink.txt
# 查看文件
ls -l /tmp/main-softlink.txt
# 删除文件
rm -rf /tmp/main-softlink.txt
# 再次检查原来的文件还来吗？
ls -l /root/main.txt
```
* 作用：为 source.txt 创建一个名为 softlink.txt 的软链接。

### 硬链接与软链接的区别


| 区别点            | 硬链接                      | 软链接（符号链接）          |
|-------------------|-----------------------------|-----------------------------|
| 是否跨文件系统    | 否                          | 是                          |
| 是否可链接目录    | 否（普通用户）              | 是                          |
| 原文件删除影响    | 不影响，内容仍可访问        | 影响，链接失效              |
| 是否有独立 inode  | 是                          | 否，指向原文件路径          |

### 练习作业
1. 创建一个文本文件 test.txt，分别为其创建硬链接和软链接，并验证删除原文件后的链接行为。
    * 创建 test.txt 文件 `echo "hello world" > test.txt`
    * 创建硬链接  `ln test.txt hardlink.txt`
    * 创建软链接  `ln -s test.txt softlink.txt`

2. 使用 ls -li 查看 inode 号，体会硬链接与软链接的区别。
    * 用 ls -li 查看 inode 号  `ls -li`
        *  发现 test.txt 和 hardlink.txt 的 inode 号相同，softlink.txt 不同。
    * 删除原文件 `rm test.txt 验证链接
        * `cat hardlink.txt `  还能看到内容
        * `cat softlink.txt`  报错，找不到目标


## Ubuntu 软件包管理系统：dpkg 与 apt 详解

在 Ubuntu 系统中，软件的安装、卸载和管理主要依赖于两个工具：`dpkg` 和 `apt`。它们是 Debian 系 Linux 发行版（比如 Ubuntu）的核心包管理工具。下面我们先从理论入手，搞清楚它们的概念和区别，再通过实际例子一步步学习操作。

## 理论基础：dpkg 和 apt 是什么？

### 什么是 dpkg？
- **dpkg**（Debian Package）是 Debian 系 Linux 的基础包管理工具，直接操作 `.deb` 格式的软件包文件。
- **作用**：负责软件包的安装、卸载、查询等基本操作，但它不会自动处理依赖关系（比如安装某个软件时需要的其他软件）。
- **特点**：适合手动管理单个软件包，操作比较底层，适合对系统有深入了解的用户。
- **局限**：如果软件有复杂的依赖关系，`dpkg` 可能会报错，需要用户手动解决。

### 什么是 apt？
- **apt**（Advanced Package Tool）是建立在 `dpkg` 之上的高级包管理工具，相当于 `dpkg` 的“智能助手”。
- **作用**：不仅能安装、卸载软件包，还能自动处理依赖关系，从软件源（在线仓库）下载软件包，并支持系统整体升级。
- **特点**：用户友好，操作简单，适合日常使用。大多数情况下，我们都用 `apt` 而不是直接用 `dpkg`。
- **常见场景**：想安装一个软件（比如 `vim` 编辑器），用 `apt` 直接从网上下载并安装，省时省力。

### dpkg 和 apt 的关系与区别
- **关系**：`apt` 是前端工具，底层实际上调用 `dpkg` 来完成软件包的安装和卸载。
- **区别**：
  - `dpkg` 直接操作本地的 `.deb` 文件，无法自动下载软件或解决依赖。
  - `apt` 连接在线软件源，自动下载软件包、解决依赖问题。
- **简单比喻**：`dpkg` 就像手动组装家具，`apt` 像是请了个装修队，帮你搞定一切。

## dpkg 包管理基础

`dpkg` 是最底层的包管理工具，主要用于处理本地的 `.deb` 软件包文件。下面是常用命令和实际操作。

### dpkg 常用参数表格

| 参数        | 含义说明                           | 使用场景示例                     |
|-------------|------------------------------------|----------------------------------|
| `-i`        | 安装软件包                         | 安装一个下载好的 `.deb` 文件     |
| `-r`        | 移除软件包但保留配置               | 卸载软件但想保留设置以便重装     |
| `-P`        | 完全移除软件包及其配置             | 彻底删除软件及所有相关配置       |
| `-l`        | 列出所有已安装的软件包             | 查看系统里装了哪些软件           |
| `-L`        | 显示软件包安装的所有文件           | 想知道某个软件装了哪些文件       |
| `-s`        | 显示已安装软件包的状态信息         | 检查某个软件是否安装及版本信息   |
| `-S`        | 查找指定文件属于哪个软件包         | 找到某个命令或文件来自哪个包     |
| `-c`        | 列出软件包中的文件（不安装）       | 查看 `.deb` 文件包含的内容      |
| `-I`        | 显示软件包信息（不安装）           | 查看 `.deb` 文件的版本、描述等   |
| `--configure`| 配置未完成配置的软件包             | 修复安装过程中断的软件配置       |

### 实际操作：dpkg 的简单例子

很多同学反馈找不到 `.deb` 文件来练习，别急，咱们可以用一个简单的软件包来做实验，比如 `hello`（一个简单的测试程序）。下面是完整的步骤，包括如何获取一个 `.deb` 文件。

#### 步骤1：获取一个简单的 `.deb` 包
我们可以通过 Ubuntu 的软件源下载一个简单的 `.deb` 文件，而不需要自己去网上找。
```bash
# 先更新软件源，确保能找到最新的软件包
apt update
# 使用 apt 下载 hello 软件包，但不安装，保存到本地
apt download hello
# 下载后，hello 的 .deb 文件会出现在当前目录下
ls
# 你会看到类似 hello_2.10-2ubuntu4_amd64.deb 的文件
```

#### 步骤2：安装 `.deb` 包
假设下载的文件名叫 `hello_2.10-2ubuntu4_amd64.deb`，用 `dpkg` 安装：
```bash
dpkg -i hello_2.10-2ubuntu4_amd64.deb
# -i 表示安装，如果有依赖问题可能会报错
```
如果遇到依赖问题（比如缺少某些包），可以用下面命令修复：
```bash
apt install -f
# 这会自动安装缺少的依赖
```

#### 步骤3：验证安装
安装后，运行 `hello` 命令看看是否成功：
```bash
hello
# 输出类似 "Hello, world!" 的内容，说明安装成功
```

#### 步骤4：查询已安装包信息
```bash
dpkg -s hello
# -s 显示 hello 软件包的状态信息，比如版本、描述等
```

#### 步骤5：查看软件包包含的文件
```bash
dpkg -L hello
# -L 列出 hello 软件包安装的所有文件，比如 /usr/bin/hello
```

#### 步骤6：卸载软件包
```bash
sudo dpkg -r hello
# -r 卸载 hello 软件包，但保留配置文件
```

#### 步骤7：完全卸载（包括配置）
```bash
sudo dpkg -P hello
# -P 彻底删除 hello 软件包及其配置文件
```

### dpkg 实用技巧
- **找不到 `.deb` 文件怎么办？** 除了用 `apt download` 获取，你也可以去官方网站下载，比如从 [Debian 软件包仓库](https://packages.debian.org/) 搜索并下载。
- **依赖问题怎么办？** 如果 `dpkg -i` 报错缺少依赖，用 `sudo apt install -f` 自动修复，或者改用 `apt` 直接安装。

### dpkg 练习作业（更贴近实际）
1. 下载一个简单的软件包（如 `hello`）并用 `dpkg` 安装：
   ```bash
   sudo apt download hello
   sudo dpkg -i hello_*.deb
   ```
2. 查询系统中所有已安装的软件包（只看前几行）：
   ```bash
   dpkg -l | head
   ```
3. 查询 `/bin/ls` 属于哪个软件包：
   ```bash
   dpkg -S /bin/ls
   ```
4. 查看 `bash` 包包含哪些文件：
   ```bash
   dpkg -L bash
   ```
5. 卸载 `hello` 软件包，但保留配置文件：
   ```bash
   sudo dpkg -r hello
   ```
6. 完全卸载 `hello` 软件包（包括配置文件）：
   ```bash
   sudo dpkg -P hello
   ```
7. 查看下载的 `.deb` 包详细信息（不安装）：
   ```bash
   dpkg -I hello_*.deb
   ```

## apt 软件包管理与国内源配置

`apt` 是更高级的工具，日常使用中我们更多依赖它来管理软件包。它能从在线软件源下载软件，自动解决依赖问题，操作更方便。

### apt 常用命令参数表
| apt 命令             | 功能                         | 使用场景示例                     |
|----------------------|------------------------------|----------------------------------|
| `apt install`        | 安装一个软件包               | 安装 `vim` 编辑器               |
| `apt remove`         | 移除一个软件包               | 卸载 `vim`，保留配置            |
| `apt purge`          | 移除包及相关配置             | 彻底删除 `vim` 及配置           |
| `apt update`         | 刷新仓库索引                 | 更新软件源列表，确保获取最新包  |
| `apt upgrade`        | 升级所有可升级的软件包       | 保持系统软件最新（谨慎操作）    |
| `apt autoremove`     | 移除多余的软件包             | 清理不再需要的依赖包            |
| `apt full-upgrade`   | 升级软件包并处理依赖         | 系统大版本升级（谨慎操作）      |
| `apt search`         | 搜索某个程序                 | 查找 `nginx` 相关软件包         |
| `apt show`           | 显示软件包详情               | 查看 `vim` 的版本、描述等       |
| `apt list --installed`| 列出已安装的软件包          | 查看系统装了哪些软件            |

### 为什么配置国内源？
- **默认软件源问题**：Ubuntu 默认使用国外的软件源，下载速度慢，尤其在国内网络环境下。
- **国内源优势**：使用国内镜像源（如阿里云、中科大源）可以大幅提高下载速度。
- **配置时机**：新装系统后，第一时间配置国内源。

### 配置国内源（以阿里云源为例）
下面以 Ubuntu 24.04 为例，配置阿里云源：
```bash
# 备份原有源文件，防止出错后无法恢复
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
# 编辑源文件，替换为国内源
sudo vim /etc/apt/sources.list
# 清空文件内容，粘贴以下内容（适用于 Ubuntu 24.04 Noble Numbat）
deb https://mirrors.aliyun.com/ubuntu/ noble main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ noble-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-security main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ noble-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-updates main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ noble-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-backports main restricted universe multiverse
# 保存并退出 vim 编辑器
# 更新软件源索引
sudo apt update
```

**注意**：如果是其他 Ubuntu 版本（如 22.04），把 `noble` 替换成对应的代号（如 `jammy`）即可。代号可以在 `/etc/os-release` 文件中查看。

### apt 实际操作：以安装 `curl` 为例
`curl` 是一个常用的下载工具，下面用它来演示 `apt` 的基本操作。

#### 步骤1：更新软件源
```bash
sudo apt update
# 确保软件包列表是最新的
```

#### 步骤2：安装软件包
```bash
sudo apt install curl
# 安装 curl，apt 会自动处理依赖
```

#### 步骤3：验证安装
```bash
curl --version
# 输出 curl 的版本信息，说明安装成功
```

#### 步骤4：查看软件包详情
```bash
apt show curl
# 显示 curl 的版本、描述、大小等信息
```

#### 步骤5：卸载软件包
```bash
sudo apt remove curl
# 卸载 curl，但保留配置文件
```

#### 步骤6：彻底卸载（包括配置）
```bash
sudo apt purge curl
# 彻底删除 curl 及配置文件
```

#### 步骤7：清理无用依赖
```bash
sudo apt autoremove
# 删除安装 curl 时带来的不再需要的依赖包
```

### apt 练习作业（简单实用）
1. 使用 `apt` 安装 `tree` 软件包（一个显示目录结构的工具）：
   ```bash
   sudo apt update
   sudo apt install tree
   tree /etc  # 测试一下，显示 /etc 目录结构
   ```
2. 搜索仓库中的 `git` 相关软件包：
   ```bash
   apt search git
   ```
3. 卸载 `tree` 软件包，并验证其状态：
   ```bash
   sudo apt remove tree
   apt show tree
   ```
4. 自动清理无用依赖包：
   ```bash
   sudo apt autoremove
   ```
5. 使用 `apt show` 查看 `vim` 软件包的详细信息：
   ```bash
   apt show vim
   ```
6. 列出所有已安装的软件包（只看前几行）：
   ```bash
   apt list --installed | head
   ```

## 总结与常见问题解答

### 总结
- **`dpkg`**：基础工具，适合处理本地 `.deb` 文件，手动管理软件包。
- **`apt`**：高级工具，连接软件源，自动处理依赖，日常使用首选。
- **建议**：新手优先用 `apt`，简单高效；需要处理离线安装时再用 `dpkg`。

### 常见问题
1. **找不到 `.deb` 文件怎么办？**
   - 用 `apt download 软件名` 获取一个简单的包来练习。
   - 或者从官网下载，比如 [Ubuntu 软件包](https://packages.ubuntu.com/)。
2. **安装报错“缺少依赖”怎么办？**
   - 用 `sudo apt install -f` 自动修复依赖。
   - 或者直接用 `apt install 软件名` 替代 `dpkg`。
3. **软件源更新失败怎么办？**
   - 检查网络是否正常。
   - 确保配置的国内源地址正确，或者换一个源（如中科大、清华源）。
4. **如何选择软件源？**
   - 国内用户推荐阿里云、清华源、中科大源，速度快且稳定。

---