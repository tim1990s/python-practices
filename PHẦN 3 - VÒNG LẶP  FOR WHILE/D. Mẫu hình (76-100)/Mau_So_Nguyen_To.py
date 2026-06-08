# Chương trình in mẫu số nguyên tố
#
# Người dùng sẽ nhập vào:
# - Số dòng.
#
# Ví dụ:
# Nếu nhập:
# số dòng = 5
# Kết quả là: chương trình in mẫu số nguyên tố theo dữ liệu đã nhập.
#
# Lưu ý:
# - Số dòng phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in mẫu số nguyên tố.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số dòng: "))

if n <= 0:
    print("Số dòng phải lớn hơn 0")
else:
    so = 2

    for i in range(1, n + 1):
        dong = ""

        for _ in range(i):
            while True:
                la_nguyen_to = True

                for uoc in range(2, int(so ** 0.5) + 1):
                    if so % uoc == 0:
                        la_nguyen_to = False
                        break

                if la_nguyen_to:
                    dong += str(so) + " "
                    so += 1
                    break

                so += 1

        print(dong)
