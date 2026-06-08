# Chương trình quản lý lịch hẹn bằng list
#
# Yêu cầu:
# - Viết chương trình lưu lịch hẹn và lọc lịch theo ngày.
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
# - Đọc lịch hẹn dạng ngày, giờ, nội dung.
# - Lưu lịch hẹn vào list.
# - Lọc lịch theo ngày.

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

records = doc_ban_ghi("Nhập lịch hẹn dạng ngày,giờ,nội_dung; ...: ")
ngay_can_xem = input("Nhập ngày cần xem: ").strip()
items = []
for dong in records:
    ngay, gio, noi_dung = tach_truong(dong)
    items.append({"ngay": ngay, "gio": gio, "noi_dung": noi_dung})
print("Lịch hẹn trong ngày:", [x for x in items if x["ngay"] == ngay_can_xem])
