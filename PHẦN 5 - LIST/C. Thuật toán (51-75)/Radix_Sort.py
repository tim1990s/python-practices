# Chương trình Radix Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list số nguyên không âm bằng Radix Sort.
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
# - Đọc list số nguyên không âm.
# - Sắp xếp theo từng chữ số.
# - Lặp từ hàng đơn vị đến chữ số cao nhất.

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

def counting_theo_chu_so(a, exp):
    ket_qua = [0] * len(a)
    dem = [0] * 10
    for x in a:
        dem[(x // exp) % 10] += 1
    for i in range(1, 10):
        dem[i] += dem[i - 1]
    for i in range(len(a) - 1, -1, -1):
        chu_so = (a[i] // exp) % 10
        ket_qua[dem[chu_so] - 1] = a[i]
        dem[chu_so] -= 1
    return ket_qua


danh_sach = doc_list_so_nguyen("Nhập list số nguyên không âm: ")
if any(x < 0 for x in danh_sach):
    print("Radix Sort chỉ nhận số nguyên không âm")
else:
    exp = 1
    lon_nhat = max(danh_sach) if danh_sach else 0
    while lon_nhat // exp > 0:
        danh_sach = counting_theo_chu_so(danh_sach, exp)
        exp *= 10
    print("List sau khi Radix Sort:", danh_sach)
