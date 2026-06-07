# Chương trình tìm bit cao nhất trong biểu diễn nhị phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên dương: "))

if n <= 0:
    print("Số phải lớn hơn 0")
else:
    vi_tri = 0
    gia_tri = 1

    while gia_tri * 2 <= n:
        gia_tri *= 2
        vi_tri += 1

    print("Bit cao nhất ở vị trí:", vi_tri)
    print("Giá trị bit cao nhất là:", gia_tri)
