# Chương trình in hình vuông sao

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for _ in range(n):
        print("* " * n)
