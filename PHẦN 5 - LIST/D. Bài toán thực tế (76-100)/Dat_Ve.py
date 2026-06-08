# Chương trình quản lý đặt vé bằng list
#
# Yêu cầu:
# - Viết chương trình lưu vé và đếm số vé theo loại.
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
# - Đọc vé dạng tên khách, loại vé.
# - Lưu vé vào list.
# - Đếm số vé từng loại.

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

from collections import Counter

records = doc_ban_ghi("Nhập vé dạng tên_khách,loại_vé; ...: ")
items = []
for dong in records:
    ten, loai = tach_truong(dong)
    items.append({"ten": ten, "loai": loai})
print("Số vé theo loại:", dict(Counter(x["loai"] for x in items)))
