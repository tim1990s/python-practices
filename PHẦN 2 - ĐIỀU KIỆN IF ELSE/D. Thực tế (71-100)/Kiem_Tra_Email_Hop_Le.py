# Chương trình kiểm tra email hợp lệ đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re

email = input("Nhập email: ")
mau = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(mau, email):
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")
