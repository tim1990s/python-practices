# Chương trình xác định tuổi lao động đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

tuoi = int(input("Nhập tuổi: "))

if tuoi < 0:
    print("Tuổi không hợp lệ")
elif 15 <= tuoi <= 60:
    print("Đang trong độ tuổi lao động")
else:
    print("Không trong độ tuổi lao động")
