# Chương trình kiểm tra số nghiệm của phương trình bậc hai
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
# Kết quả là: chương trình kiểm tra số nghiệm của phương trình bậc hai và in thông báo phù hợp.
#
# Lưu ý:
# - Phương trình có vô số nghiệm.
# - Phương trình vô nghiệm.
# - Phương trình vô nghiệm trong tập số thực.
# - Với phương trình bậc hai, hệ số a phải khác 0 để đúng dạng ax^2 + bx + c.
# - Delta quyết định số nghiệm thực của phương trình bậc hai.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Xét các trường hợp hệ số và Delta để xác định số nghiệm.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: kiểm tra số nghiệm của phương trình bậc hai.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm")
else:
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        print("Phương trình có hai nghiệm phân biệt")
    elif delta == 0:
        print("Phương trình có một nghiệm kép")
    else:
        print("Phương trình vô nghiệm trong tập số thực")
