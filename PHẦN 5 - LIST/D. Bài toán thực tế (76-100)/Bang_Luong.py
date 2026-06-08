# Chương trình lập bảng lương bằng list
#
# Yêu cầu:
# - Viết chương trình tính lương thực nhận cho danh sách nhân viên.
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
# - Đọc nhân viên dạng tên, lương cơ bản, phụ cấp, khấu trừ.
# - Lưu từng dòng lương vào list.
# - Tính thực nhận.

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

records = doc_ban_ghi("Nhập nhân viên dạng tên,lương_cơ_bản,phụ_cấp,khấu_trừ; ...: ")
items = []
for dong in records:
    ten, luong, phu_cap, khau_tru = tach_truong(dong)
    items.append({"ten": ten, "thuc_nhan": float(luong) + float(phu_cap) - float(khau_tru)})
print("Bảng lương:", items)
print("Tổng chi lương:", dinh_dang_so(sum(x["thuc_nhan"] for x in items)))
