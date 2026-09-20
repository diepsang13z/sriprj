# Project Status Snapshot

_Cập nhật lần cuối: 2026-09-20 | Trạng thái: Khám phá có kiểm soát_

---

## 1. Giai đoạn Hiện tại & Trạng thái Đề tài
* **Trạng thái đề tài:** **ĐANG KHÁM PHÁ / CHƯA CHỐT CHÍNH THỨC (Exploratory Phase)**.
* **Tiến độ:** Đã hoàn tất Survey Round 2 và synthesis `0004`; core set còn 15 nguồn, đủ theory/measure/baseline để chuyển sang targeted validation nhưng chưa đạt saturation.

## 2. Research Questions (Chưa chốt — Đang định hình)

* Hiện chưa chốt RQs chính thức; đang trong giai đoạn brainstorm và khảo sát văn hiến.
* Một số hướng giả thuyết tiềm năng đang thảo luận trong `docs/logs/brainstorm/0001_root_idea.md`:
  * Mâu thuẫn cảm xúc - điểm số (Sentiment–Rating Inconsistency / Discrepancy).
  * Tái định nghĩa Loyalty thành Sublimation (Thăng hoa / Vị tha) & Anger (Phẫn nộ / Trừng phạt).
  * Vai trò điều tiết / "tấm đệm" (Buffering Effect) của Service hoặc Sublimation trước các lỗi cơ sở vật chất.
* Round 2 xác nhận ba lớp đo: continuous magnitude, directional class và absolute aspect-level conflict; signed aspect discrepancy vẫn là candidate extension.

## 3. Quyết định Kỹ thuật đã chốt (Decisions)

- Đã chốt `RDR-0001`: Mục tiêu và tiêu chí dừng khảo sát văn hiến (Literature Survey Endpoint).
- Đã chốt `RDR-0002`: Chỉ quét chủ động bài trong cửa sổ 36 tháng mới nhất; nguồn cũ chỉ truy xuất theo citation chain có lý do.
- Survey Round 2 dừng broad search tạm thời vì core set đã chạm ngưỡng 15; chưa ban hành `RDR-0003`.

## 4. Việc tiếp theo (Next Steps)

1. Khảo sát cấu trúc nhãn trong `data/TripAdvisor_EN.json` và phân loại 402 mẫu 5 sao chứa negative span.
2. So sánh magnitude, direction và signed aspect discrepancy trên mẫu đã gắn nhãn; chốt sentiment estimator, normalization và threshold.
3. Ban hành `RDR-0003` sau validation; sau đó soạn Research Proposal.
