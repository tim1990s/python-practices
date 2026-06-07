# Chương trình tính tích chữ số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
tich = 1

if so == 0:
    tich = 0
else:
    while so > 0:
        tich *= so % 10
        so //= 10

print("Tích chữ số là:", tich)
