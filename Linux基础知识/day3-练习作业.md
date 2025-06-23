# Ubuntu 系统命令作业

以下是为你在 Ubuntu 系统下设计的三个作业，难度分别为简单、一般和复杂。作业只涉及 `cd`, `ls`, `mkdir`, `rm`, 和 `mv` 命令，并且假设你已经使用 `sudo su -` 切换到超级用户模式。

---

## 作业 1：简单 - 基础目录操作
**目标：** 熟悉基本的目录切换和查看操作。

**任务：**
1. 使用 `cd` 命令切换到 `/var` 目录。
2. 使用 `ls` 命令列出 `/var` 目录下的所有内容。
3. 返回到你的主目录（使用 `cd ~`）。

**提交内容：**
- 截图或记录 `ls` 命令的输出结果（只需要前几行即可）。

---

## 作业 2：一般 - 创建和删除目录
**目标：** 练习创建和删除目录的操作。

**任务：**
1. 在主目录下使用 `mkdir` 命令创建一个名为 `my_test_folder` 的目录。
2. 使用 `cd` 命令进入 `my_test_folder` 目录。
3. 在 `my_test_folder` 中再创建一个名为 `sub_folder` 的子目录。
4. 使用 `ls` 命令查看 `my_test_folder` 中的内容，确认 `sub_folder` 已创建。
5. 使用 `rm -r` 命令删除 `sub_folder` 目录（`-r` 参数用于递归删除目录及其内容）。
6. 再次使用 `ls` 命令确认 `sub_folder` 已删除。

**提交内容：**
- 记录每一步命令的输入和输出结果。

---

## 作业 3：复杂 - 文件夹的重命名与移动
**目标：** 综合运用所有命令，完成目录和文件的重命名与移动。

**任务：**
1. 在主目录下使用 `mkdir` 命令创建两个目录，分别命名为 `project1` 和 `backup`。
2. 使用 `cd` 命令进入 `project1` 目录，并在其中创建一个名为 `data` 的子目录。
3. 使用 `ls` 命令查看 `project1` 目录的内容，确认 `data` 目录已创建。
4. 使用 `mv` 命令将 `data` 目录重命名为 `data_old`。
5. 再次使用 `ls` 命令确认重命名成功。
6. 使用 `mv` 命令将 `data_old` 目录移动到 `backup` 目录中。
7. 使用 `cd` 命令切换到 `backup` 目录，并用 `ls` 命令确认 `data_old` 目录已成功移动。
8. 最后，使用 `rm -r` 命令删除 `backup` 目录及其内容（即包含 `data_old` 的整个目录）。
9. 使用 `ls` 命令确认 `backup` 目录已删除。

**提交内容：**
- 记录每一步命令的输入和输出结果（可以用文本或截图形式）。
- 简要说明你在执行过程中是否遇到问题，以及如何解决的（如果有）。

---

希望这三个作业能帮助你逐步掌握这些基本命令！如果有任何疑问，随时问我。😊

**教学链接：**
由于你提到需要教学链接，但没有具体要求获取实时信息，我将不使用工具直接提供一些常见的学习资源。如果你需要最新的链接或具体网站内容，请告诉我，我会使用搜索工具为你获取。

- **cd 命令**：你可以参考 [Ubuntu 官方文档](https://help.ubuntu.com/) 或 [Linux 命令教程](https://www.runoob.com/linux/linux-comm-cd.html)
- **ls 命令**：参考 [Linux 命令教程](https://www.runoob.com/linux/linux-comm-ls.html)
- **mkdir 命令**：参考 [Linux 命令教程](https://www.runoob.com/linux/linux-comm-mkdir.html)
- **rm 命令**：参考 [Linux 命令教程](https://www.runoob.com/linux/linux-comm-rm.html)
- **mv 命令**：参考 [Linux 命令教程](https://www.runoob.com/linux/linux-comm-mv.html)
