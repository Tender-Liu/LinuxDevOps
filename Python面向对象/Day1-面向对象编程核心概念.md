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
- **任务描述**：扩展 `Server` 类，添加 `stop()` 方法，输出“服务器 [hostname] 停止中...”，并创建两个服务器对象，分别调用 `start()` 和 `stop()` 方法。
- **目标**：熟悉类定义和对象创建，理解一个类可以创建多个对象。
- **参考代码（带详细注释）**：
  - **文件名**：`server_class_homework.py`
  ```python
  # 定义 Server 类，模拟服务器
  class Server:
      # 构造方法，初始化服务器的主机名
      def __init__(self, hostname):
          self.hostname = hostname  # 将主机名存为对象属性
      
      # 定义 start 方法，模拟服务器启动行为
      def start(self):
          print(f"服务器 {self.hostname} 启动中...")
      
      # 定义 stop 方法，模拟服务器停止行为
      def stop(self):
          print(f"服务器 {self.hostname} 停止中...")

  if __name__ == "__main__":
      # 创建两个服务器对象，模拟不同主机
      server1 = Server("web1.example.com")
      server2 = Server("web2.example.com")

      # 调用方法，模拟服务器操作
      server1.start()  # 输出：服务器 web1.example.com 启动中...
      server1.stop()   # 输出：服务器 web1.example.com 停止中...
      server2.start()  # 输出：服务器 web2.example.com 启动中...
      server2.stop()   # 输出：服务器 web2.example.com 停止中...
  ```
  **语法解释**：
  - `server1 = Server("web1.example.com")`：创建对象，每个对象有独立的属性值。
  - 一个类创建多个对象时，每个对象的属性和方法调用是独立的，互不干扰。

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

4. **Mermaid 结构图**
   ```mermaid
   graph TD
        Parent["父类: Animal"] -->|"继承"| Child["子类: Cat"]
        Parent -->|"提供"| Attr1["属性: name"]
        Parent -->|"提供"| Method1["方法: speak()"]
        Child -->|"重用"| Attr1
        Child -->|"重写或扩展"| Method1
   ```

5. **形象对比（日常生活中）**
   - 父类就像一个“基础食谱”，定义了做菜的基本步骤和通用配料，比如做汤的基本方法（加水、加盐）。
   - 子类就像基于基础食谱的“具体菜谱”，比如番茄鸡蛋汤，继承了基础步骤，但添加了特有配料（番茄、鸡蛋）和烹饪方式。
   - 继承的目的是复用通用步骤，类似基础食谱避免重复写通用步骤。
   - `super()` 就像在具体菜谱中调用基础食谱的步骤，确保通用部分被执行。

6. **代码示例（带详细注释和语法解释）**
   - **文件名**：`animal_inheritance.py`
   ```python
   # 定义父类 Animal，作为动物基类
   class Animal:
       def __init__(self, name):
           self.name = name  # 父类定义了 name 属性，存储动物名字
       
       def speak(self):
           print("动物在叫")  # 父类定义了一个通用方法，提供默认行为

   # 定义子类 Cat，继承自 Animal
   # 语法：在类名后加括号，写上父类名
   class Cat(Animal):
       # 子类可以重写父类方法，添加自己的行为
       def speak(self):
           print(self.name + " 在叫：喵喵！")  # 重写 speak 方法，体现猫的特有叫声
       
       # 子类可以定义自己的方法，扩展功能
       def purr(self):
           print(self.name + " 在咕噜咕噜")  # Cat 类特有方法

   if __name__ == "__main__":
       # 创建子类对象，自动继承父类的属性和方法
       cat = Cat("小花")

       # 调用继承的属性
       print(cat.name)  # 输出：小花

       # 调用重写后的方法
       cat.speak()  # 输出：小花 在叫：喵喵！

       # 调用子类特有方法
       cat.purr()  # 输出：小花 在咕噜咕噜
   ```
   **语法解释**：
   - `class Cat(Animal):`：表示 `Cat` 类继承自 `Animal` 类，子类会自动拥有父类的属性和方法。
   - `def speak(self):`：子类可以重写父类方法，覆盖父类的实现。
   - 注意：如果子类没有重写方法，会直接使用父类的方法；如果需要调用父类方法，可以用 `super().speak()`。

### 教案练习（课堂内完成）
- **任务描述**：定义一个父类 `Vehicle`，包含属性 `brand` 和方法 `move()`（输出“车辆在移动”），再定义子类 `Car`，继承 `Vehicle`，重写 `move()` 方法（输出“汽车在公路上行驶”）。
- **预期时间**：10 分钟
- **指导**：教师提醒学员注意继承语法和方法重写的写法。
- **参考代码（带详细注释）**：
  - **文件名**：`vehicle_inheritance_exercise.py`
  ```python
  # 定义父类 Vehicle，表示交通工具
  class Vehicle:
      # 构造方法，初始化品牌属性
      def __init__(self, brand):
          self.brand = brand  # 存储品牌信息
      
      # 定义 move 方法，描述车辆移动行为
      def move(self):
          print("车辆在移动")  # 通用行为

  # 定义子类 Car，继承自 Vehicle
  class Car(Vehicle):
      # 重写 move 方法，描述汽车特有行为
      def move(self):
          print(f"{self.brand} 汽车在公路上行驶")  # 使用品牌属性，体现个性化

  if __name__ == "__main__":
      # 创建 Car 对象
      car = Car("丰田")

      # 调用属性和方法
      print(car.brand)  # 输出：丰田
      car.move()  # 输出：丰田 汽车在公路上行驶
  ```
  **语法解释**：
  - `class Car(Vehicle):`：继承语法，`Car` 类继承 `Vehicle` 类，自动拥有 `brand` 属性和 `move()` 方法。
  - `def move(self):`：重写父类方法，覆盖默认行为。

### 作业练习（课后完成）
- **任务描述**：扩展上述代码，添加一个子类 `Truck`，继承 `Vehicle`，重写 `move()` 方法（输出“卡车在运输货物”），并为每个类创建对象，调用 `move()` 方法。
- **目标**：加深对继承和方法重写的理解。
- **参考代码（带详细注释）**：
  - **文件名**：`vehicle_inheritance_homework.py`
  ```python
  # 定义父类 Vehicle，表示交通工具
  class Vehicle:
      def __init__(self, brand):
          self.brand = brand
      
      def move(self):
          print("车辆在移动")

  # 定义子类 Car，继承自 Vehicle
  class Car(Vehicle):
      def move(self):
          print(f"{self.brand} 汽车在公路上行驶")

  # 定义子类 Truck，继承自 Vehicle
  class Truck(Vehicle):
      def move(self):
          print(f"{self.brand} 卡车在运输货物")

  if __name__ == "__main__":
      # 创建不同类型的车辆对象
      vehicle = Vehicle("通用")
      car = Car("丰田")
      truck = Truck("沃尔沃")

      # 调用 move 方法，观察不同行为
      vehicle.move()  # 输出：车辆在移动
      car.move()      # 输出：丰田 汽车在公路上行驶
      truck.move()    # 输出：沃尔沃 卡车在运输货物
  ```
  **语法解释**：
  - 多个子类可以继承同一个父类，每个子类可以有不同的方法实现。
  - 方法重写允许子类自定义行为，体现继承的灵活性。

---

## 第四节：多态

### 教学目标
- 理解多态的概念及其在提高代码灵活性中的作用，学会通过方法重写实现多态。
- 掌握多态在代码中的应用场景，理解动态绑定的机制。

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

4. **Mermaid 结构图**
   ```mermaid
   graph TD
        Parent["父类: Animal"] -->|"继承"| Child1["子类: Dog"]
        Parent -->|"继承"| Child2["子类: Cat"]
        Parent -->|"定义接口"| Method["speak()"]
        Child1 -->|"重写"| MethodDog["speak(): 汪汪"]
        Child2 -->|"重写"| MethodCat["speak(): 喵喵"]
   ```

5. **形象对比（日常生活中）**
   - 父类方法就像一个“遥控器上的播放按钮”，定义了一个通用操作，描述了播放的基本功能。
   - 子类重写方法就像不同设备对“播放”按钮的具体响应，比如电视播放节目，音响播放音乐，虽然按钮相同，但实际行为不同。
   - 多态的优点是操作统一，用户只需按同一个按钮，不用管背后是哪种设备。
   - 总结来说，多态就像遥控器的通用按钮，同一个动作在不同设备上有不同效果，体现了灵活性和统一性。

6. **代码示例（带详细注释和语法解释）**
   - **文件名**：`animal_polymorphism.py`
   ```python
   # 定义父类 Animal，提供通用接口
   class Animal:
       def speak(self):
           print("动物在叫")  # 父类提供默认实现，类似通用命令行为

   # 定义子类 Dog，继承 Animal 并重写 speak 方法
   class Dog(Animal):
       def speak(self):
           print("狗在叫：汪汪！")  # Dog 特有的叫声

   # 定义子类 Cat，继承 Animal 并重写 speak 方法
   class Cat(Animal):
       def speak(self):
           print("猫在叫：喵喵！")  # Cat 特有的叫声

   if __name__ == "__main__":
       # 创建不同类的对象
       dog = Dog()
       cat = Cat()

       # 使用列表存储不同对象，统一调用 speak 方法
       animals = [dog, cat]
       for animal in animals:
           animal.speak()  # 输出：狗在叫：汪汪！\n猫在叫：喵喵！
   ```
   **语法解释**：
   - `class Dog(Animal):` 和 `class Cat(Animal):`：两个子类都继承自 `Animal`，可以重写父类方法。
   - `def speak(self):`：子类重写方法，覆盖父类实现，实现多态。
   - `for animal in animals:`：循环调用方法时，Python 根据对象实际类型执行对应的方法，体现动态多态，学员应熟悉 `for` 循环语法。

### 教案练习（课堂内完成）
- **任务描述**：定义一个父类 `Shape`，包含方法 `area()`（输出“计算面积”），再定义子类 `Circle` 和 `Square`，分别重写 `area()` 方法（输出“计算圆的面积”和“计算正方形的面积”），创建对象并统一调用 `area()` 方法。
- **预期时间**：10 分钟
- **指导**：教师提醒学员注意方法重写和多态的效果。
- **参考代码（带详细注释）**：
  - **文件名**：`shape_polymorphism_exercise.py`
  ```python
  # 定义父类 Shape，表示形状
  class Shape:
      def area(self):
          print("计算面积")  # 通用方法

  # 定义子类 Circle，继承 Shape
  class Circle(Shape):
      def area(self):
          print("计算圆的面积")  # 重写方法，体现圆的特有行为

  # 定义子类 Square，继承 Shape
  class Square(Shape):
      def area(self):
          print("计算正方形的面积")  # 重写方法，体现正方形的特有行为

  if __name__ == "__main__":
      # 创建不同类型的形状对象
      shape = Shape()
      circle = Circle()
      square = Square()

      # 使用列表存储不同对象，统一调用 area 方法
      shapes = [shape, circle, square]
      for s in shapes:
          s.area()  # 输出：计算面积\n计算圆的面积\n计算正方形的面积
  ```
  **语法解释**：
  - `def area(self):`：子类重写父类方法，实现多态。
  - `for s in shapes:`：使用循环统一调用方法，体现多态效果。

### 作业练习（课后完成）
- **任务描述**：扩展上述代码，为 `Circle` 和 `Square` 添加属性（如半径、边长），并在 `area()` 方法中输出具体的面积值（可使用固定值，如圆周率取 3.14）。
- **目标**：加深对多态的理解，结合属性和方法实现更实际的功能。
- **参考代码（带详细注释）**：
  - **文件名**：`shape_polymorphism_homework.py`
  ```python
  # 定义父类 Shape，表示形状
  class Shape:
      def area(self):
          print("计算面积")

  # 定义子类 Circle，继承 Shape
  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius
      
      def area(self):
          result = 3.14 * self.radius * self.radius
          print(f"圆的面积是：{result}")

  # 定义子类 Square，继承 Shape
  class Square(Shape):
      def __init__(self, side):
          self.side = side
      
      def area(self):
          result = self.side * self.side
          print(f"正方形的面积是：{result}")

  if __name__ == "__main__":
      # 创建不同类型的形状对象
      circle = Circle(5)
      square = Square(4)

      # 使用列表存储不同对象，统一调用 area 方法
      shapes = [circle, square]
      for s in shapes:
          s.area()  # 输出：圆的面积是：78.5\n正方形的面积是：16
  ```
  **语法解释**：
  - `self.radius` 和 `self.side`：属性存储形状的具体参数。
  - `3.14 * self.radius * self.radius`：计算面积，输出具体值，体现多态。

---

## 第五节：综合复习与案例分析

### 教学目标
- 复习当天内容，整合类、对象、封装、继承、多态的概念。
- 通过一个综合案例，学会设计简单的类结构。

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

3. **Mermaid 结构图**
   ```mermaid
   graph TD
        Student["Student 类"] -->|"包含"| Attr1["属性: name"]
        Student -->|"包含"| Attr2["私有属性: __grade"]
        Student -->|"提供"| Method1["get_grade()"]
        Student -->|"提供"| Method2["set_grade()"]
        Student -->|"提供"| Method3["calculate_level()"]
        CollegeStudent["CollegeStudent 类"] -->|"继承"| Student
        CollegeStudent -->|"新增"| Attr3["属性: major"]
        CollegeStudent -->|"重写"| Method3["calculate_level()"]
   ```

4. **形象对比（日常生活中）**
   - `Student` 类就像一个“基础学生档案模板”，定义了学生的基本信息和操作。
   - `CollegeStudent` 类就像一个“大学生档案模板”，继承了基础档案，添加了额外信息（如专业）。
   - 多态就像不同学校对成绩等级的评定标准不同，但都使用“评定”这个通用操作。

5. **代码示例（带详细注释和语法解释）**
   - **文件名**：`student_management.py`
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

### 教案练习（课堂内完成）
- **任务描述**：修改 `Student` 类，添加一个方法 `show_info()`，输出学生姓名和成绩；为 `CollegeStudent` 类重写 `show_info()`，额外输出专业信息。
- **预期时间**：15 分钟
- **指导**：教师引导学员整合继承和多态知识，完成方法重写。
- **参考代码（带详细注释）**：
  - **文件名**：`student_management_exercise.py`
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

  if __name__ == "__main__":
      # 创建对象并调用方法
      student1 = Student("小明", 75)
      student2 = CollegeStudent("小红", 75, "计算机")
      student1.show_info()  # 输出：学生姓名：小明，成绩：75
      student2.show_info()  # 输出：学生姓名：小红，成绩：75，专业：计算机
  ```
  **语法解释**：
  - `def show_info(self):`：定义方法显示信息，子类重写方法添加额外内容。

### 作业练习（课后完成）
- **任务描述**：扩展学生管理系统，添加一个 `HighSchoolStudent` 类，继承 `Student`，修改 `calculate_level()` 标准（90 以上为优秀，60 以上为及格），并创建多个不同类型的学生对象，统一调用 `show_info()` 和 `calculate_level()` 方法。
- **目标**：整合所有知识点，熟悉综合类设计。
- **参考代码（带详细注释）**：
  - **文件名**：`student_management_homework.py`
  ```python
  # 定义父类 Student
  class Student:
      def __init__(self, name, grade):
          self.name = name
          self.__grade = grade
      
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
      
      def show_info(self):
          print(f"学生姓名：{self.name}，成绩：{self.__grade}")

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
      
      def show_info(self):
          print(f"学生姓名：{self.name}，成绩：{self.get_grade()}，专业：{self.major}")

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
  - **文件名**：`car_basic_exercise.py`
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

  if __name__ == "__main__":
      car = Car("丰田")
      car.accelerate()  # 输出：丰田 加速，当前速度：10
      car.accelerate()  # 输出：丰田 加速，当前速度：20
      car.brake()       # 输出：丰田 刹车，当前速度：10
      car.brake()       # 输出：丰田 刹车，当前速度：0
  ```
- **任务 2**：定义一个 `Employee` 类，使用封装实现私有薪资属性 `__salary`，提供 `get_salary()` 和 `set_salary(new_salary)` 方法（新薪资必须大于 0）。
  - **文件名**：`employee_basic_exercise.py`
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
  - **文件名**：`shape_advanced_exercise.py`
  ```python
  class Shape:
      def area(self):
          print("计算面积")

  class Circle(Shape):
      def area(self):
          print("计算圆的面积")

  class Rectangle(Shape):
      def area(self):
          print("计算矩形的面积")

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

**总结**：
这份第一天教案围绕 Python OOP 核心概念（类与对象、封装、继承、多态）展开，通过日常生活的比喻和 Mermaid 结构图帮助学员理解抽象概念。每个知识点包含详细理论、代码示例（带注释和语法解释）、教案练习和作业练习，确保学员能边学边练，逐步掌握内容。所有代码均有独立文件名和 `if __name__ == "__main__":` 入口，方便管理和运行。如果有其他需求（如调整内容或增加特定练习），请告诉我，我会进一步完善！非常抱歉之前的遗漏，希望这次完整的内容能满足你的需求。