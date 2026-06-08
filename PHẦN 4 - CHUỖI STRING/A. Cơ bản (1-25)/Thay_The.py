# Chương trình thay thế trong chuỗi
#
# Yêu cầu:
# - Viết chương trình thay thế trong chuỗi.
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

chuoi = input("Nhập chuỗi: ")
cu = input("Nhập chuỗi cần thay: ")
moi = input("Nhập chuỗi thay thế: ")
print("Kết quả:", chuoi.replace(cu, moi))
