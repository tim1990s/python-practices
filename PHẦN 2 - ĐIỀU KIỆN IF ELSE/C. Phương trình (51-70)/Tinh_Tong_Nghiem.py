# Chương trình tính tổng nghiệm của phương trình bậc hai
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
# Kết quả là: chương trình tính tổng nghiệm của phương trình bậc hai rồi in kết quả.
#
# Lưu ý:
# - Đây không phải là phương trình bậc hai.
# - Phương trình vô nghiệm trong tập số thực.
# - Delta quyết định số nghiệm thực của phương trình bậc hai.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Dùng hệ thức Viète để tính tổng nghiệm khi phương trình có nghiệm thực.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: tính tổng nghiệm của phương trình bậc hai.
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
    print("Đây không phải là phương trình bậc hai")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm trong tập số thực")
    else:
        tong = -b / a
        print("Tổng nghiệm là:", tong)
