# Chương trình kiểm tra điểm nằm trong hình tròn
#
# Người dùng sẽ nhập vào:
# - Hoành độ điểm.
# - Tung độ điểm.
# - Hoành độ tâm.
# - Tung độ tâm.
# - Bán kính.
#
# Ví dụ:
# Nếu nhập:
# hoành độ điểm = 1
# tung độ điểm = 1
# hoành độ tâm = 0
# tung độ tâm = 0
# bán kính = 5
# Kết quả là: chương trình kiểm tra điểm nằm trong hình tròn và in thông báo phù hợp.
#
# Lưu ý:
# - Bán kính phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Tính khoảng cách từ điểm đến tâm và so sánh với bán kính.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra điểm nằm trong hình tròn.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập hoành độ điểm: "))
y = float(input("Nhập tung độ điểm: "))
x_tam = float(input("Nhập hoành độ tâm: "))
y_tam = float(input("Nhập tung độ tâm: "))
r = float(input("Nhập bán kính: "))

if r <= 0:
    print("Bán kính phải lớn hơn 0")
elif (x - x_tam) ** 2 + (y - y_tam) ** 2 <= r ** 2:
    print("Điểm nằm trong hoặc trên đường tròn")
else:
    print("Điểm nằm ngoài hình tròn")
