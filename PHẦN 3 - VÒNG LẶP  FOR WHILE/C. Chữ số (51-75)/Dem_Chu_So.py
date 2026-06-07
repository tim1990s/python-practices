# Chương trình đếm chữ số của một số nguyên

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
dem = 0

if so == 0:
    dem = 1
else:
    while so > 0:
        dem += 1
        so //= 10

print("Số chữ số là:", dem)
