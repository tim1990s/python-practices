# Chương trình hàm chuyển sang bát phân
#
# Yêu cầu:
# - Viết hàm chuyển số nguyên không âm sang hệ bát phân.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý số nguyên, số thực, chữ số, ước số, bội số, dãy Fibonacci và các bài toán số học cơ bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Kiểm tra n không âm.
# - Dùng hàm oct() để chuyển hệ.
# - Bỏ tiền tố 0o trước khi trả về.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def sang_bat_phan(n):
    if n < 0:
        return None
    return oct(n)[2:]


n = int(input("Nhập n: "))
ket_qua = sang_bat_phan(n)
print("n không hợp lệ" if ket_qua is None else "Bát phân:", ket_qua)
