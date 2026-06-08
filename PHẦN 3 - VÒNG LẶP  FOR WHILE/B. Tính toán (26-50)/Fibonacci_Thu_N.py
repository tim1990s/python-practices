# Chương trình tính Fibonacci thứ n
#
# Người dùng sẽ nhập vào:
# - Vị trí n.
#
# Ví dụ:
# Nếu nhập:
# vị trí n = 6
# Kết quả là: chương trình tính Fibonacci thứ n rồi in kết quả.
#
# Lưu ý:
# - n không được âm.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cập nhật hai giá trị liên tiếp của dãy Fibonacci sau mỗi vòng lặp.
# - Thực hiện yêu cầu: tính Fibonacci thứ n.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập vị trí n: "))

if n < 0:
    print("n không được âm")
else:
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    print("Fibonacci thứ", n, "là:", a)
