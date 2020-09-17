#### 第二章，变量和简单类型

1. 单行和多行注释

   ```python
   # 单行注释
   print("Hello")
   '''
   多行注释1
   '''
   print("World")
   """
   多行注释2
   """
   ```

   

2. 变量

   变量名命名规则：必须以字母或下划线开头，不能以数字开头

   

3. 数值类型

   整型：十进制、二进制（0b或0B）、八进制（0o或0O）、十六进制（0x或0X）

   浮点型：十进制和科学计数形式

   复数

   ```python
   price = 234_234_234
   f1 = 5.12e2
   ac1 = 3 + 0.2j
   ```

   

4. 字符串

   将数值转换成字符串可以使用str()或repr()

   ```python
   st = "I will play my fife"
   print(st)
   print(repr(st))	# 结果带单引号
   ```

   原始字符串以"r"开头，不会把反斜杠当成特殊字符

   ```python
   s1 = r'G:\publish\codes\02\2.4'
   ```

   字节串

   ```python
   b3 = b'hello'
   b4 = bytes('我爱Python编程', encoding='utf-8')
   b5 = "学习Python很有趣".encoding('utf-8')
   ```

   转义字符：\b\n\r\t

   

5. 字符串格式化

   -：指定左对齐

   +：表示数值带着符号

   0：表示不补空格而是补0

   ```python
   user_name = 'Charlie'
   user_age = '8'
   print("读者名：", user_name, "年龄：", user_age)
   print("读者名：%s 年龄：%s" % (user_name, user_age))
   num = -28
   print("num is: %6d" % num)
   my_value = 3.001415926535
   print("my_value is: %08.3f" % my_value)
   the_name = "Charlie"
   print("the name is: %10.2s" % the_name)
   ```

   

6. 序列相关方法

   字符串是常量，不能改变

   切片

   title()、lower()、upper()

   ```python
   a = 'our domain is crazyit.org'
   print(a.title())
   print(a.lower())
   print(a.upper())
   ```

   strip()、lstrip()、rstrip()

   ```python
   s = ' this is a puppy '
   print(s.lstrip())
   print(s.rstrip())
   print(s.strip())
   s2 = 'i think it is a scarecrow'
   print(s2.lstrip('itow'))
   print(s2.rstrip('itow'))
   print(s2.strip('itow'))
   ```

   startswith()、endswith()、find()、index()、replace()、translate()

   ```python
   s = 'crazyit.org is a good site'
   print(s.startswith('crazyit'))
   print(s.endswith('site'))
   print(s.find('org'))
   print(s.index('org'))
   print(s.find('org', 9))	# -1
   print(s.index('org', 9))	# 引发错误
   print(s.replace('it', 'xxx'))	# 默认全部替换
   print(s.replace('it', 'xxx', 1))	# 替换一个
   table = str.maketrans('abc', '123')
   print(s.translate(table))
   ```

   split()、join()

   ```python
   s = 'crazyit.org is a good site'
   print(s.split())
   print(s.split(None, 2))	# 只分割2次
   print(','.join(s.split()))
   ```

   

7. 位运算符

   左移运算符是左移指定位数，空出的位以0填充

   右移运算符是右移指定位数，空出的位以符号位填充

   

8. 比较运算符

   ```python
   import time
   a = time.gmtime()
   b = time.gmtime()
   print(a == b)
   print(a is b)
   ```

   

9. 三目运算符

   多条语句以英文逗号隔开，每条语句都会执行，返回元组

   多条语句以英文分号隔开，每条语句都会执行，返回第一条语句的返回值

   ```python
   a = 5
   b = 3
   st = "a大于b" if a > b else "a不大于b"
   ```

   

#### 第三章，列表、元组和字典

1. 序列封包和解包

   ```python
   values = 10, 20, 30	# values是元组
   a_tuple = tuple(range(1, 10, 2))
   a, b, c, d, e = a_tuple
   x, y, z = 10, 20, 30
   first, second, *rest = range(10)
   ```

   

2. 增加列表元素

   ```python
   a_list = ['crazyit', 20, -2]
   a_tuple = (3.4, 5.6)
   a_list.append(a_tuple)
   b_list = ['a', 30]
   b_list.extend((-2, 3.1))
   ```

   

3. 删除列表元素

   ```python
   a_list = ['crazyit', 20, -2.4, (3,4), 'fkit']
   del a_list[3]
   del a_list[1: 3]
   b_list = list(range(1, 10))
   del b_list[2: -2: 0]
   name = 'crazyit'
   del name
   c_list = [20, 'crazyit', 30, -4, 'crazyit', 3.4]
   c_list.remove(30)
   c_list.remove('crazyit')	# remove()只删除第一个找到的元素
   c_list.clear()
   ```

   

4. 修改列表元素

   ```python
   b_list = list(range(1, 5))
   b_list[1: 3] = ['a', 'b']
   b_list[2: 2] = ['x', 'y']'
   b_list[2: 5] = []
   b_list[1: 3] = 'Charlie'
   c_list = list(range(1, 10))
   c_list[2: 9: 2] = ['a', 'b', 'c', 'd']	# 如果指定step参数则要求元素个数一一对应
   ```

   

5. 列表的其他方法

   count()、index()、pop()、reverse()、sort()

   ```python
   a_list = [2, 30, 'a', 'b', 'crazyit', 30]
   print(a_list.count(30))
   print(a_list.index(30))
   print(a_list.index(30, 2))
   print(a_list.index(30, 2, 4))
   stack = ['fkit', 'crazyit', 'Charlie']
   print(stack.pop())
   b_list = list(range(1, 8))
   b_list.reverse()
   c_list = ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']
   c_list.sort(key=len, reverse=True)
   ```

   

6. 创建字典

   ```python
   scores = {'语文': 89, '数学': 92, '英语': 93}
   vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
   dict3 = dict(vegetables)
   dict6 = dict(spinach = 1.39, cabbage = 2.59)
   ```

   

7. 字典的常用方法

   clear()、get()、update()

   ```python
   cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
   cars.clear()
   print(cars.get('BMW'))
   print(cars.get('PORSCHE'))	# None
   cars.update({'BMW': 4.5, 'PORSCHE', 9.3})
   ```

   items()、keys()、values()

   ```python
   cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
   ims = cars.items()
   kys = cars.keys()
   vals = cars.values()
   print(list(ims))
   print(list(kys))
   print(list(vals))
   ```

   pop()：获取指定key对应的value，并删除这个key-value对

   popitems()：随机弹出字典中的一个key-value对

   setdefault()：根据key获取value值，如果key不存在，会设置默认的value

   fromkeys()：给多个key创建字典，默认value是None

   ```python
   cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
   print(cars.pop('AUDI'))
   k, v = cars.popitem()
   print(k, v)
   print(cars.setdefault('PORSCHE', 9.2))
   a_dict = dict.fromkeys(['a', 'b'])
   b_dict = dict.fromkeys((13, 17))
   c_dict = dict.fromkeys((13, 17), 'good')
   ```

   

8. 使用字典格式化字符串

   ```python
   temp = '书名是：%(name)s，价格是：%(price)010.2f，出版社是：%(publish)s'
   book = {'name': '疯狂Python讲义', 'price': 78.9, 'publish': '电子社'}
   print(temp % book)
   ```

   

#### 第四章，流程控制

1. if条件的类型

   None、0、""、()、[]、{}会被当作False处理

   

2. 断言

   如果表达式为True，程序可以向下执行，否则会引发AssertionError

   ```python
   s_age = input("请输入您的年龄")
   age = int(s_age)
   assert 20 < age < 80
   print("您输入的年龄在20和80之间")
   ```

   

3. 循环实例，统计列表中各元素出现的次数

   ```python
   src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
   statistics = {}
   for ele in src_list:
       if ele in statistics:
           statistics[ele] += 1
   	else:
           statistics[ele] = 1
   for ele, count in statistics.item():
       print("%s出现的次数为：%d" % (ele, count))
   ```

   

4. 循环使用else

   Python的循环都可以定义else代码块，当循环条件为False时，程序会执行else代码块

   

5. for表达式

   对于使用圆括号的for表达式，它最终返回的是生成器

   ```python
   a_list = [x * x for x in range(10)]
   b_list = [x * x for x in range(10) if x % 2 == 0]
   c_generator = (x * x for x in range(10) if x % 2 ==0)
   d_list = [(x, y) for x in range(5) for y in range(4)]
   ```

   

6. 常用工具函数

   zip()：可以把两个列表压缩成一个zip对象

   reversed()：反序排列，对参数本身无影响

   sorted()：接收一个可迭代对象，返回一个对元素排序的列表

   ```python
   a = ['a', 'b', 'c']
   b = ['1', '2', '3']
   a_list = [x for x in zip(a, b)]
   c = [0.1, 0.2]
   b_list = [x for x in zip(a, c)]
   c_list = [x for x in zip(a, b, c)]
   d = range(10)
   d_list = [x for x in reversed(d)]
   e = [20, 30, -1.2, 3.5, 90, 3.6]
   print(sorted(e, reverse = True))
   f = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
   print(sorted(f, key = len))
   ```

   

#### 第五章，函数和lambda表达式

1. 为函数提供文档

   ```python
   def my_max(x, y):
       '''
       获取两个数值之间较大数的函数
       my_max(x, y)
       	返回x、y两个参数之间较大的那个数
       '''
       z = x if x > y else y
       return z
   help(my_max)
   help(my_max.__doc__)
   ```

   

2. 多个返回值

   函数之间返回多个值会自动封装成元组

   

3. 关键字参数

   ```python
   def girth(width, height):
       pass
   girth(3.5, 4.8)
   girth(width = 3.5, height = 4.8)
   girth(3.5, height = 4.8)
   girth(width, 4.8)	# 报错，关键字参数必须在最后
   ```

   

4. 参数默认值

   ```python
   def say_hi(name = "孙悟空", message = "欢迎来到疯狂软件"):
   	pass
   say_hi("白骨精")
   say_hi(message = "欢迎学习Python")
   say_hi(name = "白骨精", "欢迎学习Python")	# 报错，关键字参数必须在最后
   ```

   定义函数时指定了默认值的参数必须在没有默认值的参数之后

   ```python
   def printTriangle(char, height = 5):
       pass
   ```

   

5. 参数收集

   ```python
   def test1(a, *books):
       pass
   test1(5, "疯狂ISO讲义", "疯狂Android讲义")
   
   ```

   一个函数最多只能带一个支持普通参数收集的形参

   ```python
   def test2(*books, num):
       pass
   test2("疯狂ISO讲义", "疯狂Android讲义", num = 20)
   ```

   关键字参数作为字典

   ```python
   def test3(x, y, z=3, *books, **scores):
       pass
   test3(1, 2, 3, "疯狂ISO讲义", "疯狂Android讲义", 语文 = 89, 数学 = 94)
   ```

   

6. 逆向参数收集

   ```python
   def test4(name, message):
       pass
   my_list = ['孙悟空', '欢迎来到疯狂软件']
   test(*my_list)
   ```

   字典将会以关键字参数形式传入

   ```python
   def bar(book, price, desc):
       pass
   my_dict = {'price': 89, 'book': '疯狂Python讲义', 'desc': '这是一本系统全面的Python学习图书'}
   bar(**my_dict)
   ```

   

7. 变量作用域

   globals()：返回全局范围内所有变量组成的字典

   locals()：返回局部范围内所有变量组成的字典

   vars(object)：获取所有变量组成法人字典

   ```python
   def test():
       age = 20
       print(locals())
       print(locals['age'])
       locals['age'] = 12
       globals()['x'] = 19
   test()
   ```

   局部变量遮蔽全局变量

   ```python
   name = 'Charlie'
   def test():
       print(name)
       name = '孙悟空'	# 会报错，因为全局变量被遮蔽，如果三四行互换则不会报错
   test()
   print(name)
   ```

   解决方法一

   ```python
   name = 'Charlie'
   def test():
       print(globals()[name])
       name = '孙悟空'
   test()
   print(name)
   ```

   解决方法二

   ```python
   name = 'Charlie'
   def test():
       global name
       print(name)
       name = '孙悟空'
   test()
   print(name)
   ```

   

8. 局部函数

   通过nonlocal语句即可声明访问赋值语句只是访问该函数所在函数内部的局部变量

   ```python
   def foo():
       name = 'Charlie'
       def bar():
           nonlocal name
           print(name)
           name = '孙悟空'
       bar()
   foo()
   ```

   

9. 使用函数变量

   把函数本身赋值给变量

   

10. 使用函数作为函数形参

    ```python
    def map(data, fn):
        result = []
        for e in data:
            result.append(fn[e])
        return result
    def square(n):
        return n * n
    def cube(n):
        return n * n * n
    def factorial(n):
        result = 1
        for index in range(2, n+1):
            result *= index
        return result
    data = [3, 4, 9, 5, 8]
    print(map(data, square))
    print(map(data, cube))
    print(map(data, factorial))
    ```

    

11. 使用函数作为返回值

12. lambda表达式

    ```python
    x = map(lambda x: x * x, range(8))
    print([e for e in x])
    y = map(lambda x: x * x if x % 2 == 0 else 0, range(8))
    print([e for e in y])
    ```

    

#### 第六章，类和对象

1. 对象的产生和使用

   为对象动态增加的方法，Python不会自动将调用者自动绑定到第一个参数，需要手动调用

   ```python
   def info(self):
       print("---info函数---", self)
   p.foo = info
   p.foo(p)
   p.bar = lambda self: print('--lambda表达式--', self)
   p.bar(p)
   ```

   如果需要自动绑定，可借助types模块下的MethodType进行包装

   ```python
   def intro_func(self, content):
       print("我是一个人，信息为：%s" % content)
   from types import MethodType
   p.intro = MethodType(intro_func, p)
   p.intro("生活在别处")
   ```

   

2. 类也可以调用实例方法

   ```python
   class Bird:
       def foo():	# 必须没有self参数
           print("Bird空间的foo方法")
       bar = 200
   Bird.foo()
   prinit(Bird.bar)
   ```

   ```python
   class User:
       def walk(self):
           print(self, '正在慢慢地走')
   User.walk('fkit')
   ```

   

3. 类方法和静态方法

   类方法的第一个参数（通常建议参数名为cls）会自动绑定到类本身，静态方法则不会自动绑定

   ```python
   class Bird:
       @classmethod
       def fly(cls):
           print('类方法fly：', cls)
       @staticmethod
       def info(p):
           print('静态方法info：', p)
   Bird.fly()
   Bird.info('crazyit')
   b = Bird()
   b.fly()
   b.info('fkit')
   ```

   

4. 函数装饰器

   ```python
   def funA(fn):
       print('A')
       fn()
       return 'fkit'
   @funA
   def funB():
       print('B')
   print(funB)
   ```

   ```python
   def foo(fn):
       def bar(*args):
           print("==1==", args)
           n = args[0]
           print("==2==", n * (n - 1))
           print(fn.__name__)
           fn(n * (n - 1))
           print("*" * 15)
           return fn(n * (n - 1))
       return bar
   @foo
   def my_test(a):
       print("==my_test函数==", a)
   print(my_test)
   my_test(10)
   my_test(6, 5)
   ```

   ```python
   def auth(fn):
       def auth_fn(*args):
           print("----模拟执行权限检查----")
           fn(*args)
       return auth_fn
   @auth
   def test(a, b):
       print("执行test函数，参数a：%s，参数b：%s" % (a, b))
   test(20, 15)
   ```

   

5. 再论类命名空间

   ```python
   class Item:
       print('正在定义Item类')
       for i in range(10):
           if i % 2 == 0:
               print('偶数：', i)
           else:
               print('奇数：', i)
   ```

   ```python
   global_fn = lambda p: print('执行lambda表达式，p参数：', p)
   class Category:
       cate_fn = lambda p: print('执行lambda表达式，p参数：', p)
   global_fn('fkit')
   c = Category()
   c.cate_fn()
   ```

   

6. 类变量和实例变量

   不管在全局范围内还是函数范围内必须使用类名访问类变量

   ```python
   class Address:
       detail = '广州'
       post_code = '510660'
       def info(self):
           print(detail)	# 报错，不能直接访问类变量
           print(Address.detail)
           print(Address.post_code)
   ```

   通过对象对类变量赋值是定义新的实例变量

   ```python
   class Inventory:
       item = '鼠标'
       quantity = 2000
       def change(self, item, quantity):
           self.item = item
           self.quantity = quantity
   iv = Inventory()
   iv.change('显示器', 500)
   print(iv.item)
   print(iv.quantity)
   print(Inventory.item)
   print(Inventory.quantity)
   ```

   

7. 使用property函数定义属性

   如果类定义了getter、setter等访问器方法，则可以使用property()函数将它们定义成属性

   ```python
   class Rectangle:
       def __init__(self, width, height):
           self.width = width
           self.height = height
       def setsize(self, size):
           self.width, self.height = size
       def getsize(self):
           return self.width, self.height
       def delsize(self):
           self.width, self.height = 0, 0
       size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')
   print(Rectangle.size.__doc__)
   help(Rectangle.size)
   rect = Rectangle(4, 3)
   print(rect.size)
   rect.size = 9, 7
   print(rect.width)
   print(rect.height)
   del rect.size
   print(rect.width)
   print(rect.height)
   ```

   如下代码定义了一个读写属性，该属性不能删除

   ```python
   class User:
       def __init__(self, first, last):
           self.first = first
           self.last = last
       def getfullname(self):
           return self.first + ',' +self.last
       def setfullname(self, fullname):
           first_last = fullname.rsplit(',')
           self.first = first_last[0]
           self.last = first_last[1]
       fullname = property(getfullname, setfullname)
   u = User('悟空', '孙')
   print(u.fullname)
   u.fullname = '八戒,朱'
   print(u.first)
   print(u.last)
   ```

   还可以使用@property装饰器来修饰方法，使之成为属性

   ```python
   class Cell:
       @property
       def state(self):
           return self._state
       @state.setter
       def state(self, value):	# 名字必须要相同
           if 'alive' in value.lower():
               self._state = 'alive'
           else:
               self._state = 'dead'
       @property
       def is_dead(self):
           return not self._state.lower() == 'alive'
   c = Cell()
   c.state = 'Alive'
   print(c.state)
   print(c.is_dead)
   ```

   

8. 隐藏和封装

   ```python
   class User:
       def __hide(self):
           print('示范隐藏的hide方法')
       def getname(self):
           return self.__name
       def setname(self, name):
           if len(name) < 3 or len(name) > 8:
               raise ValueError('用户名长度必须在3～8之间')
           self.__name = name
       name = property(getname, setname)
       def setage(self, age):
           if age < 18 or age > 70:
               raise ValueError('用户名年龄必须在18在70之间')
           self.__age = age
       def getage(self):
           return self.__age
       age = property(getage, setage)
   u = User()
   u.name = 'fkit'
   u.age = 25
   print(u.name)
   print(u.age)
   u._User__hide()
   u._User__name = 'fk'
   print(u.name)
   ```

   

9. 多继承，父类重名方法就近原则

10. 使用未绑定方法调用被重写的方法

    ```python
    class BaseClass:
        def foo(self):
            print('父类中的foo方法')
    class SubClass(BaseClass):
        def foo(self):
            print('子类重写父类中的foo方法')
        def bar(self):
            print('执行bar方法')
            self.foo()
            BaseClass.foo(self)
    sc = SubClass()
    sc.bar()
    ```

    

11. 使用super函数调用父类的构造方法

    子类没有\_\_init()\_\_方法则默认调用父类的\_\_init()\_\_方法

    ```python
    class Employee:
        def __init__(self, salary):
            self.salary = salary
        def work(self):
            print('普通员工正在写代码，工资是：', self.salary)
    class Customer:
        def __init__(self, favorite, address):
            self.favorite = favorite
            self.address = address
        def info(self):
            print('我是一个顾客，我的爱好是：%s，地址是：%s' % (self.favorite, self.address))
    class Manager(Employee, Customer):
        def __init__(self, salary, favorite, address):
            print('--Manager的构造方法--')
            super().__init__(salary)	# super方法没有self参数，就近原则调用
            Customer.__init__(self, favorite, address)
    m = Manager(25000, 'IT产品', '广州')
    m.work()
    m.info()
    ```

    

12. 动态属性与\_\_slots\_\_

    如果希望为所有实例都添加方法，则可以通过为类添加方法来实现

    \_\_slots\_\_属性是一个元组，列出了该类实例允许动态添加的所有属性值和方法名

    \_\_slots\_\_属性并不限制通过类来动态添加属性或方法

    \_\_slots\_\_属性指定的限制只对当前类的实例起作用，对子类不起作用

    ```python
    class Dog:
        __slots__ = ('walk', 'age', 'name')
        def __init__(self, name):
            self.name = name
        def test(self):
            print('预先定义的test方法')
    d = Dog('Snoopy')
    from types import MethodType
    d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
    d.age = 5
    d.walk()
    d.foo = 30  # 报错
    Dog.bar = lambda self: print('abc')
    d.bar()
    ```

    

13. 使用type()函数定义类

    类的类型是type

    ```python
    def fn(self):
        print('fn函数')
    Dog = type('Dog', (object,), dict(walk=fn, age=6))
    d = Dog()
    print(type(d))
    print(type(Dog))
    d.walk()
    print(Dog.age)
    ```

    

14. 使用metaclass批量创建具有某种特征的类

    ```python
    class ItemMetaClass(type):
        def __new__(cls, name, bases, attrs):
            attrs['cal_price'] = lambda self: self.price * self.discount
            return type.__new__(cls, name, bases, attrs)
    class Book(metaclass=ItemMetaClass):
        __slots__ = ('name', 'price', '_discount')
        def __init__(self, name, price):
            self.name = name
            self.price = price
        @property
        def discount(self):
            return self._discount
        @discount.setter
        def discount(self, discount):
            self._discount = discount
    b = Book("疯狂Python讲义", 98)
    b.discount = 0.76
    print(b.cal_price())
    ```

    

15. 检查类型

    issubclass(cls, class_or_tuple)

    isinstance(obj, class_or_tuple)

    \_\_bases\_\_属性和\_\_subclasses\_\_()方法

    ```python
    class A:
        pass
    class B:
        pass
    class C(A, B):
    	pass
    print('类A的所有父类：', A.__bases__)
    print('类B的所有父类：', B.__bases__)
    print('类C的所有父类：', C.__bases__)
    print('类A的所有子类：', A.__subclasses__)
    print('类B的所有子类：', B.__subclasses__)
    ```

    

16. 枚举类

    ```python
    import enum
    Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
    print(Season.SPRING)
    print(Season.SPRING.name)
    print(Season.SPRING.value)
    print(Season['SUMMER'])
    print(Season(3))
    for name, member in Season.__members__.items():
        print(name, '=>', member, ',', member.value)
    print(Season.__members__)	# {'SPRING': <Season.SPRING: 1>, 'SUMMER': <Season.SUMMER: 2>, 'FALL': <Season.FALL: 3>, 'WINTER': <Season.WINTER: 4>}
    ```

    ```python
    import enum
    class Orientation(enum.Enum):
        EAST = '东'
        SOUTH = '南'
        WEST = '西'
        NORTH = '北'
        def info(self):
            print('这是一个代表方向【%s】的枚举' % self.value)
    print(Orientation.SOUTH)
    print(Orientation.SOUTH.value)
    print(Orientation['WEST'])
    print(Orientation('南'))
    Orientation.EAST.info()
    for name, member in Orientation.__members__.items():
        print(name, '=>', member, ',', member.value)
    ```

    

17. 枚举的构造器

    ```python
    import enum
    class Gender(enum.Enum):
        MALE = '男', '阳刚之力'
        FEMALE = '女', '柔顺之美'
        def __init__(self, cn_name, desc):
            self._cn_name = cn_name
            self._desc = desc
        @property
        def desc(self):
            return self._desc
        @property
        def cn_name(self):
            return self._cn_name
    print('FEMALE的name:', Gender.FEMALE.name)
    print('FEMALE的value', Gender.FEMALE.value)
    print('FEMALE的cn_name:', Gender.FEMALE.cn_name)
    print('FEMALE的desc:', Gender.FEMALE.desc)
    ```

    

#### 第七章，异常处理

1. 多异常捕获

   ```python
   import sys
   try:
       a = int(sys.argv[1])
       b = input(sys.argv[2])
       c = a / b
       print("您输入的两个数相除的结果是：", c)
   except (IndexError, ValueError, ArithmeticError):
       print("程序发生了数组越界、数字格式异常、算数异常之一")
   except:
       print("未知异常")
   ```

   

2. 访问异常处理信息

   args：异常的错误编号和描述字符串

   errno：异常的错误编号

   strerror：异常的描述字符串

   ```python
   def foo():
       try:
           fis = open("a.txt")
       except Exception as e:
           print(e.args)
           print(e.errno)
           print(e.strerror)
   foo()
   ```

   

3. else块

   如果希望某段代码的异常能被后面的except块捕获，那么就应该将代码放在try块的代码之后；如果希望某段代码的异常能向外传播，那么就应该将这段代码放在else块中

   ```python
   def else_test():
       s = input('请输入除数：')
       result = 20 / int(s)
       print('20除以%s的结果是：%g' % (s, result))
   def right_main():
       try:
           print('try块的代码，没有异常')
       except:
           print('程序出现异常')
       else:
           else_test()
   def wrong_main():
       try:
           print('try块的代码，没有异常')
           else_test()
       except:
           print('程序出现异常')
   wrong_main()
   right_main()
   ```

   

4. 使用fianlly回收资源

5. 使用raise引发异常

   ```python
   def main():
       try:
           mtd(3)
       except Exception as e:
           print('程序出现异常：', e)
       mtd(3)
   def mtd(a):
       if a > 0:
           raise ValueError("a的值大于0，不符合要求")
   main()
   ```

   

6. except和raise同时使用

   ```python
   class AuctionException(Exception): pass
   class AuctionTest:
       def __init__(self, init_price):
           self.init_price = init_price
       def bid(self, bid_price):
           d = 0.0
           try:
               d = float(bid_price)
           except Exception as e:
               print("转换出异常：", e)
               raise AuctionException("竞拍价必须是数字，不能包含其他字符！")
           if self.init_price > d:
               raise AuctionException("竞拍价比起拍价低，不允许竞拍！")
           initPrice = d
   def main():
       at = AuctionTest(20.4)
       try:
           at.bid("df")
       except AuctionException as ae:
           print('main函数捕获的异常：', ae)
   main()
   ```

   

7. raise不需要参数

   raise语句处于except块中自动引发上下文激活的异常，否则默认引发RuntimeError异常

   

8. Python的异常传播轨迹

   traceback.print_exc()：将异常传播轨迹输出到控制台或者指定文件中

   ```python
   import traceback
   class SelfException(Exception): pass
   def main():
       firstMethod()
   def firstMethod():
       secondMethod()
   def secondMethod():
       thirdMethod()
   def thirdMethod():
       raise SelfException("自定义异常信息")
   try:
       main()
   except:
       traceback.print_exc()
       traceback.print_exc(file=open('log.txt', 'a'))
   ```

   

#### 第八章，Python类的特殊方法

1. 常见的特殊方法

   \_\_repr\_\_()：当程序员直接打印该对象时，系统将会输出该对象的“自我描述”信息

   \_\_del\_\_()：当一个对象被垃圾回收时，Python就会自动调用该对象的\_\_del\_\_方法

   \_\_dir\_\_()：用于列出该对象内部的所有属性和方法名的序列。当对某个对象执行dir(object)时，实际上就是将该对象的\_\_dir\_\_()方法返回值进行排序，然后包装成列表

   \_\_dict\_\_：用于查看对象内部存储的所有属性名和属性值组成的字典

   \_\_getattribute\_\_(self, name)：访问对象的name属性时被自动调用

   \_\_getatt_\_(self, name)：访问对象的name属性且该属性不存在时被自动调用

   \_\_setattr\_\_(self, name, value)：对对象的name属性赋值时被自动调用。不要在\_\_setattr\_\_内再次对属性赋值，会触发死循环

   \_\_delattr\_\_(self, name)：删除对象的name属性时被自动调用

   ```python
   class Rectangle:
       def __init__(self, width, height):
           self.width = width
           self.height = height
       def __setattr__(self, name, value):
           print('----设置%s属性----' % name)
           if name == 'size':
               self.width, self.height = value
           else:
               self.__dict__[name] = value ########
       def __getattr__(self, name):
           print('----读取%s属性----' % name)
           if name == 'size':
               return self.width, self.height
           else:
               raise AttributeError
       def __delattr__(self, name):
           print('----删除%s属性----' % name)
           if name == 'size':
               self.__dict__['width'] = 0  ########
               self.__dict__['height'] = 0 ########
   rect = Rectangle(3, 4)
   print(rect.size)
   rect.size = 6, 8
   print(rect.width)
   del rect.size
   print(rect.size)
   ```

   ```python
   class User:
       def __init__(self, name, age):
           self.name = name
           self.age = age
       def __setattr__(self, name, value):
           if name == 'name':
               if 2 < len(value) <= 8 or len(value) > 8:
                   self.__dict__['name'] = value
               else:
                   raise ValueError('name的长度必须在2～8之间')
           elif name == 'age':
               if 10 < value < 60:
                   self.__dict__['age'] = value
               else:
                   raise ValueError('age值必须在10～60之间')
   u = User('fkit', 24)
   print(u.name)
   print(u.age)
   u.age = 2
   ```

   

2. 13123

   

#### 第九章，模块和包

1. 模块化编程

2. 加载模块

3. 使用包

   包就是一个文件夹，在该文件夹下包含一个\_\_init\_\_.py文件，该文件可用于包含多个模块源文件

   新建一个fk_package包

   fk_package

   |----arithmetic_chart.py

   |----billing.py

   |----print_shape.py

   |----\_\_init\_\_.py

   ```python
   # arithmetic_chart.py
   def print_multiple_chart(n):
       pass
   ```

   ```python
   # billing.py
   class Item:
       def __init__(self, price):
           self.price = price
       def __repr__(self):
           return 'item[price=%g]' % self.price
   ```

   ```python
   # print_shape.py
   def print_blank_triangle(n):
       pass
   ```

   导入包内成员

   ```python
   import fk_package	# 加载并执行包里的__init__.py文件，由于文件内容为空，所以没有任何作用
   import fk_package.print_shape
   from fk_package import billing
   import fk_package.arithmetic_chart
   ```

   编辑\_\_init\_\_.py文件

   ```python
   # __init__.py
   from . import print_shape
   from .print_shape import *
   from . import billing
   from .billing import *
   from . import arithmetic_chart
   from .arithmetic_chart import *
   ```

   理解：fk_package就相当于\_\_init\_\_，因此import fk_package后就可以使用\_\_init\_\_.py文件中导入的函数，即fk_package.print_blank_triangle(3)

4. 查看模块内容

   模块包含什么

   ```python
   >>>import String
   >>>dir(String)
   >>>String.__all__
   ```

   使用\_\_doc\_\_属性查看文档

   ```python
   >>>help(String.capwords)
   >>>print(String.capwords.__doc__)
   ```

   使用\_\_file\_\_属性查看模块的源文件路径

   ```python
   >>>String.__file__
   ```
   



#### 第十章，常见模块

1. sys

2. os

3. random

   ```python
   random.randint(a, b)
   random.choice(seq)
   random.choices(seq, weights = None, *, cum_weights = None, k = 1)	# random.choices(['Python', 'Swift', 'Kotlin'], [5, 5, 1], k = 6)
   random.shuffle(x[, random])
   random.sample(population, k)
   random.random()
   random.uniform(a, b)
   ```

4. time

   time.struct_time类代表一个时间对象，包含9个属性tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday(一年内第几天), tm_isdst(夏令时)

   ```python
   time.asctime([t])
   
   ```

   

5. JSON支持

   JSON的全称是JavaScript Object Notation，即JavaScript对象符号

   使用JSON语法创建JavaScript对象

   ```javascript
   person = 
   {
   	name : 'yeeku',
       gender : 'male',
       son : {
           name : 'tiger',
           grade : 1
       }
       info : function()
       {
           console.log("姓名：" + this.name + "性别：" + this.sex);
       }
   }
   ```

   使用JSON语法创建数组

   ```javascript
   var a = ['yeeku', 'nono'];
   ```

   Python的JSON支持

   ```mermaid
   graph LR
   	A[JSON字符串] -->|"decode(用load或loads)"| B[Python对象]
   	B -->|"encode(用dump或dumps)"| A
   ```

   

   ```python
   import json
   s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
   s2 = json.dumps("\"foo\bar")
   s3 = json.dumps('\\')
   s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys = True)
   s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators = (',', ':'))
   s6 = json.dumps({'Python': 5, 'Kotlin': 7}, sort_keys = True, indent = 4)	# indent是缩进并且换行
   s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
   f = open('a.json', 'w')
   json.dump(['Kotlin', {'Python': 'excellent'}], f)
   ```

   ```python
   import json
   result1 = json.loads('["yeeku", {"favorite": ["coding", null, "games", 25]]')
   result2 = json.loads('"\\"foo\\"bar"')
   def as_complex(dct):
       if '__complex__' in dct:
           return complex(dct['real'], dec['imag'])
       return dct
   result3 = json.loads('("__complex__": True, "real": 1, "imag": 2)', object_hook = as_complex)
   f = open('a.json')
   result4 = json.load(f)
   ```

   ```python
   import json
   class ComplexEncoder(json.JSONEncoder):
       def default(self, obj):
           if isinstance(obj ,complex):
               return {"__complex__": 'ture', "real": obj.real, 'imag': obj.imag}
           return json.JSONEncoder.default(self, obj)
   s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
   s2 = ComplexEncoder().encode(2 + 1j)
   ```

   

6. 正则表达式

   re.compile预编译正则表达式，也可以不预编译

   match()必须从字符串开始处匹配，search()不须要

   ```python
   import re
   m1 = re.match('www', 'www.fkit.org')
   m2 = re.search('www', 'www.fkit.com')
   m3 = re.search('fkit', 'www.fkit.com')
   print(m1.span())
   print(m1.group())
   print(m2.span())
   print(m2.group())
   print(m3.span())
   print(m3.group())
   print(re.match('fkit', 'www.fkit.com'))
   ```

   findall()返回列表，finditer()返回迭代器

   ```python
   import re
   print(re.findall('fkit', 'FkIt is very good, Fkit.org is my favourite', re.I))	# re.I式匹配对大小写不敏感
   it = re.finditer('fkit', 'FkIt is very good, Fkit.org is my favourite', re.I)
   for e in it:
       print(str(e.span()) + "-->" + e.group())
   ```

   fullmatch()要求整个字符串能匹配pattern，sub()用于将所有匹配pattern的内容替换

   ```python
   import re
   my_date = '2008-08-18'
   print(re.sub(r'-', '/', my_date))	# r代表原始字符串
   print(re.sub(r'-', '/', my_date, 1))
   ```

   ```python
   import re
   def fun(matched):
       value = "《疯狂" + (matched.group('lang')) + "讲义》"
       return value
   s = 'Python很好，Kotlin也很好'
   print(re.sub(r'(?P<lang>\w+)', fun, s, flags = re.A))	# ?P<lang>为该组起名为lang，re.A表示\w只能代表ASCII字符，不能代表汉字
   ```

   re.split()使用pattern对string进行分割

   ```python
   import re
   print(re.split(',', 'fkit, fkjava, crazyit'))
   print(re.split(',', 'fkit, fkjava, crazyit', 1))
   print(re.split('a', 'fkit, fkjava, crazyit'))
   print(re.split('x', 'fkit, fkjava, crazyit'))
   ```

   re.escape()对模式中除ASCII字符、数值、下划线之外的其他字符进行转义

   ```python
   import re
   print(re.escape(r'www.crazyit.org is good, i love it!'))
   print(re.escape(r'A-Zand0-9?'))
   ```

   正则表达式对象是调用re.compile函数的返回值，Match对象是match()和search()方法的返回值


   ```python
   import re
   pa = re.compile('fkit')
   print(pa.match('www.fkit.org', 4).span())
   print(pa.match('www.fkit.org', 4, 6))
   print(pa.match('www.fkit.org', 4, 8).span())
   ```

   ```python
   import re
   m = re.search(r'(fkit).(org)', r"www.fkit.org is a good domain")
   print(m.group(0))	# 0是整个正则表达式
   print(m[0])
   print(m.span(0))
   print(m.group(1))
   print(m[1])
   print(m.span(1))
   print(m.group(2))
   print(m[2])
   print(m.span(2))
   print(m.groups())
   m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)', r"www.fkit.org is a good domain")	# 为正则表达式的组指定名字
   print(m2.groupdict())
   ```

| 特殊字符 |                        说明                        |
| :------: | :------------------------------------------------: |
|    $     |                   匹配一行的结尾                   |
|    ^     |                   匹配一行的开头                   |
|    *     |             前面子表达式出现零次或多次             |
|    +     |             前面子表达式出现一次或多次             |
|    ?     |             前面子表达式出现零次或一次             |
|    .     | 匹配除\n外任意单个字符，使用re.S后还可以匹配换行符 |
|    \|    |                指定两项之间任选一项                |

| 预定义字符 |                            说明                            |
| :--------: | :--------------------------------------------------------: |
|     \d     |                        匹配0~9数字                         |
|     \D     |                         匹配非数字                         |
|     \s     | 匹配所有空白字符，包括空格、制表符、回车符、换页符、换行符 |
|     \S     |                      匹配所有非空白符                      |
|     \w     |  匹配所有单词字符，包括0~9所有数字、26个英文字母和下划线   |
|     \W     |                     匹配所有非单词字符                     |

| 方括号表达式 | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| 表示枚举     | 例如[abc]表示a、b、c中任意一个字符                           |
| 表示范围     | 例如[a-f]表示a\~f范围内的任意字符。[a-cx-z]表示a\~c、x\~z范围内的任意字符 |
| 表示求否：^  | 例如\[\^abc]表示非a、b、c的任意字符。\[^a-f]表示不是a~f范围内的任意字符 |

| 边界匹配符 | 说明                                   |
| ---------- | -------------------------------------- |
| \b         | 单词的边界，只能匹配单词前后的空白     |
| \B         | 非单词的边界只能匹配不在单词前后的空白 |
| \A         | 只匹配字符串的开头                     |
| \Z         | 只匹配字符串的结尾                     |

   {}表示出现的次数。频度限定之后加问号贪婪模式变勉强模式

   

7. 容器相关类

   frozenset是set的不可变版本，它的元素是不可变的

   ```python
   c = {'白骨精'}
   c.add("孙悟空")
   c.add(6)
   print("c集合的元素个数为:" , len(c))
   c.remove(6)
   print("c集合的元素个数为:" , len(c))
   print("c集合是否包含'孙悟空'字符串:" , ("孙悟空" in c))
   c.add("轻量级Java EE企业应用实战")
   print("c集合的元素：" , c)
   books = set()
   books.add("轻量级Java EE企业应用实战")
   books.add("疯狂Java讲义")
   print("books集合的元素：" , books)
   print("books集合是否为c的子集合？", books.issubset(c))
   print("books集合是否为c的子集合？", (books <= c))
   print("c集合是否完全包含books集合？", c.issuperset(books))
   print("c集合是否完全包含books集合？", (c >= books))
   result1 = c - books
   print(result1)
   result2 = c.difference(books)
   print(result2)
   c.difference_update(books)
   print("c集合的元素：" , c)
   c.clear()
   print("c集合的元素：" , c)
   d = {"疯狂Java讲义", '疯狂Python讲义', '疯狂Kotlin讲义'}
   print("d集合的元素：" , d)
   inter1 = d & books
   print(inter1)
   inter2 = d.intersection(books)
   print(inter2)
   d.intersection_update(books)
   print("d集合的元素：" , d)
   e = set(range(5))
   f = set(range(3, 7))
   print("e集合的元素：" , e)
   print("f集合的元素：" , f)
   xor = e ^ f
   print('e和f执行xor的结果：', xor)
   un = e.union(f)
   print('e和f执行并集的结果：', un)
   e.update(f)
   print('e集合的元素：', e)
   ```

   <=相当于issubset()，判断子集合

   \>=相当于issuperset()，判断父集合

   -相当于用difference()

   &相当于intersection()，交集

   ^，并集减交集

   交集intersection()和intersection_update()，前者不改变集合本身，后者改变第一个集合

   并集union()和update()前者不改变集合本身，后者改变第一个集合

   减法difference()和difference_update()，前者不改变集合本身，后者改变第一个集合

   双端队列的方法：append()、appendleft()、pop()、popleft()、extend()、extendleft()

   ```python
   from collections import deque
   stack = deque(('Kotlin', 'Python'))
   stack.append('Erlang')
   stack.append('Swift')
   print('stack中的元素：', stack)
   print(stack.pop())
   print(stack.pop())
   print(stack)
   ```

   ```python
   from collections import deque
   q = deque(('Kotlin', 'Python'))
   q.append('Erlang')
   q.append('Swift')
   print('q中的元素：', q)
   print(q.popleft())
   print(q.popleft())
   print(q)
   ```

   ```python
   from collections import deque
   q = deque(range(5))
   print('q中的元素：', q)
   q.rotate()
   print('q中的元素：', q)
   q.rotate()
   print('q中的元素：', q)
   ```

   heapq类堆操作

   heappush(heap, item)

   heappop(heap)

   heapify(heap)

   heapreplace(heap, x)最小元素弹出，并将元素x入堆

   merge(*iterables, key=None, reverse=False)多个有序堆合并成大的有序堆

   heappushpop(heap, item)item入堆，然后弹出并返回堆中最小的元素

   nlargest(n, iterable, key=None)

   nsmallest(n, iterable, key=None)

   ```python
   from heapq import *
   my_data = list(range(10))
   my_data.append(0.5)
   print('my_data的元素：', my_data)
   heapify(my_data)
   print('应用堆之后my_data的元素：', my_data)
   heappush(my_data, 7.2)
   print('添加7.2之后my_data的元素：', my_data)
   print(heappop(my_data)) # 0
   print(heappop(my_data)) # 0.5
   print('弹出两个元素之后my_data的元素：', my_data)
   print(heapreplace(my_data, 8.1))
   print('执行replace之后my_data的元素：', my_data)
   print('my_data中最大的3个元素：', nlargest(3, my_data))
   print('my_data中最小的4个元素：', nsmallest(4, my_data))
   ```

   

8. 123

9. 123



#### 第十二章，文件I/O

1. pathlib模块

   ```mermaid
   graph BT
   	PurePosixPath --> PurePath
   	PosixPath --> Path --> PurePath
   	WindowsPath --> Path
   	PureWindowsPath --> PurePath
   ```

   PurePath自动拼接字符串

   ```python
   from pathlib import *
   pp = PurePath('setup.py')
   print(type(pp))
   pp = PurePath('crazyit', 'some/path', 'info')
   print(pp)
   pp = PurePath(Path('crazyit'), Path('info'))
   print(pp)
   pp = PurePosixPath('crazyit', 'some/path', 'info')
   print(pp)
   pp = PurePath()
   print(pp)
   pp = PurePosixPath('/etc', '/usr', 'lib64')
   print(pp)
   pp = PureWindowsPath('c:/Windows', 'd:info')
   print(pp)
   pp = PureWindowsPath('c:/Windows', '/Program Files')
   print(pp)
   pp = PurePath('foo//bar')
   print(pp)
   pp = PurePath('foo/./bar')
   print(pp)
   pp = PurePath('foo/../bar')
   print(pp)
   ```

   UNIX区分大小写，Windows不区分

   ```python
   print(PurePosixPath('info') == PurePosixPath('INFO'))
   print(PureWindowsPath('info') == PureWindowsPath('INFO'))
   print(PurePosixPath('D:') < PurePosixPath('c:'))
   print(PureWindowsPath('D:') > PureWindowsPath('c'))
   print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))
   # print(PureWindowsPath('info') < PurePosixPath('info'))
   ```

   PurePath对象通过“/”进行拼接

   ```python
   pp = PureWindowsPath('abc')
   print(pp / 'xyz' / 'wawa')
   pp = PurePosixPath('abc')
   print(pp / 'xyz' / 'wawa')
   pp2 = PurePosixPath('haha', 'hehe')
   print(pp / pp2)
   ```

   转str

   ```python
   pp = PureWindowsPath('abc', 'xyz', 'wawa')
   print(str(pp))
   pp = PurePosixPath('abc', 'xyz', 'swawa')
   print(str(pp))
   ```

   PurePath的属性和方法：

   drive、root和anchor分别表示盘符、根路径、盘符和根路径

   parents和parent是父路径，parents[0]，parents[1]

   name是文件名

   suffix是后缀，stem是文件名（不带后缀）

   match(pattern)判断当前路径是否匹配指定通配符

   with_name(name)当前路径文件名替换成新文件名

   with_suffix(suffix)当前路径文件后缀名替换成新后缀名

   ```python
   from pathlib import *
   
   p = Path('.')
   for x in p.iterdir():
       print(x)
   p = Path('../')
   for x in p.glob('**/*.py'):
       print(x)
   p = Path('g:/publish/codes')
   for x in p.glob('**/Path_test1.py'):
       print(x)
   ```

   ```python
   from pathlib import *
   
   p = Path('a_test.txt')
   result = p.write_text('''有一个美丽的新世界
   它在远方等我
   哪里有天真的孩子
   还有姑娘的酒窝''', encoding='GBK')
   print(result)
   content = p.read_text(encoding='GBK')
   print(content)
   bb = p.read_bytes()
   print(bb)
   ```

   

2. 使用os.path操作目录

   ```python
   import os
   import time
   
   print(os.path.abspath("abc.txt"))
   print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
   print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))
   print(os.path.dirname('abc/xyz/README.txt'))
   print(os.path.exists('abc/xyz/README.txt'))
   print(time.ctime(os.path.getatime('os.path_test.py')))
   print(time.ctime(os.path.getmtime('os.path_test.py')))
   print(time.ctime(os.path.getctime('os.path_test.py')))
   print(os.path.getsize('os.path_test.py'))
   print(os.path.isfile('os.path_test.py'))
   print(os.path.isdir('os.path_test.py'))
   print(os.path.samefile('os.path_test.py', './os.path_test.py'))
   ```

   

3. 使用fnmatch处理文件名匹配

   fnmatch匹配的通配符：*，?，[字符序列]，[!字符序列]

   fnmatch.fnmatch(filename, pattern)

   fnmatch.fnmatchcase(filename, pattern)

   fnmatch.filter(names, pattern)

   fnmatch.trasnslate(pattern)

   ```python
   from pathlib import *
   import fnmatch
   for file in Path('.').iterdir():
       if fnmatch.fnmatch(file, '*_test.PY'):
           print(file)
           
   names = ['a.py', 'b.py', 'c.py', 'd.py']
   sub = fnmatch.filter(names, '[ac].py')
   print(sub)
   
   print(fnmatch.translate('?.py'))
   print(fnmatch.translate('[ac].py'))
   print(fnmatch.translate('[a-c].py'))
   ```

   

4. 打开文件

   open(file_name [, access_mode], [, buffering])

   ```python
   f = open('open_test.py')
   print(f.encoding)
   print(f.mode)
   print(f.closed)
   print(f.name)
   ```

   文件打开模式：r，w，a，+，b

   

5. 读取文件

   使用open()函数打开文本文件时，程序使用当前操作系统的字符集。使用codecs模块的open()函数打开文件允许指定字符集

   ```python
   f = open("test.txt", 'r', True)
   while True:
       ch = f.read(1)
       if not ch: break
       print(ch, end='')
   f.close()
   ```

   ```python
   f = open("test.txt", 'r', True)
   print(f.read())
   f.close()
   ```

   ```python
   f = open("test.txt", 'rb', True)
   print(f.read().decode('utf-8'))
   f.close()
   ```

   ```python
   import codecs
   f = codecs.open("read_test4.py", 'r', 'utf-8', buffering=True)
   while True:
       ch = f.read(1)
       if not ch: break
       print(ch, end='')
   f.close()
   ```

   ```python
   import codecs
   f = codecs.open("readline_test.py", 'r', 'utf-8', buffering=True)
   while True:
       line = f.readline()
       if not line: break
       print(line, end='')
   f.close()
   ```

   ```python
   import codecs
   f = codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True)
   for l in f.readlines():
       print(l, end='')
   f.close()
   ```

   ```python
   import fileinput
   for line in fileinput.input(files=('info.txt', 'test.txt')):
       print(fileinput.filename(), fileinput.filelineno(), line, end='')
   fileinput.close()
   ```

   ```python
   import codecs
   f = codecs.open("for_file.py", 'r', 'utf-8', buffering=True)
   for line in f:
       print(line, end='')
   f.close()
   ```

   ```python
   import sys
   for line in sys.stdin:
       print("用户输入：", line, end='')
   ```

   ```python
   import sys
   import re
   mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
       + '[\.][a-z]{2,3}([\.][a-z]{2})?'
   text = sys.stdin.read()
   it = re.finditer(mailPattern, text, re.I)
   for e in it:
       print(str(e.span()) + "-->" + e.group())
   ```

   ```python
   import codecs
   with codecs.open("readlines_test.py", "r", 'utf-8', buffering=True) as f:
       for line in f:
           print(line, end='')
   ```

   ```python
   import fileinput
   with fileinput.input(files=('test.txt', 'info.txt')) as f:
       for line in f:
           print(line, end='')
   ```

   with语句略

   

6. 写文件

   文件对象提供的方法：

   seek(offset [, where])：where为1时代表从文件头，where为1时代表从当前位置，where为2时代表从文件尾

   tell()：文件指针的位置

   ```python
   f = open('filept_test.py', 'rb')
   print(f.tell())
   f.seek(3)
   print(f.tell())
   print(f.read(1))
   print(f.tell())
   f.seek(5)
   print(f.tell())
   f.seek(5, 1)
   print(f.tell())
   f.seek(-10, 2)
   print(f.tell())
   print(f.read(1))
   ```

   ```python
   import os
   f = open('x.txt', 'a+')
   f.write('我爱Python' + os.linesep)
   f.writelines(('土门壁甚坚' + os.linesep,
                '杏园度亦难。' + os.linesep,
                '势亦邺城下，' + os.linesep,
                '纵死时犹宽。' + os.linesep))
   ```

   ```python
   import os
   f = open('y.txt', 'wb+')
   f.write(('我爱Python' + os.linesep).encode('utf-8'))
   f.writelines((('土门壁甚坚' + os.linesep).encode('utf-8'),
                ('杏园度亦难。' + os.linesep).encode('utf-8'),
                ('势亦邺城下，' + os.linesep).encode('utf-8'),
                ('纵死时犹宽。' + os.linesep).encode('utf-8'))
   ```

   

7. 123

