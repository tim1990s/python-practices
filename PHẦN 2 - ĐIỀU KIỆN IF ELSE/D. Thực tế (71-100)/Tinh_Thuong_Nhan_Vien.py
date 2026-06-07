# Chương trình tính thưởng nhân viên theo điểm KPI

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

luong = float(input("Nhập lương cơ bản: "))
kpi = float(input("Nhập điểm KPI: "))

if luong < 0 or kpi < 0 or kpi > 100:
    print("Dữ liệu không hợp lệ")
elif kpi >= 90:
    thuong = luong * 0.20
    print("Tiền thưởng là:", thuong)
elif kpi >= 80:
    thuong = luong * 0.10
    print("Tiền thưởng là:", thuong)
elif kpi >= 65:
    thuong = luong * 0.05
    print("Tiền thưởng là:", thuong)
else:
    thuong = 0
    print("Tiền thưởng là:", thuong)
