# Chương trình kiểm tra list đã sắp xếp
#
# Yêu cầu:
# - Viết chương trình kiểm tra list có tăng dần hay không.
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
# - Đọc list số nguyên.
# - So sánh các cặp liền kề.
# - Nếu mọi cặp đúng thứ tự thì list đã sắp xếp.

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

danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
da_sap_xep = all(danh_sach[i] <= danh_sach[i + 1] for i in range(len(danh_sach) - 1))
print("List đã được sắp xếp tăng dần" if da_sap_xep else "List chưa được sắp xếp tăng dần")
