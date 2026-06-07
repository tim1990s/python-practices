# Chương trình xác định ca làm việc theo giờ bắt đầu

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

gio = int(input("Nhập giờ bắt đầu làm việc: "))

if gio < 0 or gio > 23:
    print("Giờ không hợp lệ")
elif 6 <= gio < 14:
    print("Ca sáng")
elif 14 <= gio < 22:
    print("Ca chiều")
else:
    print("Ca đêm")
