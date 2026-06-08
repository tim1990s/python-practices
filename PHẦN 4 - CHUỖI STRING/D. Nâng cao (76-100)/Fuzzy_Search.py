# Chương trình fuzzy search đơn giản
#
# Yêu cầu:
# - Viết chương trình fuzzy search đơn giản.
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
query = input("Nhập từ khóa: ").lower()
danh_sach = [tu.strip() for tu in input("Nhập danh sách từ, cách nhau bởi dấu phẩy: ").split(",") if tu.strip()]
nguong = int(input("Nhập ngưỡng khoảng cách tối đa: "))
ket_qua = [(tu, levenshtein(query, tu.lower())) for tu in danh_sach]
ket_qua = sorted([item for item in ket_qua if item[1] <= nguong], key=lambda item: item[1])
if not ket_qua:
    print("Không tìm thấy kết quả phù hợp")
else:
    print("Kết quả fuzzy search:")
    for tu, khoang_cach in ket_qua:
        print(tu + ":", khoang_cach)
