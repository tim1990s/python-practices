# Chương trình tính tổng nghịch đảo 1 + 1/2 + ... + 1/N
#
# Người dùng sẽ nhập vào:
# - Giá trị N.
#
# Ví dụ:
# Nếu nhập:
# N = 5
# Kết quả là: chương trình tính tổng nghịch đảo 1 + 1/2 + ... + 1/N rồi in kết quả.
#
# Lưu ý:
# - N phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tính tổng nghịch đảo 1 + 1/2 + ... + 1/N.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n <= 0:
    print("N phải lớn hơn 0")
else:
    tong = 0

    for i in range(1, n + 1):
        tong += 1 / i

    print("Tổng nghịch đảo là:", tong)
