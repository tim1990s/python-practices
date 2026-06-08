# Chương trình trích xuất số điện thoại
#
# Yêu cầu:
# - Viết chương trình trích xuất số điện thoại.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Phân tích nội dung văn bản để đếm, tách, thống kê hoặc trích xuất thông tin cần thiết.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc văn bản đầu vào.
# - Tách văn bản thành ký tự, từ, câu hoặc mẫu dữ liệu phù hợp.
# - Thống kê hoặc trích xuất rồi in kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
van_ban = input("Nhập văn bản: ")
so_dien_thoai = re.findall(r"(?:\+84|0)(?:[\s.-]?\d){9,10}", van_ban)
if not so_dien_thoai:
    print("Không tìm thấy số điện thoại")
else:
    print("Số điện thoại tìm thấy:")
    for so in so_dien_thoai:
        print(so)
