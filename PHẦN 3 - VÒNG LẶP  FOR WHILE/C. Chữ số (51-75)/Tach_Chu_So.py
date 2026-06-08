# Chương trình tách từng chữ số
#
# Người dùng sẽ nhập vào:
# - Số nguyên.
#
# Ví dụ:
# Nếu nhập:
# số nguyên = 12345
# Kết quả là: chương trình thực hiện yêu cầu tách từng chữ số.
#
# Lưu ý:
# - Nếu nhập số âm, chương trình xử lý phần trị tuyệt đối khi làm việc với chữ số.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Dùng phép chia lấy dư và chia nguyên để xử lý từng chữ số.
# - Thực hiện yêu cầu: tách từng chữ số.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))

for chu_so in chuoi:
    print(chu_so)
