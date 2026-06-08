# Chương trình hàm tìm kiếm từ khóa
#
# Yêu cầu:
# - Viết hàm kiểm tra từ khóa có nằm trong chuỗi hay không.
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
# - Chuẩn hóa chuỗi và từ khóa về chữ thường.
# - Dùng toán tử in để tìm.
# - Trả về True hoặc False.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tim_tu_khoa(chuoi, tu_khoa):
    return tu_khoa.lower() in chuoi.lower()


chuoi = input("Nhập chuỗi: ")
tu_khoa = input("Nhập từ khóa: ")
print("Có tìm thấy:", tim_tu_khoa(chuoi, tu_khoa))
