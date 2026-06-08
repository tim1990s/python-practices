# Chương trình hàm parser key-value
#
# Yêu cầu:
# - Viết hàm parse chuỗi key=value thành dict.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Tách chuỗi theo dấu phẩy.
# - Mỗi phần tách tiếp theo dấu bằng.
# - Lưu key và value vào dict.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def parse_key_value(chuoi):
    ket_qua = {}
    for cap in chuoi.split(","):
        if "=" in cap:
            key, value = cap.split("=", 1)
            ket_qua[key.strip()] = value.strip()
    return ket_qua


chuoi = input("Nhập chuỗi dạng key=value,key=value: ")
print("Kết quả parse:", parse_key_value(chuoi))
