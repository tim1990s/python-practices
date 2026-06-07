# Chương trình so sánh nghiệm của phương trình bậc hai

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm trong tập số thực")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        if x1 > x2:
            print("x1 lớn hơn x2")
        elif x1 < x2:
            print("x1 nhỏ hơn x2")
        else:
            print("Hai nghiệm bằng nhau")
