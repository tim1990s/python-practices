# Chương trình hàm kiểm tra số palindrome
#
# Yêu cầu:
# - Viết hàm kiểm tra số nguyên có đối xứng hay không.
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
# - Số âm không xem là palindrome.
# - Đảo ngược số.
# - So sánh số đảo ngược với số ban đầu.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dao_nguoc_so(n):
    ket_qua = 0
    while n > 0:
        ket_qua = ket_qua * 10 + n % 10
        n //= 10
    return ket_qua


def la_palindrome_so(n):
    return n >= 0 and n == dao_nguoc_so(n)


n = int(input("Nhập n: "))
print("Là số palindrome:", la_palindrome_so(n))
