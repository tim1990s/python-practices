# Chương trình Command Pattern
#
# Yêu cầu:
# - Viết ví dụ Command Pattern đơn giản.
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
# - Đóng gói hành động trong object.
# - Mỗi command có method execute().
# - Invoker gọi execute mà không cần biết chi tiết bên trong.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class InHoaCommand:
    def __init__(self, chuoi):
        self.chuoi = chuoi

    def execute(self):
        return self.chuoi.upper()


chuoi = input("Nhập chuỗi: ")
command = InHoaCommand(chuoi)
print("Kết quả:", command.execute())
