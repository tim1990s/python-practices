# Chương trình đếm bit 1 trong biểu diễn nhị phân
#
# Người dùng sẽ nhập vào:
# - Số nguyên không âm.
#
# Ví dụ:
# Nếu nhập:
# số nguyên không âm = 10
# Kết quả là: chương trình đếm bit 1 trong biểu diễn nhị phân rồi in số lượng đếm được.
#
# Lưu ý:
# - Số phải không âm.
# - Chuỗi nhị phân hợp lệ chỉ gồm các ký tự 0 và 1.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp while để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: đếm bit 1 trong biểu diễn nhị phân.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Số phải không âm")
else:
    dem = 0

    while n > 0:
        if n % 2 == 1:
            dem += 1

        n //= 2

    print("Số bit 1 là:", dem)
