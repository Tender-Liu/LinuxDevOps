# 认识Linux操作系统

## 课程目标

1. 掌握Linux系统基础知识
   * 理解Linux操作系统的发展历史和特点
   * 掌握Linux系统的应用场景和优势
   * 了解不同Linux发行版的特点

2. 熟悉Linux系统结构
   * 掌握Linux文件系统层次结构
   * 理解各个目录的作用和管理方法
   * 熟悉Linux系统启动流程

3. 掌握虚拟机操作技能
   * 能够独立完成虚拟机的安装和配置
   * 掌握虚拟机快照管理和备份恢复
   * 学会虚拟机网络配置方法

## 课程大纲
1. Linux介绍
2. 案例：装机预备技能
3. Linux目录结构
4. 获取Linux命令行
5. 案例：Linux命令行基本操作
6. 案例：拍摄快照
7. 课后基础练习


## 1. Linux介绍

### 1.1 什么是Linux？

* Linux是一种操作系统，负责管理计算机硬件资源和为用户提供交互界面。
* 操作系统的作用：
    * 管理硬件资源（如CPU、内存、硬盘等）。
    * 提供用户与计算机交互的接口。
    * 提供应用程序运行的环境。
* Linux的核心：内核（Kernel）。
    * 内核是操作系统的核心部分，直接与硬件交互，负责资源分配和管理。
    * 用户通过命令行或图形界面与内核交互。

### 1.2 Linux的起源

* UNIX的诞生：
    * 1970年，AT&T贝尔实验室的Ken Thompson和Dennis Ritchie开发了UNIX操作系统。
    * UNIX的设计理念：小而简单，每个工具只做一件事，并且做好。
* Linux的诞生：
    * 1991年，芬兰的Linus Torvalds基于MINIX系统开发了Linux内核。
    * 他将Linux的代码免费开源，并鼓励全球开发者共同参与改进。
* Linux的发展：
    * Linux不仅是一个内核，还逐渐发展为一个完整的操作系统生态。
    * 大量的开源软件围绕Linux内核构建，形成了各种发行版。

### 1.3 为什么选择Linux？
> 文档来源: https://docs.geeksman.com/tools/ubuntu/01.ubuntu-linux-intro.html#linux-%E7%9A%84%E5%8F%91%E8%A1%8C%E7%89%88%E6%9C%AC

* 开源：Linux遵循GPL（GNU通用公共许可证），代码完全开放，用户可以自由修改和分发。
* 稳定性：Linux以其高稳定性和可靠性著称，广泛用于服务器和嵌入式设备。
* 安全性：Linux的权限管理机制强大，系统默认比Windows更安全。
* 多样性：Linux有众多发行版，适合不同需求（如服务器、桌面、开发、嵌入式等）。
* 社区支持：Linux有庞大的开源社区，用户可以免费获得帮助和资源。

### 1.4 常见的Linux发行版
Linux的发行版是基于Linux内核构建的操作系统，通常包含内核、系统工具、应用程序和包管理器。以下是几种常见的发行版：

| 发行版          | 特点                                                                 |
|-----------------|----------------------------------------------------------------------|
| Red Hat (RHEL)  | 商业版 Linux，提供企业级支持，适合服务器和企业环境。                |
| CentOS          | RHEL 的社区版，免费使用，与 RHEL 高度兼容。                        |
| Rocky Linux     | CentOS 的继任者，由原 CentOS 团队创建，与 RHEL 完全兼容。          |
| Ubuntu          | 基于 Debian，用户友好，适合桌面和开发环境。                        |
| Debian          | 稳定、安全，适合服务器和开发，许多发行版（如 Ubuntu）基于 Debian 开发。 |
| SUSE            | 企业级发行版，广泛用于服务器和高性能计算领域。                      |
| Arch Linux      | 滚动更新模式，适合高级用户，提供最新的软件包。                      |

### 1.5 Linux的哲学理念
1. 一切皆文件：
    * 在Linux中，所有内容（包括硬件设备）都被视为文件。
    * 例如：
        * /dev/sda：代表硬盘。
        * /dev/null：一个特殊设备文件，丢弃所有写入的数据。
2. 小即是美：
    * 每个工具只做一件事，并且做好。
    * 例如：ls用于列出目录内容，cat用于查看文件内容。
3. 将复杂问题分解成简单问题：
    * 通过管道（|）将多个小工具组合起来完成复杂任务。

## 2. 案例：装机预备技能

### 2.1 问题
1. RHEL、CentOS和Rocky Linux系统有什么关联？
    * RHEL是红帽公司提供的商业版Linux系统，适用于企业环境。
    * CentOS是RHEL的社区版，免费使用，但已被红帽收购。
    * Rocky Linux是CentOS的继任者，由社区维护，与RHEL完全兼容。

2. Linux系统中第三块SCSI硬盘如何表示？

* 在Linux中，硬盘设备以/dev/sdX表示：
    * 第一块硬盘：/dev/sda
    * 第二块硬盘：/dev/sdb
    * 第三块硬盘：/dev/sdc

3. ubuntu系统镜像
    * https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/22.04.5/
    * https://mirrors.aliyun.com/ubuntu-releases/22.04/

4. VMware 安装教程
    * https://www.cnblogs.com/EthanS/p/18211302
    * https://docs.geeksman.com/tools/ubuntu/02.ubuntu-install.html

5. VMware 激活码
    * https://github.com/hegdepavankumar/VMware-Workstation-Pro-17-Licence-Keys

5. 在VMware中安装Ubuntu系统
    * 英文版系统安装教程 -  https://blog.csdn.net/m0_51913750/article/details/131604868
    * 中文版系统安装教程 - https://docs.geeksman.com/tools/ubuntu/02.ubuntu-install.html#_2-%E9%85%8D%E7%BD%AE-ubuntu-%E8%99%9A%E6%8B%9F%E6%9C%BA

### 3. Linux目录结构

#### 3.1 目录结构概述
> 来源文档: https://docs.geeksman.com/tools/ubuntu/03.ubuntu-directory-structure.html

Linux采用树形结构，所有文件和目录都从根目录（/）开始。

```plaintext
/
├── bin    # 存放二进制可执行文件
├── boot   # 存放启动相关文件
├── dev    # 存放设备文件
├── etc    # 存放系统配置文件
├── home   # 普通用户的主目录
├── root   # 超级用户的主目录
├── usr    # 存放用户程序
├── var    # 存放动态数据

```

#### 3.2 重要目录详解
1. /bin：存放系统的基本命令，如ls、cp、mv。
2. /boot：存放启动引导程序和内核文件。
3. /dev：存放设备文件，如硬盘（/dev/sda）、光驱（/dev/cdrom）。
4. /etc：存放系统的配置文件，如网络配置文件。
5. /home：普通用户的主目录。
6. /root：超级用户（root）的主目录。
7. /usr：存放用户安装的程序和工具。
8. /var：存放动态数据，如日志文件和缓存。


### 4. 获取Linux命令行

#### 4.1 什么是命令行？
* 命令行是用户与Linux系统交互的主要方式，通过键入命令来完成任务。
* 优点：
    * 高效、灵活。
    * 适合自动化任务和批量操作。

#### 4.2 打开命令行
* 在桌面左上角点击“活动”，搜索“终端”并打开。
* 在虚拟机中，通常可以通过快捷键Ctrl + Alt + T打开终端。

#### 4.3 命令行提示符
* 格式：[当前用户@主机名 当前所在目录]
* 以#结尾：表示当前用户是root用户。
* 以$结尾：表示当前用户是普通用户。


## 5. 案例：Linux命令行基本操作
* Linux手册大全：https://www.linuxcool.com/
* 菜鸟Linux命令手册大全：https://www.runoob.com/linux/linux-command-manual.html

### 5.1 问题
本案例要求熟悉新装 Linux 系统中命令行界面的获取方法，并通过命令行完成以下任务：

* pwd、cd、ls 命令练习
* 路径练习与切换
* cat 和 less 命令练习
* hostname 修改与查看
* 显示 CPU 与内存信息
* 查看 IP 地址
* 创建文件与目录
* 查看文件部分内容
* 过滤文件内容
* vim 文本编辑器使用
* 关机与重启

## 步骤一：简单命令行操作练习

### 1）pwd、cd、ls 命令练习

#### 命令解释
* pwd：打印当前工作目录的绝对路径。
* cd：切换目录。
    * cd /：切换到根目录。
    * cd ~：切换到当前用户的主目录。
    * cd ..：切换到上一级目录。
* ls：列出当前目录的内容。
    * ls /：列出根目录的内容。
    * ls -l：以详细列表形式显示目录内容。
    * ls -a：显示隐藏文件（以.开头的文件）。

#### 操作内容
```bash
[root@localhost ~]# pwd           # 显示当前所在位置
/root                            # 当前目录为 root 用户的主目录

[root@localhost ~]# cd /         # 切换到根目录
[root@localhost /]# pwd          # 再次查看当前目录
/                                # 当前目录为根目录

[root@localhost /]# ls           # 列出根目录下的内容
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

[root@localhost /]# cd /home     # 切换到 /home 目录
[root@localhost home]# ls        # 查看 /home 目录内容
                                # 可能为空，表示没有用户数据
[root@localhost home]# cd /root  # 切换回 root 用户的主目录
[root@localhost ~]# ls           # 列出 root 用户主目录下的内容

```

#### 操作结果
* pwd 命令显示当前目录的绝对路径。
* cd 命令切换目录。
* ls 命令列出当前目录或指定目录的内容。


### 2）ls 命令练习
#### 命令解释
* ls：列出目录内容。
* ls /path：列出指定路径的内容。
* ls -l：以详细列表形式显示内容，包括权限、所有者、大小、修改时间等。
* ls -a：显示所有文件，包括隐藏文件。


#### 操作内容
```bash
[root@localhost ~]# cd /etc      # 切换到 /etc 目录
[root@localhost etc]# pwd        # 查看当前目录
/etc                             # 当前目录为 /etc

[root@localhost etc]# ls /root   # 查看 /root 目录的内容
[root@localhost etc]# ls /       # 查看根目录的内容
[root@localhost etc]# ls /home   # 查看 /home 目录的内容
[root@localhost etc]# ls /boot   # 查看 /boot 目录的内容
[root@localhost etc]# ls /var    # 查看 /var 目录的内容
[root@localhost etc]# ls /usr    # 查看 /usr 目录的内容

```

#### 操作结果
* 列出了指定目录的内容。
* 可以看到不同目录下的文件和子目录。


### 3）路径练习

#### 命令解释
* 绝对路径：以根目录 / 开头的路径。例如：/usr/bin。
* 相对路径：相对于当前目录的路径。例如：cd .. 返回上一级目录。

#### 操作内容
```bash
[root@localhost ~]# cd /usr       # 使用绝对路径切换到 /usr
[root@localhost usr]# ls          # 查看 /usr 的内容
bin  config  games  include  lib  lib64  local  sbin  share  src  tmp

[root@localhost usr]# cd games    # 使用相对路径切换到 games 子目录
[root@localhost games]# pwd       # 查看当前路径
/usr/games

[root@localhost games]# cd /      # 切换到根目录
[root@localhost /]# cd /usr/games # 使用绝对路径切换到 /usr/games
[root@localhost games]# pwd       # 查看当前路径
/usr/games

```


#### 操作结果
* 掌握了绝对路径和相对路径的使用方法。
* 通过 pwd 验证路径切换是否正确。

### 4）路径切换练习


#### 命令解释
* cd ..：返回上一级目录。
* cd -：返回到上一次所在的目录。

#### 操作内容
```bash
[root@localhost /]# cd /etc/pki/rpm-gpg/  # 切换到指定目录
[root@localhost rpm-gpg]# pwd             # 查看当前路径
/etc/pki/rpm-gpg

[root@localhost rpm-gpg]# cd ..           # 返回到上一级目录
[root@localhost pki]# pwd
/etc/pki

[root@localhost pki]# cd ..               # 再次返回上一级目录
[root@localhost etc]# pwd
/etc

[root@localhost etc]# cd ..               # 返回到根目录
[root@localhost /]# pwd
/

```

#### 操作结果
* 成功完成了多级目录的切换。
* 熟悉了 cd .. 的用法。

### 5）cat 命令练习

#### 命令解释
* cat 文件名：查看文本文件内容。适用于小型文件。
* cat -n 文件名：显示行号。

#### 操作内容
```bash
[root@localhost /]# cat /etc/passwd       # 查看 /etc/passwd 文件内容
[root@localhost /]# cat /etc/fstab        # 查看 /etc/fstab 文件内容
[root@localhost /]# cat /etc/redhat-release # 查看系统版本信息

```

#### 操作结果
* 成功查看了指定文件的内容。
* 了解了文件中存储的信息。

### 6）less 命令练习

#### 命令解释
* less 文件名：分页查看文件内容，适合查看大文件。
* 按键操作：
    * 上下键：滚动内容。
    * q：退出查看。

#### 操作内容
```bash
[root@localhost /]# less /etc/passwd      # 分页查看 /etc/passwd 文件内容

```

#### 操作结果
* 成功分页查看文件内容。
* 学会了 less 命令的基本操作。

### 7）hostname 命令练习

#### 命令解释
* hostname：查看主机名。
* hostname 新主机名：临时修改主机名。

#### 操作内容
```bash
[root@localhost /]# hostname             # 查看当前主机名
localhost.localdomain

[root@localhost /]# hostname svr01       # 修改主机名为 svr01
[root@localhost /]# hostname             # 再次查看主机名
svr01

```

#### 操作结果
* 成功查看并修改了主机名。


### 8）显示 CPU 与内存

#### 命令解释
* lscpu：显示 CPU 信息。
* cat /proc/meminfo：显示内存信息。

#### 操作内容
```bash
[root@localhost /]# lscpu                # 查看 CPU 信息
[root@localhost /]# cat /proc/meminfo    # 查看内存信息

```

#### 操作结果
* 成功查看到 CPU 核心数、型号、频率等信息。
* 成功查看到系统内存的详细信息。


### 9）查看 IP 地址

#### 命令解释
* ifconfig：查看网络接口的 IP 地址信息。

#### 操作内容
```bash
# 由于ubuntu安装的系统时，默认没有安装ifconfig命令
# 请使用以下命令安装
sudo apt install net-tools
```

```bash
[root@localhost /]# ifconfig             # 查看网卡 IP 地址信息


```

#### 操作结果
* 成功显示了网络接口的 IP 地址。


### 10）创建数据

#### 命令解释

* mkdir 目录名：创建目录。
* touch 文件名：创建空文件。

#### 操作内容
```bash
[root@localhost /]# mkdir /opt/test      # 创建目录
[root@localhost /]# touch /opt/1.txt     # 创建文件
[root@localhost /]# ls /opt              # 查看创建的内容

```

#### 操作结果
* 成功创建了目录和文件。


### 11）vim 文本编辑器

#### 命令解释

* vim 文件名：编辑文件。
* 模式：
    * 命令模式：默认进入模式。
    * 插入模式：按 i 键进入，输入内容。
    * 末行模式：按 : 进入，用于保存或退出。

#### 操作内容
```bash
# vim 编辑文本命令默认没有安装，使用命令安装一下
# 记得输入密码哦
sudo apt install -y vim
```

```bash
[root@localhost /]# vim /opt/test.txt    # 编辑文件
# 按 i 键进入插入模式，输入内容：
I Love Linux
# 按 Esc 键返回命令模式，输入 :wq 保存并退出

```

```bash
# 查看刚才编辑的文件
cat /opt/test.txt
```

#### 操作结果
* 成功编辑并保存了文件。