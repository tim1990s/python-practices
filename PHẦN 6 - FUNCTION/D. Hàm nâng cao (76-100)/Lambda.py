# Chương trình Lambda
#
# Yêu cầu:
# - Viết ví dụ dùng lambda để biến đổi list.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện các kỹ thuật hàm nâng cao: đệ quy, decorator, closure, higher-order function, generator, iterator, callback, async và các pattern đơn giản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số.
# - Tạo lambda tính bình phương.
# - Dùng map để áp dụng lambda cho từng phần tử.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

danh_sach = [float(x.strip()) for x in input("Nhập list số: ").split(",") if x.strip()]
binh_phuong = lambda x: x ** 2
print("List bình phương:", list(map(binh_phuong, danh_sach)))
