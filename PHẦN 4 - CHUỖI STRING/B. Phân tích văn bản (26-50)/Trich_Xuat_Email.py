# Chương trình trích xuất email
#
# Yêu cầu:
# - Viết chương trình trích xuất email.
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
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", van_ban)
if not emails:
    print("Không tìm thấy email")
else:
    print("Email tìm thấy:")
    for email in emails:
        print(email)
