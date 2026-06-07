# Chương trình tìm min trong 4 số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
d = float(input("Nhập số thứ tư: "))

min_so = a

if b < min_so:
    min_so = b

if c < min_so:
    min_so = c

if d < min_so:
    min_so = d

print("Số nhỏ nhất là:", min_so)
