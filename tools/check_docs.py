#!/usr/bin/env python3
"""Bộ kiểm trước khi commit cho tài liệu Markdown của dự án.

Bốn lớp, đều là lỗi im lặng — kiểm bằng mắt không bắt được:

  1. Link nội bộ hỏng (đường dẫn tương đối trỏ sai).
  2. Bảng Markdown lệch số ô (GitHub cắt ô tại mỗi `|`, kể cả `|` nằm trong
     code span hoặc trong công thức — dùng `\\lvert`/`\\rvert` hoặc `\\|`).
  3. Backtick lẻ trên một dòng (inline code không đóng).
  4. Mẫu escape còn sót trong văn xuôi (`\\1`, `\\n`, `\\t`) — dấu vết của
     lần thay thế bằng regex bị escape sai.

Chỉ đọc, không sửa gì. Dùng:  python tools/check_docs.py
Quy tắc: RULES.md mục 2. Bản markdown dẫn xuất từ PDF ở `refs/<cụm>/md/`
được bỏ qua — đó là nội dung của nguồn, không phải của nhóm.
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "data"}
SKIP_PATHS = re.compile(r"refs/\d\d_[a-z_]+/md/")
FENCE = re.compile(r"^\s*```")
ESCAPE = re.compile(r"\\[0-9nt](?![A-Za-z])")


def markdown_files() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT).replace("\\", "/")
            if not SKIP_PATHS.search(rel):
                out.append(rel)
    return sorted(out)


def report(kind: str, rel: str, line: int, detail: str, issues: list) -> None:
    issues.append((kind, rel, line, detail))


def check_links(rel: str, lines: list[str], issues: list) -> None:
    for i, text in enumerate(lines, 1):
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(os.path.join(ROOT, rel)), target.split("#")[0]))
            if not os.path.exists(path):
                report("link", rel, i, target, issues)


def check_tables(rel: str, lines: list[str], issues: list) -> None:
    block: list[tuple[int, int]] = []
    for i, text in enumerate(lines + [""], 1):
        if text.lstrip().startswith("|"):
            block.append((i, len(re.split(r"(?<!\\)\|", text.strip().strip("|")))))
            continue
        if len(block) > 1:
            widths = {cells for _, cells in block}
            if len(widths) > 1:
                report("bảng", rel, block[0][0], f"dòng {block[0][0]}–{block[-1][0]} có số ô {sorted(widths)}", issues)
        block = []


def check_inline(rel: str, lines: list[str], issues: list) -> None:
    for i, text in enumerate(lines, 1):
        if FENCE.match(text):
            continue
        if text.count("`") % 2:
            report("backtick", rel, i, text.strip()[:80], issues)


def check_escapes(rel: str, text: str, issues: list) -> None:
    for match in ESCAPE.finditer(text):
        before = text[match.start() - 1] if match.start() else ""
        if before.isalnum() or before in "_\\/":      # đường dẫn Windows: docs\logs\validation\0001
            continue
        report("escape", rel, text.count("\n", 0, match.start()) + 1, text[max(0, match.start() - 30):match.start() + 20].strip(), issues)


def main() -> int:
    files = markdown_files()
    issues: list = []
    for rel in files:
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        lines = text.split("\n")
        check_links(rel, lines, issues)
        check_tables(rel, lines, issues)
        check_inline(rel, lines, issues)
        check_escapes(rel, text, issues)

    for kind, rel, line, detail in issues:
        print(f"  [{kind}] {rel}:{line}  {detail}")
    print(f"quet {len(files)} tep .md · loi: {len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
