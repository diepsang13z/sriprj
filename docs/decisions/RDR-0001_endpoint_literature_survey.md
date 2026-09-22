# RDR-0001: Literature Survey Objectives & Stopping Criteria (Endpoint)

- **Trạng thái:** ACCEPTED
- **Ngày quyết định:** 2026-09-20
- **Người đề xuất:** Nghiên cứu viên / Agent
- **Phạm vi áp dụng:** Toàn bộ hoạt động khảo sát tài liệu trong giai đoạn Exploratory

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
   * *Mục tiêu tối thiểu:* Xác định được **ít nhất 1 lý thuyết hành vi** giải thích thỏa đáng cơ chế mâu thuẫn cảm xúc - điểm số (*Sentiment–Rating Inconsistency*) và hiệu ứng "tấm đệm" (*Buffering Effect*).
   * *Điểm neo ban đầu (Baseline Anchors):* **S-O-R** (Stimulus–Organism–Response), **Expectancy–Disconfirmation Theory (EDT)**, và **Herzberg’s Two-Factor Theory**.
   * *Ghi chú mở rộng (Open Exploration):* Không giới hạn ở 3 điểm neo trên; chủ động ghi nhận các khung lý thuyết hành vi/tâm lý học khác (như *Cognitive Dissonance Theory*, *Attribution Theory*, *Justice Theory*...) nếu văn hiến chứng minh tính phù hợp cao hơn.

2. **Cách lượng hóa độ bất nhất (Operationalizing Discrepancy):**
   * *Mục tiêu tối thiểu:* Xác định được **ít nhất 1 công thức/chỉ số toán học hoặc NLP** khả thi trên tập dữ liệu của dự án, phản ánh được cả độ lớn (*magnitude*) và chiều hướng (*direction*: vị tha/nâng đỡ vs. trừng phạt/bực bội).
   * *Điểm neo ban đầu (Baseline Anchors):*
     * *Phần dư mô hình (Econometric Residual):* $\text{Discrepancy} = \text{Rating} - \widehat{\text{Rating}}_{\text{text}}$ (kế thừa từ hồi quy WMLR của paper gốc).
     * *Ma trận phân cực (Polarity Discrepancy Matrix):* Phân nhóm $2 \times 2$ (Positive Text $\times$ Low Rating; Negative Text $\times$ High Rating) như 402 mẫu 5-sao đã phát hiện.
   * *Ghi chú mở rộng (Open Exploration):* Chủ động rà soát các họ công thức mới (Embedding distance, Attitudinal Ambivalence/Entropy, Aspect-Weighted Discrepancy Vector, Wasserstein distance...) và tuyển chọn dựa trên 3 tiêu chí: *Tính diễn giải hành vi*, *Độ chi tiết cấp khía cạnh*, và *Tính khả thi thực nghiệm*.

3. **Baseline & Phương pháp luận thực nghiệm (Methodology Benchmark):**
   * *Mục tiêu tối thiểu:* Xác định được **ít nhất 1 baseline kỹ thuật hoàn chỉnh** để đối chuẩn trực tiếp hiệu năng trích xuất khía cạnh và mô hình hóa tác động.
   * *Điểm neo ban đầu (Baseline Anchors):* Pipeline của bài báo gốc (Le et al., 2026): **BERTopic + VADER + WMLR**.
   * *Ghi chú mở rộng (Open Exploration):* Chủ động đối sánh với các kỹ thuật ABSA tiên tiến (DeBERTa, RoBERTa ABSA, LLM few-shot) và các mô hình kinh tế lượng phân loại thứ bậc (Ordered Logit/Probit) để chọn ra kiến trúc vượt trội cho `RDR-0002`.

4. **Lập luận đóng góp nghiên cứu (Research Gap & Contribution):**
   * Khẳng định tính mới so với paper gốc (Le et al., IJHM 2026): Khắc phục lỗi lập luận vòng (Tautology) của biến Loyalty bằng cách chuyển sang giải thích hiện tượng mâu thuẫn điểm số ở cấp độ khía cạnh (Aspect-level Discrepancy).
---

### 2.2. Tiêu chí dừng khảo sát (Stopping Criteria / Endpoint)

Hoạt động khảo sát dừng lại khi thỏa mãn đồng thời 4 điều kiện sau:

| STT | Tiêu chí                                | Ngưỡng dừng (Endpoint)                                                                                                                      | Dấu hiệu vi phạm (Over-engineering)                                      |
| :-- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------- |
| 1   | **Bão hòa lý thuyết & phương pháp**     | Đọc 3–5 bài mới liên tiếp không xuất hiện thêm khung lý thuyết hoặc công thức đo Discrepancy mới.                                           | Tiếp tục tải thêm bài chỉ để đọc abstract mà không thu được biến số mới. |
| 2   | **Quy mô tập tài liệu hạt nhân**        | Đạt **10 – 15 bài báo trọng tâm** chia đều 3 cụm: (a) _Review Inconsistency_, (b) _Hospitality ABSA_, (c) _Customer Forgiveness/Buffering_. | Danh mục vượt quá 25 bài nhưng không phân loại được đóng góp cụ thể.     |
| 3   | **Đủ nguyên liệu Proposal**             | Trả lời được 3 câu hỏi: (1) Ai làm gần nhất? (2) Hạn chế của họ là gì? (3) Ta đo lường và kiểm định khác họ ở điểm nào?                     | Chưa xác định được biến phụ thuộc / biến điều tiết sau khi đọc xong.     |
| 4   | **Xác định $\ge 1$ Baseline đối chứng** | Có tối thiểu 1 paper công bố kết quả/dữ liệu tương đồng để so sánh đối chuẩn hiệu năng.                                                     | Mô hình xây xong không có điểm quy chiếu đánh giá.                       |

---

## 3. Sản phẩm bàn giao (Deliverables & Artifacts)

Khi đạt điểm dừng, kết quả khảo sát phải được đóng gói thành các tài liệu:

1. **Synthesis Matrix:** Bảng tổng hợp các bài báo tại `docs/logs/literature_survey/id_survey_matrix.md`.
2. **Cập nhật thư viện:** Đăng ký các paper hạt nhân vào `refs/INDEX.md` kèm tóm tắt ngắn.
3. **Chuyển tiếp giai đoạn:** Soạn thảo Research Proposal draft tại `reports/md/` và ban hành `RDR-0002` chốt pipeline thực nghiệm.

---

## 4. Hệ quả & Giới hạn (Consequences)

- **Tích cực:** Ngăn chặn đọc lan man; ràng buộc mọi hoạt động đọc tài liệu phải hướng đến công thức và biến số thực nghiệm cụ thể.
- **Kỷ luật:** Mọi paper mới được đề xuất đọc thêm sau khi đạt Endpoint phải có lý do ngoại lệ được ghi nhận vào nhật ký.
