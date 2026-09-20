# Agent Guidance & Project Context

Chào mừng bạn đến với dự án nghiên cứu **Customer Sentiment Analysis & Impact of Loyalty on Online Hotel Ratings**. Tài liệu này hướng dẫn cách tiếp cận ngữ cảnh và định vị phạm vi cho các Agent tham gia dự án.

---

## 1. Lĩnh vực Nghiên cứu & Ghi chú về Paper Gốc

* **Lĩnh vực chung (Domain):** Phân tích cảm xúc khía cạnh (Aspect-Based Sentiment Analysis) và mô hình hóa hành vi đánh giá của khách hàng trong ngành khách sạn.
* **Bài toán trọng tâm (Định hướng từ Giảng viên):** Nghiên cứu hiện tượng mâu thuẫn giữa cảm xúc văn bản và điểm số (**Sentiment–Rating Inconsistency**) — giải mã hiện tượng "nói một đằng, chấm một nẻo" (chê phần cứng nhưng vẫn cho 5 sao, hoặc khen nhiều nhưng chỉ vì một sự cố mà chấm 1 sao).
* **Ý tưởng mở rộng của nhóm (Candidate Extension):** Tái định nghĩa biến `Loyalty` của bài báo gốc thành hai thái cực cảm xúc đối nghịch: **Sublimation (Thăng hoa / Vị tha)** và **Anger (Phẫn nộ / Trừng phạt)** đóng vai trò biến điều tiết (Moderator) cho mối quan hệ giữa trải nghiệm dịch vụ và điểm đánh giá.

> **Ghi chú quan trọng về Paper Gốc (Root Paper Reference):**
> * Mọi đề cập đến *"paper gốc"*, *"bài báo gốc"*, hoặc *"root paper"* đều chỉ bài báo:
>   * **Trích dẫn:** Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*. *International Journal of Hospitality Management*, 134, 104574.
>   * **Vị trí file:** `refs/root/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on online_hotel_ratings.pdf`.
>   * **Bản tóm tắt kỹ thuật:** [`refs/root/FACTSHEET.md`](refs/root/FACTSHEET.md) (Agent tra cứu file này, **KHÔNG đọc file PDF 5.4MB**).
>   * **Bản chất bài báo gốc:** Áp dụng khung S-O-R trên 1.3M review (Booking.com & TripAdvisor tại VN) dùng BERTopic + VADER + WMLR để phân 5 khía cạnh (`Facility`, `Amenity`, `Service`, `Experience Value`, `Loyalty`) giải thích cho `CoRe` (Rating $\ge 4$ sao).
>   * **Điểm kế thừa & phản biện:** Kế thừa bộ dữ liệu đối chuẩn; đồng thời chỉ ra lỗi **lập luận vòng (Tautology)** khi dùng từ khóa Loyalty dự đoán Rating để mở ra hướng nghiên cứu mới về **Sự bất nhất (Inconsistency)**.
---

## 2. Định hình Phạm vi Nghiên cứu (Scope)

### Trong phạm vi (In-Scope):

- **Xử lý Ngôn ngữ Tự nhiên (NLP) & Data Mining:**
  - Khai phá khía cạnh đánh giá (Aspect-Based Sentiment Analysis - ABSA) trên dữ liệu review khách sạn tiếng Anh (Booking.com & TripAdvisor).
  - Trích xuất các khía cạnh dịch vụ (`Facility`, `Amenity`, `Service`, `Experience Value`) và cường độ cảm xúc / trạng thái ý định (`Loyalty`, `Delight`, `Anger`).
  - Phát hiện và lượng hóa độ lệch pha (Rating–Text Discrepancy Score) giữa nội dung bài viết và điểm sao thực tế.
- **Mô hình hóa Hành vi & Kinh tế lượng (Econometric Modeling):**
  - Kiểm định cơ chế "tấm đệm" (Buffering Effect) và sự tha thứ của khách hàng dựa trên khung lý thuyết hành vi (S-O-R, Herzberg Two-Factor Theory, Expectancy-Disconfirmation Theory).
  - Ứng dụng các kỹ thuật hồi quy có trọng số (WMLR/Ordered Logit) hoặc mô hình học sâu/học máy để giải thích hành vi chấm điểm.

### Ngoài phạm vi (Out-of-Scope):

- Xây dựng ứng dụng đặt phòng thương mại đầy đủ (Booking engine full-stack) hoặc hệ thống frontend/backend cho người dùng cuối.
- Xử lý đa ngôn ngữ ngoài tiếng Anh trong giai đoạn ban đầu (tập trung vào chuẩn hóa tiếng Anh để đảm bảo chất lượng nhãn).
- Thu thập dữ liệu thời gian thực (Real-time live scraping) khi tập dữ liệu tĩnh ban đầu đã đủ lớn để nghiên cứu học thuật.

---

## 3. Quy tắc Đọc Tài liệu & Tiếp nhận Context (Navigation Protocol)

Mỗi Agent khi bắt đầu phiên làm việc mới chỉ cần đọc lướt theo thứ tự tối giản:

1. **Bước 1 — `docs/INDEX.md`:** Định vị cấu trúc tài liệu.
2. **Bước 2 — `RULES.md`:** Nắm vững các quy tắc giới hạn file, kỷ luật Git và Single Source of Truth.
3. **Bước 3 — `STATUS.md`:** Xem nhanh ảnh chụp hiện trạng dự án ($\le 40$ dòng) và các đầu việc cần làm.
4. **Bước 4 — Không tự ý đọc file PDF gốc và không đọc tràn lan `docs/logs/`**: Chỉ mở file log hoặc factsheet cụ thể khi nhiệm vụ hiện tại yêu cầu.
