import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "lawords.csv"
OUT = ROOT / "lawords_clean.csv"

SPECIFIC = {
    "Abgeschlossenheit": "封闭性",
    "Additivität": "可加性",
    "Abbildungen": "映射（复数形式）",
    "Assoziativität": "结合律",
    "Ausgangsmatrix": "初始矩阵",
    "B-Koordinaten": "B基坐标",
    "Basis-Funktionen": "基函数",
    "Basisdarstellung": "基表示",
    "Basismatrizen": "基矩阵",
    "Basissysteme": "基系统",
    "Basisvektoren": "基向量",
    "Batch-Skalarprodukt": "批量内积",
    "Bernoulli-Ungleichung": "伯努利不等式",
    "Cauchy-Schwarz-Ungleichung": "柯西-施瓦茨不等式",
    "Definitheit": "定性/正定性",
    "Distributivität": "分配律",
    "Determinanten": "行列式（复数形式）",
    "Diagonaleinträge": "对角线元素",
    "Diagonalen": "对角线（复数形式）",
    "Eigenräume": "特征空间（复数形式）",
    "Eigenwerte": "特征值（复数形式）",
    "Eigenvektoren": "特征向量（复数形式）",
    "Einheitsvektoren": "单位向量（复数形式）",
    "Frobenius-Skalarprodukt": "Frobenius内积",
    "Gram-Schmidt": "格拉姆-施密特方法",
    "Hauptachsentransformation": "主轴变换",
    "Homogenität": "齐次性",
    "Kernbasis": "核空间的一组基",
    "Kernes": "核（属格形式）",
    "Kerns": "核（属格形式）",
    "Koeffizient": "系数",
    "Koeffizienten": "系数（复数形式）",
    "Koeffizientenvektor": "系数向量",
    "Kofaktoren": "余因子（复数形式）",
    "Kofaktorenentwicklung": "余因子展开",
    "Koordinaten": "坐标（复数形式）",
    "Koordinatensystem": "坐标系",
    "Koordinatensysteme": "坐标系（复数形式）",
    "Koordinatensystemen": "坐标系（复数第三格形式）",
    "Koordinatensystems": "坐标系（属格形式）",
    "Kommutativität": "交换律",
    "Legendre-Polynom-Basen": "勒让德多项式基",
    "Legendre-Polynome": "勒让德多项式（复数形式）",
    "Legendrepolynome": "勒让德多项式（复数形式）",
    "lineare Algebra": "线性代数",
    "lineare Funktion": "线性函数",
    "lineare Funktionen": "线性函数（复数形式）",
    "lineare Operationen": "线性运算",
    "lineare Probleme": "线性问题",
    "lineare Regression": "线性回归",
    "lineare Struktur": "线性结构",
    "lineare Transformationen": "线性变换（复数形式）",
    "Linearitätsbedingung": "线性条件",
    "Linearkombinationen": "线性组合（复数形式）",
    "Lösungsmengen": "解集（复数形式）",
    "Lösungsraum": "解空间",
    "Markovkette": "马尔可夫链",
    "Markovketten": "马尔可夫链（复数形式）",
    "Matrix": "矩阵",
    "Matrix-Vektor": "矩阵-向量",
    "Matrix-Vektor-Multiplikation": "矩阵-向量乘法",
    "Matrix-Vektor-Multiplikationen": "矩阵-向量乘法（复数形式）",
    "Matrizen": "矩阵（复数形式）",
    "Monotonie": "单调性",
    "Neutralität": "中性元性质",
    "Normalgleichungen": "正规方程（复数形式）",
    "Normalisierung": "归一化",
    "Nullstellen": "零点（复数形式）",
    "Orthonormalbasis": "标准正交基",
    "Parameterform": "参数形式",
    "Projektionsmatrix": "投影矩阵",
    "Projektionstheorem": "投影定理",
    "Positivität": "正性",
    "QR-Zerlegung": "QR分解",
    "Rang-Nullität": "秩-零化度",
    "Rang-Nullitätssatz": "秩-零化度定理",
    "Singulärwerte": "奇异值（复数形式）",
    "Skalarmultiplikation": "数乘",
    "Spalten": "列（复数形式）",
    "Spaltenbasis": "列空间的一组基",
    "Spaltenvektoren": "列向量（复数形式）",
    "Spektralzerlegung": "谱分解",
    "Standardbasis": "标准基",
    "Standardmatrix": "标准矩阵",
    "Transformationsmatrix": "变换矩阵",
    "Subadditivität": "次可加性",
    "Transitivität": "传递性",
    "Unterräume": "子空间（复数形式）",
    "Untervektorraum": "子向量空间",
    "Vektoren": "向量（复数形式）",
    "Vektorraums": "向量空间（属格形式）",
    "Zeilen": "行（复数形式）",
    "Zeilenoperation": "行变换",
    "Zeilenoperationen": "行变换（复数形式）",
    "Zeilenvektor": "行向量",
}

CORE_EXTRA_TERMS = [
    "Abgeschlossenheit",
    "Additivität",
    "Assoziativität",
    "Distributivität",
    "Homogenität",
    "Kommutativität",
    "Linearitätsbedingung",
    "Monotonie",
    "Neutralität",
    "Positivität",
    "Skalarmultiplikation",
    "Subadditivität",
    "Transitivität",
]

BAD_CN_MARKERS = ("相关", "数学相关术语")
DROP_TERMS = {
    "Definitionsbereichs",
    "Inverse Methoden",
    "lineare Zusammenhang",
}


def make_example(term: str, cn: str) -> str:
    return f"Der Begriff {term} ist in der linearen Algebra ein wichtiger Fachausdruck.（术语 {term} 是线性代数中的重要专业表达，意思是{cn}。）"


def main():
    rows = []
    seen = set()
    with IN.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            term, cn = row[0].strip(), row[1].strip()
            if term in DROP_TERMS:
                continue
            if term in SPECIFIC:
                cn = SPECIFIC[term]
            elif any(marker in cn for marker in BAD_CN_MARKERS):
                continue
            key = term.lower()
            if key in seen:
                continue
            seen.add(key)
            rows.append([term, cn, make_example(term, cn)])

    existing = {r[0].lower() for r in rows}
    for term in CORE_EXTRA_TERMS:
        if term.lower() not in existing:
            cn = SPECIFIC[term]
            rows.append([term, cn, make_example(term, cn)])
            existing.add(term.lower())

    rows.sort(key=lambda r: r[0].lower())
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"wrote {OUT} with {len(rows)} terms")


if __name__ == "__main__":
    main()
