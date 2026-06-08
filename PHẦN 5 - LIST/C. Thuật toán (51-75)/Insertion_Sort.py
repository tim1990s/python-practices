# Chương trình Insertion Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng thuật toán Insertion Sort.
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
# - Đọc list số nguyên.
# - Duyệt từng phần tử từ trái sang phải.
# - Chèn phần tử hiện tại vào đúng vị trí trong đoạn đã sắp xếp.

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
for i in range(1, len(danh_sach)):
    gia_tri = danh_sach[i]
    j = i - 1
    while j >= 0 and danh_sach[j] > gia_tri:
        danh_sach[j + 1] = danh_sach[j]
        j -= 1
    danh_sach[j + 1] = gia_tri
print("List sau khi Insertion Sort:", danh_sach)
