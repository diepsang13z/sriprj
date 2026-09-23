# Literature Survey — Round 2: Latest-First Operationalization Scan

- **Ngày khảo sát:** 2026-09-20
- **Cửa sổ chủ động:** 2023-09-20 đến 2026-09-20 theo `RDR-0002`
- **Chế độ:** Scoping literature review; không tuyên bố PRISMA/systematic review
- **Mục tiêu:** (1) tìm phép đo inconsistency mới và có thể tái lập, (2) cập nhật baseline hospitality ABSA/rating, (3) kiểm tra cơ chế forgiveness/justice/buffering gần với rating behavior.
- **Kết quả:** 6 nguồn được đề xuất vào core set, 3 nguồn giữ ở watchlist; endpoint vẫn **chưa đạt** vì chưa bão hòa và chưa có kiểm định trực tiếp `forgiveness → star rating`.

---

## 1. Search Protocol

### 1.1. Nguồn và truy vấn

- **Nguồn chính:** trang nhà xuất bản/DOI, Crossref, arXiv, IEEE Xplore, SpringerLink, Wiley, ACL Anthology và PDF chính thức của tạp chí.
- **Thứ tự:** newest-first; ưu tiên online-first date; English only.
- **Cụm inconsistency:** `rating-sentiment incongruence`, `score-textual inconsistency`, `text-rating discrepancy`, `hotel rating text mismatch`, `signed continuous discrepancy`.
- **Cụm hospitality NLP:** `hospitality ABSA 2025 2026`, `hotel review rating prediction transformer`, `aspect sentiment rating drivers`.
- **Cụm forgiveness/buffering:** `hospitality consumer forgiveness service recovery`, `OTA perceived justice forgiveness`, `negative emotional contagion forgiveness`, `hotel service failure forgiveness rating`.

### 1.2. Inclusion / Exclusion

**Include:** nằm trong cửa sổ 36 tháng; trả lời trực tiếp ít nhất một điểm neo; metadata chính thức xác minh được; ưu tiên hotel/tourism/OTA; preprint chỉ dùng khi công thức hoặc dữ liệu trực tiếp lấp khoảng trống và phải gắn nhãn rõ.

**Exclude khỏi core:** sentiment chung không có rating/aspect; rating prediction dùng rating làm label nhưng không đo discrepancy; domain quá xa hospitality; metadata không đủ; trùng đóng góp; nguồn cũ không thỏa ngoại lệ citation-chain.

### 1.3. Ngoại lệ và giới hạn truy xuất

- **Valdivia et al. (2019):** ngoại lệ citation-chain hợp lệ vì Kwon et al. (2025) trích trực tiếp. Tuy nhiên OpenAlex xác nhận không có bản OA và full text nhà xuất bản bị khóa; công thức unified index **chưa được trích trực tiếp**. Không gán công thức của nguồn khác cho Valdivia.
- **Wang et al. (2025, DSS):** DOI/metadata và kết luận cấp abstract/snippet được xác minh; full text bị chặn nên định nghĩa chi tiết `review inconsistency`/`rating inconsistency` vẫn chưa đủ bằng chứng để tái lập.
- **Preprints 2026:** Abaiyan et al. và Jayakody et al. được đọc toàn văn nhưng chưa peer review; chỉ dùng làm bằng chứng mới nổi, không làm nguồn duy nhất cho quyết định phương pháp.
- Không thấy cảnh báo retraction/correction trong metadata nhà xuất bản/Crossref tại ngày quét. Đây không phải kiểm tra PubPeer toàn diện.

---

## 2. Synthesis Matrix

> **Evidence level (adapted):** III = scenario/controlled experiment; IV = observational/secondary-data study; VI = computational benchmark/cross-sectional study. Mức này mô tả thiết kế, không phải điểm chất lượng tuyệt đối.

| ID | Nguồn | Cụm | Dữ liệu / thiết kế | Construct / theory | Operationalization / method | Giá trị cho đề tài | Quality / access |
|---|---|---|---|---|---|---|---|
| R2-I1 | Kwon, Lee, Min, Kwak, & Choi (2025). [DOI](https://doi.org/10.14329/apjis.2025.35.1.49) | Inconsistency | 41,258 Amazon reviews, 173 products; ZINB | Curiosity Theory; degree vs direction inconsistency | `Degree_j = \|z(rating_j)-z(sentiment_j)\|`; direction mismatch = positive text + 1–2 stars hoặc negative text + 4–5 stars | Phép đo magnitude liên tục đã xác minh và tách riêng direction; không phải hospitality | IV; peer-reviewed; full text |
| R2-I2 | Abaiyan et al. (2026). [arXiv](https://arxiv.org/abs/2606.25518) | Inconsistency | 16,156 Sri Lankan attraction reviews, 2010–2023; 1,000 nhãn tay; transformer + logit/RF/SHAP | Weak-label reliability; 6 directional patterns | Mismatch giữa 3-class text sentiment độc lập và rating class; 18.6% incongruent | Củng cố yêu cầu không dùng rating làm ground-truth sentiment; typology định hướng cho Sublimation/Anger | IV/VI; preprint; full text |
| R2-I3 | Jayakody, Thenahandi, & Jayarathna (2026). [arXiv](https://arxiv.org/abs/2606.00084) | Hospitality inconsistency | >10,000 hotel reviews; 100 hotels; 46,565 aspect mentions; Google Reviews + TripAdvisor | Cross-modal reconciliation | `C={(h,c): \|R_norm-S_a\|>τ}` với `τ` chọn thực nghiệm | Phép đo aspect-level gần nhất; giữ magnitude nhưng bỏ dấu; giá trị `τ` không được báo cáo đủ để tái lập | VI; preprint; full text |
| R2-M1 | Öztürk (2026). [DOI](https://doi.org/10.1109/access.2026.3672490) | Hospitality ABSA/rating | 11,275 TripAdvisor reviews; 14 five-star hotels, Kuşadası; 2022–2024 | Compensatory multi-aspect patterns | 12 macro aspects; GPT-4.1-mini labels; rating-specific high-utility itemset rules | Baseline diễn giải được cho các trade-off: rating thấp do negative co-occurrence, rating giữa do bù trừ, rating cao do nhiều positive aspects | IV/VI; peer-reviewed; full text verified |
| R2-F1 | Huang & Lo (2025). [DOI](https://doi.org/10.1007/s40558-025-00314-6) | Forgiveness/buffering | 396 người; 3×2 hotel check-in scenarios: human/humanoid/non-humanoid × process/outcome failure | Mind Perception, Attribution, Expectancy Disconfirmation, S-O-R | ANCOVA + PROCESS Model 6; forgiveness và service-recovery expectation serially mediate dissatisfaction trong process failures | Chứng minh forgiveness là cơ chế theo failure type, nhưng endpoint là dissatisfaction chứ không phải rating | III; peer-reviewed OA; full text |
| R2-F2 | Wei et al. (2025). [DOI](https://doi.org/10.1002/jtr.70154) | Forgiveness/buffering | OTA scenario experiment; cỡ mẫu chưa xác minh từ abstract | Fairness, risk, empathy, negative emotional contagion | Fairness ↑ empathy; risk ↓ empathy; empathy ↑ forgiveness; negative emotional contagion làm yếu empathy→forgiveness | Cơ chế gần nhất cho `Anger` như moderator và `Sublimation` như empathy/forgiveness; vẫn chưa nối tới star rating | III; peer-reviewed; abstract/metadata |

---

## 3. Measurement Synthesis

### 3.1. Hai trục phải tách

Round 2 xác nhận inconsistency không nên bị nén thành một biến duy nhất:

1. **Magnitude:** độ lớn sai khác, ví dụ Kwon et al. (2025):

   $$D_j^{abs}=\left|z(r_j)-z(s_j)\right|$$

2. **Direction:** dấu/hướng của sai khác, giữ riêng thay vì lấy trị tuyệt đối:

   $$D_{i,a}^{signed}=r_i^*-s_{i,a}^*$$

Trong đó $r_i^*$ và $s_{i,a}^*$ phải được đưa về cùng thang đo. Công thức signed aspect-level trên là **candidate extension của dự án**, không phải “công thức chuẩn” đã được literature xác nhận.

### 3.2. Điều đã được và chưa được xác nhận

- **Đã xác nhận:** magnitude liên tục ở document/product level; directional binary/categorical mismatch; absolute aspect-level conflict trong hospitality.
- **Chưa xác nhận:** signed continuous discrepancy ở review–aspect level được dùng và validated trực tiếp trong hospitality.
- **Rủi ro SentimentLens:** `|R_norm-S_a|` mất hướng; `τ` chỉ được mô tả là empirically selected, không có giá trị/quy trình chọn đủ rõ; phân tích kết quả còn aggregate ở province–category level.
- **Rủi ro Kwon:** SentiWordNet và Amazon domain có thể không chuyển nguyên trạng sang hotel reviews; cần thay sentiment estimator nhưng giữ cấu trúc phép đo.
- **Kết luận:** nếu proposal dùng signed aspect residual, phải tuyên bố là đóng góp phương pháp mới và báo cáo đồng thời signed value, absolute magnitude, cùng directional class.

---

## 4. Theory and Mechanism Synthesis

### 4.1. Inconsistency không nhất thiết là lỗi

- Kwon et al. cho thấy degree và direction inconsistency có thể tăng perceived usefulness; Curiosity Theory giải thích việc tín hiệu mâu thuẫn kích hoạt xử lý sâu hơn.
- Abaiyan et al. cho thấy mismatch có cấu trúc: 18.6% review incongruent; `Conservative Rater` (38.4%) và `Obligatory 5-Star` (28.3%) chiếm 66.7% các mismatch.
- Vì vậy, pipeline không nên xóa mismatch như noise trước khi kiểm tra pattern và context.

### 4.2. Forgiveness/Anger là cơ chế có điều kiện

- Huang and Lo: forgiveness thay đổi theo `failure type × service-provider humanness`; serial path `humanness → forgiveness → service-recovery expectation → dissatisfaction` chỉ được hỗ trợ rõ cho process failures.
- Wei et al.: fairness/risk tác động forgiveness thông qua empathy; negative emotional contagion làm yếu đường empathy→forgiveness.
- Hai bài hỗ trợ mô hình moderator/mediator cho `Sublimation` và `Anger`, nhưng **không** chứng minh chúng điều tiết quan hệ service-aspect sentiment → star rating.

### 4.3. Khoảng trống còn mở

Không tìm thấy nghiên cứu trong vòng quét này kiểm định trực tiếp:

$$Justice/Forgiveness/Anger \rightarrow \text{observed star-rating behavior}$$

trên dữ liệu review khách sạn thực tế. Đây vẫn là khoảng trống hợp lệ, không được trình bày như quan hệ đã có bằng chứng trực tiếp.

---

## 5. Technical Watchlist — Không đưa vào core set

| Nguồn | Lý do giữ | Lý do chưa vào core |
|---|---|---|
| Topçu, Asar, & Orman (2026). [Publisher record](https://dergipark.org.tr/en/pub/saucis/article/1748175) | 68,785 TripAdvisor reviews; DeBERTa + random oversampling đạt macro-F1 0.8141 và accuracy 0.8438; có phân tích mismatch định tính | Dùng rating làm supervised label nên không tạo sentiment signal độc lập; phù hợp baseline rating prediction, không phải discrepancy measure |
| McMurry (2026). [DOI](https://doi.org/10.18653/v1/2026.wassa-1.3) | 4,994 nhãn tay + 162,840 pseudo-labels cho implicit hostel “socialness”; F1 0.826 | Không có star-rating discrepancy; construct gián tiếp |
| Patil et al. (2026). [arXiv](https://arxiv.org/abs/2602.21082) | LLM-assisted ABSA trên 4.7M Yelp reviews; baseline scale lớn | Restaurant domain, preprint, không có discrepancy operationalization |

---

## 6. Core-Set Curation and Endpoint Check

- Round 1 có 11 nguồn; Round 2 đề xuất thêm 6 nguồn trực tiếp.
- Để giữ core set trong ngưỡng 10–15 của `RDR-0001`, **Valdivia et al. (2019)** chuyển thành provenance source và **Puh & Bagić Babac (2023)** chuyển thành legacy technical baseline; không xóa khỏi reference index.
- Core set làm việc hiện tại: **15 nguồn ngoài paper gốc**; watchlist không tính vào core.

| Tiêu chí RDR-0001 | Trạng thái sau Round 2 | Bằng chứng / thiếu hụt |
|---|---|---|
| 10–15 core papers | **Đạt** | 15 sau curation |
| ≥1 theoretical explanation | **Đạt** | S-O-R/Justice, Curiosity, Mind Perception, Attribution, Expectancy Disconfirmation |
| ≥1 discrepancy operationalization | **Đạt** | Continuous magnitude + directional class + aspect-level absolute conflict |
| ≥1 technical baseline | **Đạt** | HOSSemEval/TAS-BERT, HUIM aspect rules; DeBERTa/ROS ở watchlist |
| Saturation: 3–5 bài liên tiếp không sinh construct/method | **Chưa đạt** | Cả 6 nguồn promoted đều thêm construct, measure hoặc mechanism |
| Đủ ban hành RDR-0003 | **Chưa đạt** | Cần chốt estimator/thang chuẩn hóa/threshold và kiểm tra feasibility trên 394 mẫu 5-star có negative span |

**Quyết định sau vòng quét:** dừng broad search tạm thời vì core set đã chạm 15; bước kế tiếp là validation có mục tiêu trên dữ liệu dự án. Chỉ mở Round 3 nếu validation phát hiện measure không tái lập hoặc citation chain sinh nguồn trực tiếp hơn.

---

## 7. APA References — New Core Candidates

Abaiyan, R., Sutharsan, R., Amantha, K., Krishnathas, A., Rauff, A., Sriyathurshan, K., Narasinghe, P., Munasinghe, N., de Silva, N., & Wickramanayake, S. (2026). *Fault of our stars: Behavioral drivers of rating–sentiment incongruence* [Preprint]. arXiv. https://arxiv.org/abs/2606.25518

Huang, Z., & Lo, A. (2025). Human vs. robot service provider agents in service failures: Comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation. *Information Technology & Tourism, 27*, 417–448. https://doi.org/10.1007/s40558-025-00314-6

Jayakody, D., Thenahandi, P., & Jayarathna, S. (2026). *SentimentLens: Reconciling sentiment and ratings via dual-modality in the hospitality sector* [Preprint]. arXiv. https://arxiv.org/abs/2606.00084

Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025). Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness. *Asia Pacific Journal of Information Systems, 35*(1), 49–72. https://doi.org/10.14329/apjis.2025.35.1.49

Öztürk, A. C. (2026). Discovering aspect–sentiment drivers of hotel review ratings with interpretable high-utility rules. *IEEE Access, 14*, 39496–39511. https://doi.org/10.1109/access.2026.3672490

Wei, J., Lu, Z., Chen, Q., Li, L., Fan, H., Shen, H., Lu, H., Liao, S., & Wan, W. (2025). Consumer forgiveness in online travel agency service recovery: Consumer empathy and negative emotional contagion. *International Journal of Tourism Research, 27*(6). https://doi.org/10.1002/jtr.70154
