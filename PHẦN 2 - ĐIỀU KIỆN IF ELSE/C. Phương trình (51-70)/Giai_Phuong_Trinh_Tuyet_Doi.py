# Chương trình giải phương trình tuyệt đối dạng |a*x + b| = c
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
# - Vế phải c.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 2
# hệ số b = -4
# vế phải c = 6
# Kết quả là: chương trình giải phương trình tuyệt đối dạng |a*x + b| = c rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Phương trình vô nghiệm.
# - Phương trình có vô số nghiệm.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Tách phương trình trị tuyệt đối thành các trường hợp tuyến tính.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải phương trình tuyệt đối dạng |a*x + b| = c.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập vế phải c: "))

if c < 0:
    print("Phương trình vô nghiệm")
elif a == 0:
    if abs(b) == c:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
elif c == 0:
    x = -b / a
    print("Phương trình có nghiệm x =", x)
else:
    x1 = (c - b) / a
    x2 = (-c - b) / a
    print("Phương trình có hai nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)
