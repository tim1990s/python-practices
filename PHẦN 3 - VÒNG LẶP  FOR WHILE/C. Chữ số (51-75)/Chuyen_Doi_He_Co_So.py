# Chương trình chuyển đổi hệ cơ số từ 2 đến 16

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập số cần chuyển: ").upper()
co_so_nguon = int(input("Nhập hệ cơ số nguồn (2-16): "))
co_so_dich = int(input("Nhập hệ cơ số đích (2-16): "))
ky_tu = "0123456789ABCDEF"
hop_le = True

gia_tri = 0

if co_so_nguon < 2 or co_so_nguon > 16 or co_so_dich < 2 or co_so_dich > 16 or chuoi == "":
    hop_le = False
else:
    for chu_so in chuoi:
        if chu_so not in ky_tu:
            hop_le = False
            break

        gia_tri_chu_so = ky_tu.index(chu_so)

        if gia_tri_chu_so >= co_so_nguon:
            hop_le = False
            break

        gia_tri = gia_tri * co_so_nguon + gia_tri_chu_so

if not hop_le:
    print("Dữ liệu không hợp lệ")
elif gia_tri == 0:
    print("Kết quả là: 0")
else:
    ket_qua = ""

    while gia_tri > 0:
        ket_qua = ky_tu[gia_tri % co_so_dich] + ket_qua
        gia_tri //= co_so_dich

    print("Kết quả là:", ket_qua)
