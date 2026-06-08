# Chương trình hàm đảo ngược số
#
# Yêu cầu:
# - Viết hàm đảo ngược chữ số của một số nguyên.
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
# - Giữ lại dấu của số.
# - Tách từng chữ số từ phải sang trái.
# - Xây số mới bằng cách nhân 10 và cộng chữ số.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dao_nguoc_so(n):
    dau = -1 if n < 0 else 1
    n = abs(n)
    ket_qua = 0
    while n > 0:
        ket_qua = ket_qua * 10 + n % 10
        n //= 10
    return dau * ket_qua


n = int(input("Nhập n: "))
print("Số đảo ngược:", dao_nguoc_so(n))
