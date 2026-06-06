# Chương trình giải phương trình bậc hai
#
# Phương trình bậc hai có dạng:
#     ax² + bx + c = 0
#
# Trong đó:
# - a, b, c là các số thực
# - a phải khác 0
# - x là ẩn số cần tìm
#
# Cách giải:
#
# Bước 1: Tính biệt thức (Delta)
#     Δ = b² - 4ac
#
# Bước 2: Xét giá trị của Δ
#
# - Nếu Δ > 0:
#     Phương trình có 2 nghiệm phân biệt
#     x1 = (-b + √Δ) / (2a)
#     x2 = (-b - √Δ) / (2a)
#
# - Nếu Δ = 0:
#     Phương trình có nghiệm kép
#     x = -b / (2a)
#
# - Nếu Δ < 0:
#     Phương trình vô nghiệm trong tập số thực
#
# Ví dụ:
# x² - 5x + 6 = 0
# Δ = 25 - 24 = 1
# x1 = 3, x2 = 2

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)

        print("Phương trình có nghiệm kép:")
        print("x =", x)

    else:
        print("Phương trình vô nghiệm")