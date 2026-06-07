# Chương trình đảo bit của chuỗi nhị phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập chuỗi nhị phân: ")
hop_le = True
ket_qua = ""

for bit in chuoi:
    if bit == "0":
        ket_qua += "1"
    elif bit == "1":
        ket_qua += "0"
    else:
        hop_le = False
        break

if not hop_le or chuoi == "":
    print("Chuỗi nhị phân không hợp lệ")
else:
    print("Chuỗi sau khi đảo bit là:", ket_qua)
