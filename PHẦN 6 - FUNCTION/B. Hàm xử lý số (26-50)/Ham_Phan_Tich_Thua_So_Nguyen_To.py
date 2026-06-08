# Chương trình hàm phân tích thừa số nguyên tố
#
# Yêu cầu:
# - Viết hàm phân tích một số thành các thừa số nguyên tố.
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
# - Duyệt ước từ 2 trở lên.
# - Khi chia hết thì thêm ước vào kết quả.
# - Tiếp tục chia cho đến khi không còn chia hết.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def phan_tich_thua_so(n):
    if n < 2:
        return []
    ket_qua = []
    uoc = 2
    while uoc * uoc <= n:
        while n % uoc == 0:
            ket_qua.append(uoc)
            n //= uoc
        uoc += 1
    if n > 1:
        ket_qua.append(n)
    return ket_qua


n = int(input("Nhập n: "))
print("Các thừa số nguyên tố:", phan_tich_thua_so(n))
