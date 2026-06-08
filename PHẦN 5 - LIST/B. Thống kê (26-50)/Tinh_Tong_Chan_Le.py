# Chương trình tính tổng số chẵn và số lẻ
#
# Yêu cầu:
# - Viết chương trình tính riêng tổng các số chẵn và tổng các số lẻ trong list số nguyên.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện thống kê dữ liệu số trong list như max, min, trung bình, trung vị, mode, phương sai, độ lệch chuẩn, phân vị và tần suất.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số nguyên.
# - Tách số chẵn và số lẻ bằng điều kiện chia dư.
# - Tính tổng từng nhóm.

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
tong_chan = sum(so for so in danh_sach if so % 2 == 0)
tong_le = sum(so for so in danh_sach if so % 2 != 0)
print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)
