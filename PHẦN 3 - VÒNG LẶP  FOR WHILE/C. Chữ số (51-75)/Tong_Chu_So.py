# Chương trình tính tổng chữ số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
tong = 0

if so == 0:
    tong = 0
else:
    while so > 0:
        tong += so % 10
        so //= 10

print("Tổng chữ số là:", tong)
