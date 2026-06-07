# Chương trình kiểm tra tháng hợp lệ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

thang = int(input("Nhập tháng: "))

if 1 <= thang <= 12:
    print("Tháng hợp lệ")
else:
    print("Tháng không hợp lệ")
