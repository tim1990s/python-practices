# Chương trình hàm đổi độ C sang độ F
#
# Yêu cầu:
# - Viết hàm chuyển nhiệt độ Celsius sang Fahrenheit.
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
# - Định nghĩa hàm nhận độ C.
# - Áp dụng công thức F = C * 9/5 + 32.
# - Trả về độ F.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def c_sang_f(c):
    return c * 9 / 5 + 32


c = float(input("Nhập độ C: "))
print("Độ F:", c_sang_f(c))
