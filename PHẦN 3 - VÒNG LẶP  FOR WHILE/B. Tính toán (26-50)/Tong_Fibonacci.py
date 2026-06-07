# Chương trình tính tổng n số Fibonacci đầu tiên

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử Fibonacci: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    a = 0
    b = 1
    tong = 0

    for _ in range(n):
        tong += a
        a, b = b, a + b

    print("Tổng Fibonacci là:", tong)
