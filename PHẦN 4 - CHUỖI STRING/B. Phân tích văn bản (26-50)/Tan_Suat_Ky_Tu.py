# Chương trình thống kê tần suất ký tự
#
# Yêu cầu:
# - Viết chương trình thống kê tần suất ký tự.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Phân tích nội dung văn bản để đếm, tách, thống kê hoặc trích xuất thông tin cần thiết.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc văn bản đầu vào.
# - Tách văn bản thành ký tự, từ, câu hoặc mẫu dữ liệu phù hợp.
# - Thống kê hoặc trích xuất rồi in kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from collections import Counter
chuoi = input("Nhập chuỗi: ")
tan_suat = Counter(chuoi)
if not tan_suat:
    print("Chuỗi rỗng")
else:
    print("Tần suất ký tự:")
    for ky_tu, so_lan in tan_suat.items():
        hien_thi = "khoảng trắng" if ky_tu == " " else ky_tu
        print(hien_thi + ":", so_lan)
