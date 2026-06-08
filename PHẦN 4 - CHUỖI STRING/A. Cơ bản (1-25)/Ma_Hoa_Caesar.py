# Chương trình mã hóa Caesar
#
# Yêu cầu:
# - Viết chương trình mã hóa Caesar.
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

def dich_ky_tu(ky_tu, do_dich):
    if "a" <= ky_tu <= "z":
        return chr((ord(ky_tu) - ord("a") + do_dich) % 26 + ord("a"))
    if "A" <= ky_tu <= "Z":
        return chr((ord(ky_tu) - ord("A") + do_dich) % 26 + ord("A"))
    return ky_tu
chuoi = input("Nhập chuỗi cần mã hóa: ")
do_dich = int(input("Nhập độ dịch: "))
ket_qua = "".join(dich_ky_tu(ky_tu, do_dich) for ky_tu in chuoi)
print("Chuỗi sau mã hóa:", ket_qua)
