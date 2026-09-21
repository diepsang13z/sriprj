# Kịch bản Thuyết trình Báo cáo Tiến độ Dự án (DAP391m)
## Đề tài: Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews
**Thời lượng dự kiến:** 10 – 12 phút (mỗi bạn ~3.5 – 4 phút)  
**Tài liệu trình chiếu:** `project_overview_post_survey.pptx` (hoặc `project_overview_post_survey_vi.pptx`)  
**Phân bổ:** 3 thành viên (Speaker 1, Speaker 2, Speaker 3)

---

## Phân công Tổng quan

| Người trình bày | Phạm vi Slide | Nội dung trọng tâm | Thời lượng |
|---|---|---|---|
| **Speaker 1** | Slide 1 – 4 | Bối cảnh bài toán, Hiện tượng thực tế trên dữ liệu & Phản biện bài báo gốc | ~3.5 phút |
| **Speaker 2** | Slide 5 – 8 | Kết quả 2 vòng khảo sát văn hiến, Bức tranh đo lường & Khoảng trống lý thuyết | ~4.0 phút |
| **Speaker 3** | Slide 9 – 13 (14) | 3 RQs đề xuất, Kế hoạch kiểm định có đối chứng, Trạng thái trung thực & Xin ý kiến Thầy | ~4.0 phút |

---

## CHI TIẾT KỊCH BẢN THUYẾT TRÌNH

```
================================================================================
PHẦN 1: BỐI CẢNH, HIỆN TƯỢNG VÀ BÀI BÁO GỐC (Speaker 1 — ~3.5 phút)
================================================================================
```

### [Slide 1] Cover: When Reviews and Ratings Disagree
* **Lời thoại:**
  > *"Kính chào Thầy và các bạn. Hôm nay, nhóm chúng em xin báo cáo tổng quan tiến độ dự án và kết quả đạt được sau hai vòng khảo sát văn hiến.*
  > 
  > *Đề tài nhóm đang theo đuổi có tên làm việc là: **Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews** — nghiên cứu hiện tượng mâu thuẫn giữa cảm xúc văn bản và điểm sao ở cấp khía cạnh trong ngành khách sạn.*
  > 
  > *Trong các hệ thống review trực tuyến, một khách hàng thể hiện trải nghiệm qua hai kênh đồng thời: viết bài nhận xét và chấm số sao. Hầu hết các nghiên cứu trước đây mặc định hai tín hiệu này luôn đồng nhất. Nhưng thực tế, có một tỷ lệ không nhỏ khách hàng 'nói một đằng, chấm một nẻo'. Nhóm chúng em chọn chính những trường hợp bất nhất này làm đối tượng nghiên cứu cốt lõi."*

---

### [Slide 2] Progress Snapshot: Dự án trong một phút
* **Lời thoại:**
  > *"Để Thầy nắm nhanh bức tranh tổng thể, đây là snapshot hiện trạng của nhóm:*
  > 
  > *1. Nhóm đã hoàn thành **2 vòng khảo sát văn hiến** theo chính sách ưu tiên bài mới nhất (trong 36 tháng qua), thu thập và phân loại **15 bài báo hạt nhân** cùng 3 bài watchlist kỹ thuật.*  
  > *2. Nhóm đã audit trực tiếp trên tập dữ liệu con **9.990 review tiếng Anh** kế thừa từ tác giả bài gốc, phát hiện **404 review 5 sao có chứa đoạn văn tiêu cực** và **199 review 1–2 sao có chứa đoạn văn tích cực**.*  
  > *3. Về tiến độ, nhóm đã đi qua 3 bước đầu: Khảo sát, Xác định gap và Thiết lập quy chuẩn gán nhãn. Cổng hiện tại của nhóm là chuẩn bị bước vào **Validation thực nghiệm** trên dữ liệu để chọn ra công thức đo bất nhất tối ưu trước khi ban hành Quyết định Kiến trúc RDR-0003."*

---

### [Slide 3] The Phenomenon: Vì sao khớp từ khóa là chưa đủ?
* **Lời thoại:**
  > *"Để minh họa rõ hiện tượng, slide này đưa ra hai ví dụ trích xuất trực tiếp từ dataset:*
  > 
  > * Ở ví dụ bên trái, khách chấm **5 sao** nhưng bài viết có đoạn tiêu cực về cửa phòng bị hỏng. Tuy nhiên, ngữ cảnh chỉ ra khách sạn đã lập tức đổi phòng tương đương — đây là minh chứng của **Service Recovery**, dịch vụ phục vụ tốt đã đóng vai trò 'tấm đệm' (buffering) bảo vệ điểm 5 sao.*  
  > * Ở ví dụ bên phải, khách chấm **2 sao** dù có khen nhân viên thân thiện, nhưng phòng bẩn và điều hòa ồn nghiêm trọng. Đây là trường hợp trải nghiệm hỗn hợp (mixed experience), điểm 2 sao vẫn là hợp lý chứ không phải khách trừng phạt vô lý.*
  > 
  > *Bài học rút ra: **Chỉ quét từ khóa tiêu cực không thể kết luận một review là bất nhất**. Chúng ta bắt buộc phải có nhãn người để phân tách giữa bất nhất thật, trải nghiệm bù trừ, dịch vụ khắc phục và lỗi gán nhãn."*

---

### [Slide 4] Baseline & Limitation: Điểm xuất phát từ Bài báo gốc (2026)
* **Lời thoại:**
  > *"Nền tảng của nhóm xuất phát từ bài báo công bố năm 2026 trên IJHM của tác giả Lê Thị Mỹ Hạnh và cộng sự, chạy trên 1.39 triệu review với pipeline BERTopic, SBERT, VADER và hồi quy WMLR.*
  > 
  > *Sau khi nghiên cứu kỹ factsheet và dữ liệu, nhóm kế thừa pipeline và bộ dữ liệu đối chuẩn, đồng thời chỉ ra **hai điểm phản biện mang tính học thuật** để mở rộng đề tài:*
  > 
  > * *Thứ nhất là rủi ro lập luận vòng (Tautology) ở biến Loyalty:* Dùng từ ngữ ý định hành vi ('recommend' / 'never again') để giải thích cho điểm sao trong cùng một review là giải thích một phản ứng đồng thời, thiếu giá trị nhân quả.*  
  > * *Thứ hai là bỏ qua hiện tượng bất nhất:* Khung tuyến tính của bài gốc mặc định cứ khen là điểm cao, chê là điểm thấp, nên không giải thích được vì sao phàn nàn về cơ sở vật chất vẫn có thể đi kèm 5 sao.*
  > 
  > *Mục tiêu của nhóm là: **Giải thích sự bất nhất này, chứ không coi nó là nhiễu để xóa đi**.*
  > 
  > *Sau đây, em xin nhường lời cho bạn [Tên Speaker 2] trình bày chi tiết về kết quả khảo sát văn hiến."*

```
================================================================================
PHẦN 2: KẾT QUẢ KHẢO SÁT VĂN HIẾN & KHOẢNG TRỐNG (Speaker 2 — ~4.0 phút)
================================================================================
```

### [Slide 5] Literature Survey Map: Khảo sát văn hiến đã bao phủ những gì
* **Lời thoại:**
  > *"Cảm ơn bạn [Speaker 1]. Kính thưa Thầy, để giải quyết bài toán trên một cách bài bản, nhóm đã thực hiện 2 vòng khảo sát văn hiến theo Quyết định RDR-0001 và RDR-0002, quét trong cửa sổ 36 tháng gần nhất.*
  > 
  > *Tập tài liệu hạt nhân 15 bài được chia đều vào **3 cụm bằng chứng** tương hỗ:*
  > 
  > * *Cụm 1 (7 bài) về Bất nhất review:* Định nghĩa bài toán, phân loại chiều và các họ công thức đo lường.*  
  > * *Cụm 2 (3 bài) về Hospitality ABSA:* Các benchmark trích xuất khía cạnh, phân tích cảm xúc và baseline dự đoán điểm.*  
  > * *Cụm 3 (5 bài) về Tâm lý học và Hành vi:* Các lý thuyết về sự tha thứ, cảm xúc phẫn nộ, công bằng và hiệu ứng tấm đệm.*
  > 
  > *Hiện tại nhóm đã chạm trần 15 bài hạt nhân và tạm dừng tìm kiếm diện rộng (broad search), vì mọi câu hỏi còn lại đều thuộc về kiểm định thực nghiệm trên dữ liệu."*

---

### [Slide 6] Survey Finding #1: Bất nhất là tín hiệu, không phải nhiễu
* **Lời thoại:**
  > *"Từ 15 bài báo, nhóm rút ra **Kết quả khảo sát #1**: Hiện tượng bất nhất là một tín hiệu hành vi có cấu trúc, không phải nhiễu nhãn ngẫu nhiên.*
  > 
  > *1. Các nghiên cứu quốc tế (như Abaiyan et al., 2026) chỉ ra có tới 18.6% review du lịch rơi vào trạng thái bất nhất có quy luật.*  
  > *2. Việc dùng trực tiếp điểm sao làm nhãn ground truth cho mô hình cảm xúc mà không kiểm định sẽ tạo ra **nhiễu nhãn yếu (weak-label noise)**.*  
  > *3. Cần phân biệt rõ: Review hỗn hợp (khen mặt này, chê mặt kia) là bình thường; chỉ khi tổng thể cảm xúc mâu thuẫn rõ rệt với điểm số thì mới là bất nhất.*  
  > *4. Chiều mâu thuẫn (cho thêm điểm vs. dìm điểm) mang bản chất tâm lý hoàn toàn khác nhau.*
  > 
  > *Vì vậy, nguyên tắc của nhóm là giữ lại các ca nghi vấn để đối soát, tuyệt đối không lọc bỏ trước khi phân tích."*

---

### [Slide 7] Survey Finding #2: Bức tranh đo lường độ bất nhất
* **Lời thoại:**
  > *"Kết quả khảo sát #2 cho thấy: **Hiện chưa có công thức nào đã công bố đáp ứng đồng thời cả 3 tiêu chí: giữ Magnitude, giữ Direction và tính ở Cấp khía cạnh (Aspect-level)**.*
  > 
  > * Cụ thể, ma trận phân cực thì mất độ lớn; công thức của Kwon et al. (2025) giữ độ lớn và chiều nhưng là cấp toàn văn trên dữ liệu Amazon; còn SentimentLens (2026) đo ở cấp aspect nhưng lại dùng trị tuyệt đối nên mất dấu.*
  > 
  > *Từ khoảng trống này, nhóm đề xuất một **Candidate Extension**: $D_{i,a}^{signed} = r_i^* - s_{i,a}^*$.*  
  > * Khoảng lệch dương ($>0$): điểm sao cao hơn cảm xúc bài viết — nghi vấn cơ chế vị tha / tấm đệm.*  
  > * Khoảng lệch âm ($<0$): điểm sao thấp hơn cảm xúc bài viết — nghi vấn cơ chế trừng phạt / phẫn nộ.*  
  > *Nhóm xác định rõ đây là đề xuất mở rộng của dự án, cần được kiểm chứng trên dữ liệu thực tế."*

---

### [Slide 8] Survey Finding #3: Lý thuyết dừng trước điểm sao quan sát được
* **Lời thoại:**
  > *"Kết quả khảo sát #3 chỉ ra khoảng trống lớn nhất về mặt lý thuyết:*
  > 
  > *Toàn bộ các nghiên cứu về Consumer Forgiveness, Justice Theory hay Service Recovery (như Huang & Lo 2025, Wei et al. 2025) đều dừng lại ở việc đo lường sự tha thứ hay ý định quay lại thông qua **bảng hỏi khảo sát (survey scale)**.*
  > 
  > * **Chưa có công trình nào kiểm định bằng mô hình toán xem cơ chế tha thứ hay phẫn nộ tác động trực tiếp lên ĐIỂM SAO QUAN SÁT THỰC TẾ trong review khách sạn như thế nào**.*
  > 
  > *Về mặt học thuật, nhóm giữ kỷ luật thuật ngữ: hai khái niệm 'Thăng hoa' và 'Phẫn nộ' tạm thời chỉ xem là nhãn làm việc (working labels), và nhóm sẽ dùng tên trung tính là cơ chế **Buffering** (tấm đệm) và **Punitive** (trừng phạt).*
  > 
  > *Tiếp theo, bạn [Tên Speaker 3] sẽ trình bày về các câu hỏi nghiên cứu, kế hoạch kiểm định và xin ý kiến định hướng từ Thầy."*

```
================================================================================
PHẦN 3: HƯỚNG NGHIÊN CỨU, VALIDATION & XIN Ý KIẾN (Speaker 3 — ~4.0 phút)
================================================================================
```

### [Slide 9] Draft Research Questions: Hướng nghiên cứu đề xuất
* **Lời thoại:**
  > *"Cảm ơn bạn [Speaker 2]. Kính thưa Thầy, từ các khoảng trống đã xác lập, nhóm đề xuất **3 câu hỏi nghiên cứu (RQs) dạng bản nháp** để xin ý kiến Thầy:*
  > 
  > * **RQ1 (Khám phá):** Hiện tượng bất nhất cảm xúc – điểm số xuất hiện với tỷ lệ bao nhiêu và gồm những dạng thức nào sau khi được con người đối soát?*  
  > * **RQ2 (Phương pháp):** Nên lượng hóa độ bất nhất bằng công thức nào ở cấp khía cạnh để bảo toàn cả độ lớn và chiều?*  
  > * **RQ3 (Kiểm định):** Yếu tố thái độ nhân viên (Service) có thực sự đóng vai trò 'tấm đệm' bảo vệ điểm số khi xảy ra lỗi cơ sở vật chất (Facility) hay không, và khía cạnh nào dẫn tới hành vi trừng phạt điểm?*
  > 
  > *Đóng góp chính của đề tài là kết hợp: Phép đo bất nhất có dấu cấp aspect + Benchmark nhãn người có đối chứng + Mô hình hóa hành vi điểm số thực tế."*

---

### [Slide 10] Targeted Validation: Xây dựng Evaluation Benchmark có đối chứng
* **Lời thoại:**
  > *"Để trả lời RQ1 và RQ2 một cách khoa học, bước kế tiếp của nhóm không phải là vội vã chạy mô hình lớn, mà là **xây dựng một tập đánh giá chuẩn (Evaluation Benchmark) 600 – 800 mẫu** gồm 3 nhóm:*
  > 
  > * *Nhóm 1:* 404 review 5 sao có chứa đoạn tiêu cực (nghi vấn chiều tấm đệm).*  
  > * *Nhóm 2:* 199 review 1–2 sao có chứa đoạn tích cực (nghi vấn chiều trừng phạt).*  
  > * *Nhóm 3 (Cực kỳ quan trọng):* Tập đối chứng nhất quán (Aligned Controls) lấy từ cả hai phía điểm để đo **tỷ lệ báo động giả (False Positive Rate)** của các thuật toán.*
  > 
  > *Quy trình gán nhãn gồm 3 bước: Hai bạn trong nhóm gán nhãn độc lập 30–50 mẫu đầu $\rightarrow$ Đo hệ số đồng thuận **Cohen's Kappa** (mục tiêu $\ge 0.70$) $\rightarrow$ Họp thống nhất quy chuẩn và gán nhãn toàn bộ tập dữ liệu."*

---

### [Slide 11] How RDR-0003 Will Be Earned: Cổng quyết định khoa học
* **Lời thoại:**
  > *"Khi đã có Ground Truth từ nhãn người, nhóm sẽ chạy đối chiếu đồng thời 3 công thức đo bất nhất:*
  > 
  > * 1. Ma trận phân cực 3×3 (Baseline dễ diễn giải).*  
  > * 2. Khoảng cách z-score có dấu $z(r) - z(s)$ (Mở rộng từ Kwon et al.).*  
  > * 3. Khoảng cách cấp khía cạnh có dấu $r^* - s_a^*$ (Đề xuất của dự án).*
  > 
  > *Công thức được chọn phải vượt qua 4 tiêu chí khắt khe: Đạt Macro-F1 cao, False-positive rate thấp trên nhóm đối chứng, Ổn định ở cả hai tầng điểm, và Không bị rò rỉ dữ liệu.*
  > 
  > *Nếu đạt, nhóm sẽ ban hành **Quyết định RDR-0003** để chốt phương pháp luận; nếu không đạt, nhóm giữ baseline an toàn và chỉ tìm kiếm tài liệu nhắm đúng lỗi phát hiện."*

---

### [Slide 12] Honest Status: Nhóm đã hoàn thành gì — và điều gì còn mở
* **Lời thoại:**
  > *"Slide 12 thể hiện sự trung thực trong học thuật của nhóm về hiện trạng dự án:*
  > 
  > * **Những gì nhóm ĐÃ XONG 100%:** 2 vòng khảo sát văn hiến; xác lập 15 core papers; đóng khung research gap; xây dựng quy chuẩn gán nhãn chi tiết; hoàn thành bản nháp Research Proposal; và audit trực tiếp toàn bộ 9.990 review.*  
  > * **Những gì nhóm CHƯA KẾT LUẬN và CẦN KIỂM ĐỊNH:** Tỷ lệ bất nhất thật sự; mô hình sentiment estimator tối ưu; ngưỡng threshold; phép đo cuối cùng; và kết quả kiểm định hiệu ứng tấm đệm.*
  > 
  > *Nhóm phân định rất rõ giữa tài liệu nền tảng đã sẵn sàng và các kết quả thực nghiệm cần bước vào giai đoạn kiểm định."*

---

### [Slide 13] Discussion with Supervisor: Ba quyết định cần xin ý kiến Thầy
* **Lời thoại:**
  > *"Để mở khóa cho giai đoạn thực nghiệm tiếp theo, nhóm kính mong nhận được sự góp ý và định hướng của Thầy về **3 quyết định cụ thể**:*
  > 
  > * **1. Về phạm vi dữ liệu:** Nhóm xin phép tập trung vào tập con TripAdvisor tiếng Anh đã có nhãn chuyên gia làm corpus kiểm định trước khi mở rộng.*  
  > * **2. Về thiết kế kiểm định:** Thầy có đồng thuận với cấu trúc benchmark 3 nhóm (kèm Aligned Controls) và quy trình 2 người gán nhãn độc lập không ạ?*  
  > * **3. Về mặt thuật ngữ:** Nhóm đề xuất dùng tên trung tính 'Buffering' và 'Punitive' trong các báo cáo chính thức để đảm bảo tính chặt chẽ học thuật.*
  > 
  > *Nếu Thầy đồng thuận, nhóm sẽ chuyển thẳng sang thực hiện Targeted Validation mà không cần mở thêm vòng khảo sát rộng nào nữa.*
  > 
  > *Nhóm chúng em xin chân thành cảm ơn Thầy. Chúng em rất mong nhận được những nhận xét, câu hỏi và góp ý quý báu từ Thầy!"*

---

## BÍ QUYẾT TRẢ LỜI CÂU HỎI Q&A DỰ PHÒNG

| Tình huống Thầy hỏi | Câu trả lời trọng tâm cần nắm | Slide dẫn chứng |
|---|---|---|
| *"Tại sao nhóm không huấn luyện mô hình học sâu luôn mà lại đi gán nhãn thủ công?"* | *"Dạ thưa Thầy, vì nếu chưa có Ground Truth do người thẩm định thì mô hình dự đoán bất nhất sẽ không có thước đo để biết là đang dự đoán đúng hay sai, và rất dễ bị báo động giả trên các review bình thường ạ."* | Slide 10, 11 |
| *"Biến Loyalty của bài báo gốc có gì sai mà nhóm lại đổi?"* | *"Dạ thưa Thầy, nhóm không phủ nhận kết quả bài gốc, nhưng nhận thấy việc dùng từ khóa 'recommend/never again' giải thích cho điểm sao là giải thích hai phản ứng đồng thời của cùng một cảm xúc (tautology). Nhóm muốn giải thích bằng các khía cạnh dịch vụ cụ thể ạ."* | Slide 4 |
| *"404 review 5 sao có negative span có chắc là khách vị tha không?"* | *"Dạ chưa chắc ạ. Đó mới chỉ là candidate. Có thể là lỗi nhỏ đã được khách sạn khắc phục (service recovery), hoặc chỉ là phàn nàn phụ. Vì vậy nhóm phải dùng 2 người gán nhãn độc lập để phân loại chính xác."* | Slide 3, 10 |
| *"Các tài liệu tham khảo chính của nhóm lấy từ đâu?"* | *"Dạ nhóm có danh mục 15 bài báo hạt nhân chia 3 cụm trong Slide 14 phụ lục, chủ yếu từ các tạp chí hàng đầu như IJHM, Service Business, APJIS và các kỷ yếu hội nghị uy tín ạ."* | Slide 14 |
