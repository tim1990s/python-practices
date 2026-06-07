# Chương trình tìm chữ số đầu

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)

while so >= 10:
    so //= 10

print("Chữ số đầu là:", so)
