from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("历史考试")
OUT = ROOT / "历年考试考点汇总.md"


FORMULAS = {
    "线性方程组、秩、核与像": [
        ("高斯消元 / Zeilenstufenform", "$Ax=b$", "把增广矩阵化为阶梯形，判断是否有解、自由变量个数以及解空间基。"),
        ("秩-零化度公式 / Dimensionssatz", "$\\dim\\ker f+\\dim\\operatorname{Bild} f=\\dim V$", "从秩直接推出核维数，或反过来用核维数算像维数。"),
        ("可解性判据 / Lösbarkeitskriterium", "$b\\in\\operatorname{Bild}(A)\\Longleftrightarrow Ax=b\\text{ lösbar}$", "判断右端向量是否在列空间中。"),
    ],
    "矩阵可逆、行列式与秩": [
        ("可逆判据 / Invertierbarkeitskriterium", "$A\\in GL(n,K)\\Longleftrightarrow \\det A\\ne0\\Longleftrightarrow \\operatorname{rang}A=n$", "判断矩阵是否正则、参数取值、有限域矩阵计数。"),
        ("逆矩阵增广法 / Gauß-Jordan", "$(A\\mid I)\\sim(I\\mid A^{-1})$", "直接计算逆矩阵并做验算。"),
        ("行列式乘法公式 / Determinantenmultiplikation", "$\\det(AB)=\\det A\\det B$", "证明投影矩阵、幂零矩阵、转置乘积等命题。"),
    ],
    "子空间、基、维数与仿射空间": [
        ("线性无关 / lineare Unabhängigkeit", "$\\sum_i\\lambda_i v_i=0\\Rightarrow \\lambda_i=0$", "判断一组向量能否做基，或证明补基。"),
        ("维数公式 / Dimensionsformel", "$\\dim(U+V)=\\dim U+\\dim V-\\dim(U\\cap V)$", "处理子空间和、交以及维数问题。"),
        ("仿射包 / affine Hülle", "$p+\\operatorname{span}(v_1-p,\\ldots,v_k-p)$", "把点集生成的仿射空间转成方向子空间计算。"),
    ],
    "群、同构与相似": [
        ("子群判据 / Untergruppenkriterium", "$e\\in G,\\;ab\\in G,\\;a^{-1}\\in G$", "证明矩阵集合在乘法下是子群。"),
        ("同构 / Isomorphismus", "$\\varphi(xy)=\\varphi(x)\\varphi(y)$ 且双射", "把矩阵乘法结构化成熟悉的数乘或整数加法。"),
        ("相似不变量 / Ähnlichkeitsinvariante", "$B=S^{-1}AS$", "证明多项式方程、可逆性、幂、对角线量等在相似下保持。"),
    ],
    "矩阵幂、归纳与多项式方程": [
        ("完全归纳法 / vollständige Induktion", "$P(1)$ 与 $P(n)\\Rightarrow P(n+1)$", "证明矩阵幂闭式，尤其三角矩阵或特殊矩阵。"),
        ("负幂 / negative Potenzen", "$A^{-n}=(A^n)^{-1}$", "把正整数幂公式延伸到整数幂。"),
        ("矩阵多项式 / Matrixpolynom", "$A^2=3A+4I$", "推出 $A$ 可逆、$A^{-1}$ 是 $A,I$ 的线性组合、相似矩阵也满足方程。"),
    ],
    "线性映射与矩阵表示": [
        ("矩阵表示 / darstellende Matrix", "$M=(f(e_1),\\ldots,f(e_n))$", "由线性映射写出标准基下矩阵。"),
        ("秩-核思路 / Rang-Kern-Denken", "$\\operatorname{rang}M=n-\\dim\\ker f$", "含参数映射的秩、核、满射/单射判断。"),
        ("秩一扰动 / Rang-eins-Störung", "$M=I+ba^T$", "处理 $f(x)=x+(a^Tx)b$ 类型问题。"),
    ],
    "特征值、特征空间与对角化": [
        ("特征方程 / charakteristisches Polynom", "$\\chi_A(\\lambda)=\\det(A-\\lambda I)$", "求特征值、代数重数、特征空间。"),
        ("对角化判据 / Diagonalisierbarkeit", "$A\\sim D\\Longleftrightarrow$ 有一组特征向量基", "比较代数重数和几何重数。"),
        ("特征值平移 / Verschiebung", "$Av=\\lambda v\\Rightarrow(A+cI)v=(\\lambda+c)v$", "判断 $A+cI$ 的特征值和特征向量。"),
    ],
    "正交投影、最小二乘与内积": [
        ("正交投影 / orthogonale Projektion", "$v=\\hat v+z,\\;\\hat v\\in W,\\;z\\in W^\\perp$", "把向量分解为子空间部分和垂直误差。"),
        ("法方程 / Normalengleichung", "$A^TAx=A^Tb$", "求最小二乘解。"),
        ("投影保持 / Projektion", "$v\\in W\\Rightarrow \\operatorname{proj}_W(v)=v$", "判断投影命题真假。"),
    ],
    "图、邻接矩阵与矩阵变换": [
        ("邻接矩阵路径计数 / Wegzählung", "$(A^k)_{ij}=$ 长度为 $k$ 的路径数", "由有向图判断矩阵幂是否为零。"),
        ("列空间读图 / Spaltenraum aus Bild", "$A e_i=$ 第 $i$ 列", "从基向量或图形变换读出矩阵、核、像和行列式。"),
    ],
    "抽象向量空间、函数空间与对偶": [
        ("子空间判据 / Unterraumkriterium", "$0\\in U,\\;u+v\\in U,\\;\\alpha u\\in U$", "判断函数集合、矩阵集合是否为向量空间。"),
        ("对偶基 / duale Basis", "$g_i(u_j)=\\delta_{ij}$", "证明对偶基线性无关和表示公式。"),
        ("直积向量空间 / Produktraum", "$V_1\\times\\cdots\\times V_n$", "判断乘积空间的线性结构、维数和基。"),
    ],
}


EXPECTED = {
    "ss00": 6,
    "ss01": 5,
    "ss08": 8,
    "ss17": 8,
    "ss18": 8,
    "ss19": 4,
    "ss19-2": 8,
    "ss20": 4,
    "ss21": 3,
    "ss22考试1": 5,
    "ss22考试2": 5,
    "ss24考试": 5,
    "ss25": 5,
}


ITEMS = [
    # ss00
    ("ss00", 1, "线性方程组、秩、核与像", "Bestimme eine Basis des Lösungsraums eines homogenen linearen Gleichungssystems in vier Variablen.", "求四元齐次线性方程组解空间的一组基。", "Zeilenstufenform bilden, freie Variablen wählen, Basisvektoren ablesen.", "把系数矩阵行化简；主元变量由自由变量表示。引用 $Ax=0$ 的解空间公式，最后把通解拆成自由变量乘向量，即得解空间基。"),
    ("ss00", 2, "矩阵可逆、行列式与秩", "Berechne die inverse Matrix einer gegebenen $3\\times3$-Matrix.", "计算给定 $3\\times3$ 矩阵的逆矩阵。", "Mit $(A\\mid I)\\sim(I\\mid A^{-1})$ rechnen.", "用增广矩阵 $(A\\mid I)$ 做 Gauss-Jordan；左边化为 $I$ 时右边就是 $A^{-1}$。验算可用 $AA^{-1}=I$。"),
    ("ss00", 3, "线性方程组、秩、核与像", "Zeige $b\\in\\operatorname{Bild}(f_A)$ und bestimme Dimensionen von Bild und Kern.", "证明 $b$ 在线性映射的像中，并求像和核的维数。", "Lösbarkeit von $Ax=b$ prüfen; dann Rang und Dimensionssatz nutzen.", "先解 $Ax=b$，若增广矩阵无矛盾行，则 $b\\in\\operatorname{Bild}(A)$。再由 $\dim\\operatorname{Bild}A=\\operatorname{rang}A$ 与 $\dim\\ker A=n-r$ 求维数。"),
    ("ss00", 4, "子空间、基、维数与仿射空间", "Bestimme Dimension einer affinen Hülle und einen parallelen affinen Unterraum durch einen Punkt.", "求点集张成的仿射空间维数，并写出过指定点的平行仿射空间。", "Einen Basispunkt abziehen und den Spann der Differenzvektoren untersuchen.", "选一个点 $p$，把仿射包写成 $p+\\operatorname{span}(q_i-p)$。方向子空间的秩就是仿射空间维数；平行空间换起点不换方向。"),
    ("ss00", 5, "图、邻接矩阵与矩阵变换", "Zeichne den Graphen zu einer Adjazenzmatrix und begründe $A^4=0$.", "根据邻接矩阵画有向图，并说明 $A^4=0$。", "Eintrag von $A^k$ zählt Wege der Länge $k$.", "引用路径计数公式：$(A^4)_{ij}$ 是从 $i$ 到 $j$ 的长度 4 路径数。图中最长路径小于 4，所以所有条目为 0。"),
    ("ss00", 6, "子空间、基、维数与仿射空间", "Für zwei Unterräume $U,V$ zeige Dimensionen und bestimme $\\dim(U+V)$.", "证明两个子空间维数，并求和空间维数。", "Erzeuger auf lineare Unabhängigkeit prüfen und den gemeinsamen Spann identifizieren.", "把生成向量用基 $v_1,\ldots,v_4$ 展开；证明生成元线性无关。然后说明 $U+V=\\operatorname{span}(v_1,v_2,v_3)$，所以维数为 3。"),
    # ss01
    ("ss01", 1, "矩阵可逆、行列式与秩", "Bestimmen Sie die Inverse einer $4\\times4$-Matrix und machen Sie die Probe.", "求 $4\\times4$ 矩阵逆矩阵并验算。", "Gauß-Jordan und anschließende Multiplikationsprobe.", "对 $(A\\mid I)$ 消元，得到 $(I\\mid A^{-1})$；用 $AA^{-1}=I$ 检查。"),
    ("ss01", 2, "线性方程组、秩、核与像", "Bestimmen Sie abhängig von $\\lambda$ alle Lösungen von $Ax=b$.", "按参数 $\\lambda$ 讨论线性方程组所有解。", "Erweiterte Matrix reduzieren; Sonderwerte von $\\lambda$ aus Widerspruchszeilen lesen.", "把 $(A|b)$ 化简；若出现 $0=c(\\lambda)$，则令 $c(\\lambda)=0$ 才有解。之后用自由变量写通解。"),
    ("ss01", 3, "矩阵可逆、行列式与秩", "Klären Sie abstrakt, ob $AB$ mit $A\\in\\mathbb R^{5\\times3}$ und $B\\in\\mathbb R^{3\\times5}$ regulär ist.", "不用大计算判断 $AB$ 是否可逆。", "Rang von $AB$ ist höchstens $3<5$.", "由于 $AB$ 是 $5\\times5$，但 $\operatorname{rang}(AB)\\le\\min(\\operatorname{rang}A,\\operatorname{rang}B)\\le3$，达不到 5，故不可逆。"),
    ("ss01", 4, "矩阵可逆、行列式与秩", "Zählen Sie reguläre $2\\times2$-Matrizen über $\\mathbb F_2$.", "数出有限域 $\\mathbb F_2$ 上可逆 $2\\times2$ 矩阵个数。", "Erste Spalte darf nicht null sein, zweite nicht im Spann der ersten.", "第一列有 $2^2-1=3$ 种非零选择；第二列不能落在第一列张成的一维空间中，有 $4-2=2$ 种，共 6 个。"),
    ("ss01", 5, "线性方程组、秩、核与像", "Zeigen Sie ein Kriterium $\\mathcal L(A,b)\\ne\\emptyset\\Longleftrightarrow Pb=0$ für rangdefiziente Matrizen.", "证明对秩不足矩阵存在矩阵 $P$，使 $Ax=b$ 可解等价于 $Pb=0$。", "Nach Zeilenstufenform müssen die unteren Komponenten des transformierten rechten Vektors verschwinden.", "先把 $A$ 化为有 $r$ 个主元的阶梯形。可解要求零行对应的右端项全为 0；这些条件由矩阵 $P$ 抽取，因此 $Pb=0$ 是可解性判据。"),
    # ss08
    ("ss08", 1, "矩阵幂、归纳与多项式方程", "Beweisen Sie eine geschlossene Formel für eine Matrixpotenz durch vollständige Induktion.", "用数学归纳法证明矩阵幂公式。", "Induktionsanfang prüfen, dann rechte Seite mit der Matrix multiplizieren.", "先验 $n=1$。假设 $A^{2n}$ 公式成立，再乘 $A^2$，整理成 $n+1$ 的形式。核心公式是归纳法 $P(n)\\Rightarrow P(n+1)$。"),
    ("ss08", 2, "群、同构与相似", "Zeigen Sie, dass invertierbare Diagonalmatrizen eine Gruppe bilden; diskutieren Sie nichtnegative Diagonaleinträge.", "证明非零对角元的对角矩阵成群，并讨论对角元非负时是否仍成群。", "Einheit, Produkt und Inverses diagonal prüfen; bei $d_i\\ge0$ fehlt bei $0$ das Inverse.", "非零对角元时乘积和逆仍是非零对角矩阵，单位矩阵也在内。若允许 $d_i=0$，矩阵可能不可逆，所以不是 $GL$ 的子群。"),
    ("ss08", 3, "矩阵可逆、行列式与秩", "Bestimmen Sie Parameterwerte, für die eine $3\\times3$-Matrix invertierbar ist, und berechnen Sie $A^{-1}$.", "按参数判断 $3\\times3$ 矩阵可逆并求逆。", "Determinante als Funktion von $\\alpha$ berechnen, dann Gauß-Jordan.", "先算 $\det A(\\alpha)$，非零时可逆；对这些参数用 $(A|I)$ 化简求逆。"),
    ("ss08", 4, "子空间、基、维数与仿射空间", "Bestimmen Sie eine Basis von $\\operatorname{span}(a,b,c)$ und ergänzen Sie sie mit kanonischen Basisvektoren.", "求三个向量张成空间的基，并判断能用哪些标准基向量补成 $\\mathbb R^3$ 的基。", "Rang der Spaltenmatrix bestimmen und Kandidaten auf Unabhängigkeit testen.", "把 $a,b,c$ 放入矩阵做列消元，保留主元列为基。再逐个加入 $e_i$，若行列式非零或秩升到 3，就可补成基。"),
    ("ss08", 5, "矩阵可逆、行列式与秩", "Berechnen Sie $\\det A$ und den Rang einer komplexen $4\\times4$-Matrix abhängig von $\\alpha$.", "计算复矩阵行列式并按参数求秩。", "Determinante gibt Vollrang; bei Nullfall per Zeilenumformung Rang bestimmen.", "先求 $\det A(\\alpha)$。若非零，秩为 4；若为零，代入特殊参数继续行化简，看主元个数。"),
    ("ss08", 6, "矩阵可逆、行列式与秩", "Beweisen Sie Aussagen zu idempotenten, transponierten und nilpotenten Matrizen.", "证明关于 $A^2=A$、$A^TA$、$A^2=0$ 的命题。", "Determinante und explizite Inverse verwenden.", "对 $A^2=A$ 取行列式得 $(\det A)^2=\det A$。$A^TA$ 可逆等价于 $A$ 可逆。若 $A^2=0$，则 $(I-A)(I+A)=I$。"),
    ("ss08", 7, "特征值、特征空间与对角化", "Bestimmen Sie Eigenraum, charakteristisches Polynom und Eigenwerte einer $3\\times3$-Matrix.", "求给定矩阵的特征空间、特征多项式和特征值。", "Eigenraum durch Kern von $A-\\lambda I$, weitere Eigenwerte über Spur und Polynom.", "先解 $(A-3I)x=0$ 得特征空间；再算或利用迹 $\operatorname{tr}A$ 与已知特征值补出其余特征值。"),
    ("ss08", 8, "特征值、特征空间与对角化", "Berechnen Sie Eigenwerte und Eigenvektoren einer komplexen $2\\times2$-Matrix.", "求复 $2\\times2$ 矩阵的特征值和特征向量。", "Charakteristisches Polynom lösen und Kerne berechnen.", "先求 $\chi_A(\\lambda)=\det(A-\lambda I)$，每个根代入 $(A-\lambda I)x=0$ 得特征向量。"),
    # ss17
    ("ss17", 1, "矩阵幂、归纳与多项式方程", "Zeigen Sie eine Formel für Potenzen einer reellen $3\\times3$-Matrix durch Induktion.", "用归纳法证明 $3\\times3$ 矩阵幂公式。", "Startwert und Multiplikation im Induktionsschritt.", "按 $P(1)$、$P(n)\\Rightarrow P(n+1)$ 写；关键是把右侧闭式乘原矩阵后整理成下一项。"),
    ("ss17", 2, "群、同构与相似", "Für Matrizen $M(a)$: Produkt, Inverses, Untergruppe von $GL(2,\\mathbb R)$ und Isomorphie zu $\\mathbb R^\\times$.", "对矩阵族 $M(a)$ 求乘积、逆，证明成子群并与非零实数乘法同构。", "Zeige $M(a)M(b)=M(ab)$, daraus Inverses und Isomorphismus.", "先算封闭律 $M(a)M(b)=M(ab)$。单位是 $M(1)$，逆是 $M(a^{-1})$；映射 $a\\mapsto M(a)$ 保乘法且双射。"),
    ("ss17", 3, "矩阵可逆、行列式与秩", "Berechnen Sie Determinante einer parametrischen $4\\times4$-Matrix und für $t=0$ die Inverse.", "求参数 $4\\times4$ 矩阵行列式、可逆参数，并在 $t=0$ 求逆。", "Zeilen-/Spaltenumformungen für Determinante, Gauß-Jordan für Inverse.", "先用不改变行列式的初等变换化简 $\det A(t)$；令其非零确定可逆范围。$t=0$ 时用增广法求逆。"),
    ("ss17", 4, "矩阵可逆、行列式与秩", "Untersuchen Sie Aussagen zu schiefsymmetrischen und orthogonalen Matrizen.", "研究反对称矩阵、正交矩阵相关命题。", "Nutze $A^T=-A$, $Q^TQ=I$ und Determinanten.", "反对称给出 $x^TAx=0$ 和行列式奇偶性质；正交矩阵满足 $Q^{-1}=Q^T$、$|\det Q|=1$。"),
    ("ss17", 5, "线性映射与矩阵表示", "Bestimmen Sie Matrix, Kern, Bild und Surjektivität/Injektivität einer linearen Abbildung.", "求线性映射矩阵、核、像，并判断单射满射。", "Bilder der Basisvektoren als Spalten verwenden; Rang-Kern-Satz.", "先写 $M=(f(e_i))$；解 $Mx=0$ 得核，列空间给像。用 $\dim\ker f$ 与 $\operatorname{rang}M$ 判断单射和满射。"),
    ("ss17", 6, "特征值、特征空间与对角化", "Berechnen Sie Eigenwerte und prüfen Sie Diagonalisierbarkeit einer Matrix.", "求特征值并判断对角化。", "Charakteristisches Polynom und Eigenräume vergleichen.", "算 $\chi_A$，求各特征空间维数；若几何重数总和为 $n$，则可对角化。"),
    ("ss17", 7, "特征值、特征空间与对角化", "Untersuchen Sie Eigenwerte einer symmetrischen Rang-eins-Matrix.", "研究对称秩一矩阵的特征值结构。", "Bild liegt im Spann eines Vektors; Orthogonalraum liefert Null-Eigenwerte.", "秩一矩阵 $uu^T$ 的像在 $\operatorname{span}(u)$ 中；与 $u$ 垂直的向量给零特征值，$u$ 方向给非零特征值。"),
    ("ss17", 8, "正交投影、最小二乘与内积", "Behandeln Sie eine quadratische Form/Hauptachsentransformation und bestimmen Sie Extrem- oder Normalform.", "用主轴变换或直接计算处理二次型。", "Symmetrische Matrix orthogonal diagonalisieren.", "把二次型写成 $x^TAx$，对称矩阵可正交对角化；特征值决定标准形、正定性和极值方向。"),
    # ss18
    ("ss18", 1, "矩阵幂、归纳与多项式方程", "Beweisen Sie eine $3\\times3$-Matrixpotenzformel durch vollständige Induktion.", "用归纳法证明 $3\\times3$ 矩阵幂闭式。", "Induktionsanfang plus Matrixmultiplikation.", "照归纳模板：验证首项；假设 $A^n$ 公式，右乘 $A$ 后整理出 $A^{n+1}$。"),
    ("ss18", 2, "群、同构与相似", "Für $M(a)$: berechne Produkt, Inverses, Untergruppe und Isomorphie.", "对参数矩阵族证明乘法结构、逆元、子群和同构。", "Produktformel gibt alle Gruppeneigenschaften.", "先推出 $M(a)M(b)=M(ab)$；单位、逆、封闭性都随之而来。同构映射是 $a\\mapsto M(a)$。"),
    ("ss18", 3, "矩阵可逆、行列式与秩", "Berechnen Sie Determinante und Inverse einer parametrischen Matrix.", "求参数矩阵行列式、可逆范围和逆。", "Determinante über Umformungen; Inverse bei Sonderwert.", "用行列式公式判断 $\det A(t)\ne0$；指定参数下用 Gauss-Jordan 计算。"),
    ("ss18", 4, "矩阵可逆、行列式与秩", "Beweisen Sie Aussagen über spezielle Matrizen wie orthogonale oder schiefsymmetrische Matrizen.", "证明正交、反对称等特殊矩阵性质。", "Transposition, Determinante und Inversenbeziehung einsetzen.", "利用 $Q^TQ=I$ 或 $A^T=-A$，把命题转成行列式、逆矩阵或内积等式。"),
    ("ss18", 5, "线性映射与矩阵表示", "Untersuchen Sie eine lineare Abbildung bezüglich Matrix, Kern, Bild und Rang.", "研究线性映射的矩阵表示、核、像和秩。", "Standardbasisbilder bilden die Spalten; danach Rang-Kern.", "从 $f(e_i)$ 写矩阵；行化简求秩和核。公式 $\dim\ker f=n-\operatorname{rang}M$ 是主线。"),
    ("ss18", 6, "特征值、特征空间与对角化", "Bestimmen Sie Eigenwerte, Eigenräume und Diagonalisierbarkeit.", "求特征值、特征空间并判断对角化。", "Algebraische und geometrische Vielfachheiten vergleichen.", "求 $\chi_A$，对每个特征值解核；若每个几何重数等于代数重数，则对角化。"),
    ("ss18", 7, "特征值、特征空间与对角化", "Gegeben ist eine $3\\times3$-Matrix. Bestimme Rang, charakteristisches Polynom, Eigenräume und entscheide die Diagonalisierbarkeit.", "给定一个 $3\\times3$ 矩阵，求秩、特征多项式、特征空间，并判断是否可对角化。", "Rang und Kern liefern den Eigenwert $0$; dann charakteristisches Polynom, Eigenraum und Vielfachheiten vergleichen.", "先用行化简求秩，并由核非零推出 $0$ 是特征值；再算 $\chi_A(\\lambda)$，求 $E_0=\\ker A$，最后比较几何重数和代数重数判断不可对角化。"),
    ("ss18", 8, "特征值、特征空间与对角化", "Behandeln Sie symmetrische Matrizen, Eigenbasis und orthogonale Diagonalisierung.", "处理对称矩阵、特征基和正交对角化。", "Symmetrische Matrizen besitzen orthogonale Eigenbasis.", "对称矩阵不同特征值的特征向量正交；归一化后组成正交矩阵 $Q$，有 $Q^TAQ=D$。"),
    # ss19
    ("ss19", 1, "群、同构与相似", "Beweisen Sie Potenzformeln für eine Matrix und zeigen Sie eine von ihr erzeugte Untergruppe samt Isomorphie zu $(\\mathbb Z,+)$.", "证明矩阵幂公式，并证明由该矩阵生成的子群与整数加法群同构。", "Positive und negative Potenzen berechnen; $n\\mapsto A^n$ ist Isomorphismus.", "先归纳求 $A^n$，再用逆矩阵处理负幂。集合 $\{A^n:n\in\mathbb Z\}$ 的乘法满足 $A^mA^n=A^{m+n}$，对应整数加法。"),
    ("ss19", 2, "矩阵幂、归纳与多项式方程", "Untersuchen Sie Lösungen der Matrixgleichung $M^2=3M+4I$.", "研究矩阵方程 $M^2=3M+4I$ 的解。", "Skalare Lösungen, Potenzen als Linearkombinationen, Invertierbarkeit und Ähnlichkeit.", "标量情形解 $\gamma^2=3\gamma+4$。若 $A$ 满足方程，则 $A(A-3I)=4I$，所以 $A^{-1}=\\frac14(A-3I)$；相似矩阵保持多项式方程。"),
    ("ss19", 3, "线性映射与矩阵表示", "Für $f(x)=x+(a^Tx)b$: Linearität, Matrix $I+ba^T$, Spur, Kern, Invertierbarkeit und Rang.", "对秩一扰动映射求线性、矩阵、迹、核、可逆性和秩。", "Kern liegt in $\\operatorname{span}(b)$; invertierbar genau bei $a^Tb\\ne-1$.", "先证线性；矩阵为 $I+ba^T$，迹为 $n+a^Tb$。若 $f(x)=0$，则 $x=-(a^Tx)b$，故核在 $b$ 的张成中；判断 $b$ 是否入核得可逆条件。"),
    ("ss19", 4, "特征值、特征空间与对角化", "Untersuchen Sie eine Matrix abhängig von $\\alpha$ auf Eigenwerte, geometrische Vielfachheiten und Diagonalisierbarkeit.", "按参数讨论矩阵的特征值、几何重数和对角化。", "Charakteristisches Polynom $(1-\\lambda)^2(\\alpha-\\lambda)$ und Eigenräume.", "从上三角形式读或算 $\chi_A$；分别讨论 $\alpha=1$ 与 $\alpha\ne1$。比较几何重数与代数重数判断对角化。"),
    # ss19-2
    ("ss19-2", 1, "矩阵幂、归纳与多项式方程", "Zeigen Sie eine Matrixpotenzformel durch vollständige Induktion.", "用归纳法证明矩阵幂公式。", "Induktion über $n$ mit sauberer Matrixmultiplikation.", "首项验证后，假设闭式成立，把 $A^nA$ 化简为 $n+1$ 的闭式。"),
    ("ss19-2", 2, "群、同构与相似", "Zeigen Sie, dass eine parametrisierte Matrixmenge eine kommutative Untergruppe ist und ein Homomorphismus vorliegt.", "证明参数矩阵集合是交换子群，并证明给定映射是群同态。", "Produkt entspricht Addition des Parameters.", "直接乘两矩阵得到参数相加形式；单位取参数 0，逆取相反数，因此成群且交换。同态由乘法公式给出。"),
    ("ss19-2", 3, "矩阵可逆、行列式与秩", "Berechnen Sie Determinante, Invertierbarkeit und gegebenenfalls Inverse einer Matrix.", "计算矩阵行列式、可逆性和逆矩阵。", "Determinante nicht null liefert Invertierbarkeit.", "先展开或消元求 $\det A$，非零则用增广矩阵求逆；零值时说明不可逆或求秩。"),
    ("ss19-2", 4, "矩阵可逆、行列式与秩", "Beweisen Sie Aussagen zu Determinante, Inversen und Rang spezieller Matrizen.", "证明特殊矩阵的行列式、逆和秩相关命题。", "Standardidentitäten für Determinante und Transposition.", "围绕 $\det(AB)=\det A\det B$、$(AB)^{-1}=B^{-1}A^{-1}$、$\operatorname{rang}$ 不等式组织证明。"),
    ("ss19-2", 5, "线性映射与矩阵表示", "Bestimmen Sie Matrix, Kern, Bild und Rang einer linearen Abbildung.", "求线性映射矩阵、核、像和秩。", "Spalten sind Bilder der Basis; Kern durch Gleichungssystem.", "写出矩阵后解 $Mx=0$；主元列张成像，秩和核维数用维数公式核对。"),
    ("ss19-2", 6, "特征值、特征空间与对角化", "Berechnen Sie Eigenwerte und entscheiden Sie Diagonalisierbarkeit.", "求特征值并判断对角化。", "Eigenräume zu allen Eigenwerten berechnen.", "算特征多项式，逐个求特征空间；若特征向量数不足 $n$，不可对角化。"),
    ("ss19-2", 7, "特征值、特征空间与对角化", "Untersuchen Sie eine symmetrische/rangarme Matrix mit Eigenwertmethoden.", "用特征值方法研究对称或低秩矩阵。", "Nutze Rang, Spur und Orthogonalität.", "用迹等于特征值和、秩限制非零特征值个数；对称性保证可正交对角化。"),
    ("ss19-2", 8, "矩阵可逆、行列式与秩", "Entscheiden Sie Wahr/Falsch-Aussagen zu Rang, Kern und Invertierbarkeit.", "判断关于秩、核、可逆性的真假命题。", "Jede Aussage mit Satz oder Gegenbeispiel begründen.", "真命题引用秩-核公式、可逆判据；假命题给小维度反例，常用零矩阵、投影矩阵、奇异对角矩阵。"),
    # ss20
    ("ss20", 1, "群、同构与相似", "Zeigen Sie für eine Menge reeller $3\\times3$-Matrizen Gruppeneigenschaften, Kommutativität und Isomorphie.", "证明某 $3\\times3$ 矩阵集合成交换子群并给出同构。", "Matrixprodukt entspricht Parameteraddition oder -multiplikation.", "找出参数运算规律；单位、逆、封闭性都从参数规律推出。同构用“参数 -> 矩阵”或反向读参数实现。"),
    ("ss20", 2, "矩阵可逆、行列式与秩", "Für $A\\in\\mathbb C^{2\\times3}$ berechnen Sie $AA^T$, $A^TA$ und Ränge abhängig von Parametern.", "对复 $2\\times3$ 矩阵计算 $AA^T$、$A^TA$ 并按参数求秩。", "Zeilen- und Spaltenrang sind gleich; Gramartige Produkte vergleichen.", "先直接乘矩阵；秩由行/列依赖关系判断。用 $\operatorname{rang}A=\operatorname{rang}A^T$ 和相关秩关系核对。"),
    ("ss20", 3, "线性映射与矩阵表示", "Für eine Abbildung mit Parametern $b,c$: Matrix, Rang, Determinante und Kern bestimmen.", "对含参数 $b,c$ 的线性映射求矩阵、秩、行列式和核。", "Blockstruktur nutzen und Fälle nach Parametern trennen.", "先写标准基下矩阵；行列式判断满秩。特殊参数下用行化简求秩和核。"),
    ("ss20", 4, "特征值、特征空间与对角化", "Bestimmen Sie charakteristisches Polynom, Eigenwerte, Eigenräume, Diagonalisierbarkeit und Invertierbarkeit von $A+I$.", "求特征多项式、特征值、特征空间、对角化，并判断 $A+I$ 可逆。", "Eigenwerte von $A+I$ sind $\\lambda+1$.", "先求 $\chi_A$ 和各特征空间；对角化看几何重数。$A+I$ 可逆等价于 $-1$ 不是 $A$ 的特征值。"),
    # ss21
    ("ss21", 1, "群、同构与相似", "Für Matrizen über $\\mathbb Q$: $G\\subset GL(2,\\mathbb Q)$, Inverses, Untergruppe, Isomorphie und Potenzen.", "对有理数域上矩阵族证明可逆、求逆、证明子群与同构，并计算矩阵幂。", "Parameter $k,r$ in Produkt und Inverses verfolgen.", "先用行列式证明在 $GL$ 中；计算乘法得到参数组合规律，再构造与 $(\\mathbb Z,+)\\times(\\mathbb Q^\\times,\\cdot)$ 的同构。幂由同构转成参数幂。"),
    ("ss21", 2, "群、同构与相似", "Untersuchen Sie eine Relation $A\\sim B\\Leftrightarrow A=D^{-1}BD$ mit invertierbarer Diagonalmatrix.", "研究由可逆对角矩阵相似定义的关系。", "Ähnlichkeit mit Diagonalmatrizen ist Äquivalenzrelation und erhält bestimmte Einträge.", "自反取 $D=I$，对称取 $D^{-1}$，传递乘对角矩阵。转置、逆和幂由相似公式推出；对角元和 $a_{ij}a_{ji}$ 是该变换下的不变量。"),
    ("ss21", 3, "线性映射与矩阵表示", "Für eine parametrisierte Abbildung $f:\\mathbb R^n\\to\\mathbb R^n$: Linearität, Matrix für $n=5$, Rang und Kernbasis.", "对参数线性映射证明线性，写 $n=5$ 矩阵，求秩和核基。", "Die Werte hängen nur von zwei Summenarten ab; daher Rangfälle nach $a,b$.", "先用加法和齐次性证明线性；矩阵行只有少数不同类型。按 $a=b$ 或 $a\ne b$ 判断行空间维数；给出的差向量逐个代入 $f$ 为零并验证个数匹配核维数。"),
    # ss22考试1
    ("ss22考试1", 1, "正交投影、最小二乘与内积", "Zerlegen Sie einen Vektor in Projektion auf $W$ und orthogonalen Anteil.", "把向量分解为 $W$ 中投影和垂直分量。", "Normalgleichungen für die Projektion lösen.", "设 $\hat v=c_1u_1+c_2u_2$，要求 $v-\hat v$ 同时垂直 $u_1,u_2$，得到法方程并解系数。"),
    ("ss22考试1", 2, "图、邻接矩阵与矩阵变换", "Bestimmen Sie aus einem gezeichneten linearen Bild $\\ker A$, $\\operatorname{col}A$, Rang, Determinante und Matrix $A$.", "从图形变换读出核、列空间、秩、行列式和矩阵。", "Bilder der Standardbasis sind Spalten von $A$.", "图中 $e_i$ 的像就是矩阵列；列是否共线决定秩和列空间，压到低维则行列式为 0。"),
    ("ss22考试1", 3, "特征值、特征空间与对角化", "Bearbeiten Sie Basis symmetrischer Matrizen, Eigenwertverschiebung, diagonalisierbare Involution und Wahr/Falsch-Aussagen.", "处理对称矩阵空间基、特征值平移、对角化 involution 及真假题。", "Standardbasen und Eigenwertregeln anwenden.", "对称 $2\\times2$ 矩阵基为 $E_{11},E_{22},E_{12}+E_{21}$。若 $Av=\lambda v$，则 $A+cI$ 特征值平移。特征值只有 $\pm1$ 且可对角化时 $U^{-1}=U$。"),
    ("ss22考试1", 4, "矩阵可逆、行列式与秩", "Beweisen Sie: $A$ invertierbar genau dann, wenn lineare Unabhängigkeit aller Vektorfamilien unter $A$ erhalten bleibt.", "证明矩阵可逆当且仅当保持所有线性无关组的线性无关性。", "Richtung über Kern; Gegenrichtung über Bilder der Standardbasis.", "若 $A$ 可逆，$\\sum c_iAv_i=0$ 左乘 $A^{-1}$ 得 $\sum c_iv_i=0$。反向：若保持线性无关，则标准基像线性无关，故矩阵列满秩可逆。"),
    ("ss22考试1", 5, "抽象向量空间、函数空间与对偶", "Untersuchen Sie Dualraum, duale Basis und Darstellungsformel.", "研究对偶空间、对偶基和表示公式。", "Lineare Abbildungen sind durch Basiswerte eindeutig bestimmt.", "标准基时 $g_i(x)=x_i$。证明 $g_i$ 线性无关：令 $\sum c_ig_i=0$，代入 $u_j$ 得 $c_j=0$。表示式在每个基向量上与 $f$ 相同，因此两线性映射相等。"),
    # ss22考试2
    ("ss22考试2", 1, "正交投影、最小二乘与内积", "Lösen Sie eine Projektions- oder Least-Squares-Aufgabe in einem Unterraum.", "求子空间投影或最小二乘问题。", "Orthogonalitätsbedingungen bzw. Normalgleichungen verwenden.", "把未知投影写成基向量线性组合；误差与子空间正交，得到 $A^TAx=A^Tb$。"),
    ("ss22考试2", 2, "图、邻接矩阵与矩阵变换", "Lesen Sie Kern, Bild, Rang, Determinante und Matrix einer linearen Transformation aus einem Bild ab.", "从图中读取线性变换的核、像、秩、行列式和矩阵。", "Spalten sind Bilder der Basisvektoren.", "找 $e_1,e_2,e_3$ 的像作为列；若图像落在平面/直线，核非零且 $\det A=0$。"),
    ("ss22考试2", 3, "特征值、特征空间与对角化", "Bearbeiten Sie mehrere kurze Aussagen zu Eigenwerten, Projektion, Unterräumen und linearer Unabhängigkeit.", "处理关于特征值、投影、子空间、线性无关的多小问。", "Jede Aussage mit Standardformel oder Gegenbeispiel entscheiden.", "特征值平移、投影定义、子空间判据和线性无关定义逐条套用；假命题优先找二维反例。"),
    ("ss22考试2", 4, "矩阵可逆、行列式与秩", "Beweisen Sie ein Kriterium zur Invertierbarkeit über Erhaltung linearer Unabhängigkeit.", "证明用保持线性无关刻画可逆性。", "Invertierbarkeit entspricht trivialem Kern und vollem Rang.", "同 ss22考试1 的思路：可逆保无关；若所有无关组像仍无关，则列向量像无关，矩阵满秩。"),
    ("ss22考试2", 5, "抽象向量空间、函数空间与对偶", "Untersuchen Sie Dualbasis und lineare Funktionale auf endlichdimensionalen Räumen.", "研究有限维空间上线性泛函与对偶基。", "Basiswerte bestimmen die Funktionale.", "用 $g_i(u_j)=\delta_{ij}$ 构造对偶基；代入基向量证明线性无关和张成性。"),
    # ss24
    ("ss24考试", 1, "正交投影、最小二乘与内积", "Berechnen Sie eine orthogonale Projektion bzw. Least-Squares-Zerlegung.", "计算正交投影或最小二乘分解。", "Fehlervektor orthogonal zum Unterraum.", "设投影在子空间基的线性组合中，误差向量与所有基向量内积为 0，形成法方程。"),
    ("ss24考试", 2, "图、邻接矩阵与矩阵变换", "Bestimmen Sie lineare Transformation, Kern, Spaltenraum, Rang und Determinante aus geometrischen Daten.", "从几何数据确定矩阵、核、列空间、秩和行列式。", "Geometrisches Bild der Basisvektoren liefert die Spalten.", "读出标准基像作为列；列空间由这些列张成；列相关时 $\det=0$，核由 $Ax=0$ 求。"),
    ("ss24考试", 3, "特征值、特征空间与对角化", "Lösen Sie kurze Beweis- und Gegenbeispielaufgaben zu Eigenwerten, Projektionen und Unterräumen.", "解决关于特征值、投影、子空间的证明/反例题。", "Regeln wie $A+cI$ und Unterraumkriterium verwenden.", "逐句判断：特征值用 $Av=\lambda v$ 推；投影用正交分解；子空间用零元、加法、数乘封闭。"),
    ("ss24考试", 4, "矩阵可逆、行列式与秩", "Beweisen Sie eine strukturelle Aussage zur Invertierbarkeit und linearer Unabhängigkeit.", "证明关于可逆性和线性无关保持的结构命题。", "Kernargument: nichtinvertierbar liefert nichttrivialen Kernvektor.", "若不可逆，存在 $x\ne0$ 使 $Ax=0$，单个向量 $x$ 无关但像为 0，不无关；这给逆否命题。"),
    ("ss24考试", 5, "抽象向量空间、函数空间与对偶", "Seien $V_1,\\ldots,V_n$ Vektorräume: untersuchen Sie Produktraum, Dimension und Basis.", "对多个向量空间的直积研究向量空间结构、维数和基。", "Operationen komponentenweise definieren.", "直积中加法和数乘逐分量进行；若 $B_i$ 是 $V_i$ 的基，则把 $B_i$ 放入第 $i$ 个分量得到直积基，维数相加。"),
    # ss25
    ("ss25", 1, "正交投影、最小二乘与内积", "Finde $\\hat v\\in W$ und $z\\in W^\\perp$ mit $v=\\hat v+z$.", "给定 $W=\\operatorname{span}(u_1,u_2)$ 和 $v$，求 $v$ 在 $W$ 上的投影及垂直误差。", "Löse $\\langle v-\\hat v,u_i\\rangle=0$.", "设 $\hat v=a u_1+b u_2$。令 $z=v-\hat v$，要求 $z\\perp u_1,u_2$，得到两个方程求 $a,b$。"),
    ("ss25", 2, "图、邻接矩阵与矩阵变换", "Aus einem Graphen einer Transformation $x\\mapsto Ax$: bestimme $\\ker A$, $\\operatorname{col}A$, Rang, Determinante und $A$.", "由线性变换图像确定核、列空间、秩、行列式和矩阵。", "Die Bilder von $e_1,e_2,e_3$ sind die Spalten.", "图上读出基向量和点 $P_3$ 的像，确定各列；列的张成是列空间，列相关给核和行列式信息。"),
    ("ss25", 3, "特征值、特征空间与对角化", "Kurzaufgaben zu symmetrischen Matrizen, Eigenwertverschiebung, diagonalisierbaren Matrizen und Wahr/Falsch.", "关于对称矩阵基、特征值平移、可对角化矩阵和真假题的综合题。", "Nutze Standardbasis, $A+cI$, Diagonalisierung und Gegenbeispiele.", "先列对称矩阵空间基；再证明 $A+cI$ 的特征向量不变、特征值加 $c$。若 $U=PDP^{-1}$ 且 $D^2=I$，则 $U^{-1}=U$。真假题写证明或反例。"),
    ("ss25", 4, "矩阵可逆、行列式与秩", "Beweise: $A$ ist invertierbar genau dann, wenn $A$ jede linear unabhängige Familie linear unabhängig erhält.", "证明矩阵可逆等价于保持任意线性无关向量组的线性无关性。", "Links nach rechts mit $A^{-1}$; rechts nach links mit Standardbasis.", "可逆时把 $\sum c_iAv_i=0$ 左乘 $A^{-1}$。反过来，标准基线性无关，像也线性无关，所以 $A$ 的列满秩，$A$ 可逆。"),
    ("ss25", 5, "抽象向量空间、函数空间与对偶", "Dualraum: gib Standard-Dualbasis an, beweise Unabhängigkeit und Darstellungsformel.", "对偶空间题：给标准对偶基，证明线性无关和表示公式。", "Auswertung auf Basisvektoren isoliert Koeffizienten.", "对 $\mathbb R^n$，$g_i(x)=x_i$。若 $\sum c_ig_i=0$，代入 $e_j$ 得 $c_j=0$。任意 $f$ 与 $\sum f(u_i)g_i$ 在基上取值相同，所以相等。"),
]


def md_escape(text: str) -> str:
    return text.replace("\n", " ").strip()


def grouped_items():
    groups = defaultdict(list)
    for item in ITEMS:
        groups[item[2]].append(item)
    return groups


def main():
    actual_by_exam = Counter(item[0] for item in ITEMS)
    total_expected = sum(EXPECTED.values())
    total_actual = len(ITEMS)
    if total_expected != total_actual:
        raise SystemExit(f"题目总数不一致: expected {total_expected}, actual {total_actual}")
    for exam, expected in EXPECTED.items():
        actual = actual_by_exam[exam]
        if expected != actual:
            raise SystemExit(f"{exam} 题目数不一致: expected {expected}, actual {actual}")

    groups = grouped_items()
    topic_counts = Counter(item[2] for item in ITEMS)

    lines = []
    lines.append("# 历史考试考点汇总")
    lines.append("")
    lines.append("> 汇总范围：`历史考试` 根目录中的历年考试 PDF 与 Markdown 主文件；`源文件` 目录视为来源/重复件，不重复计数。计数单位为每份试卷的主 `Aufgabe`，子问归入同一主题。")
    lines.append("")
    lines.append("## 0. 来源与题目数量核对")
    lines.append("")
    lines.append("| 试卷文件 | 原卷主题数 | 汇总纳入题数 | 核对 |")
    lines.append("|---|---:|---:|---|")
    for exam in EXPECTED:
        actual = actual_by_exam[exam]
        ok = "一致" if actual == EXPECTED[exam] else "不一致"
        lines.append(f"| {exam} | {EXPECTED[exam]} | {actual} | {ok} |")
    lines.append(f"| **总计** | **{total_expected}** | **{total_actual}** | **一致** |")
    lines.append("")

    lines.append("## 1. 所涉及的公式")
    lines.append("")
    for topic, formulas in FORMULAS.items():
        if topic not in topic_counts:
            continue
        lines.append(f"### {topic}")
        lines.append("")
        lines.append("| 名称 | 公式 | 应用场景 |")
        lines.append("|---|---|---|")
        for name, formula, scene in formulas:
            lines.append(f"| {name} | {formula} | {scene} |")
        lines.append("")

    lines.append("## 2. 德文考题（按考点组织）")
    lines.append("")
    for topic, rows in groups.items():
        lines.append(f"### {topic}")
        lines.append("")
        for exam, no, _, de, *_ in rows:
            lines.append(f"- **{exam} Aufgabe {no}**：{md_escape(de)}")
        lines.append("")

    lines.append("## 3. 中文考题（按考点组织）")
    lines.append("")
    for topic, rows in groups.items():
        lines.append(f"### {topic}")
        lines.append("")
        for exam, no, _, _, zh, *_ in rows:
            lines.append(f"- **{exam} 第 {no} 题**：{md_escape(zh)}")
        lines.append("")

    lines.append("## 4. 德文简答")
    lines.append("")
    for topic, rows in groups.items():
        lines.append(f"### {topic}")
        lines.append("")
        for exam, no, _, _, _, de_ans, _ in rows:
            lines.append(f"- **{exam} Aufgabe {no}**：{md_escape(de_ans)}")
        lines.append("")

    lines.append("## 5. 中文解答")
    lines.append("")
    for topic, rows in groups.items():
        lines.append(f"### {topic}")
        lines.append("")
        for exam, no, _, _, _, _, zh_ans in rows:
            lines.append(f"- **{exam} 第 {no} 题**：{md_escape(zh_ans)}")
        lines.append("")

    lines.append("## 6. 知识点考察次数统计")
    lines.append("")
    lines.append("| 考点 | 考察题数 | 占比 | 涉及题目 |")
    lines.append("|---|---:|---:|---|")
    for topic, count in topic_counts.most_common():
        refs = "；".join(f"{exam}-{no}" for exam, no, t, *_ in ITEMS if t == topic)
        pct = f"{count / total_actual:.1%}"
        lines.append(f"| {topic} | {count} | {pct} | {refs} |")
    lines.append(f"| **总计** | **{total_actual}** | **100.0%** | 与来源核对表总题数一致 |")
    lines.append("")
    lines.append("### 核对结论")
    lines.append("")
    lines.append(f"- 原卷主任务总数：{total_expected}。")
    lines.append(f"- 本汇总纳入主任务总数：{total_actual}。")
    lines.append("- 逐卷题数全部一致，因此本文件按主 Aufgabe 计数没有遗漏。")
    lines.append("- 一题含多个子问时，统计归入主考点；子问中的次要考点已在题目描述和解题思路中说明。")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} with {total_actual} items.")


if __name__ == "__main__":
    main()
