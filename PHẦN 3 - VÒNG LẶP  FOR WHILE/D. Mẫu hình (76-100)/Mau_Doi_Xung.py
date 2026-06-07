# Chương trình in mẫu số đối xứng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        dong = ""

        for j in range(1, i + 1):
            dong += str(j)

        for j in range(i - 1, 0, -1):
            dong += str(j)

        print(dong)
