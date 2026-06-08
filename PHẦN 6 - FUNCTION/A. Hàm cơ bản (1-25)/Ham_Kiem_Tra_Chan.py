# Chương trình hàm kiểm tra chẵn
#
# Yêu cầu:
# - Viết hàm kiểm tra một số nguyên có phải số chẵn không.
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
# - Định nghĩa hàm nhận một số nguyên.
# - Dùng phép chia dư cho 2.
# - Trả về True nếu số chẵn.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_so_chan(n):
    return n % 2 == 0


n = int(input("Nhập n: "))
print("Là số chẵn:", la_so_chan(n))
