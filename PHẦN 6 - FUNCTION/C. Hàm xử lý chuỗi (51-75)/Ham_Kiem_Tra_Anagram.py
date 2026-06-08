# Chương trình hàm kiểm tra anagram
#
# Yêu cầu:
# - Viết hàm kiểm tra hai chuỗi có phải anagram không.
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
# - Chuẩn hóa hai chuỗi về chữ thường.
# - Bỏ khoảng trắng.
# - So sánh hai chuỗi sau khi sắp xếp ký tự.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_anagram(a, b):
    a = "".join(a.lower().split())
    b = "".join(b.lower().split())
    return sorted(a) == sorted(b)


a = input("Nhập chuỗi thứ nhất: ")
b = input("Nhập chuỗi thứ hai: ")
print("Là anagram:", la_anagram(a, b))
