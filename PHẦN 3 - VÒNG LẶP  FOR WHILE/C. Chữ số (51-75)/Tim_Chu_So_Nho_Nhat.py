# Chương trình tìm chữ số nhỏ nhất

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
nho_nhat = 9

if so == 0:
    nho_nhat = 0
else:
    while so > 0:
        chu_so = so % 10

        if chu_so < nho_nhat:
            nho_nhat = chu_so

        so //= 10

print("Chữ số nhỏ nhất là:", nho_nhat)
