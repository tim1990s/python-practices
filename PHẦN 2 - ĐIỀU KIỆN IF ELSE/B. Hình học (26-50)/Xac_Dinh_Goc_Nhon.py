# Chương trình xác định góc nhọn
#
# Người dùng sẽ nhập vào:
# - Số đo góc.
#
# Ví dụ:
# Nếu nhập:
# số đo góc = 45
# Kết quả là: chương trình xác định góc nhọn và in thông báo phù hợp.
#
# Lưu ý:
# - Đây không phải là góc nhọn.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh số đo góc với điều kiện của loại góc cần xác định.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: xác định góc nhọn.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goc = float(input("Nhập số đo góc: "))

if 0 < goc < 90:
    print("Đây là góc nhọn")
else:
    print("Đây không phải là góc nhọn")
