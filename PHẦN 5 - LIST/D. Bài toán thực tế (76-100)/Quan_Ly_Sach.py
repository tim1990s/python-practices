# Chương trình quản lý sách bằng list
#
# Yêu cầu:
# - Viết chương trình lưu danh sách sách và tìm sách theo tác giả.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện cách dùng list để lưu nhiều bản ghi, duyệt dữ liệu, lọc, tìm kiếm, thống kê và cập nhật thông tin trong bài toán thực tế.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc sách dạng tên sách, tác giả, năm.
# - Lưu sách vào list.
# - Lọc sách theo tác giả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_ban_ghi(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [dong.strip() for dong in du_lieu.split(";") if dong.strip()]


def tach_truong(dong):
    return [x.strip() for x in dong.split(",")]


def dinh_dang_so(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return round(x, 2)

records = doc_ban_ghi("Nhập sách dạng tên_sách,tác_giả,năm; ...: ")
tu_khoa = input("Nhập tác giả cần tìm: ").strip().lower()
items = []
for dong in records:
    ten, tac_gia, nam = tach_truong(dong)
    items.append({"ten": ten, "tac_gia": tac_gia, "nam": int(nam)})
print("Sách tìm được:", [x for x in items if tu_khoa in x["tac_gia"].lower()])
