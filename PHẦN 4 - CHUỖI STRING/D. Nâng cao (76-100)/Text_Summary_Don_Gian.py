# Chương trình tóm tắt văn bản đơn giản
#
# Yêu cầu:
# - Viết chương trình tóm tắt văn bản đơn giản.
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
van_ban = input("Nhập văn bản: ")
so_cau = int(input("Nhập số câu tóm tắt: "))
cac_cau = [cau.strip() for cau in re.findall(r"[^.!?]+[.!?]*", van_ban) if cau.strip()]
cac_tu = re.findall(r"[^\W\d_]+", van_ban.lower(), flags=re.UNICODE)
tan_suat = Counter(tu for tu in cac_tu if tu not in STOPWORDS)
diem_cau = []
for vi_tri, cau in enumerate(cac_cau):
    diem = sum(tan_suat.get(tu, 0) for tu in re.findall(r"[^\W\d_]+", cau.lower(), flags=re.UNICODE))
    diem_cau.append((diem, vi_tri, cau))
chon = sorted(diem_cau, reverse=True)[:so_cau]
chon.sort(key=lambda item: item[1])
print("Tóm tắt:")
for _, _, cau in chon:
    print(cau)
