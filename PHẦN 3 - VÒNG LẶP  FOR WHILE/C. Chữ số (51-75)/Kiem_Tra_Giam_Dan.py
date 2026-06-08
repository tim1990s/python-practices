# Chương trình kiểm tra chữ số giảm dần
#
# Người dùng sẽ nhập vào:
# - Số nguyên.
#
# Ví dụ:
# Nếu nhập:
# số nguyên = 54321
# Kết quả là: chương trình kiểm tra chữ số giảm dần và in thông báo phù hợp.
#
# Lưu ý:
# - Nếu nhập số âm, chương trình xử lý phần trị tuyệt đối khi làm việc với chữ số.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Dùng phép chia lấy dư và chia nguyên để xử lý từng chữ số.
# - Thực hiện yêu cầu: kiểm tra chữ số giảm dần.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
la_giam_dan = True

for i in range(len(chuoi) - 1):
    if chuoi[i] <= chuoi[i + 1]:
        la_giam_dan = False
        break

if la_giam_dan:
    print("Các chữ số giảm dần")
else:
    print("Các chữ số không giảm dần")
