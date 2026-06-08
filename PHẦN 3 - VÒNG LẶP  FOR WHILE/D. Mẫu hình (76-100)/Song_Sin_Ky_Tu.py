# Chương trình in sóng sin ký tự đơn giản
#
# Người dùng sẽ nhập vào:
# - Chiều dài sóng.
#
# Ví dụ:
# Nếu nhập:
# chiều dài sóng = 12
# Kết quả là: chương trình in sóng sin ký tự đơn giản theo dữ liệu đã nhập.
#
# Lưu ý:
# - Chiều dài phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in sóng sin ký tự đơn giản.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều dài sóng: "))

if n <= 0:
    print("Chiều dài phải lớn hơn 0")
else:
    for hang in range(3):
        dong = ""

        for cot in range(n):
            vi_tri = cot % 4

            if (hang == 0 and vi_tri == 1) or (hang == 1 and (vi_tri == 0 or vi_tri == 2)) or (hang == 2 and vi_tri == 3):
                dong += "*"
            else:
                dong += " "

        print(dong)
