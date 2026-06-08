# Chương trình hàm tính tổng chữ số
#
# Yêu cầu:
# - Viết hàm tính tổng các chữ số của một số nguyên.
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
# - Lấy trị tuyệt đối của số.
# - Dùng vòng lặp chia lấy dư cho 10.
# - Cộng từng chữ số vào tổng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tong_chu_so(n):
    n = abs(n)
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong


n = int(input("Nhập n: "))
print("Tổng chữ số:", tong_chu_so(n))
