# Chương trình Quick Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng thuật toán Quick Sort.
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
# - Chọn một pivot.
# - Tách list thành nhóm nhỏ hơn, bằng và lớn hơn pivot.
# - Sắp xếp đệ quy rồi ghép kết quả.

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

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    nho = [x for x in a if x < pivot]
    bang = [x for x in a if x == pivot]
    lon = [x for x in a if x > pivot]
    return quick_sort(nho) + bang + quick_sort(lon)


danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
print("List sau khi Quick Sort:", quick_sort(danh_sach))
