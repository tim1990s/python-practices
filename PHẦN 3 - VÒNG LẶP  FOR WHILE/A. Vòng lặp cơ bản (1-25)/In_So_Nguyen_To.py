# Chương trình in các số nguyên tố từ 1 đến N
#
# Người dùng sẽ nhập vào:
# - Giá trị N.
#
# Ví dụ:
# Nếu nhập:
# N = 5
# Kết quả là: chương trình in các số nguyên tố từ 1 đến N theo dữ liệu đã nhập.
#
# Lưu ý:
# - Không có số nguyên tố nào.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in các số nguyên tố từ 1 đến N.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 2:
    print("Không có số nguyên tố nào")
else:
    for so in range(2, n + 1):
        la_nguyen_to = True

        for i in range(2, int(so ** 0.5) + 1):
            if so % i == 0:
                la_nguyen_to = False
                break

        if la_nguyen_to:
            print(so)
