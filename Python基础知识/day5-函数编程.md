# Python函数编程基础教程

## 一、函数基础

### 1.1 什么是函数？
函数是一段组织好的、可重复使用的代码块，用于实现特定的功能。函数就像一个工具箱中的工具，可以在程序中多次调用，减少重复编写代码的工作。

**函数的优点：**
1. 提高代码复用性：写一次函数，可以在多个地方调用。
2. 提高程序的可维护性：修改功能时只需改函数内部代码，不用改多处。
3. 提高代码的可读性：通过有意义的函数名，让代码逻辑更清晰。

### 1.2 函数的基本语法

```python
def 函数名(参数列表):
    """
    函数说明文档（可选）：用于描述函数的作用、参数和返回值
    """
    函数体  # 实现具体功能的代码
    return 返回值  # 可选，返回函数的结果
```

**语法详细说明：**
1. `def`：定义函数的关键字，告诉 Python 我们要创建一个函数。
2. `函数名`：函数的名字，规则如下：
   - 由字母、数字、下划线组成。
   - 不能以数字开头。
   - 不能使用 Python 关键字（如 `if`、`for` 等）。
   - 建议使用有意义的名称，比如 `say_hello` 表示打招呼。
3. `参数列表`：函数可以接受输入数据，参数可以有多个，也可以没有。
4. `函数体`：函数内部的代码，完成具体功能。
5. `return`：用于返回函数的结果，如果没有 `return`，函数默认返回 `None`。

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
    result = num1 + num2
    return result


# 控制程序的执行入口    
if __name__ == "__main__":
    # 调用函数进行测试
    say_hello()  # 输出：你好，世界！
    greet("小明")  # 输出：你好，小明！
    sum_result = add_numbers(5, 3)
    print(sum_result)  # 输出：8
```

### 1.4 函数的调用
调用函数就是执行函数内的代码。调用时需要提供函数名和对应的参数（如果有）。

**调用示例**：如上代码中的 `say_hello()`、`greet("小明")` 和 `add_numbers(5, 3)`。

### 1.5 额外知识点介绍：if __name__ == "__main__": 的作用
在 Python 中，`if __name__ == "__main__":` 是一种常见的写法，用于控制程序的执行入口。
- `__name__` 是 Python 的一个内置变量，表示当前模块的名字。
- 当一个 Python 文件直接运行时，`__name__` 的值是 `"__main__"`。
- 当这个文件被其他文件导入时，`__name__` 的值是文件名（不包含 `.py` 后缀）。
- 使用 `if __name__ == "__main__":`，可以确保某些代码只在直接运行文件时执行，而不会在被导入时执行。

**简单来说**：这段代码的作用是指定程序的入口，只有直接运行这个文件时才会执行 `main()` 函数。如果这个文件被别的程序导入，`main()` 函数不会自动运行。

## 二、函数参数详解

### 2.1 位置参数
最基本的参数形式，调用时必须按照定义的顺序传入参数。

```python
def print_student_info(name, age, grade):
    print(f"姓名：{name}，年龄：{age}，年级：{grade}")


# 控制程序的执行入口    
if __name__ == "__main__":
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



# 控制程序的执行入口    
if __name__ == "__main__":
    # 使用关键字参数，顺序可以不同
    print_student_info(age=15, name="小明", grade="初三")
    print_student_info(grade="初三", name="小明", age=15)
```

### 2.3 默认参数
为参数提供默认值，调用时可以不传入该参数。

```python
def set_user_info(name, age=18, city="北京"):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 控制程序的执行入口    
if __name__ == "__main__":
    # 使用默认参数
    set_user_info("小明")  # 输出：姓名：小明，年龄：18，城市：北京
    set_user_info("小红", 20)  # 输出：姓名：小红，年龄：20，城市：北京
    set_user_info("小华", 22, "上海")  # 输出：姓名：小华，年龄：22，城市：上海
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


# 控制程序的执行入口    
if __name__ == "__main__":
    # 测试代码
    print(add_numbers(5, 3))      # 输出：8
    print(multiply_numbers(4, 6))  # 输出：24
```

### 练习2：问候函数
**要求：**
1. 编写一个函数，根据时间段返回不同的问候语。
2. 早上（5-11点）：早上好；下午（12-17点）：下午好；晚上（其他时间）：晚上好。

```python
def get_greeting(hour):
    if 5 <= hour < 12:
        return "早上好"
    elif 12 <= hour < 18:
        return "下午好"
    else:
        return "晚上好"


# 控制程序的执行入口    
if __name__ == "__main__":
    # 测试代码
    morning_greeting = get_greeting(9)
    print(morning_greeting)  # 输出：早上好
    afternoon_greeting = get_greeting(14)
    print(afternoon_greeting)  # 输出：下午好
    evening_greeting = get_greeting(20)
    print(evening_greeting)  # 输出：晚上好
```

### 练习3：成绩等级转换
**要求：**
1. 编写一个函数，将分数转换为等级。
2. 90-100：A；80-89：B；70-79：C；60-69：D；60以下：E。

```python
def get_grade(score):
    # 首先检查输入是否为数字类型
    # 将 `isinstance` 检查拆分成更直观的逻辑，避免嵌套写法。注释中详细说明每个步骤的作用，方便初学者理解。
    # isinstance 用于判断你的值，是否是指定的类型
    if not isinstance(score, int) and not isinstance(score, float):
        return "请输入有效的分数"
    
    # 检查分数范围是否合法
    if score < 0 or score > 100:
        return "分数必须在0-100之间"
    
    # 根据分数返回等级
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


# 控制程序的执行入口    
if __name__ == "__main__":
    # 测试代码
    grade1 = get_grade(95)
    print(grade1)  # 输出：A
    grade2 = get_grade(85)
    print(grade2)  # 输出：B
    grade3 = get_grade(75)
    print(grade3)  # 输出：C
    grade4 = get_grade(65)
    print(grade4)  # 输出：D
    grade5 = get_grade(55)
    print(grade5)  # 输出：E
```

## 四、进阶内容

### 4.1 函数的类型注解
从 Python 3.5 开始，可以为函数的参数和返回值添加类型提示（类型注解），这有助于提高代码的可读性和维护性。

```python
def calculate_sum(num1: float, num2: float) -> float:
    """
    计算两个浮点数的和
    
    参数:
        num1: 第一个数
        num2: 第二个数
    
    返回值:
        两个数的和
    """
    result = num1 + num2
    return result



# 控制程序的执行入口    
if __name__ == "__main__":
    # 使用示例
    result = calculate_sum(3.14, 2.86)
    print(result)  # 输出：6.0
```

**类型注解的好处：**
1. 提高代码可读性，明确参数和返回值的类型。
2. 帮助开发工具（如 IDE）提供更好的代码提示。
3. 方便代码维护，减少类型错误。
4. 为团队协作提供清晰的接口定义。

### 4.2 进阶练习

#### 练习1：带类型注解的计算器
**要求：**
1. 实现加、减、乘、除四则运算。
2. 使用类型注解。
3. 处理异常情况。


**额外知识点介绍：try-except 异常处理**
在 Python 中，程序运行时可能会遇到错误（如除以零），我们可以使用 `try-except` 结构来捕获这些错误并进行处理，避免程序直接崩溃。
- `try`：尝试执行可能出错的代码。
- `except`：如果 `try` 中的代码出错，执行 `except` 中的代码。


```python
def calculator(num1: float, num2: float, operator: str) -> float:
    """
    实现基本的四则运算
    
    参数:
        num1: 第一个数
        num2: 第二个数
        operator: 运算符（+、-、*、/）
    
    返回值:
        计算结果
    
    异常:
        ValueError: 当运算符不支持时
        ZeroDivisionError: 当除数为0时
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("除数不能为0")
        return num1 / num2
    else:
        raise ValueError("不支持的运算符：" + operator)


# 控制程序的执行入口    
if __name__ == "__main__":
    # 测试代码，使用 try-except 处理异常
    try:
        result1 = calculator(10, 5, "+")
        print(result1)  # 输出：15.0
        result2 = calculator(10, 5, "-")
        print(result2)  # 输出：5.0
        result3 = calculator(10, 5, "*")
        print(result3)  # 输出：50.0
        result4 = calculator(10, 5, "/")
        print(result4)  # 输出：2.0
        result5 = calculator(10, 0, "/")  # 这里会引发异常
        print(result5)
    except ZeroDivisionError as error:
        print("错误：" + str(error))
    except ValueError as error:
        print("错误：" + str(error))
```

**优化说明**：在测试代码中引入 `try-except` 异常处理，并详细注释每个运算的输出结果。异常处理部分使用字符串拼接，确保初学者能看懂。

**学习建议：**

1. 先掌握基本语法
2. 多写多练
3. 从简单函数开始
4. 逐步添加复杂功能
5. 注意代码规范
6. 养成写注释的习惯
7. 学会处理异常情况


## 五、综合案例：函数版登录注册系统

### 5.1 系统概述
本案例将之前的登录注册系统用函数式编程方式重新实现，主要功能包括：
1. 用户注册。
2. 用户登录（三次尝试机会）。
3. 数据验证。
4. 菜单系统。

### 5.2 分阶段实现指南
对于初学者来说，面对一个完整的系统代码可能会感到无从下手。因此，我们将这个登录注册系统的实现分为几个阶段，逐步完成每个功能。每个阶段都有明确的目标和逻辑分析，帮助你理清思路，一步步构建整个程序。每个阶段的说明下方会直接提供需要实现的函数代码，方便你结合逻辑理解代码。

#### 实现前的逻辑梳理
在开始编写代码之前，我们需要先理清系统的整体逻辑和工作流程：
1. **明确系统的功能需求**：这个系统需要实现菜单显示、用户注册、用户登录和退出功能。
2. **拆分功能为小模块**：将大功能拆分成小的函数，每个函数只负责一个具体任务。例如，显示菜单用一个函数，注册用户用另一个函数。
3. **确定函数之间的依赖关系**：比如，注册和登录功能需要用户数据，所以要先初始化用户数据；登录和注册前需要先显示菜单获取用户选择。
4. **按优先级实现函数**：先实现基础功能（如初始化数据和显示菜单），再实现核心功能（如注册和登录），最后完善细节（如数据验证）。
5. **逐步测试**：每完成一个函数就测试一下，确保它能正常工作，再继续下一步。

通过这种方式，我们可以把复杂的系统分解成小步骤，降低学习难度。

#### 阶段划分与实现顺序
以下是具体的实现阶段，每个阶段的目标和函数实现顺序已经为你规划好。你可以按照这个顺序一步步完成代码编写，每个阶段的代码会直接嵌入在说明下方。

**阶段 1：搭建基础框架**
- **目标**：初始化用户数据并搭建程序的基本框架。
- **要实现的函数**：
  1. `init_user_data()`：初始化用户数据，返回一个包含默认用户的列表。
  2. `display_menu()`：显示主菜单并获取用户选择。
  3. `main()`：作为程序入口，调用菜单函数并根据选择执行不同操作。
- **逻辑分析**：这一阶段是系统的起点，我们需要先有用户数据（哪怕是空的），然后通过菜单让用户选择操作，最后在主函数中控制程序流程。暂时不实现注册和登录功能，只打印用户的选择以测试菜单是否正常工作。
- **测试重点**：运行程序后，检查菜单是否能正常显示，用户输入选择后程序是否能正确接收并打印出来。
- **实现代码**：

```python
# 初始化用户数据
def init_user_data():
    """
    初始化用户数据，返回包含默认用户的列表
    """
    user_list = [
        {"username": "admin", "password": "123456"}
    ]
    return user_list

def display_menu():
    """
    显示主菜单，并返回用户的选择
    """
    print("\n=== 用户管理系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    choice = input("请选择操作：")
    return choice

def main():
    """
    主函数，程序入口
    """
    users = init_user_data()
    
    while True:
        choice = display_menu()
        print("你选择了：" + choice)  # 暂时打印选择，测试菜单是否工作
        if choice == "3":
            print("退出系统，再见！")
            break

# 程序入口，只有直接运行此文件时才会执行 main() 函数
if __name__ == "__main__":
    main()
```

**阶段 2：实现用户注册功能**
- **目标**：完成用户注册功能，包括输入用户名和密码，并保存到用户列表中。
- **要实现的函数**：
  1. `register_user(users)`：处理用户注册逻辑，允许用户输入用户名和密码，并保存到列表中。
- **逻辑分析**：注册功能需要接收用户输入的用户名和密码，然后将这些信息存储到用户数据列表中。暂时不做复杂的验证，只确保能输入和保存数据。在 `main()` 中，当用户选择“2”时调用此函数。
- **测试重点**：运行程序，选择注册选项，输入用户名和密码后，检查是否能看到“注册成功”的提示，并通过打印用户列表确认数据是否保存。
- **实现代码**：

```python
def register_user(users: list) -> bool:
    """
    用户注册功能
    
    参数:
        users: 用户列表
    
    返回值:
        bool: 注册是否成功
    """
    print("\n--- 新用户注册 ---")
    
    # 输入用户名和密码，暂时不做验证
    username = input("请输入用户名：")
    password = input("请输入密码：")
    
    # 保存新用户
    new_user = {"username": username, "password": password}
    users.append(new_user)
    print("\n注册成功！")
    total_users = len(users)
    print("当前系统用户数：" + str(total_users))
    return True

# 修改 main() 函数，添加注册功能调用
def main():
    """
    主函数，程序入口
    """
    users = init_user_data()
    
    while True:
        choice = display_menu()
        if choice == "1":
            print("登录功能暂未实现")
        elif choice == "2":
            register_user(users)
            print("当前用户列表：")
            for user in users:
                print(user)  # 打印用户列表，测试是否保存成功
        elif choice == "3":
            print("退出系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 程序入口
if __name__ == "__main__":
    main()
```

**阶段 3：实现用户登录功能**
- **目标**：完成用户登录功能，允许用户输入用户名和密码进行验证。
- **要实现的函数**：
  1. `login_user(users)`：处理用户登录逻辑，检查用户名是否存在以及密码是否正确。
- **逻辑分析**：登录功能需要先查找用户输入的用户名是否在列表中，如果存在则比对密码是否正确。暂时允许无限次尝试密码，不设置次数限制。在 `main()` 中，当用户选择“1”时调用此函数。
- **测试重点**：运行程序，选择登录选项，输入正确的用户名和密码，检查是否能看到“登录成功”的提示；输入错误的用户名或密码，检查是否会提示错误。
- **实现代码**：

```python
def login_user(users: list) -> bool:
    """
    用户登录功能
    
    参数:
        users: 用户列表
    
    返回值:
        bool: 登录是否成功
    """
    print("\n--- 用户登录 ---")
    username = input("请输入用户名：")
    
    # 查找用户
    found_user = None
    for user in users:
        if user["username"] == username:
            found_user = user
            break
    
    if found_user is None:
        print("用户名不存在！")
        return False
    
    # 验证密码，暂时不限制尝试次数
    password = input("请输入密码：")
    if found_user["password"] == password:
        print("登录成功！")
        return True
    else:
        print("密码错误！")
        return False

# 修改 main() 函数，添加登录功能调用
def main():
    """
    主函数，程序入口
    """
    users = init_user_data()
    
    while True:
        choice = display_menu()
        if choice == "1":
            login_success = login_user(users)
            if login_success:
                break  # 登录成功后退出循环
        elif choice == "2":
            register_user(users)
            print("当前用户列表：")
            for user in users:
                print(user)
        elif choice == "3":
            print("退出系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 程序入口
if __name__ == "__main__":
    main()
```

**阶段 4：完善数据验证功能**
- **目标**：为注册和登录功能添加数据验证，确保输入合法。
- **要实现的函数**：
  1. `validate_username(username)`：验证用户名长度是否合法（至少4个字符）。
  2. `validate_password(password)`：验证密码长度是否合法（至少6个字符）。
  3. `check_username_exists(users, username)`：检查用户名是否已存在。
- **逻辑分析**：这一阶段是为注册功能添加约束条件，避免用户输入无效数据（如用户名太短）或重复用户名。在注册函数中调用这些验证函数，确保只有合法数据才能保存。
- **测试重点**：运行程序，尝试注册时输入过短的用户名或密码，检查是否会提示重新输入；尝试注册已存在的用户名，检查是否会提示用户名已存在。
- **实现代码**：

```python
def validate_username(username: str) -> bool:
    """
    验证用户名是否合法
    
    参数:
        username: 要验证的用户名
    
    返回值:
        bool: 用户名是否合法（长度是否大于等于4）
    """
    if len(username) >= 4:
        return True
    else:
        return False
    # 注释：这里可以用三元运算符简写为 return len(username) >= 4，但为了初学者理解，展开写成if-else形式

def validate_password(password: str) -> bool:
    """
    验证密码是否合法
    
    参数:
        password: 要验证的密码
    
    返回值:
        bool: 密码是否合法（长度是否大于等于6）
    """
    if len(password) >= 6:
        return True
    else:
        return False

def check_username_exists(users: list, username: str) -> bool:
    """
    检查用户名是否已存在
    
    参数:
        users: 用户列表
        username: 要检查的用户名
    
    返回值:
        bool: 用户名是否存在
    """
    for user in users:
        if user["username"] == username:
            return True
    return False

# 修改 register_user() 函数，添加数据验证逻辑
def register_user(users: list) -> bool:
    """
    用户注册功能
    
    参数:
        users: 用户列表
    
    返回值:
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
    new_user = {"username": username, "password": password1}
    users.append(new_user)
    print("\n注册成功！")
    total_users = len(users)
    print("当前系统用户数：" + str(total_users))
    return True
```

**阶段 5：完善登录尝试次数限制**
- **目标**：为登录功能添加尝试次数限制，最多3次机会。
- **要实现的函数**：修改 `login_user(users)` 函数，添加尝试次数逻辑。
- **逻辑分析**：在登录函数中，使用一个变量记录尝试次数，每次密码错误时减少次数，当次数为0时提示账号锁定并退出登录。
- **测试重点**：运行程序，选择登录选项，连续输入错误密码3次，检查是否会提示“账号已锁定”；输入正确密码时，检查是否能登录成功。
- **实现代码**：

```python
# 修改 login_user() 函数，添加尝试次数限制
def login_user(users: list) -> bool:
    """
    用户登录功能
    
    参数:
        users: 用户列表
    
    返回值:
        bool: 登录是否成功
    """
    print("\n--- 用户登录 ---")
    username = input("请输入用户名：")
    
    # 查找用户
    found_user = None
    for user in users:
        if user["username"] == username:
            found_user = user
            break
    
    if found_user is None:
        print("用户名不存在！")
        return False
    
    # 尝试登录，最多3次机会
    attempts = 3
    while attempts > 0:
        print("\n剩余尝试次数：" + str(attempts))
        password = input("请输入密码：")
        
        if found_user["password"] == password:
            print("登录成功！")
            return True
        
        print("密码错误！")
        attempts = attempts - 1
    
    print("\n错误次数过多，账号已锁定！")
    return False
```

**阶段 6：最终整合与测试**
- **目标**：将所有功能整合在一起，确保程序完整运行。
- **要实现的函数**：检查所有函数是否都能正常工作，完善 `main()` 函数的逻辑。
- **逻辑分析**：这一阶段主要是调整程序的整体逻辑，比如登录成功后退出程序循环，菜单选择无效时提示重新输入。确保每个功能之间没有冲突。
- **测试重点**：运行程序，测试菜单的每个选项（登录、注册、退出），确保注册能保存新用户，登录能验证用户，退出能正常结束程序。
- **实现代码**：由于这一阶段主要是整合之前的函数，代码已经在前面各阶段中完成，以下是完整的 `main()` 函数，确保逻辑完整。

```python
def main():
    """
    主函数，程序入口
    """
    users = init_user_data()
    
    while True:
        choice = display_menu()
        if choice == "1":
            login_success = login_user(users)
            if login_success:
                break  # 登录成功后退出循环
        elif choice == "2":
            register_user(users)
        elif choice == "3":
            print("退出系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 程序入口，只有直接运行此文件时才会执行 main() 函数
if __name__ == "__main__":
    main()
```


### 5.3 最终代码整合与测试

```python
# 初始化用户数据
def init_user_data():
    """
    初始化用户数据，返回包含默认用户的列表
    """
    user_list = [
        {"username": "admin", "password": "123456"}
    ]
    return user_list

def display_menu():
    """
    显示主菜单，并返回用户的选择
    """
    print("\n=== 用户管理系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    choice = input("请选择操作：")
    return choice

def validate_username(username: str) -> bool:
    """
    验证用户名是否合法
    
    参数:
        username: 要验证的用户名
    
    返回值:
        bool: 用户名是否合法（长度是否大于等于4）
    """
    if len(username) >= 4:
        return True
    else:
        return False
    # 注释：这里可以用三元运算符简写为 return len(username) >= 4，但为了初学者理解，展开写成if-else形式

def validate_password(password: str) -> bool:
    """
    验证密码是否合法
    
    参数:
        password: 要验证的密码
    
    返回值:
        bool: 密码是否合法（长度是否大于等于6）
    """
    if len(password) >= 6:
        return True
    else:
        return False

def check_username_exists(users: list, username: str) -> bool:
    """
    检查用户名是否已存在
    
    参数:
        users: 用户列表
        username: 要检查的用户名
    
    返回值:
        bool: 用户名是否存在
    """
    for user in users:
        if user["username"] == username:
            return True
    return False

def register_user(users: list) -> bool:
    """
    用户注册功能
    
    参数:
        users: 用户列表
    
    返回值:
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
    new_user = {"username": username, "password": password1}
    users.append(new_user)
    print("\n注册成功！")
    total_users = len(users)
    print("当前系统用户数：" + str(total_users))
    return True

def login_user(users: list) -> bool:
    """
    用户登录功能
    
    参数:
        users: 用户列表
    
    返回值:
        bool: 登录是否成功
    """
    print("\n--- 用户登录 ---")
    username = input("请输入用户名：")
    
    # 查找用户
    found_user = None
    for user in users:
        if user["username"] == username:
            found_user = user
            break
    
    if found_user is None:
        print("用户名不存在！")
        return False
    
    # 尝试登录，最多3次机会
    attempts = 3
    while attempts > 0:
        print("\n剩余尝试次数：" + str(attempts))
        password = input("请输入密码：")
        
        if found_user["password"] == password:
            print("登录成功！")
            return True
        
        print("密码错误！")
        attempts = attempts - 1
    
    print("\n错误次数过多，账号已锁定！")
    return False

def main():
    """
    主函数，程序入口
    """
    users = init_user_data()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            login_success = login_user(users)
            if login_success:
                break
        elif choice == "2":
            register_user(users)
        elif choice == "3":
            print("退出系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 程序入口，只有直接运行此文件时才会执行 main() 函数
if __name__ == "__main__":
    main()
```

### 5.3 代码说明（优化版）
1. **函数化设计**：每个功能都封装成独立函数，职责单一，易于维护。
2. **数据验证**：通过 `validate_username` 和 `validate_password` 函数验证输入。
3. **异常处理**：本案例中未使用复杂异常处理，但在后续改进中可以加入 `try-except`。
4. **注释详细**：每个函数都有详细的文档字符串，说明参数和返回值。


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

### 5.5 改进建议（优化版）
1. **安全性改进**：可以添加密码加密功能。
2. **数据持久化**：将用户数据保存到文件，避免程序关闭后数据丢失。
3. **异常处理**：在用户输入时使用 `try-except` 捕获可能的输入错误。

### 5.6 练习建议
1. 尝试实现用户信息修改功能。
2. 添加更多的输入验证，比如检查用户名是否包含特殊字符。
3. 使用 `try-except` 处理可能的输入异常。

## 六、总结与学习建议
1. **逐步学习**：先掌握函数的基本语法和调用，再学习参数和返回值。
2. **多练习**：通过编写小函数（如计算器、问候语）巩固基础。
3. **代码规范**：养成写注释和使用有意义函数名的习惯。
4. **异常处理**：学习使用 `try-except` 让程序更健壮。
5. **程序入口**：理解 `if __name__ == "__main__":` 的作用，规范代码结构。