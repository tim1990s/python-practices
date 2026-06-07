# Chương trình in các bội số đầu tiên của một số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so = int(input("Nhập số cần in bội số: "))
so_luong = int(input("Nhập số lượng bội số: "))

if so_luong <= 0:
    print("Số lượng bội số phải lớn hơn 0")
else:
    for i in range(1, so_luong + 1):
        print(so * i)
