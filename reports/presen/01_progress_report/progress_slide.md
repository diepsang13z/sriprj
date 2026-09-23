# BÁO CÁO TIẾN ĐỘ DỰ ÁN

**Bất nhất cảm xúc – điểm số ở cấp khía cạnh trong review khách sạn**

*Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews*

Nhóm: [điền] · Môn DAP391m · [ngày báo cáo]

---

## Nội dung báo cáo

1. Đề tài của nhóm là gì
2. Vì sao chọn đề tài này — khoảng trống nghiên cứu
3. Câu hỏi nghiên cứu
4. Cách nhóm làm — phương pháp
5. Ứng dụng của nhóm — Bảng soát điểm sao
6. Sau các đợt khảo sát văn hiến, nhóm có gì
7. Việc tiếp theo và điểm cần thầy góp ý

---

## 1. Đề tài của nhóm là gì?

> **Một câu:** khách hàng viết một đằng nhưng chấm sao một nẻo — nhóm lấy chính những ca đó làm đối tượng nghiên cứu, thay vì coi chúng là lỗi dữ liệu.

Khách hàng để lại hai tín hiệu cùng lúc khi đánh giá khách sạn:

- **Văn bản tự do** — kể lại trải nghiệm
- **Điểm sao** — chấm tổng thể 1–5 sao

Hai tín hiệu này thường được giả định là ăn khớp. Nhưng trong thực tế dữ liệu của nhóm, chúng **không luôn ăn khớp**.

---

## 2. Ví dụ cụ thể

**Ca 1 — chê mà vẫn cho điểm cao**

> *"Phòng sạch, nhân viên thân thiện, nhưng điều hoà kêu rất to và wifi yếu. Nhìn chung vẫn là chỗ ổn."* → **5 sao**

**Ca 2 — khen nhiều mà vẫn cho điểm thấp**

> *"Vị trí tuyệt vời, phòng đẹp, ăn sáng ngon. Nhưng tiếng ồn buổi tối khiến tôi không ngủ được."* → **2 sao**

Cùng một kiểu "không khớp", nhưng **hai hướng ngược nhau**. Điểm quan trọng: đó là **hành vi**, không phải lỗi nhập liệu.

---

## 3. Vì sao hiện tượng này quan trọng?

**Đối với nghiên cứu**

- Rất nhiều mô hình cảm xúc dùng **điểm sao làm nhãn để huấn luyện**. Nếu điểm sao không phản ánh đúng cảm xúc trong văn bản, các mô hình đó đang học từ **nhãn yếu (weak label)** — sai một cách âm thầm.
- Hiện tượng này bị xử lý như **nhiễu cần loại bỏ**, nên gần như không được nghiên cứu trực tiếp.

**Đối với quản trị khách sạn**

- Biết **khía cạnh nào khách sẵn sàng bỏ qua** và **khía cạnh nào bị dìm điểm** giúp phân bổ ngân sách đúng chỗ (sửa cơ sở vật chất hay đào tạo nhân viên).

---

## 4. Dữ liệu của nhóm cho thấy hiện tượng có thật

Tập dữ liệu: **9.990 review TripAdvisor tiếng Anh, giai đoạn 2015–2023, thuộc 2.622 khách sạn**

| Chỉ số | Số lượng |
| --- | ---: |
| Review 5 sao **vẫn chứa phàn nàn tiêu cực** | **404** |
| Review 1–2 sao **vẫn chứa lời khen** | **199** (trên tổng 465 review 1–2 sao) |
| Tổng số ca đáng ngờ | **603 review**, trải trên **468 khách sạn** |

Hai con số này không thể là may rủi ngẫu nhiên — chúng cho thấy một **mẫu hành vi có cấu trúc**.

*Nguồn: tính trực tiếp trên `data/TripAdvisor_EN.json`, ngày 22/09/2026.*

---

## 5. Cách làm phổ biến hiện nay và vấn đề của nó

**Cách làm phổ biến**

1. Giả định "khen thì 5 sao, chê thì 1 sao"
2. Gặp review lệch → coi là lỗi, xoá khỏi tập huấn luyện
3. Đo độ lệch bằng **trị tuyệt đối**: $|Điểm - Cảm\ xúc|$

**Vấn đề**

- **Trị tuyệt đối làm mất chiều.** Điểm lệch 2 đơn vị không cho biết khách **cho thêm điểm** hay **dìm điểm** — hai hành vi hoàn toàn khác nhau.
- **Chưa có cách đo nào giữ đồng thời độ lớn và chiều ở cấp khía cạnh** (tức là ở mức "phòng ốc", "dịch vụ", "tiện ích"… chứ không phải cả bài review).
- Các nghiên cứu hiện có hoặc làm ở cấp toàn bài, hoặc chỉ phân loại rời rạc, hoặc mất chiều.

---

## 6. Bài báo gốc nhóm kế thừa và phản biện

**Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026)** — *International Journal of Hospitality Management*

**Kế thừa:** khung S-O-R · bối cảnh review khách sạn · cách tách khía cạnh · dữ liệu đối chuẩn

**Phản biện ba điểm:**

1. **Giả định quan hệ đơn điệu** — mô hình giả định cảm xúc tích cực thì điểm tăng, tiêu cực thì điểm giảm. Giả định này không giải thích được 404 review 5 sao có phàn nàn tiêu cực trong chính dữ liệu bài báo.
2. **Lập luận vòng ở biến `Loyalty`** — biến này được định nghĩa bằng chính các câu như *"sẽ quay lại"*, *"rất khuyến khích"*, rồi đưa vào mô hình để giải thích cho điểm số. Dùng vế lời để giải thích vế số là lặp thừa.
3. **Trộn hai trục khác bản chất** — "khách nói về *cái gì*" (khía cạnh) bị trộn với "khách cảm thấy *như thế nào*" (cảm xúc).

---

## 7. Khoảng trống nghiên cứu

**Mặt đo lường (kỹ thuật)**

> Chưa có phép đo nào đồng thời giữ **độ lớn** và **chiều** ở **cấp khía cạnh** trên dữ liệu khách sạn.

**Mặt hành vi (giải thích)**

> Văn hiến mới chủ yếu giải thích *mức hài lòng tổng thể*. Chưa kiểm định trực tiếp việc **nhiều khía cạnh kết hợp bất đối xứng** để tạo ra độ lệch trên **điểm sao quan sát được**.

**Hai ranh giới nhóm tự đặt ra (không giấu)**

- Ranh giới tính mới **mỏng**: Regitz et al. (2026) làm rất gần, chỉ khác đơn vị phân tích.
- **Hạn chế nhận dạng:** chỉ có review công khai thì **không phân biệt được** bù trừ thật với thiên lệch khi trình bày và méo do nền tảng. Nhóm ghi rõ giới hạn này thay vì kết luận quá mức.

---

## 8. Câu hỏi nghiên cứu

| | Câu hỏi |
| --- | --- |
| **RQ1** | Hiện tượng bất nhất xuất hiện **với tần suất bao nhiêu**, và gồm **những dạng có hướng nào**? |
| **RQ2** | Làm thế nào để **lượng hóa** độ bất nhất theo từng khía cạnh mà giữ được **cả độ lớn lẫn chiều**? |
| **RQ3** *(đã chốt)* | Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh **kết hợp bất đối xứng như thế nào** để quyết định chiều hướng và độ lớn của độ lệch? |

RQ3 đã được **chốt chính thức** trong quyết định `RDR-0004` của nhóm. RQ1 và RQ2 còn ở dạng nháp, dự kiến chốt sau bước validation.

**Ba câu hỏi kỹ thuật bổ sung** (phục vụ phần dự báo của môn học): năm mô hình dự đoán điểm đạt kết quả thế nào khi chia tập theo khách sạn · phần dư giữa điểm thật và điểm dự báo phân bố ra sao · có dự đoán được review nào bị dìm điểm không.

---

## 9. Phương pháp — ba tầng

```
   Văn bản review
        │
        ▼
 ┌──────────────────┐   TẦNG 1 — Xử lý ngôn ngữ
 │  Tín hiệu cảm xúc│   Trích cảm xúc theo TỪNG khía cạnh
 │  theo khía cạnh  │   (từ span do chuyên gia gán nhãn)
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐   TẦNG 2 — Đo lường
 │  Điểm lệch có dấu│   So điểm sao với mức văn bản biện minh
 │  D (theo khía    │   Giữ cả ĐỘ LỚN và CHIỀU
 │  cạnh)           │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐   TẦNG 3 — Kinh tế lượng
 │  Mô hình hành vi │   Khía cạnh nào chi phối, khía cạnh nào bù trừ
 │  chấm điểm       │   dưới các điều kiện biên
 └──────────────────┘
```

---

## 10. Phương pháp — năm bước thực hiện

| Bước | Nội dung | Đầu ra |
| --- | --- | --- |
| **1** | Phân tích khám phá dữ liệu, kiểm tra tính toàn vẹn liên kết khía cạnh – cảm xúc | Bảng đặc tả dữ liệu |
| **2** | Dựng **tập đánh giá có đối chứng** (~600–800 mẫu): ca lệch hai hướng + nhóm đối chứng "nói sao chấm vậy" | Tập dữ liệu để kiểm thử mọi phép đo |
| **3** | **Hai người gán nhãn độc lập**; đo mức đồng thuận (Cohen's Kappa ≥ 0,70); giải quyết bất đồng | Ground truth |
| **4** | **So sánh ba công thức đo** độ lệch trên cùng ground truth, chọn một | Phép đo chính thức |
| **5** | Mô hình hóa hành vi chấm điểm và các điều kiện biên | Bảng kết quả kiểm định |

**Nhóm đối chứng là bắt buộc.** Nếu chỉ kiểm thử trên các ca nghi ngờ, một phép đo quá nhạy vẫn "đúng" trên tập đó nhưng sẽ báo động giả liên tục khi gặp review bình thường.

---

## 11. Một nguyên tắc kỹ thuật quan trọng

**Phải tách hai họ mô hình — đây là chỗ dễ sai nhất:**

| | Họ A — Mô hình dự đoán điểm | Họ B — Bộ ước lượng cảm xúc |
| --- | --- | --- |
| Nhiệm vụ | Đoán mức điểm từ văn bản | Đọc cảm xúc từng khía cạnh |
| Huấn luyện trên | **Nhãn điểm sao** | **Nhãn cảm xúc do người gán** |
| Dùng cho | Phần dự báo của môn, phân tích độ nhạy | Phép đo bất nhất (RQ2, RQ3) |

**Vì sao phải tách:** nếu lấy mô hình đoán điểm làm thước đo cảm xúc, mô hình sẽ tái tạo lại chính điểm sao — tức là **không kiểm chứng được gì cả**.

---

## 12. Chốt phép đo như thế nào?

Ba ứng viên được đối chiếu **trên cùng một ground truth do người gán nhãn**:

| Ứng viên | Cho ra cái gì |
| --- | --- |
| Ma trận phân cực có hướng 3×3 | Nhãn lớp — dễ diễn giải nhất, dùng làm baseline |
| Khoảng cách chuẩn hóa có dấu | Một số kèm dấu cho cả bài |
| **Khoảng cách cấp khía cạnh có dấu** | Vector theo từng khía cạnh — ứng viên chính |

**Tiêu chí chọn:** khớp với nhãn người · giữ được dấu · ổn định ở cả hai phía điểm · giải thích được theo khía cạnh · không dùng điểm sao để huấn luyện.

**Không đạt thì sao:** giữ ma trận phân cực làm baseline và ghi rõ lý do — nhóm đã định trước đường lui này.

---

## 13. Ứng dụng của nhóm — "Bảng soát điểm sao"

Các nền tảng đặt phòng chỉ hiển thị **một con số** cho mỗi khách sạn. Ứng dụng của nhóm tách con số đó thành hai:

> **Điểm khách bấm** và **điểm mà nội dung review biện minh được** — khoảng cách giữa hai con số là thứ khách sạn cần nhìn.

**Người dùng:** quản lý vận hành / revenue manager khách sạn — không phải khách du lịch.

| # | Câu hỏi của quản lý | App lấy dữ liệu ở đâu để trả lời |
| --- | --- | --- |
| 1 | Khách sạn tôi đang được điểm cao hơn thực lực bao nhiêu? | Chênh lệch giữa điểm thực tế và điểm dự báo từ văn bản |
| 2 | Khoản chênh đó đến từ khía cạnh nào? | Điểm lệch có dấu $D$ theo từng khía cạnh |
| 3 | Nên đầu tư vào đâu — cơ sở vật chất hay đào tạo? | Xếp hạng khía cạnh **bị dìm điểm** so với khía cạnh **được bỏ qua** |

---

## 14. Ứng dụng — sáu màn hình

```
┌──────────────────────────────────────────────────────────┐
│  M1 Tổng quan khách sạn   ← điểm vào, chọn khách sạn     │
│         │                                                │
│         ├──► M2 Bóc tách khía cạnh   ← vì sao lệch       │
│         │                                                │
│         └──► M3 Soát một review      ← kiểm chứng từng ca│
│                                                          │
│  M4 Hàng đợi cảnh báo   ← chạy nền, không cần mở         │
│  M5 Bản đồ địa điểm     ← so sánh thị trường             │
│  M6 Hỏi đáp             ← tra nhanh bằng câu hỏi         │
└──────────────────────────────────────────────────────────┘
```

| Màn | Hiển thị gì | Giúp khách sạn thế nào |
| --- | --- | --- |
| **M1** Tổng quan khách sạn | Điểm thực tế · điểm văn bản biện minh · khoảng chênh · số ca lệch · xu hướng | Biết mình có đang sống nhờ quán tính không |
| **M2** Bóc tách khía cạnh | Cột lệch hai phía · heatmap khía cạnh × mức sao · Sankey · word cloud | Quyết định đầu tư cơ sở vật chất hay đào tạo |
| **M3** Soát một review | Văn bản tô sáng span theo khía cạnh · điểm dự báo + độ tin cậy · $D$ | Tự kiểm chứng từng ca, có bằng chứng khi huấn luyện nhân viên |
| **M4** Hàng đợi cảnh báo | Ca vượt ngưỡng · trạng thái đã gửi cảnh báo | Vận hành chủ động, xử lý trước khi điểm trung bình tụt |
| **M5** Bản đồ địa điểm | Bản đồ choropleth theo 50 địa điểm | Phát hiện vấn đề mang tính hệ thống theo khu vực |
| **M6** Hỏi đáp | Câu trả lời dạng số cho câu hỏi tự nhiên | Lấy số ngay trong cuộc họp, không cần biết SQL |

---

## 15. Ứng dụng — màn hình chính và ca demo thật

```
┌─ SOÁT ĐIỂM SAO ──────────────────────────────────┐
│ Khách sạn: [Sofitel Legend Metropole ▾]  Năm:[▼] │
│                                                  │
│   4.0★ thực tế  │  3.2★ văn bản biện minh │ +0.8★│
│                                                  │
│   Review #131571                                 │
│   "…beds were so comfortable…"       ← tích cực  │
│   "…wait staff were very slow…"      ← tiêu cực  │
│   → khách chấm cao hơn nội dung 0.8 sao          │
│                                                  │
│   3 ca tương tự tháng này · đã gửi cảnh báo      │
└──────────────────────────────────────────────────┘
```

Ca demo có sẵn trong dữ liệu, không phải bịa: Sofitel Legend Metropole Hà Nội (8 ca / 85 review) · Anantara Hội An (6/39) · Salinda Phú Quốc (4/31) · Lavender Central (4/60) · Indochine Palace (4/30).

**Bốn ràng buộc khi xây, nhóm ghi rõ để không bị hỏi khó:**

- **Chưa ship phần hiển thị $D$** trước khi công thức đo được chốt — ba màn M1/M2/M3 đều dùng $D$, nên phải chờ validation.
- **Ngôn ngữ không suy diễn tâm lý:** app nói *"chấm cao hơn nội dung"*, không nói *"khách tha thứ"*.
- **Không hiển thị tổng hợp khách sạn khi mẫu dưới 20 review** — chỉ 76 trong 2.622 khách sạn đủ ngưỡng này.
- **Không dùng biểu đồ radar** — 46/76 khách sạn có hồ sơ gần tròn, vẽ ra không mang thông tin.

---

## 16. Vì sao nhóm khảo sát theo cách này?

Khảo sát của nhóm **không phải** quét cho thật nhiều. Cách làm được quy định trước bằng hai quyết định nội bộ:

**Quy tắc 1 — Mục tiêu dừng rõ ràng.** Khảo sát chỉ kết thúc khi có đủ nguyên liệu để viết đề cương, có ít nhất một baseline đối chứng, và **không còn phát hiện nào làm thay đổi thiết kế nghiên cứu**.

**Quy tắc 2 — Chỉ quét cửa sổ 36 tháng gần nhất.** Tài liệu cũ hơn chỉ được lấy khi thật sự là nguồn gốc của một khái niệm nhóm đang dùng, và phải ghi rõ lý do.

**Bốn nguyên tắc khi đọc:**

1. **Ưu tiên tạp chí** trước hội nghị và preprint
2. **Mỗi DOI xác minh độc lập** qua hai cơ sở dữ liệu (Crossref và OpenAlex), lệch là loại
3. **Gán mức bằng chứng I–VII** cho từng nguồn (meta-analysis là mức I, ý kiến chuyên gia là mức VII)
4. **Bắt buộc có nhánh phản biện** — phải chủ động tìm bằng chứng **chống lại** giả thuyết của mình

---

## 17. Bốn vòng khảo sát — tóm tắt

| Vòng | Mục đích | Kết quả |
| --- | --- | --- |
| **1–2** | Quét rộng, dựng nền | 15 nguồn hạt nhân, 3 cụm chủ đề |
| **3** | Kiểm tra lại RQ3 cũ | 9 ứng viên tạp chí → chốt cơ chế rộng hơn |
| **4** | **Kiểm chứng**, không mở rộng | 26 nguồn mới xác minh qua 5 nhóm; có nhánh phản biện bắt buộc |

Sau vòng 4, nhóm **đóng khảo sát có điều kiện**: đủ để viết đề cương, nhưng ghi rõ chỗ nào còn thiếu.

---

## 18. Vòng 3 — nhóm đã tái định hình câu hỏi nghiên cứu như thế nào?

**RQ3 cũ của nhóm:** *"khách sạn phục vụ tốt có cứu được lỗi cơ sở vật chất không?"*

**Vòng 3 cho thấy câu hỏi đó trộn ba giả định chưa được chứng minh:**

1. Chỉ có **một cặp khía cạnh** đáng quan tâm (dịch vụ × cơ sở vật chất)
2. Mọi lỗi cơ sở vật chất đều **nặng như nhau**
3. Điểm tổng được hình thành bằng quan hệ **bù trừ tuyến tính**

**Bằng chứng phản bác:** các nghiên cứu phân biệt thuộc tính cơ bản với thuộc tính tạo hài lòng; lý thuyết triển vọng cho thấy mất mát gây tác động mạnh hơn lợi ích tương đương; một số lỗi có mức phạt lớn đến mức không bù được.

**Kết luận vòng 3 — cơ chế rộng hơn, hai nhánh:**

- **Nhánh chi phối:** một lỗi cơ bản và nghiêm trọng có thể chi phối cả đánh giá
- **Nhánh bù trừ:** lỗi nhẹ hoặc đã được khắc phục thì các điểm tích cực mới cộng gộp được

→ Cặp "dịch vụ × cơ sở vật chất" từ chỗ **là cả đề tài** thì nay chỉ còn là **một phép so sánh dự kiến trước**.

---

## 19. Vòng 4 — kiểm chứng và tự phản biện

Vòng 4 **không** tìm thêm tài liệu để mở rộng đề tài. Nó nhằm vá hai lỗ hổng bằng chứng và **tự tấn công kết luận của mình**.

**Kết quả tích cực**

- Bất đối xứng được xác nhận trên nhiều bối cảnh và quy mô lớn (88.309 review; hơn 540.000 review)
- Mức độ nghiêm trọng của lỗi và việc khắc phục là **biến điều kiện thật**, không phải biến nền
- Có mốc so sánh cho tỷ lệ bất nhất: một nghiên cứu độc lập tìm thấy **17,3%** review có bất nhất rõ rệt

**Ba đòn phản biện — và nhóm chấp nhận**

| Đòn phản biện | Nhóm xử lý thế nào |
| --- | --- |
| Bất nhất có thể là **thiên lệch khi trình bày công khai**, không phải cơ chế bù trừ | Ghi rõ là **hạn chế nhận dạng**, không tuyên bố nhân quả |
| Bất nhất **phụ thuộc nền tảng**, không phải quy luật chung | Mọi tuyên bố về tỷ lệ phải ghi phạm vi TripAdvisor 2015–2023 |
| **Công cụ phân loại khía cạnh có lỗi quy trình** | Phần phân loại chỉ trình bày như **phân tích khám phá**, kèm bất định |

**Điểm mạnh của việc tự phản biện:** những nguồn phản biện này trở thành **vũ khí phòng thủ** khi bảo vệ đề tài — nhóm biết trước điểm yếu và đã chủ động khai báo.

---

## 20. Sau các đợt khảo sát, nhóm có gì?

**Thư viện tài liệu: 35 tệp toàn văn, xếp theo 8 cụm chức năng**

| Cụm | Vai trò |
| --- | --- |
| Bài gốc đối chuẩn | Nguồn bị phản biện |
| Định nghĩa & nguồn gốc thước đo | Khái niệm nền |
| Bằng chứng hiện tượng | Chứng minh bất nhất có thật, đo tỷ lệ |
| Lý thuyết & cơ chế bất đối xứng | Lớp giải thích chính |
| Điều kiện biên | Mức độ nghiêm trọng, khắc phục, hạng sao |
| **Phản biện & phê bình phương pháp** | Chống lại kết luận của chính mình |
| Baseline & phương pháp kỹ thuật | Mốc so sánh, công cụ |
| Audit trail | Giữ lại, không dùng dẫn dắt lập luận |

**Năm quyết định nội bộ đã ban hành** — ghi lại mục tiêu dừng khảo sát, quy tắc quét, việc mở lại khảo sát, chốt RQ3, và khóa khung lý thuyết.

**Khung lý thuyết đã khóa:** S-O-R + thuyết Kano/ba nhân tố + thuyết triển vọng + quyết định hai giai đoạn.

**Phạm vi dữ liệu đã khóa:** 9.990 review, không mở rộng lên corpus 782.584 review của bài gốc.

---

## 21. Khảo sát đang dừng lại ở đâu?

**Đóng có điều kiện — và nhóm nói rõ vì sao**

- Tiêu chí "bão hòa" ban đầu **không thể đạt** bằng cách quét trong cửa sổ 36 tháng, vì cửa sổ này liên tục sinh công bố mới. Nhóm thay bằng tiêu chí đo được: *không còn phát hiện nào làm đổi thiết kế nghiên cứu*.
- Thư viện đã đủ để viết đề cương, nhưng **chưa đủ để chốt công thức đo** — đây là chỗ nhóm đang thực sự dừng.

**Còn thiếu**

| Hạng mục | Trạng thái |
| --- | --- |
| 16 bài **đóng** cần thư viện trường hỗ trợ | Ưu tiên 3 bài: Kwon W. 2026 · Han & Anderson · Slevitch |
| Công thức đo độ lệch | Chưa chốt — **chờ validation trên dữ liệu** |
| Bộ ước lượng cảm xúc và ngưỡng phân loại | Chưa chốt — cùng nằm trong validation |
| Nguồn gốc và giấy phép dữ liệu | Chưa khai báo |

**Điểm đáng lưu ý về phương pháp:** việc còn thiếu tài liệu **không chặn** bước validation. Bước này chạy trên dữ liệu của nhóm, không phụ thuộc paywall.

---

## 22. Việc tiếp theo

| Ưu tiên | Việc | Đầu ra |
| --- | --- | --- |
| 1 | Chạy validation: dựng tập đánh giá, hai người gán nhãn, so ba công thức | **Công thức đo được chốt** |
| 2 | Nhờ thư viện trường lấy các bài đóng theo thứ tự ưu tiên | Toàn văn phục vụ phần phương pháp |
| 3 | Cập nhật Research Proposal theo khung đã khóa và RQ3 đã chốt | Bản đề cương |
| 4 | Khóa mô hình kinh tế lượng sau khi có công thức đo | Bảng kết quả kiểm định |
| 5 | Dựng nhánh ứng dụng và endpoint sớm | Ứng dụng demo được |

---

## 23. Điểm cần thầy góp ý

1. **Tên đề tài** — nhóm đang dùng tên tạm; tên chính thức nên chốt sau khi có công thức đo.
2. **RQ1 và RQ2** — hiện ở dạng nháp, cần thầy định hướng có nên chốt sớm không.
3. **Phạm vi dữ liệu** — nhóm chọn 9.990 review đã gán nhãn thay vì mở rộng lên toàn bộ 782.584 review của bài gốc. Nhóm cho rằng giới hạn này đủ, nhưng muốn xác nhận.
4. **Ba bài baseline** — nhóm đề xuất chọn Le et al. (2026), Kwon et al. (2025) và You et al. (2024).
5. **Mức độ chi tiết của phần đo lường** — nhóm định dành trọng tâm cho phép đo độ lệch và ground truth do người gán nhãn, thay vì tối ưu mô hình dự báo.

---

## Phụ lục — Gợi ý trả lời câu hỏi

**"Vì sao không dùng luôn điểm sao làm nhãn cảm xúc?"**
Vì chính dữ liệu cho thấy hai tín hiệu không khớp: 404 review 5 sao có phàn nàn tiêu cực. Nếu dùng điểm sao làm nhãn, mô hình học luôn cả phần sai đó.

**"Vì sao cần tận hai người gán nhãn?"**
Vì "thế nào là bất nhất thật" là phán đoán chủ quan. Cần đo mức đồng thuận (Cohen's Kappa) để biết quy chuẩn có dùng được không, và phải giải quyết bất đồng trước khi mở rộng.

**"Sao không dùng mô hình ngôn ngữ lớn cho nhanh?"**
Có thể dùng, nhưng vẫn phải đo trên tập do người gán nhãn. Và mô hình cảm xúc **không được** huấn luyện trên điểm sao, nếu không thì kết quả chỉ là vòng lặp.

**"Sao chỉ có 9.990 review?"**
Đây là phần đã có nhãn khía cạnh và cảm xúc ở cấp span — điều kiện bắt buộc để đo độ lệch theo khía cạnh. Corpus lớn hơn không có nhãn span thì không dùng được cho RQ2 và RQ3.

**"Có chắc là khách tha thứ không?"**
Nhóm **không** kết luận điều đó. Dữ liệu công khai không cho phép suy ra trạng thái tâm lý. Nhóm chỉ nói về **mẫu hành vi chấm điểm quan sát được** và đã ghi rõ hạn chế này.

---

*Tài liệu liên quan:* [`research_proposal.md`](../../md/research_proposal.md) · [`project_planning.md`](../../md/project_planning.md) · [`notes/project_overview.md`](../../../notes/project_overview.md) · [`notes/reference_map.md`](../../../notes/reference_map.md) · [`refs/INDEX.md`](../../../refs/INDEX.md)
