# Chương trình tách câu
#
# Yêu cầu:
# - Viết chương trình tách câu.
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

import re
van_ban = input("Nhập văn bản: ")
cac_cau = [cau.strip() for cau in re.findall(r"[^.!?]+[.!?]*", van_ban) if cau.strip()]
if not cac_cau:
    print("Không có câu nào")
else:
    print("Các câu:")
    for i, cau in enumerate(cac_cau, start=1):
        print(str(i) + ".", cau)
