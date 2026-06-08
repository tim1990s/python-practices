# Chương trình tách đoạn
#
# Yêu cầu:
# - Viết chương trình tách đoạn.
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

van_ban = input("Nhập văn bản, dùng dấu | để ngăn cách các đoạn: ")
cac_doan = [doan.strip() for doan in van_ban.split("|") if doan.strip()]
if not cac_doan:
    print("Không có đoạn nào")
else:
    print("Các đoạn:")
    for i, doan in enumerate(cac_doan, start=1):
        print("Đoạn", str(i) + ":", doan)
