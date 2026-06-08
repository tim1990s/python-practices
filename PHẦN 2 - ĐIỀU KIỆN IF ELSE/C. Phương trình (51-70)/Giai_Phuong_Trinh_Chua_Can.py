# Chương trình giải phương trình chứa căn dạng sqrt(a*x + b) = c
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
# - Vế phải c.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 2
# hệ số b = 1
# vế phải c = 3
# Kết quả là: chương trình giải phương trình chứa căn dạng sqrt(a*x + b) = c rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Phương trình vô nghiệm vì căn bậc hai không âm.
# - Phương trình có vô số nghiệm.
# - Phương trình vô nghiệm.
# - Biểu thức trong căn bậc hai phải lớn hơn hoặc bằng 0.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Kiểm tra điều kiện căn rồi bình phương hoặc biến đổi về phương trình đơn giản hơn.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình chứa căn dạng sqrt(a*x + b) = c.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập vế phải c: "))

if c < 0:
    print("Phương trình vô nghiệm vì căn bậc hai không âm")
elif a == 0:
    if b >= 0 and math.sqrt(b) == c:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = (c ** 2 - b) / a

    if a * x + b >= 0:
        print("Nghiệm của phương trình là x =", x)
    else:
        print("Phương trình vô nghiệm")
