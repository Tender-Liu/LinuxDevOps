# Python零基础入门教案（第一天）
> 面向对象：完全零基础学员

## 课程目标
* 掌握Python基本语法规则
* 理解并运用不同数据类型
* 能够进行基础的数据类型转换
* 完成简单的程序编写

## 课前准备
1. 确保每位学员电脑已安装Python和VS Code
2. 桌面新建文件夹：python_learning
3. 在该文件夹中创建 day1.py

## 一、什么是编程
### 1.1 生活中的编程
想象你在教一个机器人做事情：

1. 机器人只能听懂非常明确的指令
2. 必须按照顺序一步一步告诉它
3. 不能跳步或含糊其辞

### 1.2 Python是什么
* Python就是一种告诉计算机做事的语言
* 特点：简单、易学、容易读懂
* 应用：网站开发、人工智能、数据分析等

## 二、第一个Python程序
### 2.1 打开VS Code
* 双击桌面VS Code图标
* 点击"文件" -> "打开文件夹"
* 选择桌面的python_learning文件夹
* 打开day1.py

### 2.2 Hello World
```bash
print("Hello World")

```
* 【操作步骤】

    1. 输入上面这行代码
    2. 点击右上角的播放按钮▶运行
    3. 观察下方输出窗口
* 【解释】

    1. print 是Python的打印函数
    2. 用来在屏幕上显示内容
    3. 引号内的内容会原样显示

### 2.3 动手练习
```bash
# 练习1：打印自己的名字
print("张三")

# 练习2：打印多行文字
print("我是第一行")
print("我是第二行")

```


## 三、认识数据
### 3.1 数字
```bash
# 打印数字
print(666)        # 整数
print(13.14)      # 小数

# 基本计算
print(3 + 2)      # 加法
print(3 - 2)      # 减法
print(3 * 2)      # 乘法
print(3 / 2)      # 除法

```


### 3.2 文字（字符串）
```bash
# 打印文字
print("我爱Python")  # 双引号
print('Hello')      # 单引号都可以

# 看我，看我，这位是错误的示范
print("你好'）      # 引号必须成对

```

## 四、变量入门

### 4.1 什么是变量
把变量想象成一个贴了标签的盒子：
* 盒子里可以放东西（数据）
* 标签就是变量名
* 随时可以改变盒子里的内容


### 4.2 使用变量
```bash
# 存储数字
age = 18
print(age)

# 存储文字
name = "小明"
print(name)

# 修改变量内容
age = 20
print(age)

```

### 4.3 变量的简单计算
```bash
# 数字计算
num1 = 10
num2 = 5
print(num1 + num2)   # 15
print(num1 - num2)   # 5

# 更新变量
score = 0
score = score + 10   # score现在是10
print(score)

```

## 五、接收用户输入
### 5.1 input()函数
```bash
# 基本输入
name = input("请输入你的名字：")
print("你好，" + name)

```


### 5.2 综合练习
```bash
# 制作简单的个人信息卡
print("====个人信息收集====")
name = input("请输入姓名：")
age = input("请输入年龄：")
hobby = input("请输入爱好：")

print("=====信息展示=====")
print("姓名：" + name)
print("年龄：" + age)
print("爱好：" + hobby)

```

## 六、课堂实战练习
### 6.1 基础练习
```bash
# 练习1：打印个人介绍
print("自我介绍")
print("我叫小明")
print("今年18岁")
print("来自北京")

# 练习2：简单计算
num1 = 15
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

```

### 6.2 综合练习：简单计算器
```bash
print("简单计算器")
print("=============")

# 获取用户输入
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

# 转换为数字
num1 = int(num1)
num2 = int(num2)

# 显示计算结果
print("计算结果：")
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "×", num2, "=", num1 * num2)
print(num1, "÷", num2, "=", num1 / num2)

```

## 课后作业

1. 制作一个自我介绍程序，要求：

    * 使用print输出至少3行个人信息
    * 使用变量存储信息
    * 使用input获取用户输入

2. 编写一个简单的商品价格计算程序：
    * 输入商品单价
    * 输入购买数量
    * 计算并显示总价