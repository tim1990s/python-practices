# Chương trình đếm bit 0 trong biểu diễn nhị phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Số phải không âm")
elif n == 0:
    print("Số bit 0 là: 1")
else:
    dem = 0

    while n > 0:
        if n % 2 == 0:
            dem += 1

        n //= 2

    print("Số bit 0 là:", dem)
