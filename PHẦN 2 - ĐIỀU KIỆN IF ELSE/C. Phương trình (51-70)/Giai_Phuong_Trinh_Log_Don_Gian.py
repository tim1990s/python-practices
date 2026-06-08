# Chương trình giải phương trình log đơn giản dạng log_a(x) = b
#
# Người dùng sẽ nhập vào:
# - Cơ số a.
# - Vế phải b.
#
# Ví dụ:
# Nếu nhập:
# cơ số a = 2
# vế phải b = 3
# Kết quả là: chương trình giải phương trình log đơn giản dạng log_a(x) = b rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Cơ số a phải lớn hơn 0 và khác 1.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Kiểm tra cơ số logarit rồi biến đổi log_a(x) = b thành x = a^b.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình log đơn giản dạng log_a(x) = b.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cơ số a: "))
b = float(input("Nhập vế phải b: "))

if a <= 0 or a == 1:
    print("Cơ số a phải lớn hơn 0 và khác 1")
else:
    x = a ** b
    print("Nghiệm của phương trình là x =", x)
