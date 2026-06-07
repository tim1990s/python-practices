# Chương trình so sánh ba số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a == b == c:
    print("Ba số bằng nhau")
else:
    lon_nhat = max(a, b, c)
    nho_nhat = min(a, b, c)

    print("Số lớn nhất là:", lon_nhat)
    print("Số nhỏ nhất là:", nho_nhat)
