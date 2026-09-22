# Reference Literature Index (refs/INDEX.md)

Danh mục nguồn của dự án, tổ chức **theo chức năng** — mỗi thư mục trả lời một câu hỏi khác nhau của đề tài, không phải theo chủ đề.

- **Nguyên tắc:** không xoá file đã tải. Nguồn bị hạ ưu tiên chuyển sang `08_legacy/`, giữ nguyên audit trail.
- **Chỉ mục hành động** (còn thiếu gì, tải ở đâu, lưu vào đâu): xem Mục 9.
- **Nhật ký khảo sát:** [`docs/logs/literature_survey/`](../docs/logs/literature_survey/).

---

## 0. Sơ đồ thư mục theo chức năng

| Thư mục | Chức năng | File |
| --- | --- | ---: |
| `01_root/` | Bài gốc đối chuẩn (paper bị phản biện) + factsheet | 3 |
| `02_definition/` | Định nghĩa construct & provenance của thước đo | 2 |
| `03_phenomenon/` | Bằng chứng hiện tượng bất nhất: đo lường, prevalence | 8 |
| `04_mechanism/` | Lý thuyết & cơ chế bất đối xứng (Kano, prospect, two-stage) | 7 |
| `05_boundary_conditions/` | Điều kiện biên: severity, recovery, nền tảng, hạng sao | 6 |
| `06_counter_evidence/` | Phản biện cơ chế + phê bình phương pháp | 1 |
| `07_baselines_methods/` | Baseline dự đoán, ABSA, benchmark, công cụ giải thích | 6 |
| `08_legacy/` | Đã hạ ưu tiên; giữ audit trail | 4 |

**Quy ước tên file:** `<năm>_<tác giả chính không dấu>_<chủ đề ngắn>.pdf`; file Round 4 còn mã nhóm (`A1_`, `B5_`, `C2_`, `D3_`, `E1_`…) để truy vết về log `0006`.

---

## 1. `01_root/` — Bài gốc đối chuẩn

- **Factsheet (Agent đọc file này, không đọc PDF 5,4 MB):** [`01_root/factsheet.md`](01_root/factsheet.md)
- **Toàn văn Markdown:** [`01_root/full_paper.md`](01_root/full_paper.md)
- **File gốc:** [`01_root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on_online_hotel_ratings.pdf`](01_root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on_online_hotel_ratings.pdf)
- **Trích dẫn:** Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). _Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings_. IJHM, 134, 104574.
- **Vai trò:** cung cấp khung S-O-R, pipeline BERTopic + WMLR trên 1,3M review và dataset đối chuẩn. Dự án kế thừa, tái lập và chỉ ra lỗi ngụy biện vòng để mở sang bài toán bất nhất cảm xúc – điểm số.

---

## 2. `02_definition/` — Định nghĩa & provenance

- **Valdivia, A., et al. (2019).** _Inconsistencies on TripAdvisor reviews: A unified index..._. _Neurocomputing, 353_, 3–16. [DOI](https://doi.org/10.1016/j.neucom.2018.09.096). [Local PDF](02_definition/2019_valdivia_tripadvisor_inconsistencies.pdf). **Vai trò:** provenance của unified index $f(x,y)=\sqrt{x \cdot y^\beta}$; không dùng làm evidence hiện hành.
- **Almansour, A., Alotaibi, R., & Alharbi, H. (2022).** _Text-rating review discrepancy (TRRD): An integrative review..._. _Future Business Journal, 8_, 3. [DOI](https://doi.org/10.1186/s43093-022-00114-y). [Local PDF](02_definition/2022_almansour_trrd_integrative_review.pdf). **Vai trò:** định nghĩa TRRD; cảnh báo rating là weak sentiment label.

---

## 3. `03_phenomenon/` — Bằng chứng hiện tượng bất nhất

**Đã có toàn văn:**

- **Bigné, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023).** _Are customer star ratings and sentiments aligned?_. _Service Business, 17_, 281–314. [DOI](https://doi.org/10.1007/s11628-023-00524-0). [Local PDF](03_phenomenon/2023_bigne_customer_ratings_sentiments_aligned.pdf). **Vai trò:** compensatory/cancel-out giữa positive và negative aspect sentiments.
- **Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025).** _Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness_. _APJIS, 35_(1), 49–72. [DOI](https://doi.org/10.14329/apjis.2025.35.1.49). [Local PDF](03_phenomenon/2025_kwon_rating_text_inconsistency_curiosity.pdf). **Vai trò:** tách degree inconsistency `|z(rating)−z(sentiment)|` và directional mismatch.
- **Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025).** _Beyond the stars: Unpacking the impact of score-textual inconsistency..._. _IJHM, 130_, 104271. [DOI](https://doi.org/10.1016/j.ijhm.2025.104271). [Local PDF](03_phenomenon/2025_wang_score_textual_inconsistency.pdf). **Vai trò:** directional polarity mismatch và inconsistency proportion cấp hotel.
- **Abaiyan, R., et al. (2026).** _Fault of our stars: Behavioral drivers of rating–sentiment incongruence_. arXiv. [arXiv](https://arxiv.org/abs/2606.25518). [Local PDF](03_phenomenon/2026_abaiyan_fault_of_our_stars_incongruence.pdf). **Vai trò:** 6 dạng lệch có hướng; rating là weak label. **Chưa peer review.**
- **Jayakody, D., Thenahandi, P., & Jayarathna, S. (2026).** _SentimentLens: Reconciling sentiment and ratings via dual-modality..._. arXiv. [arXiv](https://arxiv.org/abs/2606.00084). [Local PDF](03_phenomenon/2026_jayakody_sentimentlens_dual_modality.pdf). **Vai trò:** absolute cross-modal discrepancy ở hotel–aspect level. **Chưa peer review.**
- **Hu, F., Pan, J., & Wang, H. (2024).** _Unveiling the spatial and temporal variation of customer sentiment in hotel experiences: A case study of Beppu City, Japan_. _Humanities and Social Sciences Communications, 11_(1), 1695. [DOI](https://doi.org/10.1057/s41599-024-04226-4). [Local PDF](03_phenomenon/E4_hu_sentiment_rating_inconsistency_beppu.pdf). **Vai trò:** **mốc prevalence độc lập** — 694/4.004 review (17,3%) bất nhất rõ rệt.
- **Marreira, et al. (2026).** _Rating–text mismatch in Brazilian Portuguese reviews: How reliable are zero-shot LLMs?_. _PROPOR 2026_, 959–967. [ACL Anthology](https://aclanthology.org/2026.propor-1.96/). [Local PDF](03_phenomenon/C2_marreira_rating_text_mismatch_llm.pdf). **Vai trò:** bất nhất cấp văn bản ~10%; hội nghị, không DOI.
- **Biasetton, N., Ricciardi, G., & Salmaso, L. (2026).** _How well do ratings reflect sentiment? Evidence from a large Italian review corpus_. _Applied Stochastic Models in Business and Industry, 42_(2). [DOI](https://doi.org/10.1002/asmb.70090). [Local PDF](03_phenomenon/2026_biasetton_ratings_reflect_sentiment.pdf). Text-implied rating ở cấp văn bản — **lân cận gần niche nhất**.

**Chưa có toàn văn (cần thư viện trường):**

- **Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025).** _Unravelling the effects of two inconsistencies on online review helpfulness_. _DSS, 193_, 114450. [DOI](https://doi.org/10.1016/j.dss.2025.114450). Phân biệt review inconsistency và rating inconsistency.
- **Kirilenko, A., Stepchenkova, S., Gromoll, R., & Jo, Y. (2024).** _Comprehensive examination of online reviews divergence over time and platform types_. _IJHM, 117_, 103647. [DOI](https://doi.org/10.1016/j.ijhm.2023.103647). Cùng khách sạn, khác nền tảng → khác phân bố sao và cảm xúc.
- **Kovács, I. (2025).** _The impact of construal level on review consistency and helpfulness in online evaluations_. _Computers in Human Behavior, 162_, 108550. [DOI](https://doi.org/10.1016/j.chb.2024.108550). Consistency text–sao theo mức construal.

- **Liu, X., Ma, X., & Dou, Y. (2025).** _Injecting new insights: How do review sentiment and rating inconsistency shape the helpfulness of airline reviews?_. _IP&M, 62_(2), 104088. [DOI](https://doi.org/10.1016/j.ipm.2025.104088). Bất nhất là scalar tổng hợp.

---

## 4. `04_mechanism/` — Lý thuyết & cơ chế bất đối xứng

**Đã có toàn văn:**

- **Li, S., Zhu, ..., & Yu, ... (2024).** _Two-stage satisfaction decision model_. _JTAER, 19_(1). [DOI](https://doi.org/10.3390/jtaer19010015). [Local PDF](04_mechanism/2024_li_two_stage_satisfaction_decision_model.pdf). **Vai trò:** non-compensatory trước, compensatory sau — cấu trúc toán học rõ nhất.
- **Wang, J., Wu, J., Sun, S., & Wang, S. (2024).** _The relationship between attribute performance and customer satisfaction..._. _Data Science and Management, 7_(3), 164–180. [DOI](https://doi.org/10.1016/j.dsm.2024.01.003). [Local PDF](04_mechanism/2024_wang_attribute_performance_satisfaction.pdf). **Vai trò:** XGBoost + SHAP; quan hệ nonlinear, asymmetric, dynamic.
- **Sharma, A., Shin, S., Nicolau, J. L., & Park, S. (2025).** _The review sentiment garden_. _IJHM, 129_, 104170. [DOI](https://doi.org/10.1016/j.ijhm.2025.104170). [Local PDF](04_mechanism/2025_sharma_review_sentiment_garden_accepted_manuscript.pdf). **Vai trò:** Prospect Theory — loss aversion, diminishing sensitivity.
- **Öztürk, A. C. (2026).** _Discovering aspect–sentiment drivers of hotel review ratings..._. _IEEE Access, 14_, 39496–39511. [DOI](https://doi.org/10.1109/access.2026.3672490). [Local PDF](04_mechanism/2026_ozturk_aspect_sentiment_high_utility_rules.pdf). **Vai trò:** high-utility rules cho trade-off đa khía cạnh.
- **Regitz, D., Höpken, W., & Fuchs, M. (2026).** _Online customer feedback for identifying KANO product quality features..._. _Information Technology & Tourism, 28_(1), Article 20. [DOI](https://doi.org/10.1007/s40558-025-00354-y). [Local PDF](04_mechanism/A1_regitz_kano_quality_features_reviews.pdf). **Vai trò:** phân loại Kano từ review; **ranh giới tính mới mỏng nhất của đề tài**.
- **Li, J., Lee, B., & Kim, J. (2025).** _Analyzing factors affecting overall customer satisfaction... BERTopic and three-factor theory_. _SAGE Open, 15_(3). [DOI](https://doi.org/10.1177/21582440251335169). [Local PDF](04_mechanism/2025_li_bertopic_three_factor_prca.pdf). BERTopic + PRCA; vai trò thuộc tính đổi theo hạng sao.
- **Zhang, F., Seshadri, K., Liu, S., & Santamouris, M. (2025).** _The impact of indoor environmental quality on tourist accommodation ratings using guest reviews_. _Building and Environment, 280_, 113135. [DOI](https://doi.org/10.1016/j.buildenv.2025.113135). [Local PDF](04_mechanism/2025_zhang_indoor_environment_ratings.pdf). >540.000 review; thuộc tính vật lý penalty-dominant.

**Chưa có toàn văn:**

- **Kwon, W. (2026).** _Aspect-based sentiment analysis through zero-shot text classification and impact-asymmetry analysis_. _IJHM, 133_, 104397. [DOI](https://doi.org/10.1016/j.ijhm.2025.104397). **Trục lý thuyết chính của RQ3** (Kano/impact-asymmetry). **Ưu tiên 1 khi nhờ thư viện.**

- **Park, H., Lee, M., Back, K.-J., DeFranco, A., & Suh, J. (2025).** _Dynamic roles of hotel mobile application... impact asymmetry analysis_. _IJCHM, 37_(5), 1622–1640. [DOI](https://doi.org/10.1108/ijchm-12-2023-1914). IAA trên 88.309 review.

- **Cui, J., Zhang, S., & Wang, L. (2025).** _Evaluating canal heritage tourists' satisfaction: An asymmetric impact-performance analysis..._. _JHTM, 62_, 108–115. [DOI](https://doi.org/10.1016/j.jhtm.2025.01.002). AIPA + PRCA.
- **Xu, W., Yao, Z., Ma, Y., & Li, Z. (2025).** _Understanding customer complaints from negative online hotel reviews: A BERT-based deep learning approach_. _IJHM, 126_, 104057. [DOI](https://doi.org/10.1016/j.ijhm.2024.104057). **Vai trò:** 7 complaint aspect với penalty **không đồng đều** — counter-evidence cho giả định Service là moderator trung tâm.
- **Zhong, K., Liu, K., Gao, X., & Liu, Y. (2026).** _Impact of sensory clues in reviews on hotel ratings_. _Annals of Tourism Research, 119_, 104208. [DOI](https://doi.org/10.1016/j.annals.2026.104208). **Vai trò:** negative proximal sensory cue có penalty-dominant — căn cứ tách `Facility` theo severity/diagnosticity.

---

## 5. `05_boundary_conditions/` — Điều kiện biên

**Đã có toàn văn:**

- **Huang, Z., & Lo, A. (2025).** _Human vs. robot service provider agents in service failures..._. _Information Technology & Tourism, 27_, 417–448. [DOI](https://doi.org/10.1007/s40558-025-00314-6). [Local PDF](05_boundary_conditions/2025_huang_service_failure_forgiveness_robots.pdf). **Vai trò:** failure severity & recovery expectation.
- **Lim, W. M., Saha, V., & Das, M. (2025).** _From service failure to brand loyalty: Evidence of service recovery paradox_. _Journal of Brand Management, 32_(4), 257–281. [DOI](https://doi.org/10.1057/s41262-025-00380-5). [Local PDF](05_boundary_conditions/B5_lim_service_recovery_paradox.pdf). **Vai trò:** giới hạn trên của bù trừ.
- **Das, M., Jebarajakirthy, C., Maseeh, H. I., Lim, W. M., & Shah, J. S. (2026).** _Online service failure and recovery: An integrated meta-analytic perspective..._. _JBR, 202_, 115752. [DOI](https://doi.org/10.1016/j.jbusres.2025.115752). [Local PDF](05_boundary_conditions/2026_das_online_failure_recovery_meta.pdf). **Meta-analysis 147 nghiên cứu, N=82.901 — mức bằng chứng I.**
- **Tengilimoglu, E., & Öztürk, Y. (2024).** _The effects of eWOM triggered service recovery... moderating role of failure severity_. _IJTR, 26_(4), e2673. [DOI](https://doi.org/10.1002/jtr.2673). [Local PDF](05_boundary_conditions/2024_tengilimoglu_ewom_recovery_severity.pdf). Severity làm moderator trực tiếp.
- **Leo, W. W. C., Maggioni, I., Sembada, A. Y., & Tsarenko, Y. (2026).** _The dynamics of customer participation in service recovery..._. _IJHM, 140_, 104809. [DOI](https://doi.org/10.1016/j.ijhm.2026.104809). [Local PDF](05_boundary_conditions/2026_leo_participation_recovery_severity.pdf). Severity + quality signals.
- **Hwang, J. (2024).** _The effects of service recovery actions on customers' post-recovery responses to OTAs_. _IJTR, 26_(4), e2742. [DOI](https://doi.org/10.1002/jtr.2742). [Local PDF](05_boundary_conditions/2024_hwang_double_deviation_ota.pdf). Double deviation → penalty phi tuyến.

**Chưa có toàn văn:**





- **Albayrak, T., et al. (2025).** _Unravelling the influence of service failure on negative customer engagement..._. _IJHM, 130_, 104242. [DOI](https://doi.org/10.1016/j.ijhm.2025.104242). Failure type, perceived severity, recovery.
- **Tan, K. P.-S., & Zou, S. (2024).** _The profitable art of managerial responses to online reviews..._. _JQAH&T_, 1–26. [DOI](https://doi.org/10.1080/1528008x.2024.2410214). Recovery đo từ văn bản review.

---

## 6. `06_counter_evidence/` — Phản biện & phê bình phương pháp

**Đã có toàn văn:**

- **Sterner, M. (2026).** _Biases in online reputation systems: A survey of the empirical literature_. _Electronic Commerce Research_. [DOI](https://doi.org/10.1007/s10660-026-10176-7). [Local PDF](06_counter_evidence/D3_sterner_biases_online_reputation_survey.pdf). **Vai trò:** phân rã méo thành 5 nguồn cấu trúc; can thiệp nền tảng thường làm tăng phương sai.

**Chưa có toàn văn:**

- **Han, S., & Anderson, C. K. (2025).** _The platform matters: Selection and measurement bias in online reviews_. _Cornell Hospitality Quarterly_. [DOI](https://doi.org/10.1177/19389655251327536). **Đòn phản biện mạnh nhất** — thiên lệch đo lường dương trên TripAdvisor.
- **Slevitch, L. (2024).** _Kano model categorization methods: Typology and systematic critical overview..._. _JHTR_. [DOI](https://doi.org/10.1177/10963480241230957). Phân loại Kano/PRCA có lỗi quy trình.
- **Mellinas, J. P., Di Nolfo-Aiassa, C., & Martin-Fuentes, E. (2025).** _The weight of a review: Assessing Booking.com's new scoring system_. _Tourism and Hospitality Research_. [DOI](https://doi.org/10.1177/14673584251384011). Thuật toán nền tảng tách điểm khỏi văn bản.

---

## 7. `07_baselines_methods/` — Baseline & phương pháp

**Đã có toàn văn:**

- **Puh, K., & Bagić Babac, M. (2023).** _Predicting sentiment and rating of tourist reviews using machine learning_. _JHTI, 6_(3), 1188–1204. [DOI](https://doi.org/10.1108/jhti-02-2022-0078). [Local PDF](07_baselines_methods/2023_puh_predicting_sentiment_and_rating.pdf). Baseline dự báo điểm.
- **Ameur, A., Hamdi, S., & Ben Yahia, S. (2024).** _Sentiment analysis for hotel reviews: A systematic literature review_. _ACM Computing Surveys, 56_(2), 1–38. [DOI](https://doi.org/10.1145/3605152). [Local PDF](07_baselines_methods/2024_ameur_hotel_reviews_sentiment_slr.pdf). **Mức bằng chứng I** — bản đồ kỹ thuật.
- **Pramono, B. A., Gernowo, R., & Sofwan, A. (2026).** _Explainable multilingual aspect-based sentiment analysis for tourism using SHAP and LIME_. _ETASR, 16_(3), 37077–37084. [DOI](https://doi.org/10.48084/etasr.18774). [Local PDF](07_baselines_methods/E1_pramono_explainable_absa_shap_lime.pdf). **Cảnh báo venue:** không trong DOAJ, không core — chỉ dùng cho kỹ thuật.
- **You, X.-Y., et al. (2024).** _Using multitask learning with pre-trained language models for ABSA in the hospitality industry_. _PACLIC 2024_, 131–140. [ACL Anthology](https://aclanthology.org/2024.paclic-1.12/). [Local PDF](07_baselines_methods/E2_you_multitask_plm_absa_hospitality.pdf). **Số baseline:** RoBERTa đa nhiệm AUROC 0,9214 · F1 0,5817 cho 8 khía cạnh. Hội nghị, không DOI.
- **Guidotti, D., Pandolfo, L., & Pulina, L. (2025).** _Discovering sentiment insights: Streamlining tourism review analysis with LLMs_. _Information Technology & Tourism, 27_(1), 227–261. [DOI](https://doi.org/10.1007/s40558-024-00309-9). [Local PDF](07_baselines_methods/E3_guidotti_llm_tourism_review_analysis.pdf). Prior art cho mục đích hỗ trợ ra quyết định.
- **Zhu, A., et al. (2025).** _DaNet: Dual-aware enhanced alignment network for multimodal ABSA_. _Findings of ACL 2025_, 14369–14381. [DOI](https://doi.org/10.18653/v1/2025.findings-acl.741). [Local PDF](07_baselines_methods/E6_zhu_danet_multimodal_absa.pdf). Liên quan thấp (đa phương thức).

**Chưa có toàn văn:**

- **Doan, T. T., et al. (2025).** _HOSSemEval-EB23: A robust dataset for ABSA of hospitality reviews_. _MTAP, 84_, 13057–13087. [DOI](https://doi.org/10.1007/s11042-024-19518-9). Benchmark dataset.
- **Topçu, A., Asar, M. A., & Orman, G. K. (2026).** _Improving hotel review rating prediction with transformer models_. _Sakarya Univ. J. Computer & Information Sciences, 9_(2), 451–464. [Publisher record](https://dergipark.org.tr/en/pub/saucis/article/1748175). Chỉ dùng làm baseline kỹ thuật (file ở `08_legacy/`).
- **Kumar, M., Kumar, C., Kumar, N., & Kavitha, S. (2024).** _Efficient hotel rating prediction from reviews using ensemble learning technique_. _Wireless Personal Communications, 137_(2), 1161–1187. [DOI](https://doi.org/10.1007/s11277-024-11457-w). **Cảnh báo venue-fit:** tạp chí viễn thông, ưu tiên thấp.

---

## 8. `08_legacy/` — Đã hạ ưu tiên

- **Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025).** _Consumer forgiveness: A literature review and research agenda_. _Psychology & Marketing, 42_(2), 554–578. [DOI](https://doi.org/10.1002/mar.22138). [Local PDF](08_legacy/2025_yoruk_consumer_forgiveness_review.pdf). **Lý do:** RQ3 đã chốt (`RDR-0004`) không dùng construct forgiveness.
- **McMurry, I. W. (2026).** _Quantifying social sentiment in hostels..._. _WASSA 2026_, 24–36. [DOI](https://doi.org/10.18653/v1/2026.wassa-1.3). [Local PDF](08_legacy/2026_mcmurry_hostel_social_sentiment.pdf). **Lý do:** hội nghị, hostel socialness, không có rating discrepancy.
- **Patil, V., et al. (2026).** _Beyond the star rating: A scalable framework for ABSA using LLMs..._. arXiv. [arXiv](https://arxiv.org/abs/2602.21082). [Local PDF](08_legacy/2026_patil_llm_absa_beyond_stars.pdf). **Lý do:** preprint, domain nhà hàng, không đo discrepancy.
- **Topçu, A., et al. (2026).** [Local PDF](08_legacy/2026_topcu_transformer_rating_prediction.pdf). **Lý do:** rating prediction dùng chính rating làm label. DOI publisher bị lỗi nên không dùng làm định danh.
- **McCullough, H., et al. (2024).** _Journal of Business Research, 185_, 114899. [DOI](https://doi.org/10.1016/j.jbusres.2024.114899). **Lý do:** Peak-End/first-impression không operationalize được (thiếu event chronology).
- **Kalnaovakul, K., et al. (2024).** _JHTI_. [DOI](https://doi.org/10.1108/jhti-06-2024-0591). **Lý do:** moderators chính (brand affiliation, reviewer experience) không có trong dataset.
- **Nhánh Forgiveness/Justice** (Kumar & Shankar 2024, Honora et al. 2024, Wei et al. 2025). **Lý do:** RQ3 không dùng construct forgiveness.

---

## 9. Trạng thái toàn văn — danh sách hành động

Tổng kiểm chứng Round 4: **9 + 9 + 8 = 26**. Thư viện hiện có **35 PDF** trong 8 thư mục (28 cũ + 7 bài tải tay vừa xếp).

**A. Đã tải 16 bài** (9 tự tải + 7 tải tay) — đã xếp vào cụm chức năng; xem link `[Local PDF]` ở các mục 3–5.

**B. Truy cập mở (8 bài): 7 đã tải xong** — Li (SAGE) · Zhang · Das · Tengilimoglu · Leo · Hwang · Biasetton. **Còn 1 bài phải tải tay:**
   1. `10.1177/10963480241230957` — D5 Slevitch → `refs/06_counter_evidence/2024_slevitch_kano_categorization_critique.pdf`
   Link tải trực tiếp: log `0006` mục 7.2 phần B.
   *Kiểm chứng lại 2026-09-23:* `10.1016/j.ipm.2025.104088` (C3 Liu, Ma & Dou) **không truy cập mở** — ScienceDirect chỉ trả abstract + `Purchase PDF`; ResearchGate không có full-text. Đã chuyển sang mục C.

**C. Đóng thật — cần thư viện trường hoặc nhờ giảng viên (9 bài: 11 + 12):**

1. `10.1177/19389655251327536` — D1 Han & Anderson → `06_counter_evidence/` *(ưu tiên 1)*
2. `10.1108/IJCHM-12-2023-1914` — A2 Park et al. → `04_mechanism/`
3. `10.1016/j.ijhm.2023.103647` — D2 Kirilenko et al. → `03_phenomenon/`
4. `10.1016/j.jhtm.2025.01.002` — A5 Cui et al. → `04_mechanism/`
5. `10.1016/j.chb.2024.108550` — C4 Kovács → `03_phenomenon/`
6. `10.1080/1528008X.2024.2410214` — B6 Tan & Zou → `05_boundary_conditions/`
7. `10.1177/14673584251384011` — D6 Mellinas et al. → `06_counter_evidence/` *(thử repository trước: <https://hdl.handle.net/10459.1/469937>)*
8. `10.1007/s11277-024-11457-w` — E5 Kumar et al. → `07_baselines_methods/`
9. `10.1016/j.ipm.2025.104088` — C3 Liu, Ma & Dou → `03_phenomenon/2025_liu_rating_inconsistency_airline.pdf` *(chuyển từ mục B ngày 2026-09-23: kiểm chứng là đóng thật)*

**Cộng 6 nguồn còn thiếu từ Round 3** (vẫn chưa có toàn văn, ghi ở mục tương ứng):

10. `10.1016/j.ijhm.2025.104397` — Kwon, W. (2026), IJHM → mục 4 *(trục lý thuyết RQ3)*
11. `10.1016/j.ijhm.2025.104242` — Albayrak et al. (2025), IJHM → mục 5
12. `10.1016/j.ijhm.2024.104057` — Xu et al. (2025), IJHM → mục 4
13. `10.1016/j.annals.2026.104208` — Zhong et al. (2026), Annals of TR → mục 4
14. `10.1007/s11042-024-19518-9` — Doan et al. (2025), MTAP → mục 7
15. `10.1016/j.dss.2025.114450` — Wang, D. et al. (2025), DSS → mục 3

**Tổng cần lấy: 16 bài** (10 từ Round 4 + 6 từ Round 3). Ba bài trọng yếu để quyết việc đóng khảo sát: **Kwon W.** (mục 4, ưu tiên 1) · **B1 Das** (mục 5, tải bằng trình duyệt) · **D1 Han & Anderson** (mục 6, cần thư viện).

---

## 10. Mẫu bổ sung tài liệu

1. Chọn thư mục theo **chức năng** ở Mục 0, không theo chủ đề.
2. Đặt tên `<năm>_<tác giả chính không dấu>_<chủ đề ngắn>.pdf`.
3. Thêm một dòng vào mục tương ứng: trích dẫn + DOI/publisher + `[Local PDF]` + **vai trò** trong đề tài.
4. Cập nhật bảng số file ở Mục 0.
