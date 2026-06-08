# Chương trình trích xuất tiền tệ
#
# Yêu cầu:
# - Viết chương trình trích xuất tiền tệ.
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
mau = r"(?:[$€£₫]\s?\d[\d.,]*|\d[\d.,]*\s?(?:VND|VNĐ|USD|EUR|đ|₫|dollars?))"
tien_te = re.findall(mau, van_ban, flags=re.IGNORECASE)
if not tien_te:
    print("Không tìm thấy tiền tệ")
else:
    print("Tiền tệ tìm thấy:")
    for tien in tien_te:
        print(tien)
