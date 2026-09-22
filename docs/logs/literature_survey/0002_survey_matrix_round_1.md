# Literature Survey — Round 1: Anchors, Alternatives, and Evidence Gaps

- **Ngày khảo sát:** 2026-09-20
- **Chế độ:** Scoping literature review (không tuyên bố PRISMA/systematic review)
- **Mục tiêu:** Kiểm tra ba điểm neo của `RDR-0001`: (1) khung lý thuyết, (2) cách lượng hóa bất nhất, (3) baseline/phương pháp thực nghiệm.
- **Kết quả:** 11 tài liệu ngoài paper gốc được đưa vào vòng 1; endpoint tổng thể **chưa đạt** vì chưa bão hòa và còn 3 nguồn mới chỉ được kiểm tra ở mức abstract/metadata.

---

## 1. Search Protocol

### 1.1. Nguồn và truy vấn

- **Nguồn:** trang nhà xuất bản, DOI/Crossref metadata, và 2 PDF đã lưu trong `refs/`.
- **Khoảng năm ưu tiên:** 2022–2026; chấp nhận nguồn nền tảng trước 2022 nếu trực tiếp định nghĩa/đo lường inconsistency.
- **Ngôn ngữ:** English.
- **Cụm truy vấn:**
  1. `score-textual inconsistency`, `text-rating review discrepancy`, `rating-sentiment incongruence`, `TripAdvisor inconsistency`.
  2. `hotel review aspect-based sentiment analysis`, `hospitality ABSA dataset`, `tourist review rating prediction`.
  3. `customer forgiveness service failure`, `justice theory online travel agency`, `hospitality buffering effect`.

### 1.2. Inclusion / Exclusion

**Include:** peer-reviewed journal paper; trực tiếp trả lời ít nhất một điểm neo; có DOI/metadata chính thức; ưu tiên hotel/tourism/OTA.

**Exclude:** chỉ nói sentiment chung mà không có rating/aspect; nguồn không xác minh được; bài kỹ thuật không có dữ liệu hospitality; tài liệu trùng lặp.

### 1.3. Giới hạn truy xuất

- Full text đã kiểm tra: Wang et al. (2025), Almansour et al. (2022), Bigne et al. (2023), Puh and Bagić Babac (2023), cùng paper gốc.
- Abstract/metadata chính thức: các nguồn còn lại. Không suy diễn công thức hoặc kết quả chi tiết vượt quá abstract.
- Đây là vòng khảo sát định hướng; số lượng kết quả tìm kiếm không được dùng như PRISMA flow.

---

## 2. Synthesis Matrix

> **Evidence level (adapted):** V = literature review; IV = observational/secondary-data empirical study; VI = single computational benchmark or cross-sectional empirical study. Thang ARS được dùng để mô tả loại bằng chứng, không phải xếp hạng tuyệt đối cho nghiên cứu NLP/management.

| ID | Nguồn | Cụm | Dữ liệu / phương pháp | Khung lý thuyết | Operationalization / baseline | Đóng góp trực tiếp | Evidence / kiểm tra |
|---|---|---|---|---|---|---|---|
| I1 | Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025). [DOI](https://doi.org/10.1016/j.ijhm.2025.104271) | Inconsistency | 299,975 Ctrip reviews, 300 hotels; BERT sentiment + regression | Heuristic–Systematic Model; Schema Incongruity; Cognitive Dissonance | Rating và text sentiment cùng mã hóa `{-1,0,1}`; inconsistency là cặp lệch; biến hotel-level là tỷ lệ high-score/low-sentiment reviews | Bằng chứng trực tiếp cho ma trận phân cực có hướng; inconsistency làm giảm hotel sales proxy | IV; full text + DOI verified |
| I2 | Almansour, Alotaibi, & Alharbi (2022). [DOI](https://doi.org/10.1186/s43093-022-00114-y) | Inconsistency | Integrative review; Web of Science, Scopus, ScienceDirect, Google Scholar | Không chốt một theory hành vi duy nhất | Đề xuất kiểm tra correlation/agreement giữa text và score; cảnh báo dùng rating làm nhãn sentiment mà không kiểm tra | Xác lập TRRD là bài toán độc lập và yêu cầu đo agreement/disagreement | V; open full text + DOI verified |
| I3 | Bigne, Ruiz, Perez-Cabañero, & Cuenca (2023). [DOI](https://doi.org/10.1007/s11628-023-00524-0) | Inconsistency | 20,954 TripAdvisor attraction reviews; DL sentiment, topic analysis, ANN, ANOVA | Schema Theory; Accessibility–Diagnosticity; Compensatory Choice Models | So sánh valence/positive/negative words theo nhóm sao; xem positive và negative là hai chiều có thể đồng tồn tại | “Cancel-out effect” cho mixed-neutral reviews; gợi ý trade-off giữa aspect sentiments | IV; open full text + DOI verified |
| I4 | Wang, Xia, Feng, & Cheng (2025). [DOI](https://doi.org/10.1016/j.dss.2025.114450) | Inconsistency | TripAdvisor hotel data theo title/abstract snippet; chi tiết model chưa kiểm tra | Heuristic–Systematic Model theo abstract snippet | Phân biệt review inconsistency và rating inconsistency; công thức chi tiết chưa kiểm tra được | Nguồn mới cần ưu tiên lấy full text; vòng 1 chưa trích kết quả định lượng | IV; DOI verified; **abstract/full text pending** |
| I5 | Valdivia et al. (2019). [DOI](https://doi.org/10.1016/j.neucom.2018.09.096) | Inconsistency | TripAdvisor reviews; unified index | Không xác minh trong vòng 1 | Unified index giữa user ratings và sentiment-analysis methods | Nguồn nền tảng cho phép đối chiếu một chỉ số liên tục thay vì chỉ ma trận phân cực | IV; DOI verified; **formula/full text pending** |
| M1 | Ameur, Hamdi, & Ben Yahia (2024). [DOI](https://doi.org/10.1145/3605152) | Hospitality SA/ABSA | Systematic review of hotel-review sentiment-analysis studies | Không phải theory hành vi | Phân loại preprocessing, representation, analysis level, model và dataset | Bản đồ phương pháp để tránh chọn model chỉ theo độ mới | V; DOI + abstract verified |
| M2 | Doan et al. (2025). [DOI](https://doi.org/10.1007/s11042-024-19518-9) | Hospitality ABSA | HOSSemEval-EB23; TAS Transformer variants và T5 | Không phải theory hành vi | TAS-BERT_MEDIUM đạt F1 = 79.74 theo abstract | Dataset/model benchmark trực tiếp cho aspect-level hospitality sentiment | VI; DOI + abstract verified; full details pending |
| M3 | Puh & Bagić Babac (2023). [DOI](https://doi.org/10.1108/JHTI-02-2022-0078) | Rating prediction | 20,491 TripAdvisor hotel reviews; NB, SVM, CNN, LSTM, BiLSTM | Không phải theory hành vi | BiLSTM: 72% accuracy cho 5-star rating, 89% cho 3-class sentiment | Baseline text→rating khả thi; có thể sinh `predicted rating`, nhưng paper không tự định nghĩa residual là TRRD | VI; local full text + DOI verified |
| T1 | Yoruk, Hsu, & Lee (2025). [DOI](https://doi.org/10.1002/mar.22138) | Forgiveness | Systematic review of 89 articles | Integrative psychological mechanism framework | Không đo text-rating discrepancy | Tổng hợp antecedents/mechanisms của consumer forgiveness; theory anchor rộng | V; DOI + abstract verified |
| T2 | Kumar & Shankar (2024). [DOI](https://doi.org/10.1177/14413582231194071) | OTA forgiveness | Qualitative exploration + survey `n=335`; CB-SEM + fsQCA | S-O-R + Justice Theory | Response speed, explanation, courtesy, problem-solving → justice/forgiveness → repatronage | Cầu nối trực tiếp giữa S-O-R, justice và forgiveness trong OTA context | VI; DOI + publisher abstract verified |
| T3 | Honora, Wang, & Chih (2024). [DOI](https://doi.org/10.1007/s11628-024-00563-1) | Forgiveness/buffering | Empirical moderated-mediation models | Perceived Justice; forgiveness/coping | Justice làm yếu tác động âm của service-failure severity lên forgiveness | Bằng chứng trực tiếp cho một cơ chế “buffer”: justice bảo vệ forgiveness trước service failure | VI; publisher page + DOI verified |

---

## 3. Kết quả theo ba điểm neo của RDR-0001

### 3.1. Khung lý thuyết nền

**Đã tìm được ít nhất một theory giải thích từng tầng, nhưng chưa nên chốt một theory duy nhất:**

1. **Reviewer behavior sau service failure:** `S-O-R + Justice Theory` là tổ hợp mạnh nhất vòng 1. Kumar and Shankar (2024) đặt justice/forgiveness trong S-O-R ở OTA; Honora et al. (2024) cho thấy justice làm suy yếu tác động âm của failure severity lên forgiveness.
2. **Trade-off giữa các khía cạnh trong cùng trải nghiệm:** `Compensatory Choice Models` từ Bigne et al. (2023) phù hợp để giải thích việc sentiment tích cực và tiêu cực ở các aspect khác nhau triệt tiêu/bù trừ nhau.
3. **Cách người đọc tiếp nhận review bất nhất:** `Heuristic–Systematic Model + Schema Incongruity` từ Wang et al. (2025) giải thích hậu quả của inconsistency đối với người đọc và doanh số, nhưng không trực tiếp giải thích tại sao người viết chê mà vẫn cho điểm cao.

**Kết luận tạm thời:** S-O-R vẫn dùng được làm khung vĩ mô; Justice Theory/forgiveness và Compensatory Choice Models là ứng viên cơ chế vi mô. HSM/Schema Incongruity nên được xem là theory cho **downstream reader response**, không thay thế theory về **reviewer rating behavior**.

### 3.2. Cách lượng hóa độ bất nhất

**Được chứng minh trực tiếp trong vòng 1:**

- **Categorical directional mismatch:** chuẩn hóa text sentiment và rating vào cùng thang `{-1,0,1}`, rồi đánh dấu các cặp không khớp; có thể giữ chiều `high-rating/low-sentiment` và `low-rating/high-sentiment`.
- **Aggregate proportion:** tỷ lệ review bất nhất trong mỗi hotel, như Wang et al. (2025).
- **Agreement/correlation validation:** Almansour et al. (2022) yêu cầu kiểm tra quan hệ giữa text và rating trước khi dùng rating làm sentiment label.

**Chưa đủ bằng chứng để chốt:**

- `Residual = Rating - predicted_rating_text` hiện mới là một **candidate extension** được hỗ trợ gián tiếp bởi khả năng dự đoán rating của Puh and Bagić Babac (2023), chưa được vòng 1 xác nhận là công thức TRRD chuẩn trong hospitality.
- Unified index của Valdivia et al. (2019) cần đọc full text và trích đúng công thức trước khi so sánh.
- Review inconsistency/rating inconsistency của Wang et al. (2025, DSS) cần full text để xác minh biến và phép đo.

### 3.3. Baseline và phương pháp thực nghiệm

1. **Baseline tái lập trực tiếp:** pipeline paper gốc `BERTopic + VADER + WMLR`.
2. **Baseline text→rating:** BiLSTM của Puh and Bagić Babac (2023), với reported accuracy 72% cho bài toán 5 lớp.
3. **Benchmark aspect-level:** HOSSemEval-EB23 + TAS-BERT_MEDIUM, reported F1 79.74.
4. **Không chốt model ở vòng 1:** ba baseline giải ba nhiệm vụ khác nhau; không được so sánh accuracy/F1 trực tiếp nếu label space và split khác nhau.

---

## 4. Cross-paper Tensions

| Cặp | Tension | Xử lý tạm thời |
|---|---|---|
| Bigne et al. (2023) vs. Wang et al. (2025, IJHM) | Bigne cho thấy valence nhìn chung aligned với rating; Wang tập trung vào subset high-rating/low-sentiment và thấy tác động kinh doanh âm | Không mâu thuẫn trực tiếp: alignment ở mức tổng thể có thể cùng tồn tại với một minority subset bất nhất có ý nghĩa quản trị |
| Puh & Bagić Babac (2023) vs. Almansour et al. (2022) | Puh dùng rating làm label để dự đoán; Almansour cảnh báo rating không luôn phản ánh text sentiment | Rating prediction vẫn hợp lệ như một task, nhưng residual/mismatch phải được đánh giá riêng; không đồng nhất “dự đoán rating tốt” với “đo sentiment đúng” |
| HSM/Schema Incongruity vs. S-O-R/Justice | Nhóm đầu giải thích phản ứng của người đọc; nhóm sau giải thích forgiveness/repatronage sau failure | Tách hai actor và hai outcome; không trộn theory cho reviewer với theory cho prospective reader |

**Coverage note:** 11 external papers; 3 candidate tension pairs được kiểm tra. Đây là scoped advisory scan, không phải kiểm tra mọi cặp bài báo.

---

## 5. Source Verification Summary

- **DOI/metadata existence:** 11/11 verified qua publisher/Crossref.
- **Full-text claim check:** 4/11 external papers; 7/11 chỉ dùng publisher abstract/metadata hoặc local abstract-level evidence.
- **Predatory-journal signal:** không phát hiện trong vòng 1; toàn bộ nguồn thuộc publisher/journal đã xác minh metadata.
- **COI/funding:** chưa kiểm tra đầy đủ cho 11 nguồn; chỉ ghi nhận metadata công khai, không suy diễn ảnh hưởng khi thiếu disclosure/full text.
- **Không có nguồn nào bị loại vì fabricated DOI/title.**

---

## 6. Endpoint Check và Round 2

| Tiêu chí RDR-0001 | Trạng thái vòng 1 | Bằng chứng / thiếu hụt |
|---|---|---|
| 10–15 core papers | **Đạt về số lượng ban đầu** | 11 external papers, đủ 3 cụm |
| ≥1 theoretical explanation | **Đạt tạm thời** | S-O-R + Justice; Compensatory Models; HSM/Schema Incongruity |
| ≥1 discrepancy operationalization | **Đạt tạm thời** | Directional categorical mismatch + hotel-level proportion |
| ≥1 technical baseline | **Đạt** | Root pipeline; BiLSTM rating; HOSSemEval/TAS-BERT |
| Saturation (3–5 bài không sinh thêm construct/method) | **Chưa đánh giá** | Mới vòng đầu, chưa có chuỗi 3–5 bài bão hòa |
| Đủ chốt RDR-0002 | **Chưa đạt** | Cần full text/formula của Valdivia 2019 và Wang et al. 2025 DSS; cần kiểm tra validity của signed discrepancy ở aspect level |

**Round 2 ưu tiên:**

1. Trích đúng công thức unified index của Valdivia et al. (2019).
2. Kiểm tra full text Wang et al. (2025, DSS) để phân biệt `review inconsistency` và `rating inconsistency`.
3. Tìm nghiên cứu dùng signed/continuous discrepancy ở aspect level; nếu không có, ghi rõ đây là đóng góp phương pháp mới thay vì “công thức chuẩn”.
4. Tìm hospitality papers kiểm định trực tiếp `Justice/Forgiveness → rating behavior`, không chỉ repatronage/avoidance.

---

## 7. APA References

Almansour, A., Alotaibi, R., & Alharbi, H. (2022). Text-rating review discrepancy (TRRD): An integrative review and implications for research. *Future Business Journal, 8*, Article 3. https://doi.org/10.1186/s43093-022-00114-y

Ameur, A., Hamdi, S., & Ben Yahia, S. (2024). Sentiment analysis for hotel reviews: A systematic literature review. *ACM Computing Surveys, 56*(2), 1–38. https://doi.org/10.1145/3605152

Bigne, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023). Are customer star ratings and sentiments aligned? A deep learning study of the customer service experience in tourism destinations. *Service Business, 17*, 281–314. https://doi.org/10.1007/s11628-023-00524-0

Doan, T. T., Tran, T. Q., Le, D. T., Tran, A. H., Nguyen, A. T., Le, T. H. A., Doan, T. N. T., Huynh, S. T., & Nguyen, B. T. (2025). HOSSemEval-EB23: A robust dataset for aspect-based sentiment analysis of hospitality reviews. *Multimedia Tools and Applications, 84*, 13057–13087. https://doi.org/10.1007/s11042-024-19518-9

Honora, A., Wang, K.-Y., & Chih, W.-H. (2024). The role of customer forgiveness and perceived justice in restoring relationships with customers. *Service Business, 18*, 363–393. https://doi.org/10.1007/s11628-024-00563-1

Kumar, A., & Shankar, A. (2024). Why do consumers forgive online travel agencies? A multi-study approach. *Australasian Marketing Journal, 32*(4), 323–338. https://doi.org/10.1177/14413582231194071

Puh, K., & Bagić Babac, M. (2023). Predicting sentiment and rating of tourist reviews using machine learning. *Journal of Hospitality and Tourism Insights, 6*(3), 1188–1204. https://doi.org/10.1108/JHTI-02-2022-0078

Valdivia, A., Hrabova, E., Chaturvedi, I., Luzón, M. V., Troiano, L., Cambria, E., & Herrera, F. (2019). Inconsistencies on TripAdvisor reviews: A unified index between users and sentiment analysis methods. *Neurocomputing, 353*, 3–16. https://doi.org/10.1016/j.neucom.2018.09.096

Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025). Unravelling the effects of two inconsistencies on online review helpfulness: Evidence from TripAdvisor. *Decision Support Systems, 193*, Article 114450. https://doi.org/10.1016/j.dss.2025.114450

Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025). Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance. *International Journal of Hospitality Management, 130*, Article 104271. https://doi.org/10.1016/j.ijhm.2025.104271

Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025). Consumer forgiveness: A literature review and research agenda. *Psychology & Marketing, 42*(2), 554–578. https://doi.org/10.1002/mar.22138
