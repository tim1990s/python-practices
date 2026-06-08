# Chương trình chuẩn hóa Unicode
#
# Yêu cầu:
# - Viết chương trình chuẩn hóa Unicode.
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

import unicodedata
chuoi = input("Nhập chuỗi: ")
dang = input("Nhập dạng chuẩn hóa (NFC/NFD/NFKC/NFKD), bỏ trống dùng NFC: ").upper()
if dang == "":
    dang = "NFC"
if dang not in {"NFC", "NFD", "NFKC", "NFKD"}:
    print("Dạng chuẩn hóa không hợp lệ")
else:
    print("Chuỗi sau chuẩn hóa:", unicodedata.normalize(dang, chuoi))
