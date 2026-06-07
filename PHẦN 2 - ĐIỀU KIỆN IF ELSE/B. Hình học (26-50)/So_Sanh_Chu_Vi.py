# Chương trình so sánh chu vi

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chu_vi_1 = float(input("Nhập chu vi thứ nhất: "))
chu_vi_2 = float(input("Nhập chu vi thứ hai: "))

if chu_vi_1 < 0 or chu_vi_2 < 0:
    print("Chu vi không được âm")
elif chu_vi_1 > chu_vi_2:
    print("Chu vi thứ nhất lớn hơn")
elif chu_vi_1 < chu_vi_2:
    print("Chu vi thứ hai lớn hơn")
else:
    print("Hai chu vi bằng nhau")
