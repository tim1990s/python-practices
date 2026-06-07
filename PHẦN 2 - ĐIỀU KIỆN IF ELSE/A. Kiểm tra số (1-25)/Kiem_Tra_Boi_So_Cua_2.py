# Chương trình kiểm tra bội số của 2

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n % 2 == 0:
    print(n, "là bội số của 2")
else:
    print(n, "không phải là bội số của 2")
