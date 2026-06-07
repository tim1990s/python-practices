# Chương trình in hình kim cương

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập nửa chiều cao: "))

if n <= 0:
    print("Nửa chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
