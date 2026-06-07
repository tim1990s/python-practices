# Chương trình đảo ngược số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
dao = 0

while so > 0:
    dao = dao * 10 + so % 10
    so //= 10

if n < 0:
    dao = -dao

print("Số đảo ngược là:", dao)
