# Chương trình so sánh diện tích
#
# Người dùng sẽ nhập vào:
# - Diện tích thứ nhất.
# - Diện tích thứ hai.
#
# Ví dụ:
# Nếu nhập:
# diện tích thứ nhất = 12
# diện tích thứ hai = 20
# Kết quả là: chương trình so sánh diện tích rồi in kết luận so sánh.
#
# Lưu ý:
# - Diện tích không được âm.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh hai giá trị đã nhập để đưa ra kết luận.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: so sánh diện tích.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

dien_tich_1 = float(input("Nhập diện tích thứ nhất: "))
dien_tich_2 = float(input("Nhập diện tích thứ hai: "))

if dien_tich_1 < 0 or dien_tich_2 < 0:
    print("Diện tích không được âm")
elif dien_tich_1 > dien_tich_2:
    print("Diện tích thứ nhất lớn hơn")
elif dien_tich_1 < dien_tich_2:
    print("Diện tích thứ hai lớn hơn")
else:
    print("Hai diện tích bằng nhau")
