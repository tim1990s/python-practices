# Chương trình autocomplete bằng trie
#
# Yêu cầu:
# - Viết chương trình autocomplete bằng trie.
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
def thu_thap(node, tien_to, ket_qua):
    if "$" in node:
        ket_qua.append(tien_to)
    for ky_tu, node_con in node.items():
        if ky_tu != "$":
            thu_thap(node_con, tien_to + ky_tu, ket_qua)
def autocomplete(trie, tien_to):
    node = trie
    for ky_tu in tien_to:
        if ky_tu not in node:
            return []
        node = node[ky_tu]
    ket_qua = []
    thu_thap(node, tien_to, ket_qua)
    return ket_qua
trie = {}
cac_tu = [tu.strip().lower() for tu in input("Nhập danh sách từ, cách nhau bởi dấu phẩy: ").split(",") if tu.strip()]
for tu in cac_tu:
    them_tu(trie, tu)
tien_to = input("Nhập tiền tố: ").lower()
goi_y = autocomplete(trie, tien_to)
print("Không có gợi ý" if not goi_y else "Gợi ý: " + ", ".join(goi_y))
