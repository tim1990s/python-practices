# Chương trình Recursive Tree Traversal
#
# Yêu cầu:
# - Viết hàm duyệt cây nhị phân bằng đệ quy.
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
# - Biểu diễn node bằng dict.
# - Duyệt trái, gốc, phải theo inorder.
# - Trả về list giá trị đã duyệt.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def inorder(node):
    if node is None:
        return []
    return inorder(node.get("left")) + [node["value"]] + inorder(node.get("right"))


tree = {
    "value": 4,
    "left": {"value": 2, "left": {"value": 1}, "right": {"value": 3}},
    "right": {"value": 6, "left": {"value": 5}, "right": {"value": 7}},
}
print("Inorder traversal:", inorder(tree))
