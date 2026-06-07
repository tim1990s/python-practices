# Chương trình in các số hoàn hảo từ 1 đến N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 1:
    print("N phải lớn hơn hoặc bằng 1")
else:
    for so in range(1, n + 1):
        tong_uoc = 0

        for i in range(1, so):
            if so % i == 0:
                tong_uoc += i

        if tong_uoc == so:
            print(so)
