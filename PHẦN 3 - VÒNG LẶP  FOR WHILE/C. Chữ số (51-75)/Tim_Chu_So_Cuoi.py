# Chương trình tìm chữ số cuối

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chu_so_cuoi = abs(n) % 10

print("Chữ số cuối là:", chu_so_cuoi)
