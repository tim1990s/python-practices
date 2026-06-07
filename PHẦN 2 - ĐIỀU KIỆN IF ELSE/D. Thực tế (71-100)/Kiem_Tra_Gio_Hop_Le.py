# Chương trình kiểm tra giờ hợp lệ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))

if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Giờ hợp lệ")
else:
    print("Giờ không hợp lệ")
