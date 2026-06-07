# Chương trình tính Fibonacci thứ n

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập vị trí n: "))

if n < 0:
    print("n không được âm")
else:
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    print("Fibonacci thứ", n, "là:", a)
