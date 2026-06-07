# Chương trình in chữ N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if j == 0 or j == n - 1 or i == j:
                dong += "*"
            else:
                dong += " "

        print(dong)
