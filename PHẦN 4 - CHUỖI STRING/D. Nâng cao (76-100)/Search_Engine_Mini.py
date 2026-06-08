# Chương trình search engine mini
#
# Yêu cầu:
# - Viết chương trình search engine mini.
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
van_ban = input("Nhập các tài liệu, cách nhau bởi dấu |: ")
query = input("Nhập từ khóa tìm kiếm: ").lower()
tai_lieu = [doc.strip() for doc in van_ban.split("|") if doc.strip()]
tu_query = set(re.findall(r"[^\W\d_]+", query, flags=re.UNICODE))
ket_qua = []
for vi_tri, doc in enumerate(tai_lieu, start=1):
    tu_doc = re.findall(r"[^\W\d_]+", doc.lower(), flags=re.UNICODE)
    diem = sum(1 for tu in tu_doc if tu in tu_query)
    if diem > 0:
        ket_qua.append((diem, vi_tri, doc))
ket_qua.sort(reverse=True)
if not ket_qua:
    print("Không tìm thấy tài liệu phù hợp")
else:
    print("Kết quả tìm kiếm:")
    for diem, vi_tri, doc in ket_qua:
        print("Tài liệu", vi_tri, "- điểm", str(diem) + ":", doc)
