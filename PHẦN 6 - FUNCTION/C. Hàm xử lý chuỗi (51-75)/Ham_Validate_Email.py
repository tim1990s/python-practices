# Chương trình hàm validate email
#
# Yêu cầu:
# - Viết hàm kiểm tra email hợp lệ bằng regex.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi email.
# - Dùng regex kiểm tra cấu trúc cơ bản.
# - Trả về True nếu khớp mẫu.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re


def validate_email(email):
    mau = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.fullmatch(mau, email) is not None


email = input("Nhập email: ")
print("Email hợp lệ:", validate_email(email))
