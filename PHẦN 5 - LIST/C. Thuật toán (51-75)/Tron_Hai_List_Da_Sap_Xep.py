# Chương trình trộn hai list đã sắp xếp
#
# Yêu cầu:
# - Viết chương trình trộn hai list tăng dần thành một list tăng dần.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện các thuật toán phổ biến trên list như sắp xếp, tìm kiếm, chia tách, tổng tiền tố và xử lý dãy con.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc hai list tăng dần.
# - Dùng hai con trỏ để so sánh.
# - Thêm phần tử nhỏ hơn vào list kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so_nguyen(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [int(x.strip()) for x in du_lieu.split(",") if x.strip()]

a = doc_list_so_nguyen("Nhập list thứ nhất đã sắp xếp: ")
b = doc_list_so_nguyen("Nhập list thứ hai đã sắp xếp: ")
i = j = 0
ket_qua = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        ket_qua.append(a[i])
        i += 1
    else:
        ket_qua.append(b[j])
        j += 1
ket_qua.extend(a[i:])
ket_qua.extend(b[j:])
print("List sau khi trộn:", ket_qua)
