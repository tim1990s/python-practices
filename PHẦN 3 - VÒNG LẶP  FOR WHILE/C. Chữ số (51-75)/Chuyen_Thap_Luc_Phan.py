# Chương trình chuyển số thập phân sang thập lục phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên không âm: "))
ky_tu = "0123456789ABCDEF"

if n < 0:
    print("Số phải không âm")
elif n == 0:
    print("Thập lục phân là: 0")
else:
    ket_qua = ""

    while n > 0:
        ket_qua = ky_tu[n % 16] + ket_qua
        n //= 16

    print("Thập lục phân là:", ket_qua)
