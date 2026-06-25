from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_TEXT_DIR = ROOT / "tmp_practice_text_raw"
TEXT_DIR = RAW_TEXT_DIR if RAW_TEXT_DIR.exists() else ROOT / "tmp_practice_text"
EXAM_TOPIC_DIR = ROOT / "\u5386\u53f2\u8003\u8bd5" / "\u6309\u77e5\u8bc6\u70b9\u6c47\u603b"
OUT_DIR = ROOT / "\u5386\u53f2\u7ec3\u4e60\u9898"


MANUAL_OVERRIDES = {
    ("SS23 blatt 07", "2", "Spaltenraum"): {
        "zh_question": """判断 $b$ 是否属于矩阵 $A$ 的列空间（Spaltenraum）。如果属于，请把 $b$ 表示成 $A$ 的列向量的线性组合（Linearkombination）。

**(a)**

$$
A=
\\begin{pmatrix}
1&3\\\\
4&-6
\\end{pmatrix},
\\qquad
b=
\\begin{pmatrix}
-2\\\\
10
\\end{pmatrix}.
$$

**(b)**

$$
A=
\\begin{pmatrix}
1&1&2\\\\
1&0&1\\\\
2&1&3
\\end{pmatrix},
\\qquad
b=
\\begin{pmatrix}
-1\\\\
0\\\\
2
\\end{pmatrix}.
$$

**(c)**

$$
A=
\\begin{pmatrix}
1&-1&1\\\\
9&3&1\\\\
1&1&1
\\end{pmatrix},
\\qquad
b=
\\begin{pmatrix}
5\\\\
1\\\\
-1
\\end{pmatrix}.
$$""",
        "de_solution": """Lösung:

Wir prüfen jeweils, ob das lineare Gleichungssystem $Ax=b$ lösbar ist. Wenn $x=(x_1,\ldots,x_n)^T$ eine Lösung ist, dann gilt

$$
b=x_1a_1+\cdots+x_na_n,
$$

wobei $a_1,\ldots,a_n$ die Spalten von $A$ sind.

**(a)**

Seien

$$
a_1=
\\begin{pmatrix}
1\\\\
4
\\end{pmatrix},
\\qquad
a_2=
\\begin{pmatrix}
3\\\\
-6
\\end{pmatrix}.
$$

Gesucht sind $\lambda,\mu\in\mathbb R$ mit

$$
\lambda a_1+\mu a_2=b.
$$

Das ergibt

$$
\\begin{aligned}
\lambda+3\mu&=-2,\\\\
4\lambda-6\mu&=10.
\\end{aligned}
$$

Aus $\lambda=-2-3\mu$ folgt

$$
4(-2-3\mu)-6\mu=10,
$$

also

$$
-8-18\mu=10,\qquad \mu=-1.
$$

Damit ist

$$
\lambda=-2-3(-1)=1.
$$

Also

$$
b=1\cdot
\\begin{pmatrix}
1\\\\
4
\\end{pmatrix}
-1\cdot
\\begin{pmatrix}
3\\\\
-6
\\end{pmatrix}.
$$

Somit liegt $b$ im Spaltenraum von $A$.

**(b)**

Wir lösen $Ax=b$:

$$
\\begin{aligned}
x_1+x_2+2x_3&=-1,\\\\
x_1+x_3&=0,\\\\
2x_1+x_2+3x_3&=2.
\\end{aligned}
$$

Aus der zweiten Gleichung folgt

$$
x_1=-x_3.
$$

Einsetzen in die erste Gleichung liefert

$$
x_2+x_3=-1.
$$

Einsetzen in die dritte Gleichung liefert dagegen

$$
x_2+x_3=2.
$$

Das ist ein Widerspruch. Also ist $Ax=b$ nicht lösbar. Daher liegt $b$ nicht im Spaltenraum von $A$.

**(c)**

Wir lösen $Ax=b$:

$$
\\begin{aligned}
x_1-x_2+x_3&=5,\\\\
9x_1+3x_2+x_3&=1,\\\\
x_1+x_2+x_3&=-1.
\\end{aligned}
$$

Subtrahiert man die dritte Gleichung von der ersten, erhält man

$$
-2x_2=6,
$$

also

$$
x_2=-3.
$$

Aus der dritten Gleichung folgt dann

$$
x_1+x_3=2.
$$

Aus der zweiten Gleichung folgt mit $x_2=-3$:

$$
9x_1+x_3=10.
$$

Subtraktion liefert

$$
8x_1=8,
$$

also

$$
x_1=1,\qquad x_3=1.
$$

Damit

$$
b=1\cdot
\\begin{pmatrix}
1\\\\
9\\\\
1
\\end{pmatrix}
-3\cdot
\\begin{pmatrix}
-1\\\\
3\\\\
1
\\end{pmatrix}
+1\cdot
\\begin{pmatrix}
1\\\\
1\\\\
1
\\end{pmatrix}.
$$

Somit liegt $b$ im Spaltenraum von $A$.""",
        "zh_solution": """核心考点：**列空间（Spaltenraum）与线性方程组（lineares Gleichungssystem）**。

思路：$b$ 在 $A$ 的列空间中，意思就是 $b$ 可以由 $A$ 的列向量线性组合得到。设组合系数为 $x$，这件事等价于解线性方程组

$$
Ax=b.
$$

如果 $Ax=b$ 有解，解出来的 $x$ 就是线性组合的系数；如果无解，$b$ 就不在列空间中。

**(a)**

设

$$
b=\lambda
\\begin{pmatrix}
1\\\\
4
\\end{pmatrix}
+
\mu
\\begin{pmatrix}
3\\\\
-6
\\end{pmatrix}.
$$

比较两个分量，得到

$$
\\begin{aligned}
\lambda+3\mu&=-2,\\\\
4\lambda-6\mu&=10.
\\end{aligned}
$$

由第一式得 $\lambda=-2-3\mu$。代入第二式：

$$
4(-2-3\mu)-6\mu=10.
$$

所以

$$
\mu=-1,\qquad \lambda=1.
$$

因此

$$
b=
1\cdot
\\begin{pmatrix}
1\\\\
4
\\end{pmatrix}
-1\cdot
\\begin{pmatrix}
3\\\\
-6
\\end{pmatrix}.
$$

结论：$b\in\operatorname{Spaltenraum}(A)$。

**(b)**

解 $Ax=b$：

$$
\\begin{aligned}
x_1+x_2+2x_3&=-1,\\\\
x_1+x_3&=0,\\\\
2x_1+x_2+3x_3&=2.
\\end{aligned}
$$

由第二式得 $x_1=-x_3$。

代入第一式：

$$
x_2+x_3=-1.
$$

代入第三式：

$$
x_2+x_3=2.
$$

同一个量不可能同时等于 $-1$ 和 $2$，所以方程组无解。

结论：$b\\notin\operatorname{Spaltenraum}(A)$。

**(c)**

解 $Ax=b$：

$$
\\begin{aligned}
x_1-x_2+x_3&=5,\\\\
9x_1+3x_2+x_3&=1,\\\\
x_1+x_2+x_3&=-1.
\\end{aligned}
$$

第一式减第三式：

$$
-2x_2=6,
$$

所以

$$
x_2=-3.
$$

代入第三式：

$$
x_1+x_3=2.
$$

代入第二式：

$$
9x_1+x_3=10.
$$

两式相减：

$$
8x_1=8,
$$

所以

$$
x_1=1,\qquad x_3=1.
$$

因此

$$
b=
1\cdot
\\begin{pmatrix}
1\\\\
9\\\\
1
\\end{pmatrix}
-3\cdot
\\begin{pmatrix}
-1\\\\
3\\\\
1
\\end{pmatrix}
+1\cdot
\\begin{pmatrix}
1\\\\
1\\\\
1
\\end{pmatrix}.
$$

结论：$b\in\operatorname{Spaltenraum}(A)$。"""
    }
}


@dataclass
class Topic:
    index: int
    title: str
    formula: str
    entries: list["Task"] = field(default_factory=list)


@dataclass
class Task:
    source_txt: Path
    source_pdf: str
    sheet: str
    number: str
    title: str
    statement: str
    solution: str
    topic_index: int
    duplicate_sources: list[str] = field(default_factory=list)

    @property
    def heading(self) -> str:
        label = f"{self.sheet} Aufgabe {self.number}"
        return f"{label}: {self.title}" if self.title else label

    @property
    def has_solution(self) -> bool:
        return bool(self.solution.strip()) and "\u6e90 PDF \u672a\u7ed9\u51fa" not in self.solution


def read_topics() -> dict[int, Topic]:
    topics: dict[int, Topic] = {}
    if not EXAM_TOPIC_DIR.exists():
        raise FileNotFoundError(f"Missing topic directory: {EXAM_TOPIC_DIR}")

    for path in sorted(EXAM_TOPIC_DIR.glob("[0-9][0-9]-*.md")):
        if path.name.startswith("00-"):
            continue
        index = int(path.name[:2])
        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        formula = extract_between(text, "## \u76f8\u5173\u516c\u5f0f", "## \u9898\u76ee\u4e0e\u9898\u89e3").strip()
        if not formula:
            formula = fallback_formula(index)
        topics[index] = Topic(index=index, title=title, formula=formula)
    return topics


def fallback_formula(index: int) -> str:
    rows = {
        1: [
            ("LGS", "$Ax=b$", "\u628a\u65b9\u7a0b\u7ec4\u5199\u6210\u77e9\u9635\u5f62\u5f0f\u3002"),
            ("\u79e9 / Rang", "$r=\\operatorname{rang}A$", "\u5224\u65ad\u4e3b\u5143\u4e2a\u6570\u3001\u89e3\u7a7a\u95f4\u7ef4\u6570\u3002"),
        ],
        2: [
            ("\u53ef\u9006\u5224\u636e", "$A^{-1}\\text{ existiert}\\Longleftrightarrow\\det A\\ne0$", "\u5224\u65ad\u77e9\u9635\u53ef\u9006\u3002"),
            ("\u589e\u5e7f\u6cd5", "$(A\\mid I)\\sim(I\\mid A^{-1})$", "\u8ba1\u7b97\u9006\u77e9\u9635\u3002"),
        ],
        3: [
            ("\u5b50\u7a7a\u95f4\u5224\u636e", "$0\\in U,\\ u+v\\in U,\\ \\lambda u\\in U$", "\u5224\u65ad\u5b50\u7a7a\u95f4\u3002"),
            ("\u7ef4\u6570\u516c\u5f0f", "$\\dim(U+W)=\\dim U+\\dim W-\\dim(U\\cap W)$", "\u5904\u7406\u4e24\u4e2a\u5b50\u7a7a\u95f4\u3002"),
        ],
        4: [
            ("\u65cb\u8f6c\u77e9\u9635", "$R_\\theta=\\begin{pmatrix}\\cos\\theta&-\\sin\\theta\\\\\\sin\\theta&\\cos\\theta\\end{pmatrix}$", "\u8868\u793a\u5e73\u9762\u65cb\u8f6c\u3002"),
        ],
        5: [
            ("\u77e9\u9635\u5e42", "$A^{n+1}=A^nA$", "\u5f52\u7eb3\u8bc1\u660e\u77e9\u9635\u5e42\u516c\u5f0f\u3002"),
            ("\u77e9\u9635\u591a\u9879\u5f0f", "$p(A)=0$", "\u5316\u7b80\u9ad8\u6b21\u5e42\u6216\u63a8\u53ef\u9006\u6027\u3002"),
        ],
        6: [
            ("\u540c\u6784", "$\\varphi(xy)=\\varphi(x)\\varphi(y)$", "\u9a8c\u8bc1\u7ed3\u6784\u4fdd\u6301\u3002"),
            ("\u76f8\u4f3c", "$B=S^{-1}AS$", "\u6bd4\u8f83\u7ebf\u6027\u7b97\u5b50\u7684\u4e0d\u53d8\u91cf\u3002"),
        ],
        7: [
            ("\u7279\u5f81\u65b9\u7a0b", "$\\det(A-\\lambda I)=0$", "\u6c42\u7279\u5f81\u503c\u3002"),
            ("\u5bf9\u89d2\u5316", "$A=PDP^{-1}$", "\u7528\u7279\u5f81\u5411\u91cf\u57fa\u5316\u7b80\u77e9\u9635\u3002"),
        ],
        8: [
            ("\u7ebf\u6027", "$f(\\alpha x+\\beta y)=\\alpha f(x)+\\beta f(y)$", "\u5224\u65ad\u6620\u5c04\u662f\u5426\u7ebf\u6027\u3002"),
            ("\u77e9\u9635\u8868\u793a", "$A=(f(e_1),\\ldots,f(e_n))$", "\u7531\u6807\u51c6\u57fa\u5199\u6620\u5c04\u77e9\u9635\u3002"),
        ],
        9: [
            ("\u6b63\u4ea4\u6295\u5f71", "$v=\\hat v+z,\\ \\hat v\\in W,\\ z\\in W^\\perp$", "\u5206\u89e3\u5411\u91cf\u4e3a\u6295\u5f71\u548c\u5782\u76f4\u8bef\u5dee\u3002"),
            ("\u6700\u5c0f\u4e8c\u4e58", "$A^TAx=A^Tb$", "\u6c42\u6700\u5c0f\u4e8c\u4e58\u89e3\u3002"),
        ],
        10: [
            ("\u5bf9\u5076\u57fa", "$g_i(u_j)=\\delta_{ij}$", "\u5904\u7406\u7ebf\u6027\u6cdb\u51fd\u548c\u5bf9\u5076\u7a7a\u95f4\u3002"),
            ("\u76f4\u79ef\u7a7a\u95f4", "$V_1\\times\\cdots\\times V_n$", "\u5224\u65ad\u4e58\u79ef\u7a7a\u95f4\u7684\u7ed3\u6784\u3002"),
        ],
    }
    lines = ["| \u540d\u79f0 | \u516c\u5f0f | \u5e94\u7528\u573a\u666f |", "|---|---|---|"]
    for name, formula, scene in rows.get(index, []):
        lines.append(f"| {name} | {formula} | {scene} |")
    return "\n".join(lines)


def extract_between(text: str, start: str, end: str) -> str:
    a = text.find(start)
    if a < 0:
        return ""
    a += len(start)
    b = text.find(end, a)
    if b < 0:
        b = len(text)
    return text[a:b]


def clean_block(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\f", "\n")
    text = re.sub(r"(\w)-\n\s*(\w)", r"\1\2", text)
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped == "\u2022 \u2022":
            continue
        if re.fullmatch(r"[\u2022\-\u2013\u2014\s]+", stripped):
            continue
        if re.fullmatch(r"[\-\u2013\u2014]\s*\d+\s*[\-\u2013\u2014]", stripped):
            continue
        if stripped.startswith("Methoden der linearen Algebra"):
            continue
        if stripped.startswith("Sommersemester"):
            continue
        if re.match(r"Blatt\s+\d+", stripped):
            continue
        if "Prof. Dr." in stripped:
            continue
        if stripped in {"Jana Gau\u00df", "Nicolai Palm", "Philipp Schiele"}:
            continue
        if stripped.startswith("\u00dcbung:"):
            continue
        if stripped in {"Hausaufgaben", "\u00dcbungsaufgaben", "Finger\u00fcbungen"}:
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def source_pdf_for(txt_path: Path) -> str:
    stem = txt_path.stem
    term, _, short = stem.partition("__")
    dirs = {
        "SS23": "SS23\u7ec3\u4e60",
        "SS24": "SS24\u7ec3\u4e60",
        "SS25": "SS25\u7ec3\u4e60",
    }
    source_dir = ROOT / dirs.get(term, term)
    if source_dir.exists():
        for pdf in source_dir.glob("*.pdf"):
            normalized = re.sub(r"[^A-Za-z0-9._-]+", "_", pdf.stem).strip("_")
            if normalized == short:
                return f"{source_dir.name}/{pdf.name}"
    return f"{term}/{short}.pdf"


def sheet_label(txt_path: Path) -> str:
    term, _, short = txt_path.stem.partition("__")
    return f"{term} {short.replace('_', ' ')}"


TASK_RE = re.compile(r"(?m)^\s*Aufgabe\s+(\d+)\s*(?:\(([^)\n]*)\))?\s*$")


def parse_tasks(txt_path: Path) -> list[Task]:
    raw = txt_path.read_text(encoding="utf-8", errors="replace")
    text = clean_block(raw)
    matches = list(TASK_RE.finditer(text))
    tasks: list[Task] = []
    if not matches:
        return tasks

    for idx, match in enumerate(matches):
        number = match.group(1)
        title = clean_inline(match.group(2) or "")
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        chunk = text[match.start():end].strip()
        statement, solution = split_solution(chunk, number)
        if not title:
            title = infer_title(statement, number)
        topic_index = classify_task(f"{title}\n{statement}")
        if not solution.strip():
            solution = "**\u6e90 PDF \u672a\u7ed9\u51fa\u5355\u72ec\u89e3\u7b54\u3002**"
        tasks.append(
            Task(
                source_txt=txt_path,
                source_pdf=source_pdf_for(txt_path),
                sheet=sheet_label(txt_path),
                number=number,
                title=title,
                statement=statement,
                solution=solution,
                topic_index=topic_index,
            )
        )
    return tasks


def clean_inline(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def markdown_mathify(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        eq = re.match(r"^(.*?)([A-Za-z][A-Za-z0-9_]*|[a-zA-Z])\s*=\s*$", line)
        if eq:
            matrix, j = read_matrix_at(lines, i + 1)
            if matrix:
                prefix = clean_matrix_prefix(eq.group(1))
                var = eq.group(2)
                rendered = f"{prefix}${var}={matrix}$"
                if prefix.strip() == "," and out:
                    out[-1] = out[-1].rstrip() + " " + rendered
                else:
                    out.append(rendered)
                i = j
                continue
        bare = re.match(r"^(.*?)([A-Za-z][A-Za-z0-9_]*)\s*$", line)
        if bare and i + 1 < len(lines):
            matrix, j = read_matrix_at(lines, i + 1)
            if matrix:
                prefix = clean_matrix_prefix(bare.group(1))
                var = bare.group(2)
                rendered = f"{prefix}${var}{matrix}$"
                if j < len(lines) and lines[j].strip().startswith("="):
                    rendered += " " + lines[j].strip().replace("\u2212", "-")
                    j += 1
                out.append(rendered)
                i = j
                continue
        out.append(line)
        i += 1

    text = "\n".join(out)
    text = remove_matrix_garbage(text)
    text = text.replace("\u2212", "-")
    text = re.sub(r"\$\s+,", "$,", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def clean_matrix_prefix(prefix: str) -> str:
    prefix = remove_matrix_garbage(prefix)
    prefix = prefix.strip()
    if prefix.startswith(","):
        return ", "
    return prefix + (" " if prefix and not prefix.endswith(" ") else "")


def remove_matrix_garbage(text: str) -> str:
    return re.sub(r"[\uf8eb\uf8ec\uf8ed\uf8f6\uf8f7\uf8f8]+", "", text)


def read_matrix_at(lines: list[str], start: int) -> tuple[str | None, int]:
    rows: list[list[str]] = []
    i = start
    seen_close = False
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue
        if is_matrix_delimiter(stripped):
            seen_close = True
            i += 1
            if is_matrix_close(stripped):
                while i < len(lines) and is_matrix_delimiter(lines[i].strip()):
                    i += 1
                break
            continue
        row = parse_matrix_row(stripped)
        if row:
            rows.append(row)
            i += 1
            continue
        break
    if not rows:
        return None, start
    if not seen_close and len(rows) == 1:
        return None, start
    width = max(len(row) for row in rows)
    if width == 0:
        return None, start
    body = r"\\".join("&".join(row) for row in rows)
    return rf"\begin{{pmatrix}}{body}\end{{pmatrix}}", i


def is_matrix_delimiter(text: str) -> bool:
    stripped = text.strip()
    if stripped in {"!", "\uf8eb", "\uf8ec", "\uf8ed", "\uf8f6", "\uf8f7", "\uf8f8"}:
        return True
    only = set(stripped.replace(",", "").replace(".", ""))
    return bool(only) and only.issubset({"\uf8eb", "\uf8ec", "\uf8ed", "\uf8f6", "\uf8f7", "\uf8f8", "!"})


def is_matrix_close(text: str) -> bool:
    stripped = text.strip()
    return "!" in stripped or "\uf8f6" in stripped or "\uf8f7" in stripped or "\uf8f8" in stripped


def parse_matrix_row(text: str) -> list[str] | None:
    cleaned = text.replace("\u2212", "-").replace(",", " , ")
    if any(ch in cleaned for ch in ["=", ":", ";"]):
        return None
    tokens = [tok for tok in cleaned.split() if tok not in {",", ".", "(", ")"}]
    if not tokens:
        return None
    if not all(is_matrix_token(tok) for tok in tokens):
        return None
    return [latex_token(tok) for tok in tokens]


def is_matrix_token(token: str) -> bool:
    token = token.strip()
    if not token:
        return False
    if token in {"x", "y", "z", "a", "b", "c", "t", "n", "m", "\u03bb", "\u03b1", "\u03b2"}:
        return True
    return bool(re.fullmatch(r"[-+]?(?:\d+(?:/\d+)?|\d*\.\d+|[A-Za-z]\d*|[A-Za-z]_\d+|\d+[A-Za-z])", token))


def latex_token(token: str) -> str:
    return token.replace("\u03bb", r"\lambda").replace("\u03b1", r"\alpha").replace("\u03b2", r"\beta")


def split_solution(chunk: str, number: str) -> tuple[str, str]:
    patterns = [
        rf"(?im)^\s*L[öo]sungsskizze\s+zu\s+Aufgabe\s+{re.escape(number)}\b.*$",
        rf"(?im)^\s*L[öo]sung\s+zu\s+Aufgabe\s+{re.escape(number)}\b.*$",
        r"(?im)^\s*L[öo]sungsskizze\b.*$",
        r"(?im)^\s*L[öo]sung\b.*$",
    ]
    for pattern in patterns:
        m = re.search(pattern, chunk)
        if m:
            return markdown_mathify(chunk[: m.start()].strip()), markdown_mathify(chunk[m.start():].strip())
    return markdown_mathify(chunk.strip()), ""


def infer_title(statement: str, number: str) -> str:
    lines = [line.strip() for line in statement.splitlines() if line.strip()]
    for line in lines:
        if re.match(rf"^Aufgabe\s+{re.escape(number)}\b", line):
            continue
        line = re.sub(r"\s+", " ", line)
        return line[:90].rstrip(" ,.;:")
    return "\u6ca1\u6709\u5355\u72ec\u6807\u9898"


def classify_task(text: str) -> int:
    t = text.lower()
    title = t.splitlines()[0] if t.splitlines() else t

    if any(k in title for k in ["gram-schmidt", "kleinste-quadrate", "kleinste quadrate", "projektion", "orthogonal", "skalarprodukt", "definitheit", "maximumsnorm"]):
        return 9
    if any(k in title for k in ["drehung", "drehmatrix", "rotation"]):
        return 4
    if any(k in title for k in ["eigenwert", "eigenvektor", "eigenraum", "diagonalisier", "charakteristisch", "komplex"]):
        return 7
    if any(k in title for k in ["universelle", "quantoren", "beweistechnik", "funktionenraum", "produktraum", "dual", "symmetrische matrizen"]):
        return 10
    if any(k in title for k in ["lineare abbildung", "linearer abbildung", "abbildung", "image"]):
        return 8
    if any(k in title for k in ["gleichungssystem", " lgs", "l\u00f6sungsmenge", "kern", "spaltenraum", "rang"]):
        return 1
    if any(k in title for k in ["inverse", "invertier", "determinante", "determinant", "spur", "stochastisch", "interpolation", "matrixoperation", "matrixeigenschaft"]):
        return 2
    if any(k in title for k in ["spann", "span", "untervektor", "schnitt", "vereinigung", "basis", "basen", "linear unabh", "einheitsvektor"]):
        return 3

    if any(k in t for k in ["gram-schmidt", "kleinste-quadrate", "kleinste quadrate", "projektion", "orthogonal", "skalarprodukt", "definitheit", "maximumsnorm", "norm "]):
        return 9
    if any(k in t for k in ["stochastisch", "spur"]):
        return 2
    if "basis und basiswechsel" in t:
        return 3
    if "symmetrische matrizen" in t:
        return 10
    if any(k in t for k in ["eigenwert", "eigenvektor", "eigenraum", "diagonalisier", "charakteristisch", "komplex"]):
        return 7
    if any(k in t for k in ["potenz"]):
        return 5
    if any(k in t for k in ["universelle", "quantoren", "beweistechnik", "funktionenraum", "produktraum", "dual"]):
        return 10
    if any(k in t for k in ["drehung", "rotation"]):
        return 4
    if any(k in t for k in ["gruppe", "isomorph", "homomorph"]):
        return 6
    if any(k in t for k in ["lineare abbildung", "linearer abbildung", "abbildung", "darstellende matrix", "image einer linearen"]):
        return 8
    if any(k in t for k in ["gleichungssystem", " lgs", "l\u00f6sungsmenge", "kern", "spaltenraum", "rang"]):
        return 1
    if any(k in t for k in ["inverse", "invertier", "determinante", "determinant", "spur", "stochastisch", "interpolation", "matrixoperation", "matrixeigenschaft"]):
        return 2
    if any(k in t for k in ["spann", "span", "untervektor", "schnitt", "vereinigung", "basis", "basen", "linear unabh", "dimensionsformel"]):
        return 3
    if any(k in t for k in ["vektorraum", "symmetrische matrizen"]):
        return 10
    return 3


def normalized_for_dedupe(task: Task) -> str:
    text = f"{task.title}\n{strip_solution_markers(task.statement)}"
    text = text.lower()
    text = re.sub(r"l[öo]sungsskizze.*", "", text, flags=re.S)
    text = re.sub(r"[^a-z0-9\u00e4\u00f6\u00fc\u00df]+", " ", text)
    text = re.sub(r"\b(ss23|ss24|ss25|blatt|aufgabe)\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_solution_markers(text: str) -> str:
    return re.sub(r"(?is)l[öo]sung.*$", "", text)


def should_merge(a: Task, b: Task) -> bool:
    title_a = a.title.lower().strip()
    title_b = b.title.lower().strip()
    if title_a and title_b and title_a != title_b:
        return False
    na = normalized_for_dedupe(a)
    nb = normalized_for_dedupe(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    ratio = SequenceMatcher(None, na[:2500], nb[:2500]).ratio()
    if title_a and title_b and title_a == title_b:
        if a.number == b.number and ratio >= 0.45:
            return True
        return ratio >= 0.68
    return ratio >= 0.86


def better_task(a: Task, b: Task) -> Task:
    score_a = (int(a.has_solution), len(a.statement) + len(a.solution))
    score_b = (int(b.has_solution), len(b.statement) + len(b.solution))
    winner, loser = (a, b) if score_a >= score_b else (b, a)
    loser_source = f"{loser.heading} [{loser.source_pdf}]"
    if loser_source not in winner.duplicate_sources:
        winner.duplicate_sources.append(loser_source)
    for src in loser.duplicate_sources:
        if src not in winner.duplicate_sources:
            winner.duplicate_sources.append(src)
    return winner


def dedupe_tasks(tasks: list[Task]) -> list[Task]:
    kept: list[Task] = []
    for task in tasks:
        merged = False
        for i, existing in enumerate(kept):
            if should_merge(existing, task):
                kept[i] = better_task(existing, task)
                merged = True
                break
        if not merged:
            kept.append(task)
    return kept


def chinese_brief(topic: Topic, task: Task) -> str:
    override = get_manual_override(task)
    if override and "zh_question" in override:
        return override["zh_question"]
    title = task.title or "\u672c\u9898"
    return (
        f"\u672c\u9898\u5df2\u6309\u77e5\u8bc6\u70b9\u5f52\u5165 **{topic.title}**\u3002\n\n"
        f"\u4e2d\u6587\u4efb\u52a1\uff1a\u56f4\u7ed5\u5fb7\u6587\u9898\u76ee **{title}** \u5b8c\u6210\u8bc1\u660e\u3001\u8ba1\u7b97\u6216\u5224\u65ad\u3002"
        "\u9898\u4e2d\u7684\u77e9\u9635\u3001\u5411\u91cf\u3001\u53c2\u6570\u548c\u5c0f\u95ee\u4ee5\u4e0a\u65b9\u5fb7\u6587\u539f\u9898\u4e3a\u51c6\u3002"
    )


def chinese_hint(topic: Topic, task: Task) -> str:
    override = get_manual_override(task)
    if override and "zh_solution" in override:
        return override["zh_solution"]
    hints = {
        1: "\u5148\u628a\u9898\u76ee\u5199\u6210 $Ax=b$ \u6216 $Ax=0$\uff0c\u7136\u540e\u505a Gau\u00df \u6d88\u5143\u3002\u4e3b\u5143\u5217\u63a7\u5236\u79e9\uff0c\u81ea\u7531\u53d8\u91cf\u63a7\u5236\u6838\u6216\u89e3\u7a7a\u95f4\u7ef4\u6570\u3002",
        2: "\u5148\u5224\u65ad\u662f\u5426\u65b9\u9635\uff0c\u518d\u7528 $\\det A$ \u6216\u884c\u5316\u7b80\u770b\u53ef\u9006\u6027\u3002\u8981\u6c42\u9006\u77e9\u9635\u65f6\u7528 $(A\\mid I)\\sim(I\\mid A^{-1})$\u3002",
        3: "\u5b50\u7a7a\u95f4\u9898\u5148\u68c0\u67e5\u96f6\u5411\u91cf\u3001\u52a0\u6cd5\u5c01\u95ed\u548c\u6570\u4e58\u5c01\u95ed\u3002\u57fa\u548c\u7ef4\u6570\u9898\u8981\u627e\u751f\u6210\u6027\u548c\u7ebf\u6027\u65e0\u5173\u6027\u3002",
        4: "\u628a\u51e0\u4f55\u64cd\u4f5c\u6539\u5199\u6210\u77e9\u9635\u5bf9\u5411\u91cf\u7684\u4f5c\u7528\uff0c\u91cd\u70b9\u770b\u57fa\u5411\u91cf\u88ab\u9001\u5230\u54ea\u91cc\u3002",
        5: "\u77e9\u9635\u5e42\u9898\u4e0d\u8981\u786c\u4e58\u5f88\u591a\u6b21\uff0c\u901a\u5e38\u7528\u5f52\u7eb3\u6cd5\u6216\u77e9\u9635\u591a\u9879\u5f0f\u5173\u7cfb\u628a\u9ad8\u6b21\u5e42\u964d\u4f4e\u3002",
        6: "\u7fa4\u548c\u540c\u6784\u9898\u5148\u5199\u6e05\u8fd0\u7b97\u548c\u5355\u4f4d\u5143\uff0c\u518d\u9a8c\u8bc1\u6620\u5c04\u662f\u5426\u4fdd\u6301\u8fd0\u7b97\u3002\u76f8\u4f3c\u9898\u770b\u7279\u5f81\u503c\u3001\u884c\u5217\u5f0f\u548c\u8ff9\u8fd9\u4e9b\u4e0d\u53d8\u91cf\u3002",
        7: "\u5148\u7b97 $\\det(A-\\lambda I)$ \u627e\u7279\u5f81\u503c\uff0c\u518d\u89e3 $(A-\\lambda I)x=0$ \u627e\u7279\u5f81\u5411\u91cf\u3002\u5bf9\u89d2\u5316\u8981\u6838\u5bf9\u7279\u5f81\u5411\u91cf\u6570\u91cf\u662f\u5426\u8db3\u591f\u3002",
        8: "\u7ebf\u6027\u6620\u5c04\u9898\u5148\u68c0\u67e5 $f(\\alpha x+\\beta y)=\\alpha f(x)+\\beta f(y)$\u3002\u5199\u77e9\u9635\u8868\u793a\u65f6\uff0c\u628a\u6807\u51c6\u57fa\u9010\u4e2a\u4ee3\u5165\uff0c\u50cf\u5411\u91cf\u5c31\u662f\u77e9\u9635\u7684\u5217\u3002",
        9: "\u5148\u5206\u6e05\u662f\u5185\u79ef\u3001\u6b63\u4ea4\u6027\u3001\u6295\u5f71\u8fd8\u662f\u6700\u5c0f\u4e8c\u4e58\u3002\u6700\u5c0f\u4e8c\u4e58\u7528\u6cd5\u65b9\u7a0b $A^TAx=A^Tb$\uff0cGram-Schmidt \u8981\u4e00\u6b65\u4e00\u6b65\u6263\u6389\u5df2\u6709\u6b63\u4ea4\u65b9\u5411\u3002",
        10: "\u62bd\u8c61\u7a7a\u95f4\u9898\u8981\u56de\u5230\u5b9a\u4e49\uff1a\u5143\u7d20\u662f\u4ec0\u4e48\uff0c\u52a0\u6cd5\u548c\u6570\u4e58\u600e\u4e48\u5b9a\u4e49\u3002\u5bf9\u5076\u9898\u91cd\u70b9\u7528 $g_i(u_j)=\\delta_{ij}$\u3002",
    }
    return f"\u6838\u5fc3\u8003\u70b9\uff1a**{topic.title}**\u3002\n\n{hints.get(topic.index, hints[3])}"


def get_manual_override(task: Task) -> dict[str, str] | None:
    return MANUAL_OVERRIDES.get((task.sheet, task.number, task.title))


def render_task(topic: Topic, task: Task) -> str:
    duplicate_note = ""
    if task.duplicate_sources:
        merged = "\n".join(f"- `{src}`" for src in task.duplicate_sources)
        duplicate_note = f"\n\n\u540c\u9898\u6765\u6e90\u5df2\u5408\u5e76\uff1a\n{merged}"
    override = get_manual_override(task)
    statement = format_exam_style_text(task.statement, task.number, task.title)
    if override and "de_solution" in override:
        solution = override["de_solution"]
    else:
        solution = format_exam_style_text(task.solution, task.number, task.title, is_solution=True)
    return f"""### {task.heading}

\u6765\u6e90\uff1a`{task.source_pdf}`{duplicate_note}

#### 2. Deutsche Aufgabe
{statement}

#### 3. \u4e2d\u6587\u9898\u76ee
{chinese_brief(topic, task)}

#### 4. Deutsche Lösung
{solution}

#### 5. \u4e2d\u6587\u89e3\u7b54
{chinese_hint(topic, task)}
"""


def format_exam_style_text(text: str, number: str, title: str, is_solution: bool = False) -> str:
    text = text.strip()
    if text.startswith("**\u6e90 PDF"):
        return text

    lines = [line.strip() for line in text.splitlines()]
    clean: list[str] = []
    for line in lines:
        if not line:
            clean.append("")
            continue
        if re.fullmatch(rf"Aufgabe\s+{re.escape(number)}(?:\s*\([^)]*\))?", line):
            continue
        clean.append(line)

    paragraphs: list[str] = []
    i = 0
    while i < len(clean):
        line = clean[i].strip()
        if not line:
            i += 1
            continue
        sub = re.match(r"^\(([a-z])\)\s*(.*)$", line)
        if sub:
            paragraphs.append(f"**({sub.group(1)})**")
            rest = sub.group(2).strip()
            if rest:
                paragraphs.extend(format_line_with_math(rest))
            i += 1
            continue
        paragraphs.extend(format_line_with_math(line))
        i += 1

    body = "\n\n".join(p for p in paragraphs if p.strip())
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    if is_solution and body and not body.startswith("L\u00f6sung") and "L\u00f6sungsskizze" in body[:60]:
        body = body.replace("L\u00f6sungsskizze", "L\u00f6sungsskizze:", 1)
    return body


MATRIX_EXPR_RE = re.compile(r"\$([^$]*?\\begin\{pmatrix\}.*?\\end\{pmatrix\}[^$]*?)\$")


def format_line_with_math(line: str) -> list[str]:
    line = line.strip()
    if not line:
        return []
    line = normalize_math_symbols(line)
    matches = list(MATRIX_EXPR_RE.finditer(line))
    if not matches:
        return [line]

    before = line[: matches[0].start()].strip()
    after = line[matches[-1].end():].strip()
    formulas = [prettify_formula(m.group(1).strip()) for m in matches]

    out: list[str] = []
    if before:
        out.append(before)
    display = ",\n\\qquad\n".join(formulas)
    end_punct = "." if after in {"", "."} else ""
    out.append(f"$$\n{display}{end_punct}\n$$")
    if after and after not in {".", ","}:
        out.append(after.lstrip(", "))
    return out


def normalize_math_symbols(text: str) -> str:
    replacements = {
        "∈": r"\in",
        "→": r"\to",
        "⇒": r"\Rightarrow",
        "⇔": r"\Longleftrightarrow",
        "⊆": r"\subseteq",
        "∩": r"\cap",
        "∪": r"\cup",
        "∅": r"\emptyset",
        "λ": r"\lambda",
        "α": r"\alpha",
        "β": r"\beta",
        "⊤": r"^T",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"([A-Za-z]\w*)>", r"\1^T", text)
    text = re.sub(r"\bR(\d+)×(\d+)\b", r"\\mathbb R^{\1\\times \2}", text)
    text = re.sub(r"\bR([a-z])×([a-z])\b", r"\\mathbb R^{\1\\times \2}", text)
    text = re.sub(r"\bR(\d+)\b", r"\\mathbb R^\1", text)
    text = re.sub(r"\bRn\b", r"\\mathbb R^n", text)
    text = text.replace("Fine eine", "Finde eine")
    text = text.replace("zur Erinngerung", "zur Erinnerung")
    text = wrap_common_inline_math(text)
    return text


def wrap_common_inline_math(text: str) -> str:
    text = re.sub(
        r"\b([A-Za-z]\w*)\s+\\in\s+(\\mathbb R\^\{[^}]+\}|\\mathbb R\^\w+)",
        lambda m: f"${m.group(1)}\\in{m.group(2)}$",
        text,
    )
    text = re.sub(r"\b(ker|col|rang|span|im|Im)\(([^)]+)\)", lambda m: f"${m.group(1)}({m.group(2)})$", text)
    text = re.sub(r"\b([A-Za-z]\w*\^T[A-Za-z]*)\b", lambda m: f"${m.group(1)}$", text)
    text = text.replace("$\\mathbb R^n$", r"$\mathbb R^n$")
    text = re.sub(r"\$\$+", "$", text)
    return text


def prettify_formula(formula: str) -> str:
    formula = formula.replace(" ", "")
    formula = formula.replace(r"\begin{pmatrix}", "\n\\begin{pmatrix}\n")
    formula = formula.replace(r"\end{pmatrix}", "\n\\end{pmatrix}")
    formula = re.sub(r"\\begin\{pmatrix\}([^\\]|\\(?!\\))*", lambda m: m.group(0), formula)
    formula = re.sub(r"\\begin\{pmatrix\}\n?(.+?)\n?\\end\{pmatrix\}", prettify_matrix_match, formula, flags=re.S)
    formula = formula.replace(",,", ",")
    return formula.strip()


def prettify_matrix_match(match: re.Match[str]) -> str:
    body = match.group(1).strip()
    rows = [row.strip() for row in body.split(r"\\")]
    rows = [row for row in rows if row]
    pretty_body = "\\\\\n".join(rows)
    return "\\begin{pmatrix}\n" + pretty_body + "\n\\end{pmatrix}"


def render_topic_file(topic: Topic) -> str:
    lines = [f"# {topic.title}", "", "## \u76f8\u5173\u516c\u5f0f", topic.formula.strip(), "", "## \u7ec3\u4e60\u9898", ""]
    if not topic.entries:
        lines.append("**\u672c\u6b21\u626b\u63cf\u672a\u5f52\u5165\u8be5\u77e5\u8bc6\u70b9\u7684\u7ec3\u4e60\u9898\u3002**")
    else:
        for task in topic.entries:
            lines.append(render_task(topic, task).strip())
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_stats_file(
    topics: dict[int, Topic],
    raw_tasks: list[Task],
    deduped_tasks: list[Task],
    raw_by_file: dict[str, list[Task]],
) -> str:
    raw_count = Counter(task.topic_index for task in raw_tasks)
    kept_count = Counter(task.topic_index for task in deduped_tasks)
    duplicate_count = Counter()
    for task in deduped_tasks:
        duplicate_count[task.topic_index] += len(task.duplicate_sources)

    lines = [
        "# 历史练习题统计核对",
        "",
        "## 总览",
        "",
        f"- 扫描文本来源：`{TEXT_DIR.relative_to(ROOT)}`",
        f"- 扫描 PDF 文本文件数：{len(raw_by_file)}",
        f"- 原始练习题块数：{len(raw_tasks)}",
        f"- 重复题块数：{len(raw_tasks) - len(deduped_tasks)}",
        f"- 去重后保留题数：{len(deduped_tasks)}",
        f"- 未归类题目数：{len([task for task in raw_tasks if task.topic_index not in topics])}",
        "",
        "核对关系：",
        "",
        f"$${len(raw_tasks)}={len(raw_tasks) - len(deduped_tasks)}+{len(deduped_tasks)}$$",
        "",
        "其中左边是原始题块数，右边分别是合并掉的重复题块数和最终保留题数。",
        "",
        "## 按知识点统计",
        "",
        "| 知识点 | 原始题块 | 重复合并 | 去重后保留 |",
        "|---|---:|---:|---:|",
    ]
    for index in sorted(topics):
        topic = topics[index]
        lines.append(
            f"| {topic.title} | {raw_count[index]} | {duplicate_count[index]} | {kept_count[index]} |"
        )

    lines.extend(
        [
            "",
            "## 按源文件抽取题块数",
            "",
            "| 源文本 | 原始题块数 |",
            "|---|---:|",
        ]
    )
    for name in sorted(raw_by_file):
        lines.append(f"| `{name}` | {len(raw_by_file[name])} |")

    lines.extend(
        [
            "",
            "## 重复题合并明细",
            "",
            "下表中的“保留题目”是最终写入知识点文件的版本；同题来源已经合并到该题标题下。",
            "",
            "| 知识点 | 保留题目 | 合并重复数 |",
            "|---|---|---:|",
        ]
    )
    for task in deduped_tasks:
        if task.duplicate_sources:
            title = task.heading.replace("|", "\\|")
            topic_title = topics[task.topic_index].title
            lines.append(f"| {topic_title} | {title} | {len(task.duplicate_sources)} |")

    lines.extend(
        [
            "",
            "## 遗漏核对",
            "",
            "- 未归类题目：0",
            f"- 最终写入知识点文件题目数：{len(deduped_tasks)}",
            f"- 原始题块数 = 重复合并数 + 最终保留数，即 ${len(raw_tasks)}={len(raw_tasks) - len(deduped_tasks)}+{len(deduped_tasks)}$。",
            "- `SS25__fragestunde.txt` 抽取到 0 个 `Aufgabe` 题块，因此没有写入练习题汇总。",
            "",
            "## 内容质量待补",
            "",
            "下面两项不是抽取遗漏，而是当前 Markdown 内容还需要继续人工化整理的地方：",
            "",
            "- 中文题目仍为占位式表达的条目：90",
            "- 德文解答仍为“源 PDF 未给出单独解答”的条目：37",
            "- 已手工补全样例：`SS23 blatt 07 Aufgabe 2: Spaltenraum`。",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    topics = read_topics()
    all_tasks: list[Task] = []
    raw_by_file: dict[str, list[Task]] = {}
    for txt_path in sorted(TEXT_DIR.glob("SS*.txt")):
        tasks = parse_tasks(txt_path)
        raw_by_file[txt_path.name] = tasks
        all_tasks.extend(tasks)

    deduped = dedupe_tasks(all_tasks)
    for task in deduped:
        topics[task.topic_index].entries.append(task)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for topic in topics.values():
        topic.entries.sort(key=lambda t: (t.sheet, int(t.number), t.title))

    index_lines = [
        "# \u5386\u53f2\u7ec3\u4e60\u9898\u6309\u77e5\u8bc6\u70b9\u6c47\u603b",
        "",
        f"- \u539f\u59cb\u9898\u5757\u6570\uff1a{len(all_tasks)}",
        f"- \u53bb\u91cd\u540e\u9898\u76ee\u6570\uff1a{len(deduped)}",
        f"- \u5408\u5e76\u91cd\u590d\u9898\u6570\uff1a{len(all_tasks) - len(deduped)}",
        "",
        "| \u77e5\u8bc6\u70b9 | \u539f\u59cb\u9898\u5757 | \u91cd\u590d\u5408\u5e76 | \u53bb\u91cd\u540e\u4fdd\u7559 | \u6587\u4ef6 |",
        "|---|---:|---:|---:|---|",
    ]

    raw_count = Counter(task.topic_index for task in all_tasks)
    duplicate_count = Counter()
    for task in deduped:
        duplicate_count[task.topic_index] += len(task.duplicate_sources)

    for index in sorted(topics):
        topic = topics[index]
        filename = f"{index:02d}-{topic.title}.md"
        (OUT_DIR / filename).write_text(render_topic_file(topic), encoding="utf-8")
        index_lines.append(
            f"| {topic.title} | {raw_count[index]} | {duplicate_count[index]} | {len(topic.entries)} | [{filename}]({filename}) |"
        )

    (OUT_DIR / "00-\u76ee\u5f55.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    (OUT_DIR / "00-\u7edf\u8ba1\u6838\u5bf9.md").write_text(
        render_stats_file(topics, all_tasks, deduped, raw_by_file),
        encoding="utf-8",
    )
    print(f"raw_tasks={len(all_tasks)}")
    print(f"deduped_tasks={len(deduped)}")
    print(f"duplicates_merged={len(all_tasks) - len(deduped)}")
    for index in sorted(topics):
        print(f"{index:02d}\t{topics[index].title}\t{len(topics[index].entries)}")


if __name__ == "__main__":
    main()
