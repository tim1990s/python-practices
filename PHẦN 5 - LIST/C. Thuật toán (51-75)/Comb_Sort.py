# Chương trình Comb Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng Comb Sort.
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
# - So sánh các phần tử cách nhau gap.
# - Giảm gap dần.
# - Kết thúc khi gap bằng 1 và không còn đổi chỗ.

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
gap = len(danh_sach)
da_doi = True
while gap > 1 or da_doi:
    gap = max(1, int(gap / 1.3))
    da_doi = False
    for i in range(len(danh_sach) - gap):
        if danh_sach[i] > danh_sach[i + gap]:
            danh_sach[i], danh_sach[i + gap] = danh_sach[i + gap], danh_sach[i]
            da_doi = True
print("List sau khi Comb Sort:", danh_sach)
