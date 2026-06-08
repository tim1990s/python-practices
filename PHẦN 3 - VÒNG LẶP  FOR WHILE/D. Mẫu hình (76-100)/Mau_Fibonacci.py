# Chương trình in mẫu Fibonacci
#
# Người dùng sẽ nhập vào:
# - Số dòng.
#
# Ví dụ:
# Nếu nhập:
# số dòng = 5
# Kết quả là: chương trình in mẫu Fibonacci theo dữ liệu đã nhập.
#
# Lưu ý:
# - Số dòng phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cập nhật hai giá trị liên tiếp của dãy Fibonacci sau mỗi vòng lặp.
# - Thực hiện yêu cầu: in mẫu Fibonacci.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    a = 0
    b = 1

    for i in range(1, n + 1):
        dong = ""

        for _ in range(i):
            dong += str(a) + " "
            a, b = b, a + b

        print(dong)
