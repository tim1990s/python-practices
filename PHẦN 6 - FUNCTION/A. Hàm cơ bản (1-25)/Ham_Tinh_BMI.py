# Chương trình hàm tính BMI
#
# Yêu cầu:
# - Viết hàm tính chỉ số BMI.
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
# - Định nghĩa hàm nhận cân nặng và chiều cao.
# - Kiểm tra chiều cao lớn hơn 0.
# - Áp dụng công thức BMI = cân nặng / chiều cao^2.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tinh_bmi(can_nang, chieu_cao):
    if chieu_cao <= 0:
        return None
    return can_nang / (chieu_cao ** 2)


can_nang = float(input("Nhập cân nặng kg: "))
chieu_cao = float(input("Nhập chiều cao m: "))
ket_qua = tinh_bmi(can_nang, chieu_cao)
print("Chiều cao không hợp lệ" if ket_qua is None else "BMI:", round(ket_qua, 2))
