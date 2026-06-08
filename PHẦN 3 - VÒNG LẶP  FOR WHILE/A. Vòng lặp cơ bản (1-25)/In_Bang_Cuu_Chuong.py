# Chương trình in bảng cửu chương
#
# Người dùng sẽ nhập vào:
# - Số cần in bảng cửu chương.
#
# Ví dụ:
# Nếu nhập:
# số cần in bảng cửu chương = 5
# Kết quả là: chương trình in bảng cửu chương theo dữ liệu đã nhập.
#
# Lưu ý:
# - Dữ liệu nhập cần đúng kiểu theo yêu cầu của từng dòng input.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in bảng cửu chương.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số cần in bảng cửu chương: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
