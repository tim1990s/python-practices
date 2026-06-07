# Chương trình tìm max trong 4 số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
d = float(input("Nhập số thứ tư: "))

max_so = a

if b > max_so:
    max_so = b

if c > max_so:
    max_so = c

if d > max_so:
    max_so = d

print("Số lớn nhất là:", max_so)
