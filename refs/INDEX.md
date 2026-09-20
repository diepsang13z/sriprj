# Reference Literature Index (refs/INDEX.md)

Danh mục toàn bộ các bài báo khoa học, tài liệu học thuật và nghiên cứu nền tảng được sử dụng trong dự án.

---

## 1. Root Paper (Bài báo nền tảng)
* **Factsheet đọc nhanh (Dành cho Agent):** [`refs/root/FACTSHEET.md`](root/FACTSHEET.md) *(Đọc file này thay vì đọc file PDF 5.4MB)*.
* **File gốc:** [`refs/root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on online_hotel_ratings.pdf`](root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on%20online_hotel_ratings.pdf)
* **Trích dẫn:** Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*. International Journal of Hospitality Management, 134, 104574.
* **Vai trò trong dự án:** Bài báo gốc cung cấp khung tiếp cận S-O-R, pipeline BERTopic + WMLR trên 1.3M review và dataset đối chuẩn. Dự án kế thừa, tái lập và chỉ ra lỗi ngụy biện vòng lặp để mở rộng sang bài toán Bất nhất cảm xúc - điểm số.
---

## 2. Inconsistency & Related Literature (Bài báo đối chứng & Mở rộng)

### A. Nghiên cứu về Bất nhất giữa Điểm số và Văn bản (Score-Textual Inconsistency)

- **File:** [`refs/2025_beyond_the_stars_Unpacking_the_impact_of_score-textual_inconsistency_of_online_reviews_on_hotel_performance.pdf`](2025_beyond_the_stars_Unpacking_the_impact_of_score-textual_inconsistency_of_online_reviews_on_hotel_performance.pdf)
- **Tiêu đề:** _Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance_ (2025).
- **Vai trò:** Cung cấp cơ sở lý thuyết về tác động của sự bất nhất (lệch pha giữa sao và chữ) lên hiệu quả kinh doanh của khách sạn; tài liệu then chốt cho đề tài mới.

### B. Nghiên cứu về Dự đoán Cảm xúc và Điểm số (Sentiment & Rating Prediction)

- **File:** [`refs/2022_predicting_sentiment_and_rating_of_tourist_reviews_using_machine_learning.pdf`](2022_predicting_sentiment_and_rating_of_tourist_reviews_using_machine_learning.pdf)
- **Trích dẫn:** Puh, K., & Bagić Babac, M. (2023). _Predicting sentiment and rating of tourist reviews using machine learning_. Journal of Hospitality and Tourism Insights, 6(3), 1188–1204.
- **Vai trò:** Nghiên cứu máy học dự đoán đồng thời cảm xúc và rating; cung cấp baseline và tiêu chuẩn phân loại điểm số hài lòng/không hài lòng.

---

## 3. Cấu trúc Bổ sung Tài liệu Tương lai (Template)

Khi bổ sung bài báo mới vào thư mục `refs/`, cập nhật mục này theo mẫu:

```markdown
- **File:** `refs/<năm>_<tiêu_đề_ngắn>.pdf`
- **Trích dẫn:** Tác giả (Năm). Tên bài báo. Tạp chí, Tập(Số), Trang.
- **Chủ đề:** (Topic Modeling / ABSA / Buffering Effect / Two-Factor Theory)
- **Đóng góp cho dự án:** (Tóm tắt 1-2 câu về vai trò hoặc giá trị đối chứng)
```
