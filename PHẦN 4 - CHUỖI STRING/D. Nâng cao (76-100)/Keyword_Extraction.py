# Chương trình trích xuất keyword đơn giản
#
# Yêu cầu:
# - Viết chương trình trích xuất keyword đơn giản.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Cài đặt thuật toán hoặc kỹ thuật xử lý chuỗi nâng cao để giải quyết bài toán.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc dữ liệu đầu vào theo yêu cầu.
# - Cài đặt thuật toán, cấu trúc dữ liệu hoặc hàm xử lý chuỗi cần thiết.
# - Trả về hoặc in kết quả cuối cùng rõ ràng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
from collections import Counter
STOPWORDS = {"và", "là", "của", "có", "cho", "một", "các", "the", "a", "an", "and", "or", "to", "of", "in"}
van_ban = input("Nhập văn bản: ").lower()
cac_tu = re.findall(r"[^\W\d_]+", van_ban, flags=re.UNICODE)
tu_khoa = [tu for tu in cac_tu if tu not in STOPWORDS and len(tu) > 1]
print("Keyword:")
for tu, so_lan in Counter(tu_khoa).most_common(10):
    print(tu + ":", so_lan)
