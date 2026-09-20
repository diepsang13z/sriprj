# Đánh giá & Phân loại các Phương pháp Lượng hóa Độ bất nhất (Sentiment–Rating Discrepancy)

* **Ngày tạo:** 2026-09-20
* **Mục đích:** Ghi nhận nguồn gốc học thuật, phân tích ưu nhược điểm của các phương pháp đo lường mâu thuẫn điểm số - bài viết, phục vụ định hướng khảo sát văn hiến trước khi chốt `RDR-0002`.

---

## 1. Vấn đề cốt lõi: Tại sao phải khảo sát nhiều công thức?

Trong các nghiên cứu về đánh giá trực tuyến (Online Customer Reviews), hiện tượng mâu thuẫn giữa cảm xúc trong bài viết và điểm sao thực tế (*Sentiment–Rating Inconsistency / Discrepancy / Incongruence*) được tiếp cận theo nhiều góc nhìn khác nhau.

Nếu chỉ giới hạn ở 1–2 công thức cố định, nghiên cứu sẽ đối mặt với rủi ro:
1. Không bắt kịp các kỹ thuật NLP/Deep Learning mới giai đoạn 2022–2026.
2. Bỏ sót cơ chế giải thích ở cấp độ từng khía cạnh (*Aspect-level Discrepancy*).
3. Thiếu tính tương thích với bài toán kinh tế lượng khi mô hình hóa hành vi.

> **Nguyên tắc khảo sát mở (Open Space Principle):** Danh mục dưới đây là các họ phương pháp tham khảo đã được ghi nhận trước đó, **không phải là danh sách đóng**. Đợt khảo sát văn hiến chủ động tìm kiếm các công thức/phương pháp mới xuất hiện trong các bài báo 2023–2026.

---

## 2. Bản đồ các họ phương pháp (Taxonomy of Discrepancy Formulations)

### Nhóm 1: Kinh tế lượng — Khoảng cách Phần dư (Residual-based Discrepancy)
* **Ý tưởng:** Dùng cảm xúc các khía cạnh dự đoán điểm số kỳ vọng qua hồi quy:
  $$\widehat{\text{Rating}}_i = \beta_0 + \sum_{k=1}^K \beta_k \cdot \text{Sentiment}_{ik}$$
  Độ bất nhất được tính bằng phần dư:
  $$e_i = \text{Rating}_i - \widehat{\text{Rating}}_i$$
* **Ý nghĩa hành vi:**
  * $e_i > 0$: Điểm thực tế cao hơn văn bản $\rightarrow$ Xu hướng vị tha, nâng đỡ (*Buffering effect / Sublimation*).
  * $e_i < 0$: Điểm thực tế thấp hơn văn bản $\rightarrow$ Xu hướng trừng phạt (*Punitive rating / Outrage*).
* **Ưu điểm:** Kế thừa trực tiếp cấu trúc mô hình WMLR từ bài báo gốc (Le et al., 2026); dễ kiểm định kinh tế lượng.
* **Nhược điểm:** Phụ thuộc vào chất lượng của mô hình hồi quy nền; giả định mối quan hệ tuyến tính/đơn điệu.

### Nhóm 2: Khai phá dữ liệu — Ma trận phân cực (Polarity Discrepancy Matrix)
* **Ý tưởng:** Rời rạc hóa bài viết và điểm số thành ma trận $2 \times 2$ hoặc $3 \times 3$:
  * Trục Text: Tích cực ($\ge 0$) vs. Tiêu cực ($< 0$).
  * Trục Rating: Cao (4–5 sao) vs. Thấp (1–2 sao).
* **Ứng dụng thực tế:** Nhóm đã phát hiện **402 mẫu 5-sao có chứa phàn nàn tiêu cực** trong dataset `TripAdvisor_EN.json` — đây là đại diện trực tiếp cho ô *Negative Text – High Rating*.
* **Ưu điểm:** Trực quan, dễ giải thích, không phụ thuộc vào tham số mô hình hóa phức tạp.
* **Nhược điểm:** Mất thông tin cường độ cảm xúc do việc phân nhóm nhị phân/tam phân.

### Nhóm 3: NLP & Không gian Vector — Khoảng cách Embedding (Embedding/Semantic Distance)
* **Ý tưởng:** Mã hóa văn bản bài review qua Transformer (SBERT, RoBERTa) thành vector $\mathbf{v}_{\text{text}}$, so sánh với các vector chuẩn (anchor vector) đại diện cho các mức điểm 1 sao / 5 sao bằng Cosine Similarity hoặc Euclidean Distance.
* **Ưu điểm:** Bắt được ngữ nghĩa sâu, xử lý tốt sắc thái mỉa mai (sarcasm) hoặc từ ngữ giảm nhẹ mà từ điển VADER bỏ sót.
* **Nhược điểm:** Khó diễn giải hệ số khi đưa vào các mô hình kinh tế lượng truyền thống.

### Nhóm 4: Tâm lý học hành vi — Mâu thuẫn thái độ & Entropy (Attitudinal Ambivalence / Entropy)
* **Ý tưởng:** Sử dụng các công thức đo lường mâu thuẫn nội tại (ví dụ: Griffin formula $\text{Ambivalence} = P + N - |P - N|$ với $P, N$ là cường độ tích cực và tiêu cực) hoặc Entropy thông tin để đo mức độ xung đột trong chính bài viết trước khi so với Rating.
* **Ưu điểm:** Phù hợp với lý thuyết tâm lý học về sự lưỡng lự (Cognitive Dissonance).
* **Nhược điểm:** Đo mâu thuẫn nội tại trong lời nói nhiều hơn là mâu thuẫn giữa lời nói và hành vi chấm sao.

### Nhóm 5: Khía cạnh sâu — Vector độ lệch theo khía cạnh (Aspect-Weighted Discrepancy Vector)
* **Ý tưởng:** Thay vì 1 chỉ số gộp, tính độ lệch riêng cho từng khía cạnh:
  $$\vec{D}_i = [d_{\text{facility}}, d_{\text{service}}, d_{\text{amenity}}, \dots]$$
* **Ưu điểm:** Trả lời trực diện câu hỏi nghiên cứu: *"Khách tha thứ cho lỗi ở khía cạnh nào và trừng phạt khía cạnh nào?"*
* **Nhược điểm:** Cần thuật toán ABSA gán nhãn chính xác ở cấp độ từng khía cạnh.

---

## 3. Câu hỏi định hướng khi đọc tài liệu (Literature Survey Checklist)

Khi đọc các bài báo mới (2022–2026), nghiên cứu viên cần trả lời các câu hỏi sau cho từng bài:
1. Bài báo đo lường mâu thuẫn cảm xúc - điểm số bằng công thức cụ thể nào?
2. Thuộc nhóm phương pháp nào trong 5 nhóm trên (hoặc là một họ hoàn toàn mới)?
3. Bộ dữ liệu áp dụng có phải là khách sạn/du lịch hay không?
4. Phương pháp đó có khả thi với dữ liệu `TripAdvisor_EN.json` hiện có không?
