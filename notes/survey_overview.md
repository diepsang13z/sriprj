# Tổng quan Khảo sát văn hiến (Survey Overview)

- **Cập nhật:** 2026-09-23 — viết lại thành tổng quan bốn vòng khảo sát (trước là bản mô tả riêng Survey Round 3).
- **Mục đích:** một chỗ để nắm khảo sát đã đi qua những vòng nào, mỗi vòng nhằm gì và thu được gì, và hiện đang dừng ở đâu.
- **Dùng khi:** cần trả lời "nhóm khảo sát tới đâu rồi" mà không phải đọc lại toàn bộ `docs/logs/literature_survey/`.

> **Cảnh báo thẩm quyền:** đây là bản diễn giải, **không phải nguồn sự thật**. Nguồn sự thật là các quyết định trong `docs/decisions/` (`RDR-NNNN`, số lớn nhất thắng). Trạng thái khảo sát hiện được khóa bởi `RDR-0005`.

---

## 1. Vì sao khảo sát theo cách này

Khảo sát không nhằm gom cho thật nhiều bài. Cách làm bị ràng buộc bởi hai quyết định ban hành **trước khi quét**:

| Quyết định | Nội dung |
| --- | --- |
| `RDR-0001` | Bốn tiêu chí dừng: đủ nguyên liệu viết proposal · có baseline đối chứng · đủ 10–15 bài hạt nhân chia đều ba cụm · tiêu chí bão hòa |
| `RDR-0002` | Chỉ quét chủ động trong **cửa sổ 36 tháng**; nguồn cũ hơn chỉ lấy khi là **nguồn gốc của một khái niệm đang dùng**, kèm lý do ghi rõ |

**Bốn nguyên tắc khi đọc:**

1. Ưu tiên tạp chí trước hội nghị và preprint; nguồn đóng được sàng lọc song song nguồn mở.
2. Mỗi DOI xác minh độc lập qua **Crossref** và **OpenAlex**; lệch tiêu đề hoặc năm thì loại, không đoán.
3. Gán **mức bằng chứng I–VII** cho từng nguồn (meta-analysis là I, ý kiến chuyên gia là VII).
4. **Bắt buộc có nhánh phản biện:** phải chủ động tìm bằng chứng chống lại giả thuyết của chính mình, không chỉ tìm nguồn ủng hộ.

---

## 2. Bốn vòng khảo sát

| Vòng | Thời điểm | Chế độ | Kết quả chính |
| --- | --- | --- | --- |
| **1–2** | đến 2026-09-20 | Quét rộng, dựng nền | Ma trận 11 nguồn (vòng 1) + 6 ứng viên hạt nhân mới (vòng 2); sau curation còn **15 bài hạt nhân** trong ba cụm |
| **3** | 2026-09-22 | Targeted theo `RDR-0003` | **9 ứng viên tạp chí**, 0 hội nghị/preprint; RQ3 được tái định hình; 3/9 có toàn văn |
| **4** | 2026-09-23 | **Kiểm chứng**, không mở rộng | **26 nguồn mới** xác minh qua 5 cụm A–E; có nhánh phản biện bắt buộc và kiểm tra tính mới độc lập |

Ba vòng dùng tiêu chí và mục đích khác nhau, nên **không cộng dồn số nguồn giữa các vòng** để ra một số bài duy nhất.

---

## 3. Vòng 1–2 — quét rộng, dựng nền

**Mục đích:** biết bài toán đã được làm tới đâu, có những cách đo nào, và có gì dùng làm baseline được.

**Thu được:**

- Hiện tượng cần nghiên cứu **có thật và không nên xử lý như nhiễu**: điểm sao và cảm xúc văn bản liên quan nhưng không đồng nhất; dùng điểm sao làm nhãn cảm xúc sẽ tạo nhãn yếu.
- **Bốn lớp đo** đã có bằng chứng: lệch phân loại có hướng · độ lớn liên tục · xung đột cấp khía cạnh · chỉ số hợp nhất hình học.
- Phép đo phải giữ **đồng thời độ lớn và chiều**; độ lớn là biến bổ sung, không thay thế chiều.
- **Lý thuyết phải tách actor khỏi outcome**: lý thuyết của *người đọc* review không giải thích được động cơ của *người viết*.
- Baseline kỹ thuật đã đủ: pipeline của bài gốc tái lập được, có benchmark ABSA và bộ luật khía cạnh – cảm xúc.
- **Ứng viên mở rộng của nhóm:** khoảng cách cấp khía cạnh có dấu $D_{i,a}=r_i^*-s_{i,a}^*$ — đây là **đề xuất của nhóm**, không phải công thức chuẩn từ văn hiến.

**Chưa chốt được:** bộ ước lượng cảm xúc · cách chuẩn hóa · ngưỡng phân loại · cách tổng hợp nhiều khía cạnh.

**Chưa đạt endpoint chính thức** vì chưa chứng minh bão hòa và chưa chốt phép đo.

---

## 4. Vòng 3 — tái định hình câu hỏi nghiên cứu

**Mục đích:** kiểm tra lại RQ3 thời điểm đó — *"khách sạn phục vụ tốt có cứu được lỗi cơ sở vật chất không?"*

**Phát hiện:** RQ đó trộn **ba giả định chưa được chứng minh**

1. chỉ có một cặp khía cạnh đáng quan tâm;
2. mọi lỗi cơ sở vật chất có mức nghiêm trọng như nhau;
3. điểm tổng hình thành bằng quan hệ bù trừ tuyến tính.

**Bằng chứng phản bác:** văn hiến phân biệt thuộc tính cơ bản với thuộc tính tạo hài lòng; lý thuyết triển vọng cho thấy mất mát mạnh hơn lợi ích tương đương; một số lỗi có mức phạt vượt khả năng bù.

**Kết quả:** hội tụ về cơ chế **hai nhánh** — chi phối (non-compensatory) và bù trừ (compensatory). Cặp `dịch vụ × cơ sở vật chất` từ chỗ là toàn bộ đề tài nay chỉ còn là **một phép so sánh dự kiến trước**.

Bốn điều kiện biên khả thi với dữ liệu cũng được chốt ở vòng này: cấu hình khía cạnh · mức độ nghiêm trọng · việc khắc phục · hạng sao khách sạn.

---

## 5. Vòng 4 — kiểm chứng và tự phản biện

**Mục đích:** vá hai lỗ hổng bằng chứng (điều kiện biên và baseline) và **tự tấn công kết luận của mình** — không mở rộng đề tài.

**Năm nhóm câu hỏi quét:** vai trò bất đối xứng của khía cạnh · mức độ nghiêm trọng và việc khắc phục · kiểm tra tính mới (điều tra âm tính) · **phản biện** · baseline và prior art.

**Tự phản biện — ba đòn và cách xử lý:**

| Đòn phản biện | Cách xử lý |
| --- | --- |
| Bất nhất có thể là **thiên lệch khi trình bày công khai**, không phải bù trừ thật | Ghi thành **hạn chế nhận dạng**; không tuyên bố nhân quả |
| Bất nhất **phụ thuộc nền tảng**, không phải quy luật chung | Mọi tuyên bố về tỷ lệ phải ghi phạm vi TripAdvisor 2015–2023 |
| **Công cụ phân loại Kano/PRCA có lỗi quy trình**, dễ suy ra bất đối xứng ở nơi thực tế tuyến tính | Phần phân loại khía cạnh chỉ trình bày như **phân tích khám phá**, kèm bất định |

**Kiểm tra tính mới:** không tìm thấy tiền lệ trực tiếp cho thước đo có dấu ở cấp khía cạnh. Kết luận chỉ ở mức *"chưa tìm thấy"*, vì tìm kiếm theo tiêu đề và tóm tắt không chứng minh được sự vắng mặt. Ranh giới tính mới **mỏng**: một nghiên cứu 2026 làm rất gần, chỉ khác đơn vị phân tích.

**Phán quyết:** cơ chế sống sót nhưng **có điều kiện, giới hạn nền tảng, và có ý thức về đo lường**.

---

## 6. Sau bốn vòng, nhóm có gì

**Thư viện tài liệu: 35 tệp toàn văn, xếp theo 8 cụm chức năng.** Core set dùng để viết đề cương là **31 nguồn**, chia ba cụm: hiện tượng & định nghĩa (11) · cơ chế & điều kiện biên (13) · phản biện, phương pháp & baseline (7).

**Năm quyết định đã ban hành:** mục tiêu dừng khảo sát · quy tắc quét cửa sổ 36 tháng · mở lại khảo sát để tái định hình RQ3 · chốt RQ3 · đóng khảo sát và khóa khung.

**Đã khóa theo `RDR-0005`:**

- **Khung lý thuyết:** S-O-R + Kano/ba nhân tố + thuyết triển vọng + quyết định hai giai đoạn.
- **Phạm vi dữ liệu:** 9.990 review đã gán nhãn; không mở rộng lên corpus 782.584 review của bài gốc.
- **Nhánh forgiveness/justice bị loại khỏi lớp lý thuyết trung tâm** và **không được đo** — review công khai không cho phép suy ra trạng thái tâm lý.

---

## 7. Khảo sát dừng ở đâu và vì sao

**Đóng có điều kiện.** Tiêu chí "bão hòa" của `RDR-0001` **không thể đạt** bằng cách quét trong cửa sổ 36 tháng, vì cửa sổ này liên tục sinh công bố mới — đây là lý do cấu trúc, không phải thiếu nỗ lực. `RDR-0005` miễn tiêu chí đó và thay bằng một tiêu chí đo được:

> **Không còn phát hiện nào làm thay đổi thiết kế nghiên cứu.**

Vòng 4 đạt tiêu chí này: trong 26 nguồn mới, không nguồn nào làm đổi cơ chế hay câu hỏi nghiên cứu.

`RDR-0005` đồng thời định nghĩa lại ba cụm tài liệu cho khớp cấu trúc thư mục, và bãi bỏ cụm *Forgiveness/Justice* — cụm đó không còn nội dung sau khi RQ3 đổi hướng.

---

## 8. Còn thiếu gì

| Hạng mục | Trạng thái |
| --- | --- |
| **16 bài đóng** cần thư viện trường hỗ trợ | Ưu tiên 3 bài: Kwon W. 2026 · Han & Anderson · Slevitch |
| **Công thức đo độ lệch** | Chưa chốt — chờ validation trên dữ liệu của nhóm |
| **Bộ ước lượng cảm xúc, chuẩn hóa, ngưỡng** | Chưa chốt — cùng nằm trong validation |
| Nguồn gốc và giấy phép dữ liệu | Chưa khai báo |

Điểm quan trọng: phần tài liệu còn thiếu là **việc kiểm chứng chi tiết phương pháp**, không phải việc khám phá. Nó không chặn bước validation, vì validation chạy trên dữ liệu của nhóm chứ không phụ thuộc paywall.

---

## 9. Đọc chi tiết ở đâu

| Cần gì | Đọc |
| --- | --- |
| Giao thức và ma trận từng vòng | `docs/logs/literature_survey/0002`, `0003`, `0005`, `0006` |
| Tổng kết bằng chứng và điểm còn mở sau vòng 1–2 | `docs/logs/literature_survey/0004_synthesis_and_next_step.md` |
| Lý do đóng khảo sát và định nghĩa lại cụm | `docs/decisions/RDR-0005_close_survey_and_lock_framework.md` |
| Trạng thái toàn văn từng nguồn | `refs/INDEX.md` mục 9 |
| Vai trò từng nguồn trong đề tài | `notes/reference_map.md` |
| Bối cảnh đề tài | `notes/project_overview.md` |
