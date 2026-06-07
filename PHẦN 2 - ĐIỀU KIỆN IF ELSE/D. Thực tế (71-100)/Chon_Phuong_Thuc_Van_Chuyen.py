# Chương trình chọn phương thức vận chuyển

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

khoi_luong = float(input("Nhập khối lượng hàng (kg): "))
khoang_cach = float(input("Nhập khoảng cách giao hàng (km): "))

if khoi_luong <= 0 or khoang_cach <= 0:
    print("Khối lượng và khoảng cách phải lớn hơn 0")
elif khoang_cach <= 5 and khoi_luong <= 5:
    print("Chọn giao hàng hỏa tốc")
elif khoang_cach <= 30 and khoi_luong <= 20:
    print("Chọn giao hàng nhanh")
else:
    print("Chọn giao hàng tiết kiệm")
