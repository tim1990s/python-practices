# Chương trình trích xuất địa chỉ IP
#
# Yêu cầu:
# - Viết chương trình trích xuất địa chỉ IP.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Phân tích nội dung văn bản để đếm, tách, thống kê hoặc trích xuất thông tin cần thiết.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc văn bản đầu vào.
# - Tách văn bản thành ký tự, từ, câu hoặc mẫu dữ liệu phù hợp.
# - Thống kê hoặc trích xuất rồi in kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
van_ban = input("Nhập văn bản: ")
ung_vien = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", van_ban)
dia_chi_ip = []
for ip in ung_vien:
    cac_phan = ip.split(".")
    if all(0 <= int(phan) <= 255 for phan in cac_phan):
        dia_chi_ip.append(ip)
if not dia_chi_ip:
    print("Không tìm thấy địa chỉ IPv4 hợp lệ")
else:
    print("Địa chỉ IP tìm thấy:")
    for ip in dia_chi_ip:
        print(ip)
