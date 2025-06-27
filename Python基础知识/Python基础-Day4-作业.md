## 题目 1：带菜单的登录系统
### 题目要求
编写一个程序，实现带菜单的登录系统。系统有两个默认用户，用户可以选择登录或退出，登录时需要验证用户名和密码。

### 设计思路
1. 定义两个默认用户的信息
2. 使用while循环显示菜单
3. 根据用户选择执行相应操作
4. 验证登录信息并给出提示

### 代码实现
```python
# 定义默认用户
users = [
    {"username": "admin", "password": "123456"},
    {"username": "user1", "password": "abc123"}
]

# 主循环
while True:
    # 显示菜单
    print("\n=== 登录系统 ===")
    print("1. 登录")
    print("2. 退出")
    
    # 获取用户选择
    choice = input("请选择操作：")
    
    # 处理用户选择
    if choice == "1":
        # 登录功能
        print("\n--- 登录 ---")
        username = input("请输入用户名：")
        password = input("请输入密码：")
        
        # 验证用户信息
        login_success = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                login_success = True
                break
        
        # 输出结果
        if login_success:
            print("登录成功！")
            break
        else:
            print("用户名或密码错误！")
    
    elif choice == "2":
        print("退出系统，再见！")
        break
    
    else:
        print("无效选择，请重新输入！")
```

## 题目 2：带验证的注册系统
### 题目要求
编写一个程序，实现带验证功能的注册系统。要求：
1. 用户名长度至少4个字符
2. 密码长度至少6个字符
3. 需要输入两次密码并验证是否一致

### 设计思路
1. 使用while循环实现重复注册功能
2. 验证用户名和密码的长度
3. 验证两次密码输入是否一致
4. 根据不同情况给出提示

### 代码实现
```python
# 初始化用户列表
users = []

while True:
    print("\n=== 注册系统 ===")
    print("1. 注册新用户")
    print("2. 退出")
    
    choice = input("请选择操作：")
    
    if choice == "1":
        print("\n--- 新用户注册 ---")
        
        # 验证用户名
        while True:
            username = input("请输入用户名（至少4个字符）：")
            if len(username) < 4:
                print("用户名太短，请重新输入！")
            else:
                break
        
        # 验证密码
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
        
        # 保存用户信息
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

### 设计思路
1. 使用列表存储用户信息
2. 实现菜单系统
3. 分别实现登录和注册功能
4. 添加用户名查重功能
5. 实现登录次数限制

### 代码实现
```python
# 初始化用户列表
users = [
    {"username": "admin", "password": "123456"}
]

# 主循环
while True:
    # 显示主菜单
    print("\n=== 用户管理系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    
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
                # 尝试登录
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

### 学习提示
1. 第一题重点：
   - while循环的基本使用
   - 列表和字典的操作
   - for循环遍历列表

2. 第二题重点：
   - 嵌套while循环
   - 字符串长度判断
   - continue和break的使用

3. 第三题重点：
   - 复杂条件判断
   - 多层循环控制
   - 用户数据管理
   - 登录验证逻辑