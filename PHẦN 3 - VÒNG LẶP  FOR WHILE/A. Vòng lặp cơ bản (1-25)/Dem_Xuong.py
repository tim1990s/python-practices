# Chương trình đếm xuống
#
# Người dùng sẽ nhập vào:
# - Số bắt đầu.
# - Số kết thúc.
#
# Ví dụ:
# Nếu nhập:
# số bắt đầu = 1
# số kết thúc = 5
# Kết quả là: chương trình đếm xuống rồi in số lượng đếm được.
#
# Lưu ý:
# - Số bắt đầu phải lớn hơn hoặc bằng số kết thúc.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp while để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: đếm xuống.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập số bắt đầu: "))
ket_thuc = int(input("Nhập số kết thúc: "))

if bat_dau < ket_thuc:
    print("Số bắt đầu phải lớn hơn hoặc bằng số kết thúc")
else:
    while bat_dau >= ket_thuc:
        print(bat_dau)
        bat_dau -= 1
