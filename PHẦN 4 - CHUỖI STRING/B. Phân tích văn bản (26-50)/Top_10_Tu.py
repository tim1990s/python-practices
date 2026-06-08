# Chương trình tìm top 10 từ xuất hiện nhiều nhất
#
# Yêu cầu:
# - Viết chương trình tìm top 10 từ xuất hiện nhiều nhất.
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
from collections import Counter
van_ban = input("Nhập văn bản: ")
cac_tu = re.findall(r"[^\W\d_]+", van_ban.lower(), flags=re.UNICODE)
top_10 = Counter(cac_tu).most_common(10)
if not top_10:
    print("Không có từ nào")
else:
    print("Top 10 từ:")
    for tu, so_lan in top_10:
        print(tu + ":", so_lan)
