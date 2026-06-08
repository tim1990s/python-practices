# Chương trình hàm chuyển sang thập lục phân
#
# Yêu cầu:
# - Viết hàm chuyển số nguyên không âm sang hệ thập lục phân.
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
# - Dùng hàm hex() để chuyển hệ.
# - Bỏ tiền tố 0x trước khi trả về.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def sang_thap_luc_phan(n):
    if n < 0:
        return None
    return hex(n)[2:].upper()


n = int(input("Nhập n: "))
ket_qua = sang_thap_luc_phan(n)
print("n không hợp lệ" if ket_qua is None else "Thập lục phân:", ket_qua)
