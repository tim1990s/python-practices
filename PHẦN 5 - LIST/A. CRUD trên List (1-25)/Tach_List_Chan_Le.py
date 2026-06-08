# Chương trình tách list số chẵn và số lẻ
#
# Yêu cầu:
# - Viết chương trình tách list số nguyên thành hai list chẵn và lẻ.
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
# - Đọc list số nguyên.
# - Duyệt từng số trong list.
# - Đưa số vào list chẵn hoặc list lẻ theo phần dư khi chia cho 2.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so_nguyen(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [int(phan_tu.strip()) for phan_tu in du_lieu.split(",") if phan_tu.strip()]

danh_sach = doc_list_so_nguyen("Nhập list số nguyên, các số cách nhau bởi dấu phẩy: ")
so_chan = [so for so in danh_sach if so % 2 == 0]
so_le = [so for so in danh_sach if so % 2 != 0]
print("List số chẵn:", so_chan)
print("List số lẻ:", so_le)
