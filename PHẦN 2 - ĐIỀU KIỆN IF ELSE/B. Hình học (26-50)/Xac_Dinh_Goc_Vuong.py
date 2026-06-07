# Chương trình xác định góc vuông

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goc = float(input("Nhập số đo góc: "))

if goc == 90:
    print("Đây là góc vuông")
else:
    print("Đây không phải là góc vuông")
