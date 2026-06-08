# Chương trình tìm kiếm Rabin-Karp
#
# Yêu cầu:
# - Viết chương trình tìm kiếm Rabin-Karp.
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

def rabin_karp(van_ban, mau):
    if mau == "":
        return [0]
    if len(mau) > len(van_ban):
        return []
    co_so = 256
    modulo = 101
    m = len(mau)
    hash_mau = hash_cua_so = 0
    he_so = 1
    ket_qua = []
    for _ in range(m - 1):
        he_so = (he_so * co_so) % modulo
    for i in range(m):
        hash_mau = (co_so * hash_mau + ord(mau[i])) % modulo
        hash_cua_so = (co_so * hash_cua_so + ord(van_ban[i])) % modulo
    for i in range(len(van_ban) - m + 1):
        if hash_mau == hash_cua_so and van_ban[i:i + m] == mau:
            ket_qua.append(i)
        if i < len(van_ban) - m:
            hash_cua_so = (co_so * (hash_cua_so - ord(van_ban[i]) * he_so) + ord(van_ban[i + m])) % modulo
    return ket_qua
van_ban = input("Nhập văn bản: ")
mau = input("Nhập mẫu cần tìm: ")
vi_tri = rabin_karp(van_ban, mau)
print("Không tìm thấy" if not vi_tri else "Vị trí tìm thấy: " + str(vi_tri))
