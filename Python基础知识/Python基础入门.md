# Python基础入门

## 第一部分：Python简介

### 1. 什么是Python？

#### 🌟 生活类比：
想象Python就像是一把"瑞士军刀"，它可以做很多事情：

* 切菜（处理数据）
* 开瓶器（自动化工作）
* 剪刀（处理文件） 等等...

### Python能做什么？
让我们看看身边的Python应用：

* 抖音短视频（后台数据处理）
* 微信支付（网络服务）
* 王者荣耀（游戏服务器）
* 特斯拉自动驾驶（人工智能）

### 为什么选择Python？
* 作为后续Linux运维、云计算的基础
* 自动化运维的首选语言
* 广泛的应用领域：Web开发、数据分析、人工智能
* 简单易学，适合编程入门

```bash
Python基础 → Linux基础 → 云计算基础 → DevOps实践

```

## 2. 环境搭建

### 2.1 Python安装
#### 步骤1：下载Python
1. 访问官方网站：https://www.python.org/downloads/
2. 下载Python 3.12.x Windows安装包
3. 注意选择与系统匹配的版本（32位/64位）
    ![python官网](/Python基础知识/images/python官网.png "python官网")

#### 步骤2：安装Python
1. 双击安装包运行
2. ⚠️重要：勾选"Add Python to PATH"
3. 选择"Install Now"（推荐）或"Customize installation"
    ![python安装1](/Python基础知识/images/python安装1.png "python安装1")
    ![python安装2](/Python基础知识/images/python安装2.png "python安装2")
    ![python安装3](/Python基础知识/images/python安装3.png "python安装3")

4. 等待安装完成
    ![python安装完成](/Python基础知识/images/python安装完成.png "python安装完成")

#### 步骤3：验证安装
1. 打开命令提示符（Win+R，输入cmd）
![cmd](/Python基础知识/images/cmd.png "cmd")
2. 输入以下命令验证：
```bash
python --version
pip --version

```
![python环境检查](/Python基础知识/images/python环境检查.png "python环境检查")

### VS Code安装与配置

#### 步骤1：安装VS Code
1. 访问：https://code.visualstudio.com/
2. 下载Windows版本
3. 运行安装程序
4. 建议勾选：
5. "添加到右键菜单"
6. "添加到PATH"

### 步骤2：安装Python扩展

* 打开VS Code
* 点击左侧扩展图标（或Ctrl+Shift+X）
    ![安装插件](/Python基础知识/images/安装插件.png "安装插件")
* 搜索"Python"
* 安装以下扩展：
    * Chinese (Simplified) (简体中文) Language Pack for Visual 
    * Python（Microsoft官方）
    * Python Extension Pack （包含多个实用工具）
    * Python Indent （Python代码格式化工具）
    * Pylance（Python语言服务器）

### 步骤4：配置Python环境与创建第一个Python项目
1. 创建新文件夹：python_learning
2. VS Code中打开该文件夹
    ![打开文件夹](/Python基础知识/images/打开文件夹.png "打开文件夹")
3. 创建新文件：hello.py
    ![创建Py文件](/Python基础知识/images/创建Py文件.png "创建Py文件")
4. 选择Python解释器（右下角或Ctrl+Shift+P）
    ![解释器一](/Python基础知识/images/解释器一.png "解释器一")
    ![解释器二](/Python基础知识/images/解释器二.png "解释器二")

###  编写第一个程序（20分钟）
```bash
# hello.py
print("Hello, Python!")
name = input("请输入你的名字：")
print(f"你好，{name}！")
```
![点击运行](/Python基础知识/images/点击运行.png "点击运行")


## 3. Python基础语法
### 3.1 Python基本语法规则
> 需要结合菜鸟网站文档学习：https://www.runoob.com/python3/python3-basic-syntax.html
* 缩进的重要性
* 注释的使用（# 和 """）
* 语句和表达式
* 命名规范
    1. 第一个字符必须以字母（a-z, A-Z）或下划线 _ 。
    2. 标识符的其他的部分由字母、数字和下划线组成。
    3. 标识符对大小写敏感，count 和 Count 是不同的标识符。
    4. 标识符对长度无硬性限制，但建议保持简洁（一般不超过 20 个字符）。
    5. 禁止使用保留关键字，如 if、for、class 等不能作为标识符。

```bash
# 示例代码
def greet(name):    # 函数定义
    """这是一个问候函数"""    # 文档字符串
    print(f"Hello, {name}")    # 函数体

# 调用函数
greet("张三")

```

### 3.2 变量和数据类型（基础）
```bash
# 变量定义
name = "Python"    # 字符串
age = 30           # 整数
price = 3.14       # 浮点数
is_student = True  # 布尔值

# 打印变量类型
print(type(name))
print(type(age))
print(type(price))
print(type(is_student))

```

## 四、数据类型与变量

### 4.1 数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

* int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
* bool (布尔), 如 True。
* float (浮点数), 如 1.23、3E-2
* complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
```bash
# 整数
age = 25
count = 1_000_000  # 使用下划线分隔数字

# 浮点数
pi = 3.14159
score = 98.5

# 运算
result = age + 5
print(result)

```

### 4.2 字符串
* Python 中单引号 ' 和双引号 " 使用完全相同。
* 使用三引号(''' 或 """)可以指定一个多行字符串。
* 转义符 \。
* 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
* 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
* 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
* Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
* Python 中的字符串不能改变。
* Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
* 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
* 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]


```bash
# 字符串定义
name = "Python编程"
description = '这是一门课程'
long_text = """
这是多行
字符串
"""

# 字符串操作
print(name[0])      # 索引
print(name[0:2])    # 切片
print(len(name))    # 长度
print(name + "课")  # 拼接

```

### 4.3 列表（初步介绍）

