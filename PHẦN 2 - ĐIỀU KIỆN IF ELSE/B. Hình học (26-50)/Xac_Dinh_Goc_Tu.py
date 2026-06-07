# Chương trình xác định góc tù

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goc = float(input("Nhập số đo góc: "))

if 90 < goc < 180:
    print("Đây là góc tù")
else:
    print("Đây không phải là góc tù")
