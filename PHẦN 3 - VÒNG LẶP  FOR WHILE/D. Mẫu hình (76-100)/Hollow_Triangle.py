# Chương trình in hollow triangle

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao: "))

if n <= 0:
    print("Chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        dong = ""

        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                dong += "*"
            else:
                dong += " "

        print(dong)
