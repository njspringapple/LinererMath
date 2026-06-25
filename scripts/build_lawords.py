import csv
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lawords.csv"
TEXT_DIR = ROOT / "tmp_lawords_text"
SCAN_DIRS = ["练习", "考试", "讲义", "辅导", "分章节教材"]

GLOSSARY = {
    "Abgeschlossenheit": "封闭性",
    "Abbildung": "映射/图示",
    "Additivität": "可加性",
    "adjungierte Matrix": "伴随矩阵",
    "affine Abbildung": "仿射映射",
    "algebraische Vielfachheit": "代数重数",
    "allgemeine Lösung": "通解",
    "Assoziativität": "结合律",
    "Ausgangsvektor": "输出向量",
    "Basis": "基",
    "Basiswechsel": "换基",
    "Basiswechselmatrix": "换基矩阵",
    "bijektiv": "双射的",
    "Bild": "像/值域",
    "Bildraum": "像空间",
    "charakteristische Gleichung": "特征方程",
    "charakteristisches Polynom": "特征多项式",
    "Cauchy-Schwarz Ungleichung": "柯西-施瓦茨不等式",
    "Definitionsbereich": "定义域",
    "Definitionsbereichs": "定义域（属格形式）",
    "Determinante": "行列式",
    "Diagonale": "对角线",
    "Diagonalisierung": "对角化",
    "diagonalisierbar": "可对角化的",
    "Diagonalmatrix": "对角矩阵",
    "Dimension": "维数",
    "Dreiecksmatrix": "三角矩阵",
    "Distributivität": "分配律",
    "Eigenraum": "特征空间",
    "Eigenvektor": "特征向量",
    "Eigenwert": "特征值",
    "Eigenwertgleichung": "特征值方程",
    "Eigenwertproblem": "特征值问题",
    "Einheitsmatrix": "单位矩阵",
    "Einheitsvektor": "单位向量",
    "Eintrag einer Matrix": "矩阵元素/条目",
    "elementare Zeilenoperation": "初等行变换",
    "Endomorphismus": "自同态",
    "Erzeugendensystem": "生成系",
    "erweiterte Matrix": "增广矩阵",
    "Faktorisierung": "分解/因式分解",
    "freie Variable": "自由变量",
    "Gauß-Elimination": "高斯消元",
    "Gauß-Jordan-Verfahren": "高斯-约当法",
    "Gegenbeispiel": "反例",
    "geometrische Vielfachheit": "几何重数",
    "Gleichungssystem": "方程组",
    "Gram-Schmidt-Verfahren": "格拉姆-施密特方法",
    "Hauptachsentransformation": "主轴变换",
    "homogen": "齐次的",
    "homogenes Gleichungssystem": "齐次方程组",
    "Homogenität": "齐次性",
    "Hyperebene": "超平面",
    "Identitätsmatrix": "单位矩阵",
    "indefinit": "不定的",
    "inhomogen": "非齐次的",
    "inhomogenes Gleichungssystem": "非齐次方程组",
    "injektiv": "单射的",
    "inneres Produkt": "内积",
    "Interpolation": "插值",
    "invarianter Unterraum": "不变子空间",
    "Inverse": "逆",
    "inverse Matrix": "逆矩阵",
    "invertierbar": "可逆的",
    "Kern": "核",
    "Kernraum": "核空间",
    "Kofaktor": "余因子",
    "Kofaktorentwicklung": "余子式展开",
    "Koordinate": "坐标",
    "Koordinatenvektor": "坐标向量",
    "Kommutativität": "交换律",
    "Kosinus des Winkels": "夹角余弦",
    "Kovarianzmatrix": "协方差矩阵",
    "least squares": "最小二乘",
    "linear abhängig": "线性相关",
    "linear unabhängig": "线性无关",
    "lineare Abbildung": "线性映射",
    "lineare Gleichung": "线性方程",
    "lineare Hülle": "线性包",
    "lineare Kombination": "线性组合",
    "Linearitätsbedingung": "线性条件",
    "lineares Gleichungssystem": "线性方程组",
    "lineares Modell": "线性模型",
    "Linearkombination": "线性组合",
    "Linearität": "线性",
    "Lösungsmenge": "解集",
    "Markov-Kette": "马尔可夫链",
    "Markov-Matrix": "马尔可夫矩阵",
    "Matrixprodukt": "矩阵乘积",
    "Matrix-Vektor-Produkt": "矩阵-向量乘积",
    "Minimalpolynom": "最小多项式",
    "Monotonie": "单调性",
    "Neutralität": "中性元性质",
    "Normalengleichung": "正规方程",
    "Normalgleichung": "正规方程",
    "normalisiert": "归一化的",
    "Norm": "范数",
    "Nullraum": "零空间",
    "Nullstelle": "零点",
    "Nullvektor": "零向量",
    "obere Dreiecksmatrix": "上三角矩阵",
    "orthogonal": "正交的",
    "Orthogonalbasis": "正交基",
    "orthogonale Diagonalisierung": "正交对角化",
    "orthogonale Matrix": "正交矩阵",
    "orthogonale Projektion": "正交投影",
    "orthogonales Komplement": "正交补",
    "orthonormal": "标准正交的",
    "Orthonormalbasis": "标准正交基",
    "PageRank": "网页排名算法",
    "Parameterdarstellung": "参数表示",
    "Parameterdarstellung": "参数表示",
    "Permutationsmatrix": "置换矩阵",
    "Pivot": "主元",
    "Positivität": "正性",
    "positiv definit": "正定的",
    "positiv semidefinit": "半正定的",
    "Potenz einer Matrix": "矩阵幂",
    "Projektion": "投影",
    "QR-Zerlegung": "QR分解",
    "quadratische Form": "二次型",
    "Rang": "秩",
    "Rang-Nullitätssatz": "秩-零化度定理",
    "reduzierte Zeilenstufenform": "简化行阶梯形",
    "Reflexion": "反射",
    "Residuum": "残差",
    "Rotation": "旋转",
    "Schnittmenge": "交集",
    "singulär": "奇异的",
    "Singulärwert": "奇异值",
    "Singulärwertzerlegung": "奇异值分解",
    "Skalar": "标量",
    "Skalarmultiplikation": "数乘",
    "Skalarprodukt": "内积/点积",
    "Spaltenraum": "列空间",
    "Spaltenvektor": "列向量",
    "Spann": "张成空间",
    "Spektralsatz": "谱定理",
    "Spektralzerlegung": "谱分解",
    "Spiegelung": "镜像/反射",
    "stabiler Zustand": "稳定状态",
    "stationärer Vektor": "稳定向量",
    "stationärer Zustand": "稳定状态",
    "stochastische Matrix": "随机矩阵",
    "Subadditivität": "次可加性",
    "surjektiv": "满射的",
    "symmetrische Matrix": "对称矩阵",
    "lineare Transformation": "线性变换",
    "transponierte Matrix": "转置矩阵",
    "Transposition": "转置",
    "Transitivität": "传递性",
    "triviale Lösung": "平凡解",
    "untere Dreiecksmatrix": "下三角矩阵",
    "Unterraum": "子空间",
    "Untervektorraum": "子向量空间",
    "Vektor": "向量",
    "Vektorraum": "向量空间",
    "Vielfachheit": "重数",
    "Zeilenvektor": "行向量",
    "Zeilenraum": "行空间",
    "Zeilenstufenform": "行阶梯形",
    "Zeilenumformung": "行变换",
    "Zerlegung": "分解",
    "Zielraum": "陪域/目标空间",
}

BLACKLIST = {
    "Aufgabe", "Aufgaben", "Lösung", "Lösungen", "Lösungsskizze", "Beispiel", "Beispiele",
    "Kapitel", "Seite", "Seiten", "Teil", "Punkte", "Punkt", "Fall", "Fälle", "Schritt",
    "Definition", "Theorem", "Bemerkung", "Hinweis", "Recap", "Tutorium", "Klausur",
    "Hausaufgabe", "Fingerübung", "Übungsaufgabe", "Rechnung", "Rechnungen",
    "Definition", "Definitionen", "Theorem", "Theorems", "Motivation", "Berechnung",
    "Berechnungen", "gibt", "sind", "ist", "besitzt", "tauchen", "selbst", "eine",
    "einer", "eines", "geben", "gelten", "Methoden", "Methode", "Lineare", "Linearen",
    "Charakteristische",
}

MATH_ROOTS = [
    "abbild", "abgeschlossen", "additiv", "adjung", "affin", "algebra", "assoziativ",
    "basis", "bijektiv", "charakter", "cauchy", "definit", "determin", "diagonal", "dimension", "distributiv", "dreieck", "eigen",
    "einheits", "endomorph", "erzeug", "faktor", "gauss", "gleichung", "gram",
    "hauptachsen", "homogen", "hyper", "identität", "injektiv", "inner", "interpolation",
    "invers", "kern", "koeffizient", "kofaktor", "kombination", "koordinat", "kovarianz",
    "kommutativ", "linear", "lösung", "markov", "matrix", "minimal", "monoton", "neutral", "normal", "norm", "null",
    "orthogonal", "orthonormal", "pagerank", "parameter", "permutation", "pivot",
    "polynom", "positiv", "projektion", "quadratisch", "rang", "residu", "rotation", "skalar",
    "spalte", "spann", "spektral", "spiegel", "stationär", "stochast", "subadditiv", "surjektiv",
    "symmetr", "transitiv", "transform", "transpon", "trivial", "unterraum", "vektor", "vielfach",
    "zeile", "zerlegung", "zielraum",
]

PHRASE_ADJECTIVES = [
    "algebraische", "charakteristische", "diagonale", "elementare", "geometrische",
    "homogene", "inhomogene", "inverse", "komplexe", "lineare", "orthogonale",
    "orthonormale", "positiv", "negativ", "quadratische", "reduzierte", "singuläre",
    "stochastische", "symmetrische", "transponierte", "triviale",
]

KNOWN_TRANSLATIONS = {
    **GLOSSARY,
    "Eigenräume": "特征空间（复数形式）",
    "Eigenwerte": "特征值（复数形式）",
    "Eigenvektoren": "特征向量（复数形式）",
    "Matrizen": "矩阵（复数形式）",
    "Vektoren": "向量（复数形式）",
    "Untervektorräume": "子向量空间（复数形式）",
    "Spalten": "列",
    "Zeilen": "行",
    "Spaltenvektoren": "列向量（复数形式）",
    "Zeilenvektoren": "行向量（复数形式）",
    "Eigenvektorbasis": "特征向量基",
    "Matrixdarstellung": "矩阵表示",
    "Matrixmultiplikation": "矩阵乘法",
    "Matrixgleichung": "矩阵方程",
    "Koeffizientenmatrix": "系数矩阵",
    "Übergangsmatrix": "转移矩阵",
    "Projektionsmatrix": "投影矩阵",
    "Drehmatrix": "旋转矩阵",
    "Spiegelungsmatrix": "反射矩阵",
    "Nullmatrix": "零矩阵",
    "Nullvektoren": "零向量（复数形式）",
    "LGS": "线性方程组缩写",
    "RREF": "简化行阶梯形缩写",
    "Normalgleichungen": "正规方程（复数形式）",
    "Eigenwertgleichung": "特征值方程",
    "Eigenwertgleichungen": "特征值方程（复数形式）",
    "charakteristischen Polynoms": "特征多项式（属格形式）",
    "charakteristische Gleichung": "特征方程",
    "geometrische Vielfachheit": "几何重数",
    "algebraische Vielfachheit": "代数重数",
    "orthogonale Projektion": "正交投影",
    "orthogonales Komplement": "正交补",
    "orthogonale Matrix": "正交矩阵",
    "symmetrische Matrix": "对称矩阵",
    "stochastische Matrix": "随机矩阵",
    "inverse Matrix": "逆矩阵",
    "transponierte Matrix": "转置矩阵",
    "lineare Abbildungen": "线性映射（复数形式）",
    "lineare Abbildung": "线性映射",
    "lineare Gleichung": "线性方程",
    "lineare Gleichungen": "线性方程（复数形式）",
    "lineare Unabhängigkeit": "线性无关性",
    "lineare Abhängigkeit": "线性相关性",
    "lineare Kombination": "线性组合",
    "lineare Kombinationen": "线性组合（复数形式）",
    "lineare Hülle": "线性包",
    "homogene Gleichungssysteme": "齐次方程组（复数形式）",
    "inhomogene Gleichungssysteme": "非齐次方程组（复数形式）",
    "triviale Lösung": "平凡解",
    "nichttriviale Lösung": "非平凡解",
    "allgemeine Lösung": "通解",
    "eindeutige Lösung": "唯一解",
    "unendlich viele Lösungen": "无穷多解",
    "keine Lösung": "无解",
    "positiv definit": "正定",
    "positiv semidefinit": "半正定",
    "negativ definit": "负定",
    "negativ semidefinit": "半负定",
    "quadratische Formen": "二次型（复数形式）",
    "Singulärwerte": "奇异值（复数形式）",
    "Singulärwertzerlegung": "奇异值分解",
}

ROOT_TRANSLATIONS = [
    ("eigen", "特征值/特征向量相关"),
    ("matrix", "矩阵相关"),
    ("vektor", "向量相关"),
    ("basis", "基相关"),
    ("kern", "核空间相关"),
    ("rang", "秩相关"),
    ("spalte", "列空间/列向量相关"),
    ("zeile", "行/行变换相关"),
    ("gleichung", "方程相关"),
    ("lösung", "解相关"),
    ("linear", "线性相关术语"),
    ("orthogonal", "正交相关"),
    ("projektion", "投影相关"),
    ("diagonal", "对角化相关"),
    ("determin", "行列式相关"),
    ("skalar", "内积/标量相关"),
    ("norm", "范数相关"),
    ("quadratisch", "二次型相关"),
    ("singulär", "奇异值/SVD相关"),
    ("spektral", "谱分解相关"),
    ("stochast", "随机矩阵/马尔可夫相关"),
    ("markov", "马尔可夫链相关"),
    ("koordinat", "坐标相关"),
    ("polynom", "多项式相关"),
    ("abbild", "映射相关"),
    ("transform", "变换相关"),
    ("invers", "逆矩阵相关"),
    ("symmetr", "对称矩阵相关"),
    ("definit", "正定/负定相关"),
    ("homogen", "齐次/非齐次相关"),
]


def run_pdftotext(pdf: Path, out: Path) -> str:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists() or out.stat().st_mtime < pdf.stat().st_mtime:
        subprocess.run(["pdftotext", "-layout", str(pdf), str(out)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out.read_text(encoding="utf-8", errors="ignore") if out.exists() else ""


def collect_text() -> str:
    chunks = []
    TEXT_DIR.mkdir(exist_ok=True)
    for dirname in SCAN_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_dir():
                continue
            suffix = path.suffix.lower()
            if suffix == ".pdf":
                rel = path.relative_to(ROOT)
                txt_path = TEXT_DIR / rel.with_suffix(".txt")
                chunks.append(run_pdftotext(path, txt_path))
            elif suffix in {".txt", ".md", ".csv"}:
                chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(chunks)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()


def present(term: str, text: str) -> bool:
    needle = re.escape(term.lower()).replace("\\ ", r"\s+")
    return re.search(rf"(?<![a-zäöüß]){needle}(?![a-zäöüß])", text, flags=re.I) is not None


def example_sentence(term: str, chinese: str) -> str:
    return f"Der Begriff {term} ist in der linearen Algebra ein wichtiger Fachausdruck.（术语 {term} 是线性代数中的重要专业表达，意思是{chinese}。）"


def is_math_term(term: str) -> bool:
    if term in BLACKLIST or len(term) < 4:
        return False
    if term.endswith("-") or re.search(r"\b[A-Za-zÄÖÜäöüß]{2,}-$", term):
        return False
    parts = re.split(r"\s+|-", term)
    if any(p in BLACKLIST for p in parts):
        return False
    if re.search(r"(stu|sy|vor|wer|fol|abha|definiti|voru)$", term, flags=re.I) and term not in KNOWN_TRANSLATIONS:
        return False
    if re.search(r"(ein|eintra|ali|ita|kom|kombinati)$", term, flags=re.I) and term not in KNOWN_TRANSLATIONS:
        return False
    if term in {"Lineare", "Linearen", "Linear", "Charakteristische"}:
        return False
    if term.isupper() and term not in {"LGS", "RREF", "SVD", "PCA", "QR"}:
        return False
    if term.lower().startswith("definition") and not term.lower().startswith("definitionsbereich"):
        return False
    if len(term) > 45 and term not in KNOWN_TRANSLATIONS:
        return False
    low = term.lower()
    if any(root in low for root in MATH_ROOTS):
        return True
    if " " in term and any(term.lower().startswith(adj) for adj in PHRASE_ADJECTIVES):
        return True
    return False


def guess_translation(term: str) -> str:
    if term in KNOWN_TRANSLATIONS:
        return KNOWN_TRANSLATIONS[term]
    low = term.lower()
    for root, chinese in ROOT_TRANSLATIONS:
        if root in low:
            return chinese
    return "数学相关术语"


def extract_candidates(raw_text: str) -> Counter:
    counter = Counter()
    token_re = re.compile(r"\b[A-ZÄÖÜ][A-Za-zÄÖÜäöüß-]{3,}\b")
    for m in token_re.finditer(raw_text):
        term = m.group(0).strip("-")
        if is_math_term(term):
            counter[term] += 1

    adjective_forms = PHRASE_ADJECTIVES + [a[:1].upper() + a[1:] for a in PHRASE_ADJECTIVES]
    phrase_re = re.compile(
        r"\b("
        + "|".join(map(re.escape, adjective_forms))
        + r")\s+[A-ZÄÖÜ][A-Za-zÄÖÜäöüß-]{3,}"
    )
    for m in phrase_re.finditer(raw_text):
        phrase = re.sub(r"\s+", " ", m.group(0)).strip()
        if is_math_term(phrase):
            counter[phrase] += 2
    return counter


def main():
    raw_text = collect_text()
    text = normalize(raw_text)
    candidate_counter = extract_candidates(raw_text)
    rows_by_key = {}
    for term, chinese in sorted(GLOSSARY.items(), key=lambda x: x[0].lower()):
        if present(term, text):
            rows_by_key[term.lower()] = [term, chinese, example_sentence(term, chinese)]
    for term, count in candidate_counter.items():
        if count < 2 and term not in KNOWN_TRANSLATIONS:
            continue
        chinese = guess_translation(term)
        if chinese == "数学相关术语":
            continue
        rows_by_key.setdefault(term.lower(), [term, chinese, example_sentence(term, chinese)])
    rows = [rows_by_key[k] for k in sorted(rows_by_key)]
    out_path = OUT
    try:
        f = out_path.open("w", encoding="utf-8-sig", newline="")
    except PermissionError:
        out_path = ROOT / "lawords_new.csv"
        f = out_path.open("w", encoding="utf-8-sig", newline="")
    with f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"wrote {out_path} with {len(rows)} terms")


if __name__ == "__main__":
    main()
