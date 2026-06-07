# Chương trình in hình chữ nhật rỗng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))

if chieu_dai <= 0 or chieu_rong <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(chieu_rong):
        dong = ""

        for j in range(chieu_dai):
            if i == 0 or i == chieu_rong - 1 or j == 0 or j == chieu_dai - 1:
                dong += "*"
            else:
                dong += " "

        print(dong)
