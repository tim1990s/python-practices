# Chương trình loại bỏ stopwords
#
# Yêu cầu:
# - Viết chương trình loại bỏ stopwords.
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
STOPWORDS = {"và", "là", "của", "có", "cho", "một", "những", "các", "đã", "đang", "sẽ", "the", "a", "an", "and", "or", "is", "are", "to", "of", "in", "on", "for"}
van_ban = input("Nhập văn bản: ")
cac_tu = re.findall(r"[^\W\d_]+", van_ban, flags=re.UNICODE)
ket_qua = [tu for tu in cac_tu if tu.lower() not in STOPWORDS]
print("Văn bản sau khi loại bỏ stopwords:", " ".join(ket_qua))
