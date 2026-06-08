# Chương trình tạo concordance
#
# Yêu cầu:
# - Viết chương trình tạo concordance.
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
from collections import defaultdict
van_ban = input("Nhập văn bản: ")
cac_tu = re.findall(r"[^\W\d_]+", van_ban.lower(), flags=re.UNICODE)
concordance = defaultdict(list)
for vi_tri, tu in enumerate(cac_tu, start=1):
    concordance[tu].append(vi_tri)
if not concordance:
    print("Không có từ nào")
else:
    print("Concordance:")
    for tu in sorted(concordance):
        print(tu + ":", concordance[tu])
