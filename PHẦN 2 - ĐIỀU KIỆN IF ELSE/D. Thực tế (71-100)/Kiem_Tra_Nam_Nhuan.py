# Chương trình kiểm tra năm nhuận

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

nam = int(input("Nhập năm: "))

if nam <= 0:
    print("Năm không hợp lệ")
elif nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "là năm nhuận")
else:
    print(nam, "không phải là năm nhuận")
