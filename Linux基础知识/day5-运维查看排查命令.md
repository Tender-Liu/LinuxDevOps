
## 系统查找问题命令指南
| 检查对象   | 常用命令                | 作用说明                                      |
|------------|------------------------|-----------------------------------------------|
| CPU        | top, htop, ps, mpstat  | top/htop 实时监控CPU使用率，ps查进程，mpstat多核负载 |
| 内存       | free, top, vmstat      | free/ top 实时内存，vmstat看内存/交换区动态     |
| 磁盘空间   | df, du                 | df 查看磁盘分区使用情况，du查看目录/文件占用    |
| 磁盘IO     | iostat, dstat, iotop   | iostat/dstat查看IO负载，iotop看进程级IO         |
| 磁盘健康   | smartctl, badblocks    | smartctl查硬盘健康，badblocks查坏道             |
| 分区/挂载  | lsblk, fdisk, blkid    | lsblk显示块设备，fdisk分区，blkid查分区UUID等    |
| 网络配置   | ip addr, ifconfig      | 查看网卡IP、MAC等信息                          |
| 网络连接   | netstat, ss, lsof -i   | netstat/ss查端口/连接，lsof -i查进程端口占用    |
| 网络流量   | iftop, nload, bmon     | 实时监控网卡流量                               |
| 网络抓包   | tcpdump, wireshark     | 抓取网络数据包进行分析                         |
| 路由表     | ip route, route        | 查看和配置路由表                               |
| 进程       | ps, top, htop, pstree  | ps/top/htop查进程，pstree看进程树               |
| 服务状态   | systemctl, service     | systemctl/service管理和查看服务状态            |
| 内核日志   | dmesg, journalctl      | 查看内核及系统日志                             |
| 其他硬件   | lscpu, lspci, lsusb    | lscpu查CPU，lspci查PCI设备，lsusb查USB设备      |



## 常见主机资源排查思路

1. CPU 占用高
- 使用 top 或 htop 实时查看CPU使用率，关注占用高的进程。
- ps aux --sort=-%cpu 按CPU占用排序，定位高消耗进程。
- mpstat -P ALL 1 监控多核CPU负载。

2. 内存不足或泄漏
- free -h 查看总内存和剩余内存。
- top/htop 关注高内存进程。
- ps aux --sort=-%mem 按内存占用排序。
- vmstat 1 持续监控内存、交换区变化。

3. 磁盘空间不足
- df -h 查看各分区空间使用情况。
- du -sh /* 查找哪个目录占用空间大。
- du -sh /var/log/* 检查日志目录是否过大。

4. 磁盘IO瓶颈
- iostat -x 1 监控磁盘IO利用率和等待情况。
- iotop 实时查看进程级别的IO消耗。
- dstat -d 1 综合查看磁盘读写速率。

5. 磁盘健康问题
- smartctl -a /dev/sda 检查硬盘健康状态。
- badblocks -sv /dev/sda 检查硬盘坏道（谨慎操作）。

6. 网络问题
- ip addr 或 ifconfig 查看网卡和IP信息。
- ping 目标IP 检查网络连通性。
- traceroute 目标IP 跟踪网络路径。
- netstat -tnlp 或 ss -tnlp 查看端口监听和网络连接。
- lsof -i:端口号 查找占用端口的进程。
- iftop 或 nload 实时监控网卡流量。
- tcpdump -i eth0 抓包分析网络异常。

7. 服务异常
- systemctl status 服务名 查看服务状态。
- journalctl -u 服务名 查看服务日志。
- ps aux | grep 服务名 检查服务进程是否存在。

8. 日志与系统信息
- dmesg 查看内核日志，排查硬件及驱动故障。
- tail -f /var/log/syslog 或 /var/log/messages 实时查看系统日志。

9. 其他硬件检查
- lscpu 查看CPU详细信息。
- lsblk 查看块设备和挂载情况。
- lspci 查看PCI设备。
- lsusb 查看USB设备。

建议：排查问题时，先从整体资源（CPU、内存、磁盘、网络）入手，逐步缩小范围，结合服务日志和系统日志，定位具体异常点。

## 常用系统排查工具一键安装（Ubuntu）
```bash
# 常用系统排查工具一键安装（Ubuntu）

sudo apt update

# 实时监控与进程
sudo apt install -y htop sysstat

# 内存与虚拟内存监控
sudo apt install -y vmstat procps

# 磁盘空间与IO
sudo apt install -y iotop dstat smartmontools

# 查看分区和设备
sudo apt install -y lsof lsscsi lsblk

# 网络诊断与流量监控
sudo apt install -y net-tools iproute2 iftop nload bmon traceroute tcpdump

# 服务管理与日志
sudo apt install -y systemd

# 其他硬件信息工具
sudo apt install -y lscpu lspci usbutils

# 其他常用工具
sudo apt install -y psmisc

# 推荐一次性安装全部
sudo apt install -y htop sysstat vmstat procps iotop dstat smartmontools lsof lsscsi lsblk net-tools iproute2 iftop nload bmon traceroute tcpdump systemd lscpu lspci usbutils psmisc

```

## 各工具说明及对应包名
| 工具        | 包名              | 说明                                   |
|-------------|-------------------|----------------------------------------|
| top/ps      | procps            | 系统自带，一般已安装                   |
| htop        | htop              | 进程与系统资源实时监控                 |
| vmstat      | procps/sysstat    | 内存、交换区等动态监控                 |
| iostat      | sysstat           | 磁盘IO监控                             |
| iotop       | iotop             | 进程级磁盘IO监控                       |
| dstat       | dstat             | 综合资源监控                           |
| smartctl    | smartmontools     | 硬盘健康检测                           |
| df/du       | coreutils         | 系统自带                               |
| lsblk       | util-linux        | 块设备查看，系统自带                   |
| lsof        | lsof              | 文件/端口占用查询                      |
| netstat     | net-tools         | 网络连接与端口（已被ss替代）           |
| ss/ip       | iproute2          | 新一代网络管理工具                     |
| iftop       | iftop             | 实时网卡流量                           |
| nload       | nload             | 实时网卡流量                           |
| bmon        | bmon              | 实时网卡流量                           |
| traceroute  | traceroute        | 路由追踪                               |
| tcpdump     | tcpdump           | 网络抓包                               |
| systemctl   | systemd           | 服务管理                               |
| lscpu       | util-linux        | CPU信息，系统自带                      |
| lspci       | pciutils          | PCI设备信息                            |
| lsusb       | usbutils          | USB设备信息                            |
| psmisc      | psmisc            | killall/pstree等实用小工具             |
