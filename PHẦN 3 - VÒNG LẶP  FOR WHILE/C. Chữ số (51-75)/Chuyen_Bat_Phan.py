# Chương trình chuyển số thập phân sang bát phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Số phải không âm")
elif n == 0:
    print("Bát phân là: 0")
else:
    ket_qua = ""

    while n > 0:
        ket_qua = str(n % 8) + ket_qua
        n //= 8

    print("Bát phân là:", ket_qua)
