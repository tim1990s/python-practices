# Chương trình so sánh hai chuỗi
#
# Yêu cầu:
# - Viết chương trình so sánh hai chuỗi.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Dùng các thao tác chuỗi cơ bản như độ dài, cắt chuỗi, đổi hoa thường, tìm kiếm hoặc thay thế.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi đầu vào từ bàn phím.
# - Áp dụng phương thức chuỗi hoặc phép cắt chuỗi phù hợp.
# - In kết quả sau khi xử lý.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
if chuoi_1 == chuoi_2:
    print("Hai chuỗi bằng nhau")
elif chuoi_1 > chuoi_2:
    print("Chuỗi thứ nhất lớn hơn theo thứ tự từ điển")
else:
    print("Chuỗi thứ hai lớn hơn theo thứ tự từ điển")
