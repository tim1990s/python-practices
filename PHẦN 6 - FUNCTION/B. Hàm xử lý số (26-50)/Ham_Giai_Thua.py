# Chương trình hàm giai thừa
#
# Yêu cầu:
# - Viết hàm tính giai thừa của n.
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
# - Giai thừa chỉ áp dụng cho số nguyên không âm.
# - Nhân các số từ 1 đến n.
# - Trả về tích cuối cùng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def giai_thua(n):
    if n < 0:
        return None
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua


n = int(input("Nhập n: "))
ket_qua = giai_thua(n)
print("n không hợp lệ" if ket_qua is None else "Giai thừa:", ket_qua)
