# Chương trình kiểm tra giao nhau của 2 đoạn thẳng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def huong(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def nam_tren_doan(ax, ay, bx, by, px, py):
    return min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)


x1 = float(input("Nhập x1: "))
y1 = float(input("Nhập y1: "))
x2 = float(input("Nhập x2: "))
y2 = float(input("Nhập y2: "))
x3 = float(input("Nhập x3: "))
y3 = float(input("Nhập y3: "))
x4 = float(input("Nhập x4: "))
y4 = float(input("Nhập y4: "))

d1 = huong(x1, y1, x2, y2, x3, y3)
d2 = huong(x1, y1, x2, y2, x4, y4)
d3 = huong(x3, y3, x4, y4, x1, y1)
d4 = huong(x3, y3, x4, y4, x2, y2)

if d1 == 0 and nam_tren_doan(x1, y1, x2, y2, x3, y3):
    print("Hai đoạn thẳng giao nhau")
elif d2 == 0 and nam_tren_doan(x1, y1, x2, y2, x4, y4):
    print("Hai đoạn thẳng giao nhau")
elif d3 == 0 and nam_tren_doan(x3, y3, x4, y4, x1, y1):
    print("Hai đoạn thẳng giao nhau")
elif d4 == 0 and nam_tren_doan(x3, y3, x4, y4, x2, y2):
    print("Hai đoạn thẳng giao nhau")
elif d1 * d2 < 0 and d3 * d4 < 0:
    print("Hai đoạn thẳng giao nhau")
else:
    print("Hai đoạn thẳng không giao nhau")
