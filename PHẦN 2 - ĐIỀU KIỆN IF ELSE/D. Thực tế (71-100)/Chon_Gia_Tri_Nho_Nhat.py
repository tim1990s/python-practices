# Chương trình chọn giá trị nhỏ nhất trong 3 giá trị

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập giá trị thứ nhất: "))
b = float(input("Nhập giá trị thứ hai: "))
c = float(input("Nhập giá trị thứ ba: "))

nho_nhat = a

if b < nho_nhat:
    nho_nhat = b

if c < nho_nhat:
    nho_nhat = c

print("Giá trị nhỏ nhất là:", nho_nhat)
