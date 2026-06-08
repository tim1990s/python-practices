# Chương trình in chữ A
#
# Người dùng sẽ nhập vào:
# - Chiều cao chữ A.
#
# Ví dụ:
# Nếu nhập:
# chiều cao chữ A = 5
# Kết quả là: chương trình in chữ A theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều cao phải lớn hơn hoặc bằng 3.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in chữ A.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao chữ A: "))

if n < 3:
    print("Chiều cao phải lớn hơn hoặc bằng 3")
else:
    giua = n // 2

    for i in range(n):
        dong = ""

        for j in range(2 * n - 1):
            if j == n - 1 - i or j == n - 1 + i or i == giua and n - 1 - i <= j <= n - 1 + i:
                dong += "*"
            else:
                dong += " "

        print(dong)
