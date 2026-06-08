# Chương trình giải phương trình lượng giác đơn giản sin(x) = a trên [0, 360]
#
# Người dùng sẽ nhập vào:
# - Giá trị a.
#
# Ví dụ:
# Nếu nhập:
# giá trị a = 0.5
# Kết quả là: chương trình giải phương trình lượng giác đơn giản sin(x) = a trên [0, 360] rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Phương trình vô nghiệm.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Kiểm tra miền giá trị của sin rồi tìm nghiệm trong đoạn [0, 360].
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình lượng giác đơn giản sin(x) = a trên [0, 360].
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập giá trị a: "))

if a < -1 or a > 1:
    print("Phương trình vô nghiệm")
else:
    goc_1 = math.degrees(math.asin(a))

    if goc_1 < 0:
        goc_1 += 360

    goc_2 = 180 - goc_1

    if goc_2 < 0:
        goc_2 += 360

    if abs(goc_1 - goc_2) < 1e-9:
        print("Nghiệm trong [0, 360] là x =", goc_1, "độ")
    else:
        print("Nghiệm trong [0, 360] là:")
        print("x1 =", goc_1, "độ")
        print("x2 =", goc_2, "độ")
