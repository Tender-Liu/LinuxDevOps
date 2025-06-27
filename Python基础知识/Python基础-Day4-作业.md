## 题目 1：带菜单的登录系统

### 题目要求
编写一个程序，实现带菜单的登录系统。系统有两个默认用户，用户可以选择登录或退出，登录时需要验证用户名和密码。

### 详细解题步骤
1. **定义用户数据**
   ```python
   # 使用列表存储多个用户，每个用户是一个字典
   users = [
       {"username": "admin", "password": "123456"},  # 第一个用户
       {"username": "user1", "password": "abc123"}   # 第二个用户
   ]
   ```
   - 列表 `users` 可以存储多个用户信息
   - 每个用户信息用字典存储，包含用户名和密码
   - 字典的键是固定的："username" 和 "password"

2. **实现菜单显示**
   ```python
   # 显示菜单选项
   print("\n=== 登录系统 ===")
   print("1. 登录")
   print("2. 退出")
   ```
   - 使用 `print()` 函数显示菜单
   - `\n` 用于换行，使显示更美观
   - 每个选项前加数字，方便用户选择

3. **获取用户选择**
   ```python
   choice = input("请选择操作：")
   ```
   - `input()` 函数用于获取用户输入
   - 输入的内容存储在 `choice` 变量中

### 完整代码实现
```python
# 定义默认用户列表，使用字典存储用户信息
users = [
    {"username": "admin", "password": "123456"},  # 管理员用户
    {"username": "user1", "password": "abc123"}   # 普通用户
]

# 主循环，持续显示菜单直到用户选择退出
while True:
    # 显示系统菜单
    print("\n=== 登录系统 ===")
    print("1. 登录")
    print("2. 退出")
    
    # 获取用户选择
    choice = input("请选择操作：")
    
    # 处理用户选择
    if choice == "1":
        # 登录功能
        print("\n--- 登录 ---")
        username = input("请输入用户名：")  # 获取用户名
        password = input("请输入密码：")    # 获取密码
        
        # 验证用户信息
        login_success = False  # 登录状态标志
        for user in users:     # 遍历用户列表
            if user["username"] == username and user["password"] == password:
                login_success = True  # 找到匹配的用户名和密码
                break
        
        # 输出登录结果
        if login_success:
            print("登录成功！")
            break  # 登录成功后退出循环
        else:
            print("用户名或密码错误！")
    
    elif choice == "2":
        print("退出系统，再见！")
        break  # 用户选择退出时结束循环
    
    else:
        print("无效选择，请重新输入！")
```

## 题目 2：带验证的注册系统

### 题目要求
编写一个程序，实现带验证功能的注册系统。要求：
1. 用户名长度至少4个字符
2. 密码长度至少6个字符
3. 需要输入两次密码并验证是否一致

### 详细解题步骤
1. **初始化系统**
   ```python
   # 创建空列表存储用户
   users = []
   ```
   - 使用空列表，因为用户是在运行时注册的

2. **实现输入验证**
   ```python
   # 验证用户名长度
   while True:
       username = input("请输入用户名（至少4个字符）：")
       if len(username) < 4:
           print("用户名太短，请重新输入！")
       else:
           break
   ```
   - `len()` 函数获取字符串长度
   - `while True` 循环直到输入合法
   - 使用 `break` 退出验证循环

### 完整代码实现
```python
# 初始化用户列表
users = []

# 主循环，显示菜单并处理用户选择
while True:
    # 显示系统菜单
    print("\n=== 注册系统 ===")
    print("1. 注册新用户")
    print("2. 退出")
    
    # 获取用户选择
    choice = input("请选择操作：")
    
    if choice == "1":
        print("\n--- 新用户注册 ---")
        
        # 验证用户名长度
        while True:
            username = input("请输入用户名（至少4个字符）：")
            if len(username) < 4:
                print("用户名太短，请重新输入！")
            else:
                break
        
        # 验证密码
        while True:
            # 第一次输入密码并验证长度
            password1 = input("请输入密码（至少6个字符）：")
            if len(password1) < 6:
                print("密码太短，请重新输入！")
                continue
            
            # 第二次输入密码并验证一致性
            password2 = input("请再次输入密码：")
            if password1 != password2:
                print("两次密码不一致，请重新输入！")
            else:
                break
        
        # 保存新用户信息
        users.append({"username": username, "password": password1})
        print("\n注册成功！已保存以下信息：")
        print(f"用户名：{username}")
        print(f"当前注册用户数：{len(users)}")
    
    elif choice == "2":
        print("退出系统，再见！")
        break
    
    else:
        print("无效选择，请重新输入！")
```

## 题目 3：综合登录注册系统

### 题目要求
编写一个程序，实现以下功能：
1. 支持用户注册和登录
2. 登录时有3次尝试机会
3. 注册时验证用户名是否已存在
4. 使用while循环实现菜单系统

### 详细解题步骤
1. **系统初始化**
   ```python
   # 初始化带默认用户的系统
   users = [
       {"username": "admin", "password": "123456"}
   ]
   ```
   - 系统启动时有一个默认用户
   - 后续可以注册新用户

### 完整代码实现
```python
# 初始化用户列表，包含一个默认管理员账户
users = [
    {"username": "admin", "password": "123456"}
]

# 主循环，显示菜单并处理用户选择
while True:
    # 显示主菜单
    print("\n=== 用户管理系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    
    # 获取用户选择
    choice = input("请选择操作：")
    
    if choice == "1":
        # 登录功能
        print("\n--- 用户登录 ---")
        username = input("请输入用户名：")
        
        # 检查用户是否存在
        user_exists = False
        for user in users:
            if user["username"] == username:
                user_exists = True
                # 尝试登录，最多3次机会
                attempts = 3
                while attempts > 0:
                    print(f"\n剩余尝试次数：{attempts}")
                    password = input("请输入密码：")
                    
                    if user["password"] == password:
                        print("登录成功！")
                        break
                    else:
                        print("密码错误！")
                        attempts -= 1
                
                if attempts == 0:
                    print("\n错误次数过多，账号已锁定！")
                break
        
        if not user_exists:
            print("用户名不存在！")
    
    elif choice == "2":
        # 注册功能
        print("\n--- 新用户注册 ---")
        
        # 输入并验证用户名
        while True:
            username = input("请输入用户名（至少4个字符）：")
            
            # 检查用户名长度
            if len(username) < 4:
                print("用户名太短，请重新输入！")
                continue
            
            # 检查用户名是否已存在
            username_exists = False
            for user in users:
                if user["username"] == username:
                    username_exists = True
                    break
            
            if username_exists:
                print("用户名已存在，请重新输入！")
            else:
                break
        
        # 输入并验证密码
        while True:
            password1 = input("请输入密码（至少6个字符）：")
            if len(password1) < 6:
                print("密码太短，请重新输入！")
                continue
            
            password2 = input("请再次输入密码：")
            if password1 != password2:
                print("两次密码不一致，请重新输入！")
            else:
                break
        
        # 保存新用户
        users.append({"username": username, "password": password1})
        print("\n注册成功！")
        print(f"当前系统用户数：{len(users)}")
    
    elif choice == "3":
        print("退出系统，再见！")
        break
    
    else:
        print("无效选择，请重新输入！")
```

### 知识点解释
1. **变量作用域**
   - 在循环外定义的变量在循环内可以使用
   - 循环内可以修改外部变量的值

2. **字符串格式化**
   - f-string 使用 `f"...{变量}..."`
   - 可以直接在字符串中嵌入变量

3. **程序结构**
   - 主循环控制整个程序流程
   - 子功能使用单独的代码块
   - 使用注释说明代码功能

### 扩展练习建议
1. 尝试添加以下功能：
   - 密码强度检查（必须包含数字和字母）
   - 显示所有已注册用户（不显示密码）
   - 修改密码功能

2. 思考以下问题：
   - 如何持久化存储用户数据？
   - 如何加密存储密码？
   - 如何优化用户体验？