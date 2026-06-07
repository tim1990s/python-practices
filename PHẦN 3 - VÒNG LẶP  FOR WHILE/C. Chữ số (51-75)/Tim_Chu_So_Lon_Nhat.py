# Chương trình tìm chữ số lớn nhất

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
lon_nhat = 0

if so == 0:
    lon_nhat = 0
else:
    while so > 0:
        chu_so = so % 10

        if chu_so > lon_nhat:
            lon_nhat = chu_so

        so //= 10

print("Chữ số lớn nhất là:", lon_nhat)
