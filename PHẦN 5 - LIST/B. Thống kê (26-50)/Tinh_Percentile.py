# Chương trình tính percentile
#
# Yêu cầu:
# - Viết chương trình tính phân vị p của list số.
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
# - Đọc list số và phần trăm p.
# - Sắp xếp list tăng dần.
# - Nội suy vị trí phân vị nếu cần.

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

import math

danh_sach = sorted(doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: "))
p = float(input("Nhập percentile p (0-100): "))

if not danh_sach:
    print("Không thể tính percentile của list rỗng")
elif p < 0 or p > 100:
    print("p phải nằm trong khoảng 0 đến 100")
else:
    vi_tri = (len(danh_sach) - 1) * p / 100
    duoi = math.floor(vi_tri)
    tren = math.ceil(vi_tri)
    if duoi == tren:
        ket_qua = danh_sach[int(vi_tri)]
    else:
        ty_le = vi_tri - duoi
        ket_qua = danh_sach[duoi] * (1 - ty_le) + danh_sach[tren] * ty_le
    print(f"Percentile {dinh_dang_so(p)}:", dinh_dang_so(ket_qua))
