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
* **Phương trình Booking.com:**
  $$\log(CoRe) = 1.9179 + \mathbf{2.7410} LoyalPos - 1.6632 LoyalNeg + 1.1748 ExpPos - 1.0367 ExpNeg + 0.8956 ServPos - 0.8586 ServNeg + 0.8424 FacPos - \mathbf{1.0778} FacNeg + \dots$$
* **Phương trình TripAdvisor:**
  $$\log(CoRe) = 0.9143 + \mathbf{1.7844} LoyalPos - \mathbf{2.0086} LoyalNeg - \mathbf{1.1661} FacNeg - \mathbf{1.1069} ServNeg + \dots$$
* **Quy luật phát hiện:**
  1. Biến Loyalty có hệ số $|\beta|$ lớn nhất.
  2. $FacilityNegative$ có hệ số phạt điểm nặng thứ 2 (Hygiene factor).
  3. Cảm xúc tiêu cực phạt điểm nặng hơn cảm xúc tích cực kéo điểm lên (Tính bất đối xứng).

---

## 5. Các lỗ hổng lý thuyết (Cơ sở mở rộng đề tài)
1. **Lập luận vòng (Tautology) ở biến Loyalty:** Định nghĩa Loyalty bằng từ khóa ý định (*"stay away"* $\rightarrow$ 1 sao; *"come back"* $\rightarrow$ 5 sao) rồi kết luận Loyalty quyết định Rating $\rightarrow$ ngụy biện lặp thừa, thiếu giá trị nhân quả.
2. **Loại bỏ nhãn thứ 6 `Branding`:** 1.339 span gán nhãn `Branding` trong dataset (tự chấm sao, so sánh ảnh vs thực tế) bị loại bỏ để tránh rò rỉ dữ liệu (Data leakage).
3. **Bỏ qua hiện tượng Bất nhất (Sentiment–Rating Inconsistency):** 
   * Có ít nhất **402 review rating 5 sao** nhưng vẫn chứa các span tiêu cực (*Negative Facility*).
   * Chưa giải thích được cơ chế tha thứ: Yếu tố nào (`Service` hay `Emotional connection`) đóng vai trò "tấm đệm" (Buffer) bảo vệ điểm số 5 sao.
