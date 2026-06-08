# Chương trình tính tổng n số Fibonacci đầu tiên
#
# Người dùng sẽ nhập vào:
# - Số lượng phần tử Fibonacci.
#
# Ví dụ:
# Nếu nhập:
# số lượng phần tử Fibonacci = 6
# Kết quả là: chương trình tính tổng n số Fibonacci đầu tiên rồi in kết quả.
#
# Lưu ý:
# - Số lượng phần tử phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cập nhật hai giá trị liên tiếp của dãy Fibonacci sau mỗi vòng lặp.
# - Thực hiện yêu cầu: tính tổng n số Fibonacci đầu tiên.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử Fibonacci: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    a = 0
    b = 1
    tong = 0

    for _ in range(n):
        tong += a
        a, b = b, a + b

    print("Tổng Fibonacci là:", tong)
