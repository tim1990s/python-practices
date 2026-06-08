# Chương trình ghép hai list
#
# Yêu cầu:
# - Viết chương trình ghép hai list thành một list mới.
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
# - Đọc list thứ nhất.
# - Đọc list thứ hai.
# - Dùng toán tử + để ghép list.

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

danh_sach_1 = doc_list_chuoi("Nhập list thứ nhất: ")
danh_sach_2 = doc_list_chuoi("Nhập list thứ hai: ")
ket_qua = danh_sach_1 + danh_sach_2
print("List sau khi ghép:", ket_qua)
