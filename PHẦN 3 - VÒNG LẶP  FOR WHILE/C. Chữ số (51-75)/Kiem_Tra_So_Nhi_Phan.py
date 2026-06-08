# Chương trình kiểm tra số nhị phân
#
# Người dùng sẽ nhập vào:
# - Chuỗi cần kiểm tra.
#
# Ví dụ:
# Nếu nhập:
# chuỗi cần kiểm tra = 10110
# Kết quả là: chương trình kiểm tra số nhị phân và in thông báo phù hợp.
#
# Lưu ý:
# - Đây không phải là số nhị phân.
# - Chuỗi nhị phân hợp lệ chỉ gồm các ký tự 0 và 1.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: kiểm tra số nhị phân.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập chuỗi cần kiểm tra: ")
hop_le = chuoi != ""

for ky_tu in chuoi:
    if ky_tu not in "01":
        hop_le = False
        break

if hop_le:
    print("Đây là số nhị phân")
else:
    print("Đây không phải là số nhị phân")
