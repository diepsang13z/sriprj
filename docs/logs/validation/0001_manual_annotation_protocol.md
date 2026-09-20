# Hướng dẫn Thiết kế Tập Đánh giá & Quy chuẩn Gán nhãn Thủ công (Manual Annotation Protocol)

* **Ngày tạo:** 2026-09-21
* **Mục đích:** Quy định chi tiết cấu trúc tập dữ liệu kiểm thử (Evaluation Set) và chuẩn hóa quy trình gán nhãn thủ công (Human-in-the-loop Ground Truth) để đo lường, đối soát các công thức phát hiện bất nhất cảm xúc - điểm số (Sentiment–Rating Inconsistency).

---

## 1. Mục đích & Bối cảnh

Trước khi ban hành Quyết định Kiến trúc `RDR-0003` để chốt công thức lượng hóa độ bất nhất, nhóm cần một tập dữ liệu chuẩn mực (Ground Truth) do con người trực tiếp thẩm định nhằm:
1. Đánh giá độ chính xác (Precision, Recall, Macro-F1) của các mô hình Sentiment Estimator (VADER, RoBERTa/DeBERTa, Aspect-based Sentiment).
2. Đo lường tỷ lệ báo động giả (False Positive Rate) trên các review bình thường (nhất quán).
3. So sánh hiệu năng của 3 nhóm công thức: **3×3 Polarity Matrix**, **Khoảng cách chuẩn hóa $z(r)-z(s)$**, và **Signed Aspect Gap ($r^* - s_a^*$)**.

---

## 2. Cấu trúc Tập Dữ liệu Đánh giá (Evaluation Dataset Design)

Tập đánh giá được trích xuất từ `data/TripAdvisor_EN.json` với quy mô khuyến nghị **600 – 800 mẫu**, bao gồm 3 nhóm thành phần:

1. **Nhóm Nghi ngờ Bất nhất Chiều 1 (Candidate High-Rating / Negative-Text):**
   * Toàn bộ **402 review 5 sao** có chứa span/từ khóa tiêu cực đã được bóc tách từ bước phân tích sơ bộ.
2. **Nhóm Nghi ngờ Bất nhất Chiều 2 (Mirror Subset: Low-Rating / Positive-Text):**
   * Các review **1–2 sao** nhưng có chứa span/từ khóa tích cực (khen ngợi).
   * Lấy theo tỷ lệ xuất hiện thực tế (prevalence), không tạo cân bằng nhân tạo nếu dữ liệu gốc phân bố lệch.
3. **Nhóm Đối chứng Nhất quán (Aligned Controls):**
   * Mẫu ngẫu nhiên từ hai phía:
     * Review 5 sao khen thuần túy (*Positive text + 5 stars*).
     * Review 1–2 sao chê thuần túy (*Negative text + 1–2 stars*).
   * **Vai trò:** Đo lường tỷ lệ thuật toán nhận diện nhầm review bình thường thành bất nhất (*False Positive Rate*).

---

## 3. Quy chuẩn Gán nhãn Chi tiết (Annotation Schema)

Mỗi mẫu review trong bảng tính Excel / Google Sheets sẽ được thẩm định độc lập theo 5 trường thông tin sau:

### Trường 1: `Inconsistency_Type` (Loại tương thích giữa chữ và sao)
* **Mục tiêu:** Xác định mối quan hệ tổng thể giữa cảm xúc bài viết và điểm sao.
* **Các nhãn quy ước:**
  * `aligned`: Chữ khen hết lời = 5 sao, hoặc chữ chê hết lời = 1–2 sao (hoàn toàn nhất quán).
  * `mixed-but-consistent`: Review có cả khen lẫn chê, và điểm sao phản ánh sự cân bằng hợp lý (ví dụ: 3 sao hoặc 4 sao).
  * `true-high-rating/negative-text`: **Bất nhất chiều 1** — Bài viết phàn nàn nặng hoặc toàn chê nhưng vẫn chấm 5 sao (biểu hiện của sự vị tha / nâng đỡ).
  * `true-low-rating/positive-text`: **Bất nhất chiều 2** — Bài viết khen ngợi hầu hết các mặt nhưng bị dìm xuống 1–2 sao (biểu hiện của sự phẫn nộ / trừng phạt).
  * `annotation_error`: Lỗi trích xuất (ví dụ: cụm từ bị tách sai ngữ cảnh như *"not bad"* bị máy gán là *"bad"*).

### Trường 2: `Target_Aspect` (Khía cạnh dịch vụ gây lệch)
* **Mục tiêu:** Xác định khía cạnh nào là nguyên nhân trọng tâm khiến khách bức xúc hoặc khen ngợi.
* **Các nhãn quy ước:**
  * `Facility`: Cơ sở vật chất (phòng ốc, giường, điều hòa, phòng tắm, cách âm, thang máy...).
  * `Service`: Thái độ, sự hỗ trợ, tốc độ phục vụ của nhân viên, lễ tân, quản lý.
  * `Amenity`: Tiện ích đi kèm (hồ bơi, wifi, đồ ăn sáng, bãi đỗ xe, phòng gym, spa...).
  * `Location`: Vị trí địa lý (trung tâm, gần biển, khoảng cách di chuyển, môi trường xung quanh).
  * `Price/Value`: Mức độ tương xứng giữa giá tiền bỏ ra và giá trị nhận lại.

### Trường 3: `Severity` (Mức độ nghiêm trọng của sự cố)
* **Mục tiêu:** Phân loại mức độ ảnh hưởng của lỗi dịch vụ được nhắc đến trong review.
* **Các nhãn quy ước:**
  * `Minor`: Lỗi nhỏ, không ảnh hưởng lớn đến toàn bộ kỳ nghỉ (đèn bàn hơi tối, nước chảy hơi yếu, wifi chậm một lúc).
  * `Major`: Lỗi nghiêm trọng làm hỏng trải nghiệm cốt lõi (mất điện/nước cả đêm, phòng bẩn thỉu, thái độ nhân viên thô lỗ, mất đồ, hủy phòng đột ngột).

### Trường 4: `Service_Recovery` (Khắc phục sự cố tại chỗ)
* **Mục tiêu:** Ghi nhận xem khách sạn có nhận biết lỗi và chủ động xử lý hay không.
* **Các nhãn quy ước:**
  * `Yes`: Có ghi nhận hành động xin lỗi, đổi phòng, nâng hạng phòng, hoàn tiền hoặc sửa chữa kịp thời từ phía khách sạn.
  * `No`: Không có hành động khắc phục, hoặc khách sạn phớt lờ phản ánh của khách.

### Trường 5: `Negation_or_Sarcasm` (Yếu tố ngữ nghĩa phức tạp)
* **Mục tiêu:** Đánh dấu các trường hợp dễ làm mô hình NLP đọc sai sắc thái cảm xúc.
* **Các nhãn quy ước:**
  * `None`: Diễn đạt trực diện, ngữ nghĩa bình thường.
  * `Negation`: Chứa cấu trúc phủ định (ví dụ: *"not disappointed at all"*, *"nothing to complain about"*).
  * `Sarcasm`: Chứa sắc thái châm biếm, mỉa mai (ví dụ: *"Cảm ơn vì đã tặng tôi một đêm mất ngủ tuyệt vời!"*).

---

## 4. Quy trình Phối hợp 2 Người Gán nhãn (Inter-rater Protocol)

Để đảm bảo tính khách quan và khoa học, quá trình gán nhãn tuân theo 3 giai đoạn:

```
[BƯỚC 1: CALIBRATION] 
2 người chấm thử độc lập 30-50 mẫu đầu tiên
         │
         ▼
[BƯỚC 2: TÍNH ĐỘ ĐỒNG THUẬN (INTER-RATER AGREEMENT)]
Đo chỉ số Cohen's Kappa / % trùng khớp nhãn
         │
         ├─── Nếu Kappa < 0.70 ───► Họp thảo luận (Adjudication) & Thống nhất lại quy chuẩn
         │
         └─── Nếu Kappa >= 0.70
                   │
                   ▼
[BƯỚC 3: MỞ RỘNG (FULL ANNOTATION)]
Chấm toàn bộ tập dữ liệu -> Họp giải quyết các mẫu bất đồng -> Chốt Ground Truth
```

1. **Hiệu chuẩn ban đầu (Calibration Phase):**
   * Hai người đọc kỹ tài liệu này, sau đó mở file riêng và gán nhãn độc lập **30 – 50 mẫu đầu tiên** (không trao đổi trong lúc làm).
2. **Đo độ đồng thuận & Hiệu chỉnh (Agreement & Adjudication):**
   * Dùng code tính hệ số **Cohen's Kappa** trên cột `Inconsistency_Type` và `Target_Aspect`.
   * Mục tiêu: Đạt $\text{Kappa} \ge 0.70$ (độ tin cậy tốt).
   * Nếu chưa đạt: Hai người ngồi lại xem xét các dòng chấm lệch nhau, phân tích nguyên nhân và cập nhật lại tiêu chuẩn gán nhãn.
3. **Gán nhãn toàn diện & Chốt Ground Truth (Full Annotation):**
   * Tiếp tục gán nhãn độc lập cho toàn bộ số mẫu còn lại.
   * Với những dòng hai người chấm khác nhau, tiến hành họp đối soát ngắn để thống nhất nhãn cuối cùng (Adjudicated Ground Truth).

---

## 5. Tiêu chí Đánh giá & Chốt Công thức Đo lường (Validation Metrics)

Tập Ground Truth hoàn tất sẽ được dùng để kiểm định các thuật toán theo các chỉ số:

* **Macro-F1 & Confusion Matrix:** Đo khả năng phân loại đúng các lớp bất nhất (`true-high-rating/negative-text` vs `true-low-rating/positive-text`).
* **False Positive Rate (FPR):** Đảm bảo thuật toán không báo động giả quá nhiều trên nhóm `aligned`.
* **Directional Stability:** Đảm bảo công thức phân biệt rõ ràng hai hướng bất nhất (Vị tha vs. Phẫn nộ) chứ không chỉ lấy trị tuyệt đối chung chung.
