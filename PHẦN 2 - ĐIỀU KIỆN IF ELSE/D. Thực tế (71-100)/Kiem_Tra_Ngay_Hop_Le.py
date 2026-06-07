# Chương trình kiểm tra ngày hợp lệ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if nam <= 0 or thang < 1 or thang > 12 or ngay < 1:
    print("Ngày tháng năm không hợp lệ")
else:
    nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay = 31
    elif thang in [4, 6, 9, 11]:
        so_ngay = 30
    elif nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28

    if ngay <= so_ngay:
        print("Ngày hợp lệ")
    else:
        print("Ngày không hợp lệ")
