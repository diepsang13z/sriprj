# 02 — Kano / three-factor + Impact Asymmetry (IAA · PRCA · AIPA)

**Vai trò:** lớp **cơ chế bất đối xứng ở cấp khía cạnh** — trả lời "khía cạnh nào phạt nặng hơn thưởng". Đây là lớp quyết định nội dung của kiểm định phụ #1 trong RQ3.
**Nguồn trong thư viện:** 4 bài, đều ở `refs/04_mechanism/md/` — Regitz et al. (2026) · Li, J. et al. (2025) · Zhang et al. (2025) · Wang et al. (2024).
**Nguồn phản biện:** Slevitch (2024) — **chưa có toàn văn**, chỉ biết qua [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../../docs/logs/literature_survey/0006_survey_matrix_round_4.md) mục 5.1.

---

## 1. Nội dung cốt lõi

Kano / three-factor theory chia thuộc tính thành ba nhóm theo **vai trò**, không theo mức quan trọng:

| Nhóm | Có thì sao | Không có thì sao |
| --- | --- | --- |
| **Basic / Must-be** | Không tăng hài lòng | Bất mãn mạnh — phạt nặng |
| **Performance / One-dimensional** | Tăng hài lòng | Giảm hài lòng, gần đối xứng |
| **Excitement / Attractive** | Thưởng vượt trội | Không bị phạt |

Nguồn kinh điển được các bài dẫn lại: Kano (1984), Brandt (1987), Matzler & Sauerwein (2002), Füller & Matzler (2008) cho phân loại; Mikulić & Prebežac (2008) cho chỉ số bất đối xứng. **Chưa có bản gốc nào trong `refs/`** — chỉ trích qua các bài ở mục 3.

Ba công cụ đo được dùng trong thư viện: **PRCA** (penalty–reward contrast analysis), **IAA/IA** (impact asymmetry), **AIPA** (asymmetric impact–performance analysis). Chúng khác nhau ở công thức, không khác ở ý tưởng: so độ lớn tác động của *hiệu năng thấp* với *hiệu năng cao*.

## 2. Bốn cách vận hành — cùng ý tưởng, bốn công thức

| Nguồn | Khung | Đơn vị phân tích | Ngưỡng phân loại | Kết quả chính |
| --- | --- | --- | --- | --- |
| Regitz et al. (2026) | Kano qua hồi quy đếm câu cảm xúc | 1.392 review TripAdvisor, Lake Constance, 2018–2023 | Ý nghĩa thống kê $p<0{,}05$ của từng hệ số | *Room* = Must-Be; *Connectivity* = Attractive |
| Li, J. et al. (2025) | Three-factor + PRCA + RIPA | 148.454 review, 359 khách sạn New York, 2019 | $IR = \lvert\beta_{HP}\rvert / \lvert\beta_{LP}\rvert$ với cắt tại $0{,}9$ và $1{,}1$ | 3★: *Staff* Excitement ($IR = 10{,}09$), *Location* Basic ($IR = 0{,}17$); 5★: *Room* Basic ($IR = 0{,}41$) |
| Zhang et al. (2025) | Three-factor, hồi quy đa cấp hiệu ứng hỗn hợp | 543.213 review Booking.com, 1.397 cơ sở lưu trú, 10 thành phố Úc, 2019–2022 | $\lvert LP\rvert / \lvert HP\rvert \ge 1{,}5$ là Basic; $\le 0{,}67$ là Excitement | Gần như toàn bộ 9 yếu tố môi trường trong nhà là Basic; *Cleanliness* $LP = -1{,}53$, *IAQ* $LP = -1{,}34$ |
| Wang et al. (2024) | Three-factor + AIPA/DAIPA trên SHAP của XGBoost | 297.244 review TripAdvisor, 423 khách sạn New York, 2007–2023 | $IA$ với $\theta = \pm 0{,}2$ | Base: *Value* $-0{,}53$, *Sleep quality* $-0{,}53$, *Cleanliness* $-0{,}32$; Performance: *Service* $-0{,}02$; Excitement: *Rooms* $+0{,}30$, *Location* $+0{,}81$ |

## 3. Công thức nguyên dạng (dùng để viết phương pháp luận cho đúng)

**Regitz et al. (2026) §3.3** — hồi quy tuyến tính đếm số câu tích cực/tiêu cực theo chủ đề:

$$Rating_i = \beta_0 + \sum_j \beta_j^{+}\,\text{Count}(Pos_{ij}) + \sum_j \beta_j^{-}\,\text{Count}(Neg_{ij}) + \varepsilon_i$$

Phân loại: chỉ $\beta^{-}$ có ý nghĩa và $\beta^{-}<0$ → **Must-Be**; chỉ $\beta^{+}$ có ý nghĩa và $\beta^{+}>0$ → **Attractive**; cả hai cùng có ý nghĩa → **One-Dimensional**.

**Li, J. et al. (2025)** — mã hóa nhị phân từ điểm cảm xúc $S$: $HP = 1$ nếu $S \in \{4,5\}$; $LP = 1$ nếu $S \in \{1,2\}$; $S=3$ là trung tính (cả hai bằng 0). Hồi quy $Rating = \beta_0 + \sum_k \beta_{HP,k} HP_k + \sum_k \beta_{LP,k} LP_k + \varepsilon$, rồi phân loại bằng $IR_k = \lvert\beta_{HP,k}\rvert / \lvert\beta_{LP,k}\rvert$.

**Zhang et al. (2025) §2.3** — hiệu ứng hỗn hợp hai cấp (khách hàng lồng trong cơ sở lưu trú), có random slope cho từng yếu tố:

$$Y_{ij} = b_0 + u_{0j} + \sum_x (b_x + u_{xj}) HP_{x,ij} + \sum_x (b'_x + u'_{xj}) LP_{x,ij} + \text{Covs} + \varepsilon_{ij}$$

**Wang et al. (2024) §3.2.2** — chỉ số bất đối xứng tác động:

$$IA_i = \frac{\beta^{i}_{high} - \lvert\beta^{i}_{low}\rvert}{\beta^{i}_{high} + \lvert\beta^{i}_{low}\rvert}, \qquad IA_i \in [-1, +1]$$

với $\beta^i_{low} = \mathbb{E}[\phi_i \mid AP_i = 1]$ và $\beta^i_{high} = \mathbb{E}[\phi_i \mid AP_i = 5]$ lấy từ giá trị SHAP ($\phi_i$) của mô hình XGBoost. Ma trận AIPA sáu lớp: ký hiệu H/L theo vị trí so với hiệu năng trung bình, chữ B/P/E theo nhóm Kano. Thứ tự ưu tiên phân bổ nguồn lực: $LB > LP > LE > HB > HP > HE$.

## 4. Ba điều 4 bài này nhất trí

1. **Quan hệ tuyến tính đối xứng là mô hình sai** — SERVQUAL và IPA truyền thống xếp sai thứ tự ưu tiên.
2. **Vệ sinh và điều kiện cơ sở là Basic/Basic-like.** Hệ số phạt trải từ $-0{,}36$ đến $-1{,}53$ ở ba bài độc lập, ba bối cảnh, ba quốc gia.
3. **Vai trò thuộc tính phụ thuộc phân khúc.** Cùng một thuộc tính có thể là Excitement ở hạng thấp và Basic ở hạng cao (Li, J. et al.; Zhang et al.).

## 5. Ba điều chúng bất đồng — chỗ dễ bị hỏi khi bảo vệ

1. **Phòng:** Regitz và Zhang xếp *Room/Space* là Basic thuần; Li, J. et al. và Wang xếp *Room* là Excitement ở hạng 3–4★ ($IR = 1{,}71$ và $2{,}24$; $IA = +0{,}30$), Basic chỉ ở 5★.
2. **Vị trí:** Wang xếp *Location* là Excitement ($IA = +0{,}81$); Li, J. et al. xếp Basic ở 3–4★ ($IR = 0{,}17$; $0{,}38$) nhưng Excitement ở 5★ ($IR = 3{,}88$); Regitz xếp One-Dimensional, tách riêng thành *Connectivity* thì Attractive.
3. **Ngưỡng cắt:** bốn bài dùng bốn ngưỡng khác nhau ($p<0{,}05$ · $0{,}9/1{,}1$ · $1{,}5\times$ · $\theta = 0{,}2$). **Không có chuẩn chung.** Nghĩa là nhãn Basic/Excitement phụ thuộc công cụ, không phải thuộc tính nội tại của khía cạnh.

Điểm 3 chính là lý do cho kết luận ở mục 6.

## 6. Vì sao lớp này chỉ được dùng ở mức **khám phá**

- **Slevitch (2024)** phê bình trực diện: các phương pháp phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống và **hay suy ra bất đối xứng ở nơi thực tế là tuyến tính**.
- **Li, J. et al. (2025)** đưa bằng chứng ngược chiều cụ thể: thuộc tính lõi giữ tác động ổn định/gần đối xứng giữa các hạng sao, không penalty-dominant toàn cục.
- **Hệ quả bắt buộc:** kết quả phân loại phải trình bày như phân tích khám phá, **kèm báo cáo bất định**; không dùng như construct đã kiểm định ([`INDEX.md`](INDEX.md) mục 4 điều 3).

Điểm tựa phòng thủ: Slevitch và Li, J. et al. cũng là **vũ khí phản công** — nếu người phản biện nói "Kano asymmetry là hiển nhiên", ta có sẵn nguồn nói rằng nó không hiển nhiên và thường bị suy diễn sai.

## 7. Vai trò trong đề tài

1. **Sinh câu hỏi của kiểm định phụ #1:** khía cạnh nào penalty-dominant, khía cạnh nào reward ([`RDR-0004`](../../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) mục 2.3).
2. **Biện minh cho giả định bất đối xứng** — cùng [`03_prospect_theory.md`](03_prospect_theory.md), nhưng ở tầng khía cạnh chứ không ở tầng trọng số tâm lý.
3. **Cung cấp mẫu phương pháp** để thích nghi: biến đổi sentiment cấp khía cạnh thành biến HP/LP rồi so hệ số là hướng khả thi với dữ liệu span của dự án. **Đây là gợi ý, không phải quyết định** — công thức $D$ vẫn chờ validation study.
4. **Ranh giới tính mới mỏng nhất của đề tài:** Regitz et al. (2026) làm gần đúng việc dự án định làm (hồi quy sentiment dương/âm theo topic để phân loại Kano). Khác biệt còn lại chỉ là thước đo **có dấu ở cấp khía cạnh** và đơn vị là review có nhãn người gán. Phải nói rõ khác biệt này trong phần đóng góp.

## 8. Câu hỏi bảo vệ hay gặp

| Câu hỏi | Trả lời ngắn | Căn cứ |
| --- | --- | --- |
| "Khía cạnh nào của tôi là Basic?" | Chưa trả lời được ở mức khẳng định; bốn bài trong thư viện xếp cùng một thuộc tính vào ba nhóm khác nhau | Mục 5 |
| "Vậy Kano có vô dụng không?" | Không. Hướng của hiệu ứng nhất quán (rủi ro vệ sinh phạt nặng); chỉ **danh tính từng khía cạnh** là bất định | Mục 4, 6 |
| "Sao không dùng bảng hỏi Kano cho chuẩn?" | Bảng hỏi không có trên dữ liệu review; và đề tài cố ý không mở vòng thu thập mới | [`../../AGENTS.md`](../../AGENTS.md) mục 2 |
| "Ngưỡng nào là ngưỡng đúng?" | Không có ngưỡng chuẩn; phải công bố ngưỡng đã dùng và kiểm tra độ nhạy | Mục 5.3 |
| "Có phải nhóm tự nghĩ ra bất đối xứng?" | Không; đó là kết quả lặp lại ở bốn nguồn độc lập, quy mô tới 543.213 review | Mục 4 |

## 9. Ranh giới

- **Không** khẳng định danh tính Kano của một khía cạnh trong dữ liệu dự án trước khi có kiểm định phụ #1.
- **Không** trích bản gốc Kano (1984) hoặc Mikulić & Prebežac như đã đọc — chưa có trong `refs/`.
- **Không** bê nguyên ngưỡng của bốn bài vào đề tài rồi coi là chuẩn mực.
