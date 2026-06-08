# Chương trình tìm cặp có tổng bằng k
#
# Yêu cầu:
# - Viết chương trình tìm hai phần tử trong list có tổng bằng k.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện các thuật toán phổ biến trên list như sắp xếp, tìm kiếm, chia tách, tổng tiền tố và xử lý dãy con.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số nguyên và k.
# - Lưu các số đã gặp bằng set.
# - Với mỗi số, kiểm tra k - số đã xuất hiện chưa.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so_nguyen(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [int(x.strip()) for x in du_lieu.split(",") if x.strip()]

danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
k = int(input("Nhập tổng k cần tìm: "))
da_gap = set()
cap = None
for x in danh_sach:
    if k - x in da_gap:
        cap = (k - x, x)
        break
    da_gap.add(x)
print("Không tìm thấy cặp phù hợp" if cap is None else "Cặp tìm được: " + str(cap))
