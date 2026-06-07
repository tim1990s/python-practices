# Chương trình xác định góc nhọn

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goc = float(input("Nhập số đo góc: "))

if 0 < goc < 90:
    print("Đây là góc nhọn")
else:
    print("Đây không phải là góc nhọn")
