# Chương trình chọn hình nhỏ nhất theo diện tích
#
# Người dùng sẽ nhập vào:
# - Diện tích hình thứ nhất.
# - Diện tích hình thứ hai.
# - Diện tích hình thứ ba.
#
# Ví dụ:
# Nếu nhập:
# diện tích hình thứ nhất = 12
# diện tích hình thứ hai = 20
# diện tích hình thứ ba = 15
# Kết quả là: chương trình chọn hình nhỏ nhất theo diện tích rồi in hình được chọn.
#
# Lưu ý:
# - Diện tích không được âm.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh các giá trị diện tích để chọn hình phù hợp.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: chọn hình nhỏ nhất theo diện tích.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

dien_tich_1 = float(input("Nhập diện tích hình thứ nhất: "))
dien_tich_2 = float(input("Nhập diện tích hình thứ hai: "))
dien_tich_3 = float(input("Nhập diện tích hình thứ ba: "))

if dien_tich_1 < 0 or dien_tich_2 < 0 or dien_tich_3 < 0:
    print("Diện tích không được âm")
elif dien_tich_1 <= dien_tich_2 and dien_tich_1 <= dien_tich_3:
    print("Hình thứ nhất nhỏ nhất")
elif dien_tich_2 <= dien_tich_1 and dien_tich_2 <= dien_tich_3:
    print("Hình thứ hai nhỏ nhất")
else:
    print("Hình thứ ba nhỏ nhất")
