# Chương trình hàm thay thế chuỗi
#
# Yêu cầu:
# - Viết hàm thay thế một đoạn chuỗi bằng đoạn khác.
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
# - Nhận chuỗi gốc.
# - Nhận chuỗi cũ và chuỗi mới.
# - Dùng replace() để thay thế.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def thay_the(chuoi, cu, moi):
    return chuoi.replace(cu, moi)


chuoi = input("Nhập chuỗi: ")
cu = input("Nhập chuỗi cần thay: ")
moi = input("Nhập chuỗi mới: ")
print("Kết quả:", thay_the(chuoi, cu, moi))
