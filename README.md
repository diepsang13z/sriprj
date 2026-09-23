# Bất nhất cảm xúc – điểm số trong review khách sạn

Đề tài nghiên cứu hiện tượng **"nói một đằng, chấm một nẻo"** trong review khách sạn: khách phàn nàn về một khía cạnh cụ thể mà vẫn cho 5 sao, hoặc khen ngợi hầu hết khía cạnh mà vẫn cho 1–2 sao. Nhóm lấy chính những ca đó làm đối tượng nghiên cứu, thay vì coi là nhiễu dữ liệu để loại bỏ.

Môn DAP391m (AI & Data Science) — học kỳ Fall 2026.

## Bắt đầu từ đâu

| Bạn là | Đọc theo thứ tự |
| --- | --- |
| **Agent** | [`AGENTS.md`](AGENTS.md) — tệp này tự nạp, chứa protocol đọc 5 bước |
| **Người mới vào dự án** | [`docs/INDEX.md`](docs/INDEX.md) → [`RULES.md`](RULES.md) → [`STATUS.md`](STATUS.md) → [`docs/BACKLOG.md`](docs/BACKLOG.md) |
| **Chỉ muốn biết đề tài** | [`notes/project_overview.md`](notes/project_overview.md) |

## Cấu trúc thư mục

| Thư mục | Nội dung |
| --- | --- |
| `docs/` | Router (`INDEX.md`), quyết định (`decisions/`), việc đang mở (`BACKLOG.md`), nhật ký (`logs/`) |
| `notes/` | Note định hướng: tổng quan đề tài, khảo sát văn hiến, bản đồ ref, thuật ngữ |
| `refs/` | Thư viện **35 PDF** xếp theo 8 cụm chức năng; mỗi cụm có `SOURCES.md` (dữ liệu), danh mục chung ở `refs/INDEX.md` |
| `reports/` | Báo cáo và bài trình bày của môn — `templates/`, `md/`, `presen/` |
| `data/` | Dataset — **không nằm trong git**, xem mục dưới |

## Nhận dữ liệu về

Repo **không chứa dataset** — thư mục `data/` bị gitignore. Tệp do **nhóm dự án chia sẻ qua kênh chung của nhóm**, không tải từ nguồn công khai. Liên hệ nhóm trưởng để nhận, rồi đặt vào thư mục `data/` ở gốc repo.

| | |
| --- | --- |
| Tệp | `data/TripAdvisor_EN.json` |
| Kích thước | 43.105.400 bytes (≈ 41,1 MB) |
| SHA-256 | `4b655618b860ab7c128b87cf732862336a4546b34b81f40a5b93ce424981a71d` |
| Nguồn | **Giảng viên môn học cung cấp**, nhóm dự án chia sẻ lại. Nhóm có quyền sử dụng trong phạm vi môn DAP391m. |
| Ghi chú | Tập dữ liệu gốc thuộc nhóm tác giả Le et al. (2026). Bài báo công bố repo `github.com/Hanhlevna/Manhos`, nhưng kiểm ngày 2026-09-23 thì repo chỉ có `data_Booking.com.csv` — **không có tệp TripAdvisor**. Bản đang dùng vì thế không tải lại được từ đó, nên checksum là định danh duy nhất. |

Khi nộp Final Report, khai báo nguồn dữ liệu theo dòng **Nguồn** ở trên.

Sau khi nhận, kiểm tra:

```
sha256sum data/TripAdvisor_EN.json
```

Số in ra phải khớp chuỗi SHA-256 ở bảng trên. Lệch nghĩa là khác bản — và mọi con số thống kê trong tài liệu sẽ không tái lập được.

## Làm việc nhóm

Mỗi người một nhánh `<tên>/work` và mở pull request vào `main`. **Không commit thẳng vào `main`.** Chi tiết ở [`RULES.md`](RULES.md) mục 2.
