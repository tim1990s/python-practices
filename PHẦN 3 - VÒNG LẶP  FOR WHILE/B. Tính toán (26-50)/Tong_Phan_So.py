# Chương trình tính tổng phân số 1/2 + 2/3 + ... + N/(N+1)

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n <= 0:
    print("N phải lớn hơn 0")
else:
    tong = 0

    for i in range(1, n + 1):
        tong += i / (i + 1)

    print("Tổng phân số là:", tong)
