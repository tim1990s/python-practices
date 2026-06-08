# Chương trình Recursive DFS
#
# Yêu cầu:
# - Viết hàm DFS đệ quy trên graph.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện các kỹ thuật hàm nâng cao: đệ quy, decorator, closure, higher-order function, generator, iterator, callback, async và các pattern đơn giản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Biểu diễn graph bằng dict.
# - Dùng set để lưu node đã thăm.
# - Gọi đệ quy cho từng hàng xóm chưa thăm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dfs(graph, node, da_tham=None):
    if da_tham is None:
        da_tham = set()
    da_tham.add(node)
    ket_qua = [node]
    for hang_xom in graph.get(node, []):
        if hang_xom not in da_tham:
            ket_qua.extend(dfs(graph, hang_xom, da_tham))
    return ket_qua


graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
bat_dau = input("Nhập node bắt đầu (A-E): ").strip() or "A"
print("Thứ tự DFS:", dfs(graph, bat_dau))
