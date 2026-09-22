# Reference Literature Index (refs/INDEX.md)

Danh mục toàn bộ các bài báo khoa học, tài liệu học thuật và nghiên cứu nền tảng được sử dụng trong dự án.

---

## 1. Root Paper (Bài báo nền tảng)

- **Factsheet đọc nhanh (Dành cho Agent):** [`refs/root/factsheet.md`](root/factsheet.md) _(Tóm tắt thông số cốt lõi, phương trình và phân tích phản biện)_.
- **Toàn văn Markdown đầy đủ (Dành cho Agent):** [`refs/root/full_paper.md`](root/full_paper.md) _(Trích xuất 100% nguyên văn toàn bộ 15 trang bài báo: text, bảng biểu, công thức LaTeX, trích dẫn)_.
- **File gốc:** [`refs/root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on online_hotel_ratings.pdf`](root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on%20online_hotel_ratings.pdf)
- **Trích dẫn:** Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). _Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings_. International Journal of Hospitality Management, 134, 104574.
- **Vai trò trong dự án:** Bài báo gốc cung cấp khung tiếp cận S-O-R, pipeline BERTopic + WMLR trên 1.3M review và dataset đối chuẩn. Dự án kế thừa, tái lập và chỉ ra lỗi ngụy biện vòng lặp để mở rộng sang bài toán Bất nhất cảm xúc - điểm số.

---

## 2. Active Literature & Targeted RQ3 Candidates

### A. Inconsistency Core Evidence

- **Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025).** _Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance_. _International Journal of Hospitality Management, 130_, 104271. [DOI](https://doi.org/10.1016/j.ijhm.2025.104271). [Local PDF](inconsistency/2025_wang_score_textual_inconsistency.pdf). **Vai trò:** directional polarity mismatch và hotel-level inconsistency proportion.
- **Bigne, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023).** _Are customer star ratings and sentiments aligned?_ _Service Business, 17_, 281–314. [DOI](https://doi.org/10.1007/s11628-023-00524-0). [Local PDF](inconsistency/2023_bigne_customer_ratings_sentiments_aligned.pdf). **Vai trò:** ngoài/giáp cửa sổ chủ động nhưng rất hợp RQ3 mới; compensatory/cancel-out effect giữa positive và negative aspect sentiments; vẫn dùng trong active set.
- **Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025).** _Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness_. _Asia Pacific Journal of Information Systems, 35_(1), 49–72. [DOI](https://doi.org/10.14329/apjis.2025.35.1.49). [Local PDF](inconsistency/2025_kwon_rating_text_inconsistency_curiosity.pdf). **Vai trò:** tách continuous degree inconsistency `|z(rating)-z(sentiment)|` và directional mismatch; Curiosity Theory.
- **Abaiyan, R., et al. (2026).** _Fault of our stars: Behavioral drivers of rating–sentiment incongruence_. arXiv preprint. [arXiv](https://arxiv.org/abs/2606.25518). [Local PDF](inconsistency/2026_abaiyan_fault_of_our_stars_incongruence.pdf). **Vai trò:** 6 directional patterns và kiểm tra độ tin cậy của rating như weak sentiment label; chưa peer review.
- **Jayakody, D., Thenahandi, P., & Jayarathna, S. (2026).** _SentimentLens: Reconciling sentiment and ratings via dual-modality in the hospitality sector_. arXiv preprint. [arXiv](https://arxiv.org/abs/2606.00084). [Local PDF](inconsistency/2026_jayakody_sentimentlens_dual_modality.pdf). **Vai trò:** absolute cross-modal discrepancy ở hotel–aspect level; chưa peer review.
- **Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025).** _Unravelling the effects of two inconsistencies on online review helpfulness: Evidence from TripAdvisor_. _Decision Support Systems, 193_, 114450. [DOI](https://doi.org/10.1016/j.dss.2025.114450). [Chưa kéo được PDF: Closed access — Elsevier/DSS paywall]. **Vai trò:** phân biệt review inconsistency và rating inconsistency.

### B. Hàng đợi ưu tiên lấy toàn văn (Priority Retrieval Queue — 1/8 đã lấy)

> **Quy tắc dừng:** Còn 7/8 bài cần lấy; không tiếp tục cào rộng ngoài hàng đợi này. Các nguồn forgiveness, helpfulness và Peak-End chỉ lấy khi RQ3 cuối cùng thực sự sử dụng construct tương ứng.

1. **Kwon, W. (2026).** _Aspect-based sentiment analysis through zero-shot text classification and impact-asymmetry analysis_. _IJHM, 133_, 104397. [DOI](https://doi.org/10.1016/j.ijhm.2025.104397). [Chưa kéo được PDF: Elsevier paywall]. **Ưu tiên 1:** Trục lý thuyết chính RQ3 (Zero-shot ABSA + Kano asymmetry).
2. **Sharma, A., Shin, S., Nicolau, J. L., & Park, S. (2025).** _The review sentiment garden: Blossoming loss aversion and diminishing sensitivity across time and crisis_. _IJHM, 129_, 104170. [DOI](https://doi.org/10.1016/j.ijhm.2025.104170). [Local PDF](asymmetric-compensation/2025_sharma_review_sentiment_garden_accepted_manuscript.pdf). **Ưu tiên 2 — đã lấy:** Prospect Theory, loss aversion và reference point; accepted manuscript 32 trang.
3. **Wang, J., Wu, J., Sun, S., & Wang, S. (2024).** _The relationship between attribute performance and customer satisfaction: An interpretable machine learning approach_. _Data Science and Management, 7_(3), 164–180. [DOI](https://doi.org/10.1016/j.dsm.2024.01.003). [Chưa kéo được PDF: KeAi OA nhưng Cloudflare challenge]. **Ưu tiên 3:** XGBoost/SHAP cho attribute effects asymmetric và dynamic.
4. **Öztürk, A. C. (2026).** _Discovering aspect–sentiment drivers of hotel review ratings with interpretable high-utility rules_. _IEEE Access, 14_, 39496–39511. [DOI](https://doi.org/10.1109/access.2026.3672490). [Chưa kéo được PDF: IEEE Xplore chặn bot / HTTP 420]. **Ưu tiên 4:** Aspect rules và trade-off bù trừ đa khía cạnh.
5. **Albayrak, T., et al. (2025).** _Unravelling the influence of service failure on negative customer engagement: The moderating role of service recovery_. _IJHM, 130_, 104242. [DOI](https://doi.org/10.1016/j.ijhm.2025.104242). [Chưa kéo được PDF: Elsevier paywall]. **Ưu tiên 5:** Failure severity và service recovery làm boundary conditions.
6. **Xu, W., Yao, Z., Ma, Y., & Li, Z. (2025).** _Understanding customer complaints from negative online hotel reviews: A BERT-based deep learning approach_. _IJHM, 126_, 104057. [DOI](https://doi.org/10.1016/j.ijhm.2024.104057). [Chưa kéo được PDF: Elsevier paywall]. **Ưu tiên 6:** Complaint aspects và penalty không đồng đều; counter-evidence.
7. **Zhong, K., Liu, K., Gao, X., & Liu, Y. (2026).** _Impact of sensory clues in reviews on hotel ratings_. _Annals of Tourism Research, 119_, 104208. [DOI](https://doi.org/10.1016/j.annals.2026.104208). [Chưa kéo được PDF: Elsevier paywall]. **Ưu tiên 7:** Negative proximal sensory clues và penalty-dominant facility failures.
8. **Doan, T. T., et al. (2025).** _HOSSemEval-EB23: A robust dataset for aspect-based sentiment analysis of hospitality reviews_. _Multimedia Tools and Applications, 84_, 13057–13087. [DOI](https://doi.org/10.1007/s11042-024-19518-9). [Chưa kéo được PDF: Springer paywall]. **Ưu tiên 8:** Benchmark dataset/model cho hospitality ABSA.

*(Đã kéo thành công từ Round 3)*:
- **Sharma, A., et al. (2025).** _IJHM_. [Local PDF](asymmetric-compensation/2025_sharma_review_sentiment_garden_accepted_manuscript.pdf) — Accepted manuscript toàn văn (32 trang, 1.3MB).
- **Li, S., et al. (2024).** _JTAER_. [Local PDF](asymmetric-compensation/2024_li_two_stage_satisfaction_decision_model.pdf) — Supporting method hai giai đoạn; PDF toàn văn (MDPI OA, 3.5MB).

### C. Supporting Nền & Survey Logs

- **Ameur, A., Hamdi, S., & Ben Yahia, S. (2024).** _Sentiment analysis for hotel reviews: A systematic literature review_. _ACM Computing Surveys, 56_(2), 1–38. [DOI](https://doi.org/10.1145/3605152). [Chưa kéo được PDF: ACM paywall]. **Vai trò:** bản đồ kỹ thuật SLR.
- **Huang, Z., & Lo, A. (2025).** _Human vs. robot service provider agents in service failures: Comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation_. _Information Technology & Tourism, 27_, 417–448. [DOI](https://doi.org/10.1007/s40558-025-00314-6). [Local PDF](forgiveness/2025_huang_service_failure_forgiveness_robots.pdf). **Vai trò:** baseline thực chứng failure severity & recovery expectation.
- **Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025).** _Consumer forgiveness: A literature review and research agenda_. _Psychology & Marketing, 42_(2), 554–578. [DOI](https://doi.org/10.1002/mar.22138). [Chưa kéo được PDF: Wiley paywall]. **Vai trò:** synthesis 89 nghiên cứu forgiveness; giữ làm bài nền lý thuyết.
- **Logs tổng hợp khảo sát:** [`0002_survey_matrix_round_1.md`](../docs/logs/literature-survey/0002_survey_matrix_round_1.md) (R1) · [`0003_survey_matrix_round_2.md`](../docs/logs/literature-survey/0003_survey_matrix_round_2.md) (R2) · [`0004_synthesis_and_next_step.md`](../docs/logs/literature-survey/0004_synthesis_and_next_step.md) (Synthesis R1-R2) · [`0005_survey_matrix_round_3_rq3_rescoping.md`](../docs/logs/literature-survey/0005_survey_matrix_round_3_rq3_rescoping.md) (R3 scoping & matrix).

---

## 3. Legacy Literature (Tài liệu cũ & Không còn dùng cho hướng hiện tại)

> **Nguyên tắc quản lý file:** Không xóa file đã tải. Các bài bị loại khỏi active reading set được chuyển vào `refs/legacy/`; Valdivia và Almansour vẫn nằm trong `refs/inconsistency/` vì còn dùng cho provenance và định nghĩa.

### A. Cũ nhưng vẫn phải giữ (Provenance & Definition)

- **Valdivia, A., et al. (2019).** _Inconsistencies on TripAdvisor reviews: A unified index between users and sentiment analysis methods_. _Neurocomputing, 353_, 3–16. [DOI](https://doi.org/10.1016/j.neucom.2018.09.096). [Local PDF](inconsistency/2019_valdivia_tripadvisor_inconsistencies.pdf). **Xử lý:** Giữ làm provenance của unified index ($f(x,y)=\sqrt{x \cdot y^\beta}$); không dùng làm evidence hiện hành.
- **Almansour, A., Alotaibi, R., & Alharbi, H. (2022).** _Text-rating review discrepancy (TRRD): An integrative review and implications for research_. _Future Business Journal, 8_, 3. [DOI](https://doi.org/10.1186/s43093-022-00114-y). [Local PDF](inconsistency/2022_almansour_trrd_integrative_review.pdf). **Xử lý:** Giữ cho định nghĩa TRRD và cảnh báo dùng rating làm weak sentiment label.
- **Puh, K., & Bagić Babac, M. (2023).** _Predicting sentiment and rating of tourist reviews using machine learning_. _Journal of Hospitality and Tourism Insights, 6_(3), 1188–1204. [DOI](https://doi.org/10.1108/JHTI-02-2022-0078). [Local PDF](legacy/2023_puh_predicting_sentiment_and_rating.pdf). **Xử lý:** Legacy technical baseline ngoài cửa sổ; đã chuyển file vào `refs/legacy/`.

### B. Các bài không dùng tới nữa (Legacy / Không thuộc Active Set)

- **Topçu, A., Asar, M. A., & Orman, G. K. (2026).** _Improving hotel review rating prediction with transformer models_. _Sakarya University Journal of Computer and Information Sciences, 9_(2), 451–464. [Publisher record](https://dergipark.org.tr/en/pub/saucis/article/1748175). [Local PDF](legacy/2026_topcu_transformer_rating_prediction.pdf). **Lý do loại:** rating prediction dùng chính rating làm label; đã chuyển vào `refs/legacy/`. DOI trong publisher metadata bị lỗi nên không dùng làm định danh.
- **McMurry, I. W. (2026).** _Quantifying social sentiment in hostels using a domain-specific transformer pipeline_. _Proceedings of WASSA 2026_, 24–36. [DOI](https://doi.org/10.18653/v1/2026.wassa-1.3). [Local PDF](legacy/2026_mcmurry_hostel_social_sentiment.pdf). **Lý do loại:** conference paper, implicit hostel socialness, không có rating discrepancy; đã chuyển vào `refs/legacy/`.
- **Patil, V., Bacha, S. V., Yamani, R., Sun, Y., & Kejriwal, M. (2026).** _Beyond the star rating: A scalable framework for aspect-based sentiment analysis using LLMs and text classification_. arXiv preprint. [arXiv](https://arxiv.org/abs/2602.21082). [Local PDF](legacy/2026_patil_llm_absa_beyond_stars.pdf). **Lý do loại:** preprint, Yelp/restaurant domain, không đo discrepancy; đã chuyển vào `refs/legacy/`.
- **McCullough, H., et al. (2024).** _Journal of Business Research, 185_, 114899. [DOI](https://doi.org/10.1016/j.jbusres.2024.114899). [Chưa kéo được PDF]. **Lý do loại:** theory Peak-End/first-impression thú vị nhưng không operationalize được bằng dataset hiện tại (thiếu event chronology).
- **Kalnaovakul, K., et al. (2024).** _Journal of Hospitality and Tourism Insights_. [DOI](https://doi.org/10.1108/JHTI-06-2024-0591). [Chưa kéo được PDF]. **Lý do loại:** moderators chính (brand affiliation, reviewer experience) không tồn tại trong dataset.
- **Nhánh phụ Forgiveness/Justice (Kumar & Shankar 2024, Honora et al. 2024, Wei et al. 2025):** [Chưa kéo được PDF]. **Lý do loại:** không cần lấy nếu nhóm chốt RQ3 mới về asymmetric compensation; chỉ lấy khi RQ3 cuối cùng thực sự dùng construct tương ứng.

---

## 4. Cấu trúc Bổ sung Tài liệu Tương lai (Template)

Khi bổ sung bài báo mới vào thư mục `refs/`, cập nhật mục này theo mẫu:

```markdown
- **File:** `refs/<năm>_<tiêu_đề_ngắn>.pdf`
- **Trích dẫn:** Tác giả (Năm). Tên bài báo. Tạp chí, Tập(Số), Trang.
- **Chủ đề:** (Topic Modeling / ABSA / Buffering Effect / Two-Factor Theory)
- **Đóng góp cho dự án:** (Tóm tắt 1-2 câu về vai trò hoặc giá trị đối chứng)
```
