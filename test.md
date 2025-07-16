好的，我会根据你的要求，在“分阶段实现指南”中每个阶段的说明下方，直接嵌入该阶段需要实现的函数代码。这样初学者可以一边阅读逻辑分析，一边查看对应的代码，结合得更加紧密，方便理解和实践。以下是优化后的内容，重点在综合案例的“分阶段实现指南”部分，其他部分保持不变。

---

# Python 函数编程基础教程（优化版 - 含分阶段实现指南与代码结合）

## 一、函数基础
（内容同前文，略）

## 二、函数参数详解
（内容同前文，略）

## 三、基础练习（优化版）
（内容同前文，略）

## 四、进阶内容（优化版）
（内容同前文，略）

## 五、综合案例：函数版登录注册系统（优化版）

### 5.1 系统概述
本案例将之前的登录注册系统用函数式编程方式重新实现，主要功能包括：
1. 用户注册。
2. 用户登录（三次尝试机会）。
3. 数据验证。
4. 菜单系统。

### 5.2 额外知识点介绍：if __name__ == "__main__": 的作用
（内容同前文，略）

### 5.3 分阶段实现指南
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

#### 学习建议
1. **按阶段实现**：不要急于写完整代码，按照上述阶段一步步完成，每个阶段完成后都运行测试。
2. **理解逻辑**：在写每个函数之前，先想想这个函数的作用是什么，它需要哪些输入数据，会返回什么结果。
3. **调试技巧**：如果某个功能不工作，可以在代码中添加 `print()` 语句，打印变量值，检查逻辑是否正确。
4. **记录问题**：遇到不理解的地方或错误，记下来并尝试查找资料解决，这对学习非常有帮助。

通过这种分阶段的方式，你会发现即使是复杂的系统，也可以拆分成小任务，逐步完成，最终构建出完整的程序。接下来，我们将提供完整的代码实现，你可以参考它来对照自己的代码，或者在每个阶段完成后查看相应的函数实现。

### 5.4 代码实现（优化版）
（内容同前文，完整代码略）

### 5.5 代码说明（优化版）
（内容同前文，略）

### 5.6 改进建议（优化版）
（内容同前文，略）

### 5.7 练习建议
（内容同前文，略）

## 六、总结与学习建议
（内容同前文，略）

---

**优化总结**：
1. **代码与逻辑结合**：在“分阶段实现指南”中，每个阶段的说明下方直接嵌入该阶段需要实现的函数代码，方便初学者一边阅读逻辑分析，一边查看对应的代码实现，增强理解。
2. **逐步构建**：每个阶段的代码都是可运行的，初学者可以按照顺序逐步实现，并在每个阶段进行测试，确保理解和掌握。
3. **清晰指导**：每个阶段都包含目标、逻辑分析和测试重点，帮助初学者理清思路，知道下一步该做什么。

如果有其他需求或进一步优化建议，请随时告诉我！