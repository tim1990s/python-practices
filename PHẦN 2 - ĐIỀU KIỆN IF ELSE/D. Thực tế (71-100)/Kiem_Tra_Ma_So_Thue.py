# Chương trình kiểm tra mã số thuế đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re

ma_so_thue = input("Nhập mã số thuế: ")

if re.match(r"^\d{10}$", ma_so_thue) or re.match(r"^\d{10}-\d{3}$", ma_so_thue):
    print("Mã số thuế hợp lệ")
else:
    print("Mã số thuế không hợp lệ")
