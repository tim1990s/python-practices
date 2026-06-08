# Chương trình hàm tách từ
#
# Yêu cầu:
# - Viết hàm tách chuỗi thành list từ.
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
# - Đọc chuỗi đầu vào.
# - Dùng split() để tách từ.
# - Trả về list từ.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tach_tu(chuoi):
    return chuoi.split()


chuoi = input("Nhập chuỗi: ")
print("Các từ:", tach_tu(chuoi))
