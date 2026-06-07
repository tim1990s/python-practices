# Chương trình tính tiền điện theo bậc thang đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so_kwh = float(input("Nhập số kWh đã dùng: "))

if so_kwh < 0:
    print("Số kWh không được âm")
else:
    tien = 0
    con_lai = so_kwh

    if con_lai > 0:
        bac = min(con_lai, 50)
        tien += bac * 1678
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 50)
        tien += bac * 1734
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 100)
        tien += bac * 2014
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 100)
        tien += bac * 2536
        con_lai -= bac

    if con_lai > 0:
        bac = min(con_lai, 100)
        tien += bac * 2834
        con_lai -= bac

    if con_lai > 0:
        tien += con_lai * 2927

    print("Tiền điện phải trả là:", tien, "đồng")
