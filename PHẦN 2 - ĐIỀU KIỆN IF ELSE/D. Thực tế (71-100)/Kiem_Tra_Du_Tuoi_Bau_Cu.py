# Chương trình kiểm tra đủ tuổi bầu cử

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

tuoi = int(input("Nhập tuổi: "))

if tuoi < 0:
    print("Tuổi không hợp lệ")
elif tuoi >= 18:
    print("Đủ tuổi bầu cử")
else:
    print("Chưa đủ tuổi bầu cử")
