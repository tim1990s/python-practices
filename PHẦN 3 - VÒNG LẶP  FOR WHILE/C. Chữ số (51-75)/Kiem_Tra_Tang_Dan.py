# Chương trình kiểm tra chữ số tăng dần

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
la_tang_dan = True

for i in range(len(chuoi) - 1):
    if chuoi[i] >= chuoi[i + 1]:
        la_tang_dan = False
        break

if la_tang_dan:
    print("Các chữ số tăng dần")
else:
    print("Các chữ số không tăng dần")
