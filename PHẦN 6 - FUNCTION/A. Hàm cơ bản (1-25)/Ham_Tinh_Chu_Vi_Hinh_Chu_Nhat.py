# Chương trình hàm tính chu vi hình chữ nhật
#
# Yêu cầu:
# - Viết hàm tính chu vi hình chữ nhật.
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
# - Định nghĩa hàm nhận chiều dài và chiều rộng.
# - Kiểm tra hai kích thước dương.
# - Trả về 2 * (dài + rộng).

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def chu_vi_hinh_chu_nhat(dai, rong):
    if dai <= 0 or rong <= 0:
        return None
    return 2 * (dai + rong)


dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
ket_qua = chu_vi_hinh_chu_nhat(dai, rong)
print("Kích thước không hợp lệ" if ket_qua is None else "Chu vi:", ket_qua)
