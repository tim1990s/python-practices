# Chương trình kiểm tra chữ số đầu

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))
chu_so_dau = str(abs(n))[0]

print("Chữ số đầu của", n, "là:", chu_so_dau)
