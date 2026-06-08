# Chương trình hàm đảo chuỗi
#
# Yêu cầu:
# - Viết hàm đảo ngược một chuỗi.
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
# - Nhận chuỗi đầu vào.
# - Dùng slicing để đảo chuỗi.
# - Trả về chuỗi đã đảo.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dao_chuoi(chuoi):
    return chuoi[::-1]


chuoi = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược:", dao_chuoi(chuoi))
