# Chương trình in hình chữ nhật rỗng
#
# Người dùng sẽ nhập vào:
# - Chiều dài.
# - Chiều rộng.
#
# Ví dụ:
# Nếu nhập:
# chiều dài = 6
# chiều rộng = 4
# Kết quả là: chương trình in hình chữ nhật rỗng theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in hình chữ nhật rỗng.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))

if chieu_dai <= 0 or chieu_rong <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    for i in range(chieu_rong):
        dong = ""

        for j in range(chieu_dai):
            if i == 0 or i == chieu_rong - 1 or j == 0 or j == chieu_dai - 1:
                dong += "*"
            else:
                dong += " "

        print(dong)
