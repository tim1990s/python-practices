# Chương trình quản lý lớp học bằng list
#
# Yêu cầu:
# - Viết chương trình lưu học sinh và thống kê số học sinh mỗi lớp.
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
# - Đọc học sinh dạng tên, lớp.
# - Lưu học sinh vào list.
# - Đếm số học sinh theo lớp.

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

records = doc_ban_ghi("Nhập học sinh dạng tên,lớp; ...: ")
items = []
for dong in records:
    ten, lop = tach_truong(dong)
    items.append({"ten": ten, "lop": lop})
print("Số học sinh theo lớp:", dict(Counter(x["lop"] for x in items)))
