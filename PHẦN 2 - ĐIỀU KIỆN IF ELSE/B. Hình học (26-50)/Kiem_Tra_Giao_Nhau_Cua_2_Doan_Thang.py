# Chương trình kiểm tra giao nhau của 2 đoạn thẳng
#
# Người dùng sẽ nhập vào:
# - X1.
# - Y1.
# - X2.
# - Y2.
# - X3.
# - Y3.
# - X4.
# - Y4.
#
# Ví dụ:
# Nếu nhập:
# x1 = 0
# y1 = 0
# x2 = 4
# y2 = 4
# x3 = 0
# y3 = 4
# x4 = 4
# y4 = 0
# Kết quả là: chương trình kiểm tra giao nhau của 2 đoạn thẳng và in thông báo phù hợp.
#
# Lưu ý:
# - Mỗi đoạn thẳng được xác định bởi hai điểm đầu mút.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Dùng điều kiện định hướng điểm để kiểm tra hai đoạn thẳng có giao nhau hay không.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra giao nhau của 2 đoạn thẳng.
# - In kết quả ra màn hình.

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
