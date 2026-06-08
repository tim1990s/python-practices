# Chương trình in chữ B
#
# Người dùng sẽ nhập vào:
# - Chiều cao chữ B.
#
# Ví dụ:
# Nếu nhập:
# chiều cao chữ B = 5
# Kết quả là: chương trình in chữ B theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều cao phải lớn hơn hoặc bằng 5.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in chữ B.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao chữ B: "))

if n < 5:
    print("Chiều cao phải lớn hơn hoặc bằng 5")
else:
    for i in range(n):
        dong = ""

        for j in range(n):
            if j == 0 or (i == 0 or i == n // 2 or i == n - 1) and j < n - 1 or j == n - 1 and i not in [0, n // 2, n - 1]:
                dong += "*"
            else:
                dong += " "

        print(dong)
