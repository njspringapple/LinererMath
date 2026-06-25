from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXAM_DIR = ROOT / "历史考试"
TEXT_DIR = EXAM_DIR / "文本抽取"


def main():
    TEXT_DIR.mkdir(exist_ok=True)
    files = sorted([p for p in EXAM_DIR.iterdir() if p.is_file() and p.suffix.lower() in {".pdf", ".md"}])
    for p in files:
        out = TEXT_DIR / f"{p.stem}.txt"
        if p.suffix.lower() == ".pdf":
            subprocess.run(["pdftotext", "-layout", str(p), str(out)], check=False)
        else:
            out.write_text(p.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"{p.name} -> {out.name} ({out.stat().st_size if out.exists() else 0} bytes)")


if __name__ == "__main__":
    main()
