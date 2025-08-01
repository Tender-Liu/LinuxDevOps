
# 教案：Windows 环境下配置 VSCode SSH 连接与 Shell 脚本开发环境

## 教学目标
1. 学会如何在 Windows 系统中管理统一分发的 SSH 私钥，避免与 Git 私钥冲突。
2. 掌握在 Windows 环境下配置 VSCode 的 SSH Config 文件，确保远程连接顺畅。
3. 安装并使用 Shell 脚本开发相关插件，提升编码效率。

## 适用对象
- 初次在 Windows 系统上使用 VSCode 进行远程开发的用户。
- 使用教师统一分发的 SSH 私钥连接到指定主机的用户。
- 希望在 VSCode 中高效编写 Shell 脚本的用户。

## 前置条件
- 已在 Windows 系统上安装 VSCode。
- 已获得教师统一分发的 SSH 私钥文件。
- 具备基本的文件操作和命令行知识。

---

## 第一部分：管理统一分发的 SSH 私钥（避免与 Git 私钥冲突）

### 背景说明
- SSH 私钥是连接远程服务器的重要凭证，同时 Git 也常使用 SSH 私钥进行代码仓库认证。
- 如果私钥文件命名或路径冲突，可能导致 VSCode 或 Git 无法正确识别对应的私钥，引发连接失败或认证错误。
- 本课程中，SSH 私钥由教师统一分发，适用于所有指定主机，同学无需自行生成私钥。
- 解决冲突方法：为分发的私钥设置特定的文件名和路径，避免与 Git 等其他用途的私钥冲突。

### 操作步骤

1. **接收并保存统一分发的私钥文件**
   - 教师会通过安全渠道（如加密邮件、U盘或其他方式）分发 SSH 私钥文件。
   - 将接收到的私钥文件保存到用户的 `.ssh` 目录下，建议使用特定的文件名以避免冲突，例如 `server_key`。
   - 保存路径：
     - Windows：`C:\Users\YourUsername\.ssh\server_key`
   - **具体操作**：
     - 打开文件资源管理器，导航到 `C:\Users\YourUsername\` 目录下（`YourUsername` 是你的 Windows 用户名）。
     - 如果没有看到 `.ssh` 文件夹，可以手动创建一个：右键点击空白处，选择“新建” -> “文件夹”，命名为 `.ssh`。
     - 将教师分发的私钥文件（例如 `server_key`）复制到 `C:\Users\YourUsername\.ssh\` 目录下。
   - **注意**：如果文件名与现有私钥（如 Git 使用的 `id_rsa`）冲突，请重命名分发的私钥文件。可以在文件资源管理器中右键文件，选择“重命名”，改为 `server_key`。

2. **私钥安全使用注意事项**
   - **保密性**：SSH 私钥是敏感文件，切勿将其上传到公共代码仓库、分享给他人或存储在不安全的位置。
   - **备份**：建议将私钥文件备份到安全的地方（如个人U盘或加密存储），以防设备丢失或文件损坏。
   - **丢失处理**：如果私钥文件丢失或泄露，请立即通知教师，以便采取相应措施（如更换私钥）。

---

## 第二部分：配置 VSCode SSH Config 文件

### 背景说明
- VSCode 的 Remote-SSH 插件使用 OpenSSH 客户端连接远程服务器。
- 通过配置 `.ssh\config` 文件，可以简化连接参数，避免每次手动指定私钥、端口等信息。
- 在 Windows 环境下，VSCode 会自动识别位于 `C:\Users\YourUsername\.ssh\` 目录下的配置文件。

### 操作步骤

1. **创建或编辑 SSH Config 文件**
   - 打开文件资源管理器，导航到 `C:\Users\YourUsername\.ssh\` 目录。
   - 检查是否存在 `config` 文件（无扩展名）。
   - 如果文件不存在，可以手动创建：
     - 右键点击空白处，选择“新建” -> “文本文档”。
     - 将文件名改为 `config`（确保没有 `.txt` 扩展名）。
   - 使用文本编辑器（如记事本或 VSCode）打开 `config` 文件。
   - **注意**：如果使用记事本保存文件，请确保文件编码为 UTF-8，以避免格式问题。

2. **添加主机配置**
   - 在 `config` 文件中添加以下内容，指定统一分发的私钥和连接参数：
     ````bash
     Host ServerAlias
       HostName server_ip
       User username
       Port port
       IdentityFile C:\Users\YourUsername\.ssh\server_key
     ````
   - **参数说明**：
     - `Host ServerAlias`：自定义别名，方便记忆（如 `MyServer`）。
     - `HostName server_ip`：目标服务器的 IP 地址，由教师提供。
     - `User username`：登录用户名，由教师提供。
     - `Port port`：SSH 端口号，由教师提供（默认 22，若自定义则需指定）。
     - `IdentityFile C:\Users\YourUsername\.ssh\server_key`：指定统一分发的私钥文件路径，确保路径正确。
   - **示例**（具体参数以教师提供为准）：
     ````bash
     Host MyServer
       HostName 192.168.110.8
       User ubuntu
       Port 5423
       IdentityFile C:\Users\Administrator\.ssh\server_key
     ````
   - 保存文件，确保路径为 `C:\Users\YourUsername\.ssh\config`。

3. **在 VSCode 中测试连接**
   - 打开 VSCode，按 `Ctrl+Shift+P` 打开命令面板。
   - 输入 `Remote-SSH: Connect to Host` 并回车。
   - 在弹出的列表中选择你配置的别名（如 `MyServer`）。
   - 如果连接成功，VSCode 将在新窗口中打开远程服务器的工作区，显示“已连接”状态。
   - 如果连接失败，请检查 `config` 文件内容是否正确，或查看 VSCode 右下角的 Remote-SSH 状态信息。

---

## 第三部分：安装和使用 Shell 脚本开发插件

### 背景说明
- VSCode 提供了强大的插件生态系统，可以通过安装特定插件提升 Shell 脚本的开发效率。
- 本教案推荐安装以下插件：`Shell Syntax`（语法高亮）、`ShellCheck`（错误检查）、`Bash IDE`（代码补全）。
- 这些插件适用于在远程服务器上编写和调试 Shell 脚本，且在 Windows 环境下可以直接安装和使用。

### 操作步骤

1. **安装插件**
   - 打开 VSCode，点击左侧活动栏中的“扩展”图标（形状像一个方块拼图），或按快捷键 `Ctrl+Shift+X`。
   - 在搜索框中分别输入以下插件名称，找到对应插件并点击“安装”按钮：
     - `Shell Syntax`：提供 Shell 脚本语法高亮，增强代码可读性。开发者：Jeff Hykin。
     - `ShellCheck`：静态分析工具，检测 Shell 脚本中的语法错误和潜在问题。开发者：Timon Wong。
     - `Bash IDE`：提供代码补全、符号导航等功能，适用于远程服务器或本地 Bash 环境。开发者：mads-hartmann。
   - 安装完成后，插件会自动启用，部分插件可能需要额外配置。

2. **额外配置**
   - **ShellCheck**：需要系统或远程服务器上安装 ShellCheck 工具。VSCode 插件会提示安装方法，通常可以通过 VSCode 的终端窗口运行安装命令。如果在远程服务器上操作，请确保服务器环境支持。
   - **Bash IDE**：在 Windows 环境下可以直接安装和使用。如果是在远程服务器上编写代码，`Bash IDE` 会自动适配服务器的 Bash 环境，无需额外配置。如果在本地 Windows 环境编写 Bash 脚本，建议安装 Git Bash 或 WSL（Windows Subsystem for Linux）以提供 Bash 环境支持。
   - **文件类型识别**：确保 `.sh` 文件被正确识别为 Shell 脚本语言。如果文件未高亮，可以在 VSCode 右下角状态栏手动设置语言为 `Shell Script`。

3. **使用说明**
   - **Shell Syntax**：自动为 `.sh` 文件提供语法高亮，关键字、变量等会以不同颜色显示，提升代码可读性。
   - **ShellCheck**：编写代码时，错误或警告会以波浪线标注，鼠标悬停可查看详细信息，帮助快速修复问题。
   - **Bash IDE**：支持变量、函数和命令的自动补全，按 `Ctrl+Space` 可触发提示，减少手动输入错误。

4. **其他可选插件**
   - `Shell-Format`：用于格式化 Shell 脚本，需在远程服务器或本地安装 `shfmt` 工具。安装后可自动整理代码格式。
   - `Code Runner`：快速运行 Shell 脚本片段，方便测试小段代码。点击代码右上角的“运行”按钮即可执行。

---

## 总结与注意事项

1. **私钥管理**：
   - 使用教师统一分发的 SSH 私钥，确保文件名和路径与 Git 等其他用途的私钥不冲突。
   - 将私钥文件保存到 `C:\Users\YourUsername\.ssh\` 目录下，权限调整为可选步骤，仅在遇到问题时执行。
   - 严格遵守私钥保密原则，防止泄露，做好备份并妥善保管。
2. **SSH Config 配置**：
   - 在 `C:\Users\YourUsername\.ssh\config` 文件中配置远程主机信息，简化 VSCode 连接设置。
   - 确保 `IdentityFile` 路径正确指向统一分发的私钥文件。
   - 测试连接时，确保 VSCode 已安装并启用 Remote-SSH 插件。
3. **Shell 脚本开发**：
   - 安装 `Shell Syntax`、`ShellCheck` 和 `Bash IDE` 插件，提升语法高亮、错误检查和代码补全体验。
   - `Bash IDE` 在 Windows 环境下可以直接安装和使用，远程服务器环境会自动适配。
   - 根据需求安装其他辅助插件，如 `Shell-Format` 和 `Code Runner`，以进一步优化开发流程。

## 常见问题解决

1. **私钥冲突问题**：
   - 如果 VSCode 或 Git 仍然无法识别正确的私钥，可尝试使用 `ssh-add` 添加私钥到 SSH Agent。
   - 打开命令提示符，运行以下命令：
     ````bash
     ssh-add C:\Users\YourUsername\.ssh\server_key
     ````
   - 如果提示找不到 `ssh-add` 命令，可能是 OpenSSH 未正确安装。请确保已安装 OpenSSH 客户端（Windows 10/11 可通过“设置” -> “应用” -> “可选功能”添加）。

2. **插件不生效问题**：
   - 检查文件扩展名是否为 `.sh`，或在 VSCode 右下角状态栏手动设置语言为 `Shell Script`。
   - 如果插件需要额外工具（如 ShellCheck 或 bash-language-server），请确保这些工具已在远程服务器或本地安装。

3. **连接失败问题**：
   - 查看 VSCode 的 Remote-SSH 日志以获取详细信息：
     - 按 `Ctrl+Shift+P` 打开命令面板，选择 `Remote-SSH: Show Log`。
     - 检查日志中的错误信息，常见问题包括私钥路径错误、服务器参数不正确等。
   - 确保 `config` 文件内容无误，路径使用反斜杠 `\` 而非正斜杠 `/`。
   - 如果仍然无法解决，请记录错误信息并向教师反馈。
