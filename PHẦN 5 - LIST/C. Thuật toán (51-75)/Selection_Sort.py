# Chương trình Selection Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng thuật toán Selection Sort.
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
# - Tìm phần tử nhỏ nhất trong đoạn chưa sắp xếp.
# - Đưa phần tử nhỏ nhất về đầu đoạn.

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
for i in range(len(danh_sach) - 1):
    vi_tri_min = i
    for j in range(i + 1, len(danh_sach)):
        if danh_sach[j] < danh_sach[vi_tri_min]:
            vi_tri_min = j
    danh_sach[i], danh_sach[vi_tri_min] = danh_sach[vi_tri_min], danh_sach[i]
print("List sau khi Selection Sort:", danh_sach)
