# Chương trình quản lý chi tiêu cá nhân bằng list
#
# Yêu cầu:
# - Viết chương trình lưu khoản chi và thống kê theo danh mục.
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
# - Đọc khoản chi dạng danh mục, số tiền.
# - Lưu khoản chi vào list.
# - Cộng tiền theo danh mục.

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

records = doc_ban_ghi("Nhập khoản chi dạng danh_mục,số_tiền; ...: ")
thong_ke = {}
for dong in records:
    danh_muc, so_tien = tach_truong(dong)
    thong_ke[danh_muc] = thong_ke.get(danh_muc, 0) + float(so_tien)
print("Tổng chi theo danh mục:", {k: dinh_dang_so(v) for k, v in thong_ke.items()})
