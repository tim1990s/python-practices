# Chương trình hàm thống kê số
#
# Yêu cầu:
# - Viết hàm thống kê tổng, trung bình, max và min của list số.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý số nguyên, số thực, chữ số, ước số, bội số, dãy Fibonacci và các bài toán số học cơ bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số.
# - Tách thống kê vào một hàm.
# - Trả về dict chứa các chỉ số cơ bản.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def thong_ke_so(danh_sach):
    if not danh_sach:
        return None
    return {
        "tong": sum(danh_sach),
        "trung_binh": sum(danh_sach) / len(danh_sach),
        "max": max(danh_sach),
        "min": min(danh_sach),
        "so_luong": len(danh_sach),
    }


du_lieu = input("Nhập các số, cách nhau bởi dấu phẩy: ")
danh_sach = [float(x.strip()) for x in du_lieu.split(",") if x.strip()]
print("Thống kê:", thong_ke_so(danh_sach))
