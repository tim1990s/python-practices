# Chương trình xoay list sang phải k bước
#
# Yêu cầu:
# - Viết chương trình xoay list sang phải k vị trí.
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
# - Đọc list và k.
# - Chuẩn hóa k theo độ dài list.
# - Dùng slicing để ghép phần cuối lên đầu.

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
k = int(input("Nhập số bước xoay sang phải: "))
if not danh_sach:
    print("List sau khi xoay: []")
else:
    k %= len(danh_sach)
    ket_qua = danh_sach[-k:] + danh_sach[:-k] if k else danh_sach
    print("List sau khi xoay:", ket_qua)
