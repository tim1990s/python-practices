# Chương trình trie đơn giản
#
# Yêu cầu:
# - Viết chương trình trie đơn giản.
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

def them_tu(trie, tu):
    node = trie
    for ky_tu in tu:
        node = node.setdefault(ky_tu, {})
    node["$"] = True
def tim_tu(trie, tu):
    node = trie
    for ky_tu in tu:
        if ky_tu not in node:
            return False
        node = node[ky_tu]
    return "$" in node
trie = {}
cac_tu = [tu.strip() for tu in input("Nhập danh sách từ, cách nhau bởi dấu phẩy: ").split(",") if tu.strip()]
for tu in cac_tu:
    them_tu(trie, tu.lower())
tu_can_tim = input("Nhập từ cần tìm: ").lower()
print("Từ có trong trie" if tim_tu(trie, tu_can_tim) else "Từ không có trong trie")
