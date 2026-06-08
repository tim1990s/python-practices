# Chương trình hàm đếm từ
#
# Yêu cầu:
# - Viết hàm đếm số từ trong chuỗi.
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
# - Tách chuỗi bằng split().
# - Loại bỏ khoảng trắng thừa.
# - Trả về số phần tử sau khi tách.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dem_tu(chuoi):
    return len(chuoi.split())


chuoi = input("Nhập chuỗi: ")
print("Số từ:", dem_tu(chuoi))
