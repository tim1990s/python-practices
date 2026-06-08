# Chương trình hàm đổi độ F sang độ C
#
# Yêu cầu:
# - Viết hàm chuyển nhiệt độ Fahrenheit sang Celsius.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện cách khai báo hàm, truyền tham số, trả về kết quả bằng return và tách chương trình thành các khối xử lý nhỏ.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Định nghĩa hàm nhận độ F.
# - Áp dụng công thức C = (F - 32) * 5/9.
# - Trả về độ C.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def f_sang_c(f):
    return (f - 32) * 5 / 9


f = float(input("Nhập độ F: "))
print("Độ C:", f_sang_c(f))
