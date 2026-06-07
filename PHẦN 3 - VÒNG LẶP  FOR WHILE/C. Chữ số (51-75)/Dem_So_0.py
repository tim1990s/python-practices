# Chương trình đếm số chữ số 0

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
dem = 0

for chu_so in chuoi:
    if chu_so == "0":
        dem += 1

print("Số chữ số 0 là:", dem)
