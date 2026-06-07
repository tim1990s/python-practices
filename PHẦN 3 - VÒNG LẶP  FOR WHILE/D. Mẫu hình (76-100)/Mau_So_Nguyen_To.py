# Chương trình in mẫu số nguyên tố

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    so = 2

    for i in range(1, n + 1):
        dong = ""

        for _ in range(i):
            while True:
                la_nguyen_to = True

                for uoc in range(2, int(so ** 0.5) + 1):
                    if so % uoc == 0:
                        la_nguyen_to = False
                        break

                if la_nguyen_to:
                    dong += str(so) + " "
                    so += 1
                    break

                so += 1

        print(dong)
