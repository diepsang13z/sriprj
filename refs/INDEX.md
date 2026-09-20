# Reference Literature Index (refs/INDEX.md)

Danh mục toàn bộ các bài báo khoa học, tài liệu học thuật và nghiên cứu nền tảng được sử dụng trong dự án.

---

## 1. Root Paper (Bài báo nền tảng)
* **Factsheet đọc nhanh (Dành cho Agent):** [`refs/root/FACTSHEET.md`](root/FACTSHEET.md) *(Tóm tắt thông số cốt lõi, phương trình và phân tích phản biện)*.
* **Toàn văn Markdown đầy đủ (Dành cho Agent):** [`refs/root/FULL_PAPER.md`](root/FULL_PAPER.md) *(Trích xuất 100% nguyên văn toàn bộ 15 trang bài báo: text, bảng biểu, công thức LaTeX, trích dẫn)*.
* **File gốc:** [`refs/root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on online_hotel_ratings.pdf`](root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on%20online_hotel_ratings.pdf)
* **Trích dẫn:** Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*. International Journal of Hospitality Management, 134, 104574.
* **Vai trò trong dự án:** Bài báo gốc cung cấp khung tiếp cận S-O-R, pipeline BERTopic + WMLR trên 1.3M review và dataset đối chuẩn. Dự án kế thừa, tái lập và chỉ ra lỗi ngụy biện vòng lặp để mở rộng sang bài toán Bất nhất cảm xúc - điểm số.
---

## 2. Inconsistency & Related Literature

### A. Score–Textual Inconsistency

- **Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025).** _Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance_. *International Journal of Hospitality Management, 130*, 104271. [DOI](https://doi.org/10.1016/j.ijhm.2025.104271). [Local PDF](2025_beyond_the_stars_Unpacking_the_impact_of_score-textual_inconsistency_of_online_reviews_on_hotel_performance.pdf). **Vai trò:** directional polarity mismatch và hotel-level inconsistency proportion.
- **Almansour, A., Alotaibi, R., & Alharbi, H. (2022).** _Text-rating review discrepancy (TRRD): An integrative review and implications for research_. *Future Business Journal, 8*, 3. [DOI](https://doi.org/10.1186/s43093-022-00114-y). **Vai trò:** định nghĩa TRRD và cảnh báo dùng rating làm sentiment label.
- **Bigne, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023).** _Are customer star ratings and sentiments aligned?_ *Service Business, 17*, 281–314. [DOI](https://doi.org/10.1007/s11628-023-00524-0). **Vai trò:** compensatory/cancel-out effect giữa positive và negative aspect sentiments.
- **Valdivia, A., et al. (2019).** _Inconsistencies on TripAdvisor reviews: A unified index between users and sentiment analysis methods_. *Neurocomputing, 353*, 3–16. [DOI](https://doi.org/10.1016/j.neucom.2018.09.096). **Vai trò:** ứng viên unified continuous index; cần đọc full text để trích công thức.
- **Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025).** _Unravelling the effects of two inconsistencies on online review helpfulness: Evidence from TripAdvisor_. *Decision Support Systems, 193*, 114450. [DOI](https://doi.org/10.1016/j.dss.2025.114450). **Vai trò:** phân biệt review inconsistency và rating inconsistency; full-text verification còn thiếu.

### B. Hospitality Sentiment Analysis / ABSA

- **Ameur, A., Hamdi, S., & Ben Yahia, S. (2024).** _Sentiment analysis for hotel reviews: A systematic literature review_. *ACM Computing Surveys, 56*(2), 1–38. [DOI](https://doi.org/10.1145/3605152). **Vai trò:** bản đồ preprocessing, representation, model và dataset.
- **Doan, T. T., et al. (2025).** _HOSSemEval-EB23: A robust dataset for aspect-based sentiment analysis of hospitality reviews_. *Multimedia Tools and Applications, 84*, 13057–13087. [DOI](https://doi.org/10.1007/s11042-024-19518-9). **Vai trò:** benchmark dataset/model cho aspect-level hospitality sentiment.
- **Puh, K., & Bagić Babac, M. (2023).** _Predicting sentiment and rating of tourist reviews using machine learning_. *Journal of Hospitality and Tourism Insights, 6*(3), 1188–1204. [DOI](https://doi.org/10.1108/JHTI-02-2022-0078). [Local PDF](2022_predicting_sentiment_and_rating_of_tourist_reviews_using_machine_learning.pdf). **Vai trò:** baseline text→rating; không phải phép đo discrepancy độc lập.

### C. Forgiveness, Justice, and Buffering

- **Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025).** _Consumer forgiveness: A literature review and research agenda_. *Psychology & Marketing, 42*(2), 554–578. [DOI](https://doi.org/10.1002/mar.22138). **Vai trò:** systematic synthesis của 89 nghiên cứu forgiveness.
- **Kumar, A., & Shankar, A. (2024).** _Why do consumers forgive online travel agencies? A multi-study approach_. *Australasian Marketing Journal, 32*(4), 323–338. [DOI](https://doi.org/10.1177/14413582231194071). **Vai trò:** nối S-O-R, Justice Theory, forgiveness và repatronage trong OTA context.
- **Honora, A., Wang, K.-Y., & Chih, W.-H. (2024).** _The role of customer forgiveness and perceived justice in restoring relationships with customers_. *Service Business, 18*, 363–393. [DOI](https://doi.org/10.1007/s11628-024-00563-1). **Vai trò:** perceived justice như cơ chế buffer giữa failure severity và forgiveness.

### D. Survey Synthesis

- [`docs/logs/literature-survey/0002_survey_matrix_round_1.md`](../docs/logs/literature-survey/0002_survey_matrix_round_1.md) — Search protocol, evidence matrix, cross-paper tensions, gap analysis và endpoint check của vòng khảo sát đầu tiên.

## 3. Cấu trúc Bổ sung Tài liệu Tương lai (Template)

Khi bổ sung bài báo mới vào thư mục `refs/`, cập nhật mục này theo mẫu:

```markdown
- **File:** `refs/<năm>_<tiêu_đề_ngắn>.pdf`
- **Trích dẫn:** Tác giả (Năm). Tên bài báo. Tạp chí, Tập(Số), Trang.
- **Chủ đề:** (Topic Modeling / ABSA / Buffering Effect / Two-Factor Theory)
- **Đóng góp cho dự án:** (Tóm tắt 1-2 câu về vai trò hoặc giá trị đối chứng)
```
