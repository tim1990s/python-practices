# Chương trình giải phương trình phân thức dạng (a*x + b) / (c*x + d) = 0
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
# - Hệ số c.
# - Hệ số d.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 2
# hệ số b = -4
# hệ số c = 1
# hệ số d = 3
# Kết quả là: chương trình giải phương trình phân thức dạng (a*x + b) / (c*x + d) = 0 rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Phương trình có vô số nghiệm, trừ các giá trị làm mẫu bằng 0.
# - Phương trình vô nghiệm.
# - Phương trình vô nghiệm vì nghiệm làm mẫu bằng 0.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Đưa tử số bằng 0 và loại nghiệm làm mẫu số bằng 0.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình phân thức dạng (a*x + b) / (c*x + d) = 0.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
d = float(input("Nhập hệ số d: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm, trừ các giá trị làm mẫu bằng 0")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a

    if c * x + d == 0:
        print("Phương trình vô nghiệm vì nghiệm làm mẫu bằng 0")
    else:
        print("Nghiệm của phương trình là x =", x)
