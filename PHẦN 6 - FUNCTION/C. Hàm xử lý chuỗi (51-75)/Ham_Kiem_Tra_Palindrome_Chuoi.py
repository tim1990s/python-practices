# Chương trình hàm kiểm tra chuỗi palindrome
#
# Yêu cầu:
# - Viết hàm kiểm tra chuỗi có đối xứng hay không.
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
# - Chuẩn hóa chuỗi về chữ thường.
# - Bỏ khoảng trắng hai đầu.
# - So sánh chuỗi với chuỗi đảo ngược.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_palindrome(chuoi):
    chuan_hoa = "".join(chuoi.lower().split())
    return chuan_hoa == chuan_hoa[::-1]


chuoi = input("Nhập chuỗi: ")
print("Là palindrome:", la_palindrome(chuoi))
