# Chương trình so sánh hai số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

if a > b:
    print("Số thứ nhất lớn hơn số thứ hai")
elif a < b:
    print("Số thứ nhất nhỏ hơn số thứ hai")
else:
    print("Hai số bằng nhau")
