# Chương trình in sóng sin ký tự đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều dài sóng: "))

if n <= 0:
    print("Chiều dài phải lớn hơn 0")
else:
    for hang in range(3):
        dong = ""

        for cot in range(n):
            vi_tri = cot % 4

            if (hang == 0 and vi_tri == 1) or (hang == 1 and (vi_tri == 0 or vi_tri == 2)) or (hang == 2 and vi_tri == 3):
                dong += "*"
            else:
                dong += " "

        print(dong)
