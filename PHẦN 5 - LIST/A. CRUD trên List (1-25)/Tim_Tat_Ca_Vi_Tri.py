# Chương trình tìm tất cả vị trí của phần tử
#
# Yêu cầu:
# - Viết chương trình tìm tất cả vị trí xuất hiện của một giá trị trong list.
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
# - Đọc giá trị cần tìm.
# - Duyệt list bằng enumerate() để lấy các vị trí phù hợp.

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

danh_sach = doc_list_chuoi("Nhập list, các phần tử cách nhau bởi dấu phẩy: ")
gia_tri = input("Nhập giá trị cần tìm vị trí: ")
vi_tri_tim_duoc = [vi_tri for vi_tri, phan_tu in enumerate(danh_sach) if phan_tu == gia_tri]

if vi_tri_tim_duoc:
    print("Các vị trí tìm được:", vi_tri_tim_duoc)
else:
    print("Không tìm thấy giá trị trong list")
