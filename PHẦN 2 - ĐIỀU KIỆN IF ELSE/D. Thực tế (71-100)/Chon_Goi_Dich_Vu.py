# Chương trình chọn gói dịch vụ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

nhu_cau = input("Nhập nhu cầu (co ban/tieu chuan/cao cap): ").lower()

if nhu_cau == "co ban":
    print("Chọn gói Cơ bản")
elif nhu_cau == "tieu chuan":
    print("Chọn gói Tiêu chuẩn")
elif nhu_cau == "cao cap":
    print("Chọn gói Cao cấp")
else:
    print("Nhu cầu không hợp lệ")
