# Chương trình chọn nghiệm nhỏ nhất của phương trình bậc hai

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
    if b == 0:
        print("Không có nghiệm hữu hạn để chọn")
    else:
        x = -c / b
        print("Nghiệm nhỏ nhất là:", x)
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm trong tập số thực")
    elif delta == 0:
        x = -b / (2 * a)
        print("Nghiệm nhỏ nhất là:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Nghiệm nhỏ nhất là:", min(x1, x2))
