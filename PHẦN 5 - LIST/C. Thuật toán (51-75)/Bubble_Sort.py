# Chương trình Bubble Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng thuật toán Bubble Sort.
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
# - So sánh các cặp phần tử liền kề.
# - Đổi chỗ nếu hai phần tử sai thứ tự.

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
n = len(danh_sach)
for i in range(n - 1):
    da_doi = False
    for j in range(n - 1 - i):
        if danh_sach[j] > danh_sach[j + 1]:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
            da_doi = True
    if not da_doi:
        break
print("List sau khi Bubble Sort:", danh_sach)
