# Chương trình hàm tính giá trị tuyệt đối
#
# Yêu cầu:
# - Viết hàm tính giá trị tuyệt đối của một số.
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
# - Nếu số âm thì đổi dấu.
# - Trả về giá trị không âm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def gia_tri_tuyet_doi(x):
    return -x if x < 0 else x


x = float(input("Nhập x: "))
print("Giá trị tuyệt đối:", gia_tri_tuyet_doi(x))
