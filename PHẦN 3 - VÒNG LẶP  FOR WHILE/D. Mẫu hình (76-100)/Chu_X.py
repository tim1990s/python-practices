# Chương trình in chữ X
#
# Người dùng sẽ nhập vào:
# - Kích thước lẻ.
#
# Ví dụ:
# Nếu nhập:
# kích thước lẻ = 5
# Kết quả là: chương trình in chữ X theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in chữ X.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước lẻ: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if i == j or i + j == n - 1:
                dong += "*"
            else:
                dong += " "

        print(dong)
