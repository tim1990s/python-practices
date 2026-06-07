# Chương trình chọn mức lương theo bậc nhân viên

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bac = int(input("Nhập bậc lương (1-4): "))

if bac == 1:
    print("Mức lương là: 7000000")
elif bac == 2:
    print("Mức lương là: 10000000")
elif bac == 3:
    print("Mức lương là: 15000000")
elif bac == 4:
    print("Mức lương là: 22000000")
else:
    print("Bậc lương không hợp lệ")
