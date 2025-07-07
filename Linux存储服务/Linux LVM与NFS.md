#Linux 存储基础与初步共享

## 目标：

1. 理解 Linux 磁盘阵列（RAID）的基本理论。
2. 掌握磁盘管理工具 fdisk 和 parted 的基本用法。
3. 了解 Linux 中的磁盘类型。
4. 学习 LVM（逻辑卷管理）的基本概念和操作，重点是动态卷组。
5. LVM（逻辑卷管理） 高级管理
6. 初步掌握 NFS（网络文件系统），学习如何将磁盘共享出去。
7. 实验操作 LVM + NFS 

环境准备：建议使用虚拟机（如 VirtualBox）安装一个 Linux 系统（如 Ubuntu 或 CentOS），确保有至少 2 个虚拟磁盘用于实践。

第一部分：Linux 磁盘阵列（RAID）理论（30-45 分钟）
什么是 RAID？
RAID（Redundant Array of Independent Disks，独立磁盘冗余阵列）是一种将多个物理磁盘组合起来以提高性能或可靠性的技术。RAID 主要用于数据存储的冗余备份和性能优化。

常见的 RAID 级别
RAID 0（条带化）：将数据分散在多个磁盘上以提高读写速度，但无冗余，磁盘故障会导致数据丢失。
RAID 1（镜像）：数据在多个磁盘上镜像存储，提供冗余，一个磁盘故障不影响数据，但存储容量减半。
RAID 5：结合条带化和奇偶校验，至少需要 3 个磁盘，提供性能和冗余，允许一个磁盘故障。
RAID 10（1+0）：结合 RAID 0 和 RAID 1，至少需要 4 个磁盘，提供高性能和高冗余。
RAID 的实现方式
硬件 RAID：通过专用的 RAID 控制器实现，性能更好但成本较高。
软件 RAID：通过操作系统（如 Linux 的 mdadm 工具）实现，成本低但性能稍逊。
实践思考
RAID 不是备份，而是一种提高性能或可靠性的方式，数据仍需定期备份。
在虚拟机中，可以通过 mdadm 模拟软件 RAID，但今天我们先关注理论，实践可以在后续学习中完成。
学习资源：阅读 man mdadm 或搜索 “Linux RAID tutorial” 了解更多。

第二部分：磁盘管理工具（fdisk 和 parted）（45-60 分钟）
磁盘管理基础
在 Linux 中，磁盘管理是存储技术的起点，常用工具包括 fdisk 和 parted，用于创建、删除和修改磁盘分区。

fdisk：传统分区工具
用途：管理 MBR（Master Boot Record）分区表，适用于小于 2TB 的磁盘。
基本操作：
查看磁盘：lsblk 或 fdisk -l。
进入分区模式：fdisk /dev/sdX（替换 sdX 为你的磁盘，如 /dev/sdb）。
常用命令：
n：创建新分区。
p：查看当前分区表。
w：保存并退出。
实践：在虚拟机中添加一个新磁盘（如 10GB），用 fdisk 创建一个主分区。
parted：更现代的分区工具
用途：支持 GPT（GUID Partition Table），适用于大于 2TB 的磁盘，也支持 MBR。
基本操作：
进入 parted：parted /dev/sdX。
常用命令：
mklabel gpt：创建 GPT 分区表。
mkpart primary 0% 100%：创建一个占满磁盘的主分区。
print：显示分区信息。
quit：退出。
实践：用 parted 在另一块虚拟磁盘上创建一个 GPT 分区。
格式化分区
创建分区后，需要格式化为文件系统（如 ext4）：

命令：mkfs.ext4 /dev/sdX1（替换为你的分区）。
查看：df -h 或 lsblk -f。
注意：操作磁盘时务必确认目标设备，避免误操作导致数据丢失。

第三部分：Linux 磁盘类型（30 分钟）
Linux 中的磁盘类型
机械硬盘（HDD）：传统磁盘，基于磁性存储，速度较慢，容量大，价格低。
固态硬盘（SSD）：基于闪存存储，速度快，耐用性稍差，价格较高。
NVMe SSD：使用 PCIe 接口的 SSD，速度极快，常用于高性能场景。
虚拟磁盘：在虚拟机中模拟的磁盘，用于测试和学习。
网络磁盘：如 iSCSI 或 NFS 共享的远程存储。
Linux 中的磁盘命名
SATA/SCSI 磁盘：/dev/sda, /dev/sdb 等，sda1 表示第一个分区。
NVMe 磁盘：/dev/nvme0n1 等，nvme0n1p1 表示第一个分区。
查看磁盘类型：使用 lsblk -d -o NAME,ROTA（ROTA=1 表示机械硬盘，0 表示 SSD）或 dmesg | grep disk。
实践
在虚拟机中查看当前磁盘类型：lsblk 和 cat /proc/scsi/scsi。
思考：不同磁盘类型对存储性能的影响（如 HDD vs SSD 在 RAID 中的表现）。
第四部分：LVM 动态卷组（逻辑卷管理）（60-90 分钟）
什么是 LVM？
LVM（Logical Volume Manager）是 Linux 提供的一种灵活的磁盘管理方式，允许动态调整存储空间。

LVM 的核心组件
物理卷（PV）：将物理磁盘或分区初始化为 LVM 可用的单元。
卷组（VG）：将多个 PV 组合成一个大的存储池。
逻辑卷（LV）：从卷组中分配空间，创建可调整大小的分区。
LVM 的优势
动态调整分区大小（扩展或缩小）。
支持快照（Snapshot），便于备份。
跨磁盘管理存储空间。
实践操作：创建和管理 LVM
准备磁盘：确保有至少一个未使用的分区或磁盘（如 /dev/sdb1）。
创建物理卷（PV）：
命令：pvcreate /dev/sdb1
查看：pvdisplay
创建卷组（VG）：
命令：vgcreate my_vg /dev/sdb1（my_vg 是卷组名称）
查看：vgdisplay
创建逻辑卷（LV）：
命令：lvcreate -L 5G -n my_lv my_vg（分配 5GB，逻辑卷名为 my_lv）
查看：lvdisplay
格式化和挂载：
格式化：mkfs.ext4 /dev/my_vg/my_lv
挂载：mkdir /mnt/mylv && mount /dev/my_vg/my_lv /mnt/mylv
查看：df -h
动态扩展逻辑卷（假设卷组还有剩余空间）：
扩展：lvextend -L +2G /dev/my_vg/my_lv
更新文件系统：resize2fs /dev/my_vg/my_lv
查看：df -h
注意事项
LVM 操作需要备份数据，避免误操作导致数据丢失。
缩小逻辑卷时需先缩小文件系统（resize2fs），再缩小逻辑卷（lvreduce），顺序不能错。
学习资源：man lvm 或搜索 “Linux LVM tutorial”。

第五部分：NFS（网络文件系统）基础与磁盘共享（60-90 分钟）
什么是 NFS？
NFS（Network File System）是一种分布式文件系统协议，允许通过网络共享文件目录，类似于 NAS 的功能。

NFS 的基本原理
服务器端：配置共享目录，允许客户端访问。
客户端：通过网络挂载服务器的共享目录，像本地文件系统一样使用。
实践操作：配置 NFS 共享
环境：建议准备两台虚拟机（或本机模拟），一台作为服务器，一台作为客户端。

服务器端配置（共享磁盘）：
安装 NFS：sudo apt install nfs-kernel-server（Ubuntu）或 sudo yum install nfs-utils（CentOS）。
创建共享目录：mkdir /shared && chmod 755 /shared。
编辑配置文件：sudo vim /etc/exports，添加以下内容：
复制
/shared 192.168.1.0/24(rw,sync,no_root_squash)
（192.168.1.0/24 是允许访问的网段，调整为你的网络）。
重启 NFS 服务：sudo systemctl restart nfs-kernel-server。
检查共享：showmount -e localhost。
客户端挂载：
安装 NFS 客户端：sudo apt install nfs-common 或 sudo yum install nfs-utils。
创建挂载点：mkdir /mnt/shared。
挂载共享目录：sudo mount -t nfs 192.168.1.100:/shared /mnt/shared（替换 IP 为服务器 IP）。
查看：df -h。
测试：往 /mnt/shared 写入文件，检查服务器 /shared 是否同步。
设置开机自动挂载：
编辑客户端的 /etc/fstab，添加：
复制
192.168.1.100:/shared /mnt/shared nfs defaults 0 0
注意事项
确保服务器和客户端网络连通，防火墙允许 NFS 端口（2049）。
NFS 默认安全性较低，生产环境需配置权限和认证。
学习资源：man exports 或搜索 “Linux NFS setup tutorial”。

第一天总结与作业（30 分钟）
总结
学习了 RAID 理论，了解磁盘阵列的作用和级别。
掌握了 fdisk 和 parted 的基本分区操作。
了解了 Linux 磁盘类型及其命名规则。
通过 LVM 实践，学会了创建动态卷组和逻辑卷。
配置了 NFS，实现了磁盘目录的网络共享。
作业
理论：复习 RAID 级别，写下 RAID 0、1、5、10 的优缺点。
实践：
在虚拟机中用 fdisk 创建一个新分区，并格式化为 ext4。
用 LVM 创建一个新的逻辑卷，并尝试扩展其大小。
如果可能，配置 NFS，在两台机器间共享一个目录。
学习建议
动手实践：存储技术需要反复操作才能熟练，建议在虚拟机中多尝试。
记录笔记：将今天学习的命令和步骤记录下来，形成自己的知识库。
遇到问题：如果命令报错或配置失败，查阅 man 手册或搜索相关错误信息。