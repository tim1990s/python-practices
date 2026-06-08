# Chương trình Counting Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list số nguyên không âm bằng Counting Sort.
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
# - Đọc list số nguyên không âm.
# - Đếm số lần xuất hiện từng giá trị.
# - Dựng lại list theo thứ tự tăng dần.

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

danh_sach = doc_list_so_nguyen("Nhập list số nguyên không âm: ")
if any(x < 0 for x in danh_sach):
    print("Counting Sort chỉ nhận số nguyên không âm")
elif not danh_sach:
    print("List sau khi Counting Sort: []")
else:
    dem = [0] * (max(danh_sach) + 1)
    for x in danh_sach:
        dem[x] += 1
    ket_qua = []
    for gia_tri, so_lan in enumerate(dem):
        ket_qua.extend([gia_tri] * so_lan)
    print("List sau khi Counting Sort:", ket_qua)
