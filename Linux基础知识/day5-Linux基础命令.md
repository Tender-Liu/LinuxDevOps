# Linux常用命令与系统管理基础

## 课程目标
1. 掌握Linux系统中常用命令的基本用法，包括man、date、history、df、lsblk等。
2. 熟悉文件压缩与解压缩操作，能够使用zip命令进行文件管理。
3. 理解并能实际操作软链接与硬链接（ln命令）。
4. 了解并掌握常见的软件包管理工具（rpm和apt）的基本用法。
5. 能够配置apt国内源，加快软件安装与更新速度。
6. 培养使用命令行进行系统管理和日常维护的能力，为后续深入学习Linux打下坚实基础。


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
lsz --version
lrz --version
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


## apt 软件安装以及国内源配置
rpm命令 在Linux系统下对软件包进行安装、卸载、查询、验证、升级等工作，常见的主流系统（如RHEL、CentOS、Fedora等）都采用这种软件包管理器，推荐用固定搭配“rpm-ivh 软件包名”安装软件，而卸载软件则用固定搭配“rpm -evh 软件包名”，简单好记又好用。

### rpm 常用参数表格

| 参数   | 含义说明                           |
|--------|------------------------------------|
| -a     | 显示所有软件包                     |
| -c     | 仅显示组态配置文件                 |
| -d     | 仅显示文本文件                     |
| -e     | 卸载软件包                         |
| -f     | 显示文件或命令属于哪个软件包       |
| -h     | 安装软件包时显示标记信息           |
| -i     | 安装软件包                         |
| -l     | 显示软件包的文件列表               |
| -p     | 显示指定的软件包信息               |
| -q     | 显示指定软件包是否已安装           |
| -R     | 显示软件包的依赖关系               |
| -s     | 显示文件状态信息                   |
| -U     | 升级软件包                         |
| -v     | 显示执行过程信息                   |
| -vv    | 显示执行过程详细信息               |

### 安装 rpm 包
```bash
# 安装一个本地 rpm 包
sudo rpm -ivh example.rpm
# -i 表示安装，-v 显示详细信息，-h 显示进度条

```

### 升级 rpm 包
```bash
sudo rpm -Uvh example.rpm
# -U 表示升级（如果未安装则安装），-v 和 -h 同上

```

### 卸载 rpm 包
```bash
sudo rpm -e example
# -e 表示卸载，example为包名（不是文件名）

```

### 查询已安装包
```bash
rpm -qa
# -q 查询，-a 所有软件包

```

### 查询某个文件属于哪个包
```bash
rpm -qf /bin/ls
# -q 查询，-f 文件名
```

### 查看包文件包含哪些文件
```bash
rpm -ql bash
# -q 查询，-l 文件列表，bash为包名

```

### 查看依赖关系
```bash
rpm -qR bash
# -q 查询，-R 依赖关系

```

### 查看本地 rpm 包信息
```bash
rpm -qpi example.rpm
# -q 查询，-p 指定包文件，-i 信息

```

### 6.4 练习作业
```bash
1. 使用 rpm 命令安装一个本地 rpm 包（如 wget）：
sudo rpm -ivh wget-*.rpm

2. 查询系统中所有已安装的软件包：
rpm -qa

3. 查询 /usr/bin/vim 属于哪个 rpm 包：
rpm -qf /usr/bin/vim

4. 查看 bash 包包含哪些文件：
rpm -ql bash

5. 升级一个已安装的软件包（可重复安装同一个包观察提示）：
sudo rpm -Uvh wget-*.rpm

6. 卸载 wget 包，并验证是否卸载成功：
sudo rpm -e wget
rpm -q wget

7. 查看某个 rpm 包的依赖关系（以 bash 为例）：
rpm -qR bash
```

## apt 软件安装以及国内源配置

### apt 常用命令参数表（Markdown 源码）
| apt命令             | 取代的命令            | 功能                         |
|---------------------|-----------------------|------------------------------|
| apt install         | apt-get install       | 安装一个软件包               |
| apt remove          | apt-get remove        | 移除一个软件包               |
| apt purge           | apt-get purge         | 移除包及相关配置             |
| apt update          | apt-get update        | 刷新仓库索引                 |
| apt upgrade         | apt-get upgrade       | 升级所有可升级的软件包       |
| apt autoremove      | apt-get autoremove    | 移除多余的软件包             |
| apt full-upgrade    | apt-get dist-upgrade  | 升级软件包,并自动处理依赖    |
| apt search          | apt-cache search      | 搜索某个程序                 |
| apt show            | apt-cache show        | 显示软件包详情               |

### 学习之前，配置国内源（以中科大源为例）-- 先做
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak  # 备份原有源
sudo vim /etc/apt/sources.list                           # 编辑源列表

# 替换为如下内容（以 Ubuntu 22.04 为例）：
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

sudo apt update   # 更新索引以应用新源

```

### 安装软件包（如 vim）
```bash
sudo apt update         # 先更新源列表，确保获取最新的软件包信息
sudo apt install vim    # 安装 vim 编辑器

```

### 移除软件包
```bash
sudo apt remove vim     # 卸载 vim，但保留配置文件

```

### 彻底移除软件包（含配置）
```bash
sudo apt purge vim      # 卸载 vim，并删除其配置文件

```

### 升级系统所有软件包 -- 知道就好了，别操作，卡得你起飞
```bash
sudo apt update         # 更新仓库索引
sudo apt upgrade        # 升级所有可升级的软件包

```

### 自动移除无用依赖
```bash
sudo apt autoremove     # 自动删除系统中不再需要的包
```

### 搜索软件包
```bash
apt search nginx        # 在仓库中搜索 nginx 相关的软件包

```

### 查看软件包详情
```bash
sudo apt purge vim      # 卸载 vim，并删除其配置文件

```

### 练习作业
```bash
1. 使用 apt 安装 curl 软件包：
    sudo apt update                    # 更新软件包索引
    sudo apt install curl              # 安装 curl

2. 搜索仓库中的 git 相关软件包：
    apt search git                     # 搜索包含 git 的软件包

3. 卸载 curl 软件包，并用 apt show 验证其状态：
sudo apt remove curl               # 卸载 curl 软件包
apt show curl                      # 查看 curl 软件包的详细信息，确认是否已卸载

4. 配置一个国内 apt 源，并更新索引（以中科大源为例）：
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak   # 备份原有源


    sudo vim /etc/apt/sources.list                            # 编辑源文件
    # 替换内容为以下几行（以 Ubuntu 22.04 为例）：
    # 阿里云源（Ubuntu 22.04）
    deb https://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
    deb https://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
    deb https://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
    deb https://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse


    sudo apt update                                            # 更新软件包索引

5. 自动清理无用依赖包：
    sudo apt autoremove                  # 自动删除不再需要的包

6. 使用 apt show 查看 vim 软件包的详细信息：
    apt show vim                         # 查看 vim 的详细信息

```
