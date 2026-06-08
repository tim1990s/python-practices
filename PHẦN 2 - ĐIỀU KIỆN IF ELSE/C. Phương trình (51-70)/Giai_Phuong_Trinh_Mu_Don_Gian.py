# Chương trình giải phương trình mũ đơn giản dạng a^x = b
#
# Người dùng sẽ nhập vào:
# - Cơ số a.
# - Vế phải b.
#
# Ví dụ:
# Nếu nhập:
# cơ số a = 2
# vế phải b = 8
# Kết quả là: chương trình giải phương trình mũ đơn giản dạng a^x = b rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Cơ số a phải lớn hơn 0 và khác 1.
# - Phương trình vô nghiệm.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Kiểm tra điều kiện cơ số và vế phải rồi dùng logarit để tìm x.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình mũ đơn giản dạng a^x = b.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập cơ số a: "))
b = float(input("Nhập vế phải b: "))

if a <= 0 or a == 1:
    print("Cơ số a phải lớn hơn 0 và khác 1")
elif b <= 0:
    print("Phương trình vô nghiệm")
else:
    x = math.log(b, a)
    print("Nghiệm của phương trình là x =", x)
