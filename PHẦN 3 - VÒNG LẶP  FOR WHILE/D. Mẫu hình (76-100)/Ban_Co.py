# Chương trình in mẫu bàn cờ
#
# Người dùng sẽ nhập vào:
# - Kích thước bàn cờ.
#
# Ví dụ:
# Nếu nhập:
# kích thước bàn cờ = 4
# Kết quả là: chương trình in mẫu bàn cờ theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in mẫu bàn cờ.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước bàn cờ: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if (i + j) % 2 == 0:
                dong += "* "
            else:
                dong += "  "

        print(dong)
