# Chương trình tìm dãy con liên tiếp có tổng lớn nhất
#
# Yêu cầu:
# - Viết chương trình tìm tổng dãy con liên tiếp lớn nhất bằng Kadane.
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
# - Cập nhật tổng tốt nhất kết thúc tại vị trí hiện tại.
# - Lưu tổng lớn nhất toàn cục.

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
if not danh_sach:
    print("List rỗng")
else:
    hien_tai = lon_nhat = danh_sach[0]
    for x in danh_sach[1:]:
        hien_tai = max(x, hien_tai + x)
        lon_nhat = max(lon_nhat, hien_tai)
    print("Tổng dãy con liên tiếp lớn nhất:", lon_nhat)
