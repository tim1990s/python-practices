# Chương trình in bảng cửu chương

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số cần in bảng cửu chương: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
