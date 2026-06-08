# Chương trình in các bội số đầu tiên của một số
#
# Người dùng sẽ nhập vào:
# - Số cần in bội số.
# - Số lượng bội số.
#
# Ví dụ:
# Nếu nhập:
# số cần in bội số = 3
# số lượng bội số = 5
# Kết quả là: chương trình in các bội số đầu tiên của một số theo dữ liệu đã nhập.
#
# Lưu ý:
# - Số lượng bội số phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in các bội số đầu tiên của một số.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so = int(input("Nhập số cần in bội số: "))
so_luong = int(input("Nhập số lượng bội số: "))

if so_luong <= 0:
    print("Số lượng bội số phải lớn hơn 0")
else:
    for i in range(1, so_luong + 1):
        print(so * i)
