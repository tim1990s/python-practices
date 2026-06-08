# Chương trình in tam giác số
#
# Người dùng sẽ nhập vào:
# - Chiều cao.
#
# Ví dụ:
# Nếu nhập:
# chiều cao = 5
# Kết quả là: chương trình in tam giác số theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều cao phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in tam giác số.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao: "))

if n <= 0:
    print("Chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        dong = ""

        for j in range(1, i + 1):
            dong += str(j) + " "

        print(dong)
