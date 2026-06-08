# Chương trình tính mode
#
# Yêu cầu:
# - Viết chương trình tìm giá trị xuất hiện nhiều nhất trong list số.
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
# - Đọc list số.
# - Đếm tần suất từng giá trị.
# - Lấy các giá trị có tần suất cao nhất.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [float(phan_tu.strip()) for phan_tu in du_lieu.split(",") if phan_tu.strip()]


def dinh_dang_so(gia_tri):
    if isinstance(gia_tri, float) and gia_tri.is_integer():
        return int(gia_tri)
    return round(gia_tri, 4)


def dinh_dang_list(danh_sach):
    return [dinh_dang_so(gia_tri) for gia_tri in danh_sach]

from collections import Counter

danh_sach = doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: ")
if not danh_sach:
    print("Không thể tính mode của list rỗng")
else:
    tan_suat = Counter(danh_sach)
    so_lan_lon_nhat = max(tan_suat.values())
    mode = [gia_tri for gia_tri, so_lan in tan_suat.items() if so_lan == so_lan_lon_nhat]
    print("Mode:", dinh_dang_list(mode))
    print("Số lần xuất hiện:", so_lan_lon_nhat)
