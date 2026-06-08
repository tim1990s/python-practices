# Chương trình in hình kim cương
#
# Người dùng sẽ nhập vào:
# - Nửa chiều cao.
#
# Ví dụ:
# Nếu nhập:
# nửa chiều cao = 3
# Kết quả là: chương trình in hình kim cương theo dữ liệu đã nhập.
#
# Lưu ý:
# - Nửa chiều cao phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in hình kim cương.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập nửa chiều cao: "))

if n <= 0:
    print("Nửa chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
