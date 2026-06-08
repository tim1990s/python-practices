# Chương trình xác định loại đa giác theo số cạnh
#
# Người dùng sẽ nhập vào:
# - Số cạnh của đa giác.
#
# Ví dụ:
# Nếu nhập:
# số cạnh của đa giác = 5
# Kết quả là: chương trình xác định loại đa giác theo số cạnh và in thông báo phù hợp.
#
# Lưu ý:
# - Không phải là đa giác.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dựa vào số cạnh để xác định loại đa giác.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: xác định loại đa giác theo số cạnh.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so_canh = int(input("Nhập số cạnh của đa giác: "))

if so_canh < 3:
    print("Không phải là đa giác")
elif so_canh == 3:
    print("Đây là tam giác")
elif so_canh == 4:
    print("Đây là tứ giác")
elif so_canh == 5:
    print("Đây là ngũ giác")
elif so_canh == 6:
    print("Đây là lục giác")
else:
    print("Đây là đa giác có", so_canh, "cạnh")
