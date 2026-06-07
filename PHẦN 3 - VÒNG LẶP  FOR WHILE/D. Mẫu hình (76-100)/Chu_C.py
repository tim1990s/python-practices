# Chương trình in chữ C

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước chữ C: "))

if n < 3:
    print("Kích thước phải lớn hơn hoặc bằng 3")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if i == 0 or i == n - 1 or j == 0:
                dong += "*"
            else:
                dong += " "

        print(dong)
