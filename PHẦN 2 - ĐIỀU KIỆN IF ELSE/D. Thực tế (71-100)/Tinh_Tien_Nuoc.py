# Chương trình tính tiền nước theo bậc thang đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so_m3 = float(input("Nhập số m3 nước đã dùng: "))

if so_m3 < 0:
    print("Số m3 nước không được âm")
else:
    tien = 0
    con_lai = so_m3

    if con_lai > 0:
        bac = min(con_lai, 10)
        tien += bac * 7000
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 10)
        tien += bac * 8500
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 10)
        tien += bac * 10000
        con_lai -= bac

    if con_lai > 0:
        tien += con_lai * 15000

    print("Tiền nước phải trả là:", tien, "đồng")
