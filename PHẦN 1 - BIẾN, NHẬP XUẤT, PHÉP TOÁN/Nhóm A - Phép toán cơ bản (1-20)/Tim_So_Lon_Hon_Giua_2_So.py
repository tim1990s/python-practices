# Chương trình tìm số lớn hơn giữa 2 số
#
# Khi so sánh hai số, số lớn hơn là số có giá trị lớn hơn số còn lại.
#
# Ví dụ:
# Nếu a = 8 và b = 5 thì:
# Số lớn hơn là 8
#
# Ý tưởng:
# - Nhập hai số a và b.
# - So sánh a với b.
# - Nếu a lớn hơn b thì in a.
# - Nếu b lớn hơn a thì in b.
# - Nếu hai số bằng nhau thì thông báo hai số bằng nhau.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

if a > b:
    print("Số lớn hơn là:", a)
elif b > a:
    print("Số lớn hơn là:", b)
else:
    print("Hai số bằng nhau")
