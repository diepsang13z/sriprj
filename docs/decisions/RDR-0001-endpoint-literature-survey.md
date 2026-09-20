# RDR-0001: Literature Survey Objectives & Stopping Criteria (Endpoint)

* **Trạng thái:** ACCEPTED
* **Ngày quyết định:** 2026-09-20
* **Người đề xuất:** Nghiên cứu viên / Agent
* **Phạm vi áp dụng:** Toàn bộ hoạt động khảo sát tài liệu trong giai đoạn Exploratory

---

## 1. Bối cảnh (Context)

Giai đoạn khảo sát văn hiến (Literature Survey) dễ rơi vào bẫy thu thập tài liệu tràn lan, mất định hướng và không phục vụ trực tiếp cho việc ra quyết định học thuật. Cần thiết lập một quyết định kiến trúc xác định rõ:
1. Khảo sát tài liệu nhằm chốt các thành phần cụ thể nào.
2. Tiêu chí định lượng và định tính để dừng khảo sát (Stopping Criteria / Endpoint), chuyển sang giai đoạn thực nghiệm và viết Research Proposal.

---

## 2. Quyết định (Decision)

### 2.1. Bốn mục tiêu khảo sát bắt buộc phải chốt (Objectives)

Khảo sát văn hiến chỉ hợp lệ khi phục vụ chốt 4 thành phần sau:

1. **Khung lý thuyết nền (Theoretical Framework):**
   * Xác định lý thuyết hành vi giải thích cơ chế mâu thuẫn cảm xúc - điểm số (*Sentiment–Rating Inconsistency*) và hiệu ứng "tấm đệm" (*Buffering Effect*).
   * Ứng viên ưu tiên đối chiếu: **S-O-R** (Stimulus–Organism–Response), **Expectancy–Disconfirmation Theory (EDT)**, và **Herzberg’s Two-Factor Theory**.

2. **Cách lượng hóa độ bất nhất (Operationalizing Discrepancy):**
   * Chốt công thức hoặc chỉ số toán học/kinh tế lượng đo lường độ lệch giữa văn bản và điểm sao:
     * Phần dư mô hình: $\text{Discrepancy} = \text{Rating} - \widehat{\text{Rating}}_{\text{text}}$.
     * Hoặc ma trận phân cực (Polarity Discrepancy Matrix: Positive text vs. Low rating; Negative text vs. High rating).

3. **Baseline & Phương pháp luận thực nghiệm (Methodology Benchmark):**
   * Xác định mô hình khai phá khía cạnh cảm xúc (ABSA: BERTopic + VADER vs. Pre-trained LM / LLM few-shot).
   * Xác định mô hình kinh tế lượng kiểm định tác động điều tiết (Moderated WMLR, Ordered Logit/Probit).

4. **Lập luận đóng góp nghiên cứu (Research Gap & Contribution):**
   * Khẳng định tính mới so với paper gốc (Le et al., IJHM 2026): Khắc phục lỗi lập luận vòng (Tautology) của biến Loyalty bằng cách chuyển sang giải thích hiện tượng mâu thuẫn điểm số ở cấp độ khía cạnh (Aspect-level Discrepancy).

---

### 2.2. Tiêu chí dừng khảo sát (Stopping Criteria / Endpoint)

Hoạt động khảo sát dừng lại khi thỏa mãn đồng thời 4 điều kiện sau:

| STT | Tiêu chí | Ngưỡng dừng (Endpoint) | Dấu hiệu vi phạm (Over-engineering) |
| :--- | :--- | :--- | :--- |
| 1 | **Bão hòa lý thuyết & phương pháp** | Đọc 3–5 bài mới liên tiếp không xuất hiện thêm khung lý thuyết hoặc công thức đo Discrepancy mới. | Tiếp tục tải thêm bài chỉ để đọc abstract mà không thu được biến số mới. |
| 2 | **Quy mô tập tài liệu hạt nhân** | Đạt **10 – 15 bài báo trọng tâm** chia đều 3 cụm: (a) *Review Inconsistency*, (b) *Hospitality ABSA*, (c) *Customer Forgiveness/Buffering*. | Danh mục vượt quá 25 bài nhưng không phân loại được đóng góp cụ thể. |
| 3 | **Đủ nguyên liệu Proposal** | Trả lời được 3 câu hỏi: (1) Ai làm gần nhất? (2) Hạn chế của họ là gì? (3) Ta đo lường và kiểm định khác họ ở điểm nào? | Chưa xác định được biến phụ thuộc / biến điều tiết sau khi đọc xong. |
| 4 | **Xác định $\ge 1$ Baseline đối chứng** | Có tối thiểu 1 paper công bố kết quả/dữ liệu tương đồng để so sánh đối chuẩn hiệu năng. | Mô hình xây xong không có điểm quy chiếu đánh giá. |

---

## 3. Sản phẩm bàn giao (Deliverables & Artifacts)

Khi đạt điểm dừng, kết quả khảo sát phải được đóng gói thành các tài liệu:
1. **Synthesis Matrix:** Bảng tổng hợp các bài báo tại `docs/logs/literature-survey/0001_survey_matrix.md`.
2. **Cập nhật thư viện:** Đăng ký các paper hạt nhân vào `refs/INDEX.md` kèm tóm tắt ngắn.
3. **Chuyển tiếp giai đoạn:** Soạn thảo Research Proposal draft tại `reports/md/` và ban hành `RDR-0002` chốt pipeline thực nghiệm.

---

## 4. Hệ quả & Giới hạn (Consequences)

* **Tích cực:** Ngăn chặn đọc lan man; ràng buộc mọi hoạt động đọc tài liệu phải hướng đến công thức và biến số thực nghiệm cụ thể.
* **Kỷ luật:** Mọi paper mới được đề xuất đọc thêm sau khi đạt Endpoint phải có lý do ngoại lệ được ghi nhận vào nhật ký.
