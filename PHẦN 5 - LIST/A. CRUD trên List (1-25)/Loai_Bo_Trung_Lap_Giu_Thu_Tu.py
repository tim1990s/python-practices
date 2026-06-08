# Chương trình loại bỏ phần tử trùng lặp và giữ thứ tự
#
# Yêu cầu:
# - Viết chương trình loại bỏ phần tử trùng lặp nhưng vẫn giữ thứ tự xuất hiện ban đầu.
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
# - Duyệt từng phần tử.
# - Chỉ thêm phần tử chưa từng xuất hiện vào list kết quả.

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
ket_qua = []

for phan_tu in danh_sach:
    if phan_tu not in ket_qua:
        ket_qua.append(phan_tu)

print("List sau khi loại trùng:", ket_qua)
