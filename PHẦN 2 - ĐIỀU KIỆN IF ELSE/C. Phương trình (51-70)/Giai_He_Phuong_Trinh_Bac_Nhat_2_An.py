# Chương trình giải hệ phương trình bậc nhất 2 ẩn
#
# Người dùng sẽ nhập vào:
# - A1.
# - B1.
# - C1.
# - A2.
# - B2.
# - C2.
#
# Ví dụ:
# Nếu nhập:
# a1 = 1
# b1 = 1
# c1 = 3
# a2 = 1
# b2 = -1
# c2 = 1
# Kết quả là: chương trình giải hệ phương trình bậc nhất 2 ẩn rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Hệ phương trình có vô số nghiệm.
# - Hệ phương trình vô nghiệm.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Tính các định thức và xét từng trường hợp nghiệm của hệ.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải hệ phương trình bậc nhất 2 ẩn.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1
dy = a1 * c2 - a2 * c1

if d != 0:
    x = dx / d
    y = dy / d
    print("Hệ phương trình có nghiệm x =", x, "và y =", y)
elif dx == 0 and dy == 0:
    print("Hệ phương trình có vô số nghiệm")
else:
    print("Hệ phương trình vô nghiệm")
