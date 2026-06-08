# Chương trình in bình phương các số từ 1 đến N
#
# Người dùng sẽ nhập vào:
# - Giá trị N.
#
# Ví dụ:
# Nếu nhập:
# N = 5
# Kết quả là: chương trình in bình phương các số từ 1 đến N theo dữ liệu đã nhập.
#
# Lưu ý:
# - N phải lớn hơn hoặc bằng 1.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in bình phương các số từ 1 đến N.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 1:
    print("N phải lớn hơn hoặc bằng 1")
else:
    for i in range(1, n + 1):
        print(i, "^ 2 =", i ** 2)
