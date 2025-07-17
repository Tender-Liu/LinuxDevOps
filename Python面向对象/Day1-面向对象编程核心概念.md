# 第一天教案：Python 面向对象编程（OOP）核心概念

**课程目标**：通过详细的理论讲解和实践，帮助学员全面掌握 Python OOP 的核心概念（类、对象、封装、继承、多态），理解类的定义和使用方式，并通过丰富的代码实践完成基础类设计任务。

**学员基础**：已学习 Python 基础语法（如 `if`、`for`、`while` 等），但对 OOP 概念可能不熟悉或仅了解基础。

**时间安排**：总计 8 小时（5 小时讲课 + 3 小时练习）
- 讲课：9:00-15:00（每小时一个主题，包含理论讲解、代码演示和互动）
- 练习：15:00-18:00（基础练习 + 进阶练习，教师辅导答疑）

**教学方法**：
- 使用贴近日常生活的比喻（如工厂、汽车、学生）解释 OOP 概念，增加直观性和理解度。
- 每个知识点讲解后，安排一个教案练习（课堂内完成），帮助即时巩固。
- 每节课后布置一个作业练习（课后完成），加深理解。
- 代码示例、练习代码和作业代码均包含详细注释和语法解释，确保学员能看懂并学会编写，每个代码片段有独立文件名。
- 使用 Mermaid 结构图展示类关系和概念层次，辅助理解。

---

## 第一节：类与对象

### 教学目标
- 理解类和对象的概念，学会定义类和创建对象。
- 掌握 `__init__` 方法的作用，理解属性和方法的定义方式及其应用场景。

### 教学内容（详细理论讲解）
1. **什么是类和对象？**
   - **类（Class）**：类是面向对象编程中的一个基本概念，它是一种抽象的数据结构，用来描述一组具有相同属性和行为的对象的模板。换句话说，类就像一个“设计图”或“蓝图”，定义了对象的结构和功能，但本身并不包含具体的数据。比如，在现实生活中，“汽车”是一个类，它描述了汽车应该有哪些特征（如品牌、颜色）和行为（如启动、加速），但“汽车”这个概念本身不是一辆具体的车。
   - **对象（Object）**：对象是类的实例化结果，是类的具体实现。一个类可以创建多个对象，每个对象都有自己的数据，但共享类的结构和行为。继续用“汽车”举例，一辆具体的“丰田卡罗拉，红色，2020 年产”就是“汽车”类的一个对象。
   - **类和对象的关系**：类是抽象的，定义了规则和模板；对象是具体的，是类的实例。一个类可以创建多个对象，每个对象独立存在，拥有自己的属性值，但都遵循类的定义。类就像一个模具，对象是模具生产出来的具体产品。
   - **为什么需要类和对象？**：在编程中，我们经常需要处理一组相似的数据和操作，比如管理多个学生的信息。如果没有类，每次都要为每个学生单独写代码，非常繁琐且容易出错。类允许我们定义一次通用的结构，然后通过创建对象来复用这个结构，大大提高代码的可维护性和可扩展性。

2. **如何定义类和创建对象？**
   - 在 Python 中，使用 `class` 关键字来定义类，类名通常采用首字母大写的命名约定（如 `Student`、`Car`），以便与变量名区分。
   - 类中可以定义属性（用来存储数据）和方法（用来定义行为）。属性通常在 `__init__` 方法中初始化，方法是类中定义的函数。
   - `__init__` 方法是类的构造方法，在创建对象时自动调用，用于初始化对象的属性。它是 Python 中的一个特殊方法（也叫魔法方法），名称前后有双下划线。
   - 创建对象时，使用类名加括号的方式（如 `Dog("小黑")`），如果 `__init__` 方法有参数，则需要传入相应的值。
   - 创建对象后，可以通过对象名访问属性和方法，比如 `dog.name` 获取属性，`dog.bark()` 调用方法。

3. **类和对象的实际应用场景**
   - 类和对象适用于需要管理多个相似实体的场景。比如，在一个游戏中，可以定义一个 `Player` 类来表示玩家，包含属性如姓名、等级、血量，方法如攻击、移动。然后为每个玩家创建对象，分别管理他们的数据。
   - 类的另一个重要作用是代码复用和组织。通过类，可以将相关的功能和数据封装在一起，避免代码散乱，提高可读性。

4. **Mermaid 结构图**
   ```mermaid
   graph TD
       Class[类: 模板/蓝图] -->|创建| Object1[对象1: 具体实例]
       Class -->|创建| Object2[对象2: 具体实例]
       Class -->|定义| Attributes[属性: 数据]
       Class -->|定义| Methods[方法: 行为]
   ```

5. **形象对比（日常生活中）**
   - 类就像一个“蛋糕模具”，定义了蛋糕的形状、大小和样式，但它本身不是一个可以吃的蛋糕，只是一个工具。
   - 对象就像用这个模具做出来的“具体蛋糕”，每个蛋糕可以有不同的口味（如巧克力、草莓），但形状和样式都符合模具的定义。
   - 属性是蛋糕的“具体特征”，比如口味、重量，就像每个蛋糕的具体信息。
   - 方法是蛋糕的“用途或行为”，比如“切开”、“食用”，就像蛋糕可以执行的操作。
   - 总结来说，类是设计规则，对象是具体产品，类似模具和蛋糕的关系。

6. **代码示例（带详细注释和语法解释）**
   - **文件名**：`dog_class.py`
   ```python
   # 定义一个类，使用 'class' 关键字，类名通常首字母大写（这是 Python 的命名约定）
   class Dog:
       # __init__ 方法是类的构造方法，在创建对象时自动调用，用于初始化对象属性
       # self 是对象自身的引用，表示当前实例本身
       # name 是传入的参数，用于设置狗的名字
       def __init__(self, name):
           self.name = name  # 将传入的名字赋值给对象的 name 属性
                             # self.name 是对象的属性，name 是参数，二者通过赋值关联
       
       # 定义一个方法，表示狗的行为
       # 方法必须有 self 参数，表示调用该方法的对象本身
       def bark(self):
           print(self.name + " 在叫：汪汪！")  # 使用对象的 name 属性输出信息

   if __name__ == "__main__":
       # 创建对象：使用类名加括号，传入参数给 __init__ 方法
       dog1 = Dog("小黑")  # 创建一个名叫“小黑”的狗对象
       dog2 = Dog("小白")  # 创建另一个名叫“小白”的狗对象

       # 访问对象的属性
       print(dog1.name)  # 输出：小黑
       print(dog2.name)  # 输出：小白

       # 调用对象的方法
       dog1.bark()  # 输出：小黑 在叫：汪汪！
       dog2.bark()  # 输出：小白 在叫：汪汪！
   ```
   **语法解释**：
   - `class Dog:`：定义类，`Dog` 是类名，描述一类实体的规则。
   - `def __init__(self, name):`：构造方法，`self` 是固定参数，表示对象本身；`name` 是外部传入的数据。
   - `self.name = name`：将传入的 `name` 存为对象的属性。
   - `dog1 = Dog("小黑")`：创建对象，Python 自动调用 `__init__` 方法初始化对象。
   - `if __name__ == "__main__":`：Python 脚本的标准入口，只有直接运行该文件时才会执行其中的代码，类似程序的主函数。

### 教案练习（课堂内完成）
- **任务描述**：定义一个 `Server` 类，模拟服务器，包含 `hostname` 属性和 `start()` 方法，调用 `start()` 时输出“服务器 [hostname] 启动中...”。
- **预期时间**：10 分钟
- **指导**：教师现场指导，确保学员能定义类、创建对象并调用方法。
- **参考代码（带详细注释）**：
  - **文件名**：`server_class_exercise.py`
  ```python
  # 定义 Server 类，模拟服务器
  class Server:
      # 构造方法，初始化服务器的主机名
      # self 是对象本身，hostname 是传入的参数
      def __init__(self, hostname):
          self.hostname = hostname  # 将主机名存为对象属性
      
      # 定义 start 方法，模拟服务器启动行为
      def start(self):
          print(f"服务器 {self.hostname} 启动中...")  # 使用 f-string 格式化输出

  if __name__ == "__main__":
      # 创建一个服务器对象，传入主机名
      server = Server("web1.example.com")

      # 调用 start 方法，查看启动信息
      server.start()  # 输出：服务器 web1.example.com 启动中...
  ```
  **语法解释**：
  - `self.hostname = hostname`：将参数存为属性。
  - `f"服务器 {self.hostname} 启动中..."`：使用 f-string 格式化字符串，嵌入属性值。

### 作业练习（课后完成）
- **任务描述**：扩展 `Server` 类，增加更多属性和方法，模拟更真实的服务器管理场景。具体要求：
  1. 增加属性：`status`（表示服务器状态，如 "running" 或 "stopped"）、`cpu_usage`（表示 CPU 使用率，0-100 的整数）。
  2. 改进 `start()` 方法：如果服务器已经是 "running" 状态，则输出“服务器已启动，无需重复操作”；否则将状态设为 "running" 并输出启动信息，同时初始化 `cpu_usage` 为一个随机值（例如 10-50 之间）。
  3. 改进 `stop()` 方法：如果服务器已经是 "stopped" 状态，则输出“服务器已停止，无需重复操作”；否则将状态设为 "stopped" 并输出停止信息，同时将 `cpu_usage` 设为 0。
  4. 新增 `get_status()` 方法：输出服务器当前状态和 CPU 使用率。
  5. 创建两个服务器对象，分别测试启动、停止和状态查询功能。
- **目标**：熟悉类定义、对象创建，理解属性和方法的交互，掌握简单的条件判断逻辑。
- **预期时间**：30 分钟
- **参考代码（带详细注释）**：
  - **文件名**：`server_class_homework_advanced.py`
  ```python
  import random  # 导入 random 模块，用于模拟 CPU 使用率

  # 定义 Server 类，模拟服务器
  class Server:
      # 构造方法，初始化服务器的主机名、状态和 CPU 使用率
      def __init__(self, hostname):
          self.hostname = hostname  # 主机名
          self.status = "stopped"   # 初始状态为停止
          self.cpu_usage = 0        # 初始 CPU 使用率为 0
      
      # 定义 start 方法，模拟服务器启动行为，包含状态检查
      def start(self):
          if self.status == "running":
              print(f"服务器 {self.hostname} 已启动，无需重复操作")
          else:
              self.status = "running"
              self.cpu_usage = random.randint(10, 50)  # 模拟启动后 CPU 使用率
              print(f"服务器 {self.hostname} 启动中... 当前 CPU 使用率：{self.cpu_usage}%")
      
      # 定义 stop 方法，模拟服务器停止行为，包含状态检查
      def stop(self):
          if self.status == "stopped":
              print(f"服务器 {self.hostname} 已停止，无需重复操作")
          else:
              self.status = "stopped"
              self.cpu_usage = 0  # 停止后 CPU 使用率为 0
              print(f"服务器 {self.hostname} 停止中... 当前 CPU 使用率：{self.cpu_usage}%")
      
      # 定义 get_status 方法，查看服务器当前状态和 CPU 使用率
      def get_status(self):
          print(f"服务器 {self.hostname} 当前状态：{self.status}，CPU 使用率：{self.cpu_usage}%")

  if __name__ == "__main__":
      # 创建两个服务器对象，模拟不同主机
      server1 = Server("web1.example.com")
      server2 = Server("web2.example.com")

      # 测试 server1 的操作
      print("=== 测试 server1 ===")
      server1.get_status()  # 输出初始状态
      server1.start()       # 启动服务器
      server1.get_status()  # 查看启动后状态
      server1.start()       # 尝试重复启动
      server1.stop()        # 停止服务器
      server1.get_status()  # 查看停止后状态
      server1.stop()        # 尝试重复停止

      # 测试 server2 的操作
      print("\n=== 测试 server2 ===")
      server2.start()       # 启动服务器
      server2.get_status()  # 查看状态
      server2.stop()        # 停止服务器
      server2.get_status()  # 查看状态
  ```
  **语法解释**：
  - `self.status = "stopped"`：初始化服务器状态为停止，增加状态管理。
  - `if self.status == "running":`：条件判断，避免重复操作，增加逻辑性。
  - `random.randint(10, 50)`：使用 `random` 模块生成随机数，模拟 CPU 使用率。
  - `get_status()`：新增方法，方便查看对象当前状态，体现属性和方法的交互。

### 改进亮点
1. **增加属性**：引入 `status` 和 `cpu_usage`，让类更贴近现实服务器的特性。
2. **逻辑判断**：通过 `if-else` 语句，避免重复启动或停止，增加代码的健壮性。
3. **方法扩展**：新增 `get_status()` 方法，展示如何通过方法访问和展示对象属性。
4. **测试用例**：设计更全面的操作流程，覆盖不同场景，帮助理解对象状态变化。

---

## 第二节：封装

### 教学目标
- 理解封装的概念及其重要性，学会使用私有属性保护数据。
- 掌握 getter 和 setter 方法的实现方式，理解如何控制数据访问。

### 教学内容（详细理论讲解）
1. **什么是封装？**
   - 封装（Encapsulation）是面向对象编程的三大特性之一，指将数据（属性）和操作数据的方法（函数）捆绑在一起，并限制外部对内部数据的直接访问，从而保护数据的安全性和完整性。
   - 封装的核心思想是“隐藏实现细节，只暴露必要的接口”。通过封装，类的内部数据和逻辑对外部代码是不可见的，外部只能通过类提供的公共方法（接口）来与对象交互。这种机制可以防止外部代码随意修改对象的数据，避免数据被意外破坏。
   - 封装的好处：
     - **数据保护**：防止外部代码直接修改敏感数据，确保数据的一致性。
     - **代码模块化**：将数据和方法组织在一起，降低代码耦合度，便于维护。
     - **灵活性**：内部实现可以随意修改，只要接口不变，外部代码无需调整。
   - 在现实生活中，封装无处不在。比如，汽车的发动机是一个复杂的系统，司机不需要了解发动机的内部结构，只需要通过方向盘、油门和刹车这些“接口”来操作汽车。封装隐藏了复杂性，提供了简洁的交互方式。

2. **如何实现封装？**
   - 在 Python 中，通过在属性名前加双下划线（如 `__age`）来定义私有属性。私有属性无法被外部代码直接访问，必须通过类提供的方法来获取或修改。
   - 通常会提供两种方法来访问私有属性：
     - **getter 方法**：用于获取私有属性的值，类似“只读”访问。
     - **setter 方法**：用于设置私有属性的值，可以在设置时添加条件检查，确保数据合法性，类似“受控写入”。
   - Python 的私有属性并非完全不可访问（可以通过 `_类名__属性名` 绕过），但这种方式不被推荐。

3. **封装的实际应用场景**
   - 封装适用于任何需要保护数据的场景。比如，在一个银行系统类中，账户余额是一个敏感数据，不能允许外部直接修改，必须通过存款和取款方法来操作余额，确保余额不会变成负数。
   - 封装还可以用于隐藏复杂的实现逻辑。比如，一个类可能有复杂的内部计算过程，但外部只需要调用一个简单的方法即可获取结果，无需了解计算细节。

4. **Mermaid 结构图**
    ```mermaid
    graph TD
        Class["类: Person"] -->|"包含"| PrivateAttr["私有属性: __age"]
        Class -->|"提供"| Getter["getter 方法: get_age()"]
        Class -->|"提供"| Setter["setter 方法: set_age()"]
        External["外部代码"] -.->|"无法直接访问"| PrivateAttr
        External -->|"通过"| Getter
        External -->|"通过"| Setter
    ```

5. **形象对比（日常生活中）**
   - 私有属性就像家里的“保险箱”，里面存放了贵重物品，外部人无法直接打开，只能通过主人提供的“钥匙”或“密码”来访问。
   - getter 方法就像主人告诉你保险箱里有什么，但不给你钥匙，只能看不能拿。
   - setter 方法就像主人允许你存放东西，但必须符合条件（比如不能放危险物品），类似受控访问。
   - 封装的目的是保护重要数据，防止外部随意篡改，类似保险箱保护贵重物品。

6. **代码示例（带详细注释和语法解释）**
   - **文件名**：`person_encapsulation.py`
   ```python
   # 定义一个 Person 类，展示封装的概念
   class Person:
       # __init__ 方法初始化对象
       def __init__(self, name, age):
           self.name = name  # 公开属性，外部可直接访问
           self.__age = age  # 私有属性，外部无法直接访问
       
       # getter 方法，用于获取私有属性值
       def get_age(self):
           return self.__age  # 返回私有属性的值
       
       # setter 方法，用于设置私有属性值
       def set_age(self, age):
           if age > 0:  # 添加条件检查，确保年龄合理
               self.__age = age
           else:
               print("年龄必须大于 0！")  # 如果不合理，拒绝修改并提示

   if __name__ == "__main__":
       # 创建一个 Person 对象
       person = Person("小明", 25)

       # 访问公开属性
       print(person.name)  # 输出：小明

       # 无法直接访问私有属性，会报错
       # print(person.__age)  # 错误：AttributeError

       # 通过 getter 方法访问私有属性
       print(person.get_age())  # 输出：25

       # 通过 setter 方法修改私有属性
       person.set_age(30)
       print(person.get_age())  # 输出：30

       # 尝试设置不合理的值
       person.set_age(-5)  # 输出：年龄必须大于 0！
   ```
   **语法解释**：
   - `self.__age`：双下划线表示私有属性，外部无法直接访问，Python 通过名称改写实现伪私有。
   - `def get_age(self):`：getter 方法，返回私有属性值，类似只读访问。
   - `def set_age(self, age):`：setter 方法，允许有条件地修改属性值，类似受控写入。
   - `if age > 0:`：条件判断，学员应熟悉 `if` 语法，这里用于数据验证。

### 教案练习（课堂内完成）
- **任务描述**：定义一个 `User` 类，包含公开属性 `username` 和私有属性 `__password`，提供 `get_password()` 方法查看密码，和 `set_password(new_password)` 方法修改密码（要求新密码长度大于 6）。
- **预期时间**：10 分钟
- **指导**：教师提醒学员注意私有属性的定义和条件检查的逻辑。
- **参考代码（带详细注释）**：
  - **文件名**：`user_encapsulation_exercise.py`
  ```python
  # 定义 User 类，模拟用户账户
  class User:
      # 构造方法，初始化用户名和密码
      def __init__(self, username, password):
          self.username = username  # 公开属性，外部可直接访问
          self.__password = password  # 私有属性，外部无法直接访问
      
      # getter 方法，获取密码
      def get_password(self):
          return self.__password  # 返回密码值
      
      # setter 方法，设置新密码
      def set_password(self, new_password):
          if len(new_password) > 6:  # 检查新密码长度是否大于 6
              self.__password = new_password
              print("密码设置成功！")
          else:
              print("密码长度必须大于 6 个字符！")

  if __name__ == "__main__":
      # 创建一个 User 对象
      user = User("alice", "1234567")

      # 访问公开属性
      print(user.username)  # 输出：alice

      # 通过 getter 方法查看密码
      print(user.get_password())  # 输出：1234567

      # 通过 setter 方法修改密码
      user.set_password("newpass123")  # 输出：密码设置成功！
      print(user.get_password())  # 输出：newpass123

      # 尝试设置不合规的密码
      user.set_password("short")  # 输出：密码长度必须大于 6 个字符！
  ```
  **语法解释**：
  - `self.__password`：私有属性，保护敏感数据。
  - `if len(new_password) > 6:`：条件检查，确保数据合法性。

### 作业练习（课后完成）
- **任务描述**：扩展 `User` 类，添加一个方法 `check_password(input_password)`，检查输入的密码是否与私有属性 `__password` 一致，返回 True 或 False。
- **目标**：加深对封装和私有属性的理解，熟悉 getter 和 setter 的应用。
- **参考代码（带详细注释）**：
  - **文件名**：`user_encapsulation_homework.py`
  ```python
  # 定义 User 类，模拟用户账户
  class User:
      # 构造方法，初始化用户名和密码
      def __init__(self, username, password):
          self.username = username
          self.__password = password
      
      # getter 方法，获取密码
      def get_password(self):
          return self.__password
      
      # setter 方法，设置新密码
      def set_password(self, new_password):
          if len(new_password) > 6:
              self.__password = new_password
              print("密码设置成功！")
          else:
              print("密码长度必须大于 6 个字符！")
      
      # 检查输入密码是否正确
      def check_password(self, input_password):
          return input_password == self.__password  # 返回布尔值，判断是否匹配

  if __name__ == "__main__":
      # 创建一个 User 对象
      user = User("alice", "1234567")

      # 检查密码是否正确
      print(user.check_password("1234567"))  # 输出：True
      print(user.check_password("wrongpass"))  # 输出：False

      # 修改密码并再次检查
      user.set_password("newpass123")  # 输出：密码设置成功！
      print(user.check_password("newpass123"))  # 输出：True
  ```
  **语法解释**：
  - `def check_password(self, input_password):`：定义方法，比较输入值与私有属性值。
  - `return input_password == self.__password`：返回布尔值，判断是否相等。

---

## 第三节：继承

### 教学目标
- 理解继承的概念及其在代码复用中的作用，学会实现单继承。
- 掌握 `super()` 函数调用父类方法，理解父子类关系。
- 学习文件分离与模块化编程，掌握 `import` 语句的基本使用，理解代码组织的重要性。

### 教学内容（详细理论讲解）
1. **什么是继承？**
   - 继承（Inheritance）是面向对象编程的另一大特性，允许一个类（称为子类或派生类）继承另一个类（称为父类或基类）的属性和方法。子类可以直接使用父类的代码，从而实现代码复用，同时还可以在父类基础上进行扩展或修改。
   - 继承的核心思想是“复用和扩展”。通过继承，子类可以避免重复编写父类中已有的代码，只需关注自己的特有功能。这种机制特别适合描述现实世界中的“是一种（is-a）”关系，比如“猫是一种动物”，“汽车是一种交通工具”。
   - 继承的好处：
     - **代码复用**：子类可以直接使用父类的属性和方法，避免重复编码。
     - **层次结构**：通过继承，可以构建类之间的层次关系，反映现实世界的分类逻辑。
     - **易于扩展**：子类可以在继承的基础上添加新功能或修改父类行为，增强灵活性。
   - 继承的局限性：过度使用继承可能导致类层次过于复杂，增加维护难度，因此在设计时应谨慎使用。

2. **如何实现继承？**
   - 在 Python 中，通过在类定义时使用括号指定父类来实现继承，比如 `class Cat(Animal):` 表示 `Cat` 类继承自 `Animal` 类。
   - 子类会自动继承父类的所有属性和方法。如果子类需要扩展功能，可以定义自己的属性和方法；如果需要修改父类行为，可以重写（override）父类方法。
   - 使用 `super()` 函数可以调用父类的方法，特别在子类构造方法中调用父类构造方法以初始化父类属性时非常常见。

3. **继承的实际应用场景**
   - 继承适用于描述层次关系的场景。比如，在一个图形系统中，可以定义一个 `Shape` 基类，包含通用的面积计算方法，然后派生出 `Circle` 和 `Rectangle` 子类，分别实现具体的面积计算逻辑。
   - 继承还适用于框架设计。比如，Web 框架中的视图类可以作为基类，开发者继承基类并实现自己的业务逻辑。

4. **文件分离与模块化编程（初学者重点内容）**
   - **为什么要分离代码？**
     - 随着项目复杂性增加，将所有代码放在一个文件中会导致代码难以阅读和维护。将类或功能拆分到不同文件，可以提高代码的可读性和可维护性。
     - 文件分离是模块化编程的基础，模拟真实项目中代码的组织方式。
   - **什么是模块？**
     - 在 Python 中，每个 `.py` 文件可以看作一个模块（module）。模块就像一个工具箱，里面可以包含类、函数等代码。
   - **如何使用 `import`？**
     - 通过 `import` 语句，可以引入其他模块中的代码并使用。
     - 基本语法：
       - `import module_name`：引入整个模块。
       - `from module_name import class_name`：引入模块中的特定类或函数。
     - 示例：如果 `Animal` 类在 `animal.py` 文件中，可以在另一个文件中通过 `from animal import Animal` 引入。
   - **程序入口与类定义分离**：
     - 在实际开发中，通常将类定义和程序入口（测试代码或主程序）分开存放。类定义文件只包含类的实现，程序入口文件负责创建对象和测试功能。
     - 这样做可以让类定义文件更专注于逻辑实现，避免与测试代码混杂，提高代码复用性。
   - **实际应用场景**：
     - 在大型项目中，类、函数、配置等通常会按功能拆分到不同文件甚至不同目录，通过 `import` 组织代码。
     - 文件分离还可以避免命名冲突，提高代码复用性。
   - **注意事项**：
     - 确保相关文件在同一目录下，否则 `import` 会失败。
     - 运行时，选择包含程序入口（`if __name__ == "__main__":`）的文件，而不是类定义文件。

5. **Mermaid 结构图（继承关系与文件分离）**
   为了帮助学生直观理解继承关系和文件分离，我设计了以下 Mermaid 图，展示类之间的继承关系以及文件之间的导入关系，并突出程序入口的独立性。
    ```mermaid
    graph TD
        %% 文件分离与模块导入
        subgraph "动物相关文件"
            AnimalFile["animal.py<br>包含: Animal 类"]
            CatFile["cat.py<br>包含: Cat 类"]
            AnimalTestFile["animal_test.py<br>程序入口: 测试 Animal 和 Cat"]
            
            AnimalFile -->|"被导入 from animal import Animal"| CatFile
            AnimalFile -->|"被导入 from animal import Animal"| AnimalTestFile
            CatFile -->|"被导入 from cat import Cat"| AnimalTestFile
        end

        subgraph "车辆相关文件"
            VehicleFile["vehicle.py<br>包含: Vehicle 类"]
            CarFile["car.py<br>包含: Car 类"]
            TruckFile["truck.py<br>包含: Truck 类"]
            VehicleTestFile["vehicle_test.py<br>程序入口: 测试 Vehicle, Car, Truck"]
            
            VehicleFile -->|"被导入 from vehicle import Vehicle"| CarFile
            VehicleFile -->|"被导入 from vehicle import Vehicle"| TruckFile
            VehicleFile -->|"被导入 from vehicle import Vehicle"| VehicleTestFile
            CarFile -->|"被导入 from car import Car"| VehicleTestFile
            TruckFile -->|"被导入 from truck import Truck"| VehicleTestFile
        end

    ```
    
    ```mermaid
    graph TD
        %% 继承关系
        subgraph "动物继承体系"
            Animal["Animal 类<br>(父类)"]
            Cat["Cat 类<br>(子类)"]
            
            Animal -->|"继承"| Cat
        end

        subgraph "车辆继承体系"
            Vehicle["Vehicle 类<br>(父类)"]
            Car["Car 类<br>(子类)"]
            Truck["Truck 类<br>(子类)"]
            
            Vehicle -->|"继承"| Car
            Vehicle -->|"继承"| Truck
        end

    ```

   **图表解释**：
   - 上半部分展示文件之间的关系，箭头表示 `import` 导入的方向，例如 `animal_test.py` 通过 `from animal import Animal` 引入 `Animal` 类。
   - 特别标注了程序入口文件（如 `animal_test.py` 和 `vehicle_test.py`），用于测试类功能，与类定义文件分离。
   - 下半部分展示类之间的继承关系，箭头表示继承方向，例如 `Cat` 类继承自 `Animal` 类。

6. **形象对比（日常生活中）**
   - 继承：父类就像一个“基础食谱”，定义了做菜的基本步骤和通用配料，比如做汤的基本方法（加水、加盐）。子类就像基于基础食谱的“具体菜谱”，比如番茄鸡蛋汤，继承了基础步骤，但添加了特有配料（番茄、鸡蛋）和烹饪方式。
   - 文件分离：就像把不同类型的食谱分别放在不同的笔记本上（比如“基础食谱本”和“具体菜谱本”），需要做菜时从基础食谱本中“借用”通用步骤，保持条理清晰。
   - 程序入口分离：就像有一个单独的“烹饪计划本”，专门记录今天要做的菜和步骤，而不直接写在食谱本上，保持食谱本的纯粹性。
   - `import`：就像从另一个笔记本中“借用”内容，确保你可以直接使用别人的食谱，而不需要重新抄写。

7. **代码示例（带详细注释和语法解释，包含文件分离和程序入口分离）**
   - **文件名 1**：`animal.py`
     ```python
     # 定义父类 Animal，作为动物基类
     class Animal:
         def __init__(self, name):
             self.name = name  # 父类定义了 name 属性，存储动物名字
         
         def speak(self):
             print("动物在叫")  # 父类定义了一个通用方法，提供默认行为
     ```
   - **文件名 2**：`cat.py`
     ```python
     # 从 animal 模块引入 Animal 类
     from animal import Animal

     # 定义子类 Cat，继承自 Animal
     class Cat(Animal):
         # 子类可以重写父类方法，添加自己的行为
         def speak(self):
             print(self.name + " 在叫：喵喵！")  # 重写 speak 方法，体现猫的特有叫声
         
         # 子类可以定义自己的方法，扩展功能
         def purr(self):
             print(self.name + " 在咕噜咕噜")  # Cat 类特有方法
     ```
   - **文件名 3**：`animal_test.py` （程序入口文件）
     ```python
     # 从 animal 和 cat 模块引入类
     from animal import Animal
     from cat import Cat

     if __name__ == "__main__":
         # 创建父类对象，测试默认行为
         animal = Animal("通用动物")
         animal.speak()  # 输出：动物在叫

         # 创建子类对象，自动继承父类的属性和方法
         cat = Cat("小花")
         print(cat.name)  # 输出：小花
         cat.speak()      # 输出：小花 在叫：喵喵！
         cat.purr()       # 输出：小花 在咕噜咕噜
     ```
   **语法解释**：
   - `class Cat(Animal):`：表示 `Cat` 类继承自 `Animal` 类，子类会自动拥有父类的属性和方法。
   - `from animal import Animal`：从 `animal.py` 文件中引入 `Animal` 类。
   - `animal_test.py`：作为程序入口文件，专门用于测试类功能，与类定义分离。
   - 注意：运行时应执行 `animal_test.py`，而非 `animal.py` 或 `cat.py`。

### 教案练习（课堂内完成）
- **任务描述**：创建三个文件，`vehicle.py` 中定义父类 `Vehicle`，包含属性 `brand` 和方法 `move()`（输出“车辆在移动”）；`car.py` 中定义子类 `Car`，继承 `Vehicle`，重写 `move()` 方法（输出“汽车在公路上行驶”）；`vehicle_test.py` 作为程序入口，引入 `Vehicle` 和 `Car` 类并测试功能。
- **预期时间**：15 分钟
- **指导**：教师现场指导学生创建三个文件，确保文件在同一目录下，提醒学生运行 `vehicle_test.py` 而非类定义文件。
- **参考代码（带详细注释）**：
  - **文件名 1**：`vehicle.py`
    ```python
    # 定义父类 Vehicle，表示交通工具
    class Vehicle:
        # 构造方法，初始化品牌属性
        def __init__(self, brand):
            self.brand = brand  # 存储品牌信息
        
        # 定义 move 方法，描述车辆移动行为
        def move(self):
            print("车辆在移动")  # 通用行为
    ```
  - **文件名 2**：`car.py`
    ```python
    # 从 vehicle 模块引入 Vehicle 类
    from vehicle import Vehicle

    # 定义子类 Car，继承自 Vehicle
    class Car(Vehicle):
        # 重写 move 方法，描述汽车特有行为
        def move(self):
            print(f"{self.brand} 汽车在公路上行驶")  # 使用品牌属性，体现个性化
    ```
  - **文件名 3**：`vehicle_test.py` （程序入口文件）
    ```python
    # 从 vehicle 和 car 模块引入类
    from vehicle import Vehicle
    from car import Car

    if __name__ == "__main__":
        # 创建父类对象，测试默认行为
        vehicle = Vehicle("通用")
        vehicle.move()  # 输出：车辆在移动

        # 创建子类对象，测试继承和重写
        car = Car("丰田")
        print(car.brand)  # 输出：丰田
        car.move()        # 输出：丰田 汽车在公路上行驶
    ```
  **语法解释**：
  - `class Car(Vehicle):`：继承语法，`Car` 类继承 `Vehicle` 类。
  - `from vehicle import Vehicle`：从 `vehicle.py` 文件引入 `Vehicle` 类。
  - `vehicle_test.py`：作为程序入口，专门用于测试。


### 作业练习（课后完成，增加复杂度和代码量）
- **任务描述**：扩展上述代码，创建四个文件，分别为 `vehicle.py`（定义 `Vehicle` 类，增加更多属性和方法）、`car.py`（定义 `Car` 类）、`truck.py`（定义 `Truck` 类）、`vehicle_test.py`（程序入口，测试所有类）。具体要求如下：
  1. 在 `Vehicle` 类中，增加属性 `speed`（速度）和方法 `start_engine()`（输出“引擎启动”）、`stop_engine()`（输出“引擎关闭”）。
  2. 在 `Car` 类中，增加属性 `fuel_type`（燃料类型），重写 `move()` 方法（输出“汽车在公路上行驶，速度：X 公里/小时”），并添加方法 `honk()`（输出“汽车鸣笛：滴滴！”）。
  3. 在 `Truck` 类中，增加属性 `load_capacity`（载重能力），重写 `move()` 方法（输出“卡车在运输货物，速度：X 公里/小时”），并添加方法 `load_cargo()`（输出“卡车装载货物，最大载重：X 吨”）。
  4. 在 `vehicle_test.py` 中，创建每个类的对象，调用所有方法进行测试。
- **目标**：加深对继承、方法重写、文件分离与 `import` 的理解，同时通过增加代码量和功能复杂性提升实践能力。
- **预期时间**：40 分钟
- **参考代码（带详细注释）**：
  - **文件名 1**：`vehicle.py`
    ```python
    # 定义父类 Vehicle，表示交通工具
    class Vehicle:
        def __init__(self, brand, speed):
            self.brand = brand  # 品牌信息
            self.speed = speed  # 速度信息
        
        def move(self):
            print("车辆在移动")  # 通用移动行为
        
        def start_engine(self):
            print(f"{self.brand} 引擎启动")  # 启动引擎
        
        def stop_engine(self):
            print(f"{self.brand} 引擎关闭")  # 关闭引擎
    ```
  - **文件名 2**：`car.py`
    ```python
    # 从 vehicle 模块引入 Vehicle 类
    from vehicle import Vehicle

    # 定义子类 Car，继承自 Vehicle
    class Car(Vehicle):
        def __init__(self, brand, speed, fuel_type):
            super().__init__(brand, speed)  # 调用父类构造方法初始化 brand 和 speed
            self.fuel_type = fuel_type  # 汽车特有属性：燃料类型
        
        def move(self):
            print(f"{self.brand} 汽车在公路上行驶，速度：{self.speed} 公里/小时")  # 重写 move 方法
        
        def honk(self):
            print(f"{self.brand} 汽车鸣笛：滴滴！")  # 汽车特有方法
    ```
  - **文件名 3**：`truck.py`
    ```python
    # 从 vehicle 模块引入 Vehicle 类
    from vehicle import Vehicle

    # 定义子类 Truck，继承自 Vehicle
    class Truck(Vehicle):
        def __init__(self, brand, speed, load_capacity):
            super().__init__(brand, speed)  # 调用父类构造方法初始化 brand 和 speed
            self.load_capacity = load_capacity  # 卡车特有属性：载重能力
        
        def move(self):
            print(f"{self.brand} 卡车在运输货物，速度：{self.speed} 公里/小时")  # 重写 move 方法
        
        def load_cargo(self):
            print(f"{self.brand} 卡车装载货物，最大载重：{self.load_capacity} 吨")  # 卡车特有方法
    ```
  - **文件名 4**：`vehicle_test.py` （程序入口文件）
    ```python
    # 从各个模块引入类
    from vehicle import Vehicle
    from car import Car
    from truck import Truck

    if __name__ == "__main__":
        # 创建父类 Vehicle 对象，测试默认行为
        print("=== 测试 Vehicle 类 ===")
        vehicle = Vehicle("通用", 60)
        vehicle.start_engine()  # 输出：通用 引擎启动
        vehicle.move()          # 输出：车辆在移动
        vehicle.stop_engine()   # 输出：通用 引擎关闭

        # 创建子类 Car 对象，测试继承和特有功能
        print("\n=== 测试 Car 类 ===")
        car = Car("丰田", 120, "汽油")
        car.start_engine()      # 输出：丰田 引擎启动
        car.move()              # 输出：丰田 汽车在公路上行驶，速度：120 公里/小时
        car.honk()              # 输出：丰田 汽车鸣笛：滴滴！
        car.stop_engine()       # 输出：丰田 引擎关闭
        print(f"燃料类型：{car.fuel_type}")  # 输出：燃料类型：汽油

        # 创建子类 Truck 对象，测试继承和特有功能
        print("\n=== 测试 Truck 类 ===")
        truck = Truck("沃尔沃", 80, 10)
        truck.start_engine()    # 输出：沃尔沃 引擎启动
        truck.move()            # 输出：沃尔沃 卡车在运输货物，速度：80 公里/小时
        truck.load_cargo()      # 输出：沃尔沃 卡车装载货物，最大载重：10 吨
        truck.stop_engine()     # 输出：沃尔沃 引擎关闭
    ```
  **语法解释**：
  - `super().__init__(brand, speed)`：调用父类构造方法，确保父类属性正确初始化。
  - 每个子类增加特有属性和方法，体现继承的扩展性。
  - `vehicle_test.py`：作为程序入口，集中测试所有类的功能，代码量增加，逻辑更全面。

### 常见问题与解决方案（针对初学者）
- **文件路径问题**：确保所有文件在同一目录下。如果文件不在同一目录，`import` 会失败。解决方法：将文件放在同一文件夹中运行。
- **运行哪个文件？**：运行程序入口文件（如 `vehicle_test.py`），而非类定义文件（如 `vehicle.py`）。
- **导入错误**：如果出现 `ModuleNotFoundError`，检查文件名是否正确（区分大小写），以及文件是否在同一目录下。

---

## 第四节：多态

### 教学目标
- 理解多态的概念及其在提高代码灵活性中的作用，学会通过方法重写实现多态。
- 掌握多态在代码中的应用场景，理解动态绑定的机制。
- 学习文件分离与模块化编程，掌握 `import` 语句的使用，理解代码组织的实际意义。

### 教学内容（详细理论讲解）
1. **什么是多态？**
   - 多态（Polymorphism）是面向对象编程的第三大特性，指的是不同类的对象在调用相同方法时，可以表现出不同的行为。多态允许一个接口（方法名）有多种实现方式，根据调用对象的实际类型动态决定执行哪种实现。
   - 多态的核心思想是“同一接口，多种行为”。通过多态，代码可以以统一的方式处理不同类型的对象，而无需为每种类型编写单独的逻辑。这大大提高了代码的灵活性和可扩展性。
   - 多态的好处：
     - **代码简洁**：调用者只需关注通用接口，无需关心具体实现。
     - **易于扩展**：新增类时，只需实现通用接口，无需修改调用代码。
     - **动态性**：运行时根据对象类型决定行为，体现 Python 的动态特性。
   - 在现实生活中，多态也很常见。比如，“播放”按钮在不同设备上的行为不同：在音乐播放器上播放音乐，在视频播放器上播放视频，但用户只需点击同一个按钮。

2. **如何实现多态？**
   - 多态通常通过继承和方法重写实现。父类定义一个通用方法作为接口，子类重写该方法，提供自己的具体实现。
   - 在 Python 中，多态是动态的，运行时根据对象的实际类型决定调用哪个方法。这种机制称为“动态绑定”或“运行时多态”。
   - 常见实现方式是将不同类型的对象存储在列表中，统一调用接口方法，Python 会自动根据对象类型执行对应的实现。

3. **多态的实际应用场景**
   - 多态适用于需要统一处理多种类型的场景。比如，在一个绘图程序中，可以定义一个 `Shape` 基类，包含 `draw()` 方法，然后派生出 `Circle`、`Rectangle` 等子类，分别实现不同的绘制逻辑。调用时只需遍历所有形状对象，调用 `draw()` 方法即可。
   - 多态还适用于插件系统设计。比如，一个框架定义了通用接口，插件实现具体功能，框架通过多态调用插件方法，无需关心插件的具体实现。

4. **文件分离与模块化编程**
   - 从本节开始，我们将代码拆分为多个文件，类定义和程序入口（测试代码）分离，模拟实际开发中的代码组织方式。
   - 每个类可以放在独立的文件中，通过 `import` 引入到程序入口文件中进行测试。
   - 这样做可以提高代码的可读性和可维护性，避免所有代码混杂在一个文件中。

5. **Mermaid 结构图（多态关系与文件分离）**
   为了帮助学生直观理解多态和文件分离，我设计了以下 Mermaid 图，展示类之间的继承关系、方法重写以及文件之间的导入关系。
    ```mermaid
    graph TD
        %% 文件分离与模块导入
        ShapeFile["shape.py<br>包含: Shape 类"]
        CircleFile["circle.py<br>包含: Circle 类"]
        SquareFile["square.py<br>包含: Square 类"]
        ShapeTestFile["shape_test.py<br>程序入口: 测试所有类"]
        
        ShapeFile -->|"被导入 from shape import Shape"| CircleFile
        ShapeFile -->|"被导入 from shape import Shape"| SquareFile
        ShapeFile -->|"被导入 from shape import Shape"| ShapeTestFile
        CircleFile -->|"被导入 from circle import Circle"| ShapeTestFile
        SquareFile -->|"被导入 from square import Square"| ShapeTestFile
    ```

    ```mermaid
    graph TD
        %% 多态与继承关系
        Shape["Shape 类<br>(父类)"]
        Circle["Circle 类<br>(子类)"]
        Square["Square 类<br>(子类)"]
        Method["area()"]
        MethodCircle["area(): 计算圆的面积"]
        MethodSquare["area(): 计算正方形的面积"]
        
        Shape -->|"继承"| Circle
        Shape -->|"继承"| Square
        Shape -->|"定义接口"| Method
        Circle -->|"重写"| MethodCircle
        Square -->|"重写"| MethodSquare
    ```

   **图表解释**：
   - 上半部分展示文件之间的关系，箭头表示 `import` 导入的方向，例如 `shape_test.py` 通过 `from shape import Shape` 引入 `Shape` 类。
   - 下半部分展示类之间的继承关系和方法重写，体现多态的实现机制。

6. **形象对比（日常生活中）**
   - 父类方法就像一个“遥控器上的播放按钮”，定义了一个通用操作，描述了播放的基本功能。
   - 子类重写方法就像不同设备对“播放”按钮的具体响应，比如电视播放节目，音响播放音乐，虽然按钮相同，但实际行为不同。
   - 多态的优点是操作统一，用户只需按同一个按钮，不用管背后是哪种设备。
   - 总结来说，多态就像遥控器的通用按钮，同一个动作在不同设备上有不同效果，体现了灵活性和统一性。

7. **代码示例（带详细注释和语法解释，包含文件分离）**
   - **文件名 1**：`shape.py`
     ```python
     # 定义父类 Shape，表示形状，提供通用接口
     class Shape:
         def area(self):
             print("计算面积")  # 父类提供默认实现，作为通用接口
     ```
   - **文件名 2**：`circle.py`
     ```python
     # 从 shape 模块引入 Shape 类
     from shape import Shape

     # 定义子类 Circle，继承 Shape 并重写 area 方法
     class Circle(Shape):
         def area(self):
             print("计算圆的面积")  # Circle 特有的实现，体现多态
     ```
   - **文件名 3**：`square.py`
     ```python
     # 从 shape 模块引入 Shape 类
     from shape import Shape

     # 定义子类 Square，继承 Shape 并重写 area 方法
     class Square(Shape):
         def area(self):
             print("计算正方形的面积")  # Square 特有的实现，体现多态
     ```
   - **文件名 4**：`shape_test.py` （程序入口文件）
     ```python
     # 从各个模块引入类
     from shape import Shape
     from circle import Circle
     from square import Square

     if __name__ == "__main__":
         # 创建不同类的对象
         shape = Shape()
         circle = Circle()
         square = Square()

         # 使用列表存储不同对象，统一调用 area 方法
         shapes = [shape, circle, square]
         for s in shapes:
             s.area()  # 输出：计算面积\n计算圆的面积\n计算正方形的面积
     ```
   **语法解释**：
   - `class Circle(Shape):` 和 `class Square(Shape):`：两个子类都继承自 `Shape`，可以重写父类方法。
   - `def area(self):`：子类重写方法，覆盖父类实现，实现多态。
   - `for s in shapes:`：循环调用方法时，Python 根据对象实际类型执行对应的方法，体现动态多态。
   - `from shape import Shape`：通过 `import` 引入父类，体现文件分离。

### 教案练习（课堂内完成）
- **任务描述**：创建四个文件，定义一个父类 `Animal`（在 `animal.py` 中），包含方法 `speak()`（输出“动物在叫”），再定义子类 `Dog`（在 `dog.py` 中）和 `Cat`（在 `cat.py` 中），分别重写 `speak()` 方法（输出“狗在叫：汪汪！”和“猫在叫：喵喵！”），最后在 `animal_test.py` 中创建对象并统一调用 `speak()` 方法。
- **预期时间**：15 分钟
- **指导**：教师提醒学员注意方法重写和多态的效果，确保文件在同一目录下，运行程序入口文件。
- **参考代码（带详细注释）**：
  - **文件名 1**：`animal.py`
    ```python
    # 定义父类 Animal，表示动物，提供通用接口
    class Animal:
        def speak(self):
            print("动物在叫")  # 通用方法
    ```
  - **文件名 2**：`dog.py`
    ```python
    # 从 animal 模块引入 Animal 类
    from animal import Animal

    # 定义子类 Dog，继承 Animal
    class Dog(Animal):
        def speak(self):
            print("狗在叫：汪汪！")  # 重写方法，体现狗的特有行为
    ```
  - **文件名 3**：`cat.py`
    ```python
    # 从 animal 模块引入 Animal 类
    from animal import Animal

    # 定义子类 Cat，继承 Animal
    class Cat(Animal):
        def speak(self):
            print("猫在叫：喵喵！")  # 重写方法，体现猫的特有行为
    ```
  - **文件名 4**：`animal_test.py` （程序入口文件）
    ```python
    # 从各个模块引入类
    from animal import Animal
    from dog import Dog
    from cat import Cat

    if __name__ == "__main__":
        # 创建不同类型的动物对象
        animal = Animal()
        dog = Dog()
        cat = Cat()

        # 使用列表存储不同对象，统一调用 speak 方法
        animals = [animal, dog, cat]
        for a in animals:
            a.speak()  # 输出：动物在叫\n狗在叫：汪汪！\n猫在叫：喵喵！
    ```
  **语法解释**：
  - `def speak(self):`：子类重写父类方法，实现多态。
  - `for a in animals:`：使用循环统一调用方法，体现多态效果。
  - `from animal import Animal`：通过 `import` 引入父类，体现模块化。

### 作业练习（课后完成，增加属性和方法复杂性）
- **任务描述**：扩展上述代码，创建四个文件，分别为 `shape.py`（定义 `Shape` 类）、`circle.py`（定义 `Circle` 类）、`square.py`（定义 `Square` 类）、`shape_test.py`（程序入口，测试所有类）。具体要求如下：
  1. 为 `Shape` 类添加至少3个属性（如 `color`、`border_width`、`is_visible`）和方法 `area()`（输出基本信息和默认面积计算逻辑）。
  2. 为 `Circle` 类添加至少3个属性（如 `radius`、`center_x`、`center_y`）和重写 `area()` 方法（计算圆面积，使用圆周率 3.14，输出详细信息）。
  3. 为 `Square` 类添加至少3个属性（如 `side`、`top_left_x`、`top_left_y`）和重写 `area()` 方法（计算正方形面积，输出详细信息）。
  4. 每个类的 `area()` 方法逻辑控制在10行左右，包含属性引用和输出信息。
  5. 在 `shape_test.py` 中，创建每个类的对象，调用 `area()` 方法进行测试。
- **目标**：加深对多态的理解，结合属性和方法实现更实际的功能，同时通过文件分离和模块化编程提升代码组织能力。
- **预期时间**：40 分钟
- **参考代码（带详细注释）**：
  - **文件名 1**：`shape.py`
    ```python
    # 定义父类 Shape，表示形状，提供通用接口
    class Shape:
        def __init__(self, color, border_width, is_visible):
            self.color = color  # 形状颜色
            self.border_width = border_width  # 边框宽度
            self.is_visible = is_visible  # 是否可见
        
        def area(self):
            # 父类默认实现，输出基本信息
            print("=== 形状面积计算 ===")
            print(f"形状类型：通用形状")
            print(f"颜色：{self.color}")
            print(f"边框宽度：{self.border_width}")
            if self.is_visible:
                print("形状可见")
            else:
                print("形状不可见")
            print("面积计算：未定义具体形状，无法计算")
            print("==================")
    ```
  - **文件名 2**：`circle.py`
    ```python
    # 从 shape 模块引入 Shape 类
    from shape import Shape

    # 定义子类 Circle，继承 Shape
    class Circle(Shape):
        def __init__(self, color, border_width, is_visible, radius, center_x, center_y):
            super().__init__(color, border_width, is_visible)  # 调用父类构造方法
            self.radius = radius  # 圆半径
            self.center_x = center_x  # 圆心 x 坐标
            self.center_y = center_y  # 圆心 y 坐标
        
        def area(self):
            # 重写 area 方法，计算圆面积并输出详细信息
            print("=== 形状面积计算 ===")
            print(f"形状类型：圆形")
            print(f"颜色：{self.color}")
            print(f"边框宽度：{self.border_width}")
            print(f"圆心坐标：({self.center_x}, {self.center_y})")
            print(f"半径：{self.radius}")
            if self.is_visible:
                print("形状可见")
            result = 3.14 * self.radius * self.radius
            print(f"圆的面积是：{result:.2f}")
            print("==================")
    ```
  - **文件名 3**：`square.py`
    ```python
    # 从 shape 模块引入 Shape 类
    from shape import Shape

    # 定义子类 Square，继承 Shape
    class Square(Shape):
        def __init__(self, color, border_width, is_visible, side, top_left_x, top_left_y):
            super().__init__(color, border_width, is_visible)  # 调用父类构造方法
            self.side = side  # 正方形边长
            self.top_left_x = top_left_x  # 左上角 x 坐标
            self.top_left_y = top_left_y  # 左上角 y 坐标
        
        def area(self):
            # 重写 area 方法，计算正方形面积并输出详细信息
            print("=== 形状面积计算 ===")
            print(f"形状类型：正方形")
            print(f"颜色：{self.color}")
            print(f"边框宽度：{self.border_width}")
            print(f"左上角坐标：({self.top_left_x}, {self.top_left_y})")
            print(f"边长：{self.side}")
            if self.is_visible:
                print("形状可见")
            result = self.side * self.side
            print(f"正方形的面积是：{result}")
            print("==================")
    ```
  - **文件名 4**：`shape_test.py` （程序入口文件）
    ```python
    # 从各个模块引入类
    from shape import Shape
    from circle import Circle
    from square import Square

    if __name__ == "__main__":
        # 创建父类 Shape 对象，测试默认行为
        print("测试 Shape 类：")
        shape = Shape("灰色", 1, True)
        shape.area()

        # 创建子类 Circle 对象，测试多态
        print("\n测试 Circle 类：")
        circle = Circle("红色", 2, True, 5, 10, 10)
        circle.area()

        # 创建子类 Square 对象，测试多态
        print("\n测试 Square 类：")
        square = Square("蓝色", 3, True, 4, 0, 0)
        square.area()

        # 使用列表存储不同对象，统一调用 area 方法
        print("\n统一调用 area 方法（多态效果）：")
        shapes = [shape, circle, square]
        for s in shapes:
            s.area()
    ```
  **语法解释**：
  - `super().__init__(color, border_width, is_visible)`：调用父类构造方法，确保父类属性正确初始化。
  - 每个类至少有3个属性，`area()` 方法逻辑控制在10行左右，输出详细信息，体现多态的差异化行为。
  - `for s in shapes:`：统一调用方法，Python 动态根据对象类型执行对应的 `area()` 方法，体现多态。
  - 文件分离和 `import`：类定义和测试代码分开，符合模块化编程习惯。

### 常见问题与解决方案（针对初学者）
- **文件路径问题**：确保所有文件在同一目录下。如果文件不在同一目录，`import` 会失败。解决方法：将文件放在同一文件夹中运行。
- **运行哪个文件？**：运行程序入口文件（如 `shape_test.py`），而非类定义文件（如 `shape.py`）。
- **导入错误**：如果出现 `ModuleNotFoundError`，检查文件名是否正确（区分大小写），以及文件是否在同一目录下。

---

## 第五节：综合复习与案例分析

### 教学目标
- 复习当天内容，整合类、对象、封装、继承、多态的概念。
- 通过一个综合案例，学会设计简单的类结构。
- 掌握文件分离与模块化编程，强化代码组织的实践能力。

### 教学内容
1. **知识点复习**
   - 类与对象：模板与实例的关系，类是设计图，对象是具体实现。
   - 封装：保护数据，使用 getter 和 setter 方法控制访问。
   - 继承：代码复用，子类扩展父类功能。
   - 多态：相同接口，不同实现，动态根据对象类型执行方法。

2. **综合案例：学生管理系统**
   - 设计一个 `Student` 类，包含姓名和成绩属性（成绩为私有）。
   - 设计一个 `CollegeStudent` 类，继承 `Student`，添加专业属性。
   - 实现多态，通过方法计算不同类型学生的成绩等级。

3. **Mermaid 结构图（类关系与文件分离）**
   为了帮助学生直观理解类之间的关系和文件分离，我设计了以下 Mermaid 图，展示继承、多态以及文件之间的导入关系。

   ```mermaid
    graph TD
        %% 文件分离与模块导入关系
        StudentFile["student.py<br>包含: Student 类"]
        CollegeStudentFile["college_student.py<br>包含: CollegeStudent 类"]
        StudentTestFile["student_test.py<br>程序入口: 测试所有类"]

        StudentFile -->|"被导入 from student import Student"| CollegeStudentFile
        StudentFile -->|"被导入 from student import Student"| StudentTestFile
        CollegeStudentFile -->|"被导入 from college_student import CollegeStudent"| StudentTestFile
   ```

   ```mermaid
    graph TD
        %% 类与多态关系
        Student["Student 类"]
        Attr1["属性: name"]
        Attr2["私有属性: __grade"]
        Method1["get_grade()"]
        Method2["set_grade()"]
        Method3["calculate_level()"]

        CollegeStudent["CollegeStudent 类"]
        Attr3["属性: major"]
        Method3_Override["calculate_level()"]

        Student -->|"包含"| Attr1
        Student -->|"包含"| Attr2
        Student -->|"提供"| Method1
        Student -->|"提供"| Method2
        Student -->|"提供"| Method3

        CollegeStudent -->|"继承"| Student
        CollegeStudent -->|"新增"| Attr3
        CollegeStudent -->|"重写"| Method3_Override
   ```
   **图表解释**：
   - 上半部分展示文件之间的关系，箭头表示 `import` 导入的方向，例如 `student_test.py` 通过 `from student import Student` 引入 `Student` 类。
   - 下半部分展示类之间的继承关系和方法重写，体现多态的实现机制。

4. **形象对比（日常生活中）**
   - `Student` 类就像一个“基础学生档案模板”，定义了学生的基本信息和操作。
   - `CollegeStudent` 类就像一个“大学生档案模板”，继承了基础档案，添加了额外信息（如专业）。
   - 多态就像不同学校对成绩等级的评定标准不同，但都使用“评定”这个通用操作。

5. **代码示例（带详细注释和语法解释，包含文件分离）**
   - **文件名 1**：`student.py`
     ```python
     # 定义父类 Student
     class Student:
         def __init__(self, name, grade):
             self.name = name
             self.__grade = grade  # 私有属性，保护成绩数据
         
         def get_grade(self):  # getter 方法
             return self.__grade
         
         def set_grade(self, grade):  # setter 方法
             if 0 <= grade <= 100:
                 self.__grade = grade
             else:
                 print("成绩必须在 0-100 之间！")
         
         def calculate_level(self):  # 计算成绩等级的方法
             grade = self.__grade
             if grade >= 90:
                 return "优秀"
             elif grade >= 60:
                 return "及格"
             else:
                 return "不及格"
     ```
   - **文件名 2**：`college_student.py`
     ```python
     # 从 student 模块引入 Student 类
     from student import Student

     # 定义子类 CollegeStudent，继承 Student
     class CollegeStudent(Student):
         def __init__(self, name, grade, major):
             super().__init__(name, grade)  # 调用父类构造方法，初始化 name 和 grade
             self.major = major  # 新增专业属性
         
         def calculate_level(self):  # 重写方法，体现多态
             grade = self.get_grade()
             if grade >= 85:  # 大学生标准更严格
                 return "优秀"
             elif grade >= 70:
                 return "及格"
             else:
                 return "不及格"
     ```
   - **文件名 3**：`student_test.py` （程序入口文件）
     ```python
     # 从各个模块引入类
     from student import Student
     from college_student import CollegeStudent

     if __name__ == "__main__":
         # 创建不同类型的学生对象
         student1 = Student("小明", 75)
         student2 = CollegeStudent("小红", 75, "计算机")

         # 调用方法，查看成绩等级，体现多态
         print(student1.name + " 的等级：" + student1.calculate_level())  # 输出：小明 的等级：及格
         print(student2.name + " 的等级：" + student2.calculate_level())  # 输出：小红 的等级：及格
     ```
   **语法解释**：
   - `super().__init__(name, grade)`：调用父类的构造方法，确保父类属性被正确初始化。
   - `def calculate_level(self):`：子类重写父类方法，实现多态，标准不同但接口一致。
   - `if grade >= 85:`：条件判断，体现不同标准。
   - `from student import Student`：通过 `import` 引入父类，体现文件分离。

### 教案练习（课堂内完成）
- **任务描述**：修改 `Student` 类，添加一个方法 `show_info()`，输出学生姓名和成绩；为 `CollegeStudent` 类重写 `show_info()`，额外输出专业信息。
- **预期时间**：15 分钟
- **指导**：教师引导学员整合继承和多态知识，完成方法重写。
- **参考代码（带详细注释，包含文件分离）**：
  - **文件名 1**：`student.py` （更新）
    ```python
    # 定义父类 Student
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.__grade = grade  # 私有属性
        
        def get_grade(self):
            return self.__grade
        
        def set_grade(self, grade):
            if 0 <= grade <= 100:
                self.__grade = grade
            else:
                print("成绩必须在 0-100 之间！")
        
        def calculate_level(self):
            grade = self.__grade
            if grade >= 90:
                return "优秀"
            elif grade >= 60:
                return "及格"
            else:
                return "不及格"
        
        def show_info(self):  # 新增方法，显示学生信息
            print(f"学生姓名：{self.name}，成绩：{self.__grade}")
    ```
  - **文件名 2**：`college_student.py` （更新）
    ```python
    # 从 student 模块引入 Student 类
    from student import Student

    # 定义子类 CollegeStudent，继承 Student
    class CollegeStudent(Student):
        def __init__(self, name, grade, major):
            super().__init__(name, grade)
            self.major = major
        
        def calculate_level(self):
            grade = self.get_grade()
            if grade >= 85:
                return "优秀"
            elif grade >= 70:
                return "及格"
            else:
                return "不及格"
        
        def show_info(self):  # 重写方法，显示额外信息
            print(f"学生姓名：{self.name}，成绩：{self.get_grade()}，专业：{self.major}")
    ```
  - **文件名 3**：`student_exercise_test.py` （程序入口文件）
    ```python
    # 从各个模块引入类
    from student import Student
    from college_student import CollegeStudent

    if __name__ == "__main__":
        # 创建对象并调用方法
        student1 = Student("小明", 75)
        student2 = CollegeStudent("小红", 75, "计算机")
        student1.show_info()  # 输出：学生姓名：小明，成绩：75
        student2.show_info()  # 输出：学生姓名：小红，成绩：75，专业：计算机
    ```
  **语法解释**：
  - `def show_info(self):`：定义方法显示信息，子类重写方法添加额外内容。
  - `from student import Student`：通过 `import` 引入父类，体现模块化。

### 作业练习（课后完成）
- **任务描述**：扩展学生管理系统，添加一个 `HighSchoolStudent` 类，继承 `Student`，修改 `calculate_level()` 标准（90 以上为优秀，60 以上为及格），并创建多个不同类型的学生对象，统一调用 `show_info()` 和 `calculate_level()` 方法。
- **目标**：整合所有知识点，熟悉综合类设计。
- **参考代码（带详细注释，包含文件分离）**：
  - **文件名 1**：`student.py` （保持不变，如上）
  - **文件名 2**：`college_student.py` （保持不变，如上）
  - **文件名 3**：`high_school_student.py`
    ```python
    # 从 student 模块引入 Student 类
    from student import Student

    # 定义子类 HighSchoolStudent，继承 Student
    class HighSchoolStudent(Student):
        def __init__(self, name, grade, school):
            super().__init__(name, grade)
            self.school = school
        
        def calculate_level(self):
            grade = self.get_grade()
            if grade >= 90:
                return "优秀"
            elif grade >= 60:
                return "及格"
            else:
                return "不及格"
        
        def show_info(self):
            print(f"学生姓名：{self.name}，成绩：{self.get_grade()}，学校：{self.school}")
    ```
  - **文件名 4**：`student_homework_test.py` （程序入口文件）
    ```python
    # 从各个模块引入类
    from student import Student
    from college_student import CollegeStudent
    from high_school_student import HighSchoolStudent

    if __name__ == "__main__":
        # 创建不同类型的学生对象
        student1 = Student("小明", 75)
        student2 = CollegeStudent("小红", 75, "计算机")
        student3 = HighSchoolStudent("小刚", 75, "第一中学")

        # 统一调用方法
        students = [student1, student2, student3]
        for s in students:
            s.show_info()
            print(f"等级：{s.calculate_level()}\n")
    ```
  **语法解释**：
  - `class HighSchoolStudent(Student):`：新增子类，继承父类，体现代码复用。
  - `for s in students:`：统一调用方法，体现多态效果。

---

## 练习时间安排

### 基础练习
- **任务 1**：定义一个 `Car` 类，包含品牌和速度属性，实现 `accelerate()`（速度增加 10）和 `brake()`（速度减少 10）方法，速度不能为负数。
  - **文件名 1**：`car.py`
    ```python
    class Car:
        def __init__(self, brand, speed=0):
            self.brand = brand
            self.speed = speed
        
        def accelerate(self):
            self.speed += 10
            print(f"{self.brand} 加速，当前速度：{self.speed}")
        
        def brake(self):
            self.speed -= 10
            if self.speed < 0:
                self.speed = 0
            print(f"{self.brand} 刹车，当前速度：{self.speed}")
    ```
  - **文件名 2**：`car_test.py` （程序入口文件）
    ```python
    from car import Car

    if __name__ == "__main__":
        car = Car("丰田")
        car.accelerate()  # 输出：丰田 加速，当前速度：10
        car.accelerate()  # 输出：丰田 加速，当前速度：20
        car.brake()       # 输出：丰田 刹车，当前速度：10
        car.brake()       # 输出：丰田 刹车，当前速度：0
    ```
- **任务 2**：定义一个 `Employee` 类，使用封装实现私有薪资属性 `__salary`，提供 `get_salary()` 和 `set_salary(new_salary)` 方法（新薪资必须大于 0）。
  - **文件名 1**：`employee.py`
    ```python
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.__salary = salary
        
        def get_salary(self):
            return self.__salary
        
        def set_salary(self, new_salary):
            if new_salary > 0:
                self.__salary = new_salary
                print("薪资更新成功！")
            else:
                print("薪资必须大于 0！")
    ```
  - **文件名 2**：`employee_test.py` （程序入口文件）
    ```python
    from employee import Employee

    if __name__ == "__main__":
        emp = Employee("小明", 5000)
        print(emp.get_salary())  # 输出：5000
        emp.set_salary(6000)      # 输出：薪资更新成功！
        print(emp.get_salary())  # 输出：6000
        emp.set_salary(-100)      # 输出：薪资必须大于 0！
    ```
- **目标**：熟悉类定义、属性、方法和封装的使用。
- **指导**：教师巡回辅导，提供代码提示，确保学员完成任务。

### 进阶练习
- **任务**：设计一个 `Shape` 基类，包含 `area()` 方法（输出“计算面积”），派生出 `Circle` 和 `Rectangle` 子类，重写 `area()` 方法（输出“计算圆的面积”和“计算矩形的面积”），创建对象并统一调用 `area()` 方法。
  - **文件名 1**：`shape.py`
    ```python
    class Shape:
        def area(self):
            print("计算面积")
    ```
  - **文件名 2**：`circle.py`
    ```python
    from shape import Shape

    class Circle(Shape):
        def area(self):
            print("计算圆的面积")
    ```
  - **文件名 3**：`rectangle.py`
    ```python
    from shape import Shape

    class Rectangle(Shape):
        def area(self):
            print("计算矩形的面积")
    ```
  - **文件名 4**：`shape_advanced_test.py` （程序入口文件）
    ```python
    from shape import Shape
    from circle import Circle
    from rectangle import Rectangle

    if __name__ == "__main__":
        shapes = [Shape(), Circle(), Rectangle()]
        for s in shapes:
            s.area()  # 输出：计算面积\n计算圆的面积\n计算矩形的面积
    ```
- **目标**：通过继承和多态的实现，加深对核心概念的理解。
- **指导**：教师重点帮助学员理解多态效果，解答代码问题。

---

## 第一天总结与注意事项
- **学习成果**：学员应能理解并实现类的定义、对象创建、封装、继承和多态，完成基础类设计任务。
- **注意事项**：
  - 讲课时避免过多理论，注重代码演示和日常比喻，确保内容贴近学员经验。
  - 练习任务由易到难，教师及时答疑，避免学员因语法问题卡住。
  - 鼓励学员课后完成作业练习，教师第二天上课前检查并反馈。
  - 每个代码文件独立命名，学员需分别保存和运行，避免混淆。
- **课后延伸**：推荐学员阅读 Python 官方文档中关于类的部分，预习魔法方法和属性装饰器的基础概念。

---

### 整体优化说明
1. **文件分离**：所有代码均按照类定义和程序入口分离的方式组织，每个类放在独立文件中，通过 `import` 引入到测试文件中，符合实际开发习惯。
   - 学生管理系统：拆分为 `student.py`、`college_student.py`、`high_school_student.py` 及相应的测试文件。
   - 基础练习：`Car` 和 `Employee` 类拆分为独立文件及其测试文件。
   - 进阶练习：`Shape`、`Circle`、`Rectangle` 类拆分为独立文件及其测试文件。
2. **代码一致性**：所有代码文件保持统一的命名规则和注释风格，确保清晰易读。
3. **练习与作业**：通过模块化设计，增加学生对文件组织和导入的理解，同时保留原有逻辑，确保学习效果。
4. **Mermaid 图表**：增加了文件分离的部分，帮助学生直观理解模块化编程的结构。