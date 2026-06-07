# Chương trình in mẫu zigzag

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều rộng: "))

if n <= 0:
    print("Chiều rộng phải lớn hơn 0")
else:
    for i in range(3):
        dong = ""

        for j in range(n):
            if (j + i) % 4 == 0 or (j - i) % 4 == 0:
                dong += "*"
            else:
                dong += " "

        print(dong)
