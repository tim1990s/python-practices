# Chương trình tính trung bình số chẵn và số lẻ
#
# Yêu cầu:
# - Viết chương trình tính riêng trung bình số chẵn và trung bình số lẻ trong list số nguyên.
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
# - Tách thành list chẵn và list lẻ.
# - Tính trung bình từng list nếu list không rỗng.

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

if so_chan:
    print("Trung bình số chẵn:", sum(so_chan) / len(so_chan))
else:
    print("Không có số chẵn")

if so_le:
    print("Trung bình số lẻ:", sum(so_le) / len(so_le))
else:
    print("Không có số lẻ")
