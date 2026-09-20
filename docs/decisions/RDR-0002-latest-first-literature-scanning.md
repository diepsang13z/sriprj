# RDR-0002: Latest-first Literature Scanning Policy

- **Trạng thái:** ACCEPTED
- **Ngày quyết định:** 2026-09-20
- **Người đề xuất:** Nghiên cứu viên
- **Phạm vi áp dụng:** Mọi vòng tìm kiếm và bổ sung tài liệu sau Survey Round 1

---

## 1. Bối cảnh (Context)

Khảo sát mở theo toàn bộ lịch sử công bố tạo nhiều kết quả cũ, trùng lặp và làm chậm việc xác định đóng góp mới nhất của đề tài. Dự án cần ưu tiên các công trình phản ánh theory, operationalization, dataset và phương pháp hiện hành.

Tuy nhiên, chính sách “chỉ đọc bài mới” tuyệt đối có thể làm mất nguồn gốc của construct, thang đo hoặc công thức mà bài mới chỉ trích dẫn lại. Vì vậy, quyết định này tách **quét chủ động** khỏi **truy xuất nguồn nền tảng để xác minh**.

---

## 2. Quyết định (Decision)

### 2.1. Cửa sổ “mới nhất”

1. Mọi lượt **quét chủ động** MUST giới hạn trong **36 tháng gần nhất** tính đến ngày tìm kiếm.
2. Ngày công bố được xác định bằng ngày xuất bản công khai đầu tiên: `online-first` nếu có, nếu không dùng ngày phát hành số tạp chí.
3. Kết quả MUST được sắp xếp từ mới đến cũ; ưu tiên article in press/online-first đã có DOI và metadata chính thức.
4. Với ngày tìm kiếm 2026-09-20, cửa sổ hiện tại là **2023-09-20 đến 2026-09-20**.

### 2.2. Phạm vi quét

Mỗi vòng chỉ quét các bài mới thuộc ba cụm của `RDR-0001`:

1. Review Inconsistency / Sentiment–Rating Discrepancy.
2. Hospitality ABSA / rating prediction.
3. Customer Forgiveness / Justice / Buffering.

Việc mở rộng truy vấn sang tài liệu cũ ngoài cửa sổ chỉ để “đọc cho đủ” hoặc tăng số lượng MUST NOT thực hiện.

### 2.3. Ngoại lệ có kiểm soát

Nguồn cũ hơn 36 tháng MAY được mở khi thỏa mãn đồng thời:

1. Một bài nằm trong cửa sổ mới nhất trích dẫn trực tiếp nguồn đó.
2. Nguồn cũ chứa định nghĩa construct, theory gốc, thang đo, công thức, dataset hoặc baseline mà bài mới không trình bày đủ để tái lập.
3. Nhật ký khảo sát ghi rõ bài mới dẫn tới nguồn cũ và lý do truy xuất.

Nguồn ngoại lệ dùng để **xác minh provenance**, không mở thêm một nhánh quét lịch sử. Các core papers cũ đã có trong `refs/INDEX.md` được giữ lại nhưng không tự động tạo thêm truy vấn cũ.

### 2.4. Kỷ luật ghi nhận

Mỗi survey round MUST ghi:

- Ngày quét và cửa sổ 36 tháng tương ứng.
- Cơ sở dữ liệu/nhà xuất bản và query đã dùng.
- DOI, ngày online-first và trạng thái full text/abstract-only.
- Mọi ngoại lệ ngoài cửa sổ cùng lý do.
- Số bài mới tạo thêm construct, theory, measure hoặc baseline để đánh giá saturation theo `RDR-0001`.

---

## 3. Phương án đã loại (Rejected Alternatives)

### Quét không giới hạn năm

Loại vì tạo nhiều tài liệu cũ/trùng lặp, làm tăng thời gian đọc mà không ưu tiên novelty.

### Chỉ chấp nhận bài trong năm hiện tại, không ngoại lệ

Loại vì có thể bỏ mất provenance của theory, scale và công thức; khiến phần lập luận học thuật dựa vào trích dẫn thứ cấp thay vì nguồn gốc.

---

## 4. Hệ quả (Consequences)

- Survey Round 2 trở đi tập trung vào công bố mới nhất và online-first.
- Tài liệu trước cửa sổ chỉ được đọc theo citation chain có lý do, không qua broad search.
- Endpoint và ba cụm tài liệu của `RDR-0001` vẫn giữ nguyên.
- Nếu xung đột về chiến lược tìm kiếm, `RDR-0002` được ưu tiên.
- Quyết định chốt theory, discrepancy measure và pipeline sau endpoint sẽ dùng số hiệu `RDR-0003`.
