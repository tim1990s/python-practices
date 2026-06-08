# Chương trình kiểm tra tam giác vuông
#
# Người dùng sẽ nhập vào:
# - Cạnh thứ nhất.
# - Cạnh thứ hai.
# - Cạnh thứ ba.
#
# Ví dụ:
# Nếu nhập:
# cạnh thứ nhất = 3
# cạnh thứ hai = 4
# cạnh thứ ba = 5
# Kết quả là: chương trình kiểm tra tam giác vuông và in thông báo phù hợp.
#
# Lưu ý:
# - Ba cạnh phải lớn hơn 0.
# - Ba cạnh không tạo thành tam giác.
# - Đây không phải là tam giác vuông.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Kiểm tra điều kiện tam giác rồi xét tiếp đặc điểm cạnh hoặc góc.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra tam giác vuông.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Ba cạnh phải lớn hơn 0")
elif not (a + b > c and a + c > b and b + c > a):
    print("Ba cạnh không tạo thành tam giác")
else:
    x, y, z = sorted([a, b, c])

    if abs(x * x + y * y - z * z) < 1e-9:
        print("Đây là tam giác vuông")
    else:
        print("Đây không phải là tam giác vuông")
