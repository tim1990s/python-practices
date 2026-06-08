# Chương trình tìm kiếm KMP
#
# Yêu cầu:
# - Viết chương trình tìm kiếm KMP.
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

def tao_bang_lps(mau):
    lps = [0] * len(mau)
    do_dai = 0
    i = 1
    while i < len(mau):
        if mau[i] == mau[do_dai]:
            do_dai += 1
            lps[i] = do_dai
            i += 1
        elif do_dai != 0:
            do_dai = lps[do_dai - 1]
        else:
            i += 1
    return lps
def kmp_search(van_ban, mau):
    if mau == "":
        return [0]
    lps = tao_bang_lps(mau)
    ket_qua = []
    i = j = 0
    while i < len(van_ban):
        if van_ban[i] == mau[j]:
            i += 1
            j += 1
        if j == len(mau):
            ket_qua.append(i - j)
            j = lps[j - 1]
        elif i < len(van_ban) and van_ban[i] != mau[j]:
            j = lps[j - 1] if j != 0 else 0
            if j == 0:
                i += 1
    return ket_qua
van_ban = input("Nhập văn bản: ")
mau = input("Nhập mẫu cần tìm: ")
vi_tri = kmp_search(van_ban, mau)
print("Không tìm thấy" if not vi_tri else "Vị trí tìm thấy: " + str(vi_tri))
