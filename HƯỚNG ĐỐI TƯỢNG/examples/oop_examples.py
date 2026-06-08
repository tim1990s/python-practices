"""Cac vi du tong hop ve HƯỚNG ĐỐI TƯỢNG trong Python.

Chay file:
    python examples/oop_examples.py
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []

    def add_score(self, score):
        if score < 0 or score > 10:
            raise ValueError("Diem phai nam trong khoang 0..10")
        self.scores.append(score)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def introduce(self):
        return f"Toi la {self.name}, {self.age} tuoi, hoc tai {self.school_name}"


class User:
    user_count = 0

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    def say_hello(self):
        return f"Hello, {self.name}"

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @staticmethod
    def is_valid_name(name):
        return len(name.strip()) >= 2


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("So du ban dau khong duoc am")
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("So tien nap phai duong")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("So tien rut phai duong")
        if amount > self.__balance:
            raise ValueError("Khong du so du")
        self.__balance -= amount


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return super().calculate_salary() + self.overtime_hours * 100_000


class Flyable:
    def move(self):
        return "Bay"


class Swimmable:
    def swim(self):
        return "Boi"


class Duck(Flyable, Swimmable):
    pass


class Animal:
    def speak(self):
        raise NotImplementedError("Subclass phai cai dat speak()")


class Dog(Animal):
    def speak(self):
        return "Gau"


class Cat(Animal):
    def speak(self):
        return "Meo"


def make_animal_speak(animal):
    return animal.speak()


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


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


class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return f"{self.engine.start()} -> Car started"


class Teacher:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, teacher):
        self.teacher = teacher


@dataclass
class Product:
    name: str
    price: float


def main():
    student = Student("An", 18)
    student.add_score(8)
    student.add_score(9)
    print(student.introduce())
    print("Diem trung binh:", student.average_score())

    user = User("Binh")
    print(user.say_hello())
    print("So user:", User.get_user_count())
    print("Ten hop le:", User.is_valid_name("An"))

    account = BankAccount("Chi", 1000)
    account.deposit(500)
    account.withdraw(200)
    print("So du:", account.balance)

    employees = [
        Employee("Nhan vien A", 10_000_000),
        Manager("Quan ly B", 20_000_000, 5_000_000),
        Developer("Lap trinh vien C", 15_000_000, 12),
    ]
    for employee in employees:
        print(employee.name, "luong:", employee.calculate_salary())

    duck = Duck()
    print("Duck:", duck.move(), duck.swim())
    print("MRO Duck:", [cls.__name__ for cls in Duck.mro()])

    for animal in [Dog(), Cat()]:
        print("Animal speak:", make_animal_speak(animal))

    rectangle = Rectangle(4, 5)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())

    m1 = Money(100)
    m2 = Money(200)
    print("Money:", m1, repr(m1), m1 == m2, m1 + m2)

    team = Team(["An", "Binh", "Chi"])
    print("So thanh vien team:", len(team))

    car = Car()
    print(car.start())

    teacher = Teacher("Co Lan")
    school = School(teacher)
    print("Teacher in school:", school.teacher.name)

    product = Product("Sach Python", 120_000)
    print(product)


if __name__ == "__main__":
    main()

