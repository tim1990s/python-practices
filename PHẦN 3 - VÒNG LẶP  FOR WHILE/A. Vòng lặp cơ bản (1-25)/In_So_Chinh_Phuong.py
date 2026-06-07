# Chương trình in các số chính phương từ 1 đến N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 0:
    print("N không được âm")
else:
    i = 0

    while i * i <= n:
        print(i * i)
        i += 1
