# Chương trình in chữ N
#
# Người dùng sẽ nhập vào:
# - Kích thước.
#
# Ví dụ:
# Nếu nhập:
# kích thước = 5
# Kết quả là: chương trình in chữ N theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in chữ N.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if j == 0 or j == n - 1 or i == j:
                dong += "*"
            else:
                dong += " "

        print(dong)
