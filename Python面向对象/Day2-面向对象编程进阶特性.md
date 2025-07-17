# 第二天教案：Python 面向对象编程（OOP）进阶与应用

**课程目标**：在第一天基础（类与对象、封装、继承、多态）之上，深入学习 Python OOP 的进阶特性，完善知识体系，并通过理论讲解和实践环节帮助学员将知识转化为实际应用能力。

**学员基础**：已完成第一天课程，熟悉类与对象、封装、继承、多态的基本概念和实现。

**教学方法**：
- 延续第一天的日常比喻方式（如工厂、汽车、学生），解释进阶概念，确保直观易懂。
- 每个知识点讲解后，安排一个教案练习（课堂内完成），帮助即时巩固。
- 每节课后布置一个作业练习（课后完成），加深理解。
- 代码示例、练习代码和作业代码均包含详细注释、语法解释和独立文件名，确保清晰规范，均使用 `if __name__ == "__main__":` 作为入口。
- 使用 Mermaid 结构图展示类关系和设计层次，辅助理解。
- 注重与第一天内容的衔接，复习相关基础知识。

---

## 课程整体介绍：Python 面向对象编程（OOP）进阶特性（9:00-9:10）

### 教学目标
- 让学员了解第二天的学习内容和目标，建立整体认知。
- 复习第一天基础知识，确保学习连贯性。

### 教学内容
1. **第二天的学习目标**
   - 深入掌握 Python OOP 的进阶特性，包括魔法方法、属性装饰器、类方法、静态方法、抽象类与接口。
   - 通过综合案例（图书管理系统），整合知识点，培养类设计和实际应用能力。
   - 关注代码规范和设计原则，为后续开发打下基础。

2. **第二天的内容安排**
   - 上午：魔法方法与特殊属性、属性装饰器、类方法与静态方法。
   - 下午：抽象类与接口、OOP 设计原则与综合案例。
   - 实践环节：基础练习 + 综合项目。

3. **第一天知识复习（简要回顾）**
   - 类与对象：类是模板，对象是实例，类定义属性和方法。
   - 封装：通过私有属性（如 `self.__name`）隐藏数据，使用 getter/setter 控制访问。
   - 继承：子类继承父类属性和方法，支持代码复用。
   - 多态：子类重写父类方法，实现不同行为。
   - 提问互动：请学员简要回忆一个第一天的例子（如学生类），确保基础扎实。

4. **学习方法与注意事项**
   - 每个主题结合日常比喻和代码演示，确保易于理解。
   - 课堂内完成小练习，课后完成作业，实践是关键。
   - 遇到问题随时提问，综合项目环节教师会重点辅导。

---

## 第一节：魔法方法与特殊属性（Magic Methods & Special Attributes）

### 教学目标
- 理解魔法方法（Magic Methods）的概念和常用方法，学会自定义对象行为。
- 掌握特殊属性的基本作用，了解如何访问类和对象的元信息。

### 教学内容（详细理论讲解）
1. **什么是魔法方法？**
   - 魔法方法是 Python 中以双下划线开头和结尾的特殊方法（如 `__init__`、`__str__`），用于定义对象在特定场景下的行为，比如初始化、字符串表示等。
   - 魔法方法的核心思想是“定制对象行为”。通过重写魔法方法，可以让对象支持特定的操作，比如让对象可以像字符串一样打印。
   - 常见魔法方法（本节重点）：
     - `__init__(self, ...)`：构造方法，用于初始化对象（第一天已学，复习）。
     - `__str__(self)`：返回对象的字符串表示，用于 `print()` 时显示。
     - `__repr__(self)`：返回对象的官方字符串表示，通常用于调试。
     - `__len__(self)`：定义对象长度，支持 `len()` 函数。
   - 魔法方法的好处：增强对象的功能，使其更贴近内置类型的使用方式，提高代码可读性和灵活性。

2. **什么是特殊属性？**
   - 特殊属性是 Python 中以双下划线开头和结尾的属性（如 `__name__`、`__dict__`），用于访问类或对象的元信息。
   - 常见特殊属性（简要介绍）：
     - `__dict__`：对象或类的属性字典，包含所有属性和方法。
     - `__name__`：类或模块的名称。
   - 特殊属性的作用：便于调试和了解对象或类的内部结构。

3. **魔法方法与特殊属性的实际应用场景**
   - 魔法方法适用于需要自定义对象行为的场景。比如，在一个书籍类中，可以通过 `__str__` 自定义打印格式，显示标题和作者。
   - 特殊属性适用于调试场景，比如通过 `__dict__` 查看对象的所有属性。

4. **Mermaid 结构图**
   ```mermaid
   graph TD
       Class[类: Book] -->|定义| MagicMethod1[__init__]
       Class -->|定义| MagicMethod2[__str__]
       Class -->|定义| MagicMethod3[__repr__]
       Class -->|定义| MagicMethod4[__len__]
       Class -->|包含| SpecialAttr1[__dict__]
       Class -->|包含| SpecialAttr2[__name__]
   ```

5. **形象对比（日常生活中）**
   - 魔法方法就像“家电的智能功能”，比如电视机的“开机”行为（类似 `__init__`）、“显示信息”行为（类似 `__str__`），通过定制这些行为，家电可以按照我们的需求工作。
   - 特殊属性就像家电的“说明书”或“标签”，记录了设备的基本信息（如型号），方便我们了解设备状态。
   - 总结来说，魔法方法是定制功能，特殊属性是查看信息，类似家电的操作和说明。

6. **代码示例（带详细注释和语法解释）**
   - **文件名**：`book_magic_methods.py`
   ```python
   # 定义一个 Book 类，展示魔法方法和特殊属性
   class Book:
       def __init__(self, title, pages):
           self.title = title  # 书籍标题
           self.pages = pages  # 书籍页数
       
       def __str__(self):  # 自定义字符串表示，print 时调用
           return f"书籍：{self.title}，页数：{self.pages}"
       
       def __repr__(self):  # 自定义官方表示，调试时调用
           return f"Book(title='{self.title}', pages={self.pages})"
       
       def __len__(self):  # 自定义长度，返回页数
           return self.pages

   if __name__ == "__main__":
       # 创建书籍对象
       book = Book("Python 编程", 300)

       # 使用 __str__ 方法，打印对象
       print(book)  # 输出：书籍：Python 编程，页数：300

       # 使用 __repr__ 方法，调试表示
       print(repr(book))  # 输出：Book(title='Python 编程', pages=300)

       # 使用 __len__ 方法，获取长度
       print(len(book))  # 输出：300

       # 访问特殊属性，查看对象信息
       print(book.__dict__)  # 输出：{'title': 'Python 编程', 'pages': 300}
       print(book.__class__.__name__)  # 输出：Book
   ```
   **语法解释**：
   - `__str__(self)`：返回用户友好的字符串，`print()` 时调用。
   - `__repr__(self)`：返回开发者友好的字符串，常用于调试。
   - `__len__(self)`：定义 `len()` 函数的行为，返回页数。
   - `__dict__`：特殊属性，返回属性字典，显示对象的所有属性。

### 教案练习（课堂内完成）
- **任务描述**：定义一个 `Student` 类，包含姓名和年龄属性，重写 `__str__` 方法输出学生信息（如“学生：姓名，年龄：年龄”），并查看对象的 `__dict__` 属性。
- **预期时间**：10 分钟
- **指导**：教师指导学员实现魔法方法，理解特殊属性的作用。
- **参考代码（带详细注释）**：
  - **文件名**：`student_magic_methods_exercise.py`
  ```python
  # 定义 Student 类，展示魔法方法
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      
      def __str__(self):
          return f"学生：{self.name}，年龄：{self.age}"

  if __name__ == "__main__":
      # 创建学生对象
      student = Student("小明", 20)

      # 使用 __str__ 方法打印
      print(student)  # 输出：学生：小明，年龄：20

      # 访问特殊属性
      print(student.__dict__)  # 输出：{'name': '小明', 'age': 20}
  ```
  **语法解释**：
  - `__str__(self)`：自定义打印输出，增强可读性。
  - `__dict__`：查看对象的所有属性，类似查看字典。

### 作业练习（课后完成）
- **任务描述**：扩展 `Student` 类，添加 `__repr__` 方法，返回官方表示（如 `Student(name='小明', age=20)`），并添加 `__len__` 方法，返回年龄作为长度。
- **目标**：熟悉更多魔法方法的自定义行为。
- **参考代码（带详细注释）**：
  - **文件名**：`student_magic_methods_homework.py`
  ```python
  # 定义 Student 类，展示魔法方法
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      
      def __str__(self):
          return f"学生：{self.name}，年龄：{self.age}"
      
      def __repr__(self):
          return f"Student(name='{self.name}', age={self.age})"
      
      def __len__(self):
          return self.age

  if __name__ == "__main__":
      # 创建学生对象
      student = Student("小明", 20)

      # 使用 __str__ 方法打印
      print(student)  # 输出：学生：小明，年龄：20

      # 使用 __repr__ 方法打印
      print(repr(student))  # 输出：Student(name='小明', age=20)

      # 使用 __len__ 方法
      print(len(student))  # 输出：20
  ```
  **语法解释**：
  - `__repr__(self)`：定义调试时的字符串表示。
  - `__len__(self)`：定义长度行为，返回年龄，体现魔法方法的灵活性。

---

### 总结与过渡
本节内容（魔法方法与特殊属性）作为第二天的起点，延续了第一天的 `__init__` 概念，帮助学员学会自定义对象行为，为后续进阶特性打下基础。下一节将介绍属性装饰器，深化封装概念，探索更优雅的属性管理方式。

好的！接下来我将编写第二天的教案中第二节的内容，即 **属性装饰器（Property & Descriptor）** 部分。教案将延续之前的风格，注重与第一天内容的衔接、理论与实践结合，并根据之前的讨论控制难度，重点讲解 `@property` 的使用，简化描述符部分。以下是详细内容。

---

## 第二节：属性装饰器（Property & Descriptor）

### 教学目标
- 掌握 `@property` 装饰器的用法，学会通过属性化的方式简化 getter/setter 方法，提升代码封装性。
- 初步了解描述符（Descriptor）的概念，认识其在属性管理中的作用（不深入，仅作为扩展）。

### 教学内容（详细理论讲解）
1. **复习第一天封装概念**
   - 封装是 OOP 的核心原则之一，通过私有属性（如 `self.__name`）隐藏数据，使用 getter/setter 方法控制访问。
   - 第一天的例子：定义 `Student` 类，私有属性 `__age`，通过 `get_age()` 和 `set_age()` 方法访问和修改。
   - 问题：getter/setter 方法调用不够直观，代码显得冗长，例如 `student.set_age(20)` 不如直接 `student.age = 20` 自然。
   - 引入本节主题：Python 提供了 `@property` 装饰器，可以将方法伪装成属性访问，简化代码，同时保留封装的控制能力。

2. **什么是属性装饰器（@property）？**
   - `@property` 是 Python 内置的装饰器，用于将方法变成“属性”访问方式，无需显式调用 getter/setter。
   - 核心作用：让方法像属性一样访问（`student.age` 而非 `student.get_age()`），但内部仍能执行逻辑（如数据验证）。
   - 相关装饰器：
     - `@property`：将方法定义为 getter，读取属性值。
     - `@属性名.setter`：将方法定义为 setter，设置属性值。
   - 好处：代码更简洁，符合直觉，同时保留封装特性（可以添加逻辑控制）。

3. **@property 的基本用法**
   - 定义私有属性（如 `self.__age`）存储数据。
   - 使用 `@property` 装饰 getter 方法，返回私有属性的值。
   - 使用 `@属性名.setter` 装饰 setter 方法，设置私有属性的值并添加逻辑（如验证）。
   - 调用时，直接用 `对象.属性` 读取或赋值，背后自动调用 getter/setter 方法。

4. **什么是描述符（Descriptor）？（简要介绍）**
   - 描述符是更底层的属性管理机制，通过定义 `__get__` 和 `__set__` 方法控制属性访问行为。
   - 作用：为多个属性或类提供统一的管理逻辑（如数据验证、延迟加载），是 `@property` 的底层实现。
   - 本节不深入，仅作为扩展知识点，了解其存在即可，重点仍放在 `@property` 的应用上。

5. **属性装饰器的实际应用场景**
   - 用于需要控制属性访问的场景，比如年龄不能为负数、价格必须为正数。
   - 比直接暴露属性更安全，比传统 getter/setter 更简洁。

6. **Mermaid 结构图**
   ```mermaid
    graph TD
        Class["类: Student"] -->|"私有属性"| PrivateAttr["__age"]
        Class -->|"方法"| Getter["@property<br>get_age()"]
        Class -->|"方法"| Setter["@age.setter<br>set_age()"]
        Getter -->|"返回"| PrivateAttr
        Setter -->|"修改"| PrivateAttr
        Note["使用: student.age"] -->|"读取"| Getter
        Note -->|"赋值"| Setter
   ```

7. **形象对比（日常生活中）**
   - 属性装饰器就像“智能门锁”。门锁保护家里的东西（类似私有属性），你不需要每次都手动“打电话给保安”来开门或锁门（类似传统 getter/setter），而是直接刷卡进出（类似 `student.age`），背后系统自动完成验证和操作。
   - 描述符就像“物业管理系统”，统一管理多个门锁的规则（比如所有门锁都要求刷卡），更高级但也更复杂，所以我们先用好单个门锁（`@property`）。

8. **代码示例（带详细注释和语法解释）**
   - **文件名**：`student_property.py`
   ```python
   # 定义 Student 类，展示 @property 装饰器的用法
   class Student:
       def __init__(self, name, age):
           self.name = name
           self.__age = age  # 私有属性，保护数据
       
       @property  # 将方法变成属性访问（getter）
       def age(self):
           return self.__age
       
       @age.setter  # 定义 setter 方法，控制赋值
       def age(self, value):
           if value < 0:  # 验证逻辑：年龄不能为负数
               raise ValueError("年龄不能为负数！")
           self.__age = value

   if __name__ == "__main__":
       # 创建学生对象
       student = Student("小明", 20)

       # 读取年龄，像访问属性一样（背后调用 getter）
       print(student.age)  # 输出：20

       # 设置年龄，像赋值属性一样（背后调用 setter）
       student.age = 21
       print(student.age)  # 输出：21

       # 尝试设置无效值，会触发验证
       try:
           student.age = -5
       except ValueError as e:
           print(e)  # 输出：年龄不能为负数！
   ```
   **语法解释**：
   - `@property`：将 `age` 方法变成只读属性，调用时无需加括号，直接 `student.age`。
   - `@age.setter`：定义 `age` 的 setter 方法，允许赋值 `student.age = 21`，并在内部执行验证逻辑。
   - 私有属性 `__age`：存储实际数据，通过 getter/setter 控制访问。

### 教案练习（课堂内完成）
- **任务描述**：定义一个 `Book` 类，包含私有属性 `__price`（书籍价格），使用 `@property` 实现 getter 和 setter，要求价格不能小于 0，测试读取和设置价格。
- **预期时间**：10 分钟
- **指导**：教师指导学员实现属性装饰器，理解如何在 setter 中添加验证逻辑。
- **参考代码（带详细注释）**：
  - **文件名**：`book_property_exercise.py`
  ```python
  # 定义 Book 类，展示 @property 装饰器
  class Book:
      def __init__(self, title, price):
          self.title = title
          self.__price = price  # 私有属性
      
      @property
      def price(self):
          return self.__price
      
      @price.setter
      def price(self, value):
          if value < 0:
              raise ValueError("价格不能为负数！")
          self.__price = value

  if __name__ == "__main__":
      # 创建书籍对象
      book = Book("Python 编程", 50.0)

      # 读取价格
      print(book.price)  # 输出：50.0

      # 设置价格
      book.price = 60.0
      print(book.price)  # 输出：60.0

      # 尝试设置无效值
      try:
          book.price = -10.0
      except ValueError as e:
          print(e)  # 输出：价格不能为负数！
  ```
  **语法解释**：
  - `@property`：将 `price` 方法变成属性，读取时直接 `book.price`。
  - `@price.setter`：允许赋值 `book.price = 60.0`，并验证价格非负。

### 作业练习（课后完成）
- **任务描述**：扩展 `Book` 类，添加私有属性 `__stock`（库存量），使用 `@property` 实现 getter 和 setter，要求库存量不能小于 0，测试读取和设置库存。
- **目标**：进一步熟悉属性装饰器的使用，强化封装思想。
- **参考代码（带详细注释）**：
  - **文件名**：`book_stock_property_homework.py`
  ```python
  # 定义 Book 类，展示 @property 装饰器
  class Book:
      def __init__(self, title, price, stock):
          self.title = title
          self.__price = price
          self.__stock = stock  # 私有属性
      
      @property
      def price(self):
          return self.__price
      
      @price.setter
      def price(self, value):
          if value < 0:
              raise ValueError("价格不能为负数！")
          self.__price = value
      
      @property
      def stock(self):
          return self.__stock
      
      @stock.setter
      def stock(self, value):
          if value < 0:
              raise ValueError("库存量不能为负数！")
          self.__stock = value

  if __name__ == "__main__":
      # 创建书籍对象
      book = Book("Python 编程", 50.0, 100)

      # 读取库存
      print(book.stock)  # 输出：100

      # 设置库存
      book.stock = 80
      print(book.stock)  # 输出：80

      # 尝试设置无效值
      try:
          book.stock = -10
      except ValueError as e:
          print(e)  # 输出：库存量不能为负数！
  ```
  **语法解释**：
  - 为 `stock` 添加 `@property` 和 `@stock.setter`，实现库存量的属性化访问和验证。
  - 体现封装原则：数据（`__stock`）隐藏，访问通过方法控制。

---

### 总结与过渡
本节内容（属性装饰器）深化了第一天的封装概念，通过 `@property` 让属性访问更直观，同时保留了数据保护和逻辑控制的能力。描述符作为扩展知识点，帮助学员了解属性管理的底层机制（不要求掌握）。下一节将介绍类方法与静态方法，进一步探索类和方法的设计方式，完善 OOP 知识体系。

---

## 第三节：类方法与静态方法（Class Methods & Static Methods）

### 教学目标
- 掌握 `@classmethod` 和 `@staticmethod` 的用法，理解它们与普通实例方法的区别。
- 学会在适当场景下使用类方法和静态方法，增强类设计的灵活性。

### 教学内容（详细理论讲解）
1. **复习第一天方法概念**
   - 第一天学习了实例方法（普通方法），如 `student.study()`，通过 `self` 参数操作实例属性。
   - 问题：有些方法不依赖具体实例，而是与整个类相关（如统计学生总数）；有些方法只是工具函数，与类和实例都无关。
   - 引入本节主题：Python 提供了 `@classmethod` 和 `@staticmethod`，分别用于定义与类相关的方法和独立工具方法。

2. **什么是类方法（@classmethod）？**
   - 类方法是绑定到类而不是实例的方法，使用 `@classmethod` 装饰器定义，第一个参数是 `cls`，代表类本身。
   - 作用：操作类级别的数据（如类属性），常用于需要访问或修改类状态的场景。
   - 调用方式：可以通过类调用（如 `Student.get_count()`）或实例调用（如 `student.get_count()`），但通常用类调用更清晰。

3. **什么是静态方法（@staticmethod）？**
   - 静态方法是定义在类中的普通函数，使用 `@staticmethod` 装饰器定义，不需要 `self` 或 `cls` 参数。
   - 作用：作为工具函数，逻辑上与类相关，但不操作类或实例的数据，纯粹是为了代码组织。
   - 调用方式：可以通过类或实例调用，通常用类调用更符合语义。

4. **实例方法、类方法与静态方法的区别**
   - 实例方法：绑定实例，操作实例属性，参数为 `self`。
   - 类方法：绑定类，操作类属性，参数为 `cls`。
   - 静态方法：不绑定类或实例，仅作为工具函数，无特殊参数。
   - 总结：实例方法关注对象个体，类方法关注类整体，静态方法关注功能组织。

5. **实际应用场景**
   - 类方法：统计类的实例数量、从类级别创建对象（如工厂方法）。
   - 静态方法：定义与类主题相关的工具函数（如格式化日期、计算折扣）。

6. **Mermaid 结构图**
   ```mermaid
    graph TD
        Class["类: Student"] -->|"实例方法"| InstanceMethod["study(self)"]
        Class -->|"类方法"| ClassMethod["@classmethod<br>get_count(cls)"]
        Class -->|"静态方法"| StaticMethod["@staticmethod<br>format_date()"]
        InstanceMethod -->|"操作"| InstanceAttr["实例属性"]
        ClassMethod -->|"操作"| ClassAttr["类属性"]
        StaticMethod -->|"无绑定"| Utility["工具函数"]
   ```

7. **形象对比（日常生活中）**
   - 实例方法就像“学生个人的学习行为”，每个学生有自己的方式（`self`），操作自己的笔记（实例属性）。
   - 类方法就像“班级的统计工作”，由班主任（`cls`）负责统计全班人数（类属性），与整个班级相关。
   - 静态方法就像“班级用的计算器”，只是一个工具，任何人都能用，不依赖具体学生或班级，只提供计算功能。
   - 总结：实例方法是个人的，类方法是集体的，静态方法是工具。

8. **代码示例（带详细注释和语法解释）**
   - **文件名**：`student_class_static_methods.py`
   ```python
   # 定义 Student 类，展示类方法和静态方法
   class Student:
       _count = 0  # 类属性，记录学生总数

       def __init__(self, name):
           self.name = name
           Student._count += 1  # 每次创建实例，计数加 1
       
       @classmethod  # 类方法，操作类属性
       def get_count(cls):
           return cls._count
       
       @staticmethod  # 静态方法，作为工具函数
       def format_greeting(name):
           return f"你好，{name}！欢迎加入班级！"

   if __name__ == "__main__":
       # 创建学生对象
       s1 = Student("小明")
       s2 = Student("小红")

       # 使用类方法获取学生总数
       print(Student.get_count())  # 输出：2
       print(s1.get_count())  # 也可以通过实例调用，输出：2

       # 使用静态方法格式化问候语
       print(Student.format_greeting("小刚"))  # 输出：你好，小刚！欢迎加入班级！
       print(s1.format_greeting("小李"))  # 也可以通过实例调用，输出：你好，小李！欢迎加入班级！
   ```
   **语法解释**：
   - `@classmethod`：定义 `get_count` 为类方法，参数 `cls` 代表类本身，访问类属性 `_count`。
   - `@staticmethod`：定义 `format_greeting` 为静态方法，无需特殊参数，纯粹作为工具函数。
   - 类属性 `_count`：记录学生总数，类方法可以直接操作。

### 教案练习（课堂内完成）
- **任务描述**：定义一个 `Library` 类，使用类属性记录书籍总数，使用 `@classmethod` 定义方法获取书籍总数，使用 `@staticmethod` 定义一个工具方法格式化书籍信息（如返回“标题：xxx”）。
- **预期时间**：10 分钟
- **指导**：教师指导学员实现类方法和静态方法，理解两者的区别。
- **参考代码（带详细注释）**：
  - **文件名**：`library_class_static_exercise.py`
  ```python
  # 定义 Library 类，展示类方法和静态方法
  class Library:
      _book_count = 0  # 类属性，记录书籍总数

      def __init__(self, title):
          self.title = title
          Library._book_count += 1
      
      @classmethod
      def get_book_count(cls):
          return cls._book_count
      
      @staticmethod
      def format_book_info(title):
          return f"标题：{title}"

  if __name__ == "__main__":
      # 创建书籍对象
      b1 = Library("Python 编程")
      b2 = Library("Java 编程")

      # 使用类方法获取书籍总数
      print(Library.get_book_count())  # 输出：2

      # 使用静态方法格式化书籍信息
      print(Library.format_book_info("Python 编程"))  # 输出：标题：Python 编程
  ```
  **语法解释**：
  - `@classmethod`：`get_book_count` 操作类属性 `_book_count`，返回书籍总数。
  - `@staticmethod`：`format_book_info` 作为工具函数，格式化书籍标题。

### 作业练习（课后完成）
- **任务描述**：扩展 `Library` 类，添加类方法 `add_book(cls, num)` 增加书籍总数，添加静态方法 `calculate_discount(price)` 计算书籍折扣价（假设折扣为 80%）。
- **目标**：进一步熟悉类方法和静态方法的应用。
- **参考代码（带详细注释）**：
  - **文件名**：`library_class_static_homework.py`
  ```python
  # 定义 Library 类，展示类方法和静态方法
  class Library:
      _book_count = 0  # 类属性，记录书籍总数

      def __init__(self, title):
          self.title = title
          Library._book_count += 1
      
      @classmethod
      def get_book_count(cls):
          return cls._book_count
      
      @classmethod
      def add_book(cls, num):
          cls._book_count += num
      
      @staticmethod
      def format_book_info(title):
          return f"标题：{title}"
      
      @staticmethod
      def calculate_discount(price):
          return price * 0.8

  if __name__ == "__main__":
      # 创建书籍对象
      b1 = Library("Python 编程")

      # 使用类方法获取和增加书籍总数
      print(Library.get_book_count())  # 输出：1
      Library.add_book(2)
      print(Library.get_book_count())  # 输出：3

      # 使用静态方法计算折扣价
      print(Library.calculate_discount(100))  # 输出：80.0
  ```
  **语法解释**：
  - 类方法 `add_book`：通过 `cls` 修改类属性 `_book_count`。
  - 静态方法 `calculate_discount`：作为工具函数，计算折扣价。

---

## 第四节：抽象类与接口（Abstract Classes & Interfaces）

### 教学目标
- 理解抽象类和接口的概念，掌握如何使用 `abc` 模块定义抽象类。
- 学会通过抽象类规范子类行为，提升代码设计的规范性。

### 教学内容（详细理论讲解）
1. **复习第一天继承概念**
   - 继承允许子类复用父类代码，并通过重写方法实现多态。
   - 问题：如何确保子类必须实现某些方法？比如，动物类要求所有子类都实现“叫声”方法。
   - 引入本节主题：抽象类和接口通过定义“规范”，强制子类实现特定方法，解决继承中的行为约束问题。

2. **什么是抽象类？**
   - 抽象类是不能被实例化的类，用于定义通用接口和部分实现，子类必须实现抽象方法才能实例化。
   - 在 Python 中，使用 `abc` 模块的 `ABC` 类和 `@abstractmethod` 装饰器定义抽象类和方法。
   - 作用：作为模板，规范子类行为，提供部分共享代码。

3. **什么是接口？**
   - 接口是抽象类的极端形式，只定义方法签名，不提供任何实现，类似“契约”，要求子类完全实现。
   - Python 中没有严格的接口关键字，但可以通过全抽象的 `ABC` 类模拟。
   - 作用：强调规范，解耦实现与接口。

4. **抽象类与接口的区别**
   - 抽象类：可以包含具体方法和属性，部分实现+部分抽象。
   - 接口：通常只包含抽象方法，完全规范。
   - Python 中，两者实现方式类似，区别在于设计意图。

5. **实际应用场景**
   - 抽象类：定义通用基类，如动物类要求所有子类实现叫声，但提供通用属性（如名称）。
   - 接口：定义标准协议，如支付接口要求所有支付方式实现支付方法。

6. **Mermaid 结构图**
   ```mermaid
    graph TD
        AbstractClass["抽象类: Animal ABC"] -->|"继承"| SubClass1["子类: Dog"]
        AbstractClass -->|"继承"| SubClass2["子类: Cat"]
        AbstractClass -->|"抽象方法"| AbsMethod["@abstractmethod<br>speak()"]
        AbstractClass -->|"具体属性"| Attr["name"]
        SubClass1 -->|"实现"| Speak1["speak(): '汪汪'"]
        SubClass2 -->|"实现"| Speak2["speak(): '喵喵'"]
   ```

7. **形象对比（日常生活中）**
   - 抽象类就像“建筑设计图”，规定了房子必须有的基本结构（如门窗），但也提供了一些通用设计（如墙体材料），具体样式由建造者（子类）决定。
   - 接口就像“合同条款”，只规定必须做什么（如必须有门），不关心怎么做，完全由实现者决定。
   - 总结：抽象类是半成品模板，接口是纯规范。

8. **代码示例（带详细注释和语法解释）**
   - **文件名**：`animal_abstract_class.py`
   ```python
   # 导入 abc 模块，用于定义抽象类
   from abc import ABC, abstractmethod

   # 定义抽象类 Animal
   class Animal(ABC):  # 继承 ABC 表示这是抽象类
       def __init__(self, name):
           self.name = name
       
       @abstractmethod  # 抽象方法，子类必须实现
       def speak(self):
           pass  # 抽象方法无需实现

       def introduce(self):  # 具体方法，可被子类继承
           return f"我是 {self.name}"

   # 定义子类 Dog
   class Dog(Animal):
       def speak(self):  # 实现抽象方法
           return "汪汪！"

   # 定义子类 Cat
   class Cat(Animal):
       def speak(self):  # 实现抽象方法
           return "喵喵！"

   if __name__ == "__main__":
       # 无法实例化抽象类
       try:
           animal = Animal("动物")
       except TypeError as e:
           print(e)  # 输出：Can't instantiate abstract class Animal ...

       # 实例化子类
       dog = Dog("小狗")
       cat = Cat("小猫")

       # 调用方法
       print(dog.introduce(), dog.speak())  # 输出：我是 小狗 汪汪！
       print(cat.introduce(), cat.speak())  # 输出：我是 小猫 喵喵！
   ```
   **语法解释**：
   - `ABC`：从 `abc` 模块导入，定义抽象基类。
   - `@abstractmethod`：标记抽象方法，子类必须实现。
   - 抽象类不能实例化，子类未实现抽象方法也会报错。

### 教案练习（课堂内完成，13:50-14:00）
- **任务描述**：定义一个抽象类 `Shape`（形状），包含抽象方法 `area()` 计算面积，定义两个子类 `Circle`（圆）和 `Rectangle`（矩形），分别实现面积计算。
- **预期时间**：10 分钟
- **指导**：教师指导学员实现抽象类和子类，理解规范作用。
- **参考代码（带详细注释）**：
  - **文件名**：`shape_abstract_exercise.py`
  ```python
  from abc import ABC, abstractmethod
  import math

  # 定义抽象类 Shape
  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass

  # 定义子类 Circle
  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius
      
      def area(self):
          return math.pi * self.radius ** 2

  # 定义子类 Rectangle
  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height
      
      def area(self):
          return self.width * self.height

  if __name__ == "__main__":
      # 实例化子类
      circle = Circle(5)
      rectangle = Rectangle(4, 6)

      # 计算面积
      print(f"圆面积：{circle.area():.2f}")  # 输出：圆面积：78.54
      print(f"矩形面积：{rectangle.area()}")  # 输出：矩形面积：24
  ```
  **语法解释**：
  - 抽象类 `Shape` 定义规范，子类必须实现 `area()`。
  - 子类根据自身逻辑实现面积计算。

### 作业练习（课后完成）
- **任务描述**：扩展 `Shape` 类，添加抽象方法 `perimeter()` 计算周长，子类 `Circle` 和 `Rectangle` 实现周长计算。
- **目标**：进一步熟悉抽象类的规范作用。
- **参考代码（带详细注释）**：
  - **文件名**：`shape_perimeter_homework.py`
  ```python
  from abc import ABC, abstractmethod
  import math

  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass
      
      @abstractmethod
      def perimeter(self):
          pass

  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius
      
      def area(self):
          return math.pi * self.radius ** 2
      
      def perimeter(self):
          return 2 * math.pi * self.radius

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height
      
      def area(self):
          return self.width * self.height
      
      def perimeter(self):
          return 2 * (self.width + self.height)

  if __name__ == "__main__":
      circle = Circle(5)
      rectangle = Rectangle(4, 6)

      print(f"圆面积：{circle.area():.2f}, 周长：{circle.perimeter():.2f}")
      print(f"矩形面积：{rectangle.area()}, 周长：{rectangle.perimeter()}")
  ```
  **语法解释**：
  - 增加抽象方法 `perimeter()`，子类实现周长计算。

---

## 第五节：OOP 设计原则与综合案例（OOP Design Principles & Comprehensive Case）

### 教学目标
- 初步了解 SOLID 设计原则，重点理解单一职责和开闭原则，培养良好的代码设计意识。
- 通过综合案例（图书管理系统），整合第二天所有知识点，提升实际应用能力。

### 教学内容（详细理论讲解）
1. **什么是 OOP 设计原则（SOLID）？**
   - SOLID 是面向对象设计的五大原则，帮助编写可维护、可扩展的代码。
   - 本节仅简要介绍两个核心原则（不深入，注重实践）：
     - 单一职责原则（Single Responsibility Principle, SRP）：一个类只负责一件事，避免功能耦合。
     - 开闭原则（Open/Closed Principle, OCP）：对扩展开放，对修改关闭，通过继承实现新功能。
   - 作用：提高代码质量，降低维护成本。

2. **单一职责原则（SRP）**
   - 一个类只做一件事，比如书籍类只管理书籍信息，借阅逻辑交给其他类。
   - 好处：职责清晰，修改时不影响其他功能。

3. **开闭原则（OCP）**
   - 通过继承或接口扩展功能，而不是修改原有代码，比如添加新支付方式时不改支付基类。
   - 好处：代码稳定，易于扩展。

4. **综合案例：图书管理系统**
   - 场景：设计一个简单的图书管理系统，包含书籍（`Book`）、用户（`User`）和图书馆（`Library`），实现借书和还书功能。
   - 目标：整合魔法方法、属性装饰器、类方法、静态方法、抽象类等知识点。
   - 设计思路：
     - `Book` 类：管理书籍信息，使用 `@property` 控制价格，魔法方法 `__str__` 自定义输出。
     - `User` 类：管理用户信息，记录借阅书籍。
     - `Library` 类：管理书籍库存，使用类方法统计书籍总数，静态方法格式化信息。
     - 使用抽象类 `Borrowable` 定义借阅规范。

5. **Mermaid 结构图**
   ```mermaid
    flowchart TD
        AbstractClass["Borrowable ABC"] -->|继承| LibraryClass["Library"]
        LibraryClass -->|关联| BookClass["Book"]
        LibraryClass -->|关联| UserClass["User"]
        BookClass -->|属性| BookAttr["@property price"]
        BookClass -->|魔法方法| BookMagic["__str__()"]
        LibraryClass -->|类方法| LibraryCls["@classmethod total_books()"]
        LibraryClass -->|静态方法| LibraryStatic["@staticmethod format_info()"]
   ```

6. **形象对比（日常生活中）**
   - SOLID 原则就像“建筑规范”，单一职责是“每个工人只负责一件事”，开闭原则是“房子建好后不拆墙，通过加建扩展”。
   - 图书管理系统就像“现实图书馆”，有书籍、用户和管理规则，各个角色职责清晰，功能通过规范扩展。

7. **代码示例（带详细注释和语法解释）**
   - **文件名**：`library_management_system.py`
   ```python
   from abc import ABC, abstractmethod

   # 抽象类，定义借阅规范
   class Borrowable(ABC):
       @abstractmethod
       def borrow_book(self, user, book):
           pass
       
       @abstractmethod
       def return_book(self, user, book):
           pass

   # 书籍类
   class Book:
       def __init__(self, title, price):
           self.title = title
           self.__price = price
           self.is_borrowed = False
       
       @property
       def price(self):
           return self.__price
       
       @price.setter
       def price(self, value):
           if value < 0:
               raise ValueError("价格不能为负数！")
           self.__price = value
       
       def __str__(self):
           return f"书籍：{self.title}，价格：{self.__price}"

   # 用户类
   class User:
       def __init__(self, name):
           self.name = name
           self.borrowed_books = []
       
       def __str__(self):
           return f"用户：{self.name}"

   # 图书馆类，实现借阅规范
   class Library(Borrowable):
       _total_books = 0  # 类属性，记录书籍总数

       def __init__(self, name):
           self.name = name
           self.books = []
       
       def add_book(self, book):
           self.books.append(book)
           Library._total_books += 1
       
       @classmethod
       def total_books(cls):
           return cls._total_books
       
       @staticmethod
       def format_info(title, status):
           return f"{title} - {status}"
       
       def borrow_book(self, user, book):
           if book in self.books and not book.is_borrowed:
               book.is_borrowed = True
               user.borrowed_books.append(book)
               return f"{user.name} 借阅了 {book.title}"
           return "借阅失败，书籍不可用"
       
       def return_book(self, user, book):
           if book in user.borrowed_books:
               book.is_borrowed = False
               user.borrowed_books.remove(book)
               return f"{user.name} 归还了 {book.title}"
           return "归还失败，书籍未借阅"

   if __name__ == "__main__":
       # 创建图书馆、书籍和用户
       library = Library("城市图书馆")
       book1 = Book("Python 编程", 50.0)
       book2 = Book("Java 编程", 60.0)
       user = User("小明")

       # 添加书籍
       library.add_book(book1)
       library.add_book(book2)
       print(f"书籍总数：{Library.total_books()}")  # 输出：书籍总数：2

       # 借阅和归还
       print(library.borrow_book(user, book1))  # 输出：小明 借阅了 Python 编程
       print(library.format_info(book1.title, "已借出"))  # 输出：Python 编程 - 已借出
       print(library.return_book(user, book1))  # 输出：小明 归还了 Python 编程
   ```
   **语法解释**：
   - 整合所有知识点：`Book` 使用 `@property` 和 `__str__`，`Library` 使用类方法和静态方法，`Borrowable` 定义抽象规范。

### 教案练习（课堂内完成，14:50-15:00）
- **任务描述**：初步设计图书管理系统的类结构，定义 `Book` 和 `User` 类，添加基本属性和方法，为后续综合项目做准备。
- **预期时间**：10 分钟
- **指导**：教师指导学员设计类结构，理解职责划分。
- **参考代码（带详细注释）**：
  - **文件名**：`library_system_design_exercise.py`
  ```python
  class Book:
      def __init__(self, title, price):
          self.title = title
          self.__price = price
          self.is_borrowed = False
      
      @property
      def price(self):
          return self.__price
      
      @price.setter
      def price(self, value):
          if value < 0:
              raise ValueError("价格不能为负数！")
          self.__price = value
      
      def __str__(self):
          return f"书籍：{self.title}"

  class User:
      def __init__(self, name):
          self.name = name
          self.borrowed_books = []
      
      def __str__(self):
          return f"用户：{self.name}"

  if __name__ == "__main__":
      book = Book("Python 编程", 50.0)
      user = User("小明")
      print(book)  # 输出：书籍：Python 编程
      print(user)  # 输出：用户：小明
  ```
  **语法解释**：
  - `Book` 和 `User` 类初步设计，为后续添加功能做准备。

### 作业练习（课后完成）
- **任务描述**：扩展上述代码，添加 `Library` 类初步结构，包含添加书籍和统计总数的功能。
- **目标**：为综合项目奠定基础。
- **参考代码（带详细注释）**：
  - **文件名**：`library_system_homework.py`
  ```python
  class Book:
      def __init__(self, title, price):
          self.title = title
          self.__price = price
          self.is_borrowed = False
      
      @property
      def price(self):
          return self.__price
      
      @price.setter
      def price(self, value):
          if value < 0:
              raise ValueError("价格不能为负数！")
          self.__price = value
      
      def __str__(self):
          return f"书籍：{self.title}"

  class User:
      def __init__(self, name):
          self.name = name
          self.borrowed_books = []
      
      def __str__(self):
          return f"用户：{self.name}"

  class Library:
      _total_books = 0
      
      def __init__(self, name):
          self.name = name
          self.books = []
      
      def add_book(self, book):
          self.books.append(book)
          Library._total_books += 1
      
      @classmethod
      def total_books(cls):
          return cls._total_books

  if __name__ == "__main__":
      library = Library("城市图书馆")
      book1 = Book("Python 编程", 50.0)
      library.add_book(book1)
      print(f"书籍总数：{Library.total_books()}")  # 输出：书籍总数：1
  ```
  **语法解释**：
  - `Library` 类初步实现书籍管理功能。

---

好的，我理解你的需求。以下是为“实践环节：基础练习与综合项目”部分准备的详细代码内容，每个练习和项目都包含完整的实现，并附带详细的注释和学习内容解释。这些代码和解释可以作为学员的学习材料，供他们在实践中参考和理解。虽然你不需要讲解，但这些内容会帮助学员自学和巩固知识点。所有代码都遵循规范，`if __name__ == "__main__":` 放在模块顶层。

---

## 实践环节：基础练习与综合项目

### 基础练习
- **目标**：通过小练习巩固魔法方法、属性装饰器、类方法、静态方法和抽象类的理解。
- **内容**：以下每个练习都包含完整代码和详细注释，供学员学习和实践。

#### 1. 魔法方法：修改 `Student` 类，完善 `__str__` 和 `__repr__` 方法
- **文件名**：`student_magic_methods.py`
```python
# 学习内容解释：
# 魔法方法是 Python 中以双下划线开头和结尾的特殊方法，用于自定义类的行为。
# __str__：定义对象转换为字符串时的输出，面向用户，注重可读性。
# __repr__：定义对象的“官方”表示，通常用于调试，注重准确性。
# 本练习目标：为 Student 类添加 __str__ 和 __repr__ 方法，理解两者的区别。

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # __str__ 方法返回用户友好的字符串表示
        return f"学生：{self.name}，年龄：{self.age}"
    
    def __repr__(self):
        # __repr__ 方法返回详细的字符串表示，用于调试
        return f"Student(name='{self.name}', age={self.age})"


if __name__ == "__main__":
    # 测试魔法方法
    student = Student("小明", 20)
    print(str(student))  # 输出：学生：小明，年龄：20
    print(repr(student))  # 输出：Student(name='小明', age=20)
```
- **学习内容解释**（代码注释中已包含）：学员通过此练习理解 `__str__` 和 `__repr__` 的用途和区别，学会如何自定义对象的字符串表示。

#### 2. 属性装饰器：为 `Book` 类添加库存属性，使用 `@property` 控制
- **文件名**：`book_property_stock.py`
```python
# 学习内容解释：
# 属性装饰器 @property 允许将方法伪装成属性访问，简化 getter/setter 调用。
# 本练习目标：为 Book 类添加库存属性 __stock，使用 @property 控制访问和修改，确保库存量不小于 0。

class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.__price = price
        self.__stock = stock  # 私有属性，存储库存量
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负数！")
        self.__price = value
    
    @property
    def stock(self):
        # getter 方法，读取库存量
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        # setter 方法，控制库存量修改
        if value < 0:
            raise ValueError("库存量不能为负数！")
        self.__stock = value


if __name__ == "__main__":
    # 测试属性装饰器
    book = Book("Python 编程", 50.0, 100)
    print(f"初始库存：{book.stock}")  # 输出：初始库存：100
    book.stock = 80  # 修改库存
    print(f"修改后库存：{book.stock}")  # 输出：修改后库存：80
    try:
        book.stock = -10  # 尝试设置无效值
    except ValueError as e:
        print(f"错误：{e}")  # 输出：错误：库存量不能为负数！
```
- **学习内容解释**（代码注释中已包含）：学员通过此练习掌握 `@property` 的用法，理解如何通过属性装饰器实现数据封装和验证。

#### 3. 类方法与静态方法：扩展 `Library` 类，添加类方法和静态方法
- **文件名**：`library_class_static_methods.py`
```python
# 学习内容解释：
# 类方法 (@classmethod) 绑定到类，操作类级别数据，参数为 cls。
# 静态方法 (@staticmethod) 不绑定类或实例，作为工具函数。
# 本练习目标：扩展 Library 类，使用类方法统计书籍总数，使用静态方法格式化书籍信息。

class Library:
    _book_count = 0  # 类属性，记录书籍总数

    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        Library._book_count += 1
    
    @classmethod
    def get_book_count(cls):
        # 类方法，返回书籍总数
        return cls._book_count
    
    @classmethod
    def reset_count(cls):
        # 类方法，重置书籍总数
        cls._book_count = 0
    
    @staticmethod
    def format_book_info(title, author):
        # 静态方法，作为工具函数格式化书籍信息
        return f"书籍：{title}，作者：{author}"


if __name__ == "__main__":
    # 测试类方法和静态方法
    library = Library("城市图书馆")
    library.add_book("Python 编程")
    library.add_book("Java 编程")
    print(f"书籍总数：{Library.get_book_count()}")  # 输出：书籍总数：2
    print(Library.format_book_info("Python 编程", "张三"))  # 输出：书籍：Python 编程，作者：张三
    Library.reset_count()
    print(f"重置后书籍总数：{Library.get_book_count()}")  # 输出：重置后书籍总数：0
```
- **学习内容解释**（代码注释中已包含）：学员通过此练习理解类方法和静态方法的区别与应用场景，掌握操作类属性和工具函数的定义。

#### 4. 抽象类：扩展 `Shape` 类，添加新子类 `Triangle` 实现面积和周长计算
- **文件名**：`shape_abstract_triangle.py`
```python
# 学习内容解释：
# 抽象类 (ABC) 定义规范，子类必须实现抽象方法。
# 本练习目标：扩展 Shape 抽象类，添加 Triangle 子类，实现面积和周长计算。

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        # 抽象方法，计算面积
        pass
    
    @abstractmethod
    def perimeter(self):
        # 抽象方法，计算周长
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # 三边长度
        self.b = b
        self.c = c
    
    def area(self):
        # 使用海伦公式计算三角形面积
        s = (self.a + self.b + self.c) / 2  # 半周长
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        # 计算三角形周长
        return self.a + self.b + self.c


if __name__ == "__main__":
    # 测试抽象类和子类
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    print(f"圆面积：{circle.area():.2f}，周长：{circle.perimeter():.2f}")
    print(f"矩形面积：{rectangle.area()}，周长：{rectangle.perimeter()}")
    print(f"三角形面积：{triangle.area():.2f}，周长：{triangle.perimeter()}")
    # 输出示例：
    # 圆面积：78.54，周长：31.42
    # 矩形面积：24，周长：20
    # 三角形面积：6.00，周长：12
```
- **学习内容解释**（代码注释中已包含）：学员通过此练习掌握抽象类的规范作用，学会如何通过继承实现具体功能（如三角形面积计算）。

---

### 综合项目：图书管理系统完整实现
- **目标**：整合所有知识点，完成图书管理系统的设计与实现，包含借书、还书功能。
- **任务描述**：完善 `Book`、`User` 和 `Library` 类，使用抽象类定义借阅规范，实现借书、还书、统计书籍总数等功能。
- **参考代码**：以下是完整实现，包含详细注释和学习内容解释，供学员参考和扩展。

#### 综合项目代码
- **文件名**：`library_management_system_complete.py`
```python
# 学习内容解释：
# 本项目整合了第二天的所有知识点，包括魔法方法、属性装饰器、类方法、静态方法和抽象类。
# 目标：设计一个图书管理系统，实现书籍管理、用户借阅和图书馆统计功能。
# 学习重点：
# 1. 使用 @property 控制书籍价格和库存。
# 2. 使用魔法方法 __str__ 自定义输出。
# 3. 使用类方法统计书籍总数，静态方法格式化信息。
# 4. 使用抽象类定义借阅规范，强制子类实现借书和还书功能。

from abc import ABC, abstractmethod

# 抽象类，定义借阅规范
class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, user, book):
        # 抽象方法，借书功能
        pass
    
    @abstractmethod
    def return_book(self, user, book):
        # 抽象方法，还书功能
        pass


# 书籍类，管理书籍信息
class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.__price = price  # 私有属性，价格
        self.__stock = stock  # 私有属性，库存
        self.is_borrowed = False  # 是否被借出
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负数！")
        self.__price = value
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("库存量不能为负数！")
        self.__stock = value
    
    def __str__(self):
        # 自定义字符串表示
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"书籍：{self.title}，价格：{self.__price}，状态：{status}"


# 用户类，管理用户信息
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # 借阅的书籍列表
    
    def __str__(self):
        # 自定义字符串表示
        return f"用户：{self.name}，借阅书籍数：{len(self.borrowed_books)}"


# 图书馆类，实现借阅规范和管理功能
class Library(Borrowable):
    _total_books = 0  # 类属性，记录书籍总数

    def __init__(self, name):
        self.name = name
        self.books = []  # 书籍列表
    
    def add_book(self, book):
        # 添加书籍
        self.books.append(book)
        Library._total_books += 1
    
    @classmethod
    def total_books(cls):
        # 类方法，返回书籍总数
        return cls._total_books
    
    @staticmethod
    def format_status_info(title, status):
        # 静态方法，格式化书籍状态信息
        return f"{title} - {status}"
    
    def borrow_book(self, user, book):
        # 实现借书功能
        if book in self.books and not book.is_borrowed and book.stock > 0:
            book.is_borrowed = True
            book.stock -= 1
            user.borrowed_books.append(book)
            return f"{user.name} 成功借阅了 {book.title}"
        return f"借阅失败，{book.title} 不可用"
    
    def return_book(self, user, book):
        # 实现还书功能
        if book in user.borrowed_books:
            book.is_borrowed = False
            book.stock += 1
            user.borrowed_books.remove(book)
            return f"{user.name} 成功归还了 {book.title}"
        return f"归还失败，{book.title} 未被借阅"


if __name__ == "__main__":
    # 测试图书管理系统
    # 创建图书馆、书籍和用户
    library = Library("城市图书馆")
    book1 = Book("Python 编程", 50.0, 5)
    book2 = Book("Java 编程", 60.0, 3)
    user1 = User("小明")
    user2 = User("小红")

    # 添加书籍到图书馆
    library.add_book(book1)
    library.add_book(book2)
    print(f"书籍总数：{Library.total_books()}")  # 输出：书籍总数：2

    # 测试借书功能
    print(library.borrow_book(user1, book1))  # 输出：小明 成功借阅了 Python 编程
    print(f"书籍状态：{book1}")  # 输出：书籍：Python 编程，价格：50.0，状态：已借出
    print(f"库存：{book1.stock}")  # 输出：库存：4
    print(library.borrow_book(user2, book1))  # 输出：借阅失败，Python 编程 不可用

    # 测试还书功能
    print(library.return_book(user1, book1))  # 输出：小明 成功归还了 Python 编程
    print(f"书籍状态：{book1}")  # 输出：书籍：Python 编程，价格：50.0，状态：可借阅
    print(f"库存：{book1.stock}")  # 输出：库存：5

    # 测试用户信息
    print(user1)  # 输出：用户：小明，借阅书籍数：0
    print(user2)  # 输出：用户：小红，借阅书籍数：0

    # 测试静态方法
    print(Library.format_status_info(book2.title, "可借阅"))  # 输出：Java 编程 - 可借阅
```
- **学习内容解释**（代码注释中已包含）：学员通过此项目整合所有知识点，理解如何将魔法方法、属性装饰器、类方法、静态方法和抽象类应用到实际项目中。代码展示了完整的图书管理系统功能，包括借书、还书、库存管理和信息输出。

---

### 总结与反馈
第二天的课程从魔法方法到综合案例，逐步深入 Python OOP 进阶特性，通过理论讲解、代码演示、小练习和综合项目，确保学员从理解到应用的全方位掌握。课程注重实践导向，控制难度，选用图书管理系统作为案例，贴近学员认知。
