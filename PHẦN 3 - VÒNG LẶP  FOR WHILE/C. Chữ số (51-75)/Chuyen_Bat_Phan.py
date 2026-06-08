# Chương trình chuyển số thập phân sang bát phân
#
# Người dùng sẽ nhập vào:
# - Số nguyên không âm.
#
# Ví dụ:
# Nếu nhập:
# số nguyên không âm = 10
# Kết quả là: chương trình chuyển số thập phân sang bát phân rồi in dạng sau khi chuyển.
#
# Lưu ý:
# - Số phải không âm.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp while để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: chuyển số thập phân sang bát phân.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Số phải không âm")
elif n == 0:
    print("Bát phân là: 0")
else:
    ket_qua = ""

    while n > 0:
        ket_qua = str(n % 8) + ket_qua
        n //= 8

    print("Bát phân là:", ket_qua)
