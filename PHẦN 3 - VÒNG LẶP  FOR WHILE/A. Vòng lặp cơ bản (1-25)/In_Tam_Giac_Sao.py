# Chương trình in tam giác sao
#
# Người dùng sẽ nhập vào:
# - Chiều cao tam giác sao.
#
# Ví dụ:
# Nếu nhập:
# chiều cao tam giác sao = 5
# Kết quả là: chương trình in tam giác sao theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều cao phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in tam giác sao.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao tam giác sao: "))

if n <= 0:
    print("Chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        print("* " * i)
