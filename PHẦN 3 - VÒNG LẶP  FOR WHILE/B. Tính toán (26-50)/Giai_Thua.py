# Chương trình tính giai thừa
#
# Người dùng sẽ nhập vào:
# - Giá trị N.
#
# Ví dụ:
# Nếu nhập:
# N = 5
# Kết quả là: chương trình tính giai thừa rồi in kết quả.
#
# Lưu ý:
# - N không được âm.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tính giai thừa.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

giai_thua = 1

if n < 0:
    print("N không được âm")
else:
    for i in range(1, n + 1):
        giai_thua *= i

    print(n, "! =", giai_thua)
