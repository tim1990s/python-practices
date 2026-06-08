# Chương trình in dãy Fibonacci
#
# Người dùng sẽ nhập vào:
# - Số lượng phần tử Fibonacci.
#
# Ví dụ:
# Nếu nhập:
# số lượng phần tử Fibonacci = 6
# Kết quả là: chương trình in dãy Fibonacci theo dữ liệu đã nhập.
#
# Lưu ý:
# - Số lượng phần tử phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cập nhật hai giá trị liên tiếp của dãy Fibonacci sau mỗi vòng lặp.
# - Thực hiện yêu cầu: in dãy Fibonacci.
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

    for _ in range(n):
        print(a)
        a, b = b, a + b
