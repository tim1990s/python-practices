# Chương trình Shell Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng Shell Sort.
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
# - Chọn khoảng cách gap.
# - Insertion sort theo từng gap.
# - Giảm gap đến 1.

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
gap = len(danh_sach) // 2
while gap > 0:
    for i in range(gap, len(danh_sach)):
        tam = danh_sach[i]
        j = i
        while j >= gap and danh_sach[j - gap] > tam:
            danh_sach[j] = danh_sach[j - gap]
            j -= gap
        danh_sach[j] = tam
    gap //= 2
print("List sau khi Shell Sort:", danh_sach)
