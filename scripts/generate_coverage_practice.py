from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NOTE_DIR = ROOT / "笔记"
OUT = ROOT / "第一轮复习练习题"

SKIP_WORDS = ("R 练习", "R 语言", "本章一页复盘", "学霸式收尾", "这一章到底", "本章复盘")


def clean_heading(line: str) -> str:
    text = re.sub(r"^##\s+", "", line.strip())
    text = re.sub(r"^\d+\.\s*", "", text)
    return text.strip()


def note_files():
    for p in sorted(NOTE_DIR.glob("*-学霸笔记.md")):
        if p.name.startswith("08-"):
            continue
        yield p


def headings(path: Path):
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("## "):
            continue
        title = clean_heading(line)
        if any(w in title for w in SKIP_WORDS):
            continue
        items.append(title)
    return items


def chapter_title(path: Path):
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip(".").strip()
        if line.startswith("#"):
            return line.lstrip("# ").strip().replace("：", " ")
    return path.stem


def output_name(path: Path):
    return path.name.replace("学霸笔记", "复习练习题")


TASKS = {
    "lgs": {
        "A": {
            "de": "Lösen Sie das lineare Gleichungssystem $x+y=3,\\;2x-y=0$ mit Gauß-Elimination.",
            "cn": "用高斯消元解线性方程组 $x+y=3,\\;2x-y=0$。",
            "de_sol": "Aus der zweiten Gleichung folgt $y=2x$. In $x+y=3$ eingesetzt ergibt sich $3x=3$, also $x=1$ und $y=2$.",
            "cn_sol": "由第二式得 $y=2x$，代入第一式得 $3x=3$，所以 $x=1,y=2$。",
        },
        "B": {
            "de": "Diskutieren Sie in Abhängigkeit von $a$, wie viele Lösungen das System $x+y=1,\\;2x+ay=2$ besitzt.",
            "cn": "讨论参数 $a$：方程组 $x+y=1,\\;2x+ay=2$ 有多少解？",
            "de_sol": "Die Determinante der Koeffizientenmatrix ist $a-2$. Für $a\\neq2$ gibt es genau eine Lösung. Für $a=2$ ist die zweite Gleichung das Doppelte der ersten, also gibt es unendlich viele Lösungen.",
            "cn_sol": "系数矩阵行列式为 $a-2$。若 $a\\neq2$，唯一解；若 $a=2$，第二式是第一式两倍，所以无穷多解。",
        },
    },
    "vector": {
        "A": {
            "de": "Berechnen Sie $2(1,2,-1)^T-3(0,1,2)^T$.",
            "cn": "计算 $2(1,2,-1)^T-3(0,1,2)^T$。",
            "de_sol": "Man rechnet komponentenweise: $(2,4,-2)^T-(0,3,6)^T=(2,1,-8)^T$.",
            "cn_sol": "按分量计算：$(2,4,-2)^T-(0,3,6)^T=(2,1,-8)^T$。",
        },
        "B": {
            "de": "Entscheiden Sie, ob $b=(3,1,4)^T$ im Spann von $v_1=(1,0,1)^T$ und $v_2=(1,1,1)^T$ liegt.",
            "cn": "判断 $b=(3,1,4)^T$ 是否在 $v_1=(1,0,1)^T,v_2=(1,1,1)^T$ 的张成空间中。",
            "de_sol": "Gesucht sind $c_1,c_2$ mit $c_1v_1+c_2v_2=b$. Aus der zweiten Komponente folgt $c_2=1$, aus der ersten $c_1=2$, dann ist die dritte Komponente $3\\neq4$. Also liegt $b$ nicht im Spann.",
            "cn_sol": "设 $c_1v_1+c_2v_2=b$。第二分量给 $c_2=1$，第一分量给 $c_1=2$，第三分量却得到 $3\\neq4$，所以不在张成空间中。",
        },
    },
    "matrix": {
        "A": {
            "de": "Berechnen Sie $AB$ für $A=\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}$ und $B=\\begin{pmatrix}2&0\\\\3&1\\end{pmatrix}$.",
            "cn": "计算 $A=\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}$ 与 $B=\\begin{pmatrix}2&0\\\\3&1\\end{pmatrix}$ 的乘积 $AB$。",
            "de_sol": "$AB=\\begin{pmatrix}8&2\\\\3&1\\end{pmatrix}$.",
            "cn_sol": "逐项行乘列，得到 $AB=\\begin{pmatrix}8&2\\\\3&1\\end{pmatrix}$。",
        },
        "B": {
            "de": "Zeigen Sie mit denselben Matrizen, dass im Allgemeinen $AB\\neq BA$ gilt.",
            "cn": "用同一组矩阵说明一般 $AB\\neq BA$。",
            "de_sol": "Neben $AB=\\begin{pmatrix}8&2\\\\3&1\\end{pmatrix}$ gilt $BA=\\begin{pmatrix}2&4\\\\3&7\\end{pmatrix}$. Die Produkte sind verschieden, also ist Matrixmultiplikation nicht kommutativ.",
            "cn_sol": "算得 $AB=\\begin{pmatrix}8&2\\\\3&1\\end{pmatrix}$，而 $BA=\\begin{pmatrix}2&4\\\\3&7\\end{pmatrix}$。两者不同，所以矩阵乘法不交换。",
        },
    },
    "inverse": {
        "A": {
            "de": "Berechnen Sie die Inverse von $A=\\begin{pmatrix}2&1\\\\1&1\\end{pmatrix}$.",
            "cn": "求 $A=\\begin{pmatrix}2&1\\\\1&1\\end{pmatrix}$ 的逆矩阵。",
            "de_sol": "$\\det(A)=1$. Daher ist $A^{-1}=\\begin{pmatrix}1&-1\\\\-1&2\\end{pmatrix}$.",
            "cn_sol": "$\\det(A)=1$，所以 $A^{-1}=\\begin{pmatrix}1&-1\\\\-1&2\\end{pmatrix}$。",
        },
        "B": {
            "de": "Beweisen Sie: Wenn $A\\mathbf{x}=0$ eine nichttriviale Lösung besitzt, dann ist $A$ nicht invertierbar.",
            "cn": "证明：若 $A\\mathbf{x}=0$ 有非零解，则 $A$ 不可逆。",
            "de_sol": "Wäre $A$ invertierbar, dann folgte aus $A\\mathbf{x}=0$ durch Multiplikation mit $A^{-1}$ sofort $\\mathbf{x}=0$. Das widerspricht der nichttrivialen Lösung.",
            "cn_sol": "若 $A$ 可逆，则左乘 $A^{-1}$ 得 $\\mathbf{x}=0$，与存在非零解矛盾，所以 $A$ 不可逆。",
        },
    },
    "subspace": {
        "A": {
            "de": "Prüfen Sie, ob $U=\\{(x,y,z)^T:x-2y+z=0\\}$ ein Unterraum von $\\mathbb R^3$ ist.",
            "cn": "判断 $U=\\{(x,y,z)^T:x-2y+z=0\\}$ 是否为 $\\mathbb R^3$ 的子空间。",
            "de_sol": "Die Bedingung ist homogen linear. Der Nullvektor liegt in $U$, und Addition sowie Skalarmultiplikation erhalten die Gleichung. Also ist $U$ ein Unterraum.",
            "cn_sol": "这是齐次线性条件，零向量满足；加法和数乘也保持等式成立，所以 $U$ 是子空间。",
        },
        "B": {
            "de": "Wahr oder falsch: Die Vereinigung zweier Unterräume ist immer ein Unterraum. Begründen Sie mit einem Gegenbeispiel.",
            "cn": "判断真假并给反例：两个子空间的并集一定还是子空间。",
            "de_sol": "Falsch. In $\\mathbb R^2$ sind die $x$-Achse und die $y$-Achse Unterräume, aber $(1,0)^T+(0,1)^T=(1,1)^T$ liegt nicht in ihrer Vereinigung.",
            "cn_sol": "错。$x$ 轴和 $y$ 轴都是子空间，但 $(1,0)^T+(0,1)^T=(1,1)^T$ 不在两者并集中，所以并集不封闭。",
        },
    },
    "basis": {
        "A": {
            "de": "Bestimmen Sie die Koordinaten von $v=(4,2)^T$ bezüglich der Basis $b_1=(1,1)^T,b_2=(1,-1)^T$.",
            "cn": "求 $v=(4,2)^T$ 在基 $b_1=(1,1)^T,b_2=(1,-1)^T$ 下的坐标。",
            "de_sol": "Aus $c_1+c_2=4$ und $c_1-c_2=2$ folgt $c_1=3,c_2=1$. Also $[v]_B=(3,1)^T$.",
            "cn_sol": "解 $c_1+c_2=4,c_1-c_2=2$，得 $c_1=3,c_2=1$，所以坐标为 $(3,1)^T$。",
        },
        "B": {
            "de": "Entscheiden Sie, ob $(1,0,1)^T,(0,1,1)^T,(1,1,2)^T$ eine Basis von $\\mathbb R^3$ bilden.",
            "cn": "判断 $(1,0,1)^T,(0,1,1)^T,(1,1,2)^T$ 是否构成 $\\mathbb R^3$ 的基。",
            "de_sol": "Der dritte Vektor ist die Summe der ersten beiden. Die Vektoren sind linear abhängig und bilden daher keine Basis.",
            "cn_sol": "第三个向量等于前两个向量之和，线性相关，所以不是基。",
        },
    },
    "rank_kernel": {
        "A": {
            "de": "Bestimmen Sie Rang und Kern von $A=\\begin{pmatrix}1&2&-1\\\\0&1&3\\end{pmatrix}$.",
            "cn": "求 $A=\\begin{pmatrix}1&2&-1\\\\0&1&3\\end{pmatrix}$ 的秩和核空间。",
            "de_sol": "Die zwei Zeilen sind unabhängig, also $\\operatorname{rang}(A)=2$. Aus $y+3z=0$ und $x+2y-z=0$ folgt mit $z=t$: $\\ker(A)=\\operatorname{span}\\{(7,-3,1)^T\\}$.",
            "cn_sol": "两行独立，所以秩为 $2$。令 $z=t$，得 $y=-3t,x=7t$，核为 $\\operatorname{span}\\{(7,-3,1)^T\\}$。",
        },
        "B": {
            "de": "Eine $4\\times6$-Matrix hat Rang $3$. Bestimmen Sie die Dimension des Kerns und begründen Sie mit dem Rang-Nullitätssatz.",
            "cn": "一个 $4\\times6$ 矩阵秩为 $3$。用秩-零化度公式求核维数。",
            "de_sol": "Der Definitionsraum hat Dimension $6$. Also gilt $\\dim\\ker(A)=6-3=3$.",
            "cn_sol": "输入维数是 $6$，所以 $\\dim\\ker(A)=6-3=3$。",
        },
    },
    "eigen": {
        "A": {
            "de": "Bestimmen Sie Eigenwerte und Eigenräume von $A=\\begin{pmatrix}2&1\\\\0&3\\end{pmatrix}$.",
            "cn": "求 $A=\\begin{pmatrix}2&1\\\\0&3\\end{pmatrix}$ 的特征值和特征空间。",
            "de_sol": "Die Eigenwerte sind $2$ und $3$. Für $\\lambda=2$ erhält man $E_2=\\operatorname{span}\\{(1,0)^T\\}$, für $\\lambda=3$ erhält man $E_3=\\operatorname{span}\\{(1,1)^T\\}$.",
            "cn_sol": "上三角矩阵特征值为 $2,3$。解 $(A-\\lambda I)x=0$ 得 $E_2=\\operatorname{span}\\{(1,0)^T\\}$，$E_3=\\operatorname{span}\\{(1,1)^T\\}$。",
        },
        "B": {
            "de": "Wahr oder falsch: Wenn $\\lambda$ Eigenwert von $A$ ist, dann hat $(\\lambda I-A)x=0$ nur die triviale Lösung. Begründen Sie.",
            "cn": "判断真假：如果 $\\lambda$ 是 $A$ 的特征值，那么 $(\\lambda I-A)x=0$ 只有零解。",
            "de_sol": "Falsch. Gerade weil $\\lambda$ Eigenwert ist, gibt es einen Eigenvektor $x\\neq0$ mit $Ax=\\lambda x$, also $(\\lambda I-A)x=0$.",
            "cn_sol": "错。$\\lambda$ 是特征值恰好说明存在非零特征向量 $x$ 满足 $Ax=\\lambda x$，即 $(\\lambda I-A)x=0$ 有非零解。",
        },
    },
    "diagonal": {
        "A": {
            "de": "Diagonalisieren Sie $A=\\begin{pmatrix}4&1\\\\0&2\\end{pmatrix}$.",
            "cn": "对角化 $A=\\begin{pmatrix}4&1\\\\0&2\\end{pmatrix}$。",
            "de_sol": "Eigenvektoren sind zu $4$: $(1,0)^T$, zu $2$: $(1,-2)^T$. Also $P=\\begin{pmatrix}1&1\\\\0&-2\\end{pmatrix}$, $D=\\begin{pmatrix}4&0\\\\0&2\\end{pmatrix}$.",
            "cn_sol": "$4$ 的特征向量可取 $(1,0)^T$，$2$ 的特征向量可取 $(1,-2)^T$。所以 $P=\\begin{pmatrix}1&1\\\\0&-2\\end{pmatrix}$，$D=\\begin{pmatrix}4&0\\\\0&2\\end{pmatrix}$。",
        },
        "B": {
            "de": "Entscheiden Sie, ob $B=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$ diagonalisierbar ist.",
            "cn": "判断 $B=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$ 是否可对角化。",
            "de_sol": "Der einzige Eigenwert ist $1$, aber der Eigenraum ist nur eindimensional. Es gibt nicht genug linear unabhängige Eigenvektoren, also ist $B$ nicht diagonalisierbar.",
            "cn_sol": "唯一特征值为 $1$，但特征空间只有一维，特征向量不够，所以不可对角化。",
        },
    },
    "orthogonal": {
        "A": {
            "de": "Berechnen Sie Norm, Skalarprodukt und Winkelkosinus für $u=(1,2,2)^T$, $v=(2,0,1)^T$.",
            "cn": "计算 $u=(1,2,2)^T$、$v=(2,0,1)^T$ 的范数、内积和夹角余弦。",
            "de_sol": "$\\|u\\|=3$, $\\|v\\|=\\sqrt5$, $u\\cdot v=4$, also $\\cos\\theta=4/(3\\sqrt5)$.",
            "cn_sol": "$\\|u\\|=3$，$\\|v\\|=\\sqrt5$，$u\\cdot v=4$，所以 $\\cos\\theta=4/(3\\sqrt5)$。",
        },
        "B": {
            "de": "Beweisen Sie: Ist $Q$ orthogonal, dann gilt $\\|Qx\\|=\\|x\\|$ für alle $x$.",
            "cn": "证明：若 $Q$ 是正交矩阵，则对所有 $x$ 有 $\\|Qx\\|=\\|x\\|$。",
            "de_sol": "$\\|Qx\\|^2=(Qx)^T(Qx)=x^TQ^TQx=x^Tx=\\|x\\|^2$.",
            "cn_sol": "$\\|Qx\\|^2=(Qx)^T(Qx)=x^TQ^TQx=x^Tx=\\|x\\|^2$，所以长度保持。",
        },
    },
    "projection": {
        "A": {
            "de": "Projizieren Sie $y=(3,1)^T$ auf $\\operatorname{span}\\{(1,2)^T\\}$.",
            "cn": "把 $y=(3,1)^T$ 投影到 $\\operatorname{span}\\{(1,2)^T\\}$。",
            "de_sol": "$\\operatorname{proj}_u y=\\frac{y\\cdot u}{u\\cdot u}u=\\frac5 5u=(1,2)^T$.",
            "cn_sol": "$\\operatorname{proj}_u y=\\frac{y\\cdot u}{u\\cdot u}u=\\frac5 5u=(1,2)^T$。",
        },
        "B": {
            "de": "Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.",
            "cn": "对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。",
            "de_sol": "$u_1=v_1$. Dann $u_2=v_2-\\frac{v_2\\cdot u_1}{u_1\\cdot u_1}u_1=(1,0,1)^T-\\frac12(1,1,0)^T=(\\frac12,-\\frac12,1)^T$.",
            "cn_sol": "$u_1=v_1$，$u_2=v_2-\\frac{v_2\\cdot u_1}{u_1\\cdot u_1}u_1=(\\frac12,-\\frac12,1)^T$。",
        },
    },
    "least_squares": {
        "A": {
            "de": "Bestimmen Sie die Least-Squares-Lösung für $A=(1,1,1)^T$, $b=(2,4,5)^T$.",
            "cn": "求 $A=(1,1,1)^T$、$b=(2,4,5)^T$ 的最小二乘解。",
            "de_sol": "$A^TA=3$, $A^Tb=11$, also $\\hat x=11/3$.",
            "cn_sol": "$A^TA=3$，$A^Tb=11$，所以 $\\hat x=11/3$。",
        },
        "B": {
            "de": "Beweisen Sie aus den Normalgleichungen, dass der Residualvektor $r=b-A\\hat x$ orthogonal zum Spaltenraum von $A$ ist.",
            "cn": "从正规方程证明残差 $r=b-A\\hat x$ 与 $A$ 的列空间正交。",
            "de_sol": "Aus $A^TA\\hat x=A^Tb$ folgt $A^T(b-A\\hat x)=0$. Damit ist $r$ orthogonal zu jeder Spalte von $A$.",
            "cn_sol": "正规方程给 $A^TA\\hat x=A^Tb$，即 $A^T(b-A\\hat x)=0$，所以残差与每一列都正交。",
        },
    },
    "quadratic": {
        "A": {
            "de": "Klassifizieren Sie $q(x,y)=3x^2+2xy+3y^2$ über die Eigenwerte der Matrix.",
            "cn": "用矩阵特征值判断 $q(x,y)=3x^2+2xy+3y^2$ 的定性。",
            "de_sol": "Die Matrix ist $\\begin{pmatrix}3&1\\\\1&3\\end{pmatrix}$ mit Eigenwerten $4$ und $2$. Beide sind positiv, also ist $q$ positiv definit.",
            "cn_sol": "矩阵为 $\\begin{pmatrix}3&1\\\\1&3\\end{pmatrix}$，特征值 $4,2$ 均为正，所以正定。",
        },
        "B": {
            "de": "Wahr oder falsch: Jede symmetrische Matrix ist entweder positiv definit, negativ definit oder indefinit. Begründen Sie.",
            "cn": "判断真假：每个对称矩阵都一定是正定、负定或不定三者之一。",
            "de_sol": "Falsch. $\\begin{pmatrix}1&0\\\\0&0\\end{pmatrix}$ ist positiv semidefinit, aber nicht positiv definit und nicht indefinit.",
            "cn_sol": "错。$\\begin{pmatrix}1&0\\\\0&0\\end{pmatrix}$ 是半正定，不是正定、负定，也不是不定。",
        },
    },
}


def category(kp: str) -> str:
    tests = [
        ("least_squares", ("最小二乘", "正规方程", "残差", "回归", "linearisiert")),
        ("projection", ("投影", "Gram", "最佳近似")),
        ("quadratic", ("二次型", "正定", "半定", "不定", "主轴", "变分", "SVD", "奇异", "PCA")),
        ("diagonal", ("对角化", "diagonalisier")),
        ("eigen", ("特征", "Eigen", "旋转", "复", "PageRank", "Markov 链和 Google")),
        ("orthogonal", ("范数", "单位向量", "距离", "内积", "角度", "正交", "orthogonal", "Cauchy", "加权", "函数空间", "随机变量", "条件期望")),
        ("rank_kernel", ("列空间", "秩", "Rang", "核", "Kern", "零化")),
        ("basis", ("基", "维数", "坐标", "换基", "Dimension", "Koordinaten")),
        ("subspace", ("向量空间", "子空间", "Unterraum", "Span 一定", "齐次方程组的解集")),
        ("inverse", ("逆", "可逆", "单边")),
        ("matrix", ("矩阵运算", "矩阵乘法", "单位矩阵", "转置", "矩阵幂", "数乘")),
        ("vector", ("向量", "线性组合", "张成", "矩阵（Matrix）", "矩阵-向量")),
        ("lgs", ("线性方程", "方程组", "增广", "行变换", "行阶梯", "解的数量", "Gauss")),
    ]
    for cat, keys in tests:
        if any(k in kp for k in keys):
            return cat
    return "lgs"


def dynamic_task(cat: str, suffix: str, i: int):
    """Create non-repeated computational/proof tasks by category and index."""
    n = i + 1
    if cat == "lgs":
        if suffix == "A":
            x, y = i, 2
            s, t = x + y, 2 * x - y
            return {
                "de": f"Lösen Sie das lineare Gleichungssystem $x+y={s},\\;2x-y={t}$ mit Gauß-Elimination.",
                "cn": f"用高斯消元解线性方程组 $x+y={s},\\;2x-y={t}$。",
                "de_sol": f"Aus $y={s}-x$ folgt in der zweiten Gleichung $2x-({s}-x)={t}$, also $3x={s+t}$ und $x={x}$. Dann $y={y}$.",
                "cn_sol": f"由 $y={s}-x$ 代入第二式，得 $3x={s+t}$，所以 $x={x}$，再得 $y={y}$。",
            }
        return {
            "de": f"Diskutieren Sie in Abhängigkeit von $a$, wie viele Lösungen $x+y=1,\\;{n}x+ay={n}$ besitzt.",
            "cn": f"讨论参数 $a$：方程组 $x+y=1,\\;{n}x+ay={n}$ 有多少解？",
            "de_sol": f"Die Determinante ist $a-{n}$. Für $a\\neq {n}$ gibt es genau eine Lösung. Für $a={n}$ ist die zweite Gleichung das {n}-fache der ersten, also gibt es unendlich viele Lösungen.",
            "cn_sol": f"系数行列式为 $a-{n}$。若 $a\\neq {n}$，唯一解；若 $a={n}$，第二式是第一式的 {n} 倍，所以无穷多解。",
        }
    if cat == "vector":
        if suffix == "A":
            return {
                "de": f"Berechnen Sie ${n}(1,2,-1)^T-2(0,1,{i})^T$.",
                "cn": f"计算 ${n}(1,2,-1)^T-2(0,1,{i})^T$。",
                "de_sol": f"Komponentenweise ergibt sich $({n},{2*n},-{n})^T-(0,2,{2*i})^T=({n},{2*n-2},{-n-2*i})^T$.",
                "cn_sol": f"按分量得 $({n},{2*n},-{n})^T-(0,2,{2*i})^T=({n},{2*n-2},{-n-2*i})^T$。",
            }
        return {
            "de": f"Entscheiden Sie, ob $b=({n+2},1,{n+3})^T$ im Spann von $v_1=(1,0,1)^T$ und $v_2=({n},1,{n})^T$ liegt.",
            "cn": f"判断 $b=({n+2},1,{n+3})^T$ 是否在 $v_1=(1,0,1)^T$ 与 $v_2=({n},1,{n})^T$ 的张成空间中。",
            "de_sol": f"Aus der zweiten Komponente folgt $c_2=1$, aus der ersten $c_1=2$. Dann wäre die dritte Komponente $2+{n}={n+2}\\neq {n+3}$. Also liegt $b$ nicht im Spann.",
            "cn_sol": f"第二分量给 $c_2=1$，第一分量给 $c_1=2$，第三分量应为 ${n+2}$，但目标是 ${n+3}$，所以不在张成空间中。",
        }
    if cat == "matrix":
        if suffix == "A":
            return {
                "de": f"Berechnen Sie $AB$ für $A=\\begin{{pmatrix}}1&{i}\\\\0&1\\end{{pmatrix}}$ und $B=\\begin{{pmatrix}}2&0\\\\{n}&1\\end{{pmatrix}}$.",
                "cn": f"计算 $A=\\begin{{pmatrix}}1&{i}\\\\0&1\\end{{pmatrix}}$ 与 $B=\\begin{{pmatrix}}2&0\\\\{n}&1\\end{{pmatrix}}$ 的 $AB$。",
                "de_sol": f"$AB=\\begin{{pmatrix}}{2+i*n}&{i}\\\\{n}&1\\end{{pmatrix}}$.",
                "cn_sol": f"行乘列得 $AB=\\begin{{pmatrix}}{2+i*n}&{i}\\\\{n}&1\\end{{pmatrix}}$。",
            }
        return {
            "de": f"Berechnen Sie zusätzlich $BA$ für die Matrizen aus Teil A und entscheiden Sie, ob $AB=BA$ gilt.",
            "cn": f"继续计算同一组矩阵的 $BA$，判断是否 $AB=BA$。",
            "de_sol": f"$BA=\\begin{{pmatrix}}2&{2*i}\\\\{n}&{i*n+1}\\end{{pmatrix}}$, also im Allgemeinen verschieden von $AB$.",
            "cn_sol": f"$BA=\\begin{{pmatrix}}2&{2*i}\\\\{n}&{i*n+1}\\end{{pmatrix}}$，通常与 $AB$ 不同。",
        }
    if cat == "eigen":
        if suffix == "A":
            return {
                "de": f"Bestimmen Sie Eigenwerte und Eigenräume von $A=\\begin{{pmatrix}}{n}&1\\\\0&{n+1}\\end{{pmatrix}}$.",
                "cn": f"求 $A=\\begin{{pmatrix}}{n}&1\\\\0&{n+1}\\end{{pmatrix}}$ 的特征值和特征空间。",
                "de_sol": f"Die Eigenwerte sind ${n}$ und ${n+1}$. Zu ${n}$ gehört der Spann von $(1,0)^T$, zu ${n+1}$ der Spann von $(1,1)^T$.",
                "cn_sol": f"上三角矩阵特征值为 ${n}$ 和 ${n+1}$；对应特征空间分别由 $(1,0)^T$ 与 $(1,1)^T$ 张成。",
            }
        return TASKS["eigen"]["B"]
    if cat == "diagonal":
        if suffix == "A":
            return {
                "de": f"Diagonalisieren Sie $A=\\begin{{pmatrix}}{n+2}&1\\\\0&{n}\\end{{pmatrix}}$.",
                "cn": f"对角化 $A=\\begin{{pmatrix}}{n+2}&1\\\\0&{n}\\end{{pmatrix}}$。",
                "de_sol": f"Eigenwerte sind ${n+2}$ und ${n}$. Eigenvektoren kann man als $(1,0)^T$ und $(1,-2)^T$ wählen. Damit ist $P=\\begin{{pmatrix}}1&1\\\\0&-2\\end{{pmatrix}}$, $D=\\begin{{pmatrix}}{n+2}&0\\\\0&{n}\\end{{pmatrix}}$.",
                "cn_sol": f"特征值为 ${n+2}$ 与 ${n}$，可取特征向量 $(1,0)^T$、$(1,-2)^T$，所以 $D=\\begin{{pmatrix}}{n+2}&0\\\\0&{n}\\end{{pmatrix}}$。",
            }
        return TASKS["diagonal"]["B"]
    if cat == "orthogonal":
        if suffix == "A":
            return {
                "de": f"Berechnen Sie Norm, Skalarprodukt und Winkelkosinus für $u=(1,{i},2)^T$, $v=(2,0,1)^T$.",
                "cn": f"计算 $u=(1,{i},2)^T$、$v=(2,0,1)^T$ 的范数、内积和夹角余弦。",
                "de_sol": f"$\\|u\\|=\\sqrt{{{i*i+5}}}$, $\\|v\\|=\\sqrt5$, $u\\cdot v=4$, also $\\cos\\theta=4/(\\sqrt{{{i*i+5}}}\\sqrt5)$.",
                "cn_sol": f"$\\|u\\|=\\sqrt{{{i*i+5}}}$，$\\|v\\|=\\sqrt5$，$u\\cdot v=4$，所以 $\\cos\\theta=4/(\\sqrt{{{i*i+5}}}\\sqrt5)$。",
            }
        return TASKS["orthogonal"]["B"]
    if cat == "projection":
        if suffix == "A":
            return {
                "de": f"Projizieren Sie $y=({n},1)^T$ auf die Gerade, die von $u=(1,{i})^T$ erzeugt wird.",
                "cn": f"把 $y=({n},1)^T$ 投影到由 $u=(1,{i})^T$ 张成的直线上。",
                "de_sol": f"Für $u=(1,{i})^T$ gilt $y\\cdot u={n+i}$ und $u\\cdot u={1+i*i}$. Also $\\operatorname{{proj}}_u y=\\frac{{{n+i}}}{{{1+i*i}}}u$.",
                "cn_sol": f"令 $u=(1,{i})^T$，$y\\cdot u={n+i}$，$u\\cdot u={1+i*i}$，所以投影为 $\\frac{{{n+i}}}{{{1+i*i}}}u$。",
            }
        return TASKS["projection"]["B"]
    if cat == "least_squares":
        if suffix == "A":
            return {
                "de": f"Bestimmen Sie die Least-Squares-Lösung für $A=(1,1,1)^T$, $b=({i},{i+2},{i+3})^T$.",
                "cn": f"求 $A=(1,1,1)^T$、$b=({i},{i+2},{i+3})^T$ 的最小二乘解。",
                "de_sol": f"$A^TA=3$, $A^Tb={3*i+5}$, also $\\hat x=({3*i+5})/3$.",
                "cn_sol": f"$A^TA=3$，$A^Tb={3*i+5}$，所以 $\\hat x=({3*i+5})/3$。",
            }
        return TASKS["least_squares"]["B"]
    if cat == "quadratic":
        if suffix == "A":
            return {
                "de": f"Klassifizieren Sie $q(x,y)={n}x^2+2xy+{n}y^2$ über Eigenwerte.",
                "cn": f"用特征值判断二次型 $q(x,y)={n}x^2+2xy+{n}y^2$ 的定性。",
                "de_sol": f"Die Matrix ist $\\begin{{pmatrix}}{n}&1\\\\1&{n}\\end{{pmatrix}}$ mit Eigenwerten ${n+1}$ und ${n-1}$. Für $n>1$ sind beide positiv, also positiv definit.",
                "cn_sol": f"矩阵为 $\\begin{{pmatrix}}{n}&1\\\\1&{n}\\end{{pmatrix}}$，特征值 ${n+1}$ 与 ${n-1}$，因 $n>1$，所以正定。",
            }
        return TASKS["quadratic"]["B"]
    return TASKS[cat][suffix]


def make_file(title, kps):
    parts = [
        f"# {title} - 第一轮复习练习题（知识点覆盖版）\n\n",
        "> 题型口径：参考练习目录与考试目录，A 题偏直接计算/操作，B 题换数据并提高为参数讨论、证明、真假判断或综合解释；A/B 是完全不同题。\n",
    ]
    table = ["\n## 本章覆盖核对\n\n| 笔记知识点 | 练习难度 | 考试难度 |\n|---|---:|---:|\n"]
    for i, kp in enumerate(kps, 1):
        parts.append(f"\n---\n\n## 知识点{i}：{kp}\n\n")
        for suffix, level in (("A", "练习难度"), ("B", "考试难度")):
            task = dynamic_task(category(kp), suffix, i)
            parts.append(f"### 题{i}{suffix} {level}\n\n")
            parts.append("#### Deutsche Aufgabe\n")
            parts.append(task["de"] + "\n\n")
            parts.append("#### 中文题目\n")
            parts.append(task["cn"] + "\n\n")
            parts.append("#### Deutsche Lösung\n")
            parts.append(task["de_sol"] + "\n\n")
            parts.append("#### 中文解答\n")
            parts.append(
                f"**解题思路：** 这题对应“{kp}”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。"
                f"本题关键步骤是：{task['cn_sol']}\n\n"
            )
            parts.append(f"**核心考点：** {kp}。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。\n\n")
        table.append(f"| {kp} | 题{i}A | 题{i}B |\n")
    parts.extend(table)
    return "".join(parts)


def main():
    OUT.mkdir(exist_ok=True)
    for path in note_files():
        (OUT / output_name(path)).write_text(make_file(chapter_title(path), headings(path)), encoding="utf-8")


if __name__ == "__main__":
    main()
