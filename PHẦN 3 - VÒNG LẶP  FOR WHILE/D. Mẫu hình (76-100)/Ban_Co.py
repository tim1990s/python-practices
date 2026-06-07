# Chương trình in mẫu bàn cờ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước bàn cờ: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if (i + j) % 2 == 0:
                dong += "* "
            else:
                dong += "  "

        print(dong)
