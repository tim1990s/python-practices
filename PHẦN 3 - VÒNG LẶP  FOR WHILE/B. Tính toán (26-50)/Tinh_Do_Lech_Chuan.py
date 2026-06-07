# Chương trình tính độ lệch chuẩn của dãy số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    ds = []
    tong = 0

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        ds.append(so)
        tong += so

    trung_binh = tong / n
    tong_binh_phuong_lech = 0

    for so in ds:
        tong_binh_phuong_lech += (so - trung_binh) ** 2

    variance = tong_binh_phuong_lech / n
    do_lech_chuan = variance ** 0.5
    print("Độ lệch chuẩn là:", do_lech_chuan)
