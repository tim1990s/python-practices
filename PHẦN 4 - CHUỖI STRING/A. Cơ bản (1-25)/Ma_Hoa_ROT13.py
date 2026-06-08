# Chương trình mã hóa ROT13
#
# Yêu cầu:
# - Viết chương trình mã hóa ROT13.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Dùng các thao tác chuỗi cơ bản như độ dài, cắt chuỗi, đổi hoa thường, tìm kiếm hoặc thay thế.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi đầu vào từ bàn phím.
# - Áp dụng phương thức chuỗi hoặc phép cắt chuỗi phù hợp.
# - In kết quả sau khi xử lý.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def rot13_ky_tu(ky_tu):
    if "a" <= ky_tu <= "z":
        return chr((ord(ky_tu) - ord("a") + 13) % 26 + ord("a"))
    if "A" <= ky_tu <= "Z":
        return chr((ord(ky_tu) - ord("A") + 13) % 26 + ord("A"))
    return ky_tu
chuoi = input("Nhập chuỗi: ")
ket_qua = "".join(rot13_ky_tu(ky_tu) for ky_tu in chuoi)
print("Chuỗi sau ROT13:", ket_qua)
