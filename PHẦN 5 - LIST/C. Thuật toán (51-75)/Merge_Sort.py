# Chương trình Merge Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng thuật toán Merge Sort.
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
# - Chia list thành hai nửa.
# - Sắp xếp từng nửa bằng đệ quy.
# - Trộn hai nửa đã sắp xếp.

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

def merge_sort(a):
    if len(a) <= 1:
        return a
    giua = len(a) // 2
    trai = merge_sort(a[:giua])
    phai = merge_sort(a[giua:])
    ket_qua = []
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            ket_qua.append(trai[i])
            i += 1
        else:
            ket_qua.append(phai[j])
            j += 1
    return ket_qua + trai[i:] + phai[j:]


danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
print("List sau khi Merge Sort:", merge_sort(danh_sach))
