# Chương trình Async Function
#
# Yêu cầu:
# - Viết hàm async đơn giản.
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
# - Định nghĩa async function.
# - Dùng await asyncio.sleep để mô phỏng tác vụ bất đồng bộ.
# - Chạy bằng asyncio.run().

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import asyncio


async def xu_ly_async(noi_dung):
    await asyncio.sleep(0.1)
    return "Đã xử lý: " + noi_dung


async def main():
    noi_dung = input("Nhập nội dung: ")
    ket_qua = await xu_ly_async(noi_dung)
    print(ket_qua)


asyncio.run(main())
