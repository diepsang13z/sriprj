# 03 — Prospect Theory (Lý thuyết triển vọng)

**Vai trò:** lớp giải thích **trọng số** — vì sao mất mát nặng hơn được lợi, và vì sao tác động biên giảm dần. Trong đề tài, lớp này giải thích nhánh $D < 0$ mà không cần gán trạng thái tâm lý cho người viết.
**Nguồn chính:** [`refs/04_mechanism/md/2025_sharma_review_sentiment_garden_accepted_manuscript.md`](../../refs/04_mechanism/md/2025_sharma_review_sentiment_garden_accepted_manuscript.md) — Sharma, Shin, Nicolau & Park (2025), IJHM 129, 104170. **Lưu ý bản local là accepted manuscript, không phải version of record.**

---

## 1. Ba cơ chế, định nghĩa nguyên bản

| Cơ chế | Nội dung |
| --- | --- |
| **Reference point** | Người ta không đánh giá kết quả ở mức tuyệt đối mà so với một mốc chuẩn; lệch trên mốc là *gain*, lệch dưới là *loss* |
| **Loss aversion** | Độ mất thỏa dụng của một khoản lỗ lớn hơn độ thỏa dụng của khoản lãi cùng độ lớn — nhánh lỗ của hàm giá trị dốc hơn |
| **Diminishing sensitivity** | Càng xa mốc, thay đổi thỏa dụng biên càng nhỏ — hàm giá trị cong thành hình chữ $S$: lõm ở miền lãi, lồi ở miền lỗ |

Nguồn kinh điển mà bài này dẫn: Kahneman & Tversky (1979) cho cả ba cơ chế, thêm Tversky & Kahneman (1991) cho loss aversion (§1 dòng 19; §2 dòng 35–41; §6 dòng 334).

**Cảnh báo provenance:** bài **không** nêu hệ số $\lambda \approx 2{,}25$ kinh điển (con số hay được trích). Đừng đưa $\lambda$ vào báo cáo rồi gán cho Sharma et al. — bài kiểm định bất đối xứng bằng tỷ số hệ số hồi quy, không bằng tham số lý thuyết.

## 2. Bài vận hành hóa thế nào

- **Dữ liệu:** 416.756 review tiếng Anh, 375 khách sạn (127 hạng 5★, 120 hạng 4★, 128 hạng 3★; loại 1–2★), 14 thành phố châu Âu, TripAdvisor, 2000–2022 (§Abstract, §4.2, Bảng 1).
- **Biến phụ thuộc:** điểm cảm xúc văn bản $Senti \in [-1,1]$ tính bằng từ điển LIWC (§4.2, Bảng 2).
- **Biến độc lập:**
  - $Gain_i = \text{Rating}_i - \text{Expected}_i$ khi dương, ngược lại $0$ (trung bình $0{,}2827$).
  - $Loss_i = \text{Rating}_i - \text{Expected}_i$ khi âm, ngược lại $0$ (trung bình $-0{,}2827$).
  - Biến bậc hai $Gain^2$, $Loss^2$ để bắt diminishing sensitivity (§4.1, dòng 129–143).
- **Mốc tham chiếu:** điểm đánh giá trung bình tháng của chính khách sạn đó, dùng làm proxy cho con số khách nhìn thấy trên web trước khi đặt. Bài nói thẳng **không đo được** mốc nội tại trong đầu khách (§3 dòng 59–61; §4.2 dòng 197–201).
- **Mô hình:** OLS với hiệu ứng cố định thành phố/tháng/năm, tương tác theo hạng sao và theo giai đoạn sau Covid; xử lý nội sinh hai chiều giữa điểm sao và cảm xúc bằng **Gaussian Copulas** (tách riêng cho Gain và Loss); kiểm định thêm bằng **hồi quy phân vị** $Q_{10}$–$Q_{90}$ (§4.1, §5 dòng 231–296).

## 3. Kết quả định lượng (Model 1, $R^2 = 0{,}3243$)

| Hệ số | Giá trị | Ý nghĩa |
| --- | ---: | --- |
| $Gain$ ($\delta_1$) | $+0{,}056$ ($p<0{,}01$) | Vượt kỳ vọng làm cảm xúc tăng, nhưng rất yếu |
| $Loss$ ($\delta_2$) | $+0{,}484$ ($p<0{,}01$) | Biến $Loss$ mang dấu âm, nên hệ số dương nghĩa là hụt kỳ vọng càng lớn thì cảm xúc càng sụt sâu |
| $Gain^2$ ($\delta_3$) | $-0{,}027$ ($p<0{,}01$) | Độ lõm ở miền lãi |
| $Loss^2$ ($\delta_4$) | $+0{,}028$ ($p<0{,}01$) | Độ lồi ở miền lỗ |

- **Bất đối xứng $\approx 8{,}64$ lần** ($0{,}484 / 0{,}056$), kiểm định Wald $= 1198{,}1$; $p<0{,}001$ (§5 dòng 266). Đây là con số mạnh nhất của bài.
- Đọc đúng hệ số: $\delta_2$ **dương** không có nghĩa "loss làm tăng cảm xúc". Biến $Loss$ đã mang dấu âm sẵn; hệ số dương nói rằng mức âm đó được khuếch đại.
- **Theo phân vị cảm xúc:** bất đối xứng mạnh nhất ở đuôi thấp — $Loss = 0{,}583$ tại $Q_{10}$ và $0{,}624$ tại $Q_{25}$, trong khi $Gain$ chỉ $0{,}181$ và $0{,}062$. Ở $Q_{75}$ và $Q_{90}$, hệ số Gain về $0{,}000$ (Bảng 4). Nghĩa là: **cơ chế này sống ở nhóm review tiêu cực, không phải nhóm review tích cực.**
- **Theo hạng sao:** khách sạn 5★ có loss aversion cao nhất; 4★ lệch $-0{,}118$ và 3★ lệch $-0{,}122$ so với 5★ (đều $p<0{,}01$, giai đoạn trước dịch — §5 dòng 280).
- **Theo thời gian:** loss aversion tăng vọt sau tháng 6/2020, đỉnh tháng 9/2020 ($+0{,}255$), rồi tàn dần và về mức trước dịch vào tháng 3/2022 (§5 dòng 276).

## 4. Cái bài này ĐO được, và cái chỉ SUY LUẬN

**Đo được:** điểm cảm xúc văn bản; điểm sao; khoảng lệch so với trung bình tháng; hệ số hồi quy của Gain/Loss và bậc hai; biến thiên theo tháng, theo hạng sao, theo phân vị.

**Chỉ suy luận:**
- Mốc tham chiếu thật trong đầu khách — bài tự nhận không đo được, chỉ có proxy.
- Cơ chế tâm lý đằng sau (ví dụ nỗi lo rủi ro sức khỏe thời dịch) — không có biến đo mức ngại rủi ro của từng cá nhân (§3 dòng 97–99; §6 dòng 370).
- Hệ quả "mẫu sau dịch gồm nhiều người ít ngại rủi ro hơn" — thuần lập luận, và chính bài gọi kết quả của mình là **ngưỡng tối thiểu** vì thiên lệch chọn mẫu (§6 dòng 370).

## 5. Hạn chế tác giả tự nhận (§6 dòng 364–370)

1. Một nền tảng duy nhất (TripAdvisor); cần kiểm chứng chéo Google/Yelp.
2. Mốc tham chiếu chỉ là proxy; cần phương pháp thực nghiệm để thử các mốc khác.
3. Cảm xúc đo ở **cấp toàn văn bản**, chưa bóc theo khía cạnh — bài đề xuất bổ sung topic modeling.
4. Khung thời gian 2000–2022 chưa đủ để biết bất đối xứng đã ổn định ở mức mới hay sẽ quay về trước dịch.

## 6. Vai trò trong đề tài

1. **Giải thích nhánh $D < 0$** bằng *loss dominance* — bị dìm điểm vì hụt kỳ vọng, không vì "khách phẫn nộ". Đây là điểm tựa để tránh suy diễn trạng thái tâm lý.
2. **Biện minh cho giả định bất đối xứng** của RQ3, cùng với lớp Kano.
3. **Cho phép nói "tác động biên không tuyến tính"** có bằng chứng, không phải phỏng đoán.
4. **Khoảng trống nó để lại chính là chỗ đề tài chen vào:** bài đo bất đối xứng ở cấp toàn văn bản; đề tài đo ở cấp khía cạnh, có dấu. Xem [`04_two_stage_decision.md`](04_two_stage_decision.md) và [`INDEX.md`](INDEX.md) mục 1.

**Lớp này KHÔNG phải công thức đo của đề tài.** Nó không cho $D$; nó cho lý do để tin rằng quan hệ thuộc tính → điểm số là bất đối xứng.

## 7. Câu hỏi bảo vệ hay gặp

| Câu hỏi | Trả lời ngắn | Căn cứ |
| --- | --- | --- |
| "Hệ số $\lambda$ của các anh là bao nhiêu?" | Bài không dùng $\lambda$; nó đo tỷ số hệ số hồi quy, xấp xỉ 8,64 lần | Mục 1, 3 |
| "Sao không đo mốc tham chiếu cho đúng?" | Không đo được từ review công khai; bài dùng trung bình tháng làm proxy và tự nhận hạn chế này | Mục 2, 5 |
| "Bất đối xứng 8,64 lần áp cho dữ liệu của anh được không?" | Không. Đó là kết quả trên cảm xúc cấp văn bản, mẫu 3–5★ châu Âu; ta chỉ mượn **hướng**, không mượn độ lớn | Mục 3, 5 |
| "Prospect Theory có cần thiết không, Kano đã đủ?" | Kano nói khía cạnh nào phạt nặng; Prospect Theory nói vì sao độ phạt không tuyến tính. Hai câu hỏi khác nhau | [`02_kano_three_factor_iaa.md`](02_kano_three_factor_iaa.md) |
| "Sao không viết 'khách sợ mất mát'?" | Không suy ra trạng thái tâm lý từ review công khai; chỉ nói được về bất đối xứng quan sát trên dữ liệu | [`INDEX.md`](INDEX.md) mục 4 |

## 8. Ranh giới

- Không gán hệ số 8,64 lần cho dữ liệu dự án — chỉ dẫn như bằng chứng về **hướng** bất đối xứng.
- Không suy ra trạng thái tâm lý cá nhân; cơ chế là ở mức tổng hợp, không ở mức người viết.
- Bản local là accepted manuscript: khi trích số trang hoặc nguyên văn, ghi rõ nguồn là bản thảo được chấp nhận.
