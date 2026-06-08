# Chương trình in bảng ASCII trong một khoảng mã
#
# Người dùng sẽ nhập vào:
# - Mã ASCII bắt đầu.
# - Mã ASCII kết thúc.
#
# Ví dụ:
# Nếu nhập:
# mã ASCII bắt đầu = 65
# mã ASCII kết thúc = 70
# Kết quả là: chương trình in bảng ASCII trong một khoảng mã theo dữ liệu đã nhập.
#
# Lưu ý:
# - Khoảng mã ASCII không hợp lệ.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in bảng ASCII trong một khoảng mã.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập mã ASCII bắt đầu: "))
ket_thuc = int(input("Nhập mã ASCII kết thúc: "))

if bat_dau < 0 or ket_thuc < 0 or bat_dau > ket_thuc:
    print("Khoảng mã ASCII không hợp lệ")
else:
    for ma in range(bat_dau, ket_thuc + 1):
        print(ma, "=", chr(ma))
