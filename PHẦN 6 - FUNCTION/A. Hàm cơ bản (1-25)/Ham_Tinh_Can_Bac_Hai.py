# Chương trình hàm tính căn bậc hai
#
# Yêu cầu:
# - Viết hàm tính căn bậc hai của một số không âm.
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
# - Định nghĩa hàm nhận một số.
# - Kiểm tra số có âm không.
# - Trả về căn bậc hai nếu hợp lệ.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def can_bac_hai(x):
    if x < 0:
        return "Không tính căn bậc hai của số âm trong tập số thực"
    return math.sqrt(x)


x = float(input("Nhập x: "))
print("Căn bậc hai:", can_bac_hai(x))
