# Chương trình đếm chữ số lẻ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
dem = 0

while so > 0:
    if (so % 10) % 2 != 0:
        dem += 1

    so //= 10

print("Số chữ số lẻ là:", dem)
