# Chương trình tạo N-gram
#
# Yêu cầu:
# - Viết chương trình tạo N-gram.
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

import re
van_ban = input("Nhập văn bản: ")
n = int(input("Nhập n: "))
cac_tu = re.findall(r"[^\W\d_]+", van_ban.lower(), flags=re.UNICODE)
if n <= 0:
    print("n phải lớn hơn 0")
elif n > len(cac_tu):
    print("Không đủ từ để tạo n-gram")
else:
    print(str(n) + "-gram:")
    for i in range(len(cac_tu) - n + 1):
        print(" ".join(cac_tu[i:i + n]))
