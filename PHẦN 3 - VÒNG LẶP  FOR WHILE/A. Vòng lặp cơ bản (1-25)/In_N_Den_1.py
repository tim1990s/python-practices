# Chương trình in từ N về 1

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 1:
    print("N phải lớn hơn hoặc bằng 1")
else:
    for i in range(n, 0, -1):
        print(i)
