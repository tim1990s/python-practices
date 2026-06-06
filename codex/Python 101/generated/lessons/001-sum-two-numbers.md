# 001. Tổng hai số

        # Learning Objectives

        Sau bài học này, bạn cần đạt được bốn mục tiêu. Thứ nhất, bạn hiểu đề bài
        `Tổng hai số` không chỉ như một yêu cầu tính kết quả, mà như một
        đặc tả nhỏ gồm dữ liệu vào, dữ liệu ra và quy tắc xử lý. Thứ hai, bạn biết
        sử dụng các kiến thức Python liên quan: int(), split(), toán tử +. Thứ ba, bạn kết
        nối được phần lập trình với nền tảng toán học hoặc tư duy logic: Phép cộng số nguyên.
        Thứ tư, bạn có thể tự viết lại lời giải theo từng bước, kiểm tra bằng ví dụ
        mẫu, rồi điều chỉnh nếu gặp dữ liệu khác.

        Bài học cũng rèn thói quen đọc kỹ input và output trước khi viết code. Với
        người mới học, lỗi thường không nằm ở cú pháp phức tạp mà nằm ở việc hiểu
        sai đề: đọc thiếu một dòng, in thừa chữ, làm tròn sai định dạng, hoặc dùng
        nhầm kiểu dữ liệu. Vì vậy, mục tiêu quan trọng là xây dựng quy trình làm bài:
        xác định dữ liệu, chọn biến, viết thuật toán, chuyển thuật toán thành Python,
        chạy thử với ví dụ, sau đó nghĩ thêm về các trường hợp biên.

        # Theory

        Trong nhóm bài Basic Math, trọng tâm không phải là công thức khó mà là cách biến một yêu cầu toán học thành chương trình Python tuyến tính. Người học cần nhìn thấy luồng dữ liệu đi từ input, qua biến trung gian, đến output. Đây là nền tảng cho mọi bài sau này, vì nếu chưa hiểu dữ liệu được đọc, chuyển kiểu và tính toán như thế nào thì các cấu trúc phức tạp hơn cũng sẽ trở nên mơ hồ.

        Trong bài này, các chủ đề Python chính là int(), split(), toán tử +. Bạn không nên
        học chúng như những lệnh rời rạc. Hãy xem mỗi chủ đề là một công cụ trong
        một chuỗi xử lý. `input()` hoặc `sys.stdin.read()` đưa dữ liệu thô vào chương
        trình dưới dạng chuỗi. Các hàm chuyển kiểu như `int()` và `float()` biến dữ
        liệu đó thành dạng có thể tính toán. Các toán tử, điều kiện, vòng lặp, list
        hoặc hàm sẽ thực hiện logic chính. Cuối cùng, `print()` hoặc `sys.stdout.write()`
        biến kết quả thành văn bản để người chấm hoặc người dùng đọc được.

        Một thói quen tốt là đặt tên biến theo ý nghĩa của dữ liệu, không đặt theo
        cảm hứng nhất thời. Nếu đề nói đến bán kính, hãy dùng `radius`; nếu đề nói
        đến danh sách số, hãy dùng `numbers`; nếu đề nói đến mục tiêu tìm kiếm, hãy
        dùng `target`. Tên biến rõ giúp bạn giảm gánh nặng ghi nhớ. Khi quay lại bài
        sau vài ngày, bạn vẫn hiểu code đang làm gì mà không cần đọc từng toán tử.

        Cũng cần phân biệt giữa code chạy được và code dễ học. Một dòng Python quá
        ngắn đôi khi tạo cảm giác giỏi, nhưng với người mới, việc tách thành hàm nhỏ
        hoặc biến trung gian thường hữu ích hơn. Biến trung gian cho phép bạn đặt
        tên cho từng ý tưởng: dữ liệu đã chuẩn hóa, tổng hiện tại, căn bậc hai,
        kết quả phân loại. Khi thuật toán rõ ràng, Python chỉ còn là cách diễn đạt.

        Hãy tưởng tượng chương trình như một quầy xử lý hồ sơ. Input là hồ sơ được
        đưa vào quầy. Phần xử lý kiểm tra giấy tờ, tính toán hoặc phân loại. Output
        là kết quả trả lại. Nếu hồ sơ đầu vào chưa được chuyển đúng dạng, bước xử lý
        phía sau sẽ sai. Nếu quy tắc xử lý không rõ, kết quả trả ra có thể hợp cú
        pháp nhưng sai nghiệp vụ. Lập trình tốt bắt đầu từ việc kiểm soát luồng này.

        # Mathematical Background

        Phần toán học hoặc tư duy nền tảng của bài là: Phép cộng số nguyên. Với các bài
        cơ bản, toán học thường là công thức quen thuộc. Với các bài điều kiện, toán
        học nằm trong quy tắc phân loại. Với vòng lặp, toán học xuất hiện ở mẫu lặp,
        biến tích lũy và điều kiện dừng. Với chuỗi và list, tư duy quan trọng là xem
        dữ liệu như một dãy phần tử rồi xử lý từng phần tử theo cùng một tiêu chí.

        Khi gặp một bài toán như `Tổng hai số`, bạn nên tự hỏi: đại lượng nào
        đã biết, đại lượng nào cần tìm, và quan hệ giữa chúng là gì. Nếu có công thức,
        hãy viết công thức bằng lời trước. Nếu có quy tắc, hãy liệt kê từng trường hợp.
        Nếu phải duyệt dữ liệu, hãy xác định mỗi vòng lặp cần cập nhật thông tin nào.
        Cách suy nghĩ này giúp bạn không bị cuốn vào việc gõ code quá sớm.

        Một điểm quan trọng khác là trường hợp biên. Trường hợp biên là dữ liệu vẫn
        hợp lệ nhưng dễ làm chương trình sai, ví dụ số 0, list chỉ có một phần tử,
        chuỗi rỗng, số âm, điểm đúng bằng ngưỡng, hoặc phương trình có delta bằng 0.
        Không phải bài nào cũng có tất cả các trường hợp này, nhưng thói quen nghĩ
        về chúng sẽ giúp bạn viết chương trình ổn định hơn.

        # Problem Statement

        Nhập hai số nguyên a và b, sau đó in ra tổng của chúng.

        Hãy đọc câu trên như một hợp đồng. Chương trình của bạn nhận đúng dữ liệu
        được mô tả, xử lý đúng quy tắc, và chỉ in đúng kết quả được yêu cầu. Trong
        môi trường học thuật hoặc chấm tự động, việc in thêm lời chào, chú thích,
        hoặc đơn vị không được yêu cầu đều có thể khiến bài bị sai dù thuật toán đúng.

        # Input

        Một dòng gồm hai số nguyên a và b, cách nhau bởi dấu cách.

        Trước khi parse input, hãy xác định dữ liệu gồm bao nhiêu dòng và mỗi dòng
        có bao nhiêu phần. Nếu dữ liệu nằm trên một dòng, `split()` thường đủ. Nếu
        dữ liệu có thể chứa cả khoảng trắng như một câu hoặc họ tên, bạn cần đọc cả
        dòng hoặc toàn bộ nội dung thay vì tách quá sớm.

        # Output

        Một số nguyên duy nhất là a + b.

        Output là phần dễ bị xem nhẹ. Bạn cần chú ý chữ hoa chữ thường, số chữ số
        thập phân, thứ tự in kết quả và việc có hay không có dấu cách cuối dòng. Với
        số thực, định dạng như `{value:.2f}` giúp kết quả thống nhất và dễ so sánh.

        # Example

        Sample Input:

        ```text
        3 5
        ```

        Sample Output:

        ```text
        8
        ```

        Explanation:

        Tổng của 3 và 5 là 8.

        Ví dụ mẫu không chỉ để minh họa. Nó là bài kiểm tra đầu tiên cho chương trình.
        Nếu chương trình không tạo ra đúng output mẫu, hãy kiểm tra lại từng bước:
        đọc input có đúng không, kiểu dữ liệu có đúng không, công thức hoặc điều kiện
        có đúng không, và định dạng in ra có khớp yêu cầu không.

        # Algorithm

        1. Đọc hai số nguyên a và b từ input.
2. Tính tổng bằng phép cộng.
3. In tổng ra màn hình.

        Thuật toán trên được viết bằng ngôn ngữ tự nhiên để bạn nhìn thấy ý tưởng
        trước khi nhìn thấy Python. Khi tự luyện tập, hãy cố gắng viết phần này ra
        giấy hoặc ghi chú trước. Nếu bạn không thể mô tả thuật toán bằng lời, việc
        viết code thường sẽ biến thành thử sai. Ngược lại, khi các bước đã rõ, mỗi
        dòng code chỉ cần bám theo một bước cụ thể.

        # Pseudocode

        ```text
        BEGIN
  Đọc hai số nguyên a và b từ input.
  Tính tổng bằng phép cộng.
  In tổng ra màn hình.
END
        ```

        Pseudocode là cầu nối giữa ý tưởng và Python. Nó bỏ qua chi tiết cú pháp,
        nhưng vẫn giữ thứ tự xử lý. Với người mới, pseudocode giúp giảm áp lực phải
        nhớ chính xác dấu ngoặc, dấu hai chấm hoặc tên hàm ngay từ đầu.

        # Python Solution

        ```python
        import sys


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    # Read both numbers from one line.
    a, b = map(int, sys.stdin.read().split())
    print(add_numbers(a, b))


if __name__ == "__main__":
    main()

        ```

        # Code Explanation

        Lời giải Python được viết theo cấu trúc có hàm xử lý và hàm `main()`. Hàm xử
        lý chứa logic chính của bài, còn `main()` chịu trách nhiệm đọc input và in
        output. Cách tách này giúp bạn kiểm tra logic dễ hơn. Nếu muốn thử nhiều bộ
        dữ liệu, bạn có thể gọi trực tiếp hàm xử lý trong Python shell hoặc trong
        một file test nhỏ mà không cần nhập lại từ bàn phím.

        Các dòng đọc dữ liệu dùng đúng định dạng input của bài. Khi đề yêu cầu số
        nguyên, chương trình chuyển sang `int`; khi đề yêu cầu số thực, chương trình
        chuyển sang `float`; khi đề xử lý văn bản, chương trình giữ dữ liệu ở dạng
        chuỗi. Đây là bước rất quan trọng vì Python không tự đoán rằng chuỗi `"5"`
        nên được cộng như số 5. Nếu quên chuyển kiểu, phép cộng có thể trở thành nối
        chuỗi hoặc gây lỗi.

        Phần xử lý chính bám sát thuật toán đã nêu. Với bài tính toán, code thường
        dùng công thức trực tiếp. Với bài điều kiện, code dùng các nhánh rõ ràng để
        tránh nhập nhằng. Với bài vòng lặp, code khởi tạo biến trước vòng lặp, cập
        nhật biến trong vòng lặp, rồi trả về kết quả sau khi vòng lặp kết thúc. Với
        bài list hoặc chuỗi, code duyệt từng phần tử và chỉ lưu thêm dữ liệu khi cần.

        Các comment trong solution chỉ xuất hiện ở nơi giúp người học định hướng.
        Không phải dòng nào cũng cần comment. Ví dụ, `return a + b` đã đủ rõ, nhưng
        một bước như chuẩn hóa chuỗi, cập nhật dictionary tần suất, hoặc xử lý phương
        trình suy biến nên có tên hàm hoặc comment rõ hơn. Comment tốt giải thích
        lý do hoặc ý tưởng, không lặp lại máy móc điều code đã nói.

        # Complexity Analysis

        Độ phức tạp thời gian phụ thuộc vào số lượng phần tử mà chương trình phải
        xử lý. Nếu bài chỉ đọc vài số cố định và áp dụng công thức, thời gian là
        O(1). Nếu bài duyệt từ 1 đến n, thời gian thường là O(n). Nếu bài duyệt một
        chuỗi hoặc list có n phần tử, thời gian cũng thường là O(n). Nếu có sắp xếp,
        thời gian có thể là O(n log n). Với bài này, hãy nhìn vào vòng lặp hoặc thao
        tác sắp xếp trong code để xác định chi phí chính.

        Độ phức tạp bộ nhớ cho biết chương trình cần thêm bao nhiêu bộ nhớ ngoài dữ
        liệu đầu vào. Nếu chỉ dùng vài biến, bộ nhớ phụ là O(1). Nếu tạo list kết quả,
        set các giá trị đã gặp, hoặc dictionary tần suất, bộ nhớ phụ có thể là O(n).
        Việc hiểu complexity không chỉ để thi thuật toán; nó giúp bạn dự đoán chương
        trình có còn chạy tốt khi dữ liệu lớn hơn ví dụ mẫu hay không.

        # Common Mistakes

        Một lỗi phổ biến là đọc input sai dạng. Nếu đề có nhiều số trên một dòng mà
        bạn chỉ gọi `input()` một lần nhưng không `split()`, chương trình sẽ không có
        đủ dữ liệu. Ngược lại, nếu đề là một câu văn có khoảng trắng mà bạn dùng
        `split()` ngay, bạn có thể làm mất cấu trúc ban đầu của chuỗi.

        Lỗi thứ hai là dùng sai kiểu dữ liệu. Số thực cần `float`, số nguyên cần
        `int`, còn chuỗi cần được giữ nguyên khi bài yêu cầu xử lý ký tự. Lỗi thứ ba
        là in sai định dạng: thiếu chữ hoa, thừa dấu cách, hoặc không làm tròn số
        thực đúng yêu cầu. Lỗi thứ tư là bỏ qua trường hợp biên như 0, dữ liệu chỉ
        có một phần tử, hoặc giá trị nằm đúng trên ngưỡng so sánh.

        Khi debug, đừng sửa ngẫu nhiên nhiều chỗ cùng lúc. Hãy in thử dữ liệu sau khi
        đọc, kiểm tra biến trung gian, rồi đối chiếu từng bước với thuật toán. Sau
        khi hiểu lỗi, hãy bỏ các dòng in thử để output cuối cùng sạch và đúng đặc tả.

        # Additional Exercises

        1. Thay đổi dữ liệu mẫu và tự dự đoán output trước khi chạy chương trình.
        2. Viết thêm ít nhất ba test case, trong đó có một trường hợp biên.
        3. Tách phần xử lý thành hàm riêng nếu solution hiện tại chưa có hàm.
        4. Viết lại thuật toán bằng lời của bạn mà không nhìn vào bài học.
        5. Mở rộng bài toán bằng cách xử lý nhiều bộ test liên tiếp.

        # Further Reading

        Để học sâu hơn, hãy đọc lại tài liệu Python về các chủ đề: int(), split(), toán tử +.
        Sau đó xem lại phần toán hoặc tư duy nền tảng: Phép cộng số nguyên. Bạn cũng nên
        luyện lại các kiến thức tiên quyết: Biến, Số nguyên, input(), print(). Khi gặp bài tương tự,
        hãy bắt đầu từ đặc tả input/output, viết thuật toán ngắn, sau đó mới chuyển
        sang Python. Đây là quy trình quan trọng hơn việc ghi nhớ một lời giải cụ
        thể, vì nó giúp bạn tự giải được bài mới.
