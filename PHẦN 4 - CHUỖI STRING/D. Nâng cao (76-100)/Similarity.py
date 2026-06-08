# Chương trình tính độ tương đồng chuỗi
#
# Yêu cầu:
# - Viết chương trình tính độ tương đồng chuỗi.
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

def levenshtein(a, b):
    hang_truoc = list(range(len(b) + 1))
    for i, ky_tu_a in enumerate(a, start=1):
        hang_hien_tai = [i]
        for j, ky_tu_b in enumerate(b, start=1):
            chi_phi = 0 if ky_tu_a == ky_tu_b else 1
            hang_hien_tai.append(min(hang_truoc[j] + 1, hang_hien_tai[j - 1] + 1, hang_truoc[j - 1] + chi_phi))
        hang_truoc = hang_hien_tai
    return hang_truoc[-1]
chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
do_dai_lon_nhat = max(len(chuoi_1), len(chuoi_2))
similarity = 1.0 if do_dai_lon_nhat == 0 else 1 - levenshtein(chuoi_1, chuoi_2) / do_dai_lon_nhat
print("Độ tương đồng:", round(similarity * 100, 2), "%")
