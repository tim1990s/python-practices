# Lập Trình Hướng Đối Tượng Trong Python

Tài liệu này hệ thống lại các kiến thức chính về OOP trong Python theo hướng dễ hiểu, có ví dụ và phù hợp cho người học từ cơ bản đến nâng cao.

Mỗi phần gồm:

- Khái niệm
- Khi nào dùng
- Ví dụ code Python
- Lỗi thường gặp
- Ghi nhớ ngắn gọn

---

## 1. Khái Niệm Lập Trình Hướng Đối Tượng Là Gì

### Khái niệm

OOP, hay lập trình hướng đối tượng, là cách tổ chức chương trình xoay quanh các đối tượng. Mỗi đối tượng thường có dữ liệu và hành vi riêng.

- Dữ liệu được gọi là thuộc tính.
- Hành vi được gọi là phương thức.

Ví dụ thực tế: một học sinh có tên, tuổi, điểm số và có thể thêm điểm, tính điểm trung bình, in thông tin.

### Khi nào dùng

Dùng OOP khi chương trình có nhiều thực thể cần quản lý, ví dụ học sinh, tài khoản ngân hàng, sản phẩm, đơn hàng, nhân viên, nhân vật game.

### Ví dụ code Python

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Tôi là {self.name}, {self.age} tuổi")


student = Student("An", 18)
student.introduce()
```

### Lỗi thường gặp

- Tạo class nhưng class không có hành vi rõ ràng.
- Ép mọi bài toán thành class dù chỉ cần function đơn giản.

### Ghi nhớ ngắn gọn

OOP giúp gom dữ liệu và hành vi liên quan vào cùng một nơi.

---

## 2. Class Và Object Trong Python

### Khái niệm

`class` là khuôn mẫu. `object` là đối tượng cụ thể được tạo ra từ class.

### Khi nào dùng

Dùng class khi bạn cần tạo nhiều đối tượng có chung cấu trúc và hành vi.

### Ví dụ code Python

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def run(self):
        print(f"{self.brand} đang chạy")


car1 = Car("Toyota")
car2 = Car("Honda")

car1.run()
car2.run()
```

### Lỗi thường gặp

- Nhầm class với object. `Car` là class, `car1` là object.
- Gọi instance method trực tiếp từ class mà không truyền object.

### Ghi nhớ ngắn gọn

Class giống bản thiết kế, object là sản phẩm thật tạo từ bản thiết kế đó.

---

## 3. Thuộc Tính Instance Và Thuộc Tính Class

### Khái niệm

Instance attribute thuộc về từng object riêng. Class attribute thuộc về class và được chia sẻ bởi tất cả object của class đó.

### Khi nào dùng

- Dùng instance attribute cho dữ liệu riêng của từng object.
- Dùng class attribute cho dữ liệu chung của cả class.

### Ví dụ code Python

```python
class Student:
    school_name = "ABC School"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute


s1 = Student("An")
s2 = Student("Bình")

print(s1.name)
print(s2.name)
print(Student.school_name)
```

### Lỗi thường gặp

Dùng class attribute cho dữ liệu mutable như list hoặc dict mà thực ra mỗi object cần một bản riêng.

```python
class BadClass:
    items = []  # tất cả object dùng chung list này
```

Cách đúng:

```python
class GoodClass:
    def __init__(self):
        self.items = []
```

### Ghi nhớ ngắn gọn

Dữ liệu riêng đặt trong `self`, dữ liệu chung đặt ở cấp class.

---

## 4. Instance Method, Class Method, Static Method

### Khái niệm

- Instance method nhận `self`, thao tác với object.
- Class method nhận `cls`, thao tác với class.
- Static method không nhận `self` hay `cls`, thường là hàm tiện ích liên quan đến class.

### Khi nào dùng

- Instance method: khi cần đọc/sửa dữ liệu của object.
- Class method: khi cần xử lý dữ liệu cấp class hoặc tạo constructor phụ.
- Static method: khi logic có liên quan về mặt ý nghĩa nhưng không cần truy cập object/class.

### Ví dụ code Python

```python
class User:
    user_count = 0

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    def say_hello(self):
        print(f"Hello, {self.name}")

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 2


u = User("An")
u.say_hello()
print(User.get_user_count())
print(User.is_valid_name("A"))
```

### Lỗi thường gặp

- Dùng `@staticmethod` cho method cần truy cập dữ liệu object.
- Quên tham số `self` trong instance method.
- Trong class method lại gọi thẳng tên class thay vì dùng `cls`.

### Ghi nhớ ngắn gọn

Cần object thì dùng `self`, cần class thì dùng `cls`, không cần cả hai thì có thể dùng static method.

---

## 5. Constructor `__init__`

### Khái niệm

`__init__` là method được gọi sau khi object được tạo, dùng để khởi tạo trạng thái ban đầu.

### Khi nào dùng

Dùng khi object cần có dữ liệu ban đầu hợp lệ ngay sau khi được tạo.

### Ví dụ code Python

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


account = BankAccount("An", 1000)
print(account.owner)
print(account.balance)
```

### Lỗi thường gặp

- Nghĩ `__init__` tạo object. Thực tế object được tạo trước, `__init__` chỉ khởi tạo dữ liệu.
- Dùng giá trị mutable làm default:

```python
class Student:
    def __init__(self, scores=[]):  # không nên
        self.scores = scores
```

Cách an toàn hơn:

```python
class Student:
    def __init__(self, scores=None):
        self.scores = scores or []
```

### Ghi nhớ ngắn gọn

`__init__` là nơi đặt object vào trạng thái sẵn sàng sử dụng.

---

## 6. `self` Là Gì Và Cách Sử Dụng

### Khái niệm

`self` là tham chiếu đến object hiện tại. Nó giúp method truy cập thuộc tính và method của chính object đang được gọi.

### Khi nào dùng

Dùng trong instance method bất cứ khi nào cần làm việc với dữ liệu của object.

### Ví dụ code Python

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} sủa gâu gâu")


dog = Dog("Milu")
dog.bark()
```

### Lỗi thường gặp

Quên khai báo `self`:

```python
class Bad:
    def hello():  # sai nếu gọi qua object
        print("Hello")
```

### Ghi nhớ ngắn gọn

Muốn object nhớ và xử lý dữ liệu của chính nó, dùng `self`.

---

## 7. Encapsulation - Tính Đóng Gói

### Khái niệm

Đóng gói là che giấu chi tiết bên trong object và kiểm soát cách bên ngoài truy cập hoặc sửa dữ liệu.

### Khi nào dùng

Dùng khi dữ liệu cần được bảo vệ khỏi việc gán giá trị sai, ví dụ số dư tài khoản, giá sản phẩm, mật khẩu.

### Ví dụ code Python

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp phải dương")
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```

### Lỗi thường gặp

- Cho phép sửa trực tiếp dữ liệu quan trọng.
- Tạo getter/setter máy móc cho mọi attribute dù không có logic kiểm soát.

### Ghi nhớ ngắn gọn

Đóng gói giúp object tự bảo vệ dữ liệu của nó.

---

## 8. Public, Protected, Private Attribute

### Khái niệm

Python không có private tuyệt đối như một số ngôn ngữ khác, nhưng có quy ước:

- `name`: public, có thể truy cập từ bên ngoài.
- `_name`: protected theo quy ước, chỉ nên dùng nội bộ class hoặc subclass.
- `__name`: private-like, Python sẽ name mangling thành `_ClassName__name`.

### Khi nào dùng

- Public: dữ liệu/hành vi an toàn cho người dùng class.
- Protected: chi tiết nội bộ nhưng subclass có thể cần.
- Private-like: chi tiết nội bộ không muốn class con vô tình ghi đè.

### Ví dụ code Python

```python
class User:
    def __init__(self):
        self.name = "An"
        self._role = "member"
        self.__password = "123"

    def check_password(self, password):
        return password == self.__password
```

### Lỗi thường gặp

- Nghĩ `__password` là private tuyệt đối.
- Truy cập `_role` từ bên ngoài quá nhiều, làm phá vỡ đóng gói.

### Ghi nhớ ngắn gọn

Python dựa nhiều vào quy ước: thấy dấu `_` thì hiểu đó là chi tiết nội bộ.

---

## 9. Getter, Setter Và `@property`

### Khái niệm

Getter lấy dữ liệu. Setter kiểm soát việc gán dữ liệu. `@property` giúp gọi method như attribute.

### Khi nào dùng

Dùng khi cần validate dữ liệu mà vẫn muốn API bên ngoài gọn đẹp.

### Ví dụ code Python

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá không được âm")
        self.__price = value


p = Product(100)
p.price = 200
print(p.price)
```

### Lỗi thường gặp

Trong setter gán lại `self.price = value`, gây đệ quy vô hạn.

```python
@price.setter
def price(self, value):
    self.price = value  # sai
```

### Ghi nhớ ngắn gọn

`@property` giúp object trông như đang dùng attribute, nhưng vẫn có validation bên trong.

---

## 10. Inheritance - Kế Thừa

### Khái niệm

Kế thừa cho phép class con tái sử dụng thuộc tính và method của class cha.

### Khi nào dùng

Dùng khi có quan hệ "là một". Ví dụ `Dog` là một `Animal`, `Manager` là một `Employee`.

### Ví dụ code Python

```python
class Animal:
    def eat(self):
        print("Đang ăn")


class Dog(Animal):
    def bark(self):
        print("Gâu gâu")


dog = Dog()
dog.eat()
dog.bark()
```

### Lỗi thường gặp

Dùng kế thừa cho quan hệ "có một". Ví dụ `Car` không nên kế thừa `Engine`; `Car` có `Engine`.

### Ghi nhớ ngắn gọn

Chỉ kế thừa khi class con thực sự là một dạng của class cha.

---

## 11. Overriding - Ghi Đè Phương Thức

### Khái niệm

Overriding là việc class con định nghĩa lại method đã có ở class cha.

### Khi nào dùng

Dùng khi class con cần hành vi riêng.

### Ví dụ code Python

```python
class Animal:
    def make_sound(self):
        print("Âm thanh chung")


class Cat(Animal):
    def make_sound(self):
        print("Meo meo")


cat = Cat()
cat.make_sound()
```

### Lỗi thường gặp

- Ghi đè làm mất logic quan trọng của class cha.
- Signature của method con khác quá nhiều so với method cha.

### Ghi nhớ ngắn gọn

Overriding giúp class con tùy biến hành vi thừa hưởng.

---

## 12. `super()` Trong Python

### Khái niệm

`super()` dùng để gọi method của class cha theo thứ tự MRO.

### Khi nào dùng

Dùng khi class con muốn mở rộng logic của class cha thay vì viết lại toàn bộ.

### Ví dụ code Python

```python
class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


m = Manager("An", "IT")
print(m.name, m.department)
```

### Lỗi thường gặp

Quên gọi `super().__init__()`, khiến thuộc tính của class cha không được khởi tạo.

### Ghi nhớ ngắn gọn

`super()` giúp tái sử dụng logic class cha và rất quan trọng khi có kế thừa nhiều lớp.

---

## 13. Multiple Inheritance - Đa Kế Thừa

### Khái niệm

Đa kế thừa là một class kế thừa từ nhiều class cha.

### Khi nào dùng

Dùng khi một class cần kết hợp nhiều năng lực riêng biệt. Nên dùng cẩn thận, nhất là khi các class cha có method trùng tên.

### Ví dụ code Python

```python
class Flyable:
    def fly(self):
        print("Có thể bay")


class Swimmable:
    def swim(self):
        print("Có thể bơi")


class Duck(Flyable, Swimmable):
    pass


duck = Duck()
duck.fly()
duck.swim()
print(Duck.mro())
```

### Lỗi thường gặp

- Tạo cây kế thừa quá phức tạp.
- Không hiểu MRO nên method được gọi khác với dự đoán.

### Ghi nhớ ngắn gọn

Đa kế thừa mạnh, nhưng nên ưu tiên mixin nhỏ, rõ trách nhiệm.

---

## 14. Polymorphism - Tính Đa Hình

### Khái niệm

Đa hình là việc nhiều object khác nhau có thể được xử lý qua cùng một interface. Trong Python, nếu object có method cần thiết thì có thể dùng, không cần cùng class.

### Khi nào dùng

Dùng khi muốn viết function làm việc với nhiều loại object khác nhau nhưng cùng hành vi.

### Ví dụ code Python

```python
class Dog:
    def speak(self):
        return "Gâu"


class Cat:
    def speak(self):
        return "Meo"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())
```

### Lỗi thường gặp

- Kiểm tra `type()` quá nhiều thay vì dựa vào hành vi của object.
- Đặt interface không nhất quán giữa các class.

### Ghi nhớ ngắn gọn

Đa hình trong Python thường đi kèm duck typing: có method đúng là có thể dùng.

---

## 15. Abstraction - Tính Trừu Tượng

### Khái niệm

Trừu tượng là che bớt chi tiết triển khai, chỉ để lộ những hành vi cần thiết cho người dùng class.

### Khi nào dùng

Dùng khi một quy trình có nhiều bước nội bộ, nhưng bên ngoài chỉ cần gọi một method đơn giản.

### Ví dụ code Python

```python
class CoffeeMachine:
    def make_coffee(self):
        self._boil_water()
        self._brew()

    def _boil_water(self):
        print("Đun nước")

    def _brew(self):
        print("Pha cà phê")


machine = CoffeeMachine()
machine.make_coffee()
```

### Lỗi thường gặp

Bắt người dùng class phải gọi quá nhiều bước chi tiết theo đúng thứ tự.

### Ghi nhớ ngắn gọn

Class tốt nên cung cấp interface đơn giản và giấu chi tiết phức tạp bên trong.

---

## 16. Abstract Base Class Với `abc`

### Khái niệm

Abstract Base Class định nghĩa interface bắt buộc class con phải triển khai.

### Khi nào dùng

Dùng khi bạn cần một khuôn mẫu chung cho nhiều class con.

### Ví dụ code Python

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r = Rectangle(4, 5)
print(r.area())
```

### Lỗi thường gặp

Class con quên triển khai abstract method, dẫn đến không tạo object được.

### Ghi nhớ ngắn gọn

ABC giúp ép class con tuân thủ interface chung.

---

## 17. Magic Methods / Dunder Methods

### Khái niệm

Magic methods là các method có dạng `__method__`. Chúng giúp object của bạn tương tác tự nhiên với Python.

### Khi nào dùng

Dùng khi muốn object hỗ trợ:

- `print(obj)` qua `__str__`
- debug qua `__repr__`
- `len(obj)` qua `__len__`
- so sánh qua `__eq__`
- phép cộng qua `__add__`

### Ví dụ code Python

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} VND"

    def __repr__(self):
        return f"Money({self.amount})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)


m1 = Money(100)
m2 = Money(200)

print(m1)
print(repr(m1))
print(m1 == m2)
print(m1 + m2)
```

Ví dụ `__len__`:

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["An", "Bình"])
print(len(team))
```

### Lỗi thường gặp

- `__repr__` không hữu ích cho debugging.
- Trong `__eq__`, không xử lý trường hợp object khác kiểu.
- `__add__` trả về kiểu dữ liệu không nhất quán.

### Ghi nhớ ngắn gọn

Magic methods giúp object của bạn hành xử giống object Python thật.

---

## 18. Composition Và Aggregation

### Khái niệm

Composition và aggregation đều là quan hệ "has-a".

- Composition: object cha sở hữu object con mạnh hơn; object con thường được tạo bên trong object cha.
- Aggregation: object cha tham chiếu object con; object con có thể tồn tại độc lập.

### Khi nào dùng

Dùng khi quan hệ là "có một" thay vì "là một".

### Ví dụ code Python

Composition:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()
```

Aggregation:

```python
class Teacher:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Cô Lan")
school = School(teacher)
```

### Lỗi thường gặp

Dùng kế thừa khi composition phù hợp hơn.

### Ghi nhớ ngắn gọn

Nếu A "có" B, hãy nghĩ đến composition trước khi nghĩ đến kế thừa.

---

## 19. Dataclass Trong Python

### Khái niệm

`dataclass` giúp tạo class chứa dữ liệu ngắn gọn hơn. Python tự sinh `__init__`, `__repr__`, `__eq__` cơ bản.

### Khi nào dùng

Dùng cho object chủ yếu lưu dữ liệu, ví dụ `Product`, `OrderItem`, `Point`.

### Ví dụ code Python

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    score: float


s = Student("An", 18, 8.5)
print(s)
```

### Lỗi thường gặp

Dùng dataclass cho class có quá nhiều logic nghiệp vụ phức tạp mà không thiết kế cẩn thận.

### Ghi nhớ ngắn gọn

Dataclass rất tốt cho model dữ liệu gọn, rõ, ít boilerplate.

---

## 20. So Sánh OOP Với Procedural Programming

### Khái niệm

Procedural programming tổ chức code thành các hàm và dữ liệu rời nhau. OOP tổ chức code thành object, trong đó dữ liệu và hành vi liên quan nằm cùng nhau.

### Khi nào dùng

- Procedural: script nhỏ, xử lý tuyến tính, logic đơn giản.
- OOP: hệ thống có nhiều thực thể, nhiều quan hệ, cần mở rộng.

### Ví dụ code Python

Procedural:

```python
student = {"name": "An", "score": 8}


def print_student(student):
    print(student["name"], student["score"])


print_student(student)
```

OOP:

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print(self.name, self.score)


student = Student("An", 8)
student.print_info()
```

### Lỗi thường gặp

Ép mọi thứ thành class dù bài toán chỉ cần function đơn giản.

### Ghi nhớ ngắn gọn

Không phải bài nào cũng cần OOP, nhưng OOP rất mạnh khi hệ thống lớn dần.

---

## 21. Các Lỗi Phổ Biến Khi Học OOP Python

### Khái niệm

Đây là các lỗi hay gặp khi mới học OOP.

### Khi nào dùng

Dùng như checklist khi debug và review code OOP.

### Ví dụ code Python

Sai:

```python
class Student:
    scores = []

    def add_score(self, score):
        self.scores.append(score)
```

Đúng:

```python
class Student:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
```

### Lỗi thường gặp

- Quên `self`.
- Nhầm instance attribute và class attribute.
- Làm class quá lớn, xử lý quá nhiều việc.
- Làm method quá dài.
- Dùng kế thừa khi nên dùng composition.
- Không validate dữ liệu đầu vào.
- Đặt tên class, method, attribute không rõ nghĩa.

### Ghi nhớ ngắn gọn

Class tốt có trách nhiệm rõ ràng và dữ liệu hợp lệ.

---

## 22. Best Practices Khi Thiết Kế Class Trong Python

### Khái niệm

Best practices là các nguyên tắc giúp class dễ đọc, dễ sửa, dễ test và dễ mở rộng.

### Khi nào dùng

Nên áp dụng khi viết code OOP nghiêm túc, đặc biệt khi code sẽ được bảo trì lâu dài.

### Ví dụ code Python

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Số dư ban đầu không được âm")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp phải dương")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải dương")
        if amount > self._balance:
            raise ValueError("Không đủ số dư")
        self._balance -= amount
```

### Lỗi thường gặp

- Class làm quá nhiều việc.
- Method thay đổi quá nhiều trạng thái cùng lúc.
- Public quá nhiều attribute nội bộ.
- Phụ thuộc vòng tròn giữa các class.

### Ghi nhớ ngắn gọn

Một class nên có một trách nhiệm chính, tên rõ ràng, API gọn và dữ liệu hợp lệ.

---

## Tổng Kết Nhanh

- Class là khuôn mẫu, object là thực thể.
- `self` trỏ đến object hiện tại.
- Instance attribute thuộc về object, class attribute thuộc về class.
- Encapsulation giúp bảo vệ dữ liệu.
- Inheritance dùng cho quan hệ "is-a".
- Composition dùng cho quan hệ "has-a".
- Polymorphism giúp xử lý nhiều object qua cùng interface.
- ABC giúp định nghĩa interface bắt buộc.
- Magic methods giúp object hòa nhập với Python.
- Dataclass giúp viết class dữ liệu gọn hơn.

