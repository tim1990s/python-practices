# Chương trình kiểm tra số chẵn

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n % 2 == 0:
    print(n, "là số chẵn")
else:
    print(n, "không phải là số chẵn")
