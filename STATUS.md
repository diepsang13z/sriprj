# Project Status Snapshot

_Cập nhật lần cuối: 2026-09-20 | Trạng thái: Đang khởi động (Kickoff)_

---

## 1. Giai đoạn Hiện tại & Trạng thái Đề tài
* **Trạng thái đề tài:** **ĐANG KHÁM PHÁ / CHƯA CHỐT CHÍNH THỨC (Exploratory Phase)**.
* **Tiến độ:** Khởi động dự án, bóc tách bài báo gốc (`refs/root/...`), nhận diện các hạn chế phương pháp luận (lập luận vòng ở biến Loyalty), khảo sát dataset (`data/TripAdvisor_EN.json`), chuẩn bị khung Research Questions (RQs) và khảo sát văn hiến.

## 2. Research Questions (Chưa chốt — Đang định hình)

* Hiện chưa chốt RQs chính thức; đang trong giai đoạn brainstorm và khảo sát văn hiến.
* Một số hướng giả thuyết tiềm năng đang thảo luận trong `docs/logs/brainstorm/0001_root_idea.md`:
  * Mâu thuẫn cảm xúc - điểm số (Sentiment–Rating Inconsistency / Discrepancy).
  * Tái định nghĩa Loyalty thành Sublimation (Thăng hoa / Vị tha) & Anger (Phẫn nộ / Trừng phạt).
  * Vai trò điều tiết / "tấm đệm" (Buffering Effect) của Service hoặc Sublimation trước các lỗi cơ sở vật chất.
## 3. Quyết định Kỹ thuật đã chốt (Decisions)

- Đã chốt `RDR-0001`: Mục tiêu và tiêu chí dừng khảo sát văn hiến (Literature Survey Endpoint).

## 4. Việc tiếp theo (Next Steps)

1. Khảo sát cấu trúc nhãn chi tiết trong `data/TripAdvisor_EN.json` và phân loại 402 mẫu 5 sao chứa negative span.
2. Tìm kiếm và bổ sung tài liệu liên quan về _Score-Textual Inconsistency_ vào `docs/logs/literature-survey/` và `refs/INDEX.md`.
3. Soạn thảo tài liệu đề xuất nghiên cứu (Research Proposal draft) theo mẫu tại `reports/templates/`.
4. Ban hành quyết định kỹ thuật `RDR-0002` chốt cấu trúc pipeline nghiên cứu sau khi khảo sát đạt endpoint.
