# Chương trình tính thuế thu nhập cá nhân đơn giản theo bậc

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

thu_nhap = float(input("Nhập thu nhập tính thuế: "))

if thu_nhap < 0:
    print("Thu nhập không được âm")
elif thu_nhap <= 5000000:
    thue = thu_nhap * 0.05
    print("Thuế thu nhập phải nộp là:", thue, "đồng")
elif thu_nhap <= 10000000:
    thue = 5000000 * 0.05 + (thu_nhap - 5000000) * 0.10
    print("Thuế thu nhập phải nộp là:", thue, "đồng")
elif thu_nhap <= 18000000:
    thue = 5000000 * 0.05 + 5000000 * 0.10 + (thu_nhap - 10000000) * 0.15
    print("Thuế thu nhập phải nộp là:", thue, "đồng")
else:
    thue = 5000000 * 0.05 + 5000000 * 0.10 + 8000000 * 0.15 + (thu_nhap - 18000000) * 0.20
    print("Thuế thu nhập phải nộp là:", thue, "đồng")
