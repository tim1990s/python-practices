# Chương trình in chữ A

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao chữ A: "))

if n < 3:
    print("Chiều cao phải lớn hơn hoặc bằng 3")
else:
    giua = n // 2

    for i in range(n):
        dong = ""

        for j in range(2 * n - 1):
            if j == n - 1 - i or j == n - 1 + i or i == giua and n - 1 - i <= j <= n - 1 + i:
                dong += "*"
            else:
                dong += " "

        print(dong)
