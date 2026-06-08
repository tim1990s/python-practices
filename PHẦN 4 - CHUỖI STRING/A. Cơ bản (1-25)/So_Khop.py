# Chương trình so khớp chuỗi
#
# Yêu cầu:
# - Viết chương trình so khớp chuỗi.
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
mau = input("Nhập mẫu cần so khớp chính xác: ")
if chuoi == mau:
    print("So khớp chính xác")
elif chuoi.lower() == mau.lower():
    print("So khớp nếu bỏ qua hoa thường")
else:
    print("Không so khớp")
