# Chương trình tìm bit cao nhất trong biểu diễn nhị phân
#
# Người dùng sẽ nhập vào:
# - Số nguyên dương.
#
# Ví dụ:
# Nếu nhập:
# số nguyên dương = 10
# Kết quả là: chương trình tìm bit cao nhất trong biểu diễn nhị phân rồi in giá trị tìm được.
#
# Lưu ý:
# - Số phải lớn hơn 0.
# - Chuỗi nhị phân hợp lệ chỉ gồm các ký tự 0 và 1.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp while để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tìm bit cao nhất trong biểu diễn nhị phân.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên dương: "))

if n <= 0:
    print("Số phải lớn hơn 0")
else:
    vi_tri = 0
    gia_tri = 1

    while gia_tri * 2 <= n:
        gia_tri *= 2
        vi_tri += 1

    print("Bit cao nhất ở vị trí:", vi_tri)
    print("Giá trị bit cao nhất là:", gia_tri)
