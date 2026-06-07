# Chương trình kiểm tra CCCD đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

cccd = input("Nhập số CCCD: ")

if len(cccd) == 12 and cccd.isdigit():
    print("CCCD hợp lệ")
else:
    print("CCCD không hợp lệ")
