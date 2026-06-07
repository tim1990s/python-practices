# Chương trình in số ngẫu nhiên

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import random

so_luong = int(input("Nhập số lượng số ngẫu nhiên: "))
nho_nhat = int(input("Nhập giá trị nhỏ nhất: "))
lon_nhat = int(input("Nhập giá trị lớn nhất: "))

if so_luong <= 0 or nho_nhat > lon_nhat:
    print("Dữ liệu không hợp lệ")
else:
    for _ in range(so_luong):
        print(random.randint(nho_nhat, lon_nhat))
