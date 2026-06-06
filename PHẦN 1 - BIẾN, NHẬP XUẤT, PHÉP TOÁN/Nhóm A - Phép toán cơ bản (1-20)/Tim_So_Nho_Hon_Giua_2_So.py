# Chương trình tìm số nhỏ hơn giữa 2 số
#
# Khi so sánh hai số, số nhỏ hơn là số có giá trị nhỏ hơn số còn lại.
#
# Ví dụ:
# Nếu a = 8 và b = 5 thì:
# Số nhỏ hơn là 5
#
# Ý tưởng:
# - Nhập hai số a và b.
# - So sánh a với b.
# - Nếu a nhỏ hơn b thì in a.
# - Nếu b nhỏ hơn a thì in b.
# - Nếu hai số bằng nhau thì thông báo hai số bằng nhau.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

if a < b:
    print("Số nhỏ hơn là:", a)
elif b < a:
    print("Số nhỏ hơn là:", b)
else:
    print("Hai số bằng nhau")
