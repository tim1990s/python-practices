# Chương trình hàm viết hoa chữ đầu
#
# Yêu cầu:
# - Viết hàm viết hoa chữ cái đầu mỗi từ.
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
# - Tách chuỗi thành các từ.
# - Dùng capitalize() cho từng từ.
# - Ghép các từ lại bằng khoảng trắng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def viet_hoa_chu_dau(chuoi):
    return " ".join(tu.capitalize() for tu in chuoi.split())


chuoi = input("Nhập chuỗi: ")
print("Kết quả:", viet_hoa_chu_dau(chuoi))
