# Chương trình hàm giải mã Caesar
#
# Yêu cầu:
# - Viết hàm giải mã chuỗi Caesar cipher.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Giải mã bằng cách dịch ngược khóa.
# - Tái sử dụng logic mã hóa.
# - Trả về chuỗi đã giải mã.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dich_caesar(chuoi, k):
    ket_qua = []
    for ky_tu in chuoi:
        if ky_tu.isalpha() and ky_tu.isascii():
            goc = ord("A") if ky_tu.isupper() else ord("a")
            ket_qua.append(chr((ord(ky_tu) - goc + k) % 26 + goc))
        else:
            ket_qua.append(ky_tu)
    return "".join(ket_qua)


chuoi = input("Nhập chuỗi đã mã hóa: ")
k = int(input("Nhập khóa k: "))
print("Chuỗi giải mã:", dich_caesar(chuoi, -k))
