# Chương trình kiểm tra điểm nằm trong hình chữ nhật
#
# Người dùng sẽ nhập vào:
# - Hoành độ điểm.
# - Tung độ điểm.
# - X nhỏ nhất của hình chữ nhật.
# - Y nhỏ nhất của hình chữ nhật.
# - X lớn nhất của hình chữ nhật.
# - Y lớn nhất của hình chữ nhật.
#
# Ví dụ:
# Nếu nhập:
# hoành độ điểm = 1
# tung độ điểm = 1
# x nhỏ nhất của hình chữ nhật = 0
# y nhỏ nhất của hình chữ nhật = 0
# x lớn nhất của hình chữ nhật = 5
# y lớn nhất của hình chữ nhật = 4
# Kết quả là: chương trình kiểm tra điểm nằm trong hình chữ nhật và in thông báo phù hợp.
#
# Lưu ý:
# - Tọa độ hình chữ nhật không hợp lệ.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Kiểm tra tọa độ điểm có nằm trong giới hạn của hình chữ nhật hay không.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra điểm nằm trong hình chữ nhật.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập hoành độ điểm: "))
y = float(input("Nhập tung độ điểm: "))
x_min = float(input("Nhập x nhỏ nhất của hình chữ nhật: "))
y_min = float(input("Nhập y nhỏ nhất của hình chữ nhật: "))
x_max = float(input("Nhập x lớn nhất của hình chữ nhật: "))
y_max = float(input("Nhập y lớn nhất của hình chữ nhật: "))

if x_min > x_max or y_min > y_max:
    print("Tọa độ hình chữ nhật không hợp lệ")
elif x_min <= x <= x_max and y_min <= y <= y_max:
    print("Điểm nằm trong hoặc trên cạnh hình chữ nhật")
else:
    print("Điểm nằm ngoài hình chữ nhật")
