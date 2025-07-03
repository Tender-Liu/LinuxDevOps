# Python函数编程基础教程

## 一、函数基础

### 1.1 什么是函数？
函数是组织好的，可重复使用的，用来实现特定功能的代码块。

优点：
1. 提高代码复用性
2. 提高程序的可维护性
3. 提高代码的可读性

### 1.2 函数的基本语法

```python
def 函数名(参数列表):
    '''
    函数说明文档（可选）
    '''
    函数体
    return 返回值（可选）
```

语法说明：
1. `def`：定义函数的关键字
2. `函数名`：
   - 由字母、数字、下划线组成
   - 不能以数字开头
   - 不能使用Python关键字
   - 应该使用有意义的名称
3. `参数列表`：可以为空，也可以有多个参数
4. `函数体`：实现具体功能的代码块
5. `return`：返回函数执行的结果

### 1.3 简单示例

```python
# 示例1：无参数无返回值的函数
def say_hello():
    print("你好，世界！")

# 示例2：有参数的函数
def greet(name):
    print(f"你好，{name}！")

# 示例3：有返回值的函数
def add_numbers(num1, num2):
    return num1 + num2
```

### 1.4 函数的调用

```python
# 调用无参数函数
say_hello()  # 输出：你好，世界！

# 调用有参数函数
greet("小明")  # 输出：你好，小明！

# 调用有返回值的函数
result = add_numbers(5, 3)
print(result)  # 输出：8
```

## 二、函数参数详解

### 2.1 位置参数
最基本的参数形式，调用时必须按照定义的顺序传入参数。

```python
def print_student_info(name, age, grade):
    print(f"姓名：{name}，年龄：{age}，年级：{grade}")

# 正确的调用方式
print_student_info("小明", 15, "初三")

# 错误的调用方式（参数顺序错误）
print_student_info(15, "小明", "初三")  # 逻辑错误
```

### 2.2 关键字参数
通过参数名指定参数值，可以不按照定义顺序。

```python
def print_student_info(name, age, grade):
    print(f"姓名：{name}，年龄：{age}，年级：{grade}")

# 使用关键字参数，顺序可以不同
print_student_info(age=15, name="小明", grade="初三")
print_student_info(grade="初三", name="小明", age=15)
```

### 2.3 默认参数
为参数提供默认值，调用时可以不传入该参数。

```python
def set_user_info(name, age=18, city="北京"):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 使用默认参数
set_user_info("小明")  # 使用所有默认值
set_user_info("小红", 20)  # 指定年龄，使用默认城市
set_user_info("小华", 22, "上海")  # 指定所有参数
```

## 三、基础练习

### 练习1：简单计算器
要求：
1. 编写一个函数，实现两个数的加法
2. 编写一个函数，实现两个数的乘法

```python
# 加法函数
def add_numbers(num1, num2):
    return num1 + num2

# 乘法函数
def multiply_numbers(num1, num2):
    return num1 * num2

# 测试代码
print(add_numbers(5, 3))      # 输出：8
print(multiply_numbers(4, 6))  # 输出：24
```

### 练习2：问候函数
要求：
1. 编写一个函数，根据时间段返回不同的问候语
2. 早上：早上好，下午：下午好，晚上：晚上好

```python
def get_greeting(hour):
    if 5 <= hour < 12:
        return "早上好"
    elif 12 <= hour < 18:
        return "下午好"
    else:
        return "晚上好"

# 测试代码
print(get_greeting(9))   # 输出：早上好
print(get_greeting(14))  # 输出：下午好
print(get_greeting(20))  # 输出：晚上好
```

### 练习3：成绩等级转换
要求：
1. 编写一个函数，将分数转换为等级
2. 90-100：A，80-89：B，70-79：C，60-69：D，60以下：E

```python
def get_grade(score):
    if not isinstance(score, (int, float)):
        return "请输入有效的分数"
    
    if score < 0 or score > 100:
        return "分数必须在0-100之间"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

# 测试代码
print(get_grade(95))  # 输出：A
print(get_grade(85))  # 输出：B
print(get_grade(75))  # 输出：C
print(get_grade(65))  # 输出：D
print(get_grade(55))  # 输出：E
```

## 四、进阶内容

### 4.1 函数的类型注解
从Python 3.5开始，可以为函数参数和返回值添加类型提示。

```python
def calculate_sum(num1: float, num2: float) -> float:
    """计算两个浮点数的和
    
    Args:
        num1: 第一个数
        num2: 第二个数
    
    Returns:
        两个数的和
    """
    return num1 + num2

# 使用示例
result = calculate_sum(3.14, 2.86)
print(result)  # 输出：6.0
```

类型注解的好处：
1. 提高代码可读性
2. 帮助IDE提供更好的代码提示
3. 方便代码维护
4. 有助于发现潜在的类型错误

### 4.2 进阶练习

#### 练习1：带类型注解的计算器
要求：
1. 实现加、减、乘、除四则运算
2. 使用类型注解
3. 处理异常情况

```python
def calculator(num1: float, num2: float, operator: str = '+') -> float:
    """实现基本的四则运算
    
    Args:
        num1: 第一个数
        num2: 第二个数
        operator: 运算符（+、-、*、/）
    
    Returns:
        计算结果
    
    Raises:
        ValueError: 当运算符不支持时
        ZeroDivisionError: 当除数为0时
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("除数不能为0")
        return num1 / num2
    else:
        raise ValueError(f"不支持的运算符：{operator}")

# 测试代码
try:
    print(calculator(10, 5, '+'))  # 15.0
    print(calculator(10, 5, '-'))  # 5.0
    print(calculator(10, 5, '*'))  # 50.0
    print(calculator(10, 5, '/'))  # 2.0
    print(calculator(10, 0, '/'))  # 引发异常
except Exception as e:
    print(f"错误：{e}")
```

学习建议：
1. 先掌握基本语法
2. 多写多练
3. 从简单函数开始
4. 逐步添加复杂功能
5. 注意代码规范
6. 养成写注释的习惯
7. 学会处理异常情况



## 五、综合案例：函数版登录注册系统

### 5.1 系统概述
将之前的登录注册系统使用函数式编程方式重新实现，主要功能：
1. 用户注册
2. 用户登录（三次尝试机会）
3. 数据验证
4. 菜单系统

### 5.2 代码实现

```python
# 初始化用户数据
def init_user_data():
    """初始化用户数据，返回包含默认用户的列表"""
    return [
        {"username": "admin", "password": "123456"}
    ]

def display_menu():
    """显示主菜单"""
    print("\n=== 用户管理系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    return input("请选择操作：")

def validate_username(username: str) -> bool:
    """验证用户名是否合法
    
    Args:
        username: 要验证的用户名
    
    Returns:
        bool: 用户名是否合法
    """
    return len(username) >= 4

def validate_password(password: str) -> bool:
    """验证密码是否合法
    
    Args:
        password: 要验证的密码
    
    Returns:
        bool: 密码是否合法
    """
    return len(password) >= 6

def check_username_exists(users: list, username: str) -> bool:
    """检查用户名是否已存在
    
    Args:
        users: 用户列表
        username: 要检查的用户名
    
    Returns:
        bool: 用户名是否存在
    """
    return any(user["username"] == username for user in users)

def register_user(users: list) -> bool:
    """用户注册功能
    
    Args:
        users: 用户列表
    
    Returns:
        bool: 注册是否成功
    """
    print("\n--- 新用户注册 ---")
    
    # 输入并验证用户名
    while True:
        username = input("请输入用户名（至少4个字符）：")
        if not validate_username(username):
            print("用户名太短，请重新输入！")
            continue
        
        if check_username_exists(users, username):
            print("用户名已存在，请重新输入！")
            continue
        break
    
    # 输入并验证密码
    while True:
        password1 = input("请输入密码（至少6个字符）：")
        if not validate_password(password1):
            print("密码太短，请重新输入！")
            continue
        
        password2 = input("请再次输入密码：")
        if password1 != password2:
            print("两次密码不一致，请重新输入！")
            continue
        break
    
    # 保存新用户
    users.append({"username": username, "password": password1})
    print("\n注册成功！")
    print(f"当前系统用户数：{len(users)}")
    return True

def login_user(users: list) -> bool:
    """用户登录功能
    
    Args:
        users: 用户列表
    
    Returns:
        bool: 登录是否成功
    """
    print("\n--- 用户登录 ---")
    username = input("请输入用户名：")
    
    # 普通写法， 查找用户
    user = None
    for u in users:
        if u["username"] == username:
            user = u
            break

    # 高级写法，查找用户  --  学员的自我修改哦
    # user = next((user for user in users if user["username"] == username), None)
    # if not user:
    #     print("用户名不存在！")
    #     return False
    
    # 尝试登录，最多3次机会
    attempts = 3
    while attempts > 0:
        print(f"\n剩余尝试次数：{attempts}")
        password = input("请输入密码：")
        
        if user["password"] == password:
            print("登录成功！")
            return True
        
        print("密码错误！")
        attempts -= 1    
    print("\n错误次数过多，账号已锁定！")
    return False

def main():
    """主函数，程序入口"""
    users = init_user_data()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            if login_user(users):
                break
        elif choice == "2":
            register_user(users)
        elif choice == "3":
            print("退出系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 程序入口
if __name__ == "__main__":
    main()
```

### 5.3 代码说明

1. **函数化设计**
   - 每个功能都封装成独立函数
   - 函数职责单一，易于维护
   - 使用类型注解提高代码可读性

2. **数据验证函数**
   - `validate_username`: 验证用户名长度
   - `validate_password`: 验证密码长度
   - `check_username_exists`: 检查用户名是否存在

3. **核心功能函数**
   - `register_user`: 处理用户注册
   - `login_user`: 处理用户登录
   - `display_menu`: 显示系统菜单

4. **主程序设计**
   - 使用 `main()` 函数作为程序入口
   - 通过 `if __name__ == "__main__":` 控制执行

### 5.4 改进建议

1. **安全性改进**
   ```python
   def hash_password(password: str) -> str:
       """对密码进行加密"""
       import hashlib
       return hashlib.sha256(password.encode()).hexdigest()
   ```

2. **数据持久化**
   ```python
   def save_users(users: list):
       """保存用户数据到文件"""
       import json
       with open('users.json', 'w') as f:
           json.dump(users, f)
   ```

3. **密码强度检查**
   ```python
   def check_password_strength(password: str) -> bool:
       """检查密码强度"""
       has_digit = any(c.isdigit() for c in password)
       has_letter = any(c.isalpha() for c in password)
       return has_digit and has_letter and len(password) >= 6
   ```

### 5.5 练习建议

1. 尝试实现以下功能：
   - 添加用户信息修改功能
   - 实现管理员特权操作
   - 添加用户注销功能

2. 代码优化方向：
   - 添加更多的参数验证
   - 实现日志记录功能
   - 优化用户界面
   - 添加异常处理

通过这个综合案例，你可以：
1. 学习如何将大型程序拆分成小函数
2. 理解函数式编程的优势
3. 掌握类型注解的使用
4. 提高代码组织能力
