# Chương trình kiểm tra điều kiện nghiệm không làm mẫu bằng 0
#
# Người dùng sẽ nhập vào:
# - Nghiệm cần kiểm tra.
# - Hệ số a của mẫu.
# - Hệ số b của mẫu.
#
# Ví dụ:
# Nếu nhập:
# nghiệm cần kiểm tra = 2
# hệ số a của mẫu = 1
# hệ số b của mẫu = -3
# Kết quả là: chương trình kiểm tra điều kiện nghiệm không làm mẫu bằng 0 và in thông báo phù hợp.
#
# Lưu ý:
# - Nghiệm không thỏa điều kiện vì làm mẫu bằng 0.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Thay nghiệm vào mẫu số để kiểm tra có làm mẫu bằng 0 hay không.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: kiểm tra điều kiện nghiệm không làm mẫu bằng 0.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập nghiệm cần kiểm tra: "))
a = float(input("Nhập hệ số a của mẫu: "))
b = float(input("Nhập hệ số b của mẫu: "))

if a * x + b != 0:
    print("Nghiệm thỏa điều kiện")
else:
    print("Nghiệm không thỏa điều kiện vì làm mẫu bằng 0")
