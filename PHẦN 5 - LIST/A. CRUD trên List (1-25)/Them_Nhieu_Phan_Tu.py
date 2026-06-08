# Chương trình thêm nhiều phần tử vào list
#
# Yêu cầu:
# - Viết chương trình thêm nhiều phần tử mới vào cuối list.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện các thao tác CRUD và biến đổi cơ bản trên list như thêm, xóa, sửa, tìm kiếm, sắp xếp, cắt, ghép và tách list.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list ban đầu.
# - Đọc list phần tử mới.
# - Dùng extend() để nối các phần tử mới vào cuối list.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_chuoi(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [phan_tu.strip() for phan_tu in du_lieu.split(",")]

danh_sach = doc_list_chuoi("Nhập list ban đầu: ")
phan_tu_moi = doc_list_chuoi("Nhập các phần tử cần thêm: ")
danh_sach.extend(phan_tu_moi)
print("List sau khi thêm nhiều phần tử:", danh_sach)
