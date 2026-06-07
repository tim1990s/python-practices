# 10 Bài Tập Thực Hành OOP Python

Thư mục này không có lời giải. Mỗi file `.py` chỉ là starter code để bạn tự thiết kế và cài đặt.

---

## 1. Tạo Class Student Quản Lý Học Sinh

**Mức độ:** Dễ

**Mục tiêu kiến thức:** Class, object, instance attribute, instance method, `__init__`, `self`.

**Mô tả yêu cầu:**

- Tạo class `Student` có `name`, `age`, `scores`.
- Thêm method `add_score(score)`.
- Thêm method `average_score()`.
- Thêm method `display_info()`.

**Gợi ý thiết kế class:**

- `scores` nên là instance attribute, không nên là class attribute.
- Kiểm tra điểm trong khoảng 0 đến 10.

**Input/output mẫu:**

```python
s = Student("An", 18)
s.add_score(8)
s.add_score(9)
print(s.average_score())  # 8.5
```

**Yêu cầu mở rộng:**

- Thêm method xếp loại: Giỏi, Khá, Trung bình, Yếu.

---

## 2. Tạo Class BankAccount

**Mức độ:** Dễ

**Mục tiêu kiến thức:** Encapsulation, private attribute, `@property`, validation.

**Mô tả yêu cầu:**

- Tạo class `BankAccount` có chủ tài khoản và số dư.
- Cho phép nạp tiền, rút tiền, xem số dư.
- Không cho rút quá số dư.
- Không cho nạp/rút số tiền âm.

**Gợi ý thiết kế class:**

- Dùng `_balance` hoặc `__balance`.
- Dùng `@property` cho `balance`.

**Input/output mẫu:**

```python
account = BankAccount("An", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # 1300
```

**Yêu cầu mở rộng:**

- Lưu lịch sử giao dịch.

---

## 3. Rectangle Và Circle

**Mức độ:** Dễ

**Mục tiêu kiến thức:** Method, abstraction cơ bản, magic method `__str__`.

**Mô tả yêu cầu:**

- Tạo class `Rectangle` có `width`, `height`.
- Tạo class `Circle` có `radius`.
- Mỗi class có method `area()` và `perimeter()`.

**Gợi ý thiết kế class:**

- Có thể dùng `math.pi`.
- Có thể thêm `__str__` để in thông tin đẹp hơn.

**Input/output mẫu:**

```python
r = Rectangle(4, 5)
print(r.area())       # 20
print(r.perimeter())  # 18
```

**Yêu cầu mở rộng:**

- Tạo abstract class `Shape` với `area()` và `perimeter()`.

---

## 4. Quản Lý Sách Trong Thư Viện

**Mức độ:** Trung bình

**Mục tiêu kiến thức:** Composition, list object, encapsulation.

**Mô tả yêu cầu:**

- Tạo class `Book` có `title`, `author`, `isbn`, `is_borrowed`.
- Tạo class `Library` quản lý danh sách sách.
- Có thể thêm sách, tìm sách, mượn sách, trả sách.

**Gợi ý thiết kế class:**

- `Library` có attribute `books`.
- Method tìm sách có thể tìm theo title hoặc isbn.

**Input/output mẫu:**

```python
library = Library()
library.add_book(Book("Python OOP", "Author A", "001"))
library.borrow_book("001")
```

**Yêu cầu mở rộng:**

- Thêm class `Member` để quản lý người mượn sách.

---

## 5. Quản Lý Nhân Viên Với Kế Thừa

**Mức độ:** Trung bình

**Mục tiêu kiến thức:** Inheritance, overriding, `super()`, polymorphism.

**Mô tả yêu cầu:**

- Tạo class cha `Employee`.
- Tạo class con `Manager` và `Developer`.
- Mỗi loại nhân viên có cách tính lương khác nhau.

**Gợi ý thiết kế class:**

- `Employee.calculate_salary()` trả về lương cơ bản.
- `Manager` có bonus.
- `Developer` có overtime hours.

**Input/output mẫu:**

```python
employees = [Manager("An", 2000, 500), Developer("Binh", 1500, 10)]
for employee in employees:
    print(employee.calculate_salary())
```

**Yêu cầu mở rộng:**

- Thêm phòng ban, đánh giá hiệu suất, cấp bậc.

---

## 6. ShoppingCart Và Product

**Mức độ:** Trung bình

**Mục tiêu kiến thức:** Composition, aggregation, magic method `__len__`.

**Mô tả yêu cầu:**

- Tạo `Product` có `name`, `price`.
- Tạo `CartItem` gồm product và quantity.
- Tạo `ShoppingCart` cho phép thêm, xóa, cập nhật số lượng, tính tổng tiền.

**Gợi ý thiết kế class:**

- `ShoppingCart` nên chứa list các `CartItem`.
- `CartItem.subtotal()` tính tiền theo số lượng.

**Input/output mẫu:**

```python
cart.add_product(product, quantity=2)
print(cart.total_price())
print(len(cart))
```

**Yêu cầu mở rộng:**

- Thêm mã giảm giá theo phần trăm.

---

## 7. Hệ Thống Đăng Nhập User Và AdminUser

**Mức độ:** Trung bình

**Mục tiêu kiến thức:** Encapsulation, inheritance, overriding, class method.

**Mô tả yêu cầu:**

- Tạo class `User` có username, password, trạng thái active.
- Tạo method `login(username, password)`.
- Tạo class `AdminUser` có thêm quyền khóa/mở khóa user khác.

**Gợi ý thiết kế class:**

- Không nên lưu password public.
- Có thể dùng `hashlib` nếu muốn luyện thêm.

**Input/output mẫu:**

```python
admin.lock_user(user)
print(user.is_active)
```

**Yêu cầu mở rộng:**

- Thêm role, permission và password hashing.

---

## 8. Game Nhân Vật Character, Warrior, Mage

**Mức độ:** Khó

**Mục tiêu kiến thức:** Inheritance, polymorphism, overriding, encapsulation.

**Mô tả yêu cầu:**

- Tạo class cha `Character` có name, hp, attack_power.
- Tạo class `Warrior` và `Mage`.
- Mỗi class có method `attack(target)` riêng.
- Nhân vật chết khi hp <= 0.

**Gợi ý thiết kế class:**

- `Character.take_damage(amount)`.
- `Mage` có thể có mana.
- `Warrior` có thể có armor.

**Input/output mẫu:**

```python
warrior.attack(mage)
print(mage.hp)
```

**Yêu cầu mở rộng:**

- Thêm skill đặc biệt, critical hit, defense.

---

## 9. Quản Lý Đơn Hàng

**Mức độ:** Khó

**Mục tiêu kiến thức:** Composition, aggregation, dataclass, magic method.

**Mô tả yêu cầu:**

- Tạo `Customer`.
- Tạo `Product`.
- Tạo `OrderItem`.
- Tạo `Order` gồm customer và danh sách item.
- Tính tổng tiền đơn hàng.

**Gợi ý thiết kế class:**

- `OrderItem.subtotal()`.
- `Order.total_amount()`.
- Dùng dataclass cho object dữ liệu đơn giản.

**Input/output mẫu:**

```python
order.add_item(product, 2)
print(order.total_amount())
```

**Yêu cầu mở rộng:**

- Thêm trạng thái đơn hàng: pending, paid, shipped, cancelled.

---

## 10. Mini Project Quản Lý Trường Học

**Mức độ:** Khó

**Mục tiêu kiến thức:** Áp dụng tổng hợp OOP.

**Mô tả yêu cầu:**

- Quản lý học sinh, giáo viên, lớp học, môn học, điểm số.
- Có thể thêm học sinh vào lớp.
- Có thể gán giáo viên cho môn học.
- Có thể nhập điểm và tính điểm trung bình.

**Gợi ý thiết kế class:**

- `Person`
- `Student`
- `Teacher`
- `Course`
- `ClassRoom`
- `GradeBook`

**Input/output mẫu:**

```python
school_class.add_student(student)
gradebook.add_grade(student, course, 8.5)
print(gradebook.average_score(student))
```

**Yêu cầu mở rộng:**

- Lưu dữ liệu ra file JSON.
- Tạo menu console.
- Thêm tìm kiếm và thống kê.

