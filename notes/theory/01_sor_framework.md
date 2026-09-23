# 01 — Khung S-O-R: Stimulus · Organism · Response

**Vai trò:** lớp vĩ mô, kế thừa nguyên trạng từ bài gốc Le et al. (2026, IJHM). Đây là lớp duy nhất trong bốn lớp mà đề tài **không** sửa — nó vẫn đúng, chỉ thiếu.
**Nguồn chính:** [`refs/01_root/md/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on_online_hotel_ratings.md`](../../refs/01_root/md/2026_unlocking_insights_into_customer_sentiment_analysis_impact_of_loyalty_on_online_hotel_ratings.md) — bản markdown toàn văn, tra theo § và Table.

---

## 1. Lớp này làm gì cho đề tài

1. Nối đề tài vào một dòng nghiên cứu đã có, nên không phải tự dựng khung.
2. Quan trọng hơn: nó **tách $O$ khỏi $R$**. Cảm xúc nội tại ($O$) và hành vi chấm điểm ($R$) là hai thứ khác nhau, nên chúng có thể lệch nhau. Khoảng lệch đó chính là biến phụ thuộc của đề tài.

Nếu bỏ lớp này, câu hỏi "vì sao văn và điểm không khớp" mất chỗ đứng về mặt khái niệm — khi đó rating bị ngầm coi là thước đo cảm xúc, đúng cái sai mà đề tài phản biện.

## 2. Nội dung cốt lõi

Chuỗi một chiều: **kích thích ($S$) → trạng thái nội tại ($O$) → phản ứng ($R$)**. Định nghĩa vận hành theo bài gốc: kích thích từ trải nghiệm khách hàng tác động lên trạng thái tâm lý nội tại, rồi định hình phản ứng đánh giá hành vi (bài gốc §3.4).

Ánh xạ biến trong bài gốc (bài gốc §1.2, §3.4, Table 1):

| Thành phần | Biến | Đo bằng |
| --- | --- | --- |
| $S$ | `Facility` · `Amenity` · `Service` | Cực tính cảm xúc VADER theo cụm chủ đề BERTopic |
| $O$ | `Experience Value` · `Loyalty` | Cực tính cảm xúc VADER trên cụm chủ đề tương ứng |
| $R$ | `CoRe` | Nhị phân hài lòng / không hài lòng từ điểm tổng |

Ngưỡng `CoRe`: Booking.com $\ge 7$ là hài lòng; TripAdvisor $\ge 4$ là hài lòng (bài gốc §3.4).

**Đừng lẫn hai nhát cắt:** `CoRe` là ngưỡng $\ge 4$ của bài gốc. Nhóm "review 5★" mà đề tài dùng — 7.148 review, nơi 394 ca bất nhất được đếm — là nhát cắt khác, điểm **đúng bằng 5** ([`RDR-0006`](../../docs/decisions/RDR-0006_freeze_negative_span_definition.md) mục 2.1).

## 3. Bài gốc vận hành cụ thể

- **Mô hình:** hồi quy logistic có trọng số (WMLR), biến phụ thuộc $\log(\text{CoRe})$, 15 biến độc lập = 5 khía cạnh × 3 cực tính (bài gốc Eq. 1, §3.4).
- **Vì sao có trọng số:** nhãn lệch nặng — Booking 67% tích cực so với 12% tiêu cực; TripAdvisor 68% so với 9% (bài gốc §3.4, §4.4).
- **Hai phương trình riêng cho hai nền tảng:** Eq. 2a (Booking) và Eq. 2b (TripAdvisor).

## 4. Bốn kết quả cần nhớ (để dẫn lại, không để học thuộc)

1. **`Loyalty` có hệ số lớn nhất ở cả hai nền tảng:** $+2{,}7410$ trên Booking và $-2{,}0086$ trên TripAdvisor (bài gốc Eq. 2a–2b, §4.4).
2. **Bất đối xứng đã xuất hiện ngay trong bài gốc.** `Facility`: Booking $\beta_{neg} = -1{,}0778$ so với $\beta_{pos} = +0{,}8424$; TripAdvisor $\beta_{neg} = -1{,}1661$ so với $\beta_{pos} = +0{,}4459$. Chiều âm mạnh hơn chiều dương.
3. **Nền tảng phân kỳ:** Booking nghiêng về thổi phồng tích cực, TripAdvisor nghiêng về phạt tiêu cực (bài gốc §4.4).
4. **Phạt cả mức trung tính** trên TripAdvisor: `ServNeu` $-0{,}7224$, `ExpNeu` $-0{,}5466$, `FacNeu` $-0{,}5403$, đều $p < 0{,}05$ (bài gốc Eq. 2b, §4.4).

## 5. Ba chỗ khung gãy — và đây là lý do ba lớp còn lại tồn tại

### 5.1. Vòng luẩn quẩn `Loyalty` → `CoRe`

Từ khóa tạo nên biến `Loyalty` là các ý định hành vi: *revisit, back, recommend, again, stay away, never again* (bài gốc §3.1). Biến phụ thuộc `CoRe` là điểm tổng. Hai thứ này cùng bản chất: người viết *"never again"* gần như chắc chắn chấm 1 sao.

Chính bài gốc cũng lảng tránh quan hệ nhân quả, viết rằng loyalty "co-develops" và "amplifies or attenuates" thay vì đứng trước sự hài lòng (bài gốc §5.2, §6). **Hệ số lớn nhất của mô hình vì thế là hệ quả cơ học, không phải phát hiện nhân quả.**

Đây là điểm phản biện trung tâm của đề tài, và cũng là lý do dữ liệu dự án loại span `Loyalty` (4.293 span) và `Branding` (1.339 span — span có câu khách tự viết số sao, rủi ro rò rỉ nhãn). Xem [`../glossary.md`](../glossary.md) mục 3 và [`RDR-0006`](../../docs/decisions/RDR-0006_freeze_negative_span_definition.md).

### 5.2. Bốn kết quả ở mục 4 không được khung giải thích

S-O-R **ghi nhận** chúng qua số liệu, nhưng không có cơ chế nói vì sao: (a) âm mạnh hơn dương; (b) hai nền tảng lệch nhau; (c) trung tính bị phạt; (d) tác động biên không tuyến tính. Bài gốc không đề cập Kano, Prospect Theory, hay cấu trúc bù trừ/phi bù trừ — ba lớp sau lấp đúng bốn lỗ này.

### 5.3. Lỗ hổng provenance

Bài gốc **không** viện dẫn công trình khởi nguyên của S-O-R; nó chỉ dẫn các nghiên cứu ứng dụng gần đây (Liu et al. 2021; Fan et al. 2023; Şanlıöz-Özgen & Kozak 2023; El-Adly 2019 — bài gốc §3.4). [`../glossary.md`](../glossary.md) mục 2 thì ghi nguồn gốc là Mehrabian & Russell (1974).

Hệ quả thực hành: **chưa có bản gốc S-O-R nào trong `refs/`**. Muốn trích bản gốc, chọn một trong hai: trích qua nguồn thứ cấp và ghi rõ là trích dẫn lại, hoặc đưa vào hàng đợi lấy toàn văn ở [`refs/INDEX.md`](../../refs/INDEX.md) mục 9. Đừng trích như đã đọc.

## 6. Câu hỏi bảo vệ hay gặp

| Câu hỏi | Trả lời ngắn | Căn cứ |
| --- | --- | --- |
| "S-O-R chỉ là ba chữ, có gì đáng dùng?" | Giá trị của nó là tách $O$ khỏi $R$; nếu gộp, biến phụ thuộc của đề tài biến mất | Mục 1 |
| "Vậy sao không bỏ luôn bài gốc?" | Bài gốc là đối chuẩn: cùng pipeline, cùng nền tảng, cùng dữ liệu VN — và là chỗ để chỉ ra lỗi vòng | Mục 5.1 |
| "Anh bỏ `Loyalty` vì nó bất lợi cho mình?" | Bỏ vì circularity; `Loyalty` vẫn được đếm và báo cáo trong dữ liệu, chỉ không vào mô hình | Mục 5.1 |
| "Bất đối xứng có trong bài gốc không?" | Có, ở `Facility` và toàn bộ TripAdvisor; bài gốc chỉ không giải thích nó | Mục 4, 5.2 |
| "S-O-R có kiểm định được không?" | Không theo nghĩa mô hình nhân quả; nó là khung định vị. Ba lớp sau mới là phần kiểm định được | Mục 1, 5.2 |

## 7. Ranh giới

- **Không** viết "khách tha thứ", "khách phẫn nộ" — $O$ không quan sát được từ review công khai. Xem [`INDEX.md`](INDEX.md) mục 4.
- `CoRe` là **hài lòng/không hài lòng nhị phân**, không phải "điểm cao". Nói "5 sao" là quy chiếu nhóm dữ liệu của dự án, không phải định nghĩa `CoRe` của bài gốc.
- Toàn bộ đường dẫn và hệ số ở trên trích từ bản markdown; muốn nguyên văn thì mở chính file đó, **không** mở PDF 5,4 MB.
