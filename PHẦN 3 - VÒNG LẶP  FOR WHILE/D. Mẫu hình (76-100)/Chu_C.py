# Chương trình in chữ C
#
# Người dùng sẽ nhập vào:
# - Kích thước chữ C.
#
# Ví dụ:
# Nếu nhập:
# kích thước chữ C = 5
# Kết quả là: chương trình in chữ C theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn hoặc bằng 3.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in chữ C.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước chữ C: "))

if n < 3:
    print("Kích thước phải lớn hơn hoặc bằng 3")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if i == 0 or i == n - 1 or j == 0:
                dong += "*"
            else:
                dong += " "

        print(dong)
