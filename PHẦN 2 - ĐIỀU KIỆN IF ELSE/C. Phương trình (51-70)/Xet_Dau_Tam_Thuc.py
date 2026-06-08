# Chương trình xét dấu tam thức bậc hai a*x^2 + b*x + c
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
# - Hệ số c.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 1
# hệ số b = -3
# hệ số c = 2
# Kết quả là: chương trình xét dấu tam thức bậc hai a*x^2 + b*x + c rồi in khoảng dấu tương ứng.
#
# Lưu ý:
# - Đây không phải là tam thức bậc hai.
# - Với phương trình bậc hai, hệ số a phải khác 0 để đúng dạng ax^2 + bx + c.
# - Delta quyết định số nghiệm thực của phương trình bậc hai.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Dựa vào hệ số a, Delta và nghiệm để xét dấu tam thức.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: xét dấu tam thức bậc hai a*x^2 + b*x + c.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là tam thức bậc hai")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        if a > 0:
            print("Tam thức luôn dương với mọi x")
        else:
            print("Tam thức luôn âm với mọi x")
    elif delta == 0:
        x = -b / (2 * a)
        print("Tam thức bằng 0 tại x =", x)
        if a > 0:
            print("Tam thức dương với mọi x khác", x)
        else:
            print("Tam thức âm với mọi x khác", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Hai nghiệm là", x1, "và", x2)
        if a > 0:
            print("Tam thức dương ngoài khoảng hai nghiệm và âm trong khoảng hai nghiệm")
        else:
            print("Tam thức âm ngoài khoảng hai nghiệm và dương trong khoảng hai nghiệm")
