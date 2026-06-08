# Chương trình kiểm tra hình thoi
#
# Người dùng sẽ nhập vào:
# - Cạnh thứ nhất.
# - Cạnh thứ hai.
# - Cạnh thứ ba.
# - Cạnh thứ tư.
#
# Ví dụ:
# Nếu nhập:
# cạnh thứ nhất = 3
# cạnh thứ hai = 4
# cạnh thứ ba = 5
# cạnh thứ tư = 4
# Kết quả là: chương trình kiểm tra hình thoi và in thông báo phù hợp.
#
# Lưu ý:
# - Bốn cạnh phải lớn hơn 0.
# - Đây không phải là hình thoi.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Kiểm tra các điều kiện cạnh và góc đặc trưng của hình.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra hình thoi.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
d = float(input("Nhập cạnh thứ tư: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Bốn cạnh phải lớn hơn 0")
elif a == b == c == d:
    print("Đây là hình thoi")
else:
    print("Đây không phải là hình thoi")
