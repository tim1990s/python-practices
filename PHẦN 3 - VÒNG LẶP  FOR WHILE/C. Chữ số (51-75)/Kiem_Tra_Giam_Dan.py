# Chương trình kiểm tra chữ số giảm dần

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
la_giam_dan = True

for i in range(len(chuoi) - 1):
    if chuoi[i] <= chuoi[i + 1]:
        la_giam_dan = False
        break

if la_giam_dan:
    print("Các chữ số giảm dần")
else:
    print("Các chữ số không giảm dần")
