# Chương trình in mẫu Fibonacci

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    a = 0
    b = 1

    for i in range(1, n + 1):
        dong = ""

        for _ in range(i):
            dong += str(a) + " "
            a, b = b, a + b

        print(dong)
