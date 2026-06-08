# Chương trình Observer Pattern
#
# Yêu cầu:
# - Viết ví dụ Observer Pattern đơn giản.
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
# - Subject lưu danh sách observer.
# - Observer là hàm callback.
# - Khi có dữ liệu mới thì notify toàn bộ observer.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for observer in self.observers:
            observer(data)


def logger(data):
    print("Logger nhận:", data)


subject = Subject()
subject.subscribe(logger)
data = input("Nhập dữ liệu event: ")
subject.notify(data)
