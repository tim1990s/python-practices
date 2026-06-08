# Chương trình sentiment đơn giản
#
# Yêu cầu:
# - Viết chương trình sentiment đơn giản.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Cài đặt thuật toán hoặc kỹ thuật xử lý chuỗi nâng cao để giải quyết bài toán.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc dữ liệu đầu vào theo yêu cầu.
# - Cài đặt thuật toán, cấu trúc dữ liệu hoặc hàm xử lý chuỗi cần thiết.
# - Trả về hoặc in kết quả cuối cùng rõ ràng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
TICH_CUC = {"tốt", "hay", "vui", "thích", "đẹp", "great", "good", "happy", "love", "excellent"}
TIEU_CUC = {"xấu", "buồn", "ghét", "tệ", "kém", "bad", "sad", "hate", "poor", "terrible"}
van_ban = input("Nhập văn bản: ").lower()
cac_tu = re.findall(r"[^\W\d_]+", van_ban, flags=re.UNICODE)
diem = sum(1 for tu in cac_tu if tu in TICH_CUC) - sum(1 for tu in cac_tu if tu in TIEU_CUC)
print("Điểm sentiment:", diem)
if diem > 0:
    print("Cảm xúc tích cực")
elif diem < 0:
    print("Cảm xúc tiêu cực")
else:
    print("Cảm xúc trung tính")
