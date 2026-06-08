# Chương trình xác định góc tù
#
# Người dùng sẽ nhập vào:
# - Số đo góc.
#
# Ví dụ:
# Nếu nhập:
# số đo góc = 120
# Kết quả là: chương trình xác định góc tù và in thông báo phù hợp.
#
# Lưu ý:
# - Đây không phải là góc tù.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh số đo góc với điều kiện của loại góc cần xác định.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: xác định góc tù.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goc = float(input("Nhập số đo góc: "))

if 90 < goc < 180:
    print("Đây là góc tù")
else:
    print("Đây không phải là góc tù")
