# Chương trình chọn giá trị lớn nhất trong 3 giá trị

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập giá trị thứ nhất: "))
b = float(input("Nhập giá trị thứ hai: "))
c = float(input("Nhập giá trị thứ ba: "))

lon_nhat = a

if b > lon_nhat:
    lon_nhat = b

if c > lon_nhat:
    lon_nhat = c

print("Giá trị lớn nhất là:", lon_nhat)
