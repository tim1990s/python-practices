# Chương trình kiểm tra số palindrome
#
# Người dùng sẽ nhập vào:
# - Số nguyên.
#
# Ví dụ:
# Nếu nhập:
# số nguyên = 12321
# Kết quả là: chương trình kiểm tra số palindrome và in thông báo phù hợp.
#
# Lưu ý:
# - Nếu nhập số âm, chương trình xử lý phần trị tuyệt đối khi làm việc với chữ số.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: kiểm tra số palindrome.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
la_palindrome = True

for i in range(len(chuoi) // 2):
    if chuoi[i] != chuoi[len(chuoi) - 1 - i]:
        la_palindrome = False
        break

if la_palindrome:
    print(n, "là số palindrome")
else:
    print(n, "không phải là số palindrome")
