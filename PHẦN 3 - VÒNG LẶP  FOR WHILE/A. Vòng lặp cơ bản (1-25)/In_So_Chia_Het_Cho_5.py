# Chương trình in các số chia hết cho 5 từ 1 đến N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 1:
    print("N phải lớn hơn hoặc bằng 1")
else:
    for i in range(1, n + 1):
        if i % 5 == 0:
            print(i)
