# Root Paper Factsheet & Ground Truth

> **Dành cho Agent:** Đọc file này thay vì mở file PDF 5.4MB để tra cứu nhanh thông số, phương trình và phát hiện của paper gốc.

---

## 1. Thông tin thư mục
* **Tên bài báo:** *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*
* **Tác giả:** Hanh Thi My Le, Thang Quyet Nguyen, Binh T. Nguyen (2026).
* **Tạp chí:** *International Journal of Hospitality Management* 134, 104574.
* **Bộ dữ liệu:** 1.39 triệu reviews (>13.000 khách sạn tại Việt Nam):
  * Booking.com: 607.451 reviews (902.425 câu).
  * TripAdvisor: 782.584 reviews (3.287.307 câu).
  * Gold standard (nhãn chuyên gia): 6.955 Booking + 15.741 TripAdvisor reviews.

---

## 2. Khung lý thuyết: S–O–R Framework
* **Stimulus ($S$):** `Facility` (chiếm ~70% dung lượng bình luận), `Amenity` (~5-7%), `Service` (~10-12%).
* **Organism ($O$):** `Experience Value` (giá trị/giá tiền, ảnh quảng cáo vs. thực tế), `Loyalty` (ý định quay lại/giới thiệu).
* **Response ($R$):** `CoRe` (Customer Rating regression nhị phân hóa: TripAdvisor $\ge 4$ sao; Booking $\ge 7$ điểm).

---

## 3. Pipeline Kỹ thuật
1. Lọc tiếng Anh & tách câu (Sentence segmentation).
2. Trích xuất chủ đề bằng **BERTopic** (~100 cụm chủ đề).
3. Gom cụm về 5 khía cạnh bằng **SentenceBERT + c-TF-IDF** (khoảng cách Cosine trọng số).
4. Phân loại cảm xúc cấp câu (Positive, Neutral, Negative) bằng **VADER compound score**.
5. Hồi quy Logistic đa thức có trọng số **WMLR** (cân bằng lớp thiểu số Dissatisfied).

---

## 4. Kết quả Thực nghiệm & Phương trình Hồi quy
* **McFadden Pseudo $R^2$:** 0.4617 (Booking.com), 0.5898 (TripAdvisor).
* **Phương trình Booking.com (Eq. 2a - p < 0.05):**
  $$\log(CoRe) = 1.9179 + \mathbf{2.7410} LoyalPos - 1.6632 LoyalNeg + 1.1748 ExpPos - 1.0367 ExpNeg + 0.8956 ServPos - 0.8586 ServNeg + 0.8424 FacPos - \mathbf{1.0778} FacNeg + 0.4150 AmenityPos - 0.4854 AmenityNeg$$
  *(Trên Booking.com, toàn bộ các biến Neutral đều không có ý nghĩa thống kê $p > 0.05$ nên bị loại khỏi phương trình)*.
* **Phương trình TripAdvisor (Eq. 2b - p < 0.05):**
  $$\begin{aligned}
  \log(CoRe) = 0.9143 &+ \mathbf{1.7844} LoyalPos - \mathbf{2.0086} LoyalNeg \\
  &+ 0.8229 ServPos - 0.7224 ServNeu - \mathbf{1.1069} ServNeg \\
  &+ 0.7121 ExpPos - 0.5466 ExpNeu - 0.9516 ExpNeg \\
  &+ 0.4459 FacPos - 0.5403 FacNeu - \mathbf{1.1661} FacNeg \\
  &+ 0.2692 AmenityPos - 0.6887 AmenityNeg
  \end{aligned}$$
* **Quy luật phát hiện:**
  1. **Biến Loyalty có hệ số $|\beta|$ lớn nhất** ($2.7410$ trên Booking, $-2.0086$ trên TripAdvisor).
  2. **$FacilityNegative$ có hệ số phạt điểm nặng thứ 2** sau Loyalty ($\beta = -1.0778$ trên Booking, $-1.1661$ trên TripAdvisor) $\rightarrow$ Đóng vai trò Hygiene factor sống còn.
  3. **Tính bất đối xứng (Negativity Bias):** Cảm xúc tiêu cực phạt điểm nặng hơn cảm xúc tích cực kéo điểm lên ($|ServNeg| > ServPos$, $|FacNeg| > FacPos$, $|AmenityNeg| > AmenityPos$).
  4. **Hiệu ứng phạt của phản hồi trung tính (Neutral Penalty trên TripAdvisor):** Trên TripAdvisor, thái độ trung tính ở Service ($-0.7224$), Experience ($-0.5466$), Facility ($-0.5403$) đều có ý nghĩa thống kê và đều mang hệ số âm kéo tụt điểm đánh giá đáng kể (khách hàng xem neutral là chưa đạt kỳ vọng).
---

## 5. Các lỗ hổng lý thuyết & Đóng góp phản biện (Cơ sở mở rộng đề tài)
> **Lưu ý quan trọng:** Đây là **phân tích phản biện độc lập (Critical Appraisal)** và phát hiện từ EDA tập dữ liệu gán nhãn gốc (`TripAdvisor_EN.json` từ GitHub `Hanhlevna/Manhos` của tác giả) do nhóm dự án thực hiện, **không phải nội dung bài báo gốc tự thừa nhận**.

1. **Lập luận vòng (Tautology) ở biến Loyalty:** Định nghĩa Loyalty bằng từ khóa ý định hành vi (*"stay away, never again"* $\rightarrow$ 1 sao; *"come back, highly recommend"* $\rightarrow$ 5 sao) rồi đưa vào hồi quy kết luận Loyalty quyết định Rating $\rightarrow$ Biểu hiện bằng lời và hành vi chấm sao là phản ứng đồng thời (co-occurring response), việc dùng từ ngữ giải thích cho điểm số là ngụy biện lặp thừa, thiếu giá trị nhân quả.
2. **Loại bỏ nhãn thứ 6 `Branding`:** Khảo sát tập nhãn `TripAdvisor_EN.json` cho thấy có **1.339 spans gán nhãn `Branding`** (khách tự chấm số sao bằng lời: *"give 5 star"*, hoặc so sánh ảnh vs thực tế) nhưng bị tác giả loại bỏ khỏi mô hình để tránh rò rỉ dữ liệu (Data leakage) và xung đột khung S–O–R.
3. **Bỏ qua hiện tượng Bất nhất (Sentiment–Rating Inconsistency):** 
   * Khảo sát dữ liệu phát hiện ít nhất **402 reviews rating 5 sao** nhưng vẫn chứa các span tiêu cực (*Negative Facility*).
   * Mô hình tuyến tính của paper chưa giải thích được cơ chế tha thứ: Yếu tố nào (`Service` hay `Emotional connection`) đóng vai trò "tấm đệm" (Buffer) bảo vệ điểm số 5 sao trước các phàn nàn cơ sở vật chất.
