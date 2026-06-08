# Chương trình kiểm tra Unicode
#
# Yêu cầu:
# - Viết chương trình kiểm tra Unicode.
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

chuoi = input("Nhập chuỗi: ")
ky_tu_unicode = [ky_tu for ky_tu in chuoi if ord(ky_tu) > 127]
if not ky_tu_unicode:
    print("Chuỗi chỉ chứa ký tự ASCII")
else:
    print("Chuỗi có ký tự Unicode ngoài ASCII")
    print("Các ký tự Unicode:")
    for ky_tu in ky_tu_unicode:
        print(ky_tu, "->", "U+" + format(ord(ky_tu), "04X"))
