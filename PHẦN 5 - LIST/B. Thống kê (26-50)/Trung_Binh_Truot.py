# Chương trình tính trung bình trượt
#
# Yêu cầu:
# - Viết chương trình tính moving average với cửa sổ k trên list số.
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
# - Đọc list số và kích thước cửa sổ k.
# - Duyệt từng đoạn liên tiếp có độ dài k.
# - Tính trung bình mỗi đoạn và đưa vào list kết quả.

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

danh_sach = doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: ")
k = int(input("Nhập kích thước cửa sổ k: "))

if k <= 0:
    print("k phải lớn hơn 0")
elif k > len(danh_sach):
    print("k không được lớn hơn số phần tử của list")
else:
    ket_qua = []
    for i in range(len(danh_sach) - k + 1):
        cua_so = danh_sach[i:i + k]
        ket_qua.append(sum(cua_so) / k)
    print("Trung bình trượt:", dinh_dang_list(ket_qua))
