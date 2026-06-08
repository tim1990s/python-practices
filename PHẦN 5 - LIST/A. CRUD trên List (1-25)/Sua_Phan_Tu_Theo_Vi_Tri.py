# Chương trình sửa phần tử theo vị trí
#
# Yêu cầu:
# - Viết chương trình cập nhật phần tử tại vị trí được nhập.
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
# - Đọc vị trí và giá trị mới.
# - Nếu vị trí hợp lệ thì gán lại phần tử.

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
vi_tri = int(input("Nhập vị trí cần sửa: "))
gia_tri_moi = input("Nhập giá trị mới: ")

if -len(danh_sach) <= vi_tri < len(danh_sach):
    danh_sach[vi_tri] = gia_tri_moi
    print("List sau khi sửa:", danh_sach)
else:
    print("Vị trí không hợp lệ")
