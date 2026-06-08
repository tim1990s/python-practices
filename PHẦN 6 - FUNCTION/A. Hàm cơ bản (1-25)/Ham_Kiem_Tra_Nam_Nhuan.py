# Chương trình hàm kiểm tra năm nhuận
#
# Yêu cầu:
# - Viết hàm kiểm tra một năm có phải năm nhuận không.
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
# - Định nghĩa hàm nhận năm.
# - Áp dụng quy tắc chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100.
# - Trả về True hoặc False.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_nam_nhuan(nam):
    return nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)


nam = int(input("Nhập năm: "))
print("Là năm nhuận:", la_nam_nhuan(nam))
