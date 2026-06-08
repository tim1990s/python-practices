# Chương trình tính Delta của phương trình bậc hai
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
# Kết quả là: chương trình tính Delta của phương trình bậc hai rồi in kết quả.
#
# Lưu ý:
# - Với phương trình bậc hai, hệ số a phải khác 0 để đúng dạng ax^2 + bx + c.
# - Delta quyết định số nghiệm thực của phương trình bậc hai.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Tính Delta theo công thức b^2 - 4ac.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: tính Delta của phương trình bậc hai.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b ** 2 - 4 * a * c
print("Delta =", delta)
