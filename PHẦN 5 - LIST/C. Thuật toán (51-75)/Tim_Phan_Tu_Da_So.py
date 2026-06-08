# Chương trình tìm phần tử đa số
#
# Yêu cầu:
# - Viết chương trình tìm phần tử xuất hiện nhiều hơn n/2 lần nếu có.
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
# - Tìm ứng viên bằng Boyer-Moore.
# - Kiểm tra lại tần suất của ứng viên.

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
ung_vien = None
dem = 0
for x in danh_sach:
    if dem == 0:
        ung_vien = x
        dem = 1
    elif x == ung_vien:
        dem += 1
    else:
        dem -= 1
if ung_vien is not None and danh_sach.count(ung_vien) > len(danh_sach) // 2:
    print("Phần tử đa số:", ung_vien)
else:
    print("Không có phần tử đa số")
