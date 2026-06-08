# Chương trình thống kê tần suất từ
#
# Yêu cầu:
# - Viết chương trình thống kê tần suất từ.
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
tan_suat = Counter(cac_tu)
if not tan_suat:
    print("Không có từ nào")
else:
    print("Tần suất từ:")
    for tu, so_lan in tan_suat.items():
        print(tu + ":", so_lan)
