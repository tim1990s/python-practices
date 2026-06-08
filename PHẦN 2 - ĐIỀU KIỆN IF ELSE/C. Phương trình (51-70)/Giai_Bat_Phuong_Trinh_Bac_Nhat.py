# Chương trình giải bất phương trình bậc nhất dạng a*x + b > 0
#
# Người dùng sẽ nhập vào:
# - Hệ số a.
# - Hệ số b.
#
# Ví dụ:
# Nếu nhập:
# hệ số a = 2
# hệ số b = -4
# Kết quả là: chương trình giải bất phương trình bậc nhất dạng a*x + b > 0 rồi in nghiệm hoặc kết luận phù hợp.
#
# Lưu ý:
# - Bất phương trình vô nghiệm.
# - Khi hệ số a bằng 0, cần xét riêng điều kiện của hằng số b.
#
# Ý tưởng:
# - Nhập các hệ số hoặc giá trị cần kiểm tra từ bàn phím.
# - Kiểm tra các trường hợp đặc biệt và điều kiện xác định trước khi tính nghiệm.
# - Xét dấu hệ số a để đổi chiều hoặc giữ chiều bất phương trình khi chia.
# - Dùng câu lệnh if/elif/else để chọn nhánh xử lý đúng.
# - Thực hiện yêu cầu: giải bất phương trình bậc nhất dạng a*x + b > 0.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b > 0:
        print("Bất phương trình đúng với mọi x")
    else:
        print("Bất phương trình vô nghiệm")
elif a > 0:
    print("Nghiệm của bất phương trình là x >", -b / a)
else:
    print("Nghiệm của bất phương trình là x <", -b / a)
