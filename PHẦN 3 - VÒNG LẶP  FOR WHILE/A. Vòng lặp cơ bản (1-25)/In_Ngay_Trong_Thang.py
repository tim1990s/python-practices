# Chương trình in các ngày trong tháng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if nam <= 0 or thang < 1 or thang > 12:
    print("Tháng hoặc năm không hợp lệ")
else:
    nam_nhuan = nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay = 31
    elif thang in [4, 6, 9, 11]:
        so_ngay = 30
    elif nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28

    for ngay in range(1, so_ngay + 1):
        print(ngay)
