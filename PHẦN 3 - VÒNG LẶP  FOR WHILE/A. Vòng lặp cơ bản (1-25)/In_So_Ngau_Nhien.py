# Chương trình in số ngẫu nhiên
#
# Người dùng sẽ nhập vào:
# - Số lượng số ngẫu nhiên.
# - Giá trị nhỏ nhất.
# - Giá trị lớn nhất.
#
# Ví dụ:
# Nếu nhập:
# số lượng số ngẫu nhiên = 5
# giá trị nhỏ nhất = 1
# giá trị lớn nhất = 10
# Kết quả là: chương trình in số ngẫu nhiên theo dữ liệu đã nhập.
#
# Lưu ý:
# - Dữ liệu không hợp lệ.
# - Mỗi lần chạy có thể cho kết quả khác nhau vì chương trình dùng số ngẫu nhiên.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in số ngẫu nhiên.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import random

so_luong = int(input("Nhập số lượng số ngẫu nhiên: "))
nho_nhat = int(input("Nhập giá trị nhỏ nhất: "))
lon_nhat = int(input("Nhập giá trị lớn nhất: "))

if so_luong <= 0 or nho_nhat > lon_nhat:
    print("Dữ liệu không hợp lệ")
else:
    for _ in range(so_luong):
        print(random.randint(nho_nhat, lon_nhat))
