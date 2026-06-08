# Chương trình tìm chữ số lớn nhất
#
# Người dùng sẽ nhập vào:
# - Số nguyên.
#
# Ví dụ:
# Nếu nhập:
# số nguyên = 12345
# Kết quả là: chương trình tìm chữ số lớn nhất rồi in giá trị tìm được.
#
# Lưu ý:
# - Nếu nhập số âm, chương trình xử lý phần trị tuyệt đối khi làm việc với chữ số.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Dùng phép chia lấy dư và chia nguyên để xử lý từng chữ số.
# - Thực hiện yêu cầu: tìm chữ số lớn nhất.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
so = abs(n)
lon_nhat = 0

if so == 0:
    lon_nhat = 0
else:
    while so > 0:
        chu_so = so % 10

        if chu_so > lon_nhat:
            lon_nhat = chu_so

        so //= 10

print("Chữ số lớn nhất là:", lon_nhat)
