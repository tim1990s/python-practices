# Chương trình kiểm tra số điện thoại Việt Nam đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re

so_dien_thoai = input("Nhập số điện thoại: ")

if re.match(r"^0\d{9}$", so_dien_thoai):
    print("Số điện thoại hợp lệ")
else:
    print("Số điện thoại không hợp lệ")
