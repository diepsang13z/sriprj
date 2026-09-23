# Base Idea Brainstorming

## Analyze root paper

**Thông tin bài báo gốc:**

- **Tên:** _Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings_
- **Tạp chí:** _International Journal of Hospitality Management_ 134 (2026) 104574.
- **Bộ dữ liệu:** Hơn 1.3 triệu review tiếng Anh từ Booking.com (607k) và TripAdvisor (782k) tại hơn 13.000 khách sạn ở Việt Nam; kèm tập gán nhãn thủ công (15.7k TripAdvisor, 6.9k Booking).

### 1. Paper giải quyết bài toán gì và đóng góp gì?

- **Bài toán:** Khai phá tri thức từ lượng lớn review phi cấu trúc; lượng hóa tác động của các khía cạnh dịch vụ và lòng trung thành (Loyalty) lên điểm đánh giá số (Rating); đưa khung lý thuyết hành vi người tiêu dùng vào text mining thay vì dự đoán máy học thuần túy.
- **Khung lý thuyết S–O–R (Stimulus – Organism – Response):**
  - **Stimulus ($S$):** Các kích thích môi trường/dịch vụ khách quan gồm `Facility` (cơ sở vật chất), `Amenity` (tiện ích, vị trí), `Service` (dịch vụ, con người).
  - **Organism ($O$):** Trạng thái nhận thức/tình cảm nội tại gồm `Experience Value` (cảm nhận giá trị/chi phí) và `Loyalty` (ý định gắn bó/tái ghé thăm).
  - **Response ($R$):** Biểu hiện hành vi thông qua `CoRe` (Customer Rating regression) – điểm số đánh giá thực tế của khách hàng được phân đôi (Satisfied vs. Dissatisfied), được tác giả lý thuyết hóa như thước đo định lượng của Giá trị thương hiệu số (Customer-Based Brand Equity - CBBE).
- **Phương pháp thực hiện (Pipeline):**
  - Tiền xử lý & tách câu $\rightarrow$ Khám phá chủ đề sâu bằng **BERTopic** (~100 cụm) $\rightarrow$ Gom thành 5 khía cạnh bằng **SentenceBERT + c-TF-IDF** $\rightarrow$ Gán nhãn cảm xúc cấp câu (Positive, Neutral, Negative) bằng **VADER** kết hợp **Human validation** $\rightarrow$ Chạy mô hình hồi quy **Weighted Multinomial Logistic Regression (WMLR)** để xử lý lệch nhãn.
- **Ý nghĩa quản trị của 5 khía cạnh trong khách sạn:**
  - `Facility` (Cơ sở vật chất): Chiếm ~70% dung lượng review, là yếu tố sống còn (Hygiene factor). $FacilityNegative$ phạt điểm cực nặng ($\beta \approx -1.08$ Booking, $-1.17$ TripAdvisor) $\rightarrow$ Cần đầu tư CapEx, bảo trì định kỳ.
  - `Amenity` (Tiện ích, vị trí): Yếu tố cố định, tác động đến điểm số thấp nhất $\rightarrow$ Dùng để tiếp thị ban đầu, cần bù đắp bằng dịch vụ đưa đón nếu vị trí xa.
  - `Service` (Dịch vụ, nhân viên): Yếu tố con người linh hoạt, dễ chạm đến cảm xúc $\rightarrow$ Là phao cứu sinh gỡ gạc trải nghiệm khi phần cứng có lỗi.
  - `Experience Value` (Giá trị cảm nhận): Đánh giá tương quan giá cả và sự trung thực của ảnh phòng quảng cáo vs. thực tế $\rightarrow$ Quản trị kỳ vọng, tránh quảng cáo quá đà.
  - `Loyalty` (Lòng trung thành / Ý định gắn kết): Đại sứ thương hiệu, đo lường sức khỏe thương hiệu dài hạn.

### 2. Vấn đề nhãn thứ 6 "Branding" trong dataset (`TripAdvisor_EN.json`)

- Trong dữ liệu gán nhãn thực tế (`TripAdvisor_EN.json`), ngoài 5 khía cạnh trên còn xuất hiện **1.339 spans gán nhãn `Branding`**.
- **Bản chất các câu gán nhãn `Branding`:**
  - Khách tự chấm điểm bằng chữ: _"The hotel is sure 5 stars"_, _"So i would give golden sun palace hotel 5 star"_, _"I would personally rate 2 stars"_.
  - Nhận xét về danh tiếng thương hiệu / ảnh quảng cáo vs. thực tế: _"It looked exactly like the photos"_, _"The pictures online were too nice for the actual hotel"_.
- **Tại sao paper gốc loại bỏ `Branding` khỏi mô hình?**
  1. **Nguy cơ Rò rỉ dữ liệu (Data Leakage):** Khách tự nói thẳng số sao họ chấm bằng lời trong câu. Nếu đưa vào làm biến độc lập $X$ để dự đoán điểm $R$ ($CoRe$) thì mô hình sẽ "nhìn trộm đáp án".
  2. **Xung đột khung S–O–R:** Tác giả đã nâng cấp `CoRe` thành đại diện cho Brand Equity ($R$), nếu để một biến độc lập là `Branding` ở vế $S$ hay $O$ sẽ gây nhập nhằng khái niệm.
  3. **Đặc tính trích xuất:** BERTopic không gom được cụm từ vựng riêng cho Branding; các từ ngữ ảnh/kỳ vọng đã bị sáp nhập vào `Experience Value`.

### 3. Các lỗi phương pháp luận & Lỗ hổng của paper gốc

1. **Lập luận vòng (Circular Reasoning / Tautology) ở biến `Loyalty`:**
   - Tác giả định nghĩa `Loyalty` bằng các từ khóa ý định hành vi: _revisit, recommend, come back_ (`LoyalPositive`) vs. _stay away, never again, avoid_ (`LoyalNegative`).
   - Tác giả đưa các biến này vào để giải thích cho `CoRe` (bấm 1 sao hay 5 sao) và kết luận: _"Loyalty là yếu tố có tác động mạnh nhất lên Rating"_.
   - **Bản chất:** Việc một khách hàng tức giận gõ _"stay away, never again"_ và việc họ _bấm 1 sao_ là **cùng một hành vi trút giận (co-occurring emotional response)** tại cùng thời điểm. Lấy biểu hiện bằng chữ giải thích cho biểu hiện bằng số là ngụy biện lặp thừa, không mang giá trị nhân quả thực tiễn.
2. **Giả định quan hệ phẳng tuyến tính, bỏ qua sự bất nhất (Inconsistency):**
   - Mô hình giả định: Cứ tích cực là điểm tăng, tiêu cực là điểm giảm đồng đều.
   - Bỏ qua các trường hợp mâu thuẫn thực tế: Khách chê tơi bời cơ sở vật chất (Negative Facility) nhưng vẫn bấm 5 sao; hoặc khách khen nhân viên và đồ ăn nhưng chỉ vì một trải nghiệm tồi tệ lúc trả phòng mà chấm 1 sao.
3. **Chưa phân biệt giữa Khía cạnh dịch vụ (Aspect) và Cường độ cảm xúc (Emotional Intensity):**
   - Việc gom `Loyalty` thành aspect ngang hàng với `Facility`, `Service` gây nhiễu phạm trù. Những câu mang tính cực đoan như "chắc chắn quay lại" hay "cạch mặt" thực chất là **Thăng hoa (Sublimation/Delight)** hoặc **Phẫn nộ (Anger/Rage)**.

> **Note: Thảo luận về ý tưởng tách `Loyalty` thành `Sublimation` (Thăng hoa) và `Anger` (Phẫn nộ)**
>
> * **Điểm hợp lý về mặt tâm lý học hành vi:** Các phát ngôn gắn nhãn `Loyalty` trong paper gốc (*"stay away, never again"* vs. *"definitely return, highly recommend"*) thực chất là biểu hiện của hai cực cảm xúc tột cùng:
>   * **Anger / Rage (Phẫn nộ):** Cảm xúc ức chế bùng phát, thôi thúc hành vi trừng phạt khách sạn (bấm 1 sao, kêu gọi tẩy chay).
>   * **Sublimation / Delight (Thăng hoa):** Trải nghiệm vượt mong đợi, thôi thúc hành vi khen ngợi tuyệt đối và tự nguyện làm đại sứ thương hiệu (bấm 5 sao).
> * **Tại sao không nên đổi trực tiếp thành 2 Aspect ngang hàng:**
>   * *Lỗi sai phạm trù (Category Mistake):* Trong ABSA, **Aspect** là đối tượng phục vụ (khách nói về *cái gì*: phòng, đồ ăn, nhân viên), còn **Emotion** là trạng thái nội tâm (khách cảm thấy *như thế nào*). Đặt chúng ngang hàng sẽ bị sai lệch về bản thể luận (ontology).
>   * *Vẫn vướng lập luận vòng:* Nếu coi Anger là một aspect thì việc Anger dẫn tới 1 sao hay Sublimation dẫn tới 5 sao vẫn là tương quan 1:1 hiển nhiên.
> * **Định vị chuẩn xác cho đề tài mới:** Tách thành **2 trục độc lập**:
>   1. **Trục 4 Khía cạnh khách quan (Core Aspects):** `Facility`, `Service`, `Amenity`, `Experience Value`.
>   2. **Trục Cường độ cảm xúc / Biến điều tiết (Emotional Tone / Moderator):**
>      * *Có Negative Facility nhưng KHÔNG có Anger (Mild tone):* Khách vị tha, xem lỗi là nhỏ, rating vẫn giữ **5 sao** $\rightarrow$ Giải thích hiện tượng **Positive Inconsistency** (Tha thứ).
>      * *Có Negative Facility và KÍCH HOẠT Anger:* Sự bực bội vượt ngưỡng chịu đựng, rating bị trừng phạt về **1–2 sao** $\rightarrow$ Giải thích cơ chế sụt giảm điểm số.
## Hướng nghiên cứu: Sentiment–Rating Inconsistency

Đây là hướng rất thú vị về cả AI lẫn hospitality research.

### 1. Hiện tượng trong dữ liệu

Trong paper gốc, ta có hiện tượng: **5 stars + Negative aspect**.

**Ví dụ Review:**

> _"Fantastic hotel, would definitely return, but the room was a little noisy."_ — **Rating: 5/5**

- `Experience` $\rightarrow$ Positive
- `Loyalty` $\rightarrow$ Positive
- `Facility` $\rightarrow$ Negative

Trong dataset có **394 review rating 5** nhưng vẫn chứa negative span (số này trước 2026-09-23 ghi **402**; sửa theo [`RDR-0006`](../../decisions/RDR-0006_freeze_negative_span_definition.md)). Ngược lại, với low-rating review đôi khi chứa positive aspects.

### 2. Định nghĩa toán học

Có thể định nghĩa:
$$D = f(\text{rating}, \text{aspect sentiments})$$
với $D$ là _rating–text discrepancy score_.

### 3. Research Questions (Câu hỏi nghiên cứu)

- Khi nào negative aspect không đủ làm giảm overall rating?
- Aspect nào khách hàng “tha thứ” nhiều nhất?
- Negative sentiment nào ở Facility, Service, Amenity hay Loyalty làm rating giảm mạnh nhất?
- Loyalty có đóng vai trò “buffer” cho negative service experience không?

### 4. Giá trị hướng đi

- Đây là hướng rất phù hợp để kết nối: **NLP + Consumer behavior + Hospitality**.
- Tránh sự vòng tròn khá rõ của paper cũ khi dùng “recommend/return” rồi kết luận loyalty tương quan mạnh với rating.
