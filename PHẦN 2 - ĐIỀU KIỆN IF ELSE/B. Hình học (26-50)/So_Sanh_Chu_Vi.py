# Chương trình so sánh chu vi
#
# Người dùng sẽ nhập vào:
# - Chu vi thứ nhất.
# - Chu vi thứ hai.
#
# Ví dụ:
# Nếu nhập:
# chu vi thứ nhất = 14
# chu vi thứ hai = 18
# Kết quả là: chương trình so sánh chu vi rồi in kết luận so sánh.
#
# Lưu ý:
# - Chu vi không được âm.
#
# Ý tưởng:
# - Nhập các dữ liệu hình học cần kiểm tra từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - So sánh hai giá trị đã nhập để đưa ra kết luận.
# - Dùng câu lệnh if/elif/else để chọn kết quả đúng.
# - Thực hiện yêu cầu: so sánh chu vi.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chu_vi_1 = float(input("Nhập chu vi thứ nhất: "))
chu_vi_2 = float(input("Nhập chu vi thứ hai: "))

if chu_vi_1 < 0 or chu_vi_2 < 0:
    print("Chu vi không được âm")
elif chu_vi_1 > chu_vi_2:
    print("Chu vi thứ nhất lớn hơn")
elif chu_vi_1 < chu_vi_2:
    print("Chu vi thứ hai lớn hơn")
else:
    print("Hai chu vi bằng nhau")
