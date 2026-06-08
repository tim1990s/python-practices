# Chương trình in mẫu sao hình vuông
#
# Người dùng sẽ nhập vào:
# - Kích thước mẫu sao.
#
# Ví dụ:
# Nếu nhập:
# kích thước mẫu sao = 4
# Kết quả là: chương trình in mẫu sao hình vuông theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in mẫu sao hình vuông.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước mẫu sao: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for _ in range(n):
        print("* " * n)
