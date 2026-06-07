# Chương trình tính tổng hai số nhị phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = input("Nhập số nhị phân thứ nhất: ")
b = input("Nhập số nhị phân thứ hai: ")
hop_le = True

for chu_so in a + b:
    if chu_so not in "01":
        hop_le = False
        break

if not hop_le or a == "" or b == "":
    print("Dữ liệu nhị phân không hợp lệ")
else:
    tong = 0

    for chu_so in a:
        tong = tong * 2 + int(chu_so)

    gia_tri_b = 0

    for chu_so in b:
        gia_tri_b = gia_tri_b * 2 + int(chu_so)

    tong += gia_tri_b

    if tong == 0:
        ket_qua = "0"
    else:
        ket_qua = ""

        while tong > 0:
            ket_qua = str(tong % 2) + ket_qua
            tong //= 2

    print("Tổng nhị phân là:", ket_qua)
