# Chương trình thêm phần tử tại vị trí bất kỳ
#
# Yêu cầu:
# - Viết chương trình thêm một phần tử vào list tại vị trí được nhập.
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
# - Đọc vị trí và phần tử cần chèn.
# - Chuẩn hóa vị trí rồi dùng insert().

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
vi_tri = int(input("Nhập vị trí cần chèn: "))
phan_tu = input("Nhập phần tử cần chèn: ")

if vi_tri < 0:
    vi_tri = 0
elif vi_tri > len(danh_sach):
    vi_tri = len(danh_sach)

danh_sach.insert(vi_tri, phan_tu)
print("List sau khi chèn:", danh_sach)
