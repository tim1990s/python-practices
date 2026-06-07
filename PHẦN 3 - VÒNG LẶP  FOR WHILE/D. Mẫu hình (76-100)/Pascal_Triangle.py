# Chương trình in Pascal triangle

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    hang = [1]

    for _ in range(n):
        dong = ""

        for gia_tri in hang:
            dong += str(gia_tri) + " "

        print(dong)
        hang_moi = [1]

        for i in range(len(hang) - 1):
            hang_moi.append(hang[i] + hang[i + 1])

        hang_moi.append(1)
        hang = hang_moi
