# Chương trình quản lý danh bạ bằng list
#
# Yêu cầu:
# - Viết chương trình lưu danh bạ và tìm liên hệ theo tên.
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
# - Đọc liên hệ dạng tên, số điện thoại.
# - Lưu liên hệ vào list.
# - Lọc liên hệ theo từ khóa tên.

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

records = doc_ban_ghi("Nhập liên hệ dạng tên,số_điện_thoại; ...: ")
tu_khoa = input("Nhập tên cần tìm: ").strip().lower()
items = []
for dong in records:
    ten, sdt = tach_truong(dong)
    items.append({"ten": ten, "so_dien_thoai": sdt})
print("Kết quả tìm kiếm:", [x for x in items if tu_khoa in x["ten"].lower()])
