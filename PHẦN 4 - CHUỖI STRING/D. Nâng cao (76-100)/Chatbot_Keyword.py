# Chương trình chatbot keyword
#
# Yêu cầu:
# - Viết chương trình chatbot keyword.
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

CAU_TRA_LOI = {
    "xin chào": "Chào bạn!",
    "hello": "Hello!",
    "học": "Bạn có thể luyện Python mỗi ngày bằng bài nhỏ.",
    "python": "Python phù hợp để học lập trình cơ bản và xử lý dữ liệu.",
    "tạm biệt": "Tạm biệt!"
}
cau_hoi = input("Nhập câu hỏi: ").lower()
tra_loi = "Mình chưa có câu trả lời phù hợp."
for tu_khoa, noi_dung in CAU_TRA_LOI.items():
    if tu_khoa in cau_hoi:
        tra_loi = noi_dung
        break
print("Chatbot:", tra_loi)
