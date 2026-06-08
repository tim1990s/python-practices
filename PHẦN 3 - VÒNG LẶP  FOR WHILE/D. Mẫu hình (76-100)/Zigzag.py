# Chương trình in mẫu zigzag
#
# Người dùng sẽ nhập vào:
# - Chiều rộng.
#
# Ví dụ:
# Nếu nhập:
# chiều rộng = 4
# Kết quả là: chương trình in mẫu zigzag theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều rộng phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in mẫu zigzag.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều rộng: "))

if n <= 0:
    print("Chiều rộng phải lớn hơn 0")
else:
    for i in range(3):
        dong = ""

        for j in range(n):
            if (j + i) % 4 == 0 or (j - i) % 4 == 0:
                dong += "*"
            else:
                dong += " "

        print(dong)
