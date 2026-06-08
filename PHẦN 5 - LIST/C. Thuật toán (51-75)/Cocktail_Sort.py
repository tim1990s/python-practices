# Chương trình Cocktail Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng Cocktail Sort.
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
# - Quét từ trái sang phải.
# - Quét từ phải sang trái.
# - Lặp đến khi không còn đổi chỗ.

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
bat_dau, ket_thuc = 0, len(danh_sach) - 1
da_doi = True
while da_doi:
    da_doi = False
    for i in range(bat_dau, ket_thuc):
        if danh_sach[i] > danh_sach[i + 1]:
            danh_sach[i], danh_sach[i + 1] = danh_sach[i + 1], danh_sach[i]
            da_doi = True
    ket_thuc -= 1
    for i in range(ket_thuc, bat_dau, -1):
        if danh_sach[i - 1] > danh_sach[i]:
            danh_sach[i - 1], danh_sach[i] = danh_sach[i], danh_sach[i - 1]
            da_doi = True
    bat_dau += 1
print("List sau khi Cocktail Sort:", danh_sach)
