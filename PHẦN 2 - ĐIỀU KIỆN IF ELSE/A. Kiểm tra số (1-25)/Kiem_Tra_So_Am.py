# Chương trình kiểm tra số âm

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = float(input("Nhập số cần kiểm tra: "))

if n < 0:
    print(n, "là số âm")
else:
    print(n, "không phải là số âm")
