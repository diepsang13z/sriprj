# RDR-0006: Đóng băng định nghĩa "ca bất nhất" cấp review

- **Trạng thái:** ACCEPTED
- **Ngày quyết định:** 2026-09-23
- **Người đề xuất:** Nghiên cứu viên
- **Phạm vi áp dụng:** Cách đếm ca bất nhất cho RQ1 và cách chọn mẫu cho evaluation set
- **Căn cứ:** `RDR-0005` (phạm vi 9.990 review), [`docs/logs/validation/0001_manual_annotation_protocol.md`](../logs/validation/0001_manual_annotation_protocol.md), Phụ lục A mục 10 của [`reports/md/research_proposal.md`](../../reports/md/research_proposal.md)

---

## 1. Bối cảnh (Context)

Con số mở đầu của đề tài — *bao nhiêu review cho điểm cao nhưng văn bản có phàn nàn* — tồn tại ở hai phiên bản không khớp nhau: toàn bộ `docs/` ghi **402**, toàn bộ `reports/` ghi **404**. Phụ lục A mục 10 của proposal đã ghi nợ việc chốt định nghĩa và sửa lại tài liệu.

Đo lại trực tiếp trên `data/TripAdvisor_EN.json` (9.990 bản ghi) cho thấy ba định nghĩa khả dĩ ứng với ba con số khác nhau, và **`402` không khớp định nghĩa nào** — không tái lập được, không dùng được.

**Nguyên nhân gốc, ghi lại để không lặp:** trước quyết định này **chưa từng có định nghĩa nào được đóng băng**. Con số vì thế được chép tay qua các vòng khảo sát và tài liệu mà không ai kiểm được nó tính từ tiêu chí gì — hai phe tài liệu lệch nhau là hệ quả, không phải một lỗi đánh máy. Đây là lỗi quá trình, không phải lỗi số.

Hai quy ước đếm áp dụng cho mọi phép tính ở đây:

- **Đơn vị đếm là review**, không phải span. Một review có nhiều span tiêu cực vẫn chỉ tính một ca.
- **Chỉ dùng `annotations`**, bỏ `drafts` và `predictions` (theo quy chuẩn chống rò rỉ đã ghi ở `docs/logs/brainstorm/0003_app_concept_and_course_requirements.md`).

---

## 2. Quyết định (Decision)

### 2.1. Định nghĩa đóng băng

> **Ca bất nhất chiều high-rating / negative-text** = review có `data.meta_info.score == 5` và có **ít nhất một** span `entity_sentiment` nhãn `Negative` mà span cùng `id` bên `entities` **không** mang nhãn `Branding`.

Kết quả: **394 ca** trên 7.148 review 5★ — tỷ lệ **5,5%**.

### 2.2. Thang tham chiếu (giữ để đối chiếu, không dùng làm số chính)

| Định nghĩa | Số ca |
| --- | ---: |
| Bất kỳ span `Negative` nào | 404 |
| **Loại span gắn `Branding` — CHỐT** | **394** |
| Chỉ tính khía cạnh lõi (loại thêm `Loyalty`) | 392 |

### 2.3. Chiều gương

Review có `score ≤ 2` và có ít nhất một span `Positive` (không lọc theo `Branding` vì nhãn này không áp cho chiều này): **199 ca** trên 465 review 1–2★ — tỷ lệ **42,8%**.

### 2.4. Phép đếm lại

Ba điều kiện, đủ để kiểm tra độc lập:

```
score == '5.0'
span together: from_name = 'entity_sentiment', labels chứa 'Negative', id = X
span together: from_name = 'entities',         id = X, labels ∩ {Facility, Amenity, Service, Experience} ∪ {Loyalty} ≠ ∅
```

Nói cách khác: loại đúng lớp `Branding`, giữ mọi khía cạnh còn lại.

---

## 3. Hệ quả (Consequences)

1. **`402` bị khai tử.** 9 tệp `docs/` và 3 tệp `reports/` đã sửa sang `394`; Phụ lục A mục 10 của proposal chuyển sang trạng thái đã chốt.
2. **Số dẫn xuất đổi theo**, vì chúng đều tính từ con số gốc:

| Số dẫn xuất | Cũ (theo 404) | Mới (theo 394) |
| --- | ---: | ---: |
| Tổng ca đáng ngờ | 603 | **593** |
| Khách sạn trải ca đáng ngờ | 468 | **461** |
| Đối chứng 5★ (không có span tiêu cực) | 6.744 | **6.754** |
| Ca trong khách sạn ≥20 review | 130, tại 58 khách sạn | **129, tại 57 khách sạn** |

3. **Evaluation set lấy từ 394 + 199 ca** cộng aligned controls, theo `docs/logs/validation/0001_manual_annotation_protocol.md`.
4. **Hai chiều lệch nhau rất xa (5,5% so với 42,8%) và giữ nguyên hiện trạng** — không cân bằng nhân tạo, báo đúng tỷ lệ thật.

---

## 4. Phương án đã loại (Rejected Alternatives)

### Giữ span `Branding` (404 ca)

`Branding` là lớp span khách **tự đọc điểm sao bằng lời** (*"give 5 star"*) hoặc so sánh ảnh với thực tế. Nhóm đã loại lớp này khỏi mọi đặc trưng dự đoán vì rò rỉ nhãn; đếm nó là "phàn nàn" là sai phạm trù. Loại đúng **10 ca** chỉ có span tiêu cực thuộc lớp này.

### Loại thêm `Loyalty` (392 ca)

`"never again"`, `"stay away"` đúng là biểu đạt tiêu cực trong văn bản, khác bản chất với việc dùng chúng làm biến dự đoán điểm số. Việc loại `Loyalty` khỏi **đặc trưng mô hình** vì nguy cơ lập luận vòng không kéo theo việc loại nó khỏi **phép đếm hiện tượng**. Giữ lại **2 ca**.

---

## 5. Không nằm trong quyết định này

- Công thức đo discrepancy, cách chuẩn hóa và ngưỡng phân loại — vẫn chờ validation study.
- Câu chữ chính thức của RQ1 và RQ2 (vẫn ở dạng nháp).
- Định nghĩa "span tiêu cực" ở cấp khía cạnh cho các mô hình về sau.

---

## 6. Đọc thêm

- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../logs/validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và quy chuẩn gán nhãn.
- [`docs/logs/brainstorm/0001_root_idea.md`](../logs/brainstorm/0001_root_idea.md) — phân tích bài gốc và hướng bất nhất.
- [`reports/md/research_proposal.md`](../../reports/md/research_proposal.md) — Phụ lục A, mục 10.
