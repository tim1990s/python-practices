# Chương trình in các năm nhuận trong khoảng
#
# Người dùng sẽ nhập vào:
# - Năm bắt đầu.
# - Năm kết thúc.
#
# Ví dụ:
# Nếu nhập:
# năm bắt đầu = 2020
# năm kết thúc = 2024
# Kết quả là: chương trình in các năm nhuận trong khoảng theo dữ liệu đã nhập.
#
# Lưu ý:
# - Khoảng năm không hợp lệ.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng phép chia lấy dư và chia nguyên để xử lý từng chữ số.
# - Thực hiện yêu cầu: in các năm nhuận trong khoảng.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập năm bắt đầu: "))
ket_thuc = int(input("Nhập năm kết thúc: "))

if bat_dau <= 0 or ket_thuc <= 0 or bat_dau > ket_thuc:
    print("Khoảng năm không hợp lệ")
else:
    for nam in range(bat_dau, ket_thuc + 1):
        if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
            print(nam)
