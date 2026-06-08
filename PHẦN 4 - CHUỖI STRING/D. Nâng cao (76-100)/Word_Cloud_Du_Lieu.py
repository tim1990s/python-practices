# Chương trình tạo dữ liệu word cloud
#
# Yêu cầu:
# - Viết chương trình tạo dữ liệu word cloud.
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
van_ban = input("Nhập văn bản: ").lower()
cac_tu = re.findall(r"[^\W\d_]+", van_ban, flags=re.UNICODE)
tan_suat = Counter(cac_tu)
if not tan_suat:
    print("Không có dữ liệu")
else:
    print("Dữ liệu word cloud:")
    for tu, so_lan in tan_suat.most_common():
        print(tu, "|", "#" * so_lan, "|", so_lan)
