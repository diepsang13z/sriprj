# 04 — Cấu trúc quyết định hai giai đoạn: Non-compensatory → Compensatory

**Vai trò:** lớp **cấu trúc** — nói điểm tổng được cộng gộp theo trình tự nào, chỗ nào bị cắt tỉa. Đây là lớp trực tiếp sinh ra hai nhánh của RQ3.
**Nguồn chính:** [`refs/04_mechanism/md/2024_li_two_stage_satisfaction_decision_model.md`](../../refs/04_mechanism/md/2024_li_two_stage_satisfaction_decision_model.md) — Li, S., Zhu, B., Zhang, Y., Liu, F., & Yu, Z. (2024), JTAER 19(1), 272–296.
**Nguồn phụ:** [`refs/04_mechanism/md/2024_wang_attribute_performance_satisfaction.md`](../../refs/04_mechanism/md/2024_wang_attribute_performance_satisfaction.md) · [`refs/04_mechanism/md/2026_ozturk_aspect_sentiment_high_utility_rules.md`](../../refs/04_mechanism/md/2026_ozturk_aspect_sentiment_high_utility_rules.md)

---

## 1. Cấu trúc hai giai đoạn, phát biểu chính xác

Bài của Li et al. (2024) §5.1.1, §5.1.3, Fig. 4 mô tả:

**Giai đoạn 1 — Non-compensatory (loại bỏ, không bù trừ).** Áp dụng quy tắc *elimination-by-aspects* (EBA) lên nhóm thuộc tính bắt buộc (*must-be*). Người tiêu dùng đặt ngưỡng thỏa mãn $q_i$ cho từng thuộc tính cơ bản. Nếu tồn tại **bất kỳ** thuộc tính nào dưới ngưỡng ($\exists \varphi_i < q_i$) thì kết cục bị khoá ở mức không hài lòng $Q_2$; chỉ khi **mọi** thuộc tính cơ bản đạt ngưỡng ($\forall \varphi_i \ge q_i$) mới được mức $Q_1 > Q_2$. Điểm yếu ở thuộc tính cơ bản **không thể** được bù bởi điểm mạnh ở thuộc tính khác.

**Giai đoạn 2 — Compensatory (bù trừ).** Tính thỏa dụng bổ sung $\omega_{utility}$ trên bốn nhóm Kano còn lại (*attractive, one-dimensional, indifferent, reverse*); các thuộc tính được phép bù trừ lẫn nhau, rồi cộng vào kết quả giai đoạn 1:

$$y = \omega_{EBA} + \omega_{utility}$$

Cần đọc đúng hai chữ "ngưỡng": giai đoạn 1 là một **điều kiện logic** (đạt/không đạt), không phải một trọng số lớn. Đó là lý do một lỗi ở thuộc tính cơ bản không bị "pha loãng" bởi các khía cạnh tốt khác.

## 2. Kiểm định và kết quả

| Hạng mục | Li et al. (2024) |
| --- | --- |
| Mô hình | USDM = EBA + Kano utility, tối ưu bằng thuật toán di truyền (GA) trên không gian tham số phi tuyến |
| Dữ liệu | 89.768 đánh giá hợp lệ, 50 mẫu smartphone, JD.com, 01/2020–09/2020 (80/20 train–test) |
| Kết quả | Test MSE $0{,}000538$ — thấp nhất trong 13 mô hình so sánh; MLR $0{,}000581$, GRNN $0{,}000556$, SVM $0{,}001126$, BPNN $0{,}006893$ |
| $R^2$ | USDM $0{,}052719$ so với MLR $0{,}033737$ |

Cấu trúc hai giai đoạn được ủng hộ, nhưng lưu ý **độ lớn**: $R^2$ của USDM chỉ $0{,}0527$ — trong khi BPNN đạt $0{,}4609$ (Bảng 5). Mô hình hai giai đoạn thắng ở **sai số kiểm tra**, không thắng ở khả năng giải thích phương sai. Đừng trình bày con số này như bằng chứng mạnh.

Bằng chứng bên trong bài cho thấy thuộc tính *must-be* có hệ số phạt vượt trội hệ số thưởng ($\beta^{neg} > \sigma\beta^{pos}$, với $\vartheta = 0{,}001$, $\sigma = 4{,}5$), ví dụ Signal $\beta^{pos} = 0{,}0019$ so với $\beta^{neg} = 0{,}2446$ (§4.3.2, §5.1.2, Bảng 3–4).

## 3. Bằng chứng tương đương ở bối cảnh khách sạn

Hai bài không dựng công thức hai giai đoạn, nhưng phát hiện **đúng cấu trúc đó** trên dữ liệu review khách sạn:

**Wang et al. (2024)** — 297.244 review, 423 khách sạn New York, TripAdvisor 2007–2023; XGBoost + SHAP + PRCA và AIPA động (§3.1–§3.2, §4.1–§4.3):

- Phân tầng: 3 thuộc tính Base (Value, Cleanliness, Sleep quality), 1 Performance (Service), 2 Excitement (Rooms, Location).
- Thứ tự ưu tiên phân bổ nguồn lực theo AIPA: $LB > LP > LE > HB > HP > HE$.
- **Biến động thời gian là phát hiện riêng của bài:** Cleanliness chuyển từ High-Performance sang High-performance Basic năm 2020 rồi Low-performance Basic năm 2021 — kỳ vọng vệ sinh tăng thành chuẩn bắt buộc trong dịch. Service và Location tụt từ HE xuống HP năm 2020. Trước dịch, Value và Sleep quality dần chuyển từ Excitement/Performance thành Base khi thị trường chuẩn hoá.

**Öztürk (2026)** — 11.275 review, 14 khách sạn 5★ tại Kuşadası, Thổ Nhĩ Kỳ 2022–2024; khai phá luật khía cạnh–cảm xúc hữu ích cao (§IV-B, §V, §VI):

- 1–2★: **bó lỗi đồng xuất hiện** — ví dụ $\{Room\ Comfort\ and\ Facilities(-), Staff\ and\ Front\text{-}Desk\ Service(-)\}$ dẫn tới lớp 1 (driver score $1.664$) và lớp 2 ($1.222$). Tương ứng giai đoạn không bù trừ.
- 3★: **đánh đổi bù trừ** — $\{Food\ and\ Dining(-), Room\ and\ Facilities(-)\}$ dẫn tới lớp 3, thường đi kèm $\{Location(+)\}$ hoặc $\{Beach\ and\ Sea(+)\}$.
- 4–5★: **tương hỗ tích cực** — $\{Room(+), Staff(+)\}$ dẫn tới lớp 5 với driver score $2.175$, cao nhất nghiên cứu; xuất hiện thêm yếu tố vượt trội (Entertainment).
- 2.922 luật hữu ích cao, trong đó 2.904 luật kích hoạt được trên tập đánh giá; độ phủ (coverage) $0{,}981$ ở cấu hình chuẩn; Accuracy $0{,}665$, Macro-F1 $0{,}462$ (baseline mạnh nhất BERT+LRCV: $0{,}698$ / $0{,}473$).

## 4. Vai trò trong đề tài

1. **Sinh hai nhánh của RQ3.** Non-compensatory/penalty-dominant là giai đoạn 1; compensatory là giai đoạn 2 ([`RDR-0004`](../../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) mục 2.2).
2. **Chặn mô hình tuyến tính một hệ số.** Thay vào đó là quan hệ có ngưỡng, có thứ tự ưu tiên — Wang et al. đã chứng minh quan hệ này phi tuyến và **đổi theo thời gian**.
3. **Cho phép đọc các ca cực đoan mà không cần tâm lý học:** review 5★ kèm một span tiêu cực không nhất thiết là "khách tha thứ" — có thể là lúc chấm, mọi thuộc tính cơ bản đều đạt ngưỡng nên giai đoạn 1 đã qua và điểm vẫn ở mức cao. *Đây là suy luận của nhóm, chưa kiểm định;* nó chỉ có tác dụng như cách diễn giải không vi phạm [`INDEX.md`](INDEX.md) mục 4, không phải một phát hiện.
4. **Gợi ý thiết kế kiểm định:** tìm ngưỡng và cấu trúc bó lỗi (Öztürk) là hướng phân tích khám phá cho RQ3, nhưng **chưa** là quyết định phương pháp — công thức $D$ vẫn chờ validation study ([`RDR-0004`](../../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) mục 3.2).

## 5. Giới hạn phải nói khi trích

| Nguồn | Giới hạn |
| --- | --- |
| Li et al. (2024) | **Khác domain** — review sản phẩm (smartphone), không phải khách sạn; chỉ dùng làm *supporting method*, không phải bằng chứng hospitality |
| Li et al. (2024) | Mô hình hợp nhất cho sản phẩm giá trị cao, nhiều thuộc tính; sản phẩm mua theo thói quen chỉ cần giai đoạn 1 |
| Li et al. (2024) | Không theo thời gian; không tích hợp đặc điểm cá nhân người tiêu dùng |
| Wang et al. (2024) | Chỉ 6 thuộc tính dạng số định sẵn; bỏ qua văn bản phi cấu trúc và hình ảnh |
| Öztürk (2026) | Chỉ 14 khách sạn 5★ ven biển; không đại diện phân bố hạng sao của dữ liệu dự án; chưa kiểm tra đa nền tảng, đa điểm đến |

Ghi thêm: mức bằng chứng của Li et al. (2024) đang **lệch giữa các tài liệu** — ma trận Round 3 ghi mức VI, bảng trụ cột tính như mức IV. Việc này đang mở ở [`docs/BACKLOG.md`](../../docs/BACKLOG.md) việc #6; đừng chốt thay nhóm.

## 6. Câu hỏi bảo vệ hay gặp

| Câu hỏi | Trả lời ngắn | Căn cứ |
| --- | --- | --- |
| "Sao dùng mô hình của một bài ngoài ngành?" | Dùng **cấu trúc**, không dùng bằng chứng; bằng chứng hospitality lấy từ Wang et al. và Öztürk | Mục 3, 5 |
| "Ngưỡng $q_i$ lấy ở đâu ra?" | Đó là tham số của mô hình gốc, tối ưu bằng GA. Đề tài chưa chốt ngưỡng nào — đang chờ validation study | Mục 1, 4 |
| "Hai giai đoạn có phải hai mô hình không?" | Không. Một hàm mục tiêu $y = \omega_{EBA} + \omega_{utility}$; giai đoạn 1 là điều kiện logic | Mục 1 |
| "Nếu mọi khía cạnh đều tốt thì sao?" | Vẫn là giai đoạn 2 quyết định phần vượt trên ngưỡng; phần bù trừ chỉ có hiệu lực sau khi giai đoạn 1 đã qua | Mục 1 |
| "Öztürk chỉ có 14 khách sạn 5★, tin được không?" | Đủ để nói về **dạng** quan hệ ở phân khúc cao cấp, không đủ để khái quát; phải ghi rõ khi trích | Mục 5 |

## 7. Ranh giới

- **Không** viết "khách sạn này non-compensatory" như một kết luận kiểm định. Đó là **dạng quan hệ đang xét**, và kết quả nằm ở kiểm định phụ #1 — phải báo cáo kèm bất định.
- **Không** viết "penalty luôn thắng"; cả hai nhánh đều có điều kiện (xem [`INDEX.md`](INDEX.md) mục 4 điều 2).
- Cấu trúc hai giai đoạn là **khung giải thích**, không phải công thức $D$ của đề tài.
