# Chương trình kiểm tra nghiệm thuộc tập xác định của biểu thức sqrt(a*x + b) / (c*x + d)
#
# Người dùng sẽ nhập vào:
# - Giá trị x.
# - Hệ số a trong căn.
# - Hệ số b trong căn.
# - Hệ số c ở mẫu.
# - Hệ số d ở mẫu.
#
# Ví dụ:
# Nếu nhập:
# giá trị x = 2
# hệ số a trong căn = 1
# hệ số b trong căn = 1
# hệ số c ở mẫu = 1
# hệ số d ở mẫu = -3
# Kết quả là: chương trình kiểm tra nghiệm thuộc tập xác định của biểu thức sqrt(a*x + b) / (c*x + d) và in thông báo phù hợp.
#
# Lưu ý:
# - x không thuộc tập xác định vì biểu thức trong căn âm.
# - x không thuộc tập xác định vì mẫu bằng 0.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Kiểm tra điều kiện trong căn và điều kiện mẫu khác 0.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: kiểm tra nghiệm thuộc tập xác định của biểu thức sqrt(a*x + b) / (c*x + d).
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập giá trị x: "))
a = float(input("Nhập hệ số a trong căn: "))
b = float(input("Nhập hệ số b trong căn: "))
c = float(input("Nhập hệ số c ở mẫu: "))
d = float(input("Nhập hệ số d ở mẫu: "))

if a * x + b < 0:
    print("x không thuộc tập xác định vì biểu thức trong căn âm")
elif c * x + d == 0:
    print("x không thuộc tập xác định vì mẫu bằng 0")
else:
    print("x thuộc tập xác định")
