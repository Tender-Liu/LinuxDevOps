# Python零基础入门教案（第二天）
> 面向对象：完全零基础学员

## Python的基础数据类型

### 1.1 什么是数据类型？
在开始之前，让我们用生活中的例子来理解什么是数据类型：
- 想象你有一个文具盒，里面可以放不同种类的文具
- 铅笔是一种文具，尺子是一种文具，橡皮是一种文具
- 在Python中，不同的数据也有不同的"类型"，就像不同种类的文具

### 1.2 Number（数字类型）

#### 1.2.1 整数（int）
* 生活中的例子：
    - 你现在有5个苹果
    - 教室里有35名学生
    - 银行账户里有1000元

这些都是整数的例子，它们没有小数点，可以是正数、负数或零。

`简单示例：`
```python
# 整数的例子
apple_number = 5
students_number = 35
account_balance = 1000

# 输出：我有5个苹果
print(f"我有{apple_number}个苹果")
print(f"教室里有{students_number}名学生")  
print(f"银行账户里有{account_balance}元")  
```

#### 1.2.2 浮点数（float）

生活中的例子：
* 你的身高是1.75米
* 今天的气温是23.5度
* 一瓶可乐2.5元

这些带小数点的数字就是浮点数。

简单示例：

```python
# 浮点数的例子
height = 1.75
temperature = 23.5
coke_price = 2.5

# 输出：我的身高是1.75米
print(f"我的身高是{height}米")
print(f"今天的气温是{temperature}度")
print(f"一瓶可乐{coke_price}元")

```

#### 1.2.3 布尔值（bool）
生活中的例子：

* 教室的灯是开着的吗？是的（True）或不是（False）
* 你今天吃早饭了吗？是的（True）或不是（False）
* 你是学生吗？是的（True）或不是（False）

布尔值只有两种状态：True（是）和 False（否）

> 注意 if else 简单的逻辑判断  if(如果)   else(否则)

```python
# 布尔值的例子

# 电灯状态   False 关闭  True 打开
light_status = True
# 吃饭状态   False 没吃  True 吃的
eat_status = False
# 你的身份是否  是以为学生   False 不是  True 是的
identity_is_student = True

if light_status == True:
    print("教室电灯是打开的")
else：
    print("教室电灯是关闭的")

if eat_status == True:
    print("我吃过饭了")
else：
    print("我还没有吃饭")

if identity_is_student == True:
    print("我是一名学生")
else：
    print("我不是一名学生")

```

### 1.3 数据类型转换

生活中的例子：

* 把2.5个苹果转换成2个苹果（浮点数→整数）
* 把"5"这个数字字符转换成数字5（字符→整数）
* 判断一个数字是否大于0，得到是或否的结果（数字→布尔值）

```python
# 简单的类型转换例子
number_string = "5"

# 把"5"变成5
number_int = int(number_string)

# 输出：转换前的类型：<class 'str'>
print(f"转换前的类型：{type(number_string)}") 
# 输出：转换后的类型：<class 'int'>
print(f"转换后的类型：{type(number_int)}")  

```

## 2. 实战练习

### 2.1 简单的计算器

让我们制作一个简单的计算器，帮助理解数字类型：

```python
# 这是一个简单的计算器程序
print("简单计算器")
print("==========")

# 获取用户输入的两个数字
number_1 = float(input("请输入第一个数字："))
number_2 = float(input("请输入第二个数字："))

# 显示计算结果
print(f"两个数的和是：{number_1 + number_2}")
print(f"两个数的差是：{number_1 - number_2}")
print(f"两个数的积是：{number_1 * number_2}")
print(f"两个数的商是：{number_1 / number_2}")

```

### 2.2 温度转换器
一个实用的例子 - 将摄氏温度转换为华氏温度：

```python
# 温度转换器
print("温度转换器")
print("==========")

# 获取用户输入的摄氏温度 celsius（摄氏温度）
celsius = float(input("请输入摄氏温度："))

# fahrenheit (华氏温度)
# 转换公式：华氏温度 = 摄氏温度 × 9/5 + 32
fahrenheit = celsius * 9/5 + 32

# 显示结果
print(f"{celsius}°C 等于 {fahrenheit}°F")

```

### 2.3 判断成年

使用布尔值的简单例子：

```python
# 判断是否成年
print("年龄判断器")
print("==========")

# 获取用户输入的年龄
age = int(input("请输入你的年龄："))

# 判断是否成年（大于等于18岁）
if age >= 18:
    print("年龄已满18岁,属于成年人")
else:
    print("年龄未满18岁,属于未年人")


```

## 作业练习

### 1. 基础变量和字符串操作
题目：编写一个程序，接收用户输入的姓名和年龄，然后计算并输出这个人5年后的年龄。
#### 要求
1. 使用input()函数获取用户输入
2. 进行必要的类型转换
3. 使用f-string进行字符串格式化输出

#### 结题思路
1. 使用input()获取姓名(字符串)和年龄(需转换为整数)
2. 定义一个变量表示经过的年数(如x=5)
3. 计算未来年龄
4. 使用f-string格式化输出结果

#### 答案
```python
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
x = 5
future_age = age + x
print(f"你好，{name}！再过{x}年，你就{future_age}岁了。")
```

### 简单密码验证

#### 要求：
编写一个程序，模拟简单的登录验证：
1. 程序内设置一个固定的用户名和密码（如username="admin"，password="12345"）。
2. 接收用户输入的用户名和密码，判断是否正确：
    * 如果正确，输出“登录成功”。
    * 如果用户名或密码错误，输出“用户名或密码错误”。

#### 结题思路：
* 定义固定的用户名和密码。
* 使用input()获取用户输入的用户名和密码。
* 使用if-else判断输入是否匹配。

#### 答案
```python
# 固定用户名和密码
correct_username = "admin"
correct_password = "12345"

# 用户输入
username = input("请输入用户名：")
password = input("请输入密码：")

# 验证
if username == correct_username and password == correct_password:
    print("登录成功")
else:
    print("用户名或密码错误")

```

### 简单猜数字游戏

#### 要求：
1. 程序内设置一个固定的数字（如secret_number = 50）。
2. 接收用户输入的数字，判断用户输入的数字是“大了”“小了”还是“猜对了”。

#### 结题思路：
* 定义一个固定的数字作为答案。
* 使用input()获取用户输入，并转换为int类型。
* 使用if-else判断输入数字与答案的大小关系，并输出对应提示。

#### 答案：
```python
secret_number = 50

guess = int(input("请输入你猜的数字："))

if guess > secret_number:
    print("大了")
else:
    if guess < secret_number:
        print("小了")
    else:
        print("猜对了！")

```

### 简单银行取款机
#### 要求：
编写一个程序，模拟银行取款机的简单功能：

1. 假设账户余额为500元。
2. 接收用户输入的取款金额，判断是否可以取款：
    如果取款金额大于余额，提示“余额不足”。
    如果取款金额为负数，提示“输入金额无效”。
    如果取款金额小于等于余额，完成取款并输出剩余余额。
#### 结题思路：
* 定义一个初始余额变量（如balance = 500）。
* 使用input()获取取款金额，并转换为float类型。
* 使用if-else语句判断取款金额是否合法，并更新余额。

#### 答案：
```python
# 初始余额
balance = 500

# 输入取款金额
withdraw = float(input("请输入取款金额："))

# 判断取款条件
if withdraw > balance:
    print("余额不足")
elif withdraw < 0:
    print("输入金额无效")
else:
    balance -= withdraw
    print(f"取款成功，剩余余额为：{balance}元")

```

### 工资税后计算器

#### 要求：
编写一个程序，计算税后工资：

1. 接收用户输入的税前工资。
2. 如果税前工资不超过5000元，无需缴税，税后工资等于税前工资。
3. 如果税前工资超过5000元，超过部分缴纳10%的税。

#### 结题思路：

1. 使用input()获取税前工资并转换为float类型。
2. 使用if-else语句判断税前工资是否超过5000元，并计算税后工资。
3. 输出税后工资。

#### 答案：
```python
# 输入税前工资
salary = float(input("请输入税前工资："))

# 计算税后工资
if salary <= 5000:
    net_salary = salary
else:
    net_salary = 5000 + (salary - 5000) * 0.9

# 输出结果
print(f"税后工资为：{net_salary}元")

```