# Chương trình chọn nghiệm nhỏ nhất của phương trình bậc hai
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
# - Hệ số c.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 1
# hệ số b = -3
# hệ số c = 2
# Kết quả là: chương trình chọn nghiệm nhỏ nhất của phương trình bậc hai rồi in nghiệm được chọn.
#
# Lưu ý:
# - Không có nghiệm hữu hạn để chọn.
# - Phương trình vô nghiệm trong tập số thực.
# - Với phương trình bậc hai, hệ số a phải khác 0 để đúng dạng ax^2 + bx + c.
# - Delta quyết định số nghiệm thực của phương trình bậc hai.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Tính nghiệm thực của phương trình rồi so sánh các nghiệm.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: chọn nghiệm nhỏ nhất của phương trình bậc hai.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        print("Không có nghiệm hữu hạn để chọn")
    else:
        x = -c / b
        print("Nghiệm nhỏ nhất là:", x)
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm trong tập số thực")
    elif delta == 0:
        x = -b / (2 * a)
        print("Nghiệm nhỏ nhất là:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Nghiệm nhỏ nhất là:", min(x1, x2))
