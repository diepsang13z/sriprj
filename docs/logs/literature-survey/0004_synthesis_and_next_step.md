# Literature Survey Synthesis and Next-Step Gate

- **Ngày tổng kết:** 2026-09-20
- **Phạm vi:** Tổng hợp [`0001_discrepancy_formulations.md`](0001_discrepancy_formulations.md), [`0002_survey_matrix_round_1.md`](0002_survey_matrix_round_1.md) và [`0003_survey_matrix_round_2.md`](0003_survey_matrix_round_2.md).
- **Corpus làm việc:** 15 core papers ngoài paper gốc sau curation; 3 technical-watchlist papers; ba cụm `Review Inconsistency`, `Hospitality ABSA/Rating`, `Forgiveness/Buffering`.
- **Trạng thái:** Đủ theory, operationalization candidates và baselines để chuyển sang validation; **chưa đạt endpoint chính thức** của `RDR-0001` vì chưa chứng minh saturation và chưa chốt measure trên dữ liệu dự án.

---

## 1. Những gì đã khảo sát được

### 1.1. Hiện tượng cần nghiên cứu là có thật và không nên xử lý như noise

- Rating và text sentiment là hai tín hiệu liên quan nhưng không đồng nhất. Dùng rating làm ground-truth sentiment mà không kiểm tra agreement sẽ tạo weak-label noise ([Almansour et al., 2022](https://doi.org/10.1186/s43093-022-00114-y); [Abaiyan et al., 2026](https://arxiv.org/abs/2606.25518)).
- Trong tourism/hospitality, bất nhất có thể tồn tại như một minority subset nhưng vẫn mang ý nghĩa hành vi và quản trị. Wang et al. đo nhóm high-rating/low-sentiment ở cấp hotel; Abaiyan et al. báo cáo 18.6% review incongruent với sáu directional patterns ([Wang et al., 2025](https://doi.org/10.1016/j.ijhm.2025.104271); [Abaiyan et al., 2026](https://arxiv.org/abs/2606.25518)).
- Positive và negative aspects có thể đồng tồn tại và bù trừ nhau; mixed review không tự động đồng nghĩa với inconsistency ([Bigne et al., 2023](https://doi.org/10.1007/s11628-023-00524-0); [Öztürk, 2026](https://doi.org/10.1109/access.2026.3672490)).
- Vì vậy, việc một review 5 sao chứa negative span chỉ là **candidate inconsistency**. Cần phân biệt lỗi thực sự, phàn nàn nhỏ đã được service recovery, mixed experience, negation/sarcasm và lỗi gán nhãn.

### 1.2. Measurement nên giữ đồng thời magnitude và direction

Ba lớp đo đã có bằng chứng hoặc hỗ trợ trực tiếp:

1. **Directional categorical mismatch**
   - Đưa rating và text sentiment về cùng hệ polarity, sau đó giữ các hướng `high-rating/negative-text` và `low-rating/positive-text` riêng biệt ([Wang et al., 2025](https://doi.org/10.1016/j.ijhm.2025.104271); [Abaiyan et al., 2026](https://arxiv.org/abs/2606.25518)).
   - Ưu điểm: trực quan, dễ kiểm tra thủ công; nhược điểm: mất cường độ.

2. **Continuous magnitude**
   - Kwon et al. chuẩn hóa rating và sentiment trong cùng product rồi tính:

     $$D_i^{abs}=\left|z(r_i)-z(s_i)\right|$$

   - Họ tách magnitude khỏi direction thay vì coi hai khái niệm là một ([Kwon et al., 2025](https://doi.org/10.14329/apjis.2025.35.1.49)).

3. **Aspect-level conflict**
   - SentimentLens so sánh normalized overall rating với category sentiment:

     $$C=\{(h,a): |R_{norm}-S_a|>\tau\}$$

   - Đây là operationalization hospitality gần bài toán nhất, nhưng trị tuyệt đối làm mất direction và paper không báo cáo đủ quy trình chọn $\tau$ để tái lập ([Jayakody et al., 2026](https://arxiv.org/abs/2606.00084)).

4. **Unified geometric index**
   - Valdivia et al. (2019) gộp rating và text sentiment qua trung bình nhân có trọng số:

     $$f(x, y) = \sqrt{x \cdot y^\beta}$$

   - Trong đó $x, y \in [0, 1]$ là user rating và SAM sentiment đã min–max chuẩn hóa; $\beta > 0$ điều tiết trọng số text. Điểm đặc trưng của trung bình nhân là kéo chỉ số về 0 nếu một trong hai phía cực thấp, trừng phạt mạnh review có một vế sụp đổ.

**Candidate extension của dự án:** giữ dấu ở cấp aspect:

$$D_{i,a}^{signed}=r_i^*-s_{i,a}^*$$

- $D_{i,a}^{signed}>0$: rating cao hơn tín hiệu text/aspect — candidate buffering/forgiveness.
- $D_{i,a}^{signed}<0$: rating thấp hơn tín hiệu text/aspect — candidate punitive/anger response.
- Đây là đề xuất của dự án, **không được mô tả là công thức chuẩn từ literature**.

### 1.3. Theory phải tách actor và outcome

| Tầng giải thích                     | Theory/construct phù hợp                                       | Điều giải thích được                                                       | Không được suy diễn                                        |
| ----------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Reviewer đánh giá trải nghiệm       | S-O-R, Justice Theory, Expectancy–Disconfirmation, Attribution | Service failure/recovery → empathy/forgiveness/dissatisfaction             | Chưa chứng minh trực tiếp tác động lên star rating thực tế |
| Trade-off giữa service aspects      | Compensatory Choice Models; multi-aspect rules                 | Positive và negative aspects có thể bù trừ khi hình thành overall judgment | Không tự động chứng minh “loyalty” hay “sublimation”       |
| Người đọc tiếp nhận review bất nhất | HSM, Schema Incongruity, Curiosity Theory                      | Inconsistency ảnh hưởng helpfulness, attention và information processing   | Không giải thích trực tiếp tại sao reviewer chọn mức sao   |

Bằng chứng mới nhất cho forgiveness vẫn dừng ở forgiveness, repatronage, service-recovery expectation hoặc dissatisfaction; chưa có đường kiểm định trực tiếp `Forgiveness/Anger → observed star rating` trong hotel-review data ([Kumar & Shankar, 2024](https://doi.org/10.1177/14413582231194071); [Honora et al., 2024](https://doi.org/10.1007/s11628-024-00563-1); [Huang & Lo, 2025](https://doi.org/10.1007/s40558-025-00314-6); [Wei et al., 2025](https://doi.org/10.1002/jtr.70154)).

### 1.4. Baseline kỹ thuật đã đủ để validation, chưa đủ để chốt pipeline

- **Baseline tái lập:** `BERTopic + VADER + WMLR` của [paper gốc](../../../refs/root/factsheet.md).
- **Aspect-level benchmark:** HOSSemEval-EB23/TAS-BERT cung cấp điểm quy chiếu cho hospitality ABSA ([Doan et al., 2025](https://doi.org/10.1007/s11042-024-19518-9)).
- **Interpretable rating driver:** high-utility aspect rules của Öztürk mô tả co-occurrence và trade-off giữa aspects ([Öztürk, 2026](https://doi.org/10.1109/access.2026.3672490)).
- **Rating-prediction watchlist:** DeBERTa + random oversampling của Topçu et al. là baseline dự đoán rating, nhưng không được dùng làm sentiment estimator độc lập vì rating là training label ([Topçu et al., 2026](https://doi.org/10.35377/saucis...1748175)).

Không nên so sánh trực tiếp accuracy/F1 giữa các paper vì khác label space, split, dataset và nhiệm vụ.

---

## 2. Điều đã chốt và điều còn mở

### 2.1. Có thể chốt ở mức literature

1. Không dùng rating làm nhãn sentiment mặc định.
2. Measurement chính phải giữ **direction**; magnitude là biến bổ sung, không thay thế direction.
3. Aspect-level analysis cần thiết để phân biệt lỗi nào được bỏ qua và lỗi nào dẫn đến punitive rating.
4. `Aspect` và `Emotion/Intent` là hai trục khác nhau; không đưa `Anger` hoặc `Sublimation` thành service aspect.
5. Broad search nên dừng tạm thời: core set đã chạm 15 và việc đọc thêm không giải quyết được lựa chọn estimator/normalization/threshold.

### 2.2. Chưa được chốt

1. Sentiment estimator nào đủ tin cậy trên `TripAdvisor_EN.json`.
2. Chuẩn hóa rating–sentiment bằng z-score, min–max hay calibrated probability.
3. Threshold nào phân biệt aligned, mixed và truly inconsistent review.
4. Cách tổng hợp nhiều aspect sentiments thành document-level expectation.
5. `Sublimation` và `Anger` có construct validity hay chỉ là working labels; literature hiện hỗ trợ forgiveness, empathy, negative emotion và compensatory behavior gần hơn các nhãn này.
6. Chi tiết đo lường của Wang et al. (2025, DSS) chưa lấy được từ full text (Elsevier paywall); riêng công thức unified index của Valdivia et al. (2019) **đã được trích xuất và xác minh trực tiếp từ PDF toàn văn** ($f(x,y)=\sqrt{x \cdot y^\beta}$).
7. Hai nguồn 2026 trực tiếp nhất cho directional typology và aspect conflict vẫn là preprints.

---

## 3. Next Step đề xuất: Targeted Discrepancy Validation

**Không mở Survey Round 3 ngay.** Bước kế tiếp là một validation study nhỏ trên dữ liệu dự án để chọn measure trước khi ban hành `RDR-0003`.

### Gate A — Tạo evaluation set có đối chứng

1. Bắt đầu từ **402 review 5 sao có negative span** trong `data/TripAdvisor_EN.json`.
2. Tạo mirror subset `1–2 sao + positive span`; nếu không có đủ mẫu, báo đúng prevalence thay vì cân bằng nhân tạo.
3. Thêm aligned controls từ hai phía rating để đo false-positive rate.
4. Gắn nhãn thủ công tối thiểu:
   - `aligned`, `mixed-but-consistent`, `true-high-rating/negative-text`, `true-low-rating/positive-text`, `annotation/context error`;
   - aspect gây lệch;
   - severity;
   - có/không service recovery, negation hoặc sarcasm.
5. Hai người gán nhãn độc lập một calibration subset, đo inter-rater agreement và adjudicate disagreement trước khi mở rộng.

**Rủi ro cần chặn:** 402 mẫu chỉ kiểm tra được chiều high-rating/negative-text; không đủ để kết luận về punitive/anger direction nếu thiếu mirror subset.

### Gate B — So sánh ba formulation tối thiểu

| Candidate                           | Output                    | Vai trò                            |
| ----------------------------------- | ------------------------- | ---------------------------------- |
| 3×3 directional polarity matrix     | Class                     | Baseline dễ giải thích             |
| Signed standardized gap `z(r)-z(s)` | Sign + magnitude          | Kiểm tra extension từ Kwon         |
| Signed aspect gap `r^*-s_a^*`       | Aspect vector + aggregate | Candidate measure chính của đề tài |

Residual `rating - predicted_rating_text` chỉ nên dùng như sensitivity analysis. Embedding distance và entropy chưa cần triển khai trừ khi ba formulation trên thất bại.

### Gate C — Quy tắc chọn measure

Chọn formulation chính khi nó đồng thời:

1. Khớp tốt nhất với human direction labels, báo cáo macro-F1/confusion matrix thay vì accuracy đơn lẻ.
2. Giữ được dấu và phân biệt hai hướng inconsistency.
3. Ổn định giữa high-rating và low-rating strata, không chỉ hoạt động trên 402 mẫu 5 sao.
4. Giải thích được ở cấp aspect và không dùng rating để huấn luyện sentiment estimator.
5. Không phụ thuộc vào explicit star mentions/`Branding` text gây data leakage.

Nếu không formulation nào đạt các điều kiện trên, giữ directional matrix làm baseline, không ban hành `RDR-0003`, và chỉ mở citation-chain search nhắm đúng failure đã quan sát.

### Gate D — Sản phẩm sau validation

1. Nhật ký protocol/results tiếp theo trong `docs/logs/literature-survey/` hoặc thư mục experiment hiện hữu khi được xác định.
2. `RDR-0003` chốt theory, estimator, normalization, discrepancy measure, threshold và validation evidence.
3. Research Proposal dùng gap đã xác nhận: aspect-level signed discrepancy và quan hệ giữa buffering/punitive emotional mechanisms với observed rating behavior.

---

## 4. Quyết định vận hành

- **Hiện tại:** literature phase đủ để thiết kế validation, nhưng chưa đủ để tuyên bố measure cuối cùng.
- **Next action duy nhất:** audit schema và dựng evaluation set hai chiều từ `TripAdvisor_EN.json`.
- **Round 3 chỉ mở khi:** validation thất bại vì thiếu measure phù hợp, có citation mới trực tiếp từ core papers, hoặc cần xác minh một construct cụ thể.
- **Không làm tiếp lúc này:** tải thêm paper chung chung, triển khai nhiều model đồng thời, hay viết Proposal trước khi chốt operationalization.
