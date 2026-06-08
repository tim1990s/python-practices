# Chương trình kiểm tra hai đường thẳng song song
#
# Người dùng sẽ nhập vào:
# - A1.
# - B1.
# - C1.
# - A2.
# - B2.
# - C2.
#
# Ví dụ:
# Nếu nhập:
# a1 = 1
# b1 = -1
# c1 = 0
# a2 = 2
# b2 = -2
# c2 = 3
# Kết quả là: chương trình kiểm tra hai đường thẳng song song và in thông báo phù hợp.
#
# Lưu ý:
# - Hệ số đường thẳng không hợp lệ.
# - Đường thẳng được nhập theo dạng hệ số a, b, c của phương trình ax + by + c = 0.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh hệ số của hai đường thẳng để xác định quan hệ song song.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: kiểm tra hai đường thẳng song song.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
    print("Hệ số đường thẳng không hợp lệ")
elif a1 * b2 == a2 * b1 and (a1 * c2 != a2 * c1 or b1 * c2 != b2 * c1):
    print("Hai đường thẳng song song")
else:
    print("Hai đường thẳng không song song")
