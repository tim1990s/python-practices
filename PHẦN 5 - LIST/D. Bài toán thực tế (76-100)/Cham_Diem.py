# Chương trình chấm điểm bằng list
#
# Yêu cầu:
# - Viết chương trình lưu điểm và xếp loại từng học sinh.
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
# - Đọc học sinh dạng tên, điểm.
# - Lưu điểm vào list.
# - Xếp loại theo khoảng điểm.

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

records = doc_ban_ghi("Nhập học sinh dạng tên,điểm; ...: ")
ket_qua = []
for dong in records:
    ten, diem = tach_truong(dong)
    diem = float(diem)
    xep_loai = "Giỏi" if diem >= 8 else "Khá" if diem >= 6.5 else "Trung bình" if diem >= 5 else "Yếu"
    ket_qua.append({"ten": ten, "diem": diem, "xep_loai": xep_loai})
print("Kết quả chấm điểm:", ket_qua)
