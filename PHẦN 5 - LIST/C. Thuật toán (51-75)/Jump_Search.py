# Chương trình Jump Search
#
# Yêu cầu:
# - Viết chương trình tìm kiếm nhảy trong list đã sắp xếp.
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
# - Đọc list đã sắp xếp.
# - Nhảy theo từng block.
# - Tìm tuyến tính trong block phù hợp.

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

import math

danh_sach = doc_list_so_nguyen("Nhập list đã sắp xếp tăng dần: ")
x = int(input("Nhập giá trị cần tìm: "))
n = len(danh_sach)
buoc = int(math.sqrt(n)) or 1
bat_dau = 0
while bat_dau < n and danh_sach[min(buoc, n) - 1] < x:
    bat_dau = buoc
    buoc += int(math.sqrt(n)) or 1
vi_tri = -1
for i in range(bat_dau, min(buoc, n)):
    if danh_sach[i] == x:
        vi_tri = i
        break
print("Không tìm thấy" if vi_tri == -1 else "Tìm thấy tại vị trí: " + str(vi_tri))
