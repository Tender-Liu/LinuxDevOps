# XShell安装与Ubuntu远程连接教程

本教程将指导您完成XShell的安装以及如何使用XShell连接Ubuntu服务器。


## 1. XShell安装步骤

### 1.1 下载XShell
1. 访问XShell官网 (https://www.xshell.com/zh/xshell-download/)
2. 选择"Free for Home/School"（家庭/学校免费版）
    <img src="/Linux基础知识/images/dayy3/xshell下载地址.png" alt="xshell下载地址" height="200">
3. 填写相关信息并下载安装包
    <img src="/Linux基础知识/images/dayy3/下载界面.png" alt="下载界面" height="200">

### 1.2 安装步骤
1. 双击下载的安装包启动安装程序
2. 点击"Next"（下一步）
3. 选择"I accept the agreement"（接受协议）
4. 选择安装路径（建议使用默认路径）
5. 点击"Install"（安装）开始安装
6. 等待安装完成，点击"Finish"（完成）

### 1.3 基本配置
- 首次启动时，可能需要选择配色方案
- 建议在"工具 > 选项"中将界面语言改为中文（如需要）
- 可以在选项中设置字体大小和类型



## 2. Ubuntu系统准备

### 2.1 查看IP地址
在Ubuntu终端中，可以使用以下命令查看IP地址：
```bash
# 方法1：使用ip命令（推荐）
ip addr

# 方法2：如果系统没有ip命令，可以安装net-tools后使用ifconfig
sudo apt install net-tools
ifconfig
```

### 2.2 关闭UFW防火墙
在Ubuntu中关闭UFW防火墙的命令如下：
```bash
# 查看UFW状态
sudo ufw status

# 关闭UFW防火墙
sudo ufw disable

# 如果之后需要重新启用
# sudo ufw enable
```


## 3. 使用XShell连接Ubuntu

### 3.1 创建新会话
1. 打开XShell
2. 点击"文件 > 新建"或使用快捷键`Ctrl + N`
3. 在弹出的新建会话窗口中进行配置

### 3.2 配置连接参数
1. 名称：输入便于识别的会话名称（如：Ubuntu_Server）
2. 协议：选择SSH
3. 主机：输入Ubuntu服务器的IP地址
4. 端口号：默认为22
5. 用户密码: 自己配置

<img src="/Linux基础知识/images/dayy3/配置远程连接一.png" alt="配置远程连接一" height="200">

<img src="/Linux基础知识/images/dayy3/远程配置2.png" alt="远程配置2" height="200">


### 3.3 连接测试
1. 双击创建的会话名称
2. 点击"确定"进行连接

### 3.4 连接成功标志
- 如果看到Ubuntu的命令提示符，说明连接成功
- 可以开始执行Linux命令
- 窗口标题会显示当前连接的主机信息

### 3.5 常见问题解决
- 如果连接失败，请检查：
  1. Ubuntu的IP地址是否正确
  2. UFW防火墙是否已关闭
  3. SSH服务是否正常运行
  4. 用户名和密码是否正确
  5. 网络连接是否正常


