# Chương trình phân hoạch số chẵn và số lẻ
#
# Yêu cầu:
# - Viết chương trình đưa số chẵn về trước và số lẻ về sau.
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
# - Tách số chẵn và số lẻ.
# - Ghép list chẵn trước list lẻ.

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
so_chan = [x for x in danh_sach if x % 2 == 0]
so_le = [x for x in danh_sach if x % 2 != 0]
print("List sau khi phân hoạch:", so_chan + so_le)
