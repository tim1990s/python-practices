# Chương trình tìm kiếm Boyer-Moore đơn giản
#
# Yêu cầu:
# - Viết chương trình tìm kiếm Boyer-Moore đơn giản.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Cài đặt thuật toán hoặc kỹ thuật xử lý chuỗi nâng cao để giải quyết bài toán.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc dữ liệu đầu vào theo yêu cầu.
# - Cài đặt thuật toán, cấu trúc dữ liệu hoặc hàm xử lý chuỗi cần thiết.
# - Trả về hoặc in kết quả cuối cùng rõ ràng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def boyer_moore(van_ban, mau):
    if mau == "":
        return [0]
    bang_xau = {ky_tu: vi_tri for vi_tri, ky_tu in enumerate(mau)}
    ket_qua = []
    i = 0
    while i <= len(van_ban) - len(mau):
        j = len(mau) - 1
        while j >= 0 and mau[j] == van_ban[i + j]:
            j -= 1
        if j < 0:
            ket_qua.append(i)
            i += 1
        else:
            i += max(1, j - bang_xau.get(van_ban[i + j], -1))
    return ket_qua
van_ban = input("Nhập văn bản: ")
mau = input("Nhập mẫu cần tìm: ")
vi_tri = boyer_moore(van_ban, mau)
print("Không tìm thấy" if not vi_tri else "Vị trí tìm thấy: " + str(vi_tri))
