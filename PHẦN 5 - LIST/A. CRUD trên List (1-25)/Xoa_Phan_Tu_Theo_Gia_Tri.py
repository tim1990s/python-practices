# Chương trình xóa phần tử theo giá trị
#
# Yêu cầu:
# - Viết chương trình xóa lần xuất hiện đầu tiên của một giá trị trong list.
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
# - Đọc giá trị cần xóa.
# - Nếu giá trị tồn tại thì dùng remove().

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
gia_tri = input("Nhập giá trị cần xóa: ")

if gia_tri in danh_sach:
    danh_sach.remove(gia_tri)
    print("List sau khi xóa:", danh_sach)
else:
    print("Không tìm thấy giá trị cần xóa")
    print("List hiện tại:", danh_sach)
