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
| `refs/` | Thư viện **35 PDF** xếp theo 8 cụm chức năng; mỗi cụm có `SOURCES.md` (dữ liệu) và `INDEX.md` (bản chụp) |
| `reports/` | Báo cáo và bài trình bày của môn — `templates/`, `md/`, `presen/` |
| `data/` | Dataset — **không nằm trong git**, xem mục dưới |

## Lấy dữ liệu về

Repo **không chứa dataset**. Phải tải thủ công một lần:

| | |
| --- | --- |
| Tệp | `data/TripAdvisor_EN.json` |
| Nguồn | repo GitHub `Hanhlevna/Manhos` — nhóm tác giả bài báo gốc Le et al. (2026) |
| Kích thước | 43.105.400 bytes (≈ 41,1 MB) |
| SHA-256 | `4b655618b860ab7c128b87cf732862336a4546b34b81f40a5b93ce424981a71d` |

Kiểm tra sau khi tải:

```
sha256sum data/TripAdvisor_EN.json
```

Số in ra phải khớp chuỗi SHA-256 ở bảng trên. Lệch nghĩa là khác bản — và mọi con số thống kê trong tài liệu sẽ không tái lập được.

## Làm việc nhóm

Mỗi người một nhánh `<tên>/work` và mở pull request vào `main`. **Không commit thẳng vào `main`.** Chi tiết ở [`RULES.md`](RULES.md) mục 2.
