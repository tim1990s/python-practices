# Chương trình sửa phần tử theo giá trị
#
# Yêu cầu:
# - Viết chương trình thay thế tất cả phần tử có giá trị cũ bằng giá trị mới.
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
# - Đọc giá trị cũ và giá trị mới.
# - Duyệt list để thay thế các phần tử phù hợp.

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
gia_tri_cu = input("Nhập giá trị cần thay: ")
gia_tri_moi = input("Nhập giá trị mới: ")
so_lan_thay = 0

for vi_tri, gia_tri in enumerate(danh_sach):
    if gia_tri == gia_tri_cu:
        danh_sach[vi_tri] = gia_tri_moi
        so_lan_thay += 1

print("Số lần thay thế:", so_lan_thay)
print("List sau khi thay thế:", danh_sach)
