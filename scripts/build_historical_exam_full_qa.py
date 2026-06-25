import re
from collections import Counter, defaultdict
from pathlib import Path

from build_historical_exam_summary import EXPECTED, FORMULAS, ITEMS


OUT = Path("历史考试") / "历年考试考点汇总-完整题解.md"
TEXT_DIR = Path("历史考试") / "文本抽取"


CHEATSHEET = {
    "线性方程组、秩、核与像": [
        ("高斯消元", "$Ax=b\\ \\Longleftrightarrow\\ (A\\mid b)$ 做行变换", "判断有解、写通解、求解空间基。"),
        ("齐次方程解空间", "$\\ker A=\\{x\\mid Ax=0\\}$", "求核、零空间、齐次解空间。"),
        ("非齐次方程可解", "$Ax=b$ 可解 $\\Longleftrightarrow b\\in\\operatorname{Bild}(A)$", "判断右端向量是否在列空间。"),
        ("秩-零化度公式", "$\\dim\\ker A+\\operatorname{rang}A=n$", "$A\\in K^{m\\times n}$，用秩求核维数。"),
        ("像空间维数", "$\\dim\\operatorname{Bild}(f)=\\operatorname{rang}(M_f)$", "线性映射像空间、列空间。"),
        ("秩不等式", "$\\operatorname{rang}(AB)\\le\\min(\\operatorname{rang}A,\\operatorname{rang}B)$", "判断矩阵乘积不可能可逆。"),
        ("非零子式判秩", "若某个 $k\\times k$ 子式 $\\det M_{I,J}\\ne0$，则 $\\operatorname{rang}M\\ge k$", "不用完整化简矩阵时，用一个非零子式给秩下界。"),
        ("同解行变换", "$A\\sim R\\Rightarrow Ax=0$ 与 $Rx=0$ 解集相同", "相同行阶梯形、齐次方程解集判断。"),
    ],
    "矩阵可逆、行列式与转置": [
        ("可逆等价条件", "$A^{-1}$ 存在 $\\Longleftrightarrow\\det A\\ne0\\Longleftrightarrow\\operatorname{rang}A=n\\Longleftrightarrow\\ker A=\\{0\\}$", "判断正则矩阵、满秩、单射满射。"),
        ("逆矩阵增广法", "$(A\\mid I)\\sim(I\\mid A^{-1})$", "具体计算逆矩阵。"),
        ("逆矩阵乘积", "$(AB)^{-1}=B^{-1}A^{-1}$", "证明乘积可逆、相似变换。"),
        ("转置乘积", "$(AB)^T=B^TA^T$", "处理 $A^TA$、相似转置题。"),
        ("行列式乘法", "$\\det(AB)=\\det A\\det B$", "证明可逆性、幂等矩阵、正交矩阵。"),
        ("转置行列式", "$\\det(A^T)=\\det A$", "处理 $A^TA$、正交矩阵。"),
        ("三角矩阵行列式", "$A$ 三角 $\\Rightarrow\\det A=$ 对角元乘积", "快速求特征多项式、参数行列式。"),
        ("块矩阵 Schur 补", "$\\det\\begin{pmatrix}I&a\\\\ u^T&0\\end{pmatrix}=-u^Ta$", "处理带单位块的一列一行参数矩阵。"),
        ("正交矩阵", "$Q^TQ=I\\Longleftrightarrow Q^{-1}=Q^T$, 且 $\\lvert\\det Q\\rvert=1$", "正交矩阵证明题。"),
        ("正交矩阵特征值", "$Qx=\\lambda x,\\ Q^TQ=I\\Rightarrow \\lvert\\lambda\\rvert=1$", "判断正交矩阵的特征值范围。"),
        ("反对称矩阵", "$A^T=-A$", "奇数维时常推出 $\\det A=0$；且 $x^TAx=0$。"),
        ("幂等矩阵", "$A^2=A\\Rightarrow(\\det A)^2=\\det A\\Rightarrow\\det A\\in\\{0,1\\}$", "投影/幂等矩阵判断。"),
        ("幂零矩阵", "$A^2=0\\Rightarrow(I-A)(I+A)=I$", "证明 $I-A$ 可逆。"),
    ],
    "子空间、基、维数与仿射空间": [
        ("线性无关", "$\\sum_i\\lambda_i v_i=0\\Rightarrow\\lambda_1=\\cdots=\\lambda_k=0$", "证明向量组是基。"),
        ("生成空间", "$\\operatorname{span}(v_1,\\ldots,v_k)=\\{\\sum_i\\lambda_i v_i\\}$", "写子空间、和空间、列空间。"),
        ("基", "基 $=$ 线性无关 $+$ 张成空间", "求基、补基。"),
        ("添向量判无关", "$M$ 无关且 $v\\notin\\operatorname{span}(M)\\Rightarrow M\\cup\\{v\\}$ 无关", "证明新增向量不会破坏线性无关。"),
        ("维数公式", "$\\dim(U+V)=\\dim U+\\dim V-\\dim(U\\cap V)$", "求和空间或交空间维数。"),
        ("仿射包", "$\\operatorname{aff}(p_0,\\ldots,p_k)=p_0+\\operatorname{span}(p_1-p_0,\\ldots,p_k-p_0)$", "仿射空间维数和平行仿射空间。"),
        ("平行仿射空间", "$F=q+U$", "过点 $q$ 且平行于方向空间 $U$。"),
    ],
    "群、同构与相似": [
        ("子群判据", "$e\\in G,\\ a,b\\in G\\Rightarrow ab\\in G,\\ a\\in G\\Rightarrow a^{-1}\\in G$", "证明矩阵集合成群。"),
        ("群同态", "$\\varphi(xy)=\\varphi(x)\\varphi(y)$", "证明参数群到矩阵群的结构保持。"),
        ("群同构", "同态 $+$ 单射 $+$ 满射", "证明两个群本质一样。"),
        ("相似", "$B=S^{-1}AS$", "对角化、相似不变量、矩阵方程。"),
        ("相似保持幂", "$B^k=S^{-1}A^kS$", "证明幂关系、等价关系。"),
        ("相似保持逆", "$A$ 可逆且 $B=S^{-1}AS\\Rightarrow B^{-1}=S^{-1}A^{-1}S$", "相似关系下的逆矩阵。"),
        ("相似保持矩阵多项式", "$p(B)=S^{-1}p(A)S$", "若 $p(A)=0$，则 $p(B)=0$。"),
    ],
    "矩阵幂、归纳与矩阵多项式": [
        ("完全归纳法", "$P(1)$ 成立且 $P(n)\\Rightarrow P(n+1)$，则 $P(n)$ 对所有 $n\\in\\mathbb N$ 成立", "证明矩阵幂闭式。"),
        ("矩阵正幂", "$A^{n+1}=A^nA$", "归纳步核心。"),
        ("负幂", "$A^{-n}=(A^n)^{-1}$", "整数幂公式。"),
        ("幂的乘法", "$A^mA^n=A^{m+n}$", "由单个矩阵生成的群。"),
        ("矩阵多项式求逆", "$A^2=3A+4I\\Rightarrow A(A-3I)=4I\\Rightarrow A^{-1}=\\frac14(A-3I)$", "矩阵方程推出可逆和逆。"),
        ("标量矩阵代入", "$(\\gamma I)^2=3\\gamma I+4I\\Longleftrightarrow\\gamma^2-3\\gamma-4=0$", "矩阵方程里的标量解。"),
    ],
    "线性映射与矩阵表示": [
        ("线性性", "$f(\\lambda x+\\mu y)=\\lambda f(x)+\\mu f(y)$", "证明映射线性。"),
        ("标准基矩阵", "$M_f=(f(e_1),\\ldots,f(e_n))$", "由映射写矩阵。"),
        ("核", "$\\ker f=\\{x\\mid f(x)=0\\}$", "判断单射、求核基。"),
        ("像", "$\\operatorname{Bild}f=\\{f(x)\\mid x\\in V\\}$", "求列空间、判断满射。"),
        ("同维线性映射可逆", "$f$ 可逆 $\\Longleftrightarrow\\ker f=\\{0\\}\\Longleftrightarrow\\operatorname{rang}M=n$", "判断线性映射是否双射。"),
        ("可逆映射保持无关", "$A$ 可逆且 $v_i$ 无关 $\\Rightarrow Av_i$ 无关", "证明可逆矩阵等价于保持所有线性无关组。"),
        ("秩一扰动矩阵", "$f(x)=x+(a^Tx)b\\Rightarrow M=I+ba^T$", "处理 $I+ba^T$ 型题。"),
        ("秩一扰动迹", "$\\operatorname{spur}(I+ba^T)=n+a^Tb$", "求迹。"),
        ("秩一扰动可逆", "$I+ba^T$ 可逆 $\\Longleftrightarrow 1+a^Tb\\ne0$", "判断 $f(x)=x+(a^Tx)b$ 可逆。"),
    ],
    "特征值、特征空间与对角化": [
        ("特征方程", "$\\chi_A(\\lambda)=\\det(A-\\lambda I)$", "求特征值。"),
        ("特征空间", "$E_\\lambda=\\ker(A-\\lambda I)$", "求特征向量、几何重数。"),
        ("迹与特征值", "$\\operatorname{spur}(A)=\\lambda_1+\\cdots+\\lambda_n$（按代数重数）", "用迹补特征值。"),
        ("行列式与特征值", "$\\det A=\\lambda_1\\cdots\\lambda_n$（按代数重数）", "判断是否有零特征值、可逆性。"),
        ("代数重数", "$\\lambda$ 在 $\\chi_A$ 中的重数", "对角化判据。"),
        ("几何重数", "$\\dim E_\\lambda$", "对角化判据。"),
        ("对角化判据", "$A$ 可对角化 $\\Longleftrightarrow\\sum_\\lambda\\dim E_\\lambda=n$", "判断是否能写成 $PDP^{-1}$。"),
        ("特征值平移", "$Av=\\lambda v\\Rightarrow(A+cI)v=(\\lambda+c)v$", "求 $A+cI$ 的特征值。"),
        ("逆矩阵特征值", "$Av=\\lambda v,\\lambda\\ne0\\Rightarrow A^{-1}v=\\lambda^{-1}v$", "由 $A+cI$ 的特征值求 $(A+cI)^{-1}$ 的特征值。"),
        ("不同特征空间相交", "$\\lambda_1\\ne\\lambda_2\\Rightarrow E_{\\lambda_1}\\cap E_{\\lambda_2}=\\{0\\}$", "证明不同特征值对应方向不会重叠。"),
        ("秩一矩阵谱", "$A=uu^T\\Rightarrow Au=(u^Tu)u,\\ x\\perp u\\Rightarrow Ax=0$", "处理 $A=(e_1-e_n)(e_1-e_n)^T$ 这类题。"),
        ("对称矩阵", "实对称矩阵可正交对角化", "主轴变换、二次型。"),
        ("只有 $\\pm1$ 的可对角化矩阵", "$U=PDP^{-1},\\ D^2=I\\Rightarrow U^2=I\\Rightarrow U^{-1}=U$", "证明 involution 类型命题。"),
    ],
    "正交投影、最小二乘与内积": [
        ("正交分解", "$v=\\hat v+z,\\ \\hat v\\in W,\\ z\\in W^\\perp$", "投影题标准形式。"),
        ("投影条件", "$\\langle v-\\hat v,u_i\\rangle=0$", "求投影系数。"),
        ("法方程", "$A^TAx=A^Tb$", "最小二乘解。"),
        ("正交补", "$W^\\perp=\\{z\\mid\\langle z,w\\rangle=0\\ \\forall w\\in W\\}$", "求误差方向。"),
        ("基本子空间正交关系", "$\\operatorname{col}(A)^\\perp=\\ker(A^T),\\quad\\operatorname{col}(A^T)^\\perp=\\ker(A)$", "从图像的列空间方向反推核方向。"),
        ("投影不动点", "$v\\in W\\Rightarrow\\operatorname{proj}_W(v)=v$", "判断投影真假题。"),
        ("二次型", "$q(x)=x^TAx$", "主轴变换、正定性、极值方向。"),
        ("正定/半正定/不定", "$x^TAx>0,\\ge0$；若可取正也可取负则不定", "真假题里判断正定、半正定和不定。"),
        ("加权内积", "$\\langle x,y\\rangle=w_1x_1y_1+w_2x_2y_2$ 是内积 $\\Longleftrightarrow w_1,w_2>0$", "判断加权内积是否正定。"),
    ],
    "图、邻接矩阵与几何变换": [
        ("矩阵列", "$Ae_i=$ 第 $i$ 列", "从图像读矩阵。"),
        ("列空间", "$\\operatorname{col}(A)=\\operatorname{span}(Ae_1,\\ldots,Ae_n)$", "从图像读像空间。"),
        ("核", "$\\ker A=\\{x\\mid Ax=0\\}$", "从压扁方向读核。"),
        ("行列式几何意义", "$\\det A=$ 有向体积缩放因子", "图像降维时 $\\det A=0$。"),
        ("邻接矩阵路径计数", "$(A^k)_{ij}=$ 从 $i$ 到 $j$ 长度为 $k$ 的路径数", "证明 $A^k=0$ 或数路径。"),
    ],
    "抽象向量空间、函数空间与对偶": [
        ("子空间判据", "$0\\in U,\\ u,v\\in U\\Rightarrow u+v\\in U,\\ \\alpha u\\in U$", "判断函数集合/矩阵集合是否子空间。"),
        ("函数空间运算", "$(f+g)(x)=f(x)+g(x),\\ (\\alpha f)(x)=\\alpha f(x)$", "证明函数集合成子空间。"),
        ("直积空间运算", "$(v_1,\\ldots,v_n)+(w_1,\\ldots,w_n)=(v_1+w_1,\\ldots,v_n+w_n)$", "证明 $V_1\\times\\cdots\\times V_n$ 是向量空间。"),
        ("直积空间数乘", "$c(v_1,\\ldots,v_n)=(cv_1,\\ldots,cv_n)$", "直积空间的数乘和子空间证明。"),
        ("对偶空间", "$V^*=\\{f:V\\to\\mathbb R\\mid f\\text{ linear}\\}$", "线性泛函题。"),
        ("对偶基", "$g_i(u_j)=\\delta_{ij}$", "构造和证明对偶基。"),
        ("对偶展开", "$f=\\sum_{i=1}^n f(u_i)g_i$", "证明任意线性泛函的表示。"),
        ("直积空间维数", "$\\dim(V_1\\times\\cdots\\times V_n)=\\sum_i\\dim V_i$", "产品向量空间题。"),
    ],
}


MANUAL_OVERRIDES = {
    ("ss01", 1): {
        "problem": """Bestimmen Sie die Inverse von

$$
A=
\\begin{pmatrix}
1&1&1&0\\\\
1&1&-1&0\\\\
1&-1&0&1\\\\
1&-1&0&-1
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}
$$

und machen Sie die Probe.""",
        "zh_problem": """求下列矩阵的逆矩阵（inverse Matrix），并做乘法验算：

$$
A=
\\begin{pmatrix}
1&1&1&0\\\\
1&1&-1&0\\\\
1&-1&0&1\\\\
1&-1&0&-1
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}.
$$""",
        "solution": """Lösung:

Wir bestimmen die Inverse mit Gauß-Jordan. Dazu formen wir die erweiterte Matrix $(A\\mid I_4)$ um:

$$
\\left(
\\begin{array}{rrrr|rrrr}
1&1&1&0&1&0&0&0\\\\
1&1&-1&0&0&1&0&0\\\\
1&-1&0&1&0&0&1&0\\\\
1&-1&0&-1&0&0&0&1
\\end{array}
\\right)
\\sim
\\left(
\\begin{array}{rrrr|rrrr}
1&0&0&0&\\frac14&\\frac14&\\frac14&\\frac14\\\\
0&1&0&0&\\frac14&\\frac14&-\\frac14&-\\frac14\\\\
0&0&1&0&\\frac12&-\\frac12&0&0\\\\
0&0&0&1&0&0&\\frac12&-\\frac12
\\end{array}
\\right).
$$

Also ist

$$
A^{-1}=
\\begin{pmatrix}
\\frac14&\\frac14&\\frac14&\\frac14\\\\
\\frac14&\\frac14&-\\frac14&-\\frac14\\\\
\\frac12&-\\frac12&0&0\\\\
0&0&\\frac12&-\\frac12
\\end{pmatrix}.
$$

Probe:

$$
A A^{-1}=
\\begin{pmatrix}
1&1&1&0\\\\
1&1&-1&0\\\\
1&-1&0&1\\\\
1&-1&0&-1
\\end{pmatrix}
\\begin{pmatrix}
\\frac14&\\frac14&\\frac14&\\frac14\\\\
\\frac14&\\frac14&-\\frac14&-\\frac14\\\\
\\frac12&-\\frac12&0&0\\\\
0&0&\\frac12&-\\frac12
\\end{pmatrix}
=
\\begin{pmatrix}
1&0&0&0\\\\
0&1&0&0\\\\
0&0&1&0\\\\
0&0&0&1
\\end{pmatrix}.
$$

Damit ist die berechnete Matrix tatsächlich $A^{-1}$.""",
        "zh_solution": """核心考点：**逆矩阵、Gauss-Jordan 消元、乘法验算**。

这题不能只写“用 $(A\\mid I)$ 消元”，必须把结果算出来。做法是把 $A$ 和单位矩阵拼成增广矩阵：

$$
(A\\mid I_4).
$$

然后对整块矩阵做同样的行变换，把左边的 $A$ 化成 $I_4$。右边同步变换出来的矩阵就是 $A^{-1}$：

$$
\\left(
\\begin{array}{rrrr|rrrr}
1&1&1&0&1&0&0&0\\\\
1&1&-1&0&0&1&0&0\\\\
1&-1&0&1&0&0&1&0\\\\
1&-1&0&-1&0&0&0&1
\\end{array}
\\right)
\\sim
\\left(
\\begin{array}{rrrr|rrrr}
1&0&0&0&\\frac14&\\frac14&\\frac14&\\frac14\\\\
0&1&0&0&\\frac14&\\frac14&-\\frac14&-\\frac14\\\\
0&0&1&0&\\frac12&-\\frac12&0&0\\\\
0&0&0&1&0&0&\\frac12&-\\frac12
\\end{array}
\\right).
$$

所以

$$
A^{-1}=
\\begin{pmatrix}
\\frac14&\\frac14&\\frac14&\\frac14\\\\
\\frac14&\\frac14&-\\frac14&-\\frac14\\\\
\\frac12&-\\frac12&0&0\\\\
0&0&\\frac12&-\\frac12
\\end{pmatrix}.
$$

解题思路是：逆矩阵不是靠猜，而是把“解 $AX=I$”拆成四个右端向量一起做。左边被消成单位矩阵时，右边正好记录了这四个解向量。

最后必须验算。把原矩阵乘回去：

$$
A A^{-1}=
\\begin{pmatrix}
1&0&0&0\\\\
0&1&0&0\\\\
0&0&1&0\\\\
0&0&0&1
\\end{pmatrix}=I_4.
$$

因此答案正确。""",
    },
    ("ss01", 2): {
        "problem": """Bestimmen Sie, abhängig von $\\lambda\\in\\mathbb R$, alle Lösungen des Gleichungssystems $Ax=b$, bei

$$
A=
\\begin{pmatrix}
1&2&4&3\\\\
1&2&2&-1\\\\
0&0&1&2
\\end{pmatrix}
\\in\\mathbb R^{3\\times4},
\\qquad
b=
\\begin{pmatrix}
\\lambda\\\\
-1\\\\
1
\\end{pmatrix}
\\in\\mathbb R^3.
$$""",
        "zh_problem": """按参数 $\\lambda\\in\\mathbb R$ 讨论线性方程组 $Ax=b$ 的所有解，其中

$$
A=
\\begin{pmatrix}
1&2&4&3\\\\
1&2&2&-1\\\\
0&0&1&2
\\end{pmatrix},
\\qquad
b=
\\begin{pmatrix}
\\lambda\\\\
-1\\\\
1
\\end{pmatrix}.
$$""",
        "solution": """Lösung:

Die erweiterte Matrix lautet

$$
\\left(
\\begin{array}{rrrr|r}
1&2&4&3&\\lambda\\\\
1&2&2&-1&-1\\\\
0&0&1&2&1
\\end{array}
\\right).
$$

Wir subtrahieren die zweite Zeile von der ersten:

$$
\\left(
\\begin{array}{rrrr|r}
0&0&2&4&\\lambda+1\\\\
1&2&2&-1&-1\\\\
0&0&1&2&1
\\end{array}
\\right).
$$

Die erste Zeile links ist das Doppelte der dritten Zeile links. Daher muss rechts ebenfalls gelten

$$
\\lambda+1=2.
$$

Also ist das System genau für

$$
\\lambda=1
$$

lösbar. Für $\\lambda\\ne1$ entsteht eine Widerspruchszeile und es gibt keine Lösung.

Für $\\lambda=1$ erhalten wir aus der dritten Zeile

$$
x_3+2x_4=1,
$$

also $x_3=1-2t$ mit $t=x_4$. Aus der zweiten Zeile folgt

$$
x_1+2x_2+2x_3-x_4=-1.
$$

Setzen wir $x_2=s$ und $x_4=t$, dann

$$
x_1=-1-2s-2(1-2t)+t=-3-2s+5t.
$$

Damit ist für $\\lambda=1$

$$
\\mathcal L(A,b)=
\\left\\{
\\begin{pmatrix}
-3\\\\0\\\\1\\\\0
\\end{pmatrix}
s
\\begin{pmatrix}
-2\\\\1\\\\0\\\\0
\\end{pmatrix}
t
\\begin{pmatrix}
5\\\\0\\\\-2\\\\1
\\end{pmatrix}
\\;\\middle|\\;s,t\\in\\mathbb R
\\right\\}.
$$""",
        "zh_solution": """核心考点：**参数线性方程组、相容条件、自由变量通解**。

先写增广矩阵：

$$
\\left(
\\begin{array}{rrrr|r}
1&2&4&3&\\lambda\\\\
1&2&2&-1&-1\\\\
0&0&1&2&1
\\end{array}
\\right).
$$

第一行减第二行，得到

$$
0x_1+0x_2+2x_3+4x_4=\\lambda+1.
$$

第三行是

$$
x_3+2x_4=1.
$$

注意左边第一条正好是第三条的 $2$ 倍，所以右边也必须是 $2$ 倍：

$$
\\lambda+1=2.
$$

因此

$$
\\lambda=1.
$$

如果 $\\lambda\\ne1$，左边关系一致、右边不一致，就会出现矛盾行，所以无解。

当 $\\lambda=1$ 时，令自由变量

$$
x_2=s,\qquad x_4=t.
$$

由第三行

$$
x_3+2x_4=1
$$

得

$$
x_3=1-2t.
$$

由第二行

$$
x_1+2x_2+2x_3-x_4=-1
$$

代入 $x_2=s,\ x_3=1-2t,\ x_4=t$：

$$
x_1+2s+2(1-2t)-t=-1,
$$

所以

$$
x_1=-3-2s+5t.
$$

最终通解为

$$
x=
\\begin{pmatrix}
-3\\\\0\\\\1\\\\0
\\end{pmatrix}
s
\\begin{pmatrix}
-2\\\\1\\\\0\\\\0
\\end{pmatrix}
t
\\begin{pmatrix}
5\\\\0\\\\-2\\\\1
\\end{pmatrix},
\\qquad s,t\\in\\mathbb R.
$$

解题思路：参数题先不要急着写通解，先找“左边相同或成倍数、右边必须同步”的相容条件。这里参数只决定有没有解；一旦 $\\lambda=1$，再按普通线性方程组写自由变量。""",
    },
    ("ss01", 3): {
        "problem": """Klären Sie, ob das Produkt $A\\cdot B$ der Matrizen

$$
A=
\\begin{pmatrix}
1&-2&5\\\\
3&-1&-1\\\\
0&4&0\\\\
17&1&0\\\\
7&9&-5
\\end{pmatrix}
\\in\\mathbb R^{5\\times3},
\\qquad
B=
\\begin{pmatrix}
1&3&7&15&9\\\\
2&6&8&-1&0\\\\
3&4&9&1&-3
\\end{pmatrix}
\\in\\mathbb R^{3\\times5}
$$

regulär ist.

Hinweis: Mit einem abstrakten Argument ersparen Sie sich jeglichen Rechenaufwand.""",
        "zh_problem": """判断下面两个矩阵的乘积 $AB$ 是否为正则矩阵（reguläre Matrix，即可逆矩阵），并说明理由：

$$
A=
\\begin{pmatrix}
1&-2&5\\\\
3&-1&-1\\\\
0&4&0\\\\
17&1&0\\\\
7&9&-5
\\end{pmatrix}
\\in\\mathbb R^{5\\times3},
\\qquad
B=
\\begin{pmatrix}
1&3&7&15&9\\\\
2&6&8&-1&0\\\\
3&4&9&1&-3
\\end{pmatrix}
\\in\\mathbb R^{3\\times5}.
$$

提示：用抽象的秩论证即可，不需要真的计算 $AB$。""",
        "solution": """Lösung:

Das Produkt $AB$ ist eine $5\\times5$-Matrix. Damit $AB$ regulär sein könnte, müsste

$$
\\operatorname{rang}(AB)=5
$$

gelten. Für Produkte gilt aber

$$
\\operatorname{rang}(AB)\\le \\min(\\operatorname{rang}(A),\\operatorname{rang}(B)).
$$

Da $A\\in\\mathbb R^{5\\times3}$ höchstens Rang $3$ haben kann und $B\\in\\mathbb R^{3\\times5}$ ebenfalls höchstens Rang $3$ hat, folgt

$$
\\operatorname{rang}(AB)\le3.
$$

Also kann $AB$ als $5\\times5$-Matrix keinen vollen Rang haben. Daher ist $AB$ nicht regulär.""",
        "zh_solution": """核心考点：**矩阵乘积的秩不等式、可逆矩阵必须满秩**。

先看尺寸：

$$
A\\in\\mathbb R^{5\\times3},\qquad B\\in\\mathbb R^{3\\times5},
$$

所以

$$
AB\\in\\mathbb R^{5\\times5}.
$$

如果 $AB$ 可逆，它必须是满秩矩阵：

$$
\\operatorname{rang}(AB)=5.
$$

但是矩阵乘积的秩满足

$$
\\operatorname{rang}(AB)\\le
\\min\\bigl(\\operatorname{rang}(A),\\operatorname{rang}(B)\\bigr).
$$

由于 $A$ 只有 $3$ 列，所以

$$
\\operatorname{rang}(A)\le3.
$$

由于 $B$ 只有 $3$ 行，所以

$$
\\operatorname{rang}(B)\le3.
$$

因此

$$
\\operatorname{rang}(AB)\le3<5.
$$

结论：

$$
AB\\text{ 不可逆。}
$$

解题思路：这题故意给大矩阵，是想诱导你硬乘。真正考点是“瘦矩阵夹在中间会限制秩”。$5\\times3$ 再乘 $3\\times5$，中间维度只有 $3$，最终 $5\\times5$ 的秩最多也只能是 $3$，不可能满秩。""",
    },
    ("ss01", 4): {
        "problem": """Stellen Sie fest, wie viele reguläre Matrizen es in $\\mathbb F_2^{2\\times2}$ gibt, und begründen Sie Ihre Aussage.

Hinweis: Es gibt eine Lösung, bei der man nicht alle möglichen Matrizen hinschreiben muss.""",
        "zh_problem": """判断有限域 $\\mathbb F_2$ 上有多少个 $2\\times2$ 可逆矩阵（reguläre Matrizen），并说明理由。

提示：不需要把所有矩阵逐个列出来。""",
        "solution": """Lösung:

Eine $2\\times2$-Matrix über $\\mathbb F_2$ ist genau dann regulär, wenn ihre beiden Spalten linear unabhängig sind.

In $\\mathbb F_2^2$ gibt es insgesamt vier Vektoren:

$$
\\begin{pmatrix}0\\\\0\\end{pmatrix},
\\begin{pmatrix}1\\\\0\\end{pmatrix},
\\begin{pmatrix}0\\\\1\\end{pmatrix},
\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

Die erste Spalte einer regulären Matrix darf nicht der Nullvektor sein. Dafür gibt es also $3$ Möglichkeiten.

Die zweite Spalte darf nicht im Spann der ersten Spalte liegen. Über $\\mathbb F_2$ enthält der Spann eines von Null verschiedenen Vektors nur

$$
\\{0,v\\}.
$$

Von den vier Vektoren bleiben daher $2$ Möglichkeiten für die zweite Spalte.

Also gibt es

$$
3\\cdot2=6
$$

reguläre $2\\times2$-Matrizen über $\\mathbb F_2$.""",
        "zh_solution": """核心考点：**有限域、列向量线性无关、可逆矩阵计数**。

一个 $2\\times2$ 矩阵可逆，当且仅当它的两列线性无关。

在 $\\mathbb F_2^2$ 中只有四个向量：

$$
\\begin{pmatrix}0\\\\0\\end{pmatrix},
\\begin{pmatrix}1\\\\0\\end{pmatrix},
\\begin{pmatrix}0\\\\1\\end{pmatrix},
\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

第一列不能是零向量，否则列向量组一定线性相关。所以第一列有

$$
3
$$

种选择。

第一列选定为某个非零向量 $v$ 后，第二列不能落在 $\\operatorname{span}(v)$ 里。注意在 $\\mathbb F_2$ 上，非零向量 $v$ 的张成空间只有两个元素：

$$
\\operatorname{span}(v)=\\{0,v\\}.
$$

四个向量中排除 $0$ 和 $v$，第二列还剩

$$
2
$$

种选择。

所以可逆矩阵总数为

$$
3\\cdot2=6.
$$

解题思路：不要枚举 $2^4=16$ 个矩阵。可逆性等价于“列向量是一组基”。先选第一列非零，再选第二列不在第一列张成的直线上，这就是有限域版的列向量计数。""",
    },
    ("ss01", 5): {
        "problem": """Sei $A\\in\\mathbb R^{m\\times n}$, und sei der Einfachheit halber $A\\ne0$ und $\\operatorname{rang}(A)<m$. Zeigen Sie, dass es $l\\in\\mathbb N$ und $P\\in\\mathbb R^{l\\times m}$ gibt, so dass gilt:

$$
\\forall b\\in\\mathbb R^m:\\quad \\mathcal L(A,b)\\ne\\emptyset\\Longleftrightarrow Pb=0.
$$

Das heißt: Für alle $b\\in\\mathbb R^m$ ist das Gleichungssystem $Ax=b$ genau dann lösbar, wenn $Pb$ gleich Null ist.

Hinweis: Nehmen Sie zunächst an, dass $A$ Zeilenstufenform hat mit $r$ Stufen. Dann ist $P=(0,E_{m-r})$, mit $0\\in\\mathbb R^{(m-r)\\times r}$, eine geeignete Matrix. Warum?""",
        "zh_problem": """设 $A\\in\\mathbb R^{m\\times n}$，并且为简单起见假设 $A\\ne0$ 且 $\\operatorname{rang}(A)<m$。证明：存在 $l\\in\\mathbb N$ 和矩阵 $P\\in\\mathbb R^{l\\times m}$，使得

$$
\\forall b\\in\\mathbb R^m:\\quad \\mathcal L(A,b)\\ne\\emptyset\\Longleftrightarrow Pb=0.
$$

也就是说，对所有右端向量 $b\\in\\mathbb R^m$，线性方程组 $Ax=b$ 可解，当且仅当 $Pb=0$。

提示：先考虑 $A$ 已经是有 $r$ 个阶梯的行阶梯形矩阵（Zeilenstufenform）的情形。此时

$$
P=(0,E_{m-r}),\\qquad 0\\in\\mathbb R^{(m-r)\\times r},
$$

是合适的矩阵。为什么？""",
        "solution": """Lösung:

Sei zunächst $A$ bereits in Zeilenstufenform und sei $r=\\operatorname{rang}(A)$. Dann besitzt $A$ genau $r$ von Null verschiedene Zeilen; die letzten $m-r$ Zeilen sind Nullzeilen. Für das erweiterte System

$$
(A\\mid b)
$$

bedeutet Lösbarkeit genau: In den Nullzeilen von $A$ dürfen rechts keine von Null verschiedenen Einträge stehen. Sonst entstünde eine Widerspruchszeile der Form

$$
0=b_i\\quad\\text{mit }b_i\\ne0.
$$

Also ist $Ax=b$ genau dann lösbar, wenn die letzten $m-r$ Komponenten von $b$ verschwinden. Diese Komponenten werden durch

$$
P=(0,E_{m-r})\\in\\mathbb R^{(m-r)\\times m}
$$

ausgewählt. Damit gilt in diesem Spezialfall

$$
Ax=b\\text{ lösbar}\\Longleftrightarrow Pb=0.
$$

Für eine beliebige Matrix $A$ wählen wir eine invertierbare Matrix $S\\in GL(m,\\mathbb R)$, so dass

$$
R=SA
$$

in Zeilenstufenform ist. Solch ein $S$ existiert, weil elementare Zeilenumformungen durch Multiplikation mit invertierbaren Elementarmatrizen beschrieben werden. Für jedes $b\\in\\mathbb R^m$ gilt

$$
Ax=b\\Longleftrightarrow SAx=Sb\\Longleftrightarrow Rx=Sb.
$$

Auf $R$ wenden wir den Spezialfall an. Sei

$$
\\pi=(0,E_{m-r})\\in\\mathbb R^{(m-r)\\times m}.
$$

Dann ist $Rx=Sb$ genau dann lösbar, wenn

$$
\\pi Sb=0.
$$

Setzen wir

$$
l=m-r,\qquad P=\\pi S\\in\\mathbb R^{l\\times m},
$$

so erhalten wir für alle $b\\in\\mathbb R^m$

$$
\\mathcal L(A,b)\\ne\\emptyset\\Longleftrightarrow Pb=0.
$$

Damit ist die Behauptung bewiesen.""",
        "zh_solution": """核心考点：**线性方程组的可解性、行阶梯形、秩亏缺矩阵的相容条件**。

这题不是让你算一个具体 $P$，而是证明“总能造出一个 $P$”。思路是：矩阵 $A$ 的秩小于行数 $m$，所以行化简以后一定会出现零行；零行对应的右端项必须也是 $0$，否则方程组无解。矩阵 $P$ 的作用，就是专门把这些“必须为 $0$ 的右端条件”抽出来。

第一步，先看提示里的特殊情形。假设 $A$ 已经是行阶梯形，且

$$
r=\\operatorname{rang}(A)<m.
$$

那么 $A$ 有 $r$ 个非零行，下面 $m-r$ 行全是零行。增广矩阵是

$$
(A\\mid b).
$$

如果 $b$ 的最后 $m-r$ 个分量中有一个不为 $0$，增广矩阵里就会出现

$$
0=b_i\\quad(b_i\\ne0),
$$

这就是矛盾行，所以 $Ax=b$ 无解。

反过来，如果 $b$ 的最后 $m-r$ 个分量全为 $0$，那么零行不产生矛盾；上面的 $r$ 个主元方程可以通过自由变量取 $0$，再回代求主元变量来得到至少一个解。因此在阶梯形情形下：

$$
Ax=b\\text{ 可解}\\Longleftrightarrow b\\text{ 的最后 }m-r\\text{ 个分量全为 }0.
$$

这些最后的分量可以用矩阵

$$
P=(0,E_{m-r})\\in\\mathbb R^{(m-r)\\times m}
$$

抽出来，所以

$$
Ax=b\\text{ 可解}\\Longleftrightarrow Pb=0.
$$

第二步，处理一般矩阵 $A$。对 $A$ 做初等行变换，可以找到一个可逆矩阵（invertierbare Matrix）$S\\in GL(m,\\mathbb R)$，使

$$
R=SA
$$

是行阶梯形矩阵。这里 $S$ 可逆，是因为每一步初等行变换都对应一个可逆的初等矩阵。

原方程组与行变换后的方程组等价：

$$
Ax=b
\\Longleftrightarrow
SAx=Sb
\\Longleftrightarrow
Rx=Sb.
$$

现在 $R$ 是阶梯形，可以套用第一步。令

$$
\\pi=(0,E_{m-r})\\in\\mathbb R^{(m-r)\\times m}.
$$

则

$$
Rx=Sb\\text{ 可解}
\\Longleftrightarrow
\\pi Sb=0.
$$

最后把

$$
l=m-r,\qquad P=\pi S
$$

合并成一个矩阵，就得到

$$
\\mathcal L(A,b)\\ne\\emptyset
\\Longleftrightarrow
Pb=0.
$$

所以这样的 $l$ 和 $P$ 确实存在。直观地说，$P$ 就是“可解性检测器”：它不求解 $x$，只检查右端向量 $b$ 有没有违反零行条件。""",
    },
    ("ss00", 3): {
        "problem": """Seien

$$
A=
\\begin{pmatrix}
1&2&1\\\\
3&7&6\\\\
2&6&8
\\end{pmatrix},
\\qquad
b=
\\begin{pmatrix}
2\\\\
7\\\\
6
\\end{pmatrix}.
$$

Sei weiter

$$
f_A:\\mathbb R^3\\to\\mathbb R^3,\\qquad x\\mapsto Ax.
$$

(a) Zeige: $b\\in\\operatorname{Bild}(f_A)$.

(b) Bestimme die Dimension von $\\operatorname{Bild}(f_A)$ und $\\ker(f_A)$.""",
        "solution": """Lösung:

Ad (a): Zu zeigen ist, dass $Ax=b$ lösbar ist. Dazu bilden wir die erweiterte Koeffizientenmatrix und bringen sie in Zeilenstufenform:

$$
\\left(
\\begin{array}{ccc|c}
1&2&1&2\\\\
3&7&6&7\\\\
2&6&8&6
\\end{array}
\\right)
\\longrightarrow
\\left(
\\begin{array}{ccc|c}
1&2&1&2\\\\
0&1&3&1\\\\
0&2&6&2
\\end{array}
\\right)
\\longrightarrow
\\left(
\\begin{array}{ccc|c}
1&2&1&2\\\\
0&1&3&1\\\\
0&0&0&0
\\end{array}
\\right).
$$

Es entsteht keine Widerspruchszeile der Form $0=c$ mit $c\\ne0$. Also ist $Ax=b$ lösbar. Damit gilt

$$
b\\in\\operatorname{Bild}(f_A).
$$

Ad (b): Aus der Zeilenstufenform sieht man zwei Pivotzeilen. Daher

$$
\\operatorname{rang}(A)=2.
$$

Somit ist

$$
\\dim\\operatorname{Bild}(f_A)=\\operatorname{rang}(A)=2.
$$

Mit der Dimensionsformel

$$
\\dim\\ker(f_A)+\\dim\\operatorname{Bild}(f_A)=3
$$

folgt

$$
\\dim\\ker(f_A)=3-2=1.
$$""",
    },
    ("ss00", 4): {
        "problem": """Der affine Unterraum $E$ des $\\mathbb R^4$ sei die affine Hülle von

$$
\\{(1,1,1,1),(2,3,4,3),(2,5,5,4),(1,3,2,2)\\}.
$$

(a) Berechne die Dimension von $E$.

(b) Gib denjenigen affinen Unterraum $F$ des $\\mathbb R^4$ an, der durch $(4,3,2,1)$ geht und parallel zu $E$ ist.""",
        "zh_problem": """仿射子空间（affiner Unterraum）$E\\subset\\mathbb R^4$ 是下列四个点的仿射包（affine Hülle）：

$$
\\{(1,1,1,1),(2,3,4,3),(2,5,5,4),(1,3,2,2)\\}.
$$

(a) 求 $E$ 的维数。

(b) 写出经过点 $(4,3,2,1)$，并且与 $E$ 平行的仿射子空间 $F$。""",
        "solution": """Lösung:

Wir wählen den ersten Punkt als Stützpunkt. Dann ist

$$
\\begin{aligned}
E
&=(1,1,1,1)+\\operatorname{span}\\{(2,3,4,3)-(1,1,1,1),\\\\
&\\qquad (2,5,5,4)-(1,1,1,1),\\ (1,3,2,2)-(1,1,1,1)\\}\\\\
&=(1,1,1,1)+\\operatorname{span}\\{(1,2,3,2),(1,4,4,3),(0,2,1,1)\\}.
\\end{aligned}
$$

Sei

$$
U=\\operatorname{span}\\{(1,2,3,2),(1,4,4,3),(0,2,1,1)\\}.
$$

Zur Bestimmung von $\\dim U$ bringen wir die Erzeuger als Zeilen in Zeilenstufenform:

$$
\\begin{pmatrix}
1&2&3&2\\\\
1&4&4&3\\\\
0&2&1&1
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&2&3&2\\\\
0&2&1&1\\\\
0&2&1&1
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&2&3&2\\\\
0&2&1&1\\\\
0&0&0&0
\\end{pmatrix}.
$$

Damit ist

$$
\\dim E=\\dim U=2.
$$

Eine Basis des Richtungsraums ist zum Beispiel

$$
(1,2,3,2),\\qquad (0,2,1,1).
$$

Der zu $E$ parallele affine Unterraum durch $(4,3,2,1)$ ist daher

$$
F=(4,3,2,1)+\\operatorname{span}\\{(1,2,3,2),(0,2,1,1)\\}.
$$""",
        "zh_solution": """核心考点：**仿射包、方向空间、仿射子空间维数**。

仿射空间的维数不是直接数点，而是先固定一个基点，再看其它点相对这个基点产生的方向向量。

选第一个点

$$
p_0=(1,1,1,1).
$$

其余三个点减去它：

$$
(2,3,4,3)-p_0=(1,2,3,2),
$$

$$
(2,5,5,4)-p_0=(1,4,4,3),
$$

$$
(1,3,2,2)-p_0=(0,2,1,1).
$$

所以

$$
E=p_0+U,
$$

其中方向空间（Richtungsraum）

$$
U=\\operatorname{span}\\{(1,2,3,2),(1,4,4,3),(0,2,1,1)\\}.
$$

把三个方向向量作为行向量做行化简：

$$
\\begin{pmatrix}
1&2&3&2\\\\
1&4&4&3\\\\
0&2&1&1
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&2&3&2\\\\
0&2&1&1\\\\
0&0&0&0
\\end{pmatrix}.
$$

只有两个非零行，所以

$$
\\dim E=\\dim U=2.
$$

与 $E$ 平行，意思是方向空间仍然用同一个 $U$，只是支撑点换成 $(4,3,2,1)$。因此

$$
F=(4,3,2,1)+\\operatorname{span}\\{(1,2,3,2),(0,2,1,1)\\}.
$$

解题思路：仿射题先“减一个点”，把仿射问题变成普通向量空间问题；平行仿射空间就是方向空间不变、起点改变。""",
    },
    ("ss00", 5): {
        "problem": """Ein gerichteter Graph $(V,E)$ sei durch die Adjazenzmatrix

$$
A=
\\begin{pmatrix}
0&0&0&1&0\\\\
1&0&1&0&0\\\\
0&0&0&1&0\\\\
0&0&0&0&1\\\\
0&0&0&0&0
\\end{pmatrix}
$$

gegeben.

(a) Zeichne den Graphen $(V,E)$.

(b) Begründe anhand des Graphen, dass $A^4=0$ gilt.""",
        "zh_problem": """有向图（gerichteter Graph）$(V,E)$ 由邻接矩阵（Adjazenzmatrix）

$$
A=
\\begin{pmatrix}
0&0&0&1&0\\\\
1&0&1&0&0\\\\
0&0&0&1&0\\\\
0&0&0&0&1\\\\
0&0&0&0&0
\\end{pmatrix}
$$

给出。

(a) 画出图 $(V,E)$。

(b) 利用图说明为什么 $A^4=0$。""",
        "solution": """Lösung:

Aus der Adjazenzmatrix liest man ab: Es gibt genau dann eine gerichtete Kante $x_i\\to x_j$, wenn $a_{ij}=1$ ist. Daher sind die Kanten

$$
x_1\\to x_4,\qquad x_2\\to x_1,\qquad x_2\\to x_3,\qquad x_3\\to x_4,\qquad x_4\\to x_5.
$$

Dies beschreibt den zu zeichnenden Graphen mit den fünf Knoten $x_1,\ldots,x_5$.

Für Potenzen der Adjazenzmatrix gilt:

$$
(A^k)_{ij}=\\text{Anzahl der gerichteten Wege der Länge }k\\text{ von }x_i\\text{ nach }x_j.
$$

Im Graphen enden alle gerichteten Wege spätestens nach drei Schritten in $x_5$. Der längste gerichtete Weg ist zum Beispiel

$$
x_2\\to x_1\\to x_4\\to x_5
$$

oder

$$
x_2\\to x_3\\to x_4\\to x_5.
$$

Es gibt also keinen gerichteten Weg der Länge $4$. Deshalb sind alle Einträge von $A^4$ gleich $0$, also

$$
A^4=0.
$$""",
        "zh_solution": """核心考点：**邻接矩阵、路径计数、矩阵幂的图论意义**。

邻接矩阵的读法是：

$$
a_{ij}=1\\Longleftrightarrow x_i\\to x_j
$$

有一条有向边。

从矩阵中逐行读边：

$$
x_1\\to x_4,
$$

$$
x_2\\to x_1,\qquad x_2\\to x_3,
$$

$$
x_3\\to x_4,
$$

$$
x_4\\to x_5.
$$

第 5 行全是 $0$，说明 $x_5$ 没有 outgoing edge，走到 $x_5$ 就停住。

矩阵幂的核心公式是：

$$
(A^k)_{ij}=\\text{从 }x_i\\text{ 到 }x_j\\text{ 的长度为 }k\\text{ 的有向路径条数}.
$$

图中最长路径只有 3 条边，例如

$$
x_2\\to x_1\\to x_4\\to x_5
$$

以及

$$
x_2\\to x_3\\to x_4\\to x_5.
$$

不存在长度为 $4$ 的有向路径，所以 $A^4$ 的每个元素都是 $0$：

$$
A^4=0.
$$

解题思路：不要真的去乘四次矩阵。邻接矩阵的 $k$ 次幂就是数长度为 $k$ 的路；只要图里最长路小于 $4$，就立刻得到 $A^4=0$。""",
    },
    ("ss00", 6): {
        "problem": """Es sei $v_1,v_2,v_3,v_4$ eine Basis des $\\mathbb R^4$, sowie

$$
U=\\operatorname{span}(v_1,v_1+v_2),
\\qquad
V=\\operatorname{span}(v_2,v_3-v_1).
$$

(a) Zeige: $\\dim U=\\dim V=2$.

(b) Bestimme $\\dim(U+V)$.""",
        "zh_problem": """设 $v_1,v_2,v_3,v_4$ 是 $\\mathbb R^4$ 的一组基，并且

$$
U=\\operatorname{span}(v_1,v_1+v_2),
\\qquad
V=\\operatorname{span}(v_2,v_3-v_1).
$$

(a) 证明 $\\dim U=\\dim V=2$。

(b) 求 $\\dim(U+V)$。""",
        "solution": """Lösung:

Für $U$ prüfen wir die lineare Unabhängigkeit von $v_1$ und $v_1+v_2$. Sei

$$
\\lambda v_1+\\mu(v_1+v_2)=0.
$$

Dann

$$
(\\lambda+\\mu)v_1+\\mu v_2=0.
$$

Da $v_1,v_2$ linear unabhängig sind, folgt

$$
\\lambda+\\mu=0,\qquad \\mu=0,
$$

also $\\lambda=\\mu=0$. Somit ist $\\dim U=2$.

Für $V$ sei

$$
\\lambda v_2+\\mu(v_3-v_1)=0.
$$

Dann

$$
-\\mu v_1+\\lambda v_2+\\mu v_3=0.
$$

Da $v_1,v_2,v_3$ linear unabhängig sind, folgt $\\lambda=\\mu=0$. Also ist auch $\\dim V=2$.

Nun gilt

$$
U+V=\\operatorname{span}(v_1,v_1+v_2,v_2,v_3-v_1).
$$

Diese Menge erzeugt genau

$$
\\operatorname{span}(v_1,v_2,v_3).
$$

Denn alle Erzeuger liegen in $\\operatorname{span}(v_1,v_2,v_3)$, und umgekehrt liegen $v_1$, $v_2$ und

$$
v_3=(v_3-v_1)+v_1
$$

in $U+V$. Daher

$$
U+V=\\operatorname{span}(v_1,v_2,v_3).
$$

Weil $v_1,v_2,v_3$ Teil einer Basis sind, sind sie linear unabhängig. Also

$$
\\dim(U+V)=3.
$$""",
        "zh_solution": """核心考点：**线性无关、生成空间、子空间和的维数**。

先证明 $U$ 的两个生成向量确实线性无关。设

$$
\\lambda v_1+\\mu(v_1+v_2)=0.
$$

整理：

$$
(\\lambda+\\mu)v_1+\\mu v_2=0.
$$

因为 $v_1,v_2$ 来自一组基，所以线性无关。于是

$$
\\lambda+\\mu=0,\qquad \\mu=0.
$$

推出

$$
\\lambda=0,\qquad \\mu=0.
$$

所以 $v_1,v_1+v_2$ 线性无关，$\\dim U=2$。

同理证明 $V$。设

$$
\\lambda v_2+\\mu(v_3-v_1)=0.
$$

整理：

$$
-\\mu v_1+\\lambda v_2+\\mu v_3=0.
$$

由于 $v_1,v_2,v_3$ 线性无关，所以

$$
\\lambda=0,\qquad \\mu=0.
$$

因此 $\\dim V=2$。

接着看和空间：

$$
U+V=\\operatorname{span}(v_1,v_1+v_2,v_2,v_3-v_1).
$$

这些向量都在

$$
\\operatorname{span}(v_1,v_2,v_3)
$$

里面，所以

$$
U+V\\subseteq \\operatorname{span}(v_1,v_2,v_3).
$$

反过来，$v_1\\in U+V$，$v_2\\in U+V$，并且

$$
v_3=(v_3-v_1)+v_1\\in U+V.
$$

所以

$$
\\operatorname{span}(v_1,v_2,v_3)\\subseteq U+V.
$$

两边合起来：

$$
U+V=\\operatorname{span}(v_1,v_2,v_3).
$$

由于 $v_1,v_2,v_3$ 是基的一部分，线性无关，因此

$$
\\dim(U+V)=3.
$$

解题思路：看到 $U+V$，先把所有生成向量放一起；再删掉重复信息。这里 $v_1+v_2$ 已经由 $v_1,v_2$ 表示，$v_3-v_1$ 配合 $v_1$ 可以拿回 $v_3$，所以最后就是三维空间 $\\operatorname{span}(v_1,v_2,v_3)$。""",
    },
    ("ss18", 2): {
        "problem": """Für $a\\in\\mathbb R$ sei

$$
M(a):=\\frac12
\\begin{pmatrix}
a+1 & a-1 \\\\
a-1 & a+1
\\end{pmatrix}\\in\\mathbb R^{2\\times2}.
$$

(a) Man berechne $M(a)M(b)$ für $a,b\\in\\mathbb R$.

(b) Man bestimme für $a\\in\\mathbb R\\setminus\\{0\\}$ ein $b\\in\\mathbb R$, so dass

$$
M(a)M(b)=
\\begin{pmatrix}
1&0\\\\
0&1
\\end{pmatrix}.
$$

(c) Man zeige, dass

$$
G:=\\{M(a)\\mid a\\in\\mathbb R\\setminus\\{0\\}\\}
$$

mit der Matrixmultiplikation als Verknüpfung eine Untergruppe von $GL(2,\\mathbb R)$ ist.

(d) Man zeige, dass $(G,\\cdot)$ isomorph zu $(\\mathbb R\\setminus\\{0\\},\\cdot)$ ist.""",
        "solution": """Lösung:

Ad (a): Für $a,b\\in\\mathbb R$ gilt

$$
\\begin{aligned}
M(a)M(b)
&=\\frac12
\\begin{pmatrix}
a+1 & a-1\\\\
a-1 & a+1
\\end{pmatrix}
\\cdot
\\frac12
\\begin{pmatrix}
b+1 & b-1\\\\
b-1 & b+1
\\end{pmatrix}\\\\
&=\\frac14
\\begin{pmatrix}
(a+1)(b+1)+(a-1)(b-1) & (a+1)(b-1)+(a-1)(b+1)\\\\
(a-1)(b+1)+(a+1)(b-1) & (a-1)(b-1)+(a+1)(b+1)
\\end{pmatrix}\\\\
&=\\frac14
\\begin{pmatrix}
2ab+2 & 2ab-2\\\\
2ab-2 & 2ab+2
\\end{pmatrix}\\\\
&=\\frac12
\\begin{pmatrix}
ab+1 & ab-1\\\\
ab-1 & ab+1
\\end{pmatrix}
=M(ab).
\\end{aligned}
$$

Ad (b): Nach Teil (a) gilt $M(a)M(b)=M(ab)$. Damit ist

$$
M(a)M(b)=I_2
\\Longleftrightarrow
M(ab)=M(1)
\\Longleftrightarrow
ab=1
\\Longleftrightarrow
b=a^{-1}.
$$

Also ist $M(a)^{-1}=M(a^{-1})$ für $a\\ne0$.

Ad (c): Wir prüfen das Untergruppenkriterium in $GL(2,\\mathbb R)$.

Erstens ist $M(1)=I_2\\in G$. Zweitens gilt für $a,b\\ne0$

$$
M(a)M(b)=M(ab)\\in G,
$$

weil $ab\\ne0$. Drittens gilt nach Teil (b)

$$
M(a)^{-1}=M(a^{-1})\\in G.
$$

Damit ist $G$ eine Untergruppe von $GL(2,\\mathbb R)$.

Ad (d): Definiere

$$
\\varphi:\\mathbb R\\setminus\\{0\\}\\to G,
\\qquad
\\varphi(a)=M(a).
$$

Dann gilt für alle $a,b\\ne0$

$$
\\varphi(ab)=M(ab)=M(a)M(b)=\\varphi(a)\\varphi(b),
$$

also ist $\\varphi$ ein Gruppenhomomorphismus.

Die Abbildung ist injektiv, denn aus $M(a)=M(b)$ folgt zum Beispiel aus dem $(1,1)$-Eintrag

$$
\\frac12(a+1)=\\frac12(b+1)\\Longrightarrow a=b.
$$

Sie ist surjektiv, weil jedes Element von $G$ per Definition die Form $M(a)$ mit $a\\ne0$ hat. Also ist $\\varphi$ ein Gruppenisomorphismus.""",
    },
    ("ss19", 2): {
        "problem": """Sei $n\\in\\mathbb N$. Es sollen Matrizen $M\\in\\mathbb R^{n\\times n}$ betrachtet werden, die Lösungen der Matrixgleichung

$$
M^2=3M+4I_n
$$

sind.

(a) Bestimmen Sie alle $\\gamma\\in\\mathbb R$, sodass $\\gamma I_n$ eine Lösung dieser Gleichung ist.

In den restlichen Teilaufgaben sei $A\\in\\mathbb R^{n\\times n}$ eine Lösung der Matrixgleichung.

(b) Man zeige durch vollständige Induktion, dass $A^k$ für jedes $k\\in\\mathbb N$ eine Linearkombination von $A$ und $I_n$ ist.

(c) Man zeige: $A$ ist invertierbar.

(d) Man zeige: $A^{-1}$ ist eine Linearkombination von $A$ und $I_n$.

(e) Man zeige: Ist $B$ ähnlich zu $A$, so ist $B$ ebenfalls eine Lösung der Matrixgleichung.""",
        "solution": """Lösung:

Ad (a): Für $M=\\gamma I_n$ gilt

$$
(\\gamma I_n)^2=3\\gamma I_n+4I_n
\\Longleftrightarrow
\\gamma^2 I_n=(3\\gamma+4)I_n
\\Longleftrightarrow
\\gamma^2-3\\gamma-4=0.
$$

Also

$$
(\\gamma-4)(\\gamma+1)=0,
$$

und damit

$$
\\gamma=4\\quad\\text{oder}\\quad\\gamma=-1.
$$

Ad (b): Zu zeigen ist: Für jedes $k\\in\\mathbb N$ gibt es $\\alpha_k,\\beta_k\\in\\mathbb R$ mit

$$
A^k=\\alpha_k A+\\beta_k I_n.
$$

Induktionsanfang $k=1$:

$$
A^1=1\\cdot A+0\\cdot I_n.
$$

Induktionsschritt: Angenommen

$$
A^k=\\alpha_kA+\\beta_kI_n.
$$

Dann folgt

$$
\\begin{aligned}
A^{k+1}
&=A^kA\\\\
&=(\\alpha_kA+\\beta_kI_n)A\\\\
&=\\alpha_kA^2+\\beta_kA\\\\
&=\\alpha_k(3A+4I_n)+\\beta_kA\\\\
&=(3\\alpha_k+\\beta_k)A+4\\alpha_kI_n.
\\end{aligned}
$$

Also ist auch $A^{k+1}$ eine Linearkombination von $A$ und $I_n$.

Ad (c): Da $A$ die Gleichung erfüllt, gilt

$$
A^2=3A+4I_n.
$$

Umstellen liefert

$$
A^2-3A=4I_n
\\Longleftrightarrow
A(A-3I_n)=4I_n.
$$

Daher

$$
A\\cdot \\frac14(A-3I_n)=I_n.
$$

Also ist $A$ invertierbar.

Ad (d): Aus Teil (c) folgt direkt

$$
A^{-1}=\\frac14(A-3I_n)=\\frac14A-\\frac34I_n.
$$

Damit ist $A^{-1}$ eine Linearkombination von $A$ und $I_n$.

Ad (e): Sei $B$ ähnlich zu $A$, also $B=S^{-1}AS$ mit invertierbarem $S$. Dann gilt

$$
\\begin{aligned}
B^2
&=(S^{-1}AS)(S^{-1}AS)\\\\
&=S^{-1}A^2S\\\\
&=S^{-1}(3A+4I_n)S\\\\
&=3S^{-1}AS+4S^{-1}I_nS\\\\
&=3B+4I_n.
\\end{aligned}
$$

Also erfüllt auch $B$ die Matrixgleichung.""",
    },
    ("ss19-2", 1): {
        "problem": """Man zeige für $n\\in\\mathbb N$ die folgende Gleichung für reelle $3\\times3$-Matrizen durch vollständige Induktion:

$$
\\begin{pmatrix}
1 & 0 & 0 \\\\
2 & 1 & -1 \\\\
-1 & 0 & 2
\\end{pmatrix}^n
=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^n+n-1 & 1 & -2^n+1 \\\\
-2^n+1 & 0 & 2^n
\\end{pmatrix}.
$$""",
        "solution": """Lösung:

Setze

$$
A=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2 & 1 & -1 \\\\
-1 & 0 & 2
\\end{pmatrix}.
$$

Zu zeigen ist

$$
A^n=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^n+n-1 & 1 & -2^n+1 \\\\
-2^n+1 & 0 & 2^n
\\end{pmatrix}.
$$

Induktionsanfang $n=1$:

$$
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^1+1-1 & 1 & -2^1+1 \\\\
-2^1+1 & 0 & 2^1
\\end{pmatrix}
=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2 & 1 & -1 \\\\
-1 & 0 & 2
\\end{pmatrix}
=A.
$$

Induktionsannahme: Für ein festes $n\\in\\mathbb N$ gelte

$$
A^n=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^n+n-1 & 1 & -2^n+1 \\\\
-2^n+1 & 0 & 2^n
\\end{pmatrix}.
$$

Induktionsschritt:

$$
A^{n+1}=A^nA.
$$

Mit der Induktionsannahme:

$$
\\begin{aligned}
A^{n+1}
&=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^n+n-1 & 1 & -2^n+1 \\\\
-2^n+1 & 0 & 2^n
\\end{pmatrix}
\\begin{pmatrix}
1 & 0 & 0 \\\\
2 & 1 & -1 \\\\
-1 & 0 & 2
\\end{pmatrix}\\\\
&=
\\begin{pmatrix}
1 & 0 & 0 \\\\
(2^n+n-1)+2+(-2^n+1)(-1) & 1 & -1+2(-2^n+1) \\\\
(-2^n+1)+2^n(-1) & 0 & 2\\cdot2^n
\\end{pmatrix}\\\\
&=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^{n+1}+n & 1 & -2^{n+1}+1 \\\\
-2^{n+1}+1 & 0 & 2^{n+1}
\\end{pmatrix}\\\\
&=
\\begin{pmatrix}
1 & 0 & 0 \\\\
2^{n+1}+(n+1)-1 & 1 & -2^{n+1}+1 \\\\
-2^{n+1}+1 & 0 & 2^{n+1}
\\end{pmatrix}.
\\end{aligned}
$$

Damit gilt die Formel für $n+1$. Nach vollständiger Induktion ist die Behauptung für alle $n\\in\\mathbb N$ bewiesen.""",
    },
    ("ss08", 1): {
        "problem": """Zeigen Sie die folgende Gleichung durch vollständige Induktion:

$$
\\begin{pmatrix}
1 & 0 & 1 \\\\
0 & -1 & 0 \\\\
1 & 0 & 1
\\end{pmatrix}^{2n}
=\\frac12
\\begin{pmatrix}
4^n & 0 & 4^n \\\\
0 & 2 & 0 \\\\
4^n & 0 & 4^n
\\end{pmatrix}
\\qquad (n\\in\\mathbb N).
$$""",
        "solution": """Lösung:

Setze

$$
A=\\begin{pmatrix}
1 & 0 & 1 \\\\
0 & -1 & 0 \\\\
1 & 0 & 1
\\end{pmatrix}.
$$

Zu zeigen ist

$$
A^{2n}=\\frac12
\\begin{pmatrix}
4^n & 0 & 4^n \\\\
0 & 2 & 0 \\\\
4^n & 0 & 4^n
\\end{pmatrix}.
$$

Induktionsanfang $n=1$:

$$
A^2=
\\begin{pmatrix}
1 & 0 & 1 \\\\
0 & -1 & 0 \\\\
1 & 0 & 1
\\end{pmatrix}^2
=
\\begin{pmatrix}
2 & 0 & 2 \\\\
0 & 1 & 0 \\\\
2 & 0 & 2
\\end{pmatrix}
=\\frac12
\\begin{pmatrix}
4 & 0 & 4 \\\\
0 & 2 & 0 \\\\
4 & 0 & 4
\\end{pmatrix}.
$$

Induktionsannahme: Für ein $n\\in\\mathbb N$ gelte

$$
A^{2n}=\\frac12
\\begin{pmatrix}
4^n & 0 & 4^n \\\\
0 & 2 & 0 \\\\
4^n & 0 & 4^n
\\end{pmatrix}.
$$

Induktionsschritt:

$$
A^{2(n+1)}=A^{2n}A^2.
$$

Mit der Induktionsannahme und dem oben berechneten $A^2$ folgt

$$
A^{2(n+1)}
=\\frac12
\\begin{pmatrix}
4^n & 0 & 4^n \\\\
0 & 2 & 0 \\\\
4^n & 0 & 4^n
\\end{pmatrix}
\\begin{pmatrix}
2 & 0 & 2 \\\\
0 & 1 & 0 \\\\
2 & 0 & 2
\\end{pmatrix}
=\\frac12
\\begin{pmatrix}
4^{n+1} & 0 & 4^{n+1} \\\\
0 & 2 & 0 \\\\
4^{n+1} & 0 & 4^{n+1}
\\end{pmatrix}.
$$

Damit ist die Behauptung für alle $n\\in\\mathbb N$ bewiesen.""",
    },
    ("ss18", 7): {
        "problem": """Gegeben sei

$$A:=\\begin{pmatrix}
1 & -1 & 1 \\\\
0 & 0 & 0 \\\\
-1 & 1 & -1
\\end{pmatrix}\\in\\mathbb R^{3\\times 3}.$$

(a) Man bestimme den Rang von $A$ und begründe damit, weshalb $0$ Eigenwert von $A$ ist.

(b) Man berechne das charakteristische Polynom von $A$ und gebe alle Eigenwerte von $A$ an.

(c) Man bestimme für jeden Eigenwert von $A$ den zugehörigen Eigenraum.

(d) Man beantworte mit Begründung die Frage, ob $A$ diagonalisierbar ist.""",
        "solution": """Lösung:

Ad (a): Die dritte Zeile ist das Negative der ersten Zeile und die zweite Zeile ist null. Daher gilt

$$A\\sim\\begin{pmatrix}
1 & -1 & 1 \\\\
0 & 0 & 0 \\\\
0 & 0 & 0
\\end{pmatrix},\\qquad \\operatorname{rang}(A)=1.$$

Damit ist

$$\\dim\\ker A=3-\\operatorname{rang}(A)=3-1=2.$$

Also enthält $\\ker A$ einen Vektor $v\\ne0$ mit $Av=0=0\\cdot v$. Daher ist $0$ ein Eigenwert von $A$.

Ad (b): Das charakteristische Polynom ist

$$\\chi_A(\\lambda)=\\det(A-\\lambda I)
=\\det\\begin{pmatrix}
1-\\lambda & -1 & 1 \\\\
0 & -\\lambda & 0 \\\\
-1 & 1 & -1-\\lambda
\\end{pmatrix}.$$

Entwicklung nach der zweiten Zeile liefert

$$\\chi_A(\\lambda)
=-\\lambda\\det\\begin{pmatrix}
1-\\lambda & 1 \\\\
-1 & -1-\\lambda
\\end{pmatrix}
=-\\lambda\\bigl((1-\\lambda)(-1-\\lambda)+1\\bigr)
=-\\lambda^3.$$

Der einzige Eigenwert ist also $\\lambda=0$ mit algebraischer Vielfachheit $3$.

Ad (c): Für den Eigenraum zu $0$ lösen wir $Ax=0$. Aus der Zeilenstufenform folgt

$$x_1-x_2+x_3=0.$$

Damit gilt $x_1=x_2-x_3$. Setze $x_2=s$ und $x_3=t$. Dann ist

$$x=s\\begin{pmatrix}1\\\\1\\\\0\\end{pmatrix}
+t\\begin{pmatrix}-1\\\\0\\\\1\\end{pmatrix}.$$

Also

$$E_0=\\ker A
=\\operatorname{span}\\left\\{
\\begin{pmatrix}1\\\\1\\\\0\\end{pmatrix},
\\begin{pmatrix}-1\\\\0\\\\1\\end{pmatrix}
\\right\\}.$$

Ad (d): Die geometrische Vielfachheit von $0$ ist

$$\\dim E_0=2,$$

die algebraische Vielfachheit von $0$ ist $3$. Weil geometrische und algebraische Vielfachheit nicht übereinstimmen, ist $A$ nicht diagonalisierbar.""",
    }
}


MANUAL_OVERRIDES.update({
    ("ss08", 2): {
        "problem": """(a) Zeigen Sie, dass die Menge aller reellen invertierbaren Diagonalmatrizen

$$
G=\\{\\operatorname{diag}(d_1,\\ldots,d_n)\\mid d_1,\ldots,d_n\\ne0\\}
$$

bezüglich der Matrixmultiplikation eine Gruppe bildet.

(b) Gilt dies auch, wenn man stattdessen $d_1\\ge0,\ldots,d_n\\ge0$ fordert? Begründen Sie.""",
        "zh_problem": """(a) 证明所有实可逆对角矩阵（invertierbare Diagonalmatrizen）

$$
G=\\{\\operatorname{diag}(d_1,\\ldots,d_n)\\mid d_1,\ldots,d_n\\ne0\\}
$$

在矩阵乘法下构成一个群（Gruppe）。

(b) 如果改成要求 $d_1\\ge0,\ldots,d_n\\ge0$，是否仍然构成群？请说明理由。""",
        "solution": """Lösung:

Für

$$
D=\\operatorname{diag}(d_1,\\ldots,d_n),\\qquad
E=\\operatorname{diag}(e_1,\\ldots,e_n)
$$

mit allen $d_i,e_i\\ne0$ gilt

$$
DE=\\operatorname{diag}(d_1e_1,\ldots,d_ne_n).
$$

Da $d_ie_i\\ne0$, ist $DE$ wieder in $G$. Das neutrale Element ist

$$
I_n=\\operatorname{diag}(1,\ldots,1).
$$

Außerdem hat jedes $D\\in G$ das Inverse

$$
D^{-1}=\\operatorname{diag}(d_1^{-1},\\ldots,d_n^{-1}),
$$

und dieses liegt wieder in $G$. Die Assoziativität kommt von der gewöhnlichen Matrixmultiplikation. Also ist $G$ eine Gruppe.

Für die Forderung $d_i\\ge0$ ist die Antwort: Nein, wenn $0$ erlaubt ist. Zum Beispiel

$$
D=\\operatorname{diag}(0,1,\ldots,1)
$$

hat keinen inversen Eintrag an der ersten Stelle und ist nicht invertierbar. Eine Gruppe bezüglich der Matrixmultiplikation kann aber keine nichtinvertierbaren Elemente enthalten. Nur mit der stärkeren Bedingung $d_i>0$ entstünde wieder eine Gruppe.""",
        "zh_solution": """核心考点：**矩阵群、对角矩阵乘法、逆元**。

两个对角矩阵相乘时，对角线逐项相乘：

$$
\\operatorname{diag}(d_1,\ldots,d_n)\\operatorname{diag}(e_1,\ldots,e_n)
=\\operatorname{diag}(d_1e_1,\ldots,d_ne_n).
$$

如果所有 $d_i,e_i$ 都非零，那么所有 $d_ie_i$ 也非零，所以乘法封闭。单位元是

$$
I_n=\\operatorname{diag}(1,\ldots,1).
$$

每个元素的逆矩阵是

$$
\\operatorname{diag}(d_1^{-1},\ldots,d_n^{-1}),
$$

仍然是非零对角矩阵。结合律来自矩阵乘法本身，所以这是一个群。

如果只要求 $d_i\\ge0$，则允许 $d_i=0$，例如 $\\operatorname{diag}(0,1,\ldots,1)$ 不可逆，没有逆元，因此不是群。若改成 $d_i>0$，才会重新成为群。""",
    },
    ("ss08", 3): {
        "problem": """Gegeben sei $\\alpha\\in\\mathbb R$ und

$$
A=
\\begin{pmatrix}
1&1&1\\\\
0&1&0\\\\
1&0&\\alpha+1
\\end{pmatrix}.
$$

Bestimmen Sie, für welche $\\alpha$ die Matrix $A$ invertierbar ist, und berechnen Sie dann $A^{-1}$.""",
        "zh_problem": """设 $\\alpha\\in\\mathbb R$，并给定

$$
A=
\\begin{pmatrix}
1&1&1\\\\
0&1&0\\\\
1&0&\\alpha+1
\\end{pmatrix}.
$$

求哪些 $\\alpha$ 使 $A$ 可逆，并在可逆时计算 $A^{-1}$。""",
        "solution": """Lösung:

Die Determinante ist

$$
\\det A
=
\\det\\begin{pmatrix}
1&1&1\\\\
0&1&0\\\\
1&0&\\alpha+1
\\end{pmatrix}
=\\alpha.
$$

Also ist $A$ genau dann invertierbar, wenn

$$
\\alpha\\ne0.
$$

Für $\\alpha\\ne0$ ergibt Gauß-Jordan

$$
A^{-1}=
\\begin{pmatrix}
\\frac{\\alpha+1}{\\alpha}&-\\frac{\\alpha+1}{\\alpha}&-\\frac1\\alpha\\\\
0&1&0\\\\
-\\frac1\\alpha&\\frac1\\alpha&\\frac1\\alpha
\\end{pmatrix}.
$$""",
        "zh_solution": """核心考点：**行列式判可逆、参数逆矩阵**。

先算行列式：

$$
\\det A=\\alpha.
$$

矩阵可逆当且仅当行列式非零，所以

$$
\\alpha\\ne0.
$$

当 $\\alpha\\ne0$ 时，用 Gauss-Jordan 消元或解 $AX=I$，得到

$$
A^{-1}=
\\begin{pmatrix}
\\frac{\\alpha+1}{\\alpha}&-\\frac{\\alpha+1}{\\alpha}&-\\frac1\\alpha\\\\
0&1&0\\\\
-\\frac1\\alpha&\\frac1\\alpha&\\frac1\\alpha
\\end{pmatrix}.
$$

解题思路：参数题先看行列式。只有让行列式不为零的参数，才需要继续算逆矩阵；行列式为零的参数直接不可逆。""",
    },
    ("ss08", 4): {
        "problem": """Gegeben seien

$$
a=\\begin{pmatrix}1\\\\2\\\\4\\end{pmatrix},\\quad
b=\\begin{pmatrix}1\\\\3\\\\5\\end{pmatrix},\\quad
c=\\begin{pmatrix}2\\\\4\\\\5\\end{pmatrix}.
$$

Bestimmen Sie eine Basis $B$ von $\\operatorname{span}(a,b,c)$ und untersuchen Sie, mit welchen der Vektoren $e_1,e_2,e_3$ aus der kanonischen Basis $B$ zu einer Basis von $\\mathbb R^3$ ergänzt werden kann.""",
        "zh_problem": """给定

$$
a=\\begin{pmatrix}1\\\\2\\\\4\\end{pmatrix},\\quad
b=\\begin{pmatrix}1\\\\3\\\\5\\end{pmatrix},\\quad
c=\\begin{pmatrix}2\\\\4\\\\5\\end{pmatrix}.
$$

求 $\\operatorname{span}(a,b,c)$ 的一组基 $B$，并判断可以用标准基向量 $e_1,e_2,e_3$ 中的哪些向量把 $B$ 补成 $\\mathbb R^3$ 的一组基。""",
        "solution": """Lösung:

Wir betrachten die Matrix mit den Spalten $a,b,c$:

$$
M=(a\\ b\\ c)=
\\begin{pmatrix}
1&1&2\\\\
2&3&4\\\\
4&5&5
\\end{pmatrix}.
$$

Es gilt

$$
\\det M=-3\\ne0.
$$

Daher sind $a,b,c$ linear unabhängig und bilden bereits eine Basis von $\\mathbb R^3$. Also kann man wählen

$$
B=(a,b,c).
$$

Da $B$ schon eine Basis von $\\mathbb R^3$ ist, muss und kann kein weiterer Vektor ergänzt werden. Fügt man einen der Vektoren $e_1,e_2,e_3$ hinzu, erhält man vier Vektoren in $\\mathbb R^3$, also keine Basis.""",
        "zh_solution": """核心考点：**列向量行列式、基、补基**。

把 $a,b,c$ 作为列组成矩阵：

$$
M=
\\begin{pmatrix}
1&1&2\\\\
2&3&4\\\\
4&5&5
\\end{pmatrix}.
$$

计算

$$
\\det M=-3\\ne0.
$$

所以 $a,b,c$ 线性无关。三个线性无关向量在 $\\mathbb R^3$ 中已经构成一组基，因此

$$
B=(a,b,c)
$$

就是 $\\operatorname{span}(a,b,c)=\\mathbb R^3$ 的基。

既然 $B$ 已经是 $\\mathbb R^3$ 的基，就不需要补向量；加入任意一个 $e_1,e_2,e_3$ 都会变成 $4$ 个向量，不可能仍是一组基。""",
    },
    ("ss08", 5): {
        "problem": """Für $\\alpha\\in\\mathbb C$ sei

$$
A=
\\begin{pmatrix}
i&0&0&i\\\\
0&1&1&0\\\\
i&0&1&0\\\\
1&\\alpha&1&0
\\end{pmatrix}.
$$

(a) Berechnen Sie $\\det A$.
(b) Berechnen Sie $\\operatorname{rang}A$, falls $\\det A=0$.
(c) Bestimmen Sie $\\operatorname{rang}A$, falls $\\det A\\ne0$.""",
        "zh_problem": """设 $\\alpha\\in\\mathbb C$，

$$
A=
\\begin{pmatrix}
i&0&0&i\\\\
0&1&1&0\\\\
i&0&1&0\\\\
1&\\alpha&1&0
\\end{pmatrix}.
$$

(a) 计算 $\\det A$。
(b) 当 $\\det A=0$ 时计算 $\\operatorname{rang}A$。
(c) 当 $\\det A\\ne0$ 时确定 $\\operatorname{rang}A$。""",
        "solution": """Lösung:

Eine direkte Determinantenrechnung liefert

$$
\\det A=\\alpha-1-i.
$$

Also gilt $\\det A=0$ genau für

$$
\\alpha=1+i.
$$

Für diesen Wert erhält man durch Zeilenreduktion drei Pivotzeilen, also

$$
\\operatorname{rang}A=3.
$$

Falls $\\det A\\ne0$, ist $A$ eine invertierbare $4\\times4$-Matrix. Dann hat sie vollen Rang:

$$
\\operatorname{rang}A=4.
$$""",
        "zh_solution": """核心考点：**复矩阵行列式、行列式为零时单独算秩**。

先算行列式：

$$
\\det A=\\alpha-1-i.
$$

所以

$$
\\det A=0\\Longleftrightarrow \\alpha=1+i.
$$

当 $\\alpha=1+i$ 时，把矩阵代入后行化简，有 $3$ 个主元，因此

$$
\\operatorname{rang}A=3.
$$

当 $\\det A\\ne0$ 时，$A$ 是可逆的 $4\\times4$ 矩阵，所以满秩：

$$
\\operatorname{rang}A=4.
$$

解题思路：行列式非零直接满秩；行列式为零时不能说秩是多少，必须代入特殊参数再行化简。""",
    },
    ("ss08", 6): {
        "problem": """Sei $A\\in\\mathbb R^{n\\times n}$. Zeigen Sie:

(a) $A^2=A\\Rightarrow \\det A=0$ oder $\\det A=1$.

(b) $A$ ist invertierbar genau dann, wenn $A^TA$ invertierbar ist.

(c) $A^2=0\\Rightarrow I_n-A$ ist invertierbar.""",
        "zh_problem": """设 $A\\in\\mathbb R^{n\\times n}$。证明：

(a) 若 $A^2=A$，则 $\\det A=0$ 或 $\\det A=1$。

(b) $A$ 可逆当且仅当 $A^TA$ 可逆。

(c) 若 $A^2=0$，则 $I_n-A$ 可逆。""",
        "solution": """Lösung:

(a) Aus $A^2=A$ folgt

$$
\\det(A^2)=\\det A.
$$

Mit $\\det(A^2)=(\\det A)^2$ erhält man

$$
(\\det A)^2=\\det A.
$$

Also

$$
\\det A(\\det A-1)=0,
$$

und damit $\\det A=0$ oder $\\det A=1$.

(b) Ist $A$ invertierbar, dann sind auch $A^T$ und $A^TA$ invertierbar. Umgekehrt: Ist $A^TA$ invertierbar, dann

$$
0\\ne\\det(A^TA)=\\det(A^T)\\det(A)=(\\det A)^2.
$$

Also ist $\\det A\\ne0$, somit ist $A$ invertierbar.

(c) Wenn $A^2=0$, dann gilt

$$
(I_n-A)(I_n+A)=I_n-A^2=I_n.
$$

Ebenso $(I_n+A)(I_n-A)=I_n$. Daher ist

$$
(I_n-A)^{-1}=I_n+A.
$$""",
        "zh_solution": """核心考点：**行列式乘法、转置、幂零矩阵求逆**。

(a) 对 $A^2=A$ 两边取行列式：

$$
\\det(A^2)=\\det A.
$$

左边等于

$$
(\\det A)^2.
$$

所以

$$
(\\det A)^2=\\det A
\\Longleftrightarrow
\\det A(\\det A-1)=0.
$$

因此 $\\det A=0$ 或 $\\det A=1$。

(b) 若 $A$ 可逆，则 $A^T$ 可逆，乘积 $A^TA$ 也可逆。反过来，如果 $A^TA$ 可逆，则

$$
0\\ne\\det(A^TA)=\\det(A^T)\\det(A)=(\\det A)^2.
$$

所以 $\\det A\\ne0$，即 $A$ 可逆。

(c) 题目提示“猜逆矩阵”。因为 $A^2=0$，所以

$$
(I_n-A)(I_n+A)=I_n-A^2=I_n.
$$

因此

$$
(I_n-A)^{-1}=I_n+A.
$$""",
    },
    ("ss08", 7): {
        "problem": """Gegeben sei

$$
A=
\\begin{pmatrix}
2&0&2\\\\
0&3&0\\\\
2&0&-1
\\end{pmatrix}.
$$

Sie dürfen voraussetzen, dass $3$ ein Eigenwert von $A$ ist.

(a) Bestimmen Sie $\\operatorname{Eig}_A(3)$.
(b) Berechnen Sie $\\chi_A$ und geben Sie alle Eigenwerte von $A$ an.""",
        "zh_problem": """给定

$$
A=
\\begin{pmatrix}
2&0&2\\\\
0&3&0\\\\
2&0&-1
\\end{pmatrix}.
$$

已知 $3$ 是 $A$ 的特征值。

(a) 求 $\\operatorname{Eig}_A(3)$。
(b) 计算特征多项式 $\\chi_A$ 并给出全部特征值。""",
        "solution": """Lösung:

Für $\\lambda=3$ lösen wir $(A-3I)x=0$:

$$
A-3I=
\\begin{pmatrix}
-1&0&2\\\\
0&0&0\\\\
2&0&-4
\\end{pmatrix}.
$$

Die Gleichung ist $-x_1+2x_3=0$, also $x_1=2x_3$; $x_2$ ist frei. Daher

$$
\\operatorname{Eig}_A(3)=
\\operatorname{span}\\left\\{
\\begin{pmatrix}0\\\\1\\\\0\\end{pmatrix},
\\begin{pmatrix}2\\\\0\\\\1\\end{pmatrix}
\\right\\}.
$$

Das charakteristische Polynom ist

$$
\\chi_A(\\lambda)=(\\lambda-3)^2(\\lambda+2).
$$

Die Eigenwerte sind also

$$
3\\quad\\text{mit algebraischer Vielfachheit }2,
\\qquad
-2\\quad\\text{mit algebraischer Vielfachheit }1.
$$""",
        "zh_solution": """核心考点：**特征空间、特征多项式、代数重数**。

先求 $\\lambda=3$ 的特征空间：

$$
A-3I=
\\begin{pmatrix}
-1&0&2\\\\
0&0&0\\\\
2&0&-4
\\end{pmatrix}.
$$

方程 $(A-3I)x=0$ 给出

$$
-x_1+2x_3=0,
$$

所以

$$
x_1=2x_3.
$$

令 $x_2=s,\ x_3=t$，得到

$$
x=s\\begin{pmatrix}0\\\\1\\\\0\\end{pmatrix}
t\\begin{pmatrix}2\\\\0\\\\1\\end{pmatrix}.
$$

因此

$$
\\operatorname{Eig}_A(3)=
\\operatorname{span}\\left\\{
\\begin{pmatrix}0\\\\1\\\\0\\end{pmatrix},
\\begin{pmatrix}2\\\\0\\\\1\\end{pmatrix}
\\right\\}.
$$

特征多项式为

$$
\\chi_A(\\lambda)=(\\lambda-3)^2(\\lambda+2).
$$

所以特征值是

$$
3\\quad(2\\text{ 重}),\qquad -2\\quad(1\\text{ 重}).
$$

解题思路：先利用给定特征值求特征空间；因为 $\\dim E_3=2$，所以 $3$ 至少有代数重数 $2$。再用迹或直接算特征多项式补出另一个特征值。""",
    },
    ("ss08", 8): {
        "problem": """Berechnen Sie alle Eigenwerte und Eigenvektoren der Matrix

$$
A=
\\begin{pmatrix}
0&i\\\\
-i&0
\\end{pmatrix}
\\in\\mathbb C^{2\\times2}.
$$""",
        "zh_problem": """计算复矩阵

$$
A=
\\begin{pmatrix}
0&i\\\\
-i&0
\\end{pmatrix}
\\in\\mathbb C^{2\\times2}
$$

的所有特征值和特征向量。""",
        "solution": """Lösung:

Das charakteristische Polynom ist

$$
\\chi_A(\\lambda)=\\det(A-\\lambda I)
=\\det\\begin{pmatrix}
-\\lambda&i\\\\
-i&-\\lambda
\\end{pmatrix}
=\\lambda^2-1.
$$

Also sind die Eigenwerte

$$
\\lambda_1=1,\qquad \\lambda_2=-1.
$$

Für $\\lambda=1$ löst man $(A-I)x=0$ und erhält zum Beispiel den Eigenvektor

$$
\\begin{pmatrix}i\\\\1\\end{pmatrix}.
$$

Also

$$
E_1=\\operatorname{span}\\left\\{\\begin{pmatrix}i\\\\1\\end{pmatrix}\\right\\}.
$$

Für $\\lambda=-1$ erhält man zum Beispiel

$$
\\begin{pmatrix}-i\\\\1\\end{pmatrix},
$$

also

$$
E_{-1}=\\operatorname{span}\\left\\{\\begin{pmatrix}-i\\\\1\\end{pmatrix}\\right\\}.
$$""",
        "zh_solution": """核心考点：**复矩阵特征值、特征向量**。

先算特征多项式：

$$
\\chi_A(\\lambda)
=\\det\\begin{pmatrix}
-\\lambda&i\\\\
-i&-\\lambda
\\end{pmatrix}
=\\lambda^2-1.
$$

所以

$$
\\lambda=1\\quad\\text{或}\\quad \\lambda=-1.
$$

当 $\\lambda=1$ 时，解 $(A-I)x=0$，可取特征向量

$$
\\begin{pmatrix}i\\\\1\\end{pmatrix}.
$$

于是

$$
E_1=\\operatorname{span}\\left\\{\\begin{pmatrix}i\\\\1\\end{pmatrix}\\right\\}.
$$

当 $\\lambda=-1$ 时，解 $(A+I)x=0$，可取

$$
\\begin{pmatrix}-i\\\\1\\end{pmatrix}.
$$

所以

$$
E_{-1}=\\operatorname{span}\\left\\{\\begin{pmatrix}-i\\\\1\\end{pmatrix}\\right\\}.
$$

解题思路：复数矩阵和实数矩阵算法完全一样，只是运算允许出现 $i$。先求根，再分别代回去解齐次方程。""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss17", 3): {
        "problem": """Gegeben seien $t\\in\\mathbb R$ und

$$
A=
\\begin{pmatrix}
1&0&0&t\\\\
1&0&1&t\\\\
1&0&t&1\\\\
1&1&1&1
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}.
$$

(a) Berechnen Sie $\\det A$ und bestimmen Sie alle $t\\in\\mathbb R$, für die $A$ invertierbar ist.

(b) Berechnen Sie für $t=0$ die inverse Matrix von $A$.""",
        "zh_problem": """设 $t\\in\\mathbb R$，并给定参数矩阵

$$
A=
\\begin{pmatrix}
1&0&0&t\\\\
1&0&1&t\\\\
1&0&t&1\\\\
1&1&1&1
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}.
$$

(a) 计算 $\\det A$，并求出所有使 $A$ 可逆的 $t\\in\\mathbb R$。

(b) 当 $t=0$ 时，计算 $A^{-1}$。""",
        "solution": """Lösung:

Ad (a): Entwicklung nach der zweiten Spalte liefert

$$
\\det A=1-t.
$$

Eine quadratische Matrix ist genau dann invertierbar, wenn ihre Determinante ungleich Null ist. Also

$$
A\\text{ invertierbar}
\\Longleftrightarrow
1-t\\ne0
\\Longleftrightarrow
t\\ne1.
$$

Ad (b): Für $t=0$ ist

$$
A_0=
\\begin{pmatrix}
1&0&0&0\\\\
1&0&1&0\\\\
1&0&0&1\\\\
1&1&1&1
\\end{pmatrix}.
$$

Mit Gauß-Jordan:

$$
(A_0\\mid I_4)\\sim(I_4\\mid A_0^{-1}).
$$

Das Ergebnis ist

$$
A_0^{-1}=
\\begin{pmatrix}
1&0&0&0\\\\
1&-1&-1&1\\\\
-1&1&0&0\\\\
-1&0&1&0
\\end{pmatrix}.
$$

Probe:

$$
A_0A_0^{-1}=I_4.
$$""",
        "zh_solution": """核心考点：**参数行列式、可逆判定、增广矩阵求逆**。

先算行列式。原卷使用按第二列展开，因为第二列只有最后一个元素为 $1$，计算最省力：

$$
\\det A=1-t.
$$

可逆条件是行列式非零：

$$
A\\text{ 可逆}
\\Longleftrightarrow
\\det A\\ne0
\\Longleftrightarrow
1-t\\ne0
\\Longleftrightarrow
t\\ne1.
$$

当 $t=0$ 时，

$$
A_0=
\\begin{pmatrix}
1&0&0&0\\\\
1&0&1&0\\\\
1&0&0&1\\\\
1&1&1&1
\\end{pmatrix}.
$$

用增广矩阵法：

$$
(A_0\\mid I_4)\\sim(I_4\\mid A_0^{-1}).
$$

得到

$$
A_0^{-1}=
\\begin{pmatrix}
1&0&0&0\\\\
1&-1&-1&1\\\\
-1&1&0&0\\\\
-1&0&1&0
\\end{pmatrix}.
$$

验算：

$$
A_0A_0^{-1}=I_4.
$$

解题思路：参数矩阵先算 $\det A(t)$，不要一开始就求逆。只有在 $t=0$ 这个具体值下，才把矩阵代入并做 Gauss-Jordan 求逆。""",
    },
    ("ss17", 4): {
        "problem": """Gegeben seien $a,b\\in\\mathbb R$ und

$$
A=
\\begin{pmatrix}
1&1&a&b\\\\
1&1&b&a\\\\
a&b&1&1
\\end{pmatrix}
\\in\\mathbb R^{3\\times4}.
$$

Berechnen Sie $\\operatorname{rang}(A)$ in Abhängigkeit von $a,b\\in\\mathbb R$.""",
        "zh_problem": """设 $a,b\\in\\mathbb R$，并给定矩阵

$$
A=
\\begin{pmatrix}
1&1&a&b\\\\
1&1&b&a\\\\
a&b&1&1
\\end{pmatrix}
\\in\\mathbb R^{3\\times4}.
$$

按参数 $a,b$ 讨论并计算 $\\operatorname{rang}(A)$。""",
        "solution": """Lösung:

Elementare Zeilenumformungen ändern den Rang nicht. Wir formen um:

$$
\\begin{pmatrix}
1&1&a&b\\\\
1&1&b&a\\\\
a&b&1&1
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&1&a&b\\\\
0&0&b-a&a-b\\\\
0&b-a&1-a^2&1-ab
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&1&a&b\\\\
0&b-a&1-a^2&1-ab\\\\
0&0&b-a&a-b
\\end{pmatrix}.
$$

Falls $a\\ne b$, gibt es drei Stufen. Also

$$
\\operatorname{rang}(A)=3.
$$

Falls $a=b$, wird die Stufenform zu

$$
\\begin{pmatrix}
1&1&a&a\\\\
0&0&1-a^2&1-a^2\\\\
0&0&0&0
\\end{pmatrix}.
$$

Ist $a=b$ und $a\\notin\\{-1,1\\}$, dann ist $1-a^2\\ne0$, also

$$
\\operatorname{rang}(A)=2.
$$

Ist $a=b\\in\\{-1,1\\}$, dann ist $1-a^2=0$, also bleibt nur eine nichtverschwindende Zeile:

$$
\\operatorname{rang}(A)=1.
$$

Zusammengefasst:

$$
\\operatorname{rang}(A)=
\\begin{cases}
3, & a\\ne b,\\\\
2, & a=b\\text{ und }a\\notin\\{-1,1\\},\\\\
1, & a=b\\in\\{-1,1\\}.
\\end{cases}
$$""",
        "zh_solution": """核心考点：**参数矩阵的秩、行化简、分类讨论**。

做秩题最稳的方法是行化简。对

$$
A=
\\begin{pmatrix}
1&1&a&b\\\\
1&1&b&a\\\\
a&b&1&1
\\end{pmatrix}
$$

做初等行变换，原卷的化简思路是：

$$
A\\sim
\\begin{pmatrix}
1&1&a&b\\\\
0&b-a&1-a^2&1-ab\\\\
0&0&b-a&a-b
\\end{pmatrix}.
$$

现在看关键因子 $b-a$。

第一种情况：如果

$$
a\\ne b,
$$

则 $b-a\\ne0$，第二行和第三行都能提供主元，所以有三阶：

$$
\\operatorname{rang}(A)=3.
$$

第二种情况：如果

$$
a=b,
$$

则矩阵化成

$$
\\begin{pmatrix}
1&1&a&a\\\\
0&0&1-a^2&1-a^2\\\\
0&0&0&0
\\end{pmatrix}.
$$

如果 $a\\notin\\{-1,1\\}$，则 $1-a^2\\ne0$，有两条非零行：

$$
\\operatorname{rang}(A)=2.
$$

如果 $a\\in\\{-1,1\\}$，则 $1-a^2=0$，只剩第一行非零：

$$
\\operatorname{rang}(A)=1.
$$

最终答案：

$$
\\operatorname{rang}(A)=
\\begin{cases}
3, & a\\ne b,\\\\
2, & a=b\\text{ 且 }a\\notin\\{-1,1\\},\\\\
1, & a=b\\in\\{-1,1\\}.
\\end{cases}
$$

解题思路：参数秩题的关键不是把每个参数都代入，而是行化简后盯住会变成 $0$ 的因子。这里先分 $a\\ne b$ 和 $a=b$，再在 $a=b$ 中继续看 $1-a^2$。""",
    },
    ("ss18", 3): {
        "problem": """Gegeben seien $t\\in\\mathbb R$ und

$$
A=
\\begin{pmatrix}
1&1&0&1\\\\
t&0&1&1\\\\
t&1&0&0\\\\
0&1&1&0
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}.
$$

(a) Berechnen Sie $\\det A$ und bestimmen Sie alle $t\\in\\mathbb R$, für die $A$ invertierbar ist.

(b) Berechnen Sie für $t=0$ die inverse Matrix von $A$.""",
        "zh_problem": """设 $t\\in\\mathbb R$，并给定

$$
A=
\\begin{pmatrix}
1&1&0&1\\\\
t&0&1&1\\\\
t&1&0&0\\\\
0&1&1&0
\\end{pmatrix}
\\in\\mathbb R^{4\\times4}.
$$

(a) 计算 $\\det A$，并求所有使 $A$ 可逆的 $t$。

(b) 当 $t=0$ 时，求 $A^{-1}$。""",
        "solution": """Lösung:

Ad (a): Durch elementare Zeilen- und Spaltenumformungen, die den Wert der Determinante nicht ändern, erhält man

$$
\\det A=1-3t.
$$

Also

$$
A\\text{ invertierbar}
\\Longleftrightarrow
1-3t\\ne0
\\Longleftrightarrow
t\\ne\\frac13.
$$

Ad (b): Für $t=0$ ist

$$
A_0=
\\begin{pmatrix}
1&1&0&1\\\\
0&0&1&1\\\\
0&1&0&0\\\\
0&1&1&0
\\end{pmatrix}.
$$

Gauß-Jordan liefert

$$
A_0^{-1}=
\\begin{pmatrix}
1&-1&-2&1\\\\
0&0&1&0\\\\
0&0&-1&1\\\\
0&1&1&-1
\\end{pmatrix}.
$$

Probe:

$$
A_0A_0^{-1}=I_4.
$$""",
        "zh_solution": """核心考点：**参数行列式、可逆参数、具体逆矩阵**。

先算行列式。原卷用不改变行列式的行列变换化简，结果是

$$
\\det A=1-3t.
$$

所以

$$
A\\text{ 可逆}
\\Longleftrightarrow
\\det A\\ne0
\\Longleftrightarrow
1-3t\\ne0
\\Longleftrightarrow
t\\ne\\frac13.
$$

当 $t=0$ 时，

$$
A_0=
\\begin{pmatrix}
1&1&0&1\\\\
0&0&1&1\\\\
0&1&0&0\\\\
0&1&1&0
\\end{pmatrix}.
$$

对 $(A_0\\mid I_4)$ 做 Gauss-Jordan，得到

$$
A_0^{-1}=
\\begin{pmatrix}
1&-1&-2&1\\\\
0&0&1&0\\\\
0&0&-1&1\\\\
0&1&1&-1
\\end{pmatrix}.
$$

验算：

$$
A_0A_0^{-1}=I_4.
$$

解题思路：这题和 `ss17 Aufgabe 3` 同型。参数部分只决定“什么时候可逆”；求逆只在 $t=0$ 的具体矩阵上做，不要试图求一般 $t$ 的逆。""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss19-2", 5): {
        "problem": """Seien $n\\in\\mathbb N$ und $M\\in\\mathbb R^{n\\times n}$ mit

$$
M^2=-M.
$$

Man zeige:

(a) Ist $M$ invertierbar, dann gilt $M=-I_n$.

(b) $I_n+2M$ ist invertierbar.

(c) Ist $A\\in\\mathbb R^{n\\times n}$ orthogonal und symmetrisch, dann erfüllt

$$
B:=\\frac12(A-I_n)
$$

die Gleichung $B^2=-B$.

(d) $\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M)$.

(e) $\\operatorname{rang}(I_n+M)\\le n-\\operatorname{rang}(M)$.

(f) Ist $M\\ne0$, dann ist $I_n+M$ nicht invertierbar.""",
        "zh_problem": """设 $n\\in\\mathbb N$，$M\\in\\mathbb R^{n\\times n}$，并且

$$
M^2=-M.
$$

证明：

(a) 如果 $M$ 可逆，则 $M=-I_n$。

(b) $I_n+2M$ 可逆。

(c) 如果 $A\\in\\mathbb R^{n\\times n}$ 既是正交矩阵（orthogonal）又是对称矩阵（symmetrisch），则

$$
B:=\\frac12(A-I_n)
$$

满足 $B^2=-B$。

(d) $\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M)$。

(e) $\\operatorname{rang}(I_n+M)\\le n-\\operatorname{rang}(M)$。

(f) 如果 $M\\ne0$，则 $I_n+M$ 不可逆。""",
        "solution": """Lösung:

(a) Ist $M$ invertierbar, so dürfen wir $M^2=-M$ rechts mit $M^{-1}$ multiplizieren:

$$
M^2M^{-1}=-MM^{-1}.
$$

Damit folgt

$$
M=-I_n.
$$

(b) Wir berechnen das Quadrat:

$$
(I_n+2M)^2
=I_n+4M+4M^2
=I_n+4M+4(-M)
=I_n.
$$

Also ist $I_n+2M$ invertierbar und

$$
(I_n+2M)^{-1}=I_n+2M.
$$

(c) Ist $A$ orthogonal, so gilt $A^TA=I_n$. Ist $A$ zusätzlich symmetrisch, so ist $A^T=A$. Daher

$$
A^2=I_n.
$$

Für $B=\\frac12(A-I_n)$ gilt

$$
B^2
=\\frac14(A-I_n)^2
=\\frac14(A^2-2A+I_n)
=\\frac14(I_n-2A+I_n)
=\\frac12(I_n-A)
=-\\frac12(A-I_n)
=-B.
$$

(d) Sei $y\\in\\operatorname{Bild}(M)$. Dann gibt es ein $x\\in\\mathbb R^n$ mit $y=Mx$. Also

$$
(I_n+M)y
=(I_n+M)Mx
=(M+M^2)x
=(M-M)x
=0.
$$

Damit ist $y\\in\\ker(I_n+M)$, also

$$
\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M).
$$

(e) Aus dem Rangsatz für $I_n+M$ folgt

$$
n=\\operatorname{rang}(I_n+M)+\\dim\\ker(I_n+M).
$$

Wegen (d) gilt

$$
\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M),
$$

also

$$
\\operatorname{rang}(M)=\\dim\\operatorname{Bild}(M)
\\le\\dim\\ker(I_n+M).
$$

Daher

$$
\\operatorname{rang}(I_n+M)
=n-\\dim\\ker(I_n+M)
\\le n-\\operatorname{rang}(M).
$$

(f) Ist $M\\ne0$, dann ist $\\operatorname{rang}(M)\\ge1$. Mit (e) folgt

$$
\\operatorname{rang}(I_n+M)\\le n-1<n.
$$

Also hat $I_n+M$ keinen vollen Rang und ist nicht invertierbar.""",
        "zh_solution": """核心考点：**矩阵方程、可逆性、正交对称矩阵、像与核、秩-零化度公式**。

(a) 题目给出

$$
M^2=-M.
$$

如果 $M$ 可逆，就可以右乘 $M^{-1}$：

$$
M^2M^{-1}=-MM^{-1}.
$$

左边化为 $M$，右边化为 $-I_n$，所以

$$
M=-I_n.
$$

(b) 要证明 $I_n+2M$ 可逆，最直接是猜它自己的逆。计算：

$$
(I_n+2M)^2
=I_n+4M+4M^2.
$$

代入 $M^2=-M$：

$$
I_n+4M+4(-M)=I_n.
$$

所以

$$
(I_n+2M)^{-1}=I_n+2M.
$$

(c) $A$ 正交说明

$$
A^TA=I_n.
$$

$A$ 对称说明

$$
A^T=A.
$$

合起来得到

$$
A^2=I_n.
$$

令

$$
B=\\frac12(A-I_n).
$$

则

$$
B^2
=\\frac14(A-I_n)^2
=\\frac14(A^2-2A+I_n).
$$

代入 $A^2=I_n$：

$$
B^2
=\\frac14(2I_n-2A)
=\\frac12(I_n-A)
=-\\frac12(A-I_n)
=-B.
$$

(d) 要证明像空间包含于核空间，就从任意像空间元素出发。取

$$
y\\in\\operatorname{Bild}(M).
$$

则存在 $x$ 使得

$$
y=Mx.
$$

于是

$$
(I_n+M)y
=(I_n+M)Mx
=(M+M^2)x.
$$

由于 $M^2=-M$，

$$
(M+M^2)x=(M-M)x=0.
$$

所以 $y\\in\\ker(I_n+M)$，即

$$
\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M).
$$

(e) 对线性映射 $I_n+M$ 使用维数公式：

$$
n=\\operatorname{rang}(I_n+M)+\\dim\\ker(I_n+M).
$$

由 (d) 知道

$$
\\operatorname{Bild}(M)\\subseteq\\ker(I_n+M),
$$

所以

$$
\\operatorname{rang}(M)=\\dim\\operatorname{Bild}(M)
\\le\\dim\\ker(I_n+M).
$$

因此

$$
\\operatorname{rang}(I_n+M)
=n-\\dim\\ker(I_n+M)
\\le n-\\operatorname{rang}(M).
$$

(f) 如果 $M\\ne0$，那么至少有一列非零，所以

$$
\\operatorname{rang}(M)\ge1.
$$

由 (e) 得

$$
\\operatorname{rang}(I_n+M)\le n-1<n.
$$

一个 $n\\times n$ 矩阵可逆必须满秩；现在 $I_n+M$ 不满秩，所以不可逆。

解题思路：这道题的主线是 $M^2=-M$。它让 $M+M^2=0$，所以能把像空间压进核空间；再用维数公式把“包含关系”变成“秩不等式”。""",
    },
})


KAOSHI = chr(0x8003) + chr(0x8bd5)

MANUAL_OVERRIDES.update({
    ("ss20", 3): {
        "problem": """Seien $n\\in\\mathbb N$ und $b,c\\in\\mathbb R^n$. Betrachten Sie die Abbildung

$$
f:\\mathbb R^{n+1}\\to\\mathbb R^{n+1},\qquad
f\\begin{pmatrix}x\\\\ \\xi\\end{pmatrix}
=
\\begin{pmatrix}
x-\\xi b\\\\
c^Tx+\\xi
\\end{pmatrix},
$$

wobei $x\\in\\mathbb R^n$ und $\\xi\\in\\mathbb R$.

(a) Zeigen Sie: $f$ ist linear.

(b) Bestimmen Sie die darstellende Matrix $M$ von $f$ in Blockmatrixschreibweise.

(c) Berechnen Sie $\\operatorname{rang}M$ und $\\det M$ in Abhängigkeit von $b$ und $c$.

(d) Geben Sie $\\dim\\ker f$ in Abhängigkeit von $b$ und $c$ an.

(e) Berechnen Sie $\\ker f$ in Abhängigkeit von $b$ und $c$.""",
        "zh_problem": """设 $n\\in\\mathbb N$，$b,c\\in\\mathbb R^n$。考虑映射

$$
f:\\mathbb R^{n+1}\\to\\mathbb R^{n+1},\qquad
f\\begin{pmatrix}x\\\\ \\xi\\end{pmatrix}
=
\\begin{pmatrix}
x-\\xi b\\\\
c^Tx+\\xi
\\end{pmatrix},
$$

其中 $x\\in\\mathbb R^n$，$\\xi\\in\\mathbb R$。

(a) 证明 $f$ 是线性映射（lineare Abbildung）。

(b) 用分块矩阵写出 $f$ 的表示矩阵 $M$。

(c) 根据 $b,c$ 计算 $\\operatorname{rang}M$ 和 $\\det M$。

(d) 根据 $b,c$ 给出 $\\dim\\ker f$。

(e) 根据 $b,c$ 计算 $\\ker f$。""",
        "solution": """Lösung:

(a) Beide Komponenten von $f$ sind linear in $(x,\\xi)$. Für $\\lambda,\\mu\\in\\mathbb R$ und $u,v\\in\\mathbb R^{n+1}$ gilt daher

$$
f(\\lambda u+\\mu v)=\\lambda f(u)+\\mu f(v).
$$

Also ist $f$ linear.

(b) Aus

$$
f\\begin{pmatrix}x\\\\ \\xi\\end{pmatrix}
=
\\begin{pmatrix}
I_n&-b\\\\
c^T&1
\\end{pmatrix}
\\begin{pmatrix}x\\\\ \\xi\\end{pmatrix}
$$

folgt

$$
M=
\\begin{pmatrix}
I_n&-b\\\\
c^T&1
\\end{pmatrix}.
$$

(c) Mit der Schur-Komplement-Formel, da $I_n$ invertierbar ist:

$$
\\det M
=\\det(I_n)\\bigl(1-c^T I_n^{-1}(-b)\\bigr)
=1+c^Tb.
$$

Da die ersten $n$ Spalten wegen des Blocks $I_n$ linear unabhängig sind, gilt immer $\\operatorname{rang}M\\ge n$. Also

$$
\\operatorname{rang}M=
\\begin{cases}
n+1,&1+c^Tb\\ne0,\\\\
n,&1+c^Tb=0.
\\end{cases}
$$

(d)

$$
\\dim\\ker f=(n+1)-\\operatorname{rang}M
=
\\begin{cases}
0,&1+c^Tb\\ne0,\\\\
1,&1+c^Tb=0.
\\end{cases}
$$

(e) Löse $M\\binom{x}{\\xi}=0$. Aus der oberen Blockzeile folgt

$$
x-\\xi b=0,
$$

also $x=\\xi b$. Die letzte Zeile ergibt

$$
c^Tx+\\xi=\\xi(c^Tb+1)=0.
$$

Damit

$$
\\ker f=
\\begin{cases}
\\{0\\},&1+c^Tb\\ne0,\\\\
\\operatorname{span}\\left\\{\\begin{pmatrix}b\\\\1\\end{pmatrix}\\right\\},&1+c^Tb=0.
\\end{cases}
$$""",
        "zh_solution": """核心考点：**分块矩阵、Schur 补、秩-零化度公式、核空间**。

先看线性性。$x-\\xi b$ 对 $x$ 和 $\\xi$ 都是线性的，$c^Tx+\\xi$ 也是线性的，所以整个 $f$ 是线性映射。

把输入写成

$$
\\begin{pmatrix}x\\\\ \\xi\\end{pmatrix}.
$$

上半部分 $x-\\xi b$ 对应矩阵块 $I_n$ 和 $-b$；下半部分 $c^Tx+\\xi$ 对应矩阵块 $c^T$ 和 $1$。因此

$$
M=
\\begin{pmatrix}
I_n&-b\\\\
c^T&1
\\end{pmatrix}.
$$

因为左上角 $I_n$ 可逆，用 Schur 补：

$$
\\det M
=\\det(I_n)\\left(1-c^TI_n^{-1}(-b)\\right)
=1+c^Tb.
$$

前 $n$ 列含有 $I_n$，所以至少有 $n$ 个线性无关列。如果 $1+c^Tb\\ne0$，矩阵可逆，秩为 $n+1$；如果 $1+c^Tb=0$，行列式为零但前 $n$ 列仍独立，秩为 $n$：

$$
\\operatorname{rang}M=
\\begin{cases}
n+1,&1+c^Tb\\ne0,\\\\
n,&1+c^Tb=0.
\\end{cases}
$$

由维数公式

$$
\\dim\\ker f=(n+1)-\\operatorname{rang}M
$$

得到

$$
\\dim\\ker f=
\\begin{cases}
0,&1+c^Tb\\ne0,\\\\
1,&1+c^Tb=0.
\\end{cases}
$$

最后直接解核。方程 $M\\binom{x}{\\xi}=0$ 的上半部分给出

$$
x=\\xi b.
$$

代入最后一行：

$$
c^Tx+\\xi=\\xi(c^Tb+1)=0.
$$

所以

$$
\\ker f=
\\begin{cases}
\\{0\\},&1+c^Tb\\ne0,\\\\
\\operatorname{span}\\left\\{\\begin{pmatrix}b\\\\1\\end{pmatrix}\\right\\},&1+c^Tb=0.
\\end{cases}
$$""",
    },
    ("ss21", 3): {
        "problem": """Seien $n\\in\\mathbb N$, $n\\ge5$, und $a,b\\in\\mathbb R$. Betrachten Sie $f:\\mathbb R^n\\to\\mathbb R^n$ mit

$$
f_i(x)=
\\begin{cases}
a(x_1+x_n)+\\displaystyle\\sum_{j=2}^{n-1}x_j,& i=1\\text{ oder }i=n,\\\\
b(x_1+x_n)+\\displaystyle\\sum_{j=2}^{n-1}x_j,& i\\in\\{2,\\ldots,n-1\\}.
\\end{cases}
$$

(a) Zeigen Sie, dass $f$ linear ist.

(b) Geben Sie die darstellende Matrix $M$ für $n=5$ an.

(c) Bestimmen Sie den Rang von $M$ in Abhängigkeit von $n,a,b$.

(d) Sei $a\\ne b$. Zeigen Sie, dass

$$
e_1-e_n,\\ e_2-e_3,\\ e_2-e_4,\\ldots,e_2-e_{n-1}
$$

eine Basis von $\\ker f$ ist.""",
        "zh_problem": """设 $n\\in\\mathbb N$，$n\\ge5$，$a,b\\in\\mathbb R$。定义 $f:\\mathbb R^n\\to\\mathbb R^n$：

$$
f_i(x)=
\\begin{cases}
a(x_1+x_n)+\\displaystyle\\sum_{j=2}^{n-1}x_j,& i=1\\text{ 或 }i=n,\\\\
b(x_1+x_n)+\\displaystyle\\sum_{j=2}^{n-1}x_j,& i\\in\\{2,\\ldots,n-1\\}.
\\end{cases}
$$

(a) 证明 $f$ 是线性的。

(b) 写出 $n=5$ 时的表示矩阵 $M$。

(c) 根据 $n,a,b$ 求 $\\operatorname{rang}M$。

(d) 若 $a\\ne b$，证明

$$
e_1-e_n,\\ e_2-e_3,\\ e_2-e_4,\\ldots,e_2-e_{n-1}
$$

是 $\\ker f$ 的一组基。""",
        "solution": """Lösung:

(a) Jede Komponente von $f$ ist eine lineare Kombination der Koordinaten $x_1,\ldots,x_n$. Also ist $f$ linear.

(b) Für $n=5$ ist

$$
M=
\\begin{pmatrix}
a&1&1&1&a\\\\
b&1&1&1&b\\\\
b&1&1&1&b\\\\
b&1&1&1&b\\\\
a&1&1&1&a
\\end{pmatrix}.
$$

(c) Die Zeilen von $M$ sind nur von zwei Typen:

$$
r_a=(a,1,\ldots,1,a),\qquad r_b=(b,1,\ldots,1,b).
$$

Falls $a=b$, sind alle Zeilen gleich und nicht null. Daher

$$
\\operatorname{rang}M=1.
$$

Falls $a\\ne b$, sind $r_a$ und $r_b$ linear unabhängig, denn

$$
r_a-r_b=(a-b)(e_1^T+e_n^T)\\ne0
$$

und $r_b$ besitzt Einträge $1$ in den mittleren Koordinaten. Also

$$
\\operatorname{rang}M=2.
$$

(d) Für $a\\ne b$ hat $\\ker f$ die Dimension $n-2$. Die angegebenen Vektoren sind $n-2$ Stück. Sie liegen im Kern, denn bei $e_1-e_n$ ist $x_1+x_n=0$ und alle mittleren Koordinaten sind null; bei $e_2-e_j$ ist $x_1+x_n=0$ und die Summe der mittleren Koordinaten ebenfalls null. Also ist jeweils $f(x)=0$.

Die Vektoren sind linear unabhängig: In

$$
\\alpha(e_1-e_n)+\\sum_{j=3}^{n-1}\\beta_j(e_2-e_j)=0
$$

erzwingen die Koordinaten $e_1$ und $e_n$ zunächst $\\alpha=0$, und die Koordinaten $e_3,\ldots,e_{n-1}$ erzwingen alle $\\beta_j=0$. Damit bilden sie eine Basis von $\\ker f$.""",
        "zh_solution": """核心考点：**线性映射矩阵、秩、核空间基**。

每个 $f_i(x)$ 都是坐标 $x_1,\ldots,x_n$ 的线性组合，所以 $f$ 线性。

当 $n=5$ 时，第一行和最后一行使用系数 $a$，中间行使用系数 $b$：

$$
M=
\\begin{pmatrix}
a&1&1&1&a\\\\
b&1&1&1&b\\\\
b&1&1&1&b\\\\
b&1&1&1&b\\\\
a&1&1&1&a
\\end{pmatrix}.
$$

一般 $n$ 时，矩阵只有两种行：

$$
r_a=(a,1,\ldots,1,a),\qquad r_b=(b,1,\ldots,1,b).
$$

若 $a=b$，两种行相同，且行不为零，所以

$$
\\operatorname{rang}M=1.
$$

若 $a\\ne b$，则 $r_a-r_b=(a-b)(e_1^T+e_n^T)$ 非零，并且与 $r_b$ 不成比例，所以行空间维数为 $2$：

$$
\\operatorname{rang}M=2.
$$

当 $a\\ne b$ 时，

$$
\\dim\\ker f=n-2.
$$

题目给出的向量共有 $n-2$ 个。对 $e_1-e_n$，有 $x_1+x_n=0$，中间坐标和为 $0$；对 $e_2-e_j$，同样 $x_1+x_n=0$，且中间坐标和 $1-1=0$。因此它们都在核中。

再看线性无关：

$$
\\alpha(e_1-e_n)+\\sum_{j=3}^{n-1}\\beta_j(e_2-e_j)=0.
$$

看第 $1$ 和第 $n$ 个坐标得到 $\\alpha=0$；再看第 $3,\ldots,n-1$ 个坐标得到所有 $\\beta_j=0$。所以这些向量线性无关。数量正好等于核的维数，因此它们构成 $\\ker f$ 的一组基。""",
    },
    ("ss17", 8): {
        "problem": """Seien $n\\in\\mathbb N$, $n\\ge2$, und $e_1,\ldots,e_n$ die Einheitsvektoren von $\\mathbb R^n$. Sei

$$
A=(e_1+e_n)(e_1+e_n)^T\\in\\mathbb R^{n\\times n}.
$$

(a) Geben Sie $A$ für $n=2,3,4$ explizit an.

(b) Zeigen Sie direkt aus der Definition, dass $A$ symmetrisch ist.

(c) Zeigen Sie, dass $v=e_1+e_n$ Eigenvektor von $A=vv^T$ ist, und geben Sie den Eigenwert an.

(d) Zeigen Sie: Für alle $u\\in\\mathbb R^n$ gilt $u\\perp v\\Rightarrow Au=0$.

(e) Zeigen Sie, dass auch $0$ Eigenwert von $A$ ist und dass $A$ keine weiteren Eigenwerte hat.""",
        "zh_problem": """设 $n\\in\\mathbb N$，$n\\ge2$，$e_1,\ldots,e_n$ 是 $\\mathbb R^n$ 的标准单位向量。定义

$$
A=(e_1+e_n)(e_1+e_n)^T\\in\\mathbb R^{n\\times n}.
$$

(a) 分别写出 $n=2,3,4$ 时的矩阵 $A$。

(b) 直接由定义证明 $A$ 是对称矩阵。

(c) 令 $v=e_1+e_n$，证明 $v$ 是 $A=vv^T$ 的特征向量，并给出对应特征值。

(d) 证明：对所有 $u\\in\\mathbb R^n$，若 $u\\perp v$，则 $Au=0$。

(e) 证明 $0$ 也是 $A$ 的特征值，并说明 $A$ 没有其它特征值。""",
        "solution": """Lösung:

(a)

$$
n=2:\\quad A=\\begin{pmatrix}1&1\\\\1&1\\end{pmatrix},
$$

$$
n=3:\\quad A=\\begin{pmatrix}1&0&1\\\\0&0&0\\\\1&0&1\\end{pmatrix},
$$

$$
n=4:\\quad A=\\begin{pmatrix}1&0&0&1\\\\0&0&0&0\\\\0&0&0&0\\\\1&0&0&1\\end{pmatrix}.
$$

(b) Mit $v=e_1+e_n$ gilt $A=vv^T$. Daher

$$
A^T=(vv^T)^T=vv^T=A.
$$

(c)

$$
Av=vv^Tv=v(v^Tv).
$$

Da $v=e_1+e_n$ die Normquadratsumme $v^Tv=2$ hat, folgt

$$
Av=2v.
$$

Also ist $v$ Eigenvektor zum Eigenwert $2$.

(d) Ist $u\\perp v$, dann gilt $v^Tu=0$. Also

$$
Au=vv^Tu=v(v^Tu)=0.
$$

(e) Da $v^\\perp$ nichttrivial ist, gibt es $u\\ne0$ mit $u\\perp v$. Nach (d) gilt $Au=0$, also ist $0$ Eigenwert. Jeder Vektor $x\\in\\mathbb R^n$ zerfällt in einen Anteil in $\\operatorname{span}(v)$ und einen Anteil in $v^\\perp$. Auf $\\operatorname{span}(v)$ wirkt $A$ mit Eigenwert $2$, auf $v^\\perp$ mit Eigenwert $0$. Daher gibt es keine weiteren Eigenwerte.""",
        "zh_solution": """核心考点：**秩一矩阵、对称矩阵、特征值、正交补**。

令

$$
v=e_1+e_n.
$$

则

$$
A=vv^T.
$$

当 $n=2$：

$$
A=\\begin{pmatrix}1&1\\\\1&1\\end{pmatrix}.
$$

当 $n=3$：

$$
A=\\begin{pmatrix}1&0&1\\\\0&0&0\\\\1&0&1\\end{pmatrix}.
$$

当 $n=4$：

$$
A=\\begin{pmatrix}1&0&0&1\\\\0&0&0&0\\\\0&0&0&0\\\\1&0&0&1\\end{pmatrix}.
$$

对称性直接来自转置公式：

$$
A^T=(vv^T)^T=vv^T=A.
$$

计算 $Av$：

$$
Av=vv^Tv=v(v^Tv).
$$

因为

$$
v^Tv=\\|e_1+e_n\\|^2=2,
$$

所以

$$
Av=2v.
$$

因此 $v$ 是特征向量，特征值是 $2$。

若 $u\\perp v$，则 $v^Tu=0$，于是

$$
Au=vv^Tu=v(v^Tu)=0.
$$

所以所有 $v^\\perp$ 中的非零向量都是特征值 $0$ 的特征向量。因为 $\\mathbb R^n=\\operatorname{span}(v)\\oplus v^\\perp$，矩阵在这两个方向上只分别给出特征值 $2$ 和 $0$，没有其它特征值。""",
    },
    ("ss22"+KAOSHI+"1", 1): {
        "problem": """Berechnen Sie die Kleinste-Quadrate-Lösung zum System $Ax=b$ mit

$$
A=\\begin{pmatrix}
2&-2\\\\
1&1\\\\
3&1
\\end{pmatrix},
\\qquad
b=\\begin{pmatrix}
2\\\\-1\\\\1
\\end{pmatrix}.
$$""",
        "zh_problem": """计算线性系统 $Ax=b$ 的最小二乘解（Kleinste-Quadrate-Lösung），其中

$$
A=\\begin{pmatrix}
2&-2\\\\
1&1\\\\
3&1
\\end{pmatrix},
\\qquad
b=\\begin{pmatrix}
2\\\\-1\\\\1
\\end{pmatrix}.
$$""",
        "solution": """Lösung:

Die Normalgleichung lautet

$$
A^TA\\hat x=A^Tb.
$$

Wir berechnen

$$
A^TA=
\\begin{pmatrix}
14&0\\\\
0&6
\\end{pmatrix},
\\qquad
A^Tb=
\\begin{pmatrix}
6\\\\-4
\\end{pmatrix}.
$$

Also

$$
\\begin{pmatrix}
14&0\\\\
0&6
\\end{pmatrix}
\\hat x=
\\begin{pmatrix}
6\\\\-4
\\end{pmatrix}.
$$

Daraus folgt

$$
\\hat x=
\\begin{pmatrix}
\\frac37\\\\
-\\frac23
\\end{pmatrix}.
$$""",
        "zh_solution": """核心考点：**最小二乘、法方程**。

最小二乘解不一定满足 $Ax=b$，而是满足法方程：

$$
A^TA\\hat x=A^Tb.
$$

先算

$$
A^TA=
\\begin{pmatrix}
14&0\\\\
0&6
\\end{pmatrix},
\\qquad
A^Tb=
\\begin{pmatrix}
6\\\\-4
\\end{pmatrix}.
$$

所以

$$
\\begin{pmatrix}
14&0\\\\
0&6
\\end{pmatrix}
\\hat x=
\\begin{pmatrix}
6\\\\-4
\\end{pmatrix}.
$$

直接读出

$$
14\\hat x_1=6,\qquad 6\\hat x_2=-4.
$$

因此

$$
\\hat x=
\\begin{pmatrix}
\\frac37\\\\
-\\frac23
\\end{pmatrix}.
$$""",
    },
    ("ss22"+KAOSHI+"2", 1): {
        "problem": """Finden Sie eine Orthogonalmatrix $P$, welche

$$
A=\\begin{pmatrix}3&1\\\\1&3\\end{pmatrix}
$$

diagonalisiert.""",
        "zh_problem": """求一个正交矩阵（Orthogonalmatrix）$P$，使

$$
A=\\begin{pmatrix}3&1\\\\1&3\\end{pmatrix}
$$

被对角化。""",
        "solution": """Lösung:

Das charakteristische Polynom ist

$$
\\det(A-\\lambda I)=(3-\\lambda)^2-1
=\\lambda^2-6\\lambda+8.
$$

Also sind die Eigenwerte

$$
\\lambda_1=2,\qquad \\lambda_2=4.
$$

Zu $\\lambda_1=2$ gehört ein Eigenvektor

$$
v_1=\\begin{pmatrix}-1\\\\1\\end{pmatrix}.
$$

Zu $\\lambda_2=4$ gehört ein Eigenvektor

$$
v_2=\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

Die beiden Vektoren sind orthogonal. Nach Normierung:

$$
u_1=\\frac1{\\sqrt2}\\begin{pmatrix}-1\\\\1\\end{pmatrix},
\\qquad
u_2=\\frac1{\\sqrt2}\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

Damit kann man wählen

$$
P=
\\frac1{\\sqrt2}
\\begin{pmatrix}
-1&1\\\\
1&1
\\end{pmatrix},
\\qquad
D=
\\begin{pmatrix}
2&0\\\\
0&4
\\end{pmatrix},
$$

und es gilt

$$
P^TAP=D.
$$""",
        "zh_solution": """核心考点：**实对称矩阵的正交对角化**。

先求特征值：

$$
\\det(A-\\lambda I)
=\\det\\begin{pmatrix}3-\\lambda&1\\\\1&3-\\lambda\\end{pmatrix}
=(3-\\lambda)^2-1.
$$

所以

$$
\\lambda^2-6\\lambda+8=0,
$$

得到

$$
\\lambda_1=2,\qquad \\lambda_2=4.
$$

对 $\\lambda=2$，可取特征向量

$$
v_1=\\begin{pmatrix}-1\\\\1\\end{pmatrix}.
$$

对 $\\lambda=4$，可取

$$
v_2=\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

两个向量点积为 $0$，已经正交。单位化：

$$
u_1=\\frac1{\\sqrt2}\\begin{pmatrix}-1\\\\1\\end{pmatrix},
\\qquad
u_2=\\frac1{\\sqrt2}\\begin{pmatrix}1\\\\1\\end{pmatrix}.
$$

把它们作为列向量：

$$
P=\\frac1{\\sqrt2}
\\begin{pmatrix}
-1&1\\\\
1&1
\\end{pmatrix}.
$$

于是

$$
P^TAP=
\\begin{pmatrix}
2&0\\\\
0&4
\\end{pmatrix}.
$$""",
    },
    ("ss24"+KAOSHI, 1): {
        "problem": """Sei

$$
v_1=\\begin{pmatrix}1\\\\2\\\\-3\\end{pmatrix}.
$$

Finden Sie $v_2,v_3$, so dass $\\{v_1,v_2,v_3\\}$ eine Orthogonalbasis von $\\mathbb R^3$ ist.""",
        "zh_problem": """给定

$$
v_1=\\begin{pmatrix}1\\\\2\\\\-3\\end{pmatrix}.
$$

求 $v_2,v_3$，使 $\\{v_1,v_2,v_3\\}$ 成为 $\\mathbb R^3$ 的一组正交基（Orthogonalbasis）。""",
        "solution": """Lösung:

Wir suchen zwei Vektoren, die zu $v_1$ und zueinander orthogonal sind. Eine mögliche Wahl ist

$$
v_2=\\begin{pmatrix}13\\\\-2\\\\3\\end{pmatrix},
\\qquad
v_3=\\begin{pmatrix}0\\\\3\\\\2\\end{pmatrix}.
$$

Prüfung:

$$
v_1^Tv_2=1\\cdot13+2\\cdot(-2)+(-3)\\cdot3=13-4-9=0,
$$

$$
v_1^Tv_3=1\\cdot0+2\\cdot3+(-3)\\cdot2=6-6=0,
$$

$$
v_2^Tv_3=13\\cdot0+(-2)\\cdot3+3\\cdot2=0.
$$

Die drei Vektoren sind nicht null und paarweise orthogonal, also linear unabhängig. Damit bilden sie eine Orthogonalbasis von $\\mathbb R^3$.""",
        "zh_solution": """核心考点：**Gram-Schmidt、正交基**。

题目只要求找出 $v_2,v_3$，不要求单位化。我们可以给出一组简单整数向量：

$$
v_2=\\begin{pmatrix}13\\\\-2\\\\3\\end{pmatrix},
\\qquad
v_3=\\begin{pmatrix}0\\\\3\\\\2\\end{pmatrix}.
$$

检查正交性：

$$
v_1^Tv_2=13-4-9=0,
$$

$$
v_1^Tv_3=6-6=0,
$$

$$
v_2^Tv_3=-6+6=0.
$$

三个非零向量两两正交，因此自动线性无关。在 $\\mathbb R^3$ 中三个线性无关向量就是一组基，所以

$$
\\left\\{
\\begin{pmatrix}1\\\\2\\\\-3\\end{pmatrix},
\\begin{pmatrix}13\\\\-2\\\\3\\end{pmatrix},
\\begin{pmatrix}0\\\\3\\\\2\\end{pmatrix}
\\right\\}
$$

是一组正交基。""",
    },
    ("ss25", 1): {
        "problem": """Sei $W=\\operatorname{span}\\{u_1,u_2\\}$ mit

$$
u_1=\\begin{pmatrix}1\\\\0\\\\1\\end{pmatrix},
\\qquad
u_2=\\begin{pmatrix}1\\\\2\\\\-1\\end{pmatrix}.
$$

Sei

$$
v=\\begin{pmatrix}3\\\\0\\\\2\\end{pmatrix}.
$$

Finden Sie $\\hat v\\in W$ und $z\\in W^\\perp$, so dass $v=\\hat v+z$.""",
        "zh_problem": """设 $W=\\operatorname{span}\\{u_1,u_2\\}$，其中

$$
u_1=\\begin{pmatrix}1\\\\0\\\\1\\end{pmatrix},
\\qquad
u_2=\\begin{pmatrix}1\\\\2\\\\-1\\end{pmatrix}.
$$

给定

$$
v=\\begin{pmatrix}3\\\\0\\\\2\\end{pmatrix}.
$$

求 $\\hat v\\in W$ 和 $z\\in W^\\perp$，使得 $v=\\hat v+z$。""",
        "solution": """Lösung:

Setze

$$
\\hat v=\\alpha u_1+\\beta u_2.
$$

Die Bedingung $z=v-\\hat v\\in W^\\perp$ bedeutet

$$
u_1^T(v-\\hat v)=0,\qquad u_2^T(v-\\hat v)=0.
$$

Mit $U=(u_1\\ u_2)$ erhält man die Normalgleichung

$$
U^TU\\begin{pmatrix}\\alpha\\\\\\beta\\end{pmatrix}=U^Tv.
$$

Es gilt

$$
U^TU=
\\begin{pmatrix}
2&0\\\\
0&6
\\end{pmatrix},
\\qquad
U^Tv=
\\begin{pmatrix}
5\\\\1
\\end{pmatrix}.
$$

Also

$$
\\alpha=\\frac52,\qquad \\beta=\\frac16.
$$

Damit

$$
\\hat v=\\frac52u_1+\\frac16u_2
=\\begin{pmatrix}\\frac83\\\\\\frac13\\\\\\frac73\\end{pmatrix}.
$$

und

$$
z=v-\\hat v
=\\begin{pmatrix}\\frac13\\\\-\\frac13\\\\-\\frac13\\end{pmatrix}.
$$""",
        "zh_solution": """核心考点：**正交投影、误差向量、正规方程**。

投影一定在 $W$ 里，所以先设

$$
\\hat v=\\alpha u_1+\\beta u_2.
$$

误差

$$
z=v-\\hat v
$$

必须垂直于 $W$，只要垂直于 $u_1,u_2$ 即可：

$$
u_1^T(v-\\hat v)=0,\qquad u_2^T(v-\\hat v)=0.
$$

令 $U=(u_1\\ u_2)$，得到正规方程

$$
U^TU\\begin{pmatrix}\\alpha\\\\\\beta\\end{pmatrix}=U^Tv.
$$

计算：

$$
U^TU=
\\begin{pmatrix}
2&0\\\\
0&6
\\end{pmatrix},
\\qquad
U^Tv=
\\begin{pmatrix}
5\\\\1
\\end{pmatrix}.
$$

所以

$$
\\alpha=\\frac52,\qquad \\beta=\\frac16.
$$

于是

$$
\\hat v=\\frac52u_1+\\frac16u_2
=\\begin{pmatrix}\\frac83\\\\\\frac13\\\\\\frac73\\end{pmatrix}.
$$

最后

$$
z=v-\\hat v
=\\begin{pmatrix}\\frac13\\\\-\\frac13\\\\-\\frac13\\end{pmatrix}.
$$

验算：

$$
u_1^Tz=0,\qquad u_2^Tz=0,
$$

所以 $z\\in W^\\perp$。""",
    },
})


PRODUCT_SPACE_PROBLEM_DE = """Seien $V_1,\ldots,V_n$ mit $n\\ge2$ Vektorräume.

(a) Definieren Sie Addition, skalare Multiplikation und den Nullvektor so, dass

$$
V=V_1\\times\\cdots\\times V_n
$$

ein Vektorraum ist.

(b) Zeigen Sie, dass $V_1$ im Allgemeinen kein Untervektorraum von $V$ ist.

(c) Seien $W_i\\le V_i$ Unterräume. Zeigen Sie, dass

$$
W=W_1\\times\\cdots\\times W_n
$$

ein Unterraum von $V$ ist."""

PRODUCT_SPACE_PROBLEM_ZH = """设 $V_1,\ldots,V_n$ 是向量空间，$n\\ge2$。

(a) 定义加法、数乘和零向量，使

$$
V=V_1\\times\\cdots\\times V_n
$$

成为一个向量空间。

(b) 证明 $V_1$ 一般不是 $V$ 的子空间。

(c) 若 $W_i\\le V_i$ 都是子空间，证明

$$
W=W_1\\times\\cdots\\times W_n
$$

是 $V$ 的子空间。"""

PRODUCT_SPACE_SOLUTION_DE = """Lösung:

(a) Für

$$
v=(v_1,\ldots,v_n),\\qquad w=(w_1,\ldots,w_n)
$$

definieren wir

$$
v+w=(v_1+w_1,\ldots,v_n+w_n).
$$

Für $\\lambda\\in\\mathbb R$ definieren wir

$$
\\lambda v=(\\lambda v_1,\ldots,\lambda v_n).
$$

Sind $0_i$ die Nullvektoren von $V_i$, dann ist der Nullvektor von $V$

$$
0_V=(0_1,\ldots,0_n).
$$

(b) Ein Untervektorraum muss zuerst eine Teilmenge des Vektorraums sein. Ein Element von $V_1$ hat die Form $v_1$, ein Element von $V$ hat aber die Form

$$
(v_1,\ldots,v_n).
$$

Ohne zusätzliche Einbettung ist $V_1$ also keine Teilmenge von $V$ und damit kein Untervektorraum von $V$.

(c) Wir prüfen das Unterraumkriterium. Da jedes $W_i$ ein Unterraum ist, gilt $0_i\\in W_i$. Also

$$
(0_1,\ldots,0_n)\\in W.
$$

Seien $w=(w_1,\ldots,w_n)$ und $u=(u_1,\ldots,u_n)$ in $W$. Dann gilt $w_i,u_i\\in W_i$. Weil $W_i$ Unterraum ist, ist $w_i+u_i\\in W_i$. Daher

$$
w+u=(w_1+u_1,\ldots,w_n+u_n)\\in W.
$$

Für $\\lambda\\in\\mathbb R$ gilt außerdem $\\lambda w_i\\in W_i$ für alle $i$. Also

$$
\\lambda w=(\\lambda w_1,\ldots,\lambda w_n)\\in W.
$$

Damit ist $W$ ein Unterraum von $V$."""

PRODUCT_SPACE_SOLUTION_ZH = """核心考点：**直积向量空间、子空间判据、分量化证明**。

(a) 直积空间里的运算按分量定义。对

$$
v=(v_1,\ldots,v_n),\qquad w=(w_1,\ldots,w_n)
$$

定义

$$
v+w=(v_1+w_1,\ldots,v_n+w_n).
$$

对 $\\lambda\\in\\mathbb R$，定义

$$
\\lambda v=(\\lambda v_1,\ldots,\lambda v_n).
$$

如果 $0_i$ 是 $V_i$ 的零向量，那么

$$
0_V=(0_1,\ldots,0_n)
$$

就是 $V$ 的零向量。

(b) 子空间首先必须是母空间的子集。$V_1$ 的元素形如 $v_1$，而 $V=V_1\\times\\cdots\\times V_n$ 的元素形如

$$
(v_1,\ldots,v_n).
$$

两者对象类型不同，所以没有额外嵌入时，$V_1$ 不是 $V$ 的子集，因此不是 $V$ 的子空间。

(c) 用子空间判据。因为每个 $W_i$ 都是 $V_i$ 的子空间，所以 $0_i\\in W_i$，于是

$$
(0_1,\ldots,0_n)\in W.
$$

若

$$
w=(w_1,\ldots,w_n),\qquad u=(u_1,\ldots,u_n)
$$

都在 $W$ 中，则 $w_i,u_i\in W_i$。由于 $W_i$ 对加法封闭，

$$
w_i+u_i\in W_i.
$$

所以

$$
w+u=(w_1+u_1,\ldots,w_n+u_n)\in W.
$$

若 $\\lambda\\in\\mathbb R$，由于每个 $W_i$ 对数乘封闭，

$$
\\lambda w_i\in W_i.
$$

因此

$$
\\lambda w=(\\lambda w_1,\ldots,\lambda w_n)\in W.
$$

零向量、加法封闭、数乘封闭都成立，所以 $W$ 是 $V$ 的子空间。"""

MANUAL_OVERRIDES.update({
    ("ss22"+KAOSHI+"1", 5): {
        "problem": """Sei $n\\ge1$ und sei $V=\\{f:\\mathbb R^n\\to\\mathbb R^2\\}$ der Vektorraum aller Funktionen mit punktweiser Addition und Skalarmultiplikation. Sei

$$
L=\\{f:\\mathbb R^n\\to\\mathbb R^2\\mid f\\text{ linear}\\}.
$$

(a) Sei $\\mathcal B$ eine Basis von $\\mathbb R^{2\\times n}$. Zeigen Sie, dass

$$
\\mathcal L=\\{f_B(x)=Bx\\mid B\\in\\mathcal B\\}
$$

eine Basis von $L$ ist.

(b) Bestimmen Sie $\\dim L$.

(c) Beweisen Sie, dass $L$ ein Untervektorraum von $V$ ist.""",
        "zh_problem": """设 $n\\ge1$，$V=\\{f:\\mathbb R^n\\to\\mathbb R^2\\}$ 是所有函数组成的向量空间，运算为逐点加法和逐点数乘。令

$$
L=\\{f:\\mathbb R^n\\to\\mathbb R^2\\mid f\\text{ 是线性的}\\}.
$$

(a) 设 $\\mathcal B$ 是矩阵空间 $\\mathbb R^{2\\times n}$ 的一组基。证明

$$
\\mathcal L=\\{f_B(x)=Bx\\mid B\\in\\mathcal B\\}
$$

是 $L$ 的一组基。

(b) 求 $\\dim L$。

(c) 证明 $L$ 是 $V$ 的子空间。""",
        "solution": """Lösung:

(a) Jede lineare Abbildung $f:\\mathbb R^n\\to\\mathbb R^2$ besitzt genau eine Darstellung

$$
f(x)=Ax
$$

mit einer Matrix $A\\in\\mathbb R^{2\\times n}$. Da $\\mathcal B$ eine Basis von $\\mathbb R^{2\\times n}$ ist, gibt es eindeutige Koeffizienten $c_B$ mit

$$
A=\\sum_{B\\in\\mathcal B}c_BB.
$$

Dann

$$
f(x)=Ax=\\sum_{B\\in\\mathcal B}c_BBx
=\\sum_{B\\in\\mathcal B}c_B f_B(x).
$$

Also erzeugt $\\mathcal L$ den Raum $L$. Die Eindeutigkeit der Koeffizienten folgt aus der Eindeutigkeit der Matrixdarstellung in der Basis $\\mathcal B$. Daher ist $\\mathcal L$ eine Basis von $L$.

(b)

$$
\\dim\\mathbb R^{2\\times n}=2n.
$$

Also

$$
\\dim L=2n.
$$

(c) Die Nullabbildung ist linear, also ist $L$ nicht leer. Sind $f_A(x)=Ax$ und $f_B(x)=Bx$ linear, dann

$$
(f_A+f_B)(x)=Ax+Bx=(A+B)x,
$$

also $f_A+f_B=f_{A+B}\\in L$. Für $\\lambda\\in\\mathbb R$ gilt

$$
(\\lambda f_A)(x)=\\lambda Ax=(\\lambda A)x,
$$

also $\\lambda f_A=f_{\\lambda A}\\in L$. Damit ist $L$ ein Untervektorraum von $V$.""",
        "zh_solution": """核心考点：**线性映射与矩阵表示、函数空间、子空间判据**。

(a) 任意线性映射

$$
f:\\mathbb R^n\\to\\mathbb R^2
$$

都能唯一写成

$$
f(x)=Ax,
$$

其中 $A\\in\\mathbb R^{2\\times n}$。因为 $\\mathcal B$ 是 $\\mathbb R^{2\\times n}$ 的一组基，矩阵 $A$ 可以唯一表示为

$$
A=\\sum_{B\\in\\mathcal B}c_BB.
$$

于是

$$
f(x)=Ax
=\\sum_{B\\in\\mathcal B}c_BBx
=\\sum_{B\\in\\mathcal B}c_Bf_B(x).
$$

这说明这些 $f_B$ 张成 $L$。如果函数线性组合为零，则对应的矩阵线性组合为零；由于 $\\mathcal B$ 线性无关，所有系数都为零，所以这些 $f_B$ 线性无关。因此它们构成 $L$ 的一组基。

(b) 一个 $2\\times n$ 矩阵有 $2n$ 个自由 entries，所以

$$
\\dim L=\\dim\\mathbb R^{2\\times n}=2n.
$$

(c) 证明 $L$ 是 $V$ 的子空间。零映射是线性的。若

$$
f_A(x)=Ax,\qquad f_B(x)=Bx,
$$

则

$$
(f_A+f_B)(x)=Ax+Bx=(A+B)x,
$$

仍是线性映射。若 $\\lambda\\in\\mathbb R$，

$$
(\\lambda f_A)(x)=\\lambda Ax=(\\lambda A)x,
$$

也仍是线性映射。所以 $L$ 对加法和数乘封闭，是 $V$ 的子空间。""",
    },
    ("ss22"+KAOSHI+"2", 5): {
        "problem": PRODUCT_SPACE_PROBLEM_DE,
        "zh_problem": PRODUCT_SPACE_PROBLEM_ZH,
        "solution": PRODUCT_SPACE_SOLUTION_DE,
        "zh_solution": PRODUCT_SPACE_SOLUTION_ZH,
    },
    ("ss24"+KAOSHI, 5): {
        "problem": PRODUCT_SPACE_PROBLEM_DE,
        "zh_problem": PRODUCT_SPACE_PROBLEM_ZH,
        "solution": PRODUCT_SPACE_SOLUTION_DE,
        "zh_solution": PRODUCT_SPACE_SOLUTION_ZH,
    },
    ("ss25", 5): {
        "problem": """Sei $V$ ein endlichdimensionaler Vektorraum. Der Dualraum ist

$$
V^*=\\{f:V\\to\\mathbb R\\mid f\\text{ linear}\\}.
$$

Sei $u_1,\ldots,u_n$ eine Basis von $V$. Die linearen Funktionen $g_1,\ldots,g_n$ seien durch

$$
g_i(u_j)=\\delta_{ij}
$$

definiert.

(a) Für $V=\\mathbb R^n$ mit Standardbasis: Geben Sie eine geschlossene Formel für $g_i(x)$ an.

(b) Zeigen Sie, dass $g_1,\ldots,g_n$ linear unabhängig sind.

(c) Zeigen Sie: Für jedes $f\\in V^*$ gilt

$$
f=\\sum_{i=1}^n f(u_i)g_i.
$$""",
        "zh_problem": """设 $V$ 是有限维向量空间。对偶空间（Dualraum）定义为

$$
V^*=\\{f:V\\to\\mathbb R\\mid f\\text{ 线性}\\}.
$$

设 $u_1,\ldots,u_n$ 是 $V$ 的一组基。线性函数 $g_1,\ldots,g_n$ 由

$$
g_i(u_j)=\\delta_{ij}
$$

定义。

(a) 当 $V=\\mathbb R^n$ 且基为标准基时，写出 $g_i(x)$ 的闭式表达。

(b) 证明 $g_1,\ldots,g_n$ 线性无关。

(c) 证明：对任意 $f\\in V^*$，

$$
f=\\sum_{i=1}^n f(u_i)g_i.
$$""",
        "solution": """Lösung:

(a) Für $V=\\mathbb R^n$ mit Standardbasis $e_1,\ldots,e_n$ ist

$$
g_i(x_1,\ldots,x_n)=x_i.
$$

Denn $g_i(e_j)=\\delta_{ij}$.

(b) Sei

$$
\\sum_{i=1}^n\\alpha_i g_i=0
$$

als lineare Funktion. Wir setzen $u_j$ ein:

$$
0=\\left(\\sum_{i=1}^n\\alpha_i g_i\\right)(u_j)
=\\sum_{i=1}^n\\alpha_i g_i(u_j)
=\\alpha_j.
$$

Da dies für jedes $j$ gilt, sind alle $\\alpha_j=0$. Also sind $g_1,\ldots,g_n$ linear unabhängig.

(c) Definiere

$$
\\hat f=\\sum_{i=1}^n f(u_i)g_i.
$$

Für jedes Basiselement $u_j$ gilt

$$
\\hat f(u_j)
=\\sum_{i=1}^n f(u_i)g_i(u_j)
=f(u_j).
$$

Die linearen Abbildungen $f$ und $\\hat f$ stimmen also auf einer Basis überein. Daher sind sie gleich:

$$
f=\\hat f=\\sum_{i=1}^n f(u_i)g_i.
$$""",
        "zh_solution": """核心考点：**对偶空间、对偶基、线性函数由基上的取值唯一决定**。

(a) 在 $\\mathbb R^n$ 的标准基下，$g_i$ 就是“取第 $i$ 个坐标”的函数：

$$
g_i(x_1,\ldots,x_n)=x_i.
$$

因为对标准基向量 $e_j$，

$$
g_i(e_j)=\\delta_{ij}.
$$

(b) 证明线性无关。设

$$
\\sum_{i=1}^n\\alpha_i g_i=0.
$$

这里右边的 $0$ 是零函数。把 $u_j$ 代入：

$$
0=\\left(\\sum_{i=1}^n\\alpha_i g_i\\right)(u_j)
=\\sum_{i=1}^n\\alpha_i g_i(u_j).
$$

由于 $g_i(u_j)=\\delta_{ij}$，上式只剩

$$
0=\\alpha_j.
$$

每个 $j$ 都成立，所以所有系数都是 $0$，因此 $g_1,\ldots,g_n$ 线性无关。

(c) 令

$$
\\hat f=\\sum_{i=1}^n f(u_i)g_i.
$$

检查它和 $f$ 在基向量上的取值。对任意 $u_j$，

$$
\\hat f(u_j)
=\\sum_{i=1}^n f(u_i)g_i(u_j)
=f(u_j).
$$

也就是说 $\\hat f$ 和 $f$ 在整组基 $u_1,\ldots,u_n$ 上完全相同。线性映射由它在一组基上的取值唯一决定，所以

$$
f=\\hat f
=\\sum_{i=1}^n f(u_i)g_i.
$$""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss00", 1): {
        "problem": """Bestimmen Sie eine Basis des Lösungsraumes des homogenen linearen Gleichungssystems

$$
\\begin{aligned}
x_1+3x_2+2x_3+x_4&=0,\\\\
3x_1+9x_2+7x_3+5x_4&=0,\\\\
2x_1+6x_2+7x_3+8x_4&=0.
\\end{aligned}
$$""",
        "zh_problem": """求下列齐次线性方程组（homogenes lineares Gleichungssystem）解空间的一组基：

$$
\\begin{aligned}
x_1+3x_2+2x_3+x_4&=0,\\\\
3x_1+9x_2+7x_3+5x_4&=0,\\\\
2x_1+6x_2+7x_3+8x_4&=0.
\\end{aligned}
$$""",
        "solution": """Lösung:

Die Koeffizientenmatrix wird in Zeilenstufenform gebracht:

$$
\\begin{pmatrix}
1&3&2&1\\\\
3&9&7&5\\\\
2&6&7&8
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&3&2&1\\\\
0&0&1&2\\\\
0&0&0&0
\\end{pmatrix}.
$$

Damit gilt

$$
x_3+2x_4=0,
\\qquad
x_1+3x_2+2x_3+x_4=0.
$$

Setze $x_2=s$ und $x_4=t$. Dann

$$
x_3=-2t
$$

und

$$
x_1=-3s-2(-2t)-t=-3s+3t.
$$

Also

$$
x=
s\\begin{pmatrix}-3\\\\1\\\\0\\\\0\end{pmatrix}
t\\begin{pmatrix}3\\\\0\\\\-2\\\\1\end{pmatrix},
\\qquad s,t\\in\\mathbb R.
$$

Eine Basis des Lösungsraumes ist daher

$$
\\left\\{
\\begin{pmatrix}-3\\\\1\\\\0\\\\0\end{pmatrix},
\\begin{pmatrix}3\\\\0\\\\-2\\\\1\end{pmatrix}
\\right\\}.
$$""",
        "zh_solution": """核心考点：**齐次方程组、自由变量、解空间基**。

先把系数矩阵行化简：

$$
\\begin{pmatrix}
1&3&2&1\\\\
3&9&7&5\\\\
2&6&7&8
\\end{pmatrix}
\\sim
\\begin{pmatrix}
1&3&2&1\\\\
0&0&1&2\\\\
0&0&0&0
\\end{pmatrix}.
$$

第二行给出

$$
x_3=-2x_4.
$$

令自由变量

$$
x_2=s,\qquad x_4=t.
$$

则

$$
x_3=-2t.
$$

代回第一行：

$$
x_1+3s+2(-2t)+t=0,
$$

所以

$$
x_1=-3s+3t.
$$

因此通解为

$$
x=
s\\begin{pmatrix}-3\\\\1\\\\0\\\\0\end{pmatrix}
t\\begin{pmatrix}3\\\\0\\\\-2\\\\1\end{pmatrix}.
$$

解空间的一组基就是

$$
\\left\\{
\\begin{pmatrix}-3\\\\1\\\\0\\\\0\end{pmatrix},
\\begin{pmatrix}3\\\\0\\\\-2\\\\1\end{pmatrix}
\\right\\}.
$$""",
    },
    ("ss00", 2): {
        "problem": """Gegeben sei

$$
A=
\\begin{pmatrix}
1&1&2\\\\
-1&0&-1\\\\
-2&-2&-3
\\end{pmatrix}.
$$

Berechnen Sie $A^{-1}$.""",
        "zh_problem": """给定矩阵

$$
A=
\\begin{pmatrix}
1&1&2\\\\
-1&0&-1\\\\
-2&-2&-3
\\end{pmatrix}.
$$

计算 $A^{-1}$。""",
        "solution": """Lösung:

Wir verwenden Gauß-Jordan:

$$
\\left(
\\begin{array}{ccc|ccc}
1&1&2&1&0&0\\\\
-1&0&-1&0&1&0\\\\
-2&-2&-3&0&0&1
\\end{array}
\\right)
\\sim
\\left(
\\begin{array}{ccc|ccc}
1&0&0&-2&-1&-1\\\\
0&1&0&-1&1&-1\\\\
0&0&1&2&0&1
\\end{array}
\\right).
$$

Daher

$$
A^{-1}=
\\begin{pmatrix}
-2&-1&-1\\\\
-1&1&-1\\\\
2&0&1
\\end{pmatrix}.
$$""",
        "zh_solution": """核心考点：**逆矩阵、增广矩阵法**。

把 $A$ 和单位矩阵拼成增广矩阵：

$$
(A\\mid I).
$$

做 Gauss-Jordan 消元：

$$
\\left(
\\begin{array}{ccc|ccc}
1&1&2&1&0&0\\\\
-1&0&-1&0&1&0\\\\
-2&-2&-3&0&0&1
\\end{array}
\\right)
\\sim
\\left(
\\begin{array}{ccc|ccc}
1&0&0&-2&-1&-1\\\\
0&1&0&-1&1&-1\\\\
0&0&1&2&0&1
\\end{array}
\\right).
$$

左边化成 $I$ 后，右边就是 $A^{-1}$：

$$
A^{-1}=
\\begin{pmatrix}
-2&-1&-1\\\\
-1&1&-1\\\\
2&0&1
\\end{pmatrix}.
$$""",
    },
    ("ss17", 1): {
        "problem": """Zeigen Sie für $n\\in\\mathbb N$ durch vollständige Induktion:

$$
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}^n
=
2^{n-1}
\\begin{pmatrix}
2&-n&n\\\\
0&n+2&-n\\\\
0&n&2-n
\\end{pmatrix}.
$$""",
        "zh_problem": """用完全归纳法证明：对所有 $n\\in\\mathbb N$，

$$
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}^n
=
2^{n-1}
\\begin{pmatrix}
2&-n&n\\\\
0&n+2&-n\\\\
0&n&2-n
\\end{pmatrix}.
$$""",
        "solution": """Lösung:

Für $n=1$ ist die rechte Seite

$$
2^0
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix},
$$

also stimmt die Behauptung.

Sei die Formel für ein $n\\in\\mathbb N$ richtig. Setze

$$
B=
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}.
$$

Dann

$$
B^{n+1}=B^nB
=2^{n-1}
\\begin{pmatrix}
2&-n&n\\\\
0&n+2&-n\\\\
0&n&2-n
\\end{pmatrix}
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}.
$$

Die Matrixmultiplikation ergibt

$$
\\begin{pmatrix}
4&-2n-2&2n+2\\\\
0&2n+6&-2n-2\\\\
0&2n+2&2-2n
\\end{pmatrix}
=2
\\begin{pmatrix}
2&-(n+1)&n+1\\\\
0&(n+1)+2&-(n+1)\\\\
0&n+1&2-(n+1)
\\end{pmatrix}.
$$

Also

$$
B^{n+1}
=2^n
\\begin{pmatrix}
2&-(n+1)&n+1\\\\
0&(n+1)+2&-(n+1)\\\\
0&n+1&2-(n+1)
\\end{pmatrix}.
$$

Damit ist die Induktion abgeschlossen.""",
        "zh_solution": """核心考点：**矩阵幂公式、完全归纳法**。

记

$$
B=
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}.
$$

当 $n=1$ 时，右边为

$$
2^0
\\begin{pmatrix}
2&-1&1\\\\
0&3&-1\\\\
0&1&1
\\end{pmatrix}=B,
$$

所以起点成立。

归纳假设：

$$
B^n=
2^{n-1}
\\begin{pmatrix}
2&-n&n\\\\
0&n+2&-n\\\\
0&n&2-n
\\end{pmatrix}.
$$

归纳步从

$$
B^{n+1}=B^nB
$$

开始，把归纳假设代入：

$$
B^{n+1}
=2^{n-1}
\\begin{pmatrix}
2&-n&n\\\\
0&n+2&-n\\\\
0&n&2-n
\\end{pmatrix}
B.
$$

直接乘矩阵得到

$$
\\begin{pmatrix}
4&-2n-2&2n+2\\\\
0&2n+6&-2n-2\\\\
0&2n+2&2-2n
\\end{pmatrix}
=2
\\begin{pmatrix}
2&-(n+1)&n+1\\\\
0&(n+1)+2&-(n+1)\\\\
0&n+1&2-(n+1)
\\end{pmatrix}.
$$

因此

$$
B^{n+1}
=2^n
\\begin{pmatrix}
2&-(n+1)&n+1\\\\
0&(n+1)+2&-(n+1)\\\\
0&n+1&2-(n+1)
\\end{pmatrix}.
$$

这正是把公式里的 $n$ 换成 $n+1$，证明完成。""",
    },
    ("ss17", 2): {
        "problem": """Betrachten Sie

$$
R=\\left\\{
\\begin{pmatrix}
a&b\\\\
0&a
\\end{pmatrix}
\\mid a,b\\in\\mathbb R
\\right\\}.
$$

(a) Zeigen Sie, dass $(R,+,\\cdot)$ ein kommutativer Ring mit Einselement ist.

(b) Bestimmen Sie alle $M\\in R$ mit $M^2=0$.

(c) Zeigen Sie, dass $(R,+,\\cdot)$ kein Körper ist.""",
        "zh_problem": """考虑矩阵集合

$$
R=\\left\\{
\\begin{pmatrix}
a&b\\\\
0&a
\\end{pmatrix}
\\mid a,b\\in\\mathbb R
\\right\\}.
$$

(a) 证明 $(R,+,\\cdot)$ 是带单位元的交换环（kommutativer Ring mit Einselement）。

(b) 求所有满足 $M^2=0$ 的 $M\\in R$。

(c) 证明 $(R,+,\\cdot)$ 不是域（Körper）。""",
        "solution": """Lösung:

Seien

$$
A=\\begin{pmatrix}a&b\\\\0&a\end{pmatrix},
\\qquad
B=\\begin{pmatrix}c&d\\\\0&c\end{pmatrix}.
$$

Dann

$$
A-B=
\\begin{pmatrix}
a-c&b-d\\\\
0&a-c
\\end{pmatrix}\\in R,
$$

also ist $(R,+)$ eine Untergruppe. Außerdem

$$
AB=
\\begin{pmatrix}
ac&ad+bc\\\\
0&ac
\\end{pmatrix}\\in R.
$$

Da $ad+bc=cb+da$, gilt auch $AB=BA$. Das Einselement ist

$$
I_2=\\begin{pmatrix}1&0\\\\0&1\end{pmatrix}\\in R.
$$

Damit ist $R$ ein kommutativer Ring mit Einselement.

Für

$$
M=\\begin{pmatrix}a&b\\\\0&a\end{pmatrix}
$$

gilt

$$
M^2=
\\begin{pmatrix}
a^2&2ab\\\\
0&a^2
\\end{pmatrix}.
$$

Also ist $M^2=0$ genau dann, wenn $a=0$. Daher

$$
M=
\\begin{pmatrix}
0&b\\\\
0&0
\\end{pmatrix},
\\qquad b\\in\\mathbb R.
$$

Der Ring ist kein Körper, denn

$$
N=\\begin{pmatrix}0&1\\\\0&0\end{pmatrix}\\ne0
$$

erfüllt $N^2=0$. Ein Körper besitzt keine von Null verschiedenen Nullteiler.""",
        "zh_solution": """核心考点：**矩阵环、交换性、零因子、域判定**。

取

$$
A=\\begin{pmatrix}a&b\\\\0&a\end{pmatrix},
\\qquad
B=\\begin{pmatrix}c&d\\\\0&c\end{pmatrix}.
$$

先看加法：

$$
A-B=
\\begin{pmatrix}
a-c&b-d\\\\
0&a-c
\\end{pmatrix}\\in R.
$$

所以加法下封闭并有加法逆。再看乘法：

$$
AB=
\\begin{pmatrix}
ac&ad+bc\\\\
0&ac
\\end{pmatrix}\\in R.
$$

而

$$
BA=
\\begin{pmatrix}
ca&cb+da\\\\
0&ca
\\end{pmatrix}.
$$

因为实数乘法交换，$ad+bc=cb+da$，所以 $AB=BA$。单位元是

$$
I_2=\\begin{pmatrix}1&0\\\\0&1\end{pmatrix}.
$$

因此这是带单位元的交换环。

设

$$
M=\\begin{pmatrix}a&b\\\\0&a\end{pmatrix}.
$$

计算

$$
M^2=
\\begin{pmatrix}
a^2&2ab\\\\
0&a^2
\\end{pmatrix}.
$$

要 $M^2=0$，必须 $a^2=0$，所以 $a=0$；此时 $b$ 任意：

$$
M=
\\begin{pmatrix}
0&b\\\\
0&0
\\end{pmatrix}.
$$

取

$$
N=\\begin{pmatrix}0&1\\\\0&0\end{pmatrix}.
$$

它非零，但 $N^2=0$。这说明 $R$ 有非零零因子；域中不能有非零零因子，所以 $R$ 不是域。""",
    },
    ("ss17", 5): {
        "problem": """Seien $n\\in\\mathbb N$ und $A\\in\\mathbb R^{n\\times n}$ mit $A^T=-A$. Zeigen Sie:

(a) $x^TAy=-y^TAx$ für alle $x,y\\in\\mathbb R^n$.

(b) $x^TAx=0$ für alle $x\\in\\mathbb R^n$.

(c) Aus $x=-Ax$ folgt $x=0$.

(d) $I_n+A$ ist invertierbar.

(e) $(I_n+A)^{-1}(I_n-A)=(I_n-A)(I_n+A)^{-1}$.

(f) Für

$$
U=(I_n+A)^{-1}(I_n-A)
$$

gilt $U^TU=I_n$.""",
        "zh_problem": """设 $n\\in\\mathbb N$，$A\\in\\mathbb R^{n\\times n}$ 且 $A^T=-A$。证明：

(a) 对所有 $x,y\\in\\mathbb R^n$，$x^TAy=-y^TAx$。

(b) 对所有 $x\\in\\mathbb R^n$，$x^TAx=0$。

(c) 若 $x=-Ax$，则 $x=0$。

(d) $I_n+A$ 可逆。

(e) $(I_n+A)^{-1}(I_n-A)=(I_n-A)(I_n+A)^{-1}$。

(f) 对

$$
U=(I_n+A)^{-1}(I_n-A)
$$

证明 $U^TU=I_n$。""",
        "solution": """Lösung:

(a) Da $x^TAy$ ein Skalar ist,

$$
x^TAy=(x^TAy)^T=y^TA^Tx=-y^TAx.
$$

(b) Setze $y=x$ in (a). Dann

$$
x^TAx=-x^TAx,
$$

also $x^TAx=0$.

(c) Aus $x=-Ax$ folgt $Ax=-x$. Mit (b):

$$
0=x^TAx=x^T(-x)=-x^Tx.
$$

Also $x^Tx=0$ und daher $x=0$.

(d) Sei $(I_n+A)x=0$. Dann $x=-Ax$, also nach (c) $x=0$. Der Kern ist trivial, daher ist $I_n+A$ invertierbar.

(e) Da

$$
(I_n+A)(I_n-A)=I_n-A^2=(I_n-A)(I_n+A),
$$

kommutieren $I_n+A$ und $I_n-A$. Weil $I_n+A$ invertierbar ist, folgt

$$
(I_n+A)^{-1}(I_n-A)=(I_n-A)(I_n+A)^{-1}.
$$

(f) Es gilt

$$
U^T=\\bigl((I_n+A)^{-1}(I_n-A)\\bigr)^T
=(I_n-A)^T\\bigl((I_n+A)^{-1}\\bigr)^T.
$$

Mit $A^T=-A$ ist

$$
(I_n-A)^T=I_n+A,
\\qquad
\\bigl((I_n+A)^{-1}\\bigr)^T=(I_n-A)^{-1}.
$$

Also

$$
U^T=(I_n+A)(I_n-A)^{-1}.
$$

Damit

$$
U^TU=(I_n+A)(I_n-A)^{-1}(I_n+A)^{-1}(I_n-A)=I_n,
$$

wobei die Faktoren wegen (e) passend vertauscht werden dürfen. Also ist $U$ orthogonal.""",
        "zh_solution": """核心考点：**反对称矩阵、可逆性、Cayley-Transform、正交矩阵**。

(a) 因为 $x^TAy$ 是 $1\\times1$ 标量，所以它等于自己的转置：

$$
x^TAy=(x^TAy)^T=y^TA^Tx.
$$

又因为 $A^T=-A$，

$$
x^TAy=-y^TAx.
$$

(b) 令 $y=x$：

$$
x^TAx=-x^TAx.
$$

所以

$$
x^TAx=0.
$$

(c) 如果 $x=-Ax$，即 $Ax=-x$。由 (b)：

$$
0=x^TAx=x^T(-x)=-x^Tx.
$$

于是 $x^Tx=0$，所以 $x=0$。

(d) 若 $(I_n+A)x=0$，则 $x=-Ax$。由 (c) 得 $x=0$。所以 $I_n+A$ 的核只有零向量，因此可逆。

(e) 计算：

$$
(I_n+A)(I_n-A)=I_n-A^2=(I_n-A)(I_n+A).
$$

所以 $I_n+A$ 与 $I_n-A$ 交换。由于 $I_n+A$ 可逆，

$$
(I_n+A)^{-1}(I_n-A)=(I_n-A)(I_n+A)^{-1}.
$$

(f) 令

$$
U=(I_n+A)^{-1}(I_n-A).
$$

利用转置和逆矩阵公式：

$$
U^T=(I_n+A)(I_n-A)^{-1}.
$$

于是

$$
U^TU=(I_n+A)(I_n-A)^{-1}(I_n+A)^{-1}(I_n-A)=I_n.
$$

所以 $U$ 是正交矩阵。""",
    },
    ("ss17", 6): {
        "problem": """Sei $f:\\mathbb R^4\\to\\mathbb R^2$ definiert durch

$$
f\\begin{pmatrix}x_1\\\\x_2\\\\x_3\\\\x_4\end{pmatrix}
=
\\begin{pmatrix}
x_1+x_2+x_3\\\\
x_2+x_3+x_4
\\end{pmatrix}.
$$

(a) Schreiben Sie $f(x)=Mx$.

(b) Zeigen Sie, dass

$$
U=\\{x\\in\\mathbb R^4\\mid x_1+x_2+x_3=0,\ x_2+x_3+x_4=0\\}
$$

ein Untervektorraum ist, und bestimmen Sie eine Basis von $U$.

(c) Zeigen Sie, dass $f$ surjektiv, aber nicht injektiv ist.""",
        "zh_problem": """定义 $f:\\mathbb R^4\\to\\mathbb R^2$：

$$
f\\begin{pmatrix}x_1\\\\x_2\\\\x_3\\\\x_4\end{pmatrix}
=
\\begin{pmatrix}
x_1+x_2+x_3\\\\
x_2+x_3+x_4
\\end{pmatrix}.
$$

(a) 写成 $f(x)=Mx$。

(b) 证明

$$
U=\\{x\\in\\mathbb R^4\\mid x_1+x_2+x_3=0,\ x_2+x_3+x_4=0\\}
$$

是子空间，并求一组基。

(c) 证明 $f$ 满射但不是单射。""",
        "solution": """Lösung:

(a)

$$
M=
\\begin{pmatrix}
1&1&1&0\\\\
0&1&1&1
\\end{pmatrix}.
$$

(b) Es gilt $U=\ker f$, also ist $U$ ein Untervektorraum. Löse $Mx=0$:

$$
x_1+x_2+x_3=0,\qquad x_2+x_3+x_4=0.
$$

Setze $x_2=s$ und $x_3=t$. Dann

$$
x_1=-s-t,\qquad x_4=-s-t.
$$

Also

$$
x=s\\begin{pmatrix}-1\\\\1\\\\0\\\\-1\end{pmatrix}
t\\begin{pmatrix}-1\\\\0\\\\1\\\\-1\end{pmatrix}.
$$

Eine Basis von $U$ ist

$$
\\left\\{
\\begin{pmatrix}-1\\\\1\\\\0\\\\-1\end{pmatrix},
\\begin{pmatrix}-1\\\\0\\\\1\\\\-1\end{pmatrix}
\\right\\}.
$$

(c) Die beiden Zeilen von $M$ sind linear unabhängig, also $\\operatorname{rang}M=2$. Da der Zielraum $\\mathbb R^2$ Dimension $2$ hat, ist $f$ surjektiv. Wegen

$$
\\dim\\ker f=4-2=2
$$

ist der Kern nicht trivial; daher ist $f$ nicht injektiv.""",
        "zh_solution": """核心考点：**线性映射矩阵、核、满射与单射**。

(a) 直接从两个分量读出矩阵：

$$
M=
\\begin{pmatrix}
1&1&1&0\\\\
0&1&1&1
\\end{pmatrix}.
$$

(b) 集合 $U$ 正好是 $Mx=0$ 的解集，所以

$$
U=\ker f.
$$

核空间一定是子空间。求基时解方程：

$$
x_1+x_2+x_3=0,\qquad x_2+x_3+x_4=0.
$$

令

$$
x_2=s,\qquad x_3=t.
$$

则

$$
x_1=-s-t,\qquad x_4=-s-t.
$$

所以

$$
x=s\\begin{pmatrix}-1\\\\1\\\\0\\\\-1\end{pmatrix}
t\\begin{pmatrix}-1\\\\0\\\\1\\\\-1\end{pmatrix}.
$$

因此 $U$ 的一组基为

$$
\\left\\{
\\begin{pmatrix}-1\\\\1\\\\0\\\\-1\end{pmatrix},
\\begin{pmatrix}-1\\\\0\\\\1\\\\-1\end{pmatrix}
\\right\\}.
$$

(c) 矩阵 $M$ 的两行线性无关，所以

$$
\\operatorname{rang}M=2.
$$

目标空间是 $\\mathbb R^2$，秩等于 $2$，所以 $f$ 满射。另一方面

$$
\\dim\\ker f=4-2=2,
$$

核不只是零向量，所以 $f$ 不是单射。""",
    },
    ("ss17", 7): {
        "problem": """Gegeben sei

$$
A=
\\begin{pmatrix}
3&-2&-4\\\\
0&1&0\\\\
2&-2&-3
\\end{pmatrix}.
$$

(a) Zeigen Sie, dass $1$ Eigenwert von $A$ ist, und bestimmen Sie den Eigenraum.

(b) Berechnen Sie alle weiteren Eigenwerte und die zugehörigen Eigenräume.

(c) Entscheiden Sie, ob $A$ diagonalisierbar ist.""",
        "zh_problem": """给定

$$
A=
\\begin{pmatrix}
3&-2&-4\\\\
0&1&0\\\\
2&-2&-3
\\end{pmatrix}.
$$

(a) 证明 $1$ 是 $A$ 的特征值，并求对应特征空间。

(b) 求其它所有特征值及其特征空间。

(c) 判断 $A$ 是否可对角化。""",
        "solution": """Lösung:

Das charakteristische Polynom ist

$$
\\chi_A(\\lambda)
=\\det(A-\\lambda I)
=(\\lambda-1)^2(\\lambda+1).
$$

Die Eigenwerte sind also

$$
\\lambda_1=1,\qquad \\lambda_2=-1.
$$

Für $\\lambda=1$ löst man $(A-I)x=0$ und erhält

$$
E_1=
\\operatorname{span}\\left\\{
\\begin{pmatrix}1\\\\1\\\\0\end{pmatrix},
\\begin{pmatrix}2\\\\0\\\\1\end{pmatrix}
\\right\\}.
$$

Für $\\lambda=-1$ gilt

$$
E_{-1}=
\\operatorname{span}\\left\\{
\\begin{pmatrix}1\\\\0\\\\1\end{pmatrix}
\\right\\}.
$$

Damit besitzt $A$ insgesamt drei linear unabhängige Eigenvektoren. Also ist $A$ diagonalisierbar.""",
        "zh_solution": """核心考点：**特征多项式、特征空间、对角化判定**。

先算特征多项式：

$$
\\chi_A(\\lambda)
=\\det(A-\\lambda I)
=(\\lambda-1)^2(\\lambda+1).
$$

所以特征值为

$$
1\\quad(2\\text{ 重}),\qquad -1\\quad(1\\text{ 重}).
$$

对 $\\lambda=1$，解

$$
(A-I)x=0.
$$

得到

$$
E_1=
\\operatorname{span}\\left\\{
\\begin{pmatrix}1\\\\1\\\\0\end{pmatrix},
\\begin{pmatrix}2\\\\0\\\\1\end{pmatrix}
\\right\\}.
$$

对 $\\lambda=-1$，解

$$
(A+I)x=0.
$$

得到

$$
E_{-1}=
\\operatorname{span}\\left\\{
\\begin{pmatrix}1\\\\0\\\\1\end{pmatrix}
\\right\\}.
$$

特征向量总数维度为

$$
\\dim E_1+\dim E_{-1}=2+1=3.
$$

矩阵是 $3\\times3$，所以有一组由特征向量组成的基，因此 $A$ 可对角化。""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss18", 1): {
        "problem": r"""Zeigen Sie für alle $n\in\mathbb N$ durch vollständige Induktion:

$$
A^n
=
2^n
\begin{pmatrix}
-1&1&0\\
-2&2&0\\
0&0&0
\end{pmatrix}
+
\begin{pmatrix}
2&-1&n\\
2&-1&n\\
0&0&1
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
0&1&1\\
-2&3&1\\
0&0&1
\end{pmatrix}.
$$""",
        "zh_problem": r"""用数学归纳法证明：对所有 $n\in\mathbb N$，

$$
A^n
=
2^n
\begin{pmatrix}
-1&1&0\\
-2&2&0\\
0&0&0
\end{pmatrix}
+
\begin{pmatrix}
2&-1&n\\
2&-1&n\\
0&0&1
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
0&1&1\\
-2&3&1\\
0&0&1
\end{pmatrix}.
$$""",
        "solution": r"""Setze

$$
P=\begin{pmatrix}-1&1&0\\-2&2&0\\0&0&0\end{pmatrix},
\qquad
Q_n=\begin{pmatrix}2&-1&n\\2&-1&n\\0&0&1\end{pmatrix}.
$$

Zu zeigen ist $A^n=2^nP+Q_n$.

**Induktionsanfang $n=1$.**

$$
2P+Q_1=
\begin{pmatrix}-2&2&0\\-4&4&0\\0&0&0\end{pmatrix}
+
\begin{pmatrix}2&-1&1\\2&-1&1\\0&0&1\end{pmatrix}
=
\begin{pmatrix}0&1&1\\-2&3&1\\0&0&1\end{pmatrix}
=A.
$$

**Induktionsannahme.** Für ein festes $n\in\mathbb N$ gelte

$$
A^n=2^nP+Q_n.
$$

**Induktionsschritt.** Dann gilt

$$
A^{n+1}=A^nA=(2^nP+Q_n)A=2^n(PA)+Q_nA.
$$

Die beiden benötigten Produkte sind

$$
PA=
\begin{pmatrix}-2&2&0\\-4&4&0\\0&0&0\end{pmatrix}
=2P,
$$

und

$$
Q_nA
=
\begin{pmatrix}
2&-1&n+1\\
2&-1&n+1\\
0&0&1
\end{pmatrix}
=Q_{n+1}.
$$

Also

$$
A^{n+1}=2^n\cdot2P+Q_{n+1}=2^{n+1}P+Q_{n+1}.
$$

Damit ist die Formel für alle $n\in\mathbb N$ bewiesen.""",
        "zh_solution": r"""核心考点：**矩阵幂与数学归纳法**。

这题不要直接硬算 $A^n$，而是把右边拆成两个好乘的块：

$$
P=\begin{pmatrix}-1&1&0\\-2&2&0\\0&0&0\end{pmatrix},
\qquad
Q_n=\begin{pmatrix}2&-1&n\\2&-1&n\\0&0&1\end{pmatrix}.
$$

要证的是 $A^n=2^nP+Q_n$。

先验算 $n=1$：

$$
2P+Q_1
=
\begin{pmatrix}0&1&1\\-2&3&1\\0&0&1\end{pmatrix}
=A.
$$

归纳假设：某个 $n$ 时成立，即

$$
A^n=2^nP+Q_n.
$$

归纳步的关键是右乘一个 $A$：

$$
A^{n+1}=A^nA=(2^nP+Q_n)A=2^nPA+Q_nA.
$$

分别算两个小乘法：

$$
PA=2P,
\qquad
Q_nA=Q_{n+1}.
$$

所以

$$
A^{n+1}=2^n\cdot2P+Q_{n+1}=2^{n+1}P+Q_{n+1}.
$$

解题思路：归纳法题最怕把矩阵乘法写成一坨。这里真正要观察的是 $P$ 右乘 $A$ 只会放大 $2$ 倍，而 $Q_n$ 右乘 $A$ 只会把右上角的 $n$ 变成 $n+1$。这就是公式能传递下去的原因。""",
    },
    ("ss18", 4): {
        "problem": r"""Gegeben seien $a,b\in\mathbb R$ und

$$
A=
\begin{pmatrix}
1&0&0&1\\
a&1&0&b\\
b&0&1&a\\
0&a&b&0
\end{pmatrix}.
$$

Berechnen Sie $\operatorname{rang}(A)$ in Abhängigkeit von $a$ und $b$ und fassen Sie die Fälle in einer Tabelle zusammen.""",
        "zh_problem": r"""给定 $a,b\in\mathbb R$ 以及

$$
A=
\begin{pmatrix}
1&0&0&1\\
a&1&0&b\\
b&0&1&a\\
0&a&b&0
\end{pmatrix}.
$$

求 $\operatorname{rang}(A)$ 关于参数 $a,b$ 的分类，并用表格汇总。""",
        "solution": r"""Wir bringen $A$ mit rang-erhaltenden Zeilenumformungen in Stufenform.

Zuerst

$$
R_2\leftarrow R_2-aR_1,\qquad
R_3\leftarrow R_3-bR_1
$$

liefert

$$
\begin{pmatrix}
1&0&0&1\\
0&1&0&b-a\\
0&0&1&a-b\\
0&a&b&0
\end{pmatrix}.
$$

Danach

$$
R_4\leftarrow R_4-aR_2-bR_3.
$$

Damit erhält man

$$
\begin{pmatrix}
1&0&0&1\\
0&1&0&b-a\\
0&0&1&a-b\\
0&0&0&(a-b)^2
\end{pmatrix}.
$$

Also gibt es drei sichere Pivotzeilen. Die vierte Pivotzeile tritt genau dann auf, wenn

$$
(a-b)^2\ne0
\quad\Longleftrightarrow\quad
a\ne b.
$$

Damit:

| Rang | Bedingung |
|---:|---|
| $4$ | $a\ne b$ |
| $3$ | $a=b$ |""",
        "zh_solution": r"""核心考点：**参数矩阵的秩分类**。

秩不怕参数，先做不改变秩的行变换。对

$$
A=
\begin{pmatrix}
1&0&0&1\\
a&1&0&b\\
b&0&1&a\\
0&a&b&0
\end{pmatrix}
$$

先消掉第一列下面的 $a,b$：

$$
R_2\leftarrow R_2-aR_1,\qquad
R_3\leftarrow R_3-bR_1.
$$

得到

$$
\begin{pmatrix}
1&0&0&1\\
0&1&0&b-a\\
0&0&1&a-b\\
0&a&b&0
\end{pmatrix}.
$$

再用第二、三行消掉第四行的 $a,b$：

$$
R_4\leftarrow R_4-aR_2-bR_3,
$$

于是

$$
\begin{pmatrix}
1&0&0&1\\
0&1&0&b-a\\
0&0&1&a-b\\
0&0&0&(a-b)^2
\end{pmatrix}.
$$

前三行一定有主元。第四行是否给新主元，只看 $(a-b)^2$ 是否为零：

| 秩 | 参数条件 |
|---:|---|
| $4$ | $a\ne b$ |
| $3$ | $a=b$ |

解题思路：这类题不要先算 $4\times4$ 行列式。用高斯消元把参数集中到最后一个位置，最后只需判断 $(a-b)^2$ 是否为零。""",
    },
    ("ss18", 5): {
        "problem": r"""Seien $n\in\mathbb N$ und $A\in\mathbb R^{n\times n}$ mit

$$
A^2=-I_n.
$$

Zeigen Sie:

(a) $A$ ist invertierbar.

(b) $I_n+A$ ist invertierbar und

$$
(I_n+A)^{-1}=\frac12(I_n-A).
$$

(c) Gilt zusätzlich $A^T=-A$, so ist

$$
\frac1{\sqrt2}(I_n+A)
$$

orthogonal.

(d) $n$ ist gerade.""",
        "zh_problem": r"""设 $n\in\mathbb N$，$A\in\mathbb R^{n\times n}$，并且

$$
A^2=-I_n.
$$

证明：

(a) $A$ 可逆。

(b) $I_n+A$ 可逆，且

$$
(I_n+A)^{-1}=\frac12(I_n-A).
$$

(c) 若还满足 $A^T=-A$，则

$$
\frac1{\sqrt2}(I_n+A)
$$

是正交矩阵。

(d) $n$ 必为偶数。""",
        "solution": r"""(a) Aus $A^2=-I_n$ folgt

$$
A(-A)=(-A)A=-A^2=I_n.
$$

Also ist $A$ invertierbar und

$$
A^{-1}=-A.
$$

(b) Wir rechnen direkt nach:

$$
(I_n+A)\frac12(I_n-A)
=\frac12(I_n-A+A-A^2)
=\frac12(I_n-A^2).
$$

Wegen $A^2=-I_n$ ist

$$
\frac12(I_n-A^2)=\frac12(I_n+I_n)=I_n.
$$

Analog gilt

$$
\frac12(I_n-A)(I_n+A)=I_n.
$$

Damit ist

$$
(I_n+A)^{-1}=\frac12(I_n-A).
$$

(c) Setze

$$
Q=\frac1{\sqrt2}(I_n+A).
$$

Aus $A^T=-A$ folgt

$$
Q^T=\frac1{\sqrt2}(I_n-A).
$$

Dann

$$
Q^TQ
=\frac12(I_n-A)(I_n+A)
=\frac12(I_n-A^2)
=I_n.
$$

Also ist $Q$ orthogonal.

(d) Wende die Determinante auf $A^2=-I_n$ an:

$$
\det(A^2)=\det(-I_n).
$$

Damit

$$
(\det A)^2=(-1)^n.
$$

Da $A$ invertierbar ist, gilt $\det A\ne0$, also ist $(\det A)^2>0$. Folglich muss

$$
(-1)^n>0
$$

gelten. Das ist genau für gerade $n$ der Fall. Also ist $n$ gerade.""",
        "zh_solution": r"""核心考点：**矩阵方程、逆矩阵、正交矩阵、行列式奇偶性**。

(a) 从

$$
A^2=-I_n
$$

直接得到

$$
A(-A)=(-A)A=I_n.
$$

所以 $A$ 可逆，且 $A^{-1}=-A$。

(b) 验证候选逆矩阵：

$$
(I_n+A)\frac12(I_n-A)
=\frac12(I_n-A^2)
=\frac12(I_n+I_n)
=I_n.
$$

右乘同理，因此

$$
(I_n+A)^{-1}=\frac12(I_n-A).
$$

(c) 设

$$
Q=\frac1{\sqrt2}(I_n+A).
$$

若 $A^T=-A$，则

$$
Q^T=\frac1{\sqrt2}(I_n-A).
$$

于是

$$
Q^TQ=\frac12(I_n-A)(I_n+A)=\frac12(I_n-A^2)=I_n.
$$

所以 $Q$ 是正交矩阵。

(d) 对 $A^2=-I_n$ 取行列式：

$$
(\det A)^2=(-1)^n.
$$

左边是非零实数的平方，必须大于 $0$，所以右边也必须是正数。只有 $n$ 为偶数时 $(-1)^n=1$，因此 $n$ 是偶数。

解题思路：矩阵方程题要主动“找逆”。看到 $A^2=-I$，就想到 $A(-A)=I$；看到正交矩阵，就算 $Q^TQ$；看到维数奇偶，就用行列式把矩阵条件压成标量条件。""",
    },
    ("ss18", 6): {
        "problem": r"""Seien $n\in\mathbb N$ und $a_1,\ldots,a_{n+1}\in\mathbb R^n$ mit

$$
a_1+a_2+\cdots+a_{n+1}=0,
\qquad
\operatorname{rang}(a_1\ a_2\ \cdots\ a_{n+1})=n.
$$

Zeigen Sie:

(a) $a_1,\ldots,a_{n+1}$ sind linear abhängig.

(b) $a_{n+1}$ ist linear abhängig von $a_1-a_{n+1},\ldots,a_n-a_{n+1}$.

(c)

$$
\operatorname{rang}(a_1-a_{n+1}\ \cdots\ a_n-a_{n+1})=n.
$$

(d)

$$
\operatorname{rang}
\begin{pmatrix}
a_1&a_2&\cdots&a_{n+1}\\
1&1&\cdots&1
\end{pmatrix}
=n+1.
$$

(e) Für jedes $b\in\mathbb R^n$ gibt es genau ein $\lambda\in\mathbb R^{n+1}$ mit

$$
\sum_{j=1}^{n+1}\lambda_j a_j=b,
\qquad
\sum_{j=1}^{n+1}\lambda_j=1.
$$""",
        "zh_problem": r"""设 $n\in\mathbb N$，$a_1,\ldots,a_{n+1}\in\mathbb R^n$，满足

$$
a_1+a_2+\cdots+a_{n+1}=0,
\qquad
\operatorname{rang}(a_1\ a_2\ \cdots\ a_{n+1})=n.
$$

证明：

(a) $a_1,\ldots,a_{n+1}$ 线性相关。

(b) $a_{n+1}$ 可由 $a_1-a_{n+1},\ldots,a_n-a_{n+1}$ 线性表示。

(c)

$$
\operatorname{rang}(a_1-a_{n+1}\ \cdots\ a_n-a_{n+1})=n.
$$

(d)

$$
\operatorname{rang}
\begin{pmatrix}
a_1&a_2&\cdots&a_{n+1}\\
1&1&\cdots&1
\end{pmatrix}
=n+1.
$$

(e) 对每个 $b\in\mathbb R^n$，存在唯一 $\lambda\in\mathbb R^{n+1}$ 使

$$
\sum_{j=1}^{n+1}\lambda_j a_j=b,
\qquad
\sum_{j=1}^{n+1}\lambda_j=1.
$$""",
        "solution": r"""(a) Wegen

$$
1\cdot a_1+\cdots+1\cdot a_{n+1}=0
$$

liegt eine nichttriviale Linearkombination des Nullvektors vor. Also sind $a_1,\ldots,a_{n+1}$ linear abhängig.

Außerdem hat die Matrix mit den Spalten $a_1,\ldots,a_{n+1}$ Rang $n$. Daher hat ihr Kern Dimension

$$
(n+1)-n=1.
$$

Da $(1,\ldots,1)^T$ im Kern liegt, gilt

$$
\ker(a_1\ \cdots\ a_{n+1})=\operatorname{span}\{(1,\ldots,1)^T\}.
$$

(b) Aus der Summenbedingung folgt

$$
0=\sum_{j=1}^{n+1}a_j
=\sum_{j=1}^{n}(a_j-a_{n+1})+(n+1)a_{n+1}.
$$

Also

$$
a_{n+1}
=-\frac1{n+1}\sum_{j=1}^{n}(a_j-a_{n+1}).
$$

Damit liegt $a_{n+1}$ im Spann der Vektoren $a_1-a_{n+1},\ldots,a_n-a_{n+1}$.

(c) Wir zeigen lineare Unabhängigkeit. Sei

$$
\sum_{j=1}^{n}\lambda_j(a_j-a_{n+1})=0.
$$

Setze $\lambda=\sum_{j=1}^n\lambda_j$. Mit $a_{n+1}=-(a_1+\cdots+a_n)$ erhält man

$$
0=\sum_{j=1}^{n}\lambda_j a_j-\lambda a_{n+1}
=\sum_{j=1}^{n}(\lambda_j+\lambda)a_j.
$$

Das ist eine Relation der Spalten $a_1,\ldots,a_{n+1}$ mit letztem Koeffizienten $0$. Da alle Relationen Vielfache von $(1,\ldots,1)$ sind, muss sie die Nullrelation sein. Also

$$
\lambda_1=\cdots=\lambda_n=0.
$$

Die $n$ Differenzvektoren sind linear unabhängig, also haben sie Rang $n$.

(d) Sei

$$
\sum_{j=1}^{n+1}\lambda_j
\begin{pmatrix}a_j\\1\end{pmatrix}=0.
$$

Dann gelten gleichzeitig

$$
\sum_{j=1}^{n+1}\lambda_j a_j=0,
\qquad
\sum_{j=1}^{n+1}\lambda_j=0.
$$

Aus der ersten Gleichung folgt wegen der eindimensionalen Kernstruktur

$$
(\lambda_1,\ldots,\lambda_{n+1})=t(1,\ldots,1).
$$

Die zweite Gleichung ergibt $(n+1)t=0$, also $t=0$. Somit sind die $n+1$ Spalten linear unabhängig. Der Rang ist $n+1$.

(e) Die Matrix

$$
B=
\begin{pmatrix}
a_1&a_2&\cdots&a_{n+1}\\
1&1&\cdots&1
\end{pmatrix}
$$

ist nach (d) invertierbar. Für jedes $b\in\mathbb R^n$ besitzt daher

$$
B\lambda=
\begin{pmatrix}b\\1\end{pmatrix}
$$

genau eine Lösung $\lambda$. Diese Gleichung ist genau

$$
\sum_{j=1}^{n+1}\lambda_j a_j=b,
\qquad
\sum_{j=1}^{n+1}\lambda_j=1.
$$""",
        "zh_solution": r"""核心考点：**线性相关、秩、仿射坐标**。

(a) 因为

$$
a_1+\cdots+a_{n+1}=0,
$$

且系数全是 $1$，不是零系数组合，所以这些向量线性相关。又因为列矩阵有 $n+1$ 列、秩为 $n$，所以核维数为

$$
n+1-n=1.
$$

已知 $(1,\ldots,1)^T$ 是一个核向量，因此所有线性关系都只能是它的倍数。

(b) 把每个 $a_j$ 写成 $a_j-a_{n+1}+a_{n+1}$：

$$
0=\sum_{j=1}^{n+1}a_j
=\sum_{j=1}^{n}(a_j-a_{n+1})+(n+1)a_{n+1}.
$$

所以

$$
a_{n+1}
=-\frac1{n+1}\sum_{j=1}^{n}(a_j-a_{n+1}).
$$

(c) 证明差向量满秩，只要证它们线性无关。设

$$
\sum_{j=1}^{n}\lambda_j(a_j-a_{n+1})=0.
$$

令 $\lambda=\sum_{j=1}^{n}\lambda_j$，并用 $a_{n+1}=-(a_1+\cdots+a_n)$，得到

$$
0=\sum_{j=1}^{n}(\lambda_j+\lambda)a_j.
$$

这相当于 $a_1,\ldots,a_{n+1}$ 的一个线性关系，而且最后一个系数是 $0$。但所有关系都是 $(1,\ldots,1)$ 的倍数，所以只能是零关系。因此所有 $\lambda_j=0$，差向量线性无关，秩为 $n$。

(d) 看增广后的 $n+1$ 个列向量：

$$
\begin{pmatrix}a_j\\1\end{pmatrix}.
$$

若

$$
\sum_{j=1}^{n+1}\lambda_j
\begin{pmatrix}a_j\\1\end{pmatrix}=0,
$$

则

$$
\sum_{j=1}^{n+1}\lambda_j a_j=0,
\qquad
\sum_{j=1}^{n+1}\lambda_j=0.
$$

第一条说明 $\lambda=t(1,\ldots,1)$，第二条给出 $(n+1)t=0$，所以 $t=0$。列向量线性无关，因此秩是 $n+1$。

(e) 上一步说明矩阵

$$
B=
\begin{pmatrix}
a_1&a_2&\cdots&a_{n+1}\\
1&1&\cdots&1
\end{pmatrix}
$$

可逆。于是对任意 $b$，方程

$$
B\lambda=
\begin{pmatrix}b\\1\end{pmatrix}
$$

有唯一解。这正好等价于

$$
\sum_{j=1}^{n+1}\lambda_j a_j=b,
\qquad
\sum_{j=1}^{n+1}\lambda_j=1.
$$

解题思路：这题其实在讲“仿射坐标”。$a_1+\cdots+a_{n+1}=0$ 给出唯一方向的线性关系；加上一行全 $1$ 后，仿射条件 $\sum\lambda_j=1$ 把表示变成唯一。""",
    },
    ("ss18", 8): {
        "problem": r"""Seien $n\in\mathbb N$, $n\ge3$, $e_1,\ldots,e_n$ die Einheitsvektoren von $\mathbb R^n$ und

$$
e=\sum_{j=1}^{n}e_j,
\qquad
A=e(e_1+e_n)^T\in\mathbb R^{n\times n}.
$$

(a) Geben Sie $A$ für $n=3$ und $n=4$ explizit an.

(b) Zeigen Sie, dass $e_2,\ldots,e_{n-1},e_1-e_n$ und $e$ Eigenvektoren von $A$ sind, und geben Sie die Eigenwerte an.

(c) Zeigen Sie, dass $A$ diagonalisierbar ist.

(d) Zeigen Sie, dass $\mathbb R^n$ keine Orthonormalbasis aus Eigenvektoren von $A$ besitzt.""",
        "zh_problem": r"""设 $n\in\mathbb N$，$n\ge3$，$e_1,\ldots,e_n$ 是 $\mathbb R^n$ 的标准单位向量，并令

$$
e=\sum_{j=1}^{n}e_j,
\qquad
A=e(e_1+e_n)^T\in\mathbb R^{n\times n}.
$$

(a) 写出 $n=3$ 和 $n=4$ 时的矩阵 $A$。

(b) 证明 $e_2,\ldots,e_{n-1},e_1-e_n$ 和 $e$ 都是 $A$ 的特征向量，并给出对应特征值。

(c) 证明 $A$ 可对角化。

(d) 证明 $\mathbb R^n$ 不存在由 $A$ 的特征向量组成的标准正交基。""",
        "solution": r"""(a) Da $e=(1,\ldots,1)^T$ und $(e_1+e_n)^T=(1,0,\ldots,0,1)$, hat $A$ nur in der ersten und letzten Spalte Einträge $1$:

$$
A=
\begin{pmatrix}
1&0&\cdots&0&1\\
1&0&\cdots&0&1\\
\vdots&\vdots&&\vdots&\vdots\\
1&0&\cdots&0&1
\end{pmatrix}.
$$

Für $n=3$:

$$
A_3=
\begin{pmatrix}
1&0&1\\
1&0&1\\
1&0&1
\end{pmatrix}.
$$

Für $n=4$:

$$
A_4=
\begin{pmatrix}
1&0&0&1\\
1&0&0&1\\
1&0&0&1\\
1&0&0&1
\end{pmatrix}.
$$

(b) Für $2\le j\le n-1$ gilt

$$
Ae_j=e(e_1+e_n)^Te_j=0,
$$

also ist $e_j$ Eigenvektor zum Eigenwert $0$.

Weiter:

$$
A(e_1-e_n)=e(e_1+e_n)^T(e_1-e_n)=e(1-1)=0,
$$

also gehört $e_1-e_n$ ebenfalls zum Eigenwert $0$.

Schließlich

$$
Ae=e(e_1+e_n)^Te=e(1+1)=2e.
$$

Also ist $e$ Eigenvektor zum Eigenwert $2$.

(c) Die Vektoren

$$
e_2,\ldots,e_{n-1},\ e_1-e_n,\ e
$$

sind $n$ Vektoren. Zeige ihre lineare Unabhängigkeit. Sei

$$
\sum_{j=2}^{n-1}\alpha_j e_j+\beta(e_1-e_n)+\gamma e=0.
$$

Aus der ersten und letzten Koordinate folgt

$$
\beta+\gamma=0,
\qquad
-\beta+\gamma=0.
$$

Daraus folgt $\beta=\gamma=0$. Dann ergeben die mittleren Koordinaten $\alpha_j=0$ für alle $j$. Also bilden diese Eigenvektoren eine Basis von $\mathbb R^n$. Damit ist $A$ diagonalisierbar.

(d) Eine Orthonormalbasis aus Eigenvektoren müsste Eigenräume zu verschiedenen Eigenwerten orthogonal machen. Hier ist

$$
E_2=\operatorname{span}\{e\},
\qquad
E_0=\ker A=\{x\in\mathbb R^n\mid x_1+x_n=0\}.
$$

Aber für $2\le j\le n-1$ gilt $e_j\in E_0$ und

$$
\langle e_j,e\rangle=1\ne0.
$$

Also ist $E_0$ nicht orthogonal zu $E_2$. Daher kann es keine Orthonormalbasis aus Eigenvektoren von $A$ geben.""",
        "zh_solution": r"""核心考点：**秩一矩阵、特征向量、对角化、正交对角化**。

(a) 因为

$$
e=(1,\ldots,1)^T,\qquad (e_1+e_n)^T=(1,0,\ldots,0,1),
$$

所以 $A=e(e_1+e_n)^T$ 的第一列和最后一列全是 $1$，中间列全是 $0$。

$$
A_3=
\begin{pmatrix}
1&0&1\\
1&0&1\\
1&0&1
\end{pmatrix},
\qquad
A_4=
\begin{pmatrix}
1&0&0&1\\
1&0&0&1\\
1&0&0&1\\
1&0&0&1
\end{pmatrix}.
$$

(b) 对 $2\le j\le n-1$，

$$
Ae_j=e(e_1+e_n)^Te_j=0,
$$

所以 $e_j$ 是特征值 $0$ 的特征向量。

再看

$$
A(e_1-e_n)=e(1-1)=0,
$$

所以 $e_1-e_n$ 也属于特征值 $0$。

最后

$$
Ae=e(e_1+e_n)^Te=e(1+1)=2e,
$$

所以 $e$ 的特征值是 $2$。

(c) 现在已经有 $n$ 个特征向量：

$$
e_2,\ldots,e_{n-1},\ e_1-e_n,\ e.
$$

设它们线性组合为零：

$$
\sum_{j=2}^{n-1}\alpha_j e_j+\beta(e_1-e_n)+\gamma e=0.
$$

看第一和最后一个坐标：

$$
\beta+\gamma=0,\qquad -\beta+\gamma=0.
$$

推出 $\beta=\gamma=0$，再看中间坐标得到所有 $\alpha_j=0$。所以这些特征向量线性无关，组成 $\mathbb R^n$ 的一组基，故 $A$ 可对角化。

(d) 如果存在由特征向量组成的标准正交基，那么不同特征值对应的特征空间必须相互正交。这里

$$
E_2=\operatorname{span}\{e\},
\qquad
E_0=\ker A.
$$

但 $e_2\in E_0$，同时

$$
\langle e_2,e\rangle=1\ne0.
$$

所以 $E_0$ 和 $E_2$ 不是正交的，不能构造出全由特征向量组成的标准正交基。

解题思路：对角化只要求“有一组特征向量基”；标准正交特征向量基更强，它要求不同特征空间互相垂直。这题就是可对角化，但不能正交对角化。""",
    },
    ("ss19", 1): {
        "problem": r"""Sei

$$
A=
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}.
$$

(a) Zeigen Sie für alle $n\in\mathbb N$:

$$
A^n=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}.
$$

(b) Berechnen Sie $A^{-n}$ für $n\in\mathbb N$.""",
        "zh_problem": r"""设

$$
A=
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}.
$$

(a) 证明对所有 $n\in\mathbb N$：

$$
A^n=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}.
$$

(b) 求 $A^{-n}$。""",
        "solution": r"""(a) Wir beweisen die Formel durch Induktion.

Für $n=1$ gilt

$$
\begin{pmatrix}
2^1&0\\
2^1-3^1&3^1
\end{pmatrix}
=
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}
=A.
$$

Sei nun

$$
A^n=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}.
$$

Dann

$$
A^{n+1}=A^nA
=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}.
$$

Ausmultiplizieren ergibt

$$
A^{n+1}
=
\begin{pmatrix}
2^{n+1}&0\\
2(2^n-3^n)-3^n&3^{n+1}
\end{pmatrix}
=
\begin{pmatrix}
2^{n+1}&0\\
2^{n+1}-3^{n+1}&3^{n+1}
\end{pmatrix}.
$$

(b) Da $\det A=6\ne0$, ist $A$ invertierbar. Es gilt

$$
A^{-n}=(A^n)^{-1}.
$$

Für eine Matrix

$$
\begin{pmatrix}p&0\\q&r\end{pmatrix}
$$

mit $p,r\ne0$ ist die Inverse

$$
\begin{pmatrix}
p^{-1}&0\\
-q/(pr)&r^{-1}
\end{pmatrix}.
$$

Mit $p=2^n$, $q=2^n-3^n$, $r=3^n$ erhält man

$$
A^{-n}
=
\begin{pmatrix}
2^{-n}&0\\
2^{-n}-3^{-n}&3^{-n}
\end{pmatrix}.
$$""",
        "zh_solution": r"""核心考点：**矩阵幂、归纳法、负幂**。

(a) 先验证 $n=1$：

$$
\begin{pmatrix}
2&0\\
2-3&3
\end{pmatrix}
=
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}
=A.
$$

假设

$$
A^n=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}.
$$

则

$$
A^{n+1}=A^nA
=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix}
\begin{pmatrix}
2&0\\
-1&3
\end{pmatrix}.
$$

乘出来：

$$
A^{n+1}
=
\begin{pmatrix}
2^{n+1}&0\\
2(2^n-3^n)-3^n&3^{n+1}
\end{pmatrix}
=
\begin{pmatrix}
2^{n+1}&0\\
2^{n+1}-3^{n+1}&3^{n+1}
\end{pmatrix}.
$$

归纳完成。

(b) 负幂不是把指数直接乱改，要先用

$$
A^{-n}=(A^n)^{-1}.
$$

因为

$$
A^n=
\begin{pmatrix}
2^n&0\\
2^n-3^n&3^n
\end{pmatrix},
$$

三角矩阵求逆得到

$$
A^{-n}
=
\begin{pmatrix}
2^{-n}&0\\
2^{-n}-3^{-n}&3^{-n}
\end{pmatrix}.
$$

解题思路：先用归纳法拿到 $A^n$ 的闭式，再求逆。下三角矩阵的逆仍是下三角矩阵，所以计算量很小。""",
    },
    ("ss19", 3): {
        "problem": r"""Seien $n\in\mathbb N$ und $a,b\in\mathbb R^n$. Betrachten Sie

$$
f:\mathbb R^n\to\mathbb R^n,
\qquad
f(x)=x+(a^Tx)b.
$$

(a) Zeigen Sie, dass $f$ linear ist.

(b) Zeigen Sie, dass $M=I_n+ba^T$ die darstellende Matrix von $f$ ist.

(c) Berechnen Sie $\operatorname{spur}(M)$.

(d) Zeigen Sie $\ker f\subseteq\operatorname{span}(b)$.

(e) Zeigen Sie unter Verwendung von (d):

$$
f\text{ invertierbar}
\quad\Longleftrightarrow\quad
a^Tb\ne-1.
$$

(f) Zeigen Sie

$$
\operatorname{rang}(M)=
\begin{cases}
n,&a^Tb\ne-1,\\
n-1,&a^Tb=-1.
\end{cases}
$$""",
        "zh_problem": r"""设 $n\in\mathbb N$，$a,b\in\mathbb R^n$。定义

$$
f:\mathbb R^n\to\mathbb R^n,
\qquad
f(x)=x+(a^Tx)b.
$$

(a) 证明 $f$ 线性。

(b) 证明 $M=I_n+ba^T$ 是 $f$ 的表示矩阵。

(c) 求 $\operatorname{spur}(M)$。

(d) 证明 $\ker f\subseteq\operatorname{span}(b)$。

(e) 利用 (d) 证明：

$$
f\text{ 可逆}
\quad\Longleftrightarrow\quad
a^Tb\ne-1.
$$

(f) 证明

$$
\operatorname{rang}(M)=
\begin{cases}
n,&a^Tb\ne-1,\\
n-1,&a^Tb=-1.
\end{cases}
$$""",
        "solution": r"""(a) Für $x,y\in\mathbb R^n$ und $\lambda,\mu\in\mathbb R$ gilt

$$
f(\lambda x+\mu y)
=\lambda x+\mu y+a^T(\lambda x+\mu y)b
=\lambda x+\mu y+\lambda(a^Tx)b+\mu(a^Ty)b.
$$

Also

$$
f(\lambda x+\mu y)=\lambda f(x)+\mu f(y).
$$

Damit ist $f$ linear.

(b) Es gilt

$$
(I_n+ba^T)x=x+b(a^Tx)=x+(a^Tx)b=f(x).
$$

Also ist $M=I_n+ba^T$ die darstellende Matrix.

(c) Schreibe $a=(a_1,\ldots,a_n)^T$ und $b=(b_1,\ldots,b_n)^T$. Dann hat $ba^T$ Diagonaleinträge $b_i a_i$. Daher

$$
\operatorname{spur}(ba^T)=\sum_{i=1}^n b_i a_i=a^Tb.
$$

Somit

$$
\operatorname{spur}(M)=\operatorname{spur}(I_n)+\operatorname{spur}(ba^T)=n+a^Tb.
$$

(d) Sei $x\in\ker f$. Dann

$$
0=f(x)=x+(a^Tx)b.
$$

Also

$$
x=-(a^Tx)b\in\operatorname{span}(b).
$$

(e) Wegen (d) reicht es, Vektoren der Form $x=tb$ zu prüfen. Dann

$$
f(tb)=tb+(a^Ttb)b=t(1+a^Tb)b.
$$

Falls $a^Tb\ne-1$, ist $t(1+a^Tb)b=0$ nur mit $t=0$ möglich; also ist $\ker f=\{0\}$ und $f$ ist invertierbar.

Falls $a^Tb=-1$, gilt

$$
f(b)=b+(a^Tb)b=b-b=0.
$$

Dann ist $b\ne0$ und der Kern ist nicht trivial. Also ist $f$ nicht invertierbar.

(f) Im Fall $a^Tb\ne-1$ ist $f$ invertierbar, daher

$$
\operatorname{rang}(M)=n.
$$

Im Fall $a^Tb=-1$ gilt $\ker f=\operatorname{span}(b)$, also

$$
\dim\ker f=1.
$$

Nach dem Dimensionssatz folgt

$$
\operatorname{rang}(M)=n-\dim\ker f=n-1.
$$""",
        "zh_solution": r"""核心考点：**秩一扰动 $I+ba^T$、线性映射、核与秩**。

(a) 对 $x,y\in\mathbb R^n$、$\lambda,\mu\in\mathbb R$：

$$
f(\lambda x+\mu y)
=\lambda x+\mu y+a^T(\lambda x+\mu y)b
=\lambda f(x)+\mu f(y).
$$

所以 $f$ 线性。

(b) 直接算矩阵作用：

$$
(I_n+ba^T)x=x+b(a^Tx)=x+(a^Tx)b=f(x).
$$

因此表示矩阵是

$$
M=I_n+ba^T.
$$

(c) $ba^T$ 的第 $i$ 个对角元是 $b_i a_i$，所以

$$
\operatorname{spur}(ba^T)=\sum_{i=1}^n b_i a_i=a^Tb.
$$

于是

$$
\operatorname{spur}(M)=n+a^Tb.
$$

(d) 若 $x\in\ker f$，则

$$
0=x+(a^Tx)b,
$$

所以

$$
x=-(a^Tx)b\in\operatorname{span}(b).
$$

(e) 核里的向量只能沿着 $b$ 的方向，所以令 $x=tb$：

$$
f(tb)=t(1+a^Tb)b.
$$

若 $a^Tb\ne-1$，只能得到 $t=0$，所以核为 $\{0\}$，同维空间上线性映射可逆。

若 $a^Tb=-1$，则

$$
f(b)=0.
$$

核非零，因此不可逆。

(f) 当 $a^Tb\ne-1$ 时，$f$ 可逆，秩为 $n$。当 $a^Tb=-1$ 时，

$$
\ker f=\operatorname{span}(b),
\qquad
\dim\ker f=1.
$$

由维数公式

$$
\operatorname{rang}(M)=n-\dim\ker f=n-1.
$$

解题思路：这题核心是 $ba^T$ 是秩一扰动。先把 $f(x)$ 写成 $(I+ba^T)x$，再用核判断可逆；最后用 $\dim\ker+\operatorname{rang}=n$ 收尾。""",
    },
    ("ss19", 4): {
        "problem": r"""Sei $\alpha\in\mathbb R$ und

$$
A=
\begin{pmatrix}
1&0&1\\
0&\alpha&0\\
0&0&1
\end{pmatrix}.
$$

(a) Untersuchen Sie, welche Einheitsvektoren Eigenvektoren von $A$ sind, und geben Sie die Eigenwerte an.

(b) Berechnen Sie das charakteristische Polynom und alle Eigenwerte mit algebraischer Vielfachheit.

(c) Bestimmen Sie die geometrische Vielfachheit jedes Eigenwerts in Abhängigkeit von $\alpha$.

(d) Untersuchen Sie die Diagonalisierbarkeit von $A$ in Abhängigkeit von $\alpha$.""",
        "zh_problem": r"""设 $\alpha\in\mathbb R$，

$$
A=
\begin{pmatrix}
1&0&1\\
0&\alpha&0\\
0&0&1
\end{pmatrix}.
$$

(a) 判断哪些标准单位向量是 $A$ 的特征向量，并给出对应特征值。

(b) 求特征多项式以及各特征值的代数重数。

(c) 根据 $\alpha$ 分类求各特征值的几何重数。

(d) 判断 $A$ 何时可对角化。""",
        "solution": r"""(a) Die Spalten von $A$ liefern sofort:

$$
Ae_1=e_1,
\qquad
Ae_2=\alpha e_2,
\qquad
Ae_3=e_1+e_3.
$$

Also sind $e_1$ und $e_2$ Eigenvektoren, mit Eigenwerten $1$ bzw. $\alpha$. Der Vektor $e_3$ ist kein Eigenvektor, denn $e_1+e_3$ ist kein Vielfaches von $e_3$.

(b) Da $A-\lambda I$ obere Dreiecksgestalt hat,

$$
\chi_A(\lambda)=\det(A-\lambda I)
=
\det
\begin{pmatrix}
1-\lambda&0&1\\
0&\alpha-\lambda&0\\
0&0&1-\lambda
\end{pmatrix}
=(1-\lambda)^2(\alpha-\lambda).
$$

Falls $\alpha\ne1$, sind die Eigenwerte:

$$
\lambda=1\quad\text{mit algebraischer Vielfachheit }2,
\qquad
\lambda=\alpha\quad\text{mit algebraischer Vielfachheit }1.
$$

Falls $\alpha=1$, ist der einzige Eigenwert

$$
\lambda=1
$$

mit algebraischer Vielfachheit $3$.

(c) Für $\lambda=1$:

$$
A-I=
\begin{pmatrix}
0&0&1\\
0&\alpha-1&0\\
0&0&0
\end{pmatrix}.
$$

Ist $\alpha\ne1$, dann gelten $x_3=0$ und $x_2=0$, also

$$
E_1=\operatorname{span}\{e_1\},
\qquad
\dim E_1=1.
$$

Für $\lambda=\alpha$ bei $\alpha\ne1$ ist wegen der algebraischen Vielfachheit $1$ automatisch

$$
\dim E_\alpha=1.
$$

Ist $\alpha=1$, dann

$$
A-I=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix},
$$

also $x_3=0$ und

$$
E_1=\operatorname{span}\{e_1,e_2\},
\qquad
\dim E_1=2.
$$

(d) Für $\alpha\ne1$ ist die Summe der geometrischen Vielfachheiten

$$
1+1=2<3.
$$

Für $\alpha=1$ ist die geometrische Vielfachheit des einzigen Eigenwerts gleich $2<3$.

In beiden Fällen gibt es nicht genug linear unabhängige Eigenvektoren. Also ist $A$ für kein $\alpha\in\mathbb R$ diagonalisierbar.""",
        "zh_solution": r"""核心考点：**特征值、几何重数、对角化判定**。

(a) 看标准基向量就是看矩阵列：

$$
Ae_1=e_1,\qquad Ae_2=\alpha e_2,\qquad Ae_3=e_1+e_3.
$$

所以 $e_1$ 是特征值 $1$ 的特征向量，$e_2$ 是特征值 $\alpha$ 的特征向量，$e_3$ 不是特征向量。

(b) 因为 $A-\lambda I$ 是上三角矩阵，

$$
\chi_A(\lambda)
=\det(A-\lambda I)
=(1-\lambda)^2(\alpha-\lambda).
$$

若 $\alpha\ne1$，特征值是

$$
1\text{（代数重数 }2\text{）},\qquad
\alpha\text{（代数重数 }1\text{）}.
$$

若 $\alpha=1$，唯一特征值是 $1$，代数重数 $3$。

(c) 对 $\lambda=1$：

$$
A-I=
\begin{pmatrix}
0&0&1\\
0&\alpha-1&0\\
0&0&0
\end{pmatrix}.
$$

当 $\alpha\ne1$ 时，$x_2=0,x_3=0$，所以

$$
E_1=\operatorname{span}\{e_1\},
\qquad
\dim E_1=1.
$$

此时 $\lambda=\alpha$ 的代数重数是 $1$，所以几何重数也是 $1$。

当 $\alpha=1$ 时，

$$
A-I=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix},
$$

所以 $x_3=0$，

$$
E_1=\operatorname{span}\{e_1,e_2\},
\qquad
\dim E_1=2.
$$

(d) 对角化需要总共 $3$ 个线性无关特征向量。若 $\alpha\ne1$，几何重数总和是 $1+1=2$；若 $\alpha=1$，唯一特征空间维数是 $2$。两种情况都不足 $3$。

因此 $A$ 对任何 $\alpha\in\mathbb R$ 都不可对角化。

解题思路：上三角矩阵的特征值直接看对角线，但对角线上重复出现的 $1$ 不保证有足够特征向量。必须回到 $(A-\lambda I)x=0$ 算几何重数。""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss19-2", 2): {
        "problem": r"""Betrachten Sie

$$
G=\left\{
M(a)=
\begin{pmatrix}
2a+1&-a\\
4a&-2a+1
\end{pmatrix}
\;\middle|\;a\in\mathbb R
\right\}.
$$

(a) Zeigen Sie, dass $G$ mit der Matrixmultiplikation eine kommutative Untergruppe von $GL(2,\mathbb R)$ ist.

(b) Zeigen Sie, dass

$$
\varphi:\mathbb R\to G,\qquad \varphi(a)=M(a)
$$

ein Gruppenhomomorphismus von $(\mathbb R,+)$ nach $(G,\cdot)$ ist.

(c) Berechnen Sie

$$
\begin{pmatrix}
-1&1\\
-4&3
\end{pmatrix}^n
\qquad(n\in\mathbb N).
$$""",
        "zh_problem": r"""考虑矩阵集合

$$
G=\left\{
M(a)=
\begin{pmatrix}
2a+1&-a\\
4a&-2a+1
\end{pmatrix}
\;\middle|\;a\in\mathbb R
\right\}.
$$

(a) 证明 $G$ 在矩阵乘法下是 $GL(2,\mathbb R)$ 的交换子群。

(b) 证明

$$
\varphi:\mathbb R\to G,\qquad \varphi(a)=M(a)
$$

是从 $(\mathbb R,+)$ 到 $(G,\cdot)$ 的群同态。

(c) 计算

$$
\begin{pmatrix}
-1&1\\
-4&3
\end{pmatrix}^n
\qquad(n\in\mathbb N).
$$""",
        "solution": r"""Zunächst

$$
\det M(a)=(2a+1)(-2a+1)-(-a)4a=1.
$$

Also gilt $G\subset GL(2,\mathbb R)$.

Für $a,b\in\mathbb R$ rechnet man aus:

$$
M(a)M(b)
=
\begin{pmatrix}
2(a+b)+1&-(a+b)\\
4(a+b)&-2(a+b)+1
\end{pmatrix}
=M(a+b).
$$

Daraus folgen sofort:

$$
M(0)=I_2,\qquad M(a)^{-1}=M(-a),
$$

und

$$
M(a)M(b)=M(a+b)=M(b+a)=M(b)M(a).
$$

Damit ist $G$ eine kommutative Untergruppe von $GL(2,\mathbb R)$.

Für die Abbildung $\varphi(a)=M(a)$ gilt

$$
\varphi(a+b)=M(a+b)=M(a)M(b)=\varphi(a)\varphi(b).
$$

Also ist $\varphi$ ein Gruppenhomomorphismus.

Für (c) erkennt man

$$
\begin{pmatrix}
-1&1\\
-4&3
\end{pmatrix}
=M(-1).
$$

Daher

$$
M(-1)^n=M(-n).
$$

Also

$$
\begin{pmatrix}
-1&1\\
-4&3
\end{pmatrix}^n
=
\begin{pmatrix}
1-2n&n\\
-4n&1+2n
\end{pmatrix}.
$$""",
        "zh_solution": r"""核心考点：**参数矩阵群与同态**。

先证明每个元素可逆：

$$
\det M(a)=(2a+1)(-2a+1)-(-a)4a=1.
$$

所以 $M(a)\in GL(2,\mathbb R)$。

关键乘法公式是

$$
M(a)M(b)=M(a+b).
$$

这一个公式同时给出封闭性、单位元、逆元和交换性：

$$
M(0)=I_2,\qquad M(a)^{-1}=M(-a),
$$

并且

$$
M(a)M(b)=M(a+b)=M(b+a)=M(b)M(a).
$$

因此 $G$ 是交换子群。

同态也直接来自同一个公式：

$$
\varphi(a+b)=M(a+b)=M(a)M(b)=\varphi(a)\varphi(b).
$$

最后

$$
\begin{pmatrix}-1&1\\-4&3\end{pmatrix}=M(-1),
$$

所以

$$
\begin{pmatrix}-1&1\\-4&3\end{pmatrix}^n
=M(-n)
=
\begin{pmatrix}
1-2n&n\\
-4n&1+2n
\end{pmatrix}.
$$

解题思路：群题不要逐条硬背定义，先算两个一般元素的乘积。这里乘积把参数 $a,b$ 变成 $a+b$，整个群结构就被“翻译”为实数加法了。""",
    },
    ("ss19-2", 3): {
        "problem": r"""Gegeben seien $t\in\mathbb R$ und

$$
A=
\begin{pmatrix}
1&1&0\\
1&1&t\\
0&1&1
\end{pmatrix}.
$$

(a) Berechnen Sie $\det A$ und bestimmen Sie, für welche $t$ die Matrix invertierbar ist.

(b) Berechnen Sie $A^{-1}$ für alle invertierbaren Fälle.""",
        "zh_problem": r"""给定 $t\in\mathbb R$ 与

$$
A=
\begin{pmatrix}
1&1&0\\
1&1&t\\
0&1&1
\end{pmatrix}.
$$

(a) 求 $\det A$，并判断哪些 $t$ 使 $A$ 可逆。

(b) 对所有可逆情形求 $A^{-1}$。""",
        "solution": r"""Mit der Zeilenoperation $R_2\leftarrow R_2-R_1$ erhält man

$$
\det A
=
\det
\begin{pmatrix}
1&1&0\\
0&0&t\\
0&1&1
\end{pmatrix}
=-t.
$$

Also ist $A$ genau dann invertierbar, wenn

$$
t\ne0.
$$

Für $t\ne0$ ergibt Gauss-Jordan

$$
A^{-1}
=
\begin{pmatrix}
\frac{t-1}{t}&\frac1t&-1\\
\frac1t&-\frac1t&1\\
-\frac1t&\frac1t&0
\end{pmatrix}.
$$

Probe:

$$
A A^{-1}
=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$""",
        "zh_solution": r"""核心考点：**参数行列式与逆矩阵**。

先用 $R_2\leftarrow R_2-R_1$：

$$
\det A
=
\det
\begin{pmatrix}
1&1&0\\
0&0&t\\
0&1&1
\end{pmatrix}
=-t.
$$

因此

$$
A\text{ 可逆}\Longleftrightarrow t\ne0.
$$

当 $t\ne0$ 时，用 Gauss-Jordan 求得

$$
A^{-1}
=
\begin{pmatrix}
\frac{t-1}{t}&\frac1t&-1\\
\frac1t&-\frac1t&1\\
-\frac1t&\frac1t&0
\end{pmatrix}.
$$

验算：

$$
A A^{-1}=I_3.
$$

解题思路：参数题先算行列式确定可逆范围。只有 $t\ne0$ 时才允许除以 $t$，所以求逆过程里所有 $\frac1t$ 都是合法的。""",
    },
    ("ss19-2", 4): {
        "problem": r"""Gegeben seien $a,b\in\mathbb R$ und

$$
A=
\begin{pmatrix}
1&0&-1&a\\
1&1&0&0\\
a&1&1&a\\
0&b&b&0
\end{pmatrix}.
$$

Berechnen Sie $\operatorname{rang}(A)$ in Abhängigkeit von $a,b$ und geben Sie die Fälle tabellarisch an.""",
        "zh_problem": r"""给定 $a,b\in\mathbb R$ 与

$$
A=
\begin{pmatrix}
1&0&-1&a\\
1&1&0&0\\
a&1&1&a\\
0&b&b&0
\end{pmatrix}.
$$

求 $\operatorname{rang}(A)$ 关于 $a,b$ 的分类，并用表格列出。""",
        "solution": r"""Durch elementare Zeilenumformungen erhält man

$$
A\sim
\begin{pmatrix}
1&0&-1&a\\
0&1&1&-a\\
0&0&a&2a-a^2\\
0&0&0&ab
\end{pmatrix}.
$$

Jetzt liest man die Fälle ab.

Wenn $a=0$, bleiben nur die ersten beiden Pivotzeilen:

$$
\operatorname{rang}(A)=2.
$$

Wenn $a\ne0$ und $b=0$, liefert die dritte Zeile einen Pivot, die vierte nicht:

$$
\operatorname{rang}(A)=3.
$$

Wenn $a\ne0$ und $b\ne0$, liefern dritte und vierte Zeile Pivots:

$$
\operatorname{rang}(A)=4.
$$

| Rang | Bedingung |
|---:|---|
| $2$ | $a=0$ |
| $3$ | $a\ne0$ und $b=0$ |
| $4$ | $a\ne0$ und $b\ne0$ |""",
        "zh_solution": r"""核心考点：**参数矩阵秩分类**。

行化简得到阶梯形：

$$
A\sim
\begin{pmatrix}
1&0&-1&a\\
0&1&1&-a\\
0&0&a&2a-a^2\\
0&0&0&ab
\end{pmatrix}.
$$

现在只看第三、第四行是否出现主元。

若 $a=0$，第三、四行都不能提供主元，所以

$$
\operatorname{rang}(A)=2.
$$

若 $a\ne0$ 且 $b=0$，第三行有主元，第四行没有主元，所以

$$
\operatorname{rang}(A)=3.
$$

若 $a\ne0$ 且 $b\ne0$，第三行和第四行都有主元，所以

$$
\operatorname{rang}(A)=4.
$$

| 秩 | 参数条件 |
|---:|---|
| $2$ | $a=0$ |
| $3$ | $a\ne0,\ b=0$ |
| $4$ | $a\ne0,\ b\ne0$ |

解题思路：参数秩题的目标是把参数压到阶梯形主元位置。这里最终只需要看 $a$ 和 $ab$ 是否为零。""",
    },
    ("ss19-2", 6): {
        "problem": r"""Seien $n\in\mathbb N$, $a\in\mathbb R^n$ und

$$
f:\mathbb R^{n+1}\to\mathbb R^{n+1},
\qquad
f\begin{pmatrix}x\\ \xi\end{pmatrix}
=
\begin{pmatrix}
x+\xi a\\
\sum_{j=1}^n x_j
\end{pmatrix},
$$

wobei $x\in\mathbb R^n$ und $\xi\in\mathbb R$.

(a) Zeigen Sie, dass $f$ linear ist.

(b) Geben Sie die darstellende Matrix von $f$ an und berechnen Sie Rang und Determinante.

(c) Zeigen Sie

$$
f\text{ bijektiv}
\quad\Longleftrightarrow\quad
\sum_{j=1}^n a_j\ne0.
$$""",
        "zh_problem": r"""设 $n\in\mathbb N$，$a\in\mathbb R^n$，定义

$$
f:\mathbb R^{n+1}\to\mathbb R^{n+1},
\qquad
f\begin{pmatrix}x\\ \xi\end{pmatrix}
=
\begin{pmatrix}
x+\xi a\\
\sum_{j=1}^n x_j
\end{pmatrix},
$$

其中 $x\in\mathbb R^n$，$\xi\in\mathbb R$。

(a) 证明 $f$ 线性。

(b) 写出 $f$ 的表示矩阵，并求秩与行列式。

(c) 证明

$$
f\text{ 双射}
\quad\Longleftrightarrow\quad
\sum_{j=1}^n a_j\ne0.
$$""",
        "solution": r"""(a) Jede Komponente von $f$ ist eine lineare Kombination der Koordinaten von $(x,\xi)$. Also ist $f$ linear. Direkt:

$$
f\left(\lambda\begin{pmatrix}x\\ \xi\end{pmatrix}
+\mu\begin{pmatrix}y\\ \eta\end{pmatrix}\right)
=
\lambda f\begin{pmatrix}x\\ \xi\end{pmatrix}
+\mu f\begin{pmatrix}y\\ \eta\end{pmatrix}.
$$

(b) In Blockform ist die Matrix

$$
M=
\begin{pmatrix}
I_n&a\\
\mathbf 1^T&0
\end{pmatrix},
\qquad
\mathbf 1^T=(1,\ldots,1).
$$

Mit dem Schur-Komplement erhält man

$$
\det M
=
\det(I_n)\cdot(0-\mathbf 1^T a)
=
-\sum_{j=1}^n a_j.
$$

Da die ersten $n$ Zeilen wegen des Blocks $I_n$ linear unabhängig sind, gilt

$$
\operatorname{rang}(M)=
\begin{cases}
n+1,&\sum_{j=1}^n a_j\ne0,\\
n,&\sum_{j=1}^n a_j=0.
\end{cases}
$$

(c) Da Definitions- und Zielraum beide Dimension $n+1$ haben, ist $f$ genau dann bijektiv, wenn $\det M\ne0$. Also

$$
f\text{ bijektiv}
\Longleftrightarrow
\det M\ne0
\Longleftrightarrow
\sum_{j=1}^n a_j\ne0.
$$""",
        "zh_solution": r"""核心考点：**线性映射的矩阵表示、块矩阵行列式、双射判定**。

(a) $f$ 的每个分量都是 $x_1,\ldots,x_n,\xi$ 的线性组合，所以 $f$ 线性。也可以直接写：

$$
f(\lambda u+\mu v)=\lambda f(u)+\mu f(v).
$$

(b) 把输入写成 $\begin{pmatrix}x\\ \xi\end{pmatrix}$，矩阵就是

$$
M=
\begin{pmatrix}
I_n&a\\
\mathbf 1^T&0
\end{pmatrix},
\qquad
\mathbf 1^T=(1,\ldots,1).
$$

用块矩阵的 Schur 补：

$$
\det M
=0-\mathbf 1^Ta
=-\sum_{j=1}^n a_j.
$$

前 $n$ 行因为有 $I_n$，一定线性无关，所以秩至少为 $n$。最后一行是否增加一个维度，就看行列式是否非零：

$$
\operatorname{rang}(M)=
\begin{cases}
n+1,&\sum_{j=1}^n a_j\ne0,\\
n,&\sum_{j=1}^n a_j=0.
\end{cases}
$$

(c) 同维空间上线性映射双射等价于表示矩阵可逆：

$$
f\text{ 双射}
\Longleftrightarrow
\det M\ne0
\Longleftrightarrow
\sum_{j=1}^n a_j\ne0.
$$

解题思路：这题的矩阵是“单位矩阵加一列，再加一行”。不要展开大行列式，用 Schur 补一行算完。""",
    },
    ("ss19-2", 7): {
        "problem": r"""Gegeben sei

$$
A=
\begin{pmatrix}
0&-1&0\\
4&0&4\\
4&0&4
\end{pmatrix}.
$$

(a) Zeigen Sie, dass $(1,0,-1)^T$ ein Eigenvektor ist, und geben Sie den Eigenwert an.

(b) Berechnen Sie $\chi_A$ und zeigen Sie $\chi_A(2)=0$.

(c) Bestimmen Sie für jeden Eigenwert algebraische und geometrische Vielfachheit sowie den Eigenraum.

(d) Entscheiden Sie, ob $A$ diagonalisierbar ist.""",
        "zh_problem": r"""给定

$$
A=
\begin{pmatrix}
0&-1&0\\
4&0&4\\
4&0&4
\end{pmatrix}.
$$

(a) 证明 $(1,0,-1)^T$ 是特征向量，并给出特征值。

(b) 求 $\chi_A$，并证明 $\chi_A(2)=0$。

(c) 对每个特征值求代数重数、几何重数和特征空间。

(d) 判断 $A$ 是否可对角化。""",
        "solution": r"""(a)

$$
A\begin{pmatrix}1\\0\\-1\end{pmatrix}
=
\begin{pmatrix}0\\0\\0\end{pmatrix}.
$$

Also ist $(1,0,-1)^T$ ein Eigenvektor zum Eigenwert $0$.

(b)

$$
\chi_A(\lambda)=\det(A-\lambda I)
=
\det
\begin{pmatrix}
-\lambda&-1&0\\
4&-\lambda&4\\
4&0&4-\lambda
\end{pmatrix}
=-\lambda(\lambda-2)^2.
$$

Insbesondere ist $\chi_A(2)=0$.

(c) Die Eigenwerte sind $0$ und $2$.

Für $\lambda=0$:

$$
E_0=\ker A
=
\operatorname{span}\left\{
\begin{pmatrix}1\\0\\-1\end{pmatrix}
\right\}.
$$

Also hat $\lambda=0$ algebraische und geometrische Vielfachheit $1$.

Für $\lambda=2$:

$$
A-2I=
\begin{pmatrix}
-2&-1&0\\
4&-2&4\\
4&0&2
\end{pmatrix}.
$$

Lösen von $(A-2I)x=0$ ergibt

$$
E_2=
\operatorname{span}\left\{
\begin{pmatrix}-1\\2\\2\end{pmatrix}
\right\}.
$$

Der Eigenwert $2$ hat algebraische Vielfachheit $2$, aber geometrische Vielfachheit $1$.

(d) Insgesamt gibt es nur

$$
\dim E_0+\dim E_2=1+1=2
$$

linear unabhängige Eigenvektoren. Für eine $3\times3$-Matrix braucht man aber $3$. Also ist $A$ nicht diagonalisierbar.""",
        "zh_solution": r"""核心考点：**特征多项式、特征空间、对角化**。

(a) 直接乘：

$$
A\begin{pmatrix}1\\0\\-1\end{pmatrix}
=0.
$$

所以它是特征值 $0$ 的特征向量。

(b)

$$
\chi_A(\lambda)=\det(A-\lambda I)
=-\lambda(\lambda-2)^2.
$$

因此 $\chi_A(2)=0$。

(c) 特征值为 $0$ 和 $2$。

对 $\lambda=0$：

$$
E_0=
\operatorname{span}\left\{
\begin{pmatrix}1\\0\\-1\end{pmatrix}
\right\}.
$$

代数重数 $1$，几何重数 $1$。

对 $\lambda=2$，解 $(A-2I)x=0$ 得

$$
E_2=
\operatorname{span}\left\{
\begin{pmatrix}-1\\2\\2\end{pmatrix}
\right\}.
$$

特征值 $2$ 的代数重数是 $2$，几何重数是 $1$。

(d) 几何重数总和只有

$$
1+1=2<3,
$$

所以没有 $3$ 个线性无关特征向量，$A$ 不可对角化。

解题思路：重复特征值最容易出坑。代数重数是多项式里的次数，几何重数必须解核；这里 $\lambda=2$ 代数重数是 $2$，但特征空间只有一维。""",
    },
    ("ss19-2", 8): {
        "problem": r"""Sei $n\ge3$ und $A=(a_{ij})\in\mathbb R^{n\times n}$ definiert durch

$$
a_{11}=1,\quad a_{1n}=-1,\quad a_{n1}=-1,\quad a_{nn}=1,
$$

und alle anderen Einträge sind $0$.

(a) Geben Sie $A$ für $n=4$ explizit an.

(b) Zeigen Sie durch Ausmultiplizieren:

$$
A=(e_1-e_n)(e_1-e_n)^T.
$$

(c) Zeigen Sie mit (b), dass $A$ symmetrisch ist.

(d) Bestimmen Sie das charakteristische Polynom und die algebraischen und geometrischen Vielfachheiten.

(e) Geben Sie eine Orthonormalbasis von $\mathbb R^n$ aus Eigenvektoren von $A$ an.""",
        "zh_problem": r"""设 $n\ge3$，矩阵 $A=(a_{ij})\in\mathbb R^{n\times n}$ 满足

$$
a_{11}=1,\quad a_{1n}=-1,\quad a_{n1}=-1,\quad a_{nn}=1,
$$

其余元素全为 $0$。

(a) 写出 $n=4$ 时的 $A$。

(b) 通过展开证明：

$$
A=(e_1-e_n)(e_1-e_n)^T.
$$

(c) 用 (b) 证明 $A$ 对称。

(d) 求特征多项式以及代数重数、几何重数。

(e) 给出一组由 $A$ 的特征向量组成的标准正交基。""",
        "solution": r"""(a)

$$
A_4=
\begin{pmatrix}
1&0&0&-1\\
0&0&0&0\\
0&0&0&0\\
-1&0&0&1
\end{pmatrix}.
$$

(b) Setze $u=e_1-e_n$. Dann

$$
uu^T=(e_1-e_n)(e_1^T-e_n^T)
=e_1e_1^T-e_1e_n^T-e_ne_1^T+e_ne_n^T.
$$

Das erzeugt genau die vier Einträge $1,-1,-1,1$ an den Positionen $(1,1),(1,n),(n,1),(n,n)$. Also $A=uu^T$.

(c)

$$
A^T=(uu^T)^T=uu^T=A.
$$

Also ist $A$ symmetrisch.

(d) Für $u=e_1-e_n$ gilt

$$
Au=uu^Tu=u(u^Tu)=2u.
$$

Also ist $2$ ein Eigenwert. Wenn $x\perp u$, dann

$$
Ax=uu^Tx=u(u^Tx)=0.
$$

Somit hat $0$ den Eigenraum $u^\perp$ mit Dimension $n-1$, und $2$ hat den Eigenraum $\operatorname{span}\{u\}$ mit Dimension $1$.

Das charakteristische Polynom ist

$$
\chi_A(\lambda)=(-\lambda)^{n-1}(2-\lambda).
$$

Also:

| Eigenwert | algebraische Vielfachheit | geometrische Vielfachheit |
|---:|---:|---:|
| $0$ | $n-1$ | $n-1$ |
| $2$ | $1$ | $1$ |

(e) Eine passende Orthonormalbasis ist

$$
\left(
\frac{e_1-e_n}{\sqrt2},
e_2,\ldots,e_{n-1},
\frac{e_1+e_n}{\sqrt2}
\right).
$$

Dabei gehört $\frac{e_1-e_n}{\sqrt2}$ zum Eigenwert $2$; alle übrigen Vektoren liegen in $u^\perp$ und gehören zum Eigenwert $0$.""",
        "zh_solution": r"""核心考点：**秩一对称矩阵、谱分解、标准正交特征基**。

(a)

$$
A_4=
\begin{pmatrix}
1&0&0&-1\\
0&0&0&0\\
0&0&0&0\\
-1&0&0&1
\end{pmatrix}.
$$

(b) 令

$$
u=e_1-e_n.
$$

则

$$
uu^T=e_1e_1^T-e_1e_n^T-e_ne_1^T+e_ne_n^T.
$$

这正好在 $(1,1),(1,n),(n,1),(n,n)$ 四个位置产生 $1,-1,-1,1$，其他位置为 $0$。所以

$$
A=(e_1-e_n)(e_1-e_n)^T.
$$

(c)

$$
A^T=(uu^T)^T=uu^T=A,
$$

所以 $A$ 对称。

(d) 因为

$$
Au=uu^Tu=u(u^Tu)=2u,
$$

所以 $2$ 是特征值。若 $x\perp u$，则

$$
Ax=uu^Tx=0,
$$

所以 $u^\perp$ 是特征值 $0$ 的特征空间，维数为 $n-1$。

因此

$$
\chi_A(\lambda)=(-\lambda)^{n-1}(2-\lambda).
$$

重数如下：

| 特征值 | 代数重数 | 几何重数 |
|---:|---:|---:|
| $0$ | $n-1$ | $n-1$ |
| $2$ | $1$ | $1$ |

(e) 一组标准正交特征向量基为

$$
\left(
\frac{e_1-e_n}{\sqrt2},
e_2,\ldots,e_{n-1},
\frac{e_1+e_n}{\sqrt2}
\right).
$$

解题思路：看到 $A=uu^T$，就知道它只在 $u$ 方向上有作用。沿 $u$ 的方向特征值是 $u^Tu=2$，所有垂直于 $u$ 的方向都会被压到 $0$。""",
    },
    ("ss20", 1): {
        "problem": r"""Betrachten Sie

$$
G=\left\{
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}
\;\middle|\;a_1,a_2\in\mathbb R
\right\}.
$$

(a) Für $A\in G$: Zeigen Sie, dass $A$ invertierbar ist, und berechnen Sie $A^{-1}$.

(b) Zeigen Sie, dass $(G,\cdot)$ eine kommutative Untergruppe von $GL(3,\mathbb R)$ ist.

(c) Zeigen Sie, dass $\varphi:\mathbb R^2\to G$ mit

$$
\varphi(a_1,a_2)=
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}
$$

ein Gruppenisomorphismus ist.

(d) Formulieren und beweisen Sie

$$
\varphi(na_1,na_2)=\varphi(a_1,a_2)^n
\qquad(n\in\mathbb N_0).
$$

(e) Zeigen Sie ohne Induktion, dass die Gleichung auch für $n\in\mathbb Z\setminus\mathbb N_0$ gilt.""",
        "zh_problem": r"""考虑

$$
G=\left\{
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}
\;\middle|\;a_1,a_2\in\mathbb R
\right\}.
$$

(a) 对 $A\in G$，证明 $A$ 可逆并求 $A^{-1}$。

(b) 证明 $(G,\cdot)$ 是 $GL(3,\mathbb R)$ 的交换子群。

(c) 证明给定的 $\varphi:\mathbb R^2\to G$ 是群同构。

(d) 写成矩阵等式并用归纳法证明

$$
\varphi(na_1,na_2)=\varphi(a_1,a_2)^n
\qquad(n\in\mathbb N_0).
$$

(e) 不用归纳法证明该式对负整数 $n$ 也成立。""",
        "solution": r"""Schreibe

$$
M(a_1,a_2)=
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$

Dann

$$
M(a_1,a_2)M(b_1,b_2)=M(a_1+b_1,a_2+b_2).
$$

(a) Da

$$
M(a_1,a_2)M(-a_1,-a_2)=M(0,0)=I_3,
$$

gilt

$$
M(a_1,a_2)^{-1}=M(-a_1,-a_2).
$$

(b) Die Produktformel liefert Abgeschlossenheit. Außerdem $M(0,0)=I_3$ und die Inversen liegen wieder in $G$. Wegen

$$
M(a_1,a_2)M(b_1,b_2)=M(a_1+b_1,a_2+b_2)=M(b_1,b_2)M(a_1,a_2)
$$

ist die Gruppe kommutativ.

(c) Für $\varphi(a_1,a_2)=M(a_1,a_2)$ gilt

$$
\varphi((a_1,a_2)+(b_1,b_2))
=M(a_1+b_1,a_2+b_2)
=\varphi(a_1,a_2)\varphi(b_1,b_2).
$$

Die Abbildung ist injektiv und surjektiv, weil jedes Element von $G$ eindeutig durch $(a_1,a_2)$ bestimmt ist. Also ist $\varphi$ ein Isomorphismus.

(d) Die Matrixgleichung lautet

$$
\begin{pmatrix}
1&na_1&na_2\\
0&1&0\\
0&0&1
\end{pmatrix}
=
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}^n.
$$

Für $n=0$ ist das $I_3=I_3$. Angenommen, es gilt für $n$. Dann

$$
M(a_1,a_2)^{n+1}=M(na_1,na_2)M(a_1,a_2)=M((n+1)a_1,(n+1)a_2).
$$

(e) Für $n=-m<0$ folgt mit der Homomorphie

$$
\varphi(na_1,na_2)=\varphi(-m(a_1,a_2))
=\varphi(m(a_1,a_2))^{-1}
=\left(\varphi(a_1,a_2)^m\right)^{-1}
=\varphi(a_1,a_2)^{-m}.
$$""",
        "zh_solution": r"""核心考点：**矩阵群、群同构、矩阵幂归纳**。

记

$$
M(a_1,a_2)=
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$

最关键的乘法公式是

$$
M(a_1,a_2)M(b_1,b_2)=M(a_1+b_1,a_2+b_2).
$$

(a) 因此

$$
M(a_1,a_2)^{-1}=M(-a_1,-a_2).
$$

(b) 封闭性、单位元、逆元都由上式得到；交换性来自实数加法交换：

$$
M(a)M(b)=M(a+b)=M(b+a)=M(b)M(a).
$$

(c) $\varphi(a_1,a_2)=M(a_1,a_2)$ 保运算：

$$
\varphi(u+v)=\varphi(u)\varphi(v).
$$

而且每个矩阵唯一对应一对 $(a_1,a_2)$，所以既单射又满射，是同构。

(d) 要证的矩阵等式是

$$
\begin{pmatrix}
1&na_1&na_2\\
0&1&0\\
0&0&1
\end{pmatrix}
=
\begin{pmatrix}
1&a_1&a_2\\
0&1&0\\
0&0&1
\end{pmatrix}^n.
$$

$n=0$ 时两边都是 $I_3$。若 $n$ 时成立，则

$$
M(a_1,a_2)^{n+1}=M(na_1,na_2)M(a_1,a_2)=M((n+1)a_1,(n+1)a_2).
$$

(e) 负整数不用重新乘。设 $n=-m$：

$$
\varphi(nv)=\varphi(-mv)=\varphi(mv)^{-1}
=\left(\varphi(v)^m\right)^{-1}
=\varphi(v)^n.
$$

解题思路：这题把矩阵乘法完全翻译成 $\mathbb R^2$ 加法。只要抓住 $M(a)M(b)=M(a+b)$，后面都是加法群的语言。""",
    },
    ("ss20", 2): {
        "problem": r"""Seien $\alpha,\beta\in\mathbb C$ und

$$
A=
\begin{pmatrix}
1&1&0\\
\alpha&-\alpha&\beta
\end{pmatrix}
\in\mathbb C^{2\times3}.
$$

(a) Berechnen Sie $AA^T$ und $A^TA$.

(b) Berechnen Sie $\operatorname{rang}A$ in Abhängigkeit von $\alpha,\beta$.

(c) Bestimmen Sie alle $\alpha,\beta$, sodass $\operatorname{rang}(AA^T)\ne\operatorname{rang}A$.

(d) Zeigen Sie ohne Zeilenstufenform von $A^TA$:

$$
1\le \operatorname{rang}(A^TA)\le2.
$$

(e) Zeigen Sie: Ist ein führender $k\times k$-Minor einer Matrix $M\in K^{n\times n}$ ungleich $0$, dann $\operatorname{rang}M\ge k$.

(f) Bestimmen Sie $\operatorname{rang}(A^TA)$.""",
        "zh_problem": r"""设 $\alpha,\beta\in\mathbb C$，

$$
A=
\begin{pmatrix}
1&1&0\\
\alpha&-\alpha&\beta
\end{pmatrix}
\in\mathbb C^{2\times3}.
$$

(a) 计算 $AA^T$ 与 $A^TA$。

(b) 根据 $\alpha,\beta$ 求 $\operatorname{rang}A$。

(c) 求所有使 $\operatorname{rang}(AA^T)\ne\operatorname{rang}A$ 的 $\alpha,\beta$。

(d) 不化简 $A^TA$，证明 $1\le \operatorname{rang}(A^TA)\le2$。

(e) 证明：若矩阵某个前导 $k\times k$ 子式不为 $0$，则 $\operatorname{rang}M\ge k$。

(f) 求 $\operatorname{rang}(A^TA)$。""",
        "solution": r"""(a)

$$
AA^T=
\begin{pmatrix}
2&0\\
0&2\alpha^2+\beta^2
\end{pmatrix}.
$$

Außerdem

$$
A^TA=
\begin{pmatrix}
\alpha^2+1&1-\alpha^2&\alpha\beta\\
1-\alpha^2&\alpha^2+1&-\alpha\beta\\
\alpha\beta&-\alpha\beta&\beta^2
\end{pmatrix}.
$$

(b) Die erste Zeile $(1,1,0)$ ist nie $0$. Die zweite Zeile $(\alpha,-\alpha,\beta)$ ist genau dann ein Vielfaches der ersten, wenn $\alpha=\beta=0$. Also

$$
\operatorname{rang}A=
\begin{cases}
1,&\alpha=0,\ \beta=0,\\
2,&\text{sonst}.
\end{cases}
$$

(c) Aus (a) folgt

$$
\operatorname{rang}(AA^T)=
\begin{cases}
1,&2\alpha^2+\beta^2=0,\\
2,&2\alpha^2+\beta^2\ne0.
\end{cases}
$$

Ein Rangunterschied tritt genau dann auf, wenn

$$
(\alpha,\beta)\ne(0,0)
\quad\text{und}\quad
2\alpha^2+\beta^2=0.
$$

Äquivalent:

$$
\alpha\ne0,\qquad \beta=\pm i\sqrt2\,\alpha.
$$

Ein Beispiel ist $\alpha=1,\ \beta=i\sqrt2$.

(d) Es gilt allgemein

$$
\operatorname{rang}(A^TA)\le\operatorname{rang}(A^T)\le2.
$$

Außerdem ist $A^TA$ nicht die Nullmatrix, denn die ersten beiden Einträge können nicht beide verschwinden:

$$
\alpha^2+1=0
\quad\text{und}\quad
1-\alpha^2=0
$$

wären widersprüchlich. Also $\operatorname{rang}(A^TA)\ge1$.

(e) Wenn ein $k\times k$-Minor von $M$ Determinante ungleich $0$ hat, sind die entsprechenden $k$ Zeilen und $k$ Spalten linear unabhängig. Damit enthält $M$ eine reguläre $k\times k$-Untermatrix, also muss $\operatorname{rang}M\ge k$ gelten.

(f) Die $2\times2$-Minoren von $A^TA$ enthalten

$$
4\alpha^2,\qquad \beta^2,\qquad -2\alpha\beta.
$$

Ist $(\alpha,\beta)\ne(0,0)$, ist mindestens einer dieser Minoren ungleich $0$, also

$$
\operatorname{rang}(A^TA)=2.
$$

Ist $\alpha=\beta=0$, dann

$$
A^TA=
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
$$

also Rang $1$. Somit

$$
\operatorname{rang}(A^TA)=
\begin{cases}
1,&\alpha=0,\ \beta=0,\\
2,&\text{sonst}.
\end{cases}
$$""",
        "zh_solution": r"""核心考点：**复数域上转置不是共轭转置、秩与 Gram 型矩阵**。

(a) 直接乘：

$$
AA^T=
\begin{pmatrix}
2&0\\
0&2\alpha^2+\beta^2
\end{pmatrix},
$$

以及

$$
A^TA=
\begin{pmatrix}
\alpha^2+1&1-\alpha^2&\alpha\beta\\
1-\alpha^2&\alpha^2+1&-\alpha\beta\\
\alpha\beta&-\alpha\beta&\beta^2
\end{pmatrix}.
$$

(b) 第一行 $(1,1,0)$ 永远非零。第二行 $(\alpha,-\alpha,\beta)$ 只有在 $\alpha=\beta=0$ 时才和第一行相关。因此

$$
\operatorname{rang}A=
\begin{cases}
1,&\alpha=\beta=0,\\
2,&\text{否则}.
\end{cases}
$$

(c) 从 $AA^T$ 看，

$$
\operatorname{rang}(AA^T)=1
\Longleftrightarrow
2\alpha^2+\beta^2=0.
$$

但要和 $\operatorname{rang}A$ 不同，还必须 $A$ 的秩是 $2$，即 $(\alpha,\beta)\ne(0,0)$。所以条件是

$$
\alpha\ne0,\qquad \beta=\pm i\sqrt2\,\alpha.
$$

例子：

$$
\alpha=1,\qquad \beta=i\sqrt2.
$$

(d) 因为

$$
\operatorname{rang}(A^TA)\le\operatorname{rang}A\le2,
$$

所以上界是 $2$。又 $A^TA$ 不可能是零矩阵，因此秩至少是 $1$。

(e) 一个 $k\times k$ 子式非零，说明这 $k$ 行 $k$ 列组成的小矩阵可逆，里面已经有 $k$ 个独立方向，所以原矩阵的秩至少是 $k$。

(f) 看 $A^TA$ 的 $2\times2$ 子式，可得到

$$
4\alpha^2,\qquad \beta^2,\qquad -2\alpha\beta.
$$

只要 $(\alpha,\beta)\ne(0,0)$，至少一个非零，秩就是 $2$。若 $\alpha=\beta=0$，

$$
A^TA=
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
$$

秩为 $1$。因此

$$
\operatorname{rang}(A^TA)=
\begin{cases}
1,&\alpha=\beta=0,\\
2,&\text{否则}.
\end{cases}
$$

解题思路：这里在复数域用的是 $A^T$，不是 $\overline A^T$，所以 $AA^T$ 的秩可能和 $A$ 不同。关键异常来自 $2\alpha^2+\beta^2=0$ 在复数里有非零解。""",
    },
    ("ss20", 4): {
        "problem": r"""Sei $\alpha\in\mathbb R$ und

$$
A=
\begin{pmatrix}
1&0&1\\
0&0&\alpha\\
1&0&1
\end{pmatrix}.
$$

(a) Berechnen Sie das charakteristische Polynom und die Eigenwerte mit algebraischen Vielfachheiten.

(b) Bestimmen Sie zu jedem Eigenwert den Eigenraum in Abhängigkeit von $\alpha$.

(c) Untersuchen Sie die Diagonalisierbarkeit von $A$.

(d) Zeigen Sie, dass $A+I_3$ invertierbar ist, und geben Sie die Eigenwerte von $(A+I_3)^{-1}$ an.""",
        "zh_problem": r"""设 $\alpha\in\mathbb R$，

$$
A=
\begin{pmatrix}
1&0&1\\
0&0&\alpha\\
1&0&1
\end{pmatrix}.
$$

(a) 求特征多项式和各特征值的代数重数。

(b) 按 $\alpha$ 分类求每个特征值的特征空间。

(c) 判断 $A$ 何时可对角化。

(d) 证明 $A+I_3$ 可逆，并给出 $(A+I_3)^{-1}$ 的特征值。""",
        "solution": r"""(a)

$$
\chi_A(\lambda)=\det(A-\lambda I)
=-\lambda^2(\lambda-2).
$$

Also hat $0$ algebraische Vielfachheit $2$ und $2$ algebraische Vielfachheit $1$.

(b) Für $\lambda=2$:

$$
(A-2I)x=0
\quad\Longrightarrow\quad
x_3=x_1,\qquad x_2=\frac{\alpha}{2}x_1.
$$

Also

$$
E_2=
\operatorname{span}\left\{
\begin{pmatrix}2\\ \alpha\\2\end{pmatrix}
\right\}.
$$

Für $\lambda=0$ muss $Ax=0$ gelten:

$$
x_1+x_3=0,\qquad \alpha x_3=0.
$$

Falls $\alpha\ne0$, folgt $x_3=0$ und $x_1=0$, also

$$
E_0=\operatorname{span}\{e_2\}.
$$

Falls $\alpha=0$, bleibt nur $x_1+x_3=0$, also

$$
E_0=
\operatorname{span}\left\{
e_2,\begin{pmatrix}1\\0\\-1\end{pmatrix}
\right\}.
$$

(c) Wenn $\alpha=0$, ist

$$
\dim E_0+\dim E_2=2+1=3,
$$

also ist $A$ diagonalisierbar.

Wenn $\alpha\ne0$, ist

$$
\dim E_0+\dim E_2=1+1=2<3,
$$

also ist $A$ nicht diagonalisierbar.

(d) Die Eigenwerte von $A+I_3$ sind die Eigenwerte von $A$ plus $1$, also

$$
1,1,3.
$$

Keiner davon ist $0$, also ist $A+I_3$ invertierbar. Die Eigenwerte des Inversen sind die Kehrwerte:

$$
1,\ 1,\ \frac13.
$$""",
        "zh_solution": r"""核心考点：**特征空间分类、对角化、特征值平移与取逆**。

(a)

$$
\chi_A(\lambda)=\det(A-\lambda I)=-\lambda^2(\lambda-2).
$$

所以特征值 $0$ 的代数重数是 $2$，特征值 $2$ 的代数重数是 $1$。

(b) 对 $\lambda=2$，解 $(A-2I)x=0$：

$$
x_3=x_1,\qquad x_2=\frac{\alpha}{2}x_1.
$$

因此

$$
E_2=
\operatorname{span}\left\{
\begin{pmatrix}2\\ \alpha\\2\end{pmatrix}
\right\}.
$$

对 $\lambda=0$，解 $Ax=0$：

$$
x_1+x_3=0,\qquad \alpha x_3=0.
$$

若 $\alpha\ne0$，则 $x_3=0,x_1=0$，

$$
E_0=\operatorname{span}\{e_2\}.
$$

若 $\alpha=0$，则只有 $x_1+x_3=0$，

$$
E_0=
\operatorname{span}\left\{
e_2,\begin{pmatrix}1\\0\\-1\end{pmatrix}
\right\}.
$$

(c) 当 $\alpha=0$ 时，特征空间维数总和为 $2+1=3$，可对角化。当 $\alpha\ne0$ 时，总和为 $1+1=2<3$，不可对角化。

(d) $A+I_3$ 的特征值是在 $A$ 的特征值上加 $1$：

$$
1,1,3.
$$

没有零特征值，所以 $A+I_3$ 可逆。逆矩阵的特征值取倒数：

$$
1,\ 1,\ \frac13.
$$

解题思路：参数 $\alpha$ 不影响特征值，但会影响零特征空间的维数；对角化看的是特征向量数量，不是只看特征值。""",
    },
    ("ss21", 1): {
        "problem": r"""Betrachten Sie

$$
G=
\left\{
M(k,r)=
\begin{pmatrix}
r&0\\
3^k-r&3^k
\end{pmatrix}
\;\middle|\;
k\in\mathbb Z,\ r\in\mathbb Q\setminus\{0\}
\right\}.
$$

(a) Zeigen Sie $G\subset GL(2,\mathbb Q)$.

(b) Berechnen Sie $A^{-1}$ für $A\in G$.

(c) Zeigen Sie, dass $(G,\cdot)$ eine kommutative Untergruppe von $GL(2,\mathbb Q)$ ist.

(d) Zeigen Sie, dass $(\mathbb Z,+)\times(\mathbb Q\setminus\{0\},\cdot)$ isomorph zu $(G,\cdot)$ ist.

(e) Berechnen Sie mit der Isomorphie

$$
\begin{pmatrix}
4&0\\
-1&3
\end{pmatrix}^n.
$$""",
        "zh_problem": r"""考虑

$$
G=
\left\{
M(k,r)=
\begin{pmatrix}
r&0\\
3^k-r&3^k
\end{pmatrix}
\;\middle|\;
k\in\mathbb Z,\ r\in\mathbb Q\setminus\{0\}
\right\}.
$$

(a) 证明 $G\subset GL(2,\mathbb Q)$。

(b) 对 $A\in G$ 求 $A^{-1}$。

(c) 证明 $(G,\cdot)$ 是 $GL(2,\mathbb Q)$ 的交换子群。

(d) 证明 $(\mathbb Z,+)\times(\mathbb Q\setminus\{0\},\cdot)$ 与 $(G,\cdot)$ 同构。

(e) 用同构计算

$$
\begin{pmatrix}
4&0\\
-1&3
\end{pmatrix}^n.
$$""",
        "solution": r"""Für

$$
M(k,r)=
\begin{pmatrix}
r&0\\
3^k-r&3^k
\end{pmatrix}
$$

gilt

$$
\det M(k,r)=r3^k\ne0.
$$

Also $G\subset GL(2,\mathbb Q)$.

Die Inverse ist

$$
M(k,r)^{-1}
=
\begin{pmatrix}
r^{-1}&0\\
3^{-k}-r^{-1}&3^{-k}
\end{pmatrix}
=M(-k,r^{-1}).
$$

Das Produkt zweier Elemente ist

$$
M(k,r)M(\ell,s)=M(k+\ell,rs).
$$

Daraus folgen Abgeschlossenheit, Einheit $M(0,1)=I_2$, inverse Elemente und Kommutativität.

Die Abbildung

$$
\Phi:\mathbb Z\times\mathbb Q^\times\to G,\qquad
\Phi(k,r)=M(k,r)
$$

ist bijektiv und erfüllt

$$
\Phi(k+\ell,rs)=M(k+\ell,rs)=M(k,r)M(\ell,s)=\Phi(k,r)\Phi(\ell,s).
$$

Also ist $\Phi$ ein Gruppenisomorphismus.

Schließlich

$$
\begin{pmatrix}
4&0\\
-1&3
\end{pmatrix}
=M(1,4).
$$

Also

$$
M(1,4)^n=M(n,4^n)
=
\begin{pmatrix}
4^n&0\\
3^n-4^n&3^n
\end{pmatrix}.
$$""",
        "zh_solution": r"""核心考点：**参数矩阵群与直积同构**。

先算行列式：

$$
\det M(k,r)=r3^k\ne0.
$$

所以每个元素都可逆。逆矩阵是

$$
M(k,r)^{-1}
=M(-k,r^{-1})
=
\begin{pmatrix}
r^{-1}&0\\
3^{-k}-r^{-1}&3^{-k}
\end{pmatrix}.
$$

乘法公式为

$$
M(k,r)M(\ell,s)=M(k+\ell,rs).
$$

因此矩阵乘法对应到参数上就是

$$
(k,r)(\ell,s)=(k+\ell,rs).
$$

这说明

$$
\Phi(k,r)=M(k,r)
$$

是从 $(\mathbb Z,+)\times(\mathbb Q^\times,\cdot)$ 到 $G$ 的同构。

最后

$$
\begin{pmatrix}4&0\\-1&3\end{pmatrix}
=M(1,4),
$$

所以

$$
\begin{pmatrix}4&0\\-1&3\end{pmatrix}^n
=M(n,4^n)
=
\begin{pmatrix}
4^n&0\\
3^n-4^n&3^n
\end{pmatrix}.
$$

解题思路：同构题的关键不是抽象说理，而是找到参数乘法。这里 $k$ 相加，$r$ 相乘，所以就是 $\mathbb Z\times\mathbb Q^\times$。""",
    },
    ("ss21", 2): {
        "problem": r"""Sei $K$ ein Körper. Für $A,B\in K^{n\times n}$ sei

$$
A\sim B
\quad:\Longleftrightarrow\quad
\exists D\in K^{n\times n}:
D\text{ invertierbare Diagonalmatrix und }A=D^{-1}BD.
$$

Zeigen Sie:

(a) $A\sim B\Rightarrow A^T\sim B^T$.

(b) $A\in GL(n,K)$ und $A\sim B\Rightarrow B\in GL(n,K)$ und $A^{-1}\sim B^{-1}$.

(c) $A\sim B\Rightarrow A^k\sim B^k$ für $k\in\mathbb N$.

(d) $\sim$ ist eine Äquivalenzrelation.

(e) Aus $A=(a_{ij})$, $B=(b_{ij})$ und $A\sim B$ folgt

$$
a_{ii}=b_{ii},
\qquad
a_{ij}a_{ji}=b_{ij}b_{ji}.
$$""",
        "zh_problem": r"""设 $K$ 是域。对 $A,B\in K^{n\times n}$ 定义关系

$$
A\sim B
\quad:\Longleftrightarrow\quad
\exists D\in K^{n\times n}:
D\text{ 是可逆对角矩阵且 }A=D^{-1}BD.
$$

证明：

(a) $A\sim B\Rightarrow A^T\sim B^T$。

(b) $A\in GL(n,K)$ 且 $A\sim B\Rightarrow B\in GL(n,K)$ 且 $A^{-1}\sim B^{-1}$。

(c) $A\sim B\Rightarrow A^k\sim B^k$，$k\in\mathbb N$。

(d) $\sim$ 是等价关系。

(e) 若 $A=(a_{ij})$、$B=(b_{ij})$ 且 $A\sim B$，则

$$
a_{ii}=b_{ii},
\qquad
a_{ij}a_{ji}=b_{ij}b_{ji}.
$$""",
        "solution": r"""Sei $A=D^{-1}BD$ mit invertierbarer Diagonalmatrix $D$.

(a) Da $D^T=D$, gilt

$$
A^T=(D^{-1}BD)^T=DB^TD^{-1}.
$$

Mit $E=D^{-1}$ ist

$$
A^T=E^{-1}B^TE,
$$

also $A^T\sim B^T$.

(b) Aus $A=D^{-1}BD$ folgt

$$
B=DAD^{-1}.
$$

Ist $A$ invertierbar, dann ist auch $B$ invertierbar. Außerdem

$$
A^{-1}=(D^{-1}BD)^{-1}=D^{-1}B^{-1}D.
$$

Also $A^{-1}\sim B^{-1}$.

(c) Durch Kürzen der Zwischenfaktoren:

$$
A^k=(D^{-1}BD)^k=D^{-1}B^kD.
$$

Also $A^k\sim B^k$.

(d) Reflexivität: $A=I^{-1}AI$.

Symmetrie: Aus $A=D^{-1}BD$ folgt $B=DAD^{-1}$, also $B\sim A$.

Transitivität: Aus

$$
A=D^{-1}BD,\qquad B=E^{-1}CE
$$

folgt

$$
A=D^{-1}E^{-1}CED=(ED)^{-1}C(ED).
$$

Das Produkt $ED$ ist wieder eine invertierbare Diagonalmatrix. Also ist $\sim$ transitiv.

(e) Schreibe $D=\operatorname{diag}(d_1,\ldots,d_n)$. Dann gilt eintragsweise

$$
a_{ij}=d_i^{-1}b_{ij}d_j.
$$

Für $i=j$ folgt

$$
a_{ii}=d_i^{-1}b_{ii}d_i=b_{ii}.
$$

Für $i,j$:

$$
a_{ij}a_{ji}
=(d_i^{-1}b_{ij}d_j)(d_j^{-1}b_{ji}d_i)
=b_{ij}b_{ji}.
$$""",
        "zh_solution": r"""核心考点：**对角相似、转置、逆、幂、等价关系、不变量**。

设

$$
A=D^{-1}BD,
$$

其中 $D$ 是可逆对角矩阵。

(a) 因为 $D^T=D$，

$$
A^T=(D^{-1}BD)^T=DB^TD^{-1}.
$$

令 $E=D^{-1}$，则

$$
A^T=E^{-1}B^TE,
$$

所以 $A^T\sim B^T$。

(b) 由

$$
B=DAD^{-1}
$$

可知 $A$ 可逆时 $B$ 也可逆。并且

$$
A^{-1}=(D^{-1}BD)^{-1}=D^{-1}B^{-1}D,
$$

所以 $A^{-1}\sim B^{-1}$。

(c)

$$
A^k=(D^{-1}BD)^k=D^{-1}B^kD,
$$

中间的 $DD^{-1}$ 会逐个抵消，因此 $A^k\sim B^k$。

(d) 等价关系三步：

反身性：$A=I^{-1}AI$。

对称性：$A=D^{-1}BD$ 等价于 $B=DAD^{-1}$。

传递性：若 $A=D^{-1}BD$ 且 $B=E^{-1}CE$，则

$$
A=(ED)^{-1}C(ED),
$$

而 $ED$ 仍是可逆对角矩阵。

(e) 写

$$
D=\operatorname{diag}(d_1,\ldots,d_n).
$$

则

$$
a_{ij}=d_i^{-1}b_{ij}d_j.
$$

所以对角元不变：

$$
a_{ii}=b_{ii}.
$$

而对称位置乘积也不变：

$$
a_{ij}a_{ji}
=(d_i^{-1}b_{ij}d_j)(d_j^{-1}b_{ji}d_i)
=b_{ij}b_{ji}.
$$

解题思路：对角相似的本质是第 $i$ 行乘 $d_i^{-1}$、第 $j$ 列乘 $d_j$。所以单个非对角元会变，但 $a_{ij}a_{ji}$ 中的缩放因子刚好抵消。""",
    },
})


MANUAL_OVERRIDES.update({
    ("ss22"+KAOSHI+"1", 2): {
        "problem": r"""Aus dem Graphen einer linearen Abbildung $x\mapsto Ax$ in $\mathbb R^2$ sollen $\ker(A)$, $\operatorname{col}(A)$, $\operatorname{rang}(A)$, $\det(A)$ und die Matrix $A$ bestimmt werden. Im Bild liest man ab:

$$
A(-2e_1)=\begin{pmatrix}-1\\0\end{pmatrix},
\qquad
A(-e_2)=\begin{pmatrix}0\\0\end{pmatrix}.
$$""",
        "zh_problem": r"""根据二维线性变换图像求 $\ker(A)$、$\operatorname{col}(A)$、$\operatorname{rang}(A)$、$\det(A)$ 和矩阵 $A$。图中读出：

$$
A(-2e_1)=\begin{pmatrix}-1\\0\end{pmatrix},
\qquad
A(-e_2)=\begin{pmatrix}0\\0\end{pmatrix}.
$$""",
        "solution": r"""Da $A(-2e_1)=-2Ae_1$, gilt

$$
Ae_1=\begin{pmatrix}\frac12\\0\end{pmatrix}.
$$

Aus $A(-e_2)=0$ folgt

$$
Ae_2=0.
$$

Die Spalten von $A$ sind also

$$
A=
\begin{pmatrix}
\frac12&0\\
0&0
\end{pmatrix}.
$$

Damit

$$
\operatorname{col}(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\0\end{pmatrix}
\right\},
\qquad
\ker(A)=
\operatorname{span}\left\{
\begin{pmatrix}0\\1\end{pmatrix}
\right\}.
$$

Also

$$
\operatorname{rang}(A)=1,
\qquad
\det(A)=0.
$$""",
        "zh_solution": r"""核心考点：**从图像读矩阵列、核与像**。

矩阵的第 $j$ 列就是 $Ae_j$。图中给的是 $-2e_1$ 与 $-e_2$ 的像：

$$
A(-2e_1)=\begin{pmatrix}-1\\0\end{pmatrix}
\Rightarrow
Ae_1=\begin{pmatrix}\frac12\\0\end{pmatrix},
$$

$$
A(-e_2)=0
\Rightarrow
Ae_2=0.
$$

所以

$$
A=
\begin{pmatrix}
\frac12&0\\
0&0
\end{pmatrix}.
$$

列空间是一条 $x$ 轴方向的直线：

$$
\operatorname{col}(A)=\operatorname{span}\left\{\begin{pmatrix}1\\0\end{pmatrix}\right\}.
$$

核是被压到零的 $y$ 轴方向：

$$
\ker(A)=\operatorname{span}\left\{\begin{pmatrix}0\\1\end{pmatrix}\right\}.
$$

因此 $\operatorname{rang}(A)=1$，且矩阵不可逆，$\det(A)=0$。""",
    },
    ("ss22"+KAOSHI+"1", 3): {
        "problem": r"""Entscheiden Sie mit Begründung, ob die Aussagen wahr oder falsch sind: positive/negative Definitheit, Kerne inverser Matrizen, Produkte $AB$ und $BA$, Orthogonalität zu einer Basis, Spalten von $A^{-1}$, Basis von $P_2$ und Unterraum invertierbarer Matrizen.""",
        "zh_problem": r"""判断并证明下列命题真假：正定/负定、逆矩阵的核、$AB$ 与 $BA$ 的尺寸、与基中所有向量正交、$A^{-1}$ 的列、$P_2$ 的基、可逆矩阵集合是否为子空间。""",
        "solution": r"""(a) Wahr. Ist $A$ positiv definit, dann gilt für $x\ne0$:

$$
x^T(-A)x=-x^TAx<0.
$$

(b) Wahr. Ist $A$ invertierbar, dann sind $A$ und $A^{-1}$ beide invertierbar, also

$$
\ker(A)=\ker(A^{-1})=\{0\}.
$$

(c) Wahr. Wenn $A\in\mathbb R^{k\times m}$ und $B\in\mathbb R^{n\times \ell}$, dann erzwingt die Existenz von $AB$ und $BA$ die Bedingungen $m=n$ und $\ell=k$. Also ist $AB\in\mathbb R^{k\times k}$ und $BA\in\mathbb R^{n\times n}$.

(d) Wahr. Ist $w$ orthogonal zu allen Basisvektoren $v_i$, dann ist $w$ orthogonal zu jeder Linearkombination, also auch zu sich selbst. Somit

$$
\langle w,w\rangle=0
\Rightarrow w=0.
$$

(e) Wahr. $A^{-1}$ ist invertierbar; seine Spalten sind daher linear unabhängig und bilden eine Basis von $\mathbb R^n$.

(f) Falsch. Die Funktionen $1$, $x^2+1$, $x^2-1$ erzeugen nur Polynome ohne $x$-Term. Das Polynom $x\in P_2$ kann nicht dargestellt werden.

(g) Falsch. Die Menge der invertierbaren Matrizen enthält nicht die Nullmatrix und ist nicht unter Addition abgeschlossen, also kein Untervektorraum.""",
        "zh_solution": r"""核心考点：**真假判断中的定义链条**。

(a) 真。正定 $A$ 满足 $x^TAx>0$，所以

$$
x^T(-A)x=-x^TAx<0.
$$

(b) 真。可逆矩阵的核是 $\{0\}$，$A^{-1}$ 也可逆，所以二者核相同。

(c) 真。若 $AB$ 和 $BA$ 都有定义，设 $A$ 是 $k\times m$、$B$ 是 $n\times \ell$，则 $m=n$ 且 $\ell=k$，所以 $AB$ 与 $BA$ 都是方阵。

(d) 真。若 $w$ 与一组基全部正交，则它与所有向量都正交，特别是与自己正交：

$$
\langle w,w\rangle=0\Rightarrow w=0.
$$

(e) 真。$A^{-1}$ 可逆，因此它的 $n$ 个列向量线性无关并张成 $\mathbb R^n$。

(f) 假。$1,x^2+1,x^2-1$ 的线性组合没有一次项，不能表示多项式 $x$。

(g) 假。可逆矩阵集合不含零矩阵，也不对加法封闭，所以不是子空间。""",
    },
    ("ss22"+KAOSHI+"1", 4): {
        "problem": r"""Sei $M\subset\mathbb R^n$ nichtleer. Beweisen Sie:

$$
M\text{ ist linear unabhängig}
\Longleftrightarrow
\forall v\notin\operatorname{span}(M):\ M\cup\{v\}\text{ ist linear unabhängig}.
$$""",
        "zh_problem": r"""设 $M\subset\mathbb R^n$ 非空。证明：

$$
M\text{ 线性无关}
\Longleftrightarrow
\forall v\notin\operatorname{span}(M):\ M\cup\{v\}\text{ 线性无关}.
$$""",
        "solution": r"""Sei $M=\{m_1,\ldots,m_k\}$.

**Hinrichtung.** Sei $M$ linear unabhängig und $v\notin\operatorname{span}(M)$. Angenommen,

$$
\sum_{i=1}^k c_i m_i+c_{k+1}v=0.
$$

Ist $c_{k+1}=0$, folgt wegen der linearen Unabhängigkeit von $M$, dass alle $c_i=0$ sind. Ist $c_{k+1}\ne0$, dann

$$
v=-\sum_{i=1}^k\frac{c_i}{c_{k+1}}m_i\in\operatorname{span}(M),
$$

Widerspruch. Also ist $M\cup\{v\}$ linear unabhängig.

**Rückrichtung.** Wenn es ein $v\notin\operatorname{span}(M)$ gibt, sodass $M\cup\{v\}$ linear unabhängig ist, dann ist jede Teilmenge davon linear unabhängig. Insbesondere ist $M$ linear unabhängig.""",
        "zh_solution": r"""核心考点：**线性无关与张成空间**。

设 $M=\{m_1,\ldots,m_k\}$。

先证“$\Rightarrow$”。设 $M$ 线性无关，且 $v\notin\operatorname{span}(M)$。若

$$
\sum_{i=1}^k c_i m_i+c_{k+1}v=0,
$$

分两种情况：

若 $c_{k+1}=0$，则由 $M$ 线性无关得到所有 $c_i=0$。

若 $c_{k+1}\ne0$，则

$$
v=-\sum_{i=1}^k\frac{c_i}{c_{k+1}}m_i\in\operatorname{span}(M),
$$

这与 $v\notin\operatorname{span}(M)$ 矛盾。所以只能是零系数，$M\cup\{v\}$ 线性无关。

再证“$\Leftarrow$”。如果 $M\cup\{v\}$ 线性无关，那么它的任意子集也线性无关，特别是 $M$ 线性无关。

解题思路：新增一个不在张成空间里的向量，不可能被原来的向量表示，所以不会制造新的线性相关关系。""",
    },
    ("ss22"+KAOSHI+"2", 2): {
        "problem": r"""Aus dem Graphen liest man ab:

$$
Ae_1=\begin{pmatrix}\frac12\\0\end{pmatrix},
\qquad
Ae_2=\begin{pmatrix}0\\2\end{pmatrix}.
$$

Bestimmen Sie $A$, $\ker(A)$, $\operatorname{col}(A)$, $\operatorname{rang}(A)$ und $\det(A)$.""",
        "zh_problem": r"""由图像读出：

$$
Ae_1=\begin{pmatrix}\frac12\\0\end{pmatrix},
\qquad
Ae_2=\begin{pmatrix}0\\2\end{pmatrix}.
$$

求 $A$、$\ker(A)$、$\operatorname{col}(A)$、$\operatorname{rang}(A)$ 和 $\det(A)$。""",
        "solution": r"""Die Spalten sind $Ae_1$ und $Ae_2$, also

$$
A=
\begin{pmatrix}
\frac12&0\\
0&2
\end{pmatrix}.
$$

Beide Spalten sind linear unabhängig. Daher

$$
\operatorname{col}(A)=\mathbb R^2,
\qquad
\operatorname{rang}(A)=2,
\qquad
\ker(A)=\{0\}.
$$

Außerdem

$$
\det(A)=\frac12\cdot2=1.
$$""",
        "zh_solution": r"""核心考点：**从单位向量像读矩阵**。

矩阵列就是单位向量的像：

$$
A=
\begin{pmatrix}
\frac12&0\\
0&2
\end{pmatrix}.
$$

两列线性无关，所以列空间是整个平面：

$$
\operatorname{col}(A)=\mathbb R^2.
$$

因此

$$
\operatorname{rang}(A)=2,\qquad \ker(A)=\{0\}.
$$

行列式是面积缩放因子：

$$
\det(A)=\frac12\cdot2=1.
$$""",
    },
    ("ss22"+KAOSHI+"2", 3): {
        "problem": r"""Entscheiden Sie wahr/falsch mit Begründung: Indefinitheit einer Matrix, Eigenwertgleichung, Eigenwerte orthogonaler Matrizen, orthogonales Komplement des Kerns, Zeilenbasis, gewichtetes Skalarprodukt und gerade Funktionen als Unterraum.""",
        "zh_problem": r"""判断并证明真假：矩阵不定性、特征值方程、正交矩阵特征值、核的正交补、行向量为基、加权内积、偶函数集合是否为子空间。""",
        "solution": r"""(a) Wahr. Für

$$
A=\begin{pmatrix}1&-3\\0&2\end{pmatrix}
$$

gilt

$$
x^TAx=x_1^2-3x_1x_2+2x_2^2.
$$

Dies nimmt positive und negative Werte an, z.B. $x=(1,0)^T$ gibt $1$, $x=(3,2)^T$ gibt $-1$.

(b) Falsch. Wenn $\lambda$ Eigenwert ist, besitzt $(\lambda I-A)x=0$ gerade eine nichttriviale Lösung.

(c) Wahr. Ist $Q$ orthogonal und $Qx=\lambda x$, $x\ne0$, dann

$$
\|x\|=\|Qx\|=\|\lambda x\|=|\lambda|\|x\|,
$$

also $|\lambda|=1$.

(d) Wahr. Ist $A$ invertierbar, dann $\ker(A)=\{0\}$ und daher $\ker(A)^\perp=\mathbb R^n$.

(e) Wahr. Wenn die Zeilen von $A\in\mathbb R^{m\times n}$ eine Basis von $\mathbb R^n$ bilden, dann hat $A$ Rang $n$. Also hat $Ax=0$ nur die triviale Lösung.

(f) Wahr. Die Form $\langle x,y\rangle=w_1x_1y_1+w_2x_2y_2$ ist genau dann positiv definit, wenn $w_1,w_2>0$.

(g) Wahr. Gerade Funktionen erfüllen $f(-x)=f(x)$. Summe und skalare Vielfache gerader Funktionen sind wieder gerade; die Nullfunktion ist enthalten.""",
        "zh_solution": r"""核心考点：**真假判断综合题**。

(a) 真。二次型

$$
x^TAx=x_1^2-3x_1x_2+2x_2^2
$$

可正可负，例如 $(1,0)^T$ 得 $1$，$(3,2)^T$ 得 $-1$，所以不定。

(b) 假。$\lambda$ 是特征值时，$(\lambda I-A)x=0$ 必有非零解，这正是特征向量的定义。

(c) 真。正交矩阵保持长度：

$$
\|x\|=\|Qx\|=\|\lambda x\|=|\lambda|\|x\|,
$$

故 $|\lambda|=1$。

(d) 真。$A$ 可逆则 $\ker(A)=\{0\}$，零空间的正交补是整个 $\mathbb R^n$。

(e) 真。行向量组成 $\mathbb R^n$ 的一组基，说明秩为 $n$，所以 $Ax=0$ 只有零解。

(f) 真。加权内积要正定，必须且只需 $w_1,w_2>0$。

(g) 真。偶函数对加法、数乘封闭，并含零函数，所以是子空间。""",
    },
    ("ss22"+KAOSHI+"2", 4): {
        "problem": r"""Sei $A\in\mathbb R^{m\times n}$ und $Q\in\mathbb R^{n\times n}$ invertierbar. Beweisen Sie: $Ax=0$ hat genau dann nur die triviale Lösung, wenn $AQx=0$ nur die triviale Lösung hat.""",
        "zh_problem": r"""设 $A\in\mathbb R^{m\times n}$，$Q\in\mathbb R^{n\times n}$ 可逆。证明：$Ax=0$ 只有零解，当且仅当 $AQx=0$ 只有零解。""",
        "solution": r"""Angenommen, $Ay=0$ hat nur $y=0$ als Lösung. Wenn $AQx=0$, setze $y=Qx$. Dann $Ay=0$, also $Qx=0$. Da $Q$ invertierbar ist, folgt $x=0$.

Umgekehrt: Hat $Ay=0$ eine nichttriviale Lösung $y\ne0$, dann setze

$$
x=Q^{-1}y.
$$

Dann $x\ne0$ und

$$
AQx=AQQ^{-1}y=Ay=0.
$$

Also hat $AQx=0$ genau dann nur die triviale Lösung, wenn $Ax=0$ nur die triviale Lösung hat.""",
        "zh_solution": r"""核心考点：**可逆变换不改变零解唯一性**。

先设 $Ax=0$ 只有零解。若

$$
AQx=0,
$$

令 $y=Qx$，则 $Ay=0$，所以 $y=0$。又 $Q$ 可逆，因此 $Qx=0$ 推出 $x=0$。

反过来，如果 $Ay=0$ 有非零解 $y\ne0$，令

$$
x=Q^{-1}y.
$$

由于 $Q$ 可逆，$x\ne0$，并且

$$
AQx=AQQ^{-1}y=Ay=0.
$$

所以 $AQx=0$ 也有非零解。由此两者“只有零解”完全等价。""",
    },
    ("ss24"+KAOSHI, 2): {
        "problem": r"""Aus dem Graphen liest man ab:

$$
Ae_1=\begin{pmatrix}1\\-\frac12\end{pmatrix},
\qquad
Ae_2=\begin{pmatrix}-\frac12\\\frac14\end{pmatrix}.
$$

Bestimmen Sie $A$, $\ker(A)$, $\operatorname{col}(A)$, $\operatorname{rang}(A)$ und $\det(A)$.""",
        "zh_problem": r"""由图像读出：

$$
Ae_1=\begin{pmatrix}1\\-\frac12\end{pmatrix},
\qquad
Ae_2=\begin{pmatrix}-\frac12\\\frac14\end{pmatrix}.
$$

求 $A$、$\ker(A)$、$\operatorname{col}(A)$、$\operatorname{rang}(A)$ 与 $\det(A)$。""",
        "solution": r"""Die Spalten sind

$$
A=
\begin{pmatrix}
1&-\frac12\\
-\frac12&\frac14
\end{pmatrix}.
$$

Die zweite Spalte ist $-\frac12$ mal die erste. Daher

$$
\operatorname{col}(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\-\frac12\end{pmatrix}
\right\},
\qquad
\operatorname{rang}(A)=1.
$$

Aus $Ax=0$ folgt

$$
x_1-\frac12x_2=0,
$$

also

$$
\ker(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\2\end{pmatrix}
\right\}.
$$

Da die Spalten abhängig sind,

$$
\det(A)=0.
$$""",
        "zh_solution": r"""核心考点：**图像读列空间与核**。

从图像读出单位向量的像：

$$
Ae_1=\begin{pmatrix}1\\-\frac12\end{pmatrix},
\qquad
Ae_2=\begin{pmatrix}-\frac12\\\frac14\end{pmatrix}.
$$

所以

$$
A=
\begin{pmatrix}
1&-\frac12\\
-\frac12&\frac14
\end{pmatrix}.
$$

第二列是第一列的 $-\frac12$ 倍，因此

$$
\operatorname{col}(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\-\frac12\end{pmatrix}
\right\},
\qquad
\operatorname{rang}(A)=1.
$$

解 $Ax=0$ 得

$$
x_1-\frac12x_2=0,
$$

所以

$$
\ker(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\2\end{pmatrix}
\right\}.
$$

秩不足，所以 $\det(A)=0$。""",
    },
    ("ss24"+KAOSHI, 3): {
        "problem": r"""Entscheiden Sie wahr/falsch: positive Semidefinitheit, Determinante und Rang, $(A+B)^2$, Nullspalten, negative Eigenwerte und Spaltenraum, Diagonalisierbarkeit/orthogonale Diagonalisierbarkeit, gleiche Zeilenstufenform, Skalarproduktgleichheit, Unterraum $f(0)=1$.""",
        "zh_problem": r"""判断真假：半正定、行列式与秩、$(A+B)^2$、零列、负特征值与列空间、可对角化/正交对角化、相同行阶梯形、内积等式、$f(0)=1$ 是否为子空间。""",
        "solution": r"""(a) Wahr. $\operatorname{diag}(1,2)$ ist sogar positiv definit.

(b) Wahr. $\det(A)\ge1$ impliziert $\det(A)\ne0$, also $\operatorname{rang}(A)=n\ge1$.

(c) Falsch. Allgemein

$$
(A+B)^2=A^2+AB+BA+B^2,
$$

und nur bei $AB=BA$ wird daraus $A^2+2AB+B^2$.

(d) Wahr. Ist $b_i=0$ eine Nullspalte von $B$, dann ist die $i$-te Spalte von $AB$ gleich $Ab_i=0$.

(e) Wahr. Strikt negative Eigenwerte sind alle ungleich $0$, also ist $A$ invertierbar und $\operatorname{col}(A)=\mathbb R^n$.

(f) Wahr. Eine Dreiecksmatrix mit paarweise verschiedenen Diagonaleigenwerten ist diagonalisierbar. Sie ist aber nicht symmetrisch, also nicht orthogonal diagonalisierbar.

(g) Wahr. Elementare Zeilenumformungen ändern die Lösungsmenge von $Ax=0$ nicht.

(h) Falsch. Mit $v=0$ gilt $\langle v,w\rangle=\langle v,z\rangle=0$ für beliebige $w,z$.

(i) Falsch. Die Menge $\{f\mid f(0)=1\}$ enthält nicht die Nullfunktion und ist nicht additiv abgeschlossen.""",
        "zh_solution": r"""核心考点：**综合真假判断**。

(a) 真。$\begin{pmatrix}1&0\\0&2\end{pmatrix}$ 的二次型是 $x_1^2+2x_2^2>0$，所以更强地正定。

(b) 真。$\det(A)\ge1$ 保证 $\det(A)\ne0$，故满秩。

(c) 假。矩阵不一定交换：

$$
(A+B)^2=A^2+AB+BA+B^2.
$$

(d) 真。$B$ 的某列为 $0$，则 $AB$ 对应列是 $A0=0$。

(e) 真。所有特征值严格为负，特别都非零，所以 $A$ 可逆，列空间是 $\mathbb R^n$。

(f) 真。三角矩阵且特征值互异，所以可对角化；但不对称，所以不能正交对角化。

(g) 真。相同阶梯形意味着齐次方程经过相同等价行变换后相同，解集相同。

(h) 假。取 $v=0$，则 $\langle v,w\rangle=\langle v,z\rangle=0$，但 $w$ 不必等于 $z$。

(i) 假。$f(0)=1$ 的函数集合不含零函数；两个这样的函数相加后在 $0$ 处取值为 $2$。""",
    },
    ("ss24"+KAOSHI, 4): {
        "problem": r"""Beweisen Sie:

(a) Ist $\lambda$ Eigenwert von $A$ mit Eigenvektor $x$, dann ist $\lambda-c$ Eigenwert von $A-cI$ mit demselben Eigenvektor.

(b) Für $\lambda_1\ne\lambda_2$ gilt $E_{\lambda_1}\cap E_{\lambda_2}=\{0\}$.""",
        "zh_problem": r"""证明：

(a) 若 $\lambda$ 是 $A$ 的特征值，$x$ 是对应特征向量，则 $\lambda-c$ 是 $A-cI$ 的特征值，特征向量仍为 $x$。

(b) 若 $\lambda_1\ne\lambda_2$，则 $E_{\lambda_1}\cap E_{\lambda_2}=\{0\}$。""",
        "solution": r"""(a) Aus $Ax=\lambda x$ und $x\ne0$ folgt

$$
(A-cI)x=Ax-cx=\lambda x-cx=(\lambda-c)x.
$$

Also ist $x$ Eigenvektor von $A-cI$ zum Eigenwert $\lambda-c$.

(b) Sei $v\in E_{\lambda_1}\cap E_{\lambda_2}$. Dann

$$
Av=\lambda_1v
\qquad\text{und}\qquad
Av=\lambda_2v.
$$

Also

$$
(\lambda_1-\lambda_2)v=0.
$$

Da $\lambda_1\ne\lambda_2$, folgt $v=0$. Somit ist der Schnitt genau $\{0\}$.""",
        "zh_solution": r"""核心考点：**特征值平移与不同特征空间交集**。

(a) 由 $Ax=\lambda x$：

$$
(A-cI)x=Ax-cx=\lambda x-cx=(\lambda-c)x.
$$

所以同一个 $x$ 仍是特征向量，特征值变成 $\lambda-c$。

(b) 若 $v$ 同时属于两个不同特征值的特征空间，则

$$
Av=\lambda_1v,\qquad Av=\lambda_2v.
$$

相减：

$$
(\lambda_1-\lambda_2)v=0.
$$

因为 $\lambda_1\ne\lambda_2$，只能 $v=0$。所以交集是 $\{0\}$。""",
    },
    ("ss25", 2): {
        "problem": r"""Aus dem Graphen in `ss25-2.png` liest man:

![ss25 Aufgabe 2](ss25-2.png)

$$
P_1=e_1,\qquad P_2=2e_2,\qquad P_3=\begin{pmatrix}1\\1\\1\end{pmatrix},
$$

und

$$
AP_1=\begin{pmatrix}1\\0\\0\end{pmatrix},
\qquad
AP_2=\begin{pmatrix}0\\-2\\0\end{pmatrix},
\qquad
AP_3=0.
$$

Bestimmen Sie $A$, $\ker(A)$, $\operatorname{col}(A)$, $\operatorname{rang}(A)$ und $\det(A)$.""",
        "zh_problem": r"""从 `ss25-2.png` 图中读出：

![ss25 Aufgabe 2](ss25-2.png)

$$
P_1=e_1,\qquad P_2=2e_2,\qquad P_3=\begin{pmatrix}1\\1\\1\end{pmatrix},
$$

并且

$$
AP_1=\begin{pmatrix}1\\0\\0\end{pmatrix},
\qquad
AP_2=\begin{pmatrix}0\\-2\\0\end{pmatrix},
\qquad
AP_3=0.
$$

求 $A$、$\ker(A)$、$\operatorname{col}(A)$、$\operatorname{rang}(A)$ 与 $\det(A)$。""",
        "solution": r"""Aus $AP_1=Ae_1$ folgt

$$
a_1=\begin{pmatrix}1\\0\\0\end{pmatrix}.
$$

Aus $P_2=2e_2$ und $AP_2=(0,-2,0)^T$ folgt

$$
a_2=Ae_2=\begin{pmatrix}0\\-1\\0\end{pmatrix}.
$$

Da $P_3=e_1+e_2+e_3$ und $AP_3=0$, gilt

$$
a_1+a_2+a_3=0,
$$

also

$$
a_3=-a_1-a_2=
\begin{pmatrix}-1\\1\\0\end{pmatrix}.
$$

Damit

$$
A=
\begin{pmatrix}
1&0&-1\\
0&-1&1\\
0&0&0
\end{pmatrix}.
$$

Der Spaltenraum ist

$$
\operatorname{col}(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\0\\0\end{pmatrix},
\begin{pmatrix}0\\-1\\0\end{pmatrix}
\right\}
=\{(x,y,0)^T:x,y\in\mathbb R\}.
$$

Also $\operatorname{rang}(A)=2$. Aus

$$
Ax=
\begin{pmatrix}
x_1-x_3\\
-x_2+x_3\\
0
\end{pmatrix}
=0
$$

folgt $x_1=x_2=x_3$. Daher

$$
\ker(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\}.
$$

Da $\operatorname{rang}(A)<3$, gilt

$$
\det(A)=0.
$$""",
        "zh_solution": r"""核心考点：**三维图像读矩阵列、核与列空间**。

图上 $P_1=e_1$，所以

$$
a_1=Ae_1=AP_1=\begin{pmatrix}1\\0\\0\end{pmatrix}.
$$

$P_2=2e_2$，图上 $AP_2=(0,-2,0)^T$，因此

$$
a_2=Ae_2=\frac12AP_2=\begin{pmatrix}0\\-1\\0\end{pmatrix}.
$$

又 $P_3=(1,1,1)^T=e_1+e_2+e_3$，且图上 $AP_3=0$，所以

$$
a_1+a_2+a_3=0
\Rightarrow
a_3=-a_1-a_2=\begin{pmatrix}-1\\1\\0\end{pmatrix}.
$$

因此

$$
A=
\begin{pmatrix}
1&0&-1\\
0&-1&1\\
0&0&0
\end{pmatrix}.
$$

列空间是 $xy$ 平面：

$$
\operatorname{col}(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\0\\0\end{pmatrix},
\begin{pmatrix}0\\-1\\0\end{pmatrix}
\right\},
$$

所以 $\operatorname{rang}(A)=2$。

解核：

$$
Ax=0
\Longleftrightarrow
x_1=x_2=x_3,
$$

所以

$$
\ker(A)=
\operatorname{span}\left\{
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\}.
$$

秩不是 $3$，所以 $\det(A)=0$。""",
    },
    ("ss25", 3): {
        "problem": r"""(a) Geben Sie eine Basis der symmetrischen $2\times2$-Matrizen an.

(b) Bestimmen und beweisen Sie Eigenwerte/Eigenvektoren von $A+cI_n$.

(c) Ist $U$ diagonalisierbar und hat nur Eigenwerte $\pm1$, zeigen Sie $U^{-1}=U$.

(d)-(f) Entscheiden Sie Aussagen zu Projektion, punktsymmetrischen Funktionen und linear unabhängigen Vereinigungen.""",
        "zh_problem": r"""(a) 给出对称 $2\times2$ 矩阵空间的一组基。

(b) 证明 $A+cI_n$ 的特征值/特征向量如何变化。

(c) 若 $U$ 可对角化且特征值只为 $\pm1$，证明 $U^{-1}=U$。

(d)-(f) 判断投影、奇函数子空间、线性无关并集相关命题真假。""",
        "solution": r"""(a) Eine Basis ist

$$
\left\{
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\right\}.
$$

(b) Ist $Av_i=\lambda_i v_i$, dann

$$
(A+cI)v_i=Av_i+cv_i=(\lambda_i+c)v_i.
$$

Also bleiben die Eigenvektoren gleich und die Eigenwerte werden zu $\lambda_i+c$.

(c) Da $U$ diagonalisierbar ist,

$$
U=SDS^{-1},
$$

wobei $D$ diagonal ist und nur Einträge $1$ oder $-1$ hat. Dann $D^2=I$, also

$$
U^2=SD^2S^{-1}=I.
$$

Damit $U^{-1}=U$.

(d) Wahr. Für $v\in W$ ist die orthogonale Projektion auf $W$ gleich $v$ selbst.

(e) Wahr. Punktsymmetrische Funktionen sind ungerade Funktionen. Für $f,g$ ungerade und $\alpha\in\mathbb R$ gilt

$$
(f+g)(-x)=-(f+g)(x),
\qquad
(\alpha f)(-x)=-(\alpha f)(x).
$$

(f) Falsch. In $\mathbb R^2$ setze

$$
A=\{e_1\},\quad B=\{e_2\},\quad C=\{e_1+e_2\}.
$$

Dann sind $A\cup B$, $A\cup C$ und $B\cup C$ jeweils linear unabhängig, aber

$$
(e_1+e_2)-e_1-e_2=0,
$$

also ist $A\cup B\cup C$ linear abhängig.""",
        "zh_solution": r"""核心考点：**基、特征值平移、对角化、投影与反例**。

(a) 对称 $2\times2$ 矩阵形如

$$
\begin{pmatrix}a&b\\b&c\end{pmatrix},
$$

所以一组基为

$$
\left\{
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\right\}.
$$

(b) 若 $Av_i=\lambda_i v_i$，则

$$
(A+cI)v_i=(\lambda_i+c)v_i.
$$

所以特征向量不变，特征值整体加 $c$。

(c) $U$ 可对角化，写成

$$
U=SDS^{-1}.
$$

$D$ 对角元只可能是 $1$ 或 $-1$，所以 $D^2=I$。于是

$$
U^2=SD^2S^{-1}=I,
$$

因此 $U^{-1}=U$。

(d) 真。$v$ 已经在 $W$ 里，投影到 $W$ 上不会改变它。

(e) 真。奇函数集合对加法和数乘封闭，并含零函数，所以是子空间。

(f) 假。反例：

$$
A=\{e_1\},\quad B=\{e_2\},\quad C=\{e_1+e_2\}.
$$

任意两个集合的并都线性无关，但三个合在一起有关系

$$
(e_1+e_2)-e_1-e_2=0.
$$""",
    },
    ("ss25", 4): {
        "problem": r"""Sei $A\in\mathbb R^{n\times n}$. Beweisen Sie:

$$
A\text{ ist invertierbar}
\Longleftrightarrow
\text{für jede linear unabhängige Menge }v_1,\ldots,v_k
\text{ ist }Av_1,\ldots,Av_k\text{ linear unabhängig}.
$$""",
        "zh_problem": r"""设 $A\in\mathbb R^{n\times n}$。证明：

$$
A\text{ 可逆}
\Longleftrightarrow
\text{任意线性无关组 }v_1,\ldots,v_k
\text{ 的像 }Av_1,\ldots,Av_k\text{ 仍线性无关}.
$$""",
        "solution": r"""**Hinrichtung.** Sei $A$ invertierbar und seien $v_1,\ldots,v_k$ linear unabhängig. Angenommen,

$$
\sum_{i=1}^k c_i Av_i=0.
$$

Dann

$$
A\left(\sum_{i=1}^k c_i v_i\right)=0.
$$

Multiplikation mit $A^{-1}$ liefert

$$
\sum_{i=1}^k c_i v_i=0.
$$

Da die $v_i$ linear unabhängig sind, folgt $c_1=\cdots=c_k=0$. Also sind $Av_1,\ldots,Av_k$ linear unabhängig.

**Rückrichtung.** Angenommen, $A$ erhält jede lineare Unabhängigkeit. Wäre $A$ nicht invertierbar, dann gäbe es ein $v\ne0$ mit

$$
Av=0.
$$

Die Menge $\{v\}$ ist linear unabhängig, aber ihr Bild $\{Av\}=\{0\}$ ist linear abhängig. Widerspruch. Also ist $A$ invertierbar.""",
        "zh_solution": r"""核心考点：**可逆线性映射保持线性无关**。

先证“可逆 $\Rightarrow$ 保持线性无关”。设 $v_1,\ldots,v_k$ 线性无关，并且

$$
\sum_{i=1}^k c_i Av_i=0.
$$

把 $A$ 提出来：

$$
A\left(\sum_{i=1}^k c_i v_i\right)=0.
$$

因为 $A$ 可逆，左右乘 $A^{-1}$ 得

$$
\sum_{i=1}^k c_i v_i=0.
$$

由 $v_i$ 线性无关，所有 $c_i=0$，所以 $Av_i$ 线性无关。

再证反向。若 $A$ 不可逆，则存在非零向量 $v$ 使

$$
Av=0.
$$

单个非零向量集合 $\{v\}$ 线性无关，但它的像是 $\{0\}$，线性相关。这与“保持所有线性无关组”矛盾。

因此 $A$ 必须可逆。""",
    },
})


TOPIC_SOLUTIONS = {
    "线性方程组、秩、核与像": {
        "de": [
            "1. Schreibe das Gleichungssystem als Matrixgleichung $Ax=b$ oder $Ax=0$.",
            "2. Bringe die Koeffizientenmatrix bzw. die erweiterte Matrix mit Gauß-Umformungen in Zeilenstufenform.",
            "3. Prüfe Widerspruchszeilen. Bei einer Zeile $0=c$ mit $c\\ne0$ gibt es keine Lösung.",
            "4. Bestimme die Pivotvariablen und freien Variablen. Die freien Variablen liefern die Parameter der Lösungsmenge.",
            "5. Für eine lineare Abbildung gilt $\\dim\\operatorname{Bild}f=\\operatorname{rang}A$ und $\\dim\\ker f=n-\\operatorname{rang}A$.",
        ],
        "zh": [
            "先把题目翻译成矩阵语言：齐次题是 $Ax=0$，非齐次题是 $Ax=b$，像空间问题就是问 $b$ 是否能写成 $Ax$。",
            "做高斯消元，把矩阵化成阶梯形。主元列告诉我们哪些变量被控制，自由变量告诉我们解空间有几个方向。",
            "如果增广矩阵出现 $0=c$ 且 $c\\ne0$，系统无解；如果没有矛盾行，就能继续写通解。",
            "齐次解空间的基来自自由变量分别取 $1,0,\\ldots$ 的那些方向向量。",
            "最后用 $\\dim\\ker f+\\dim\\operatorname{Bild}f=\\dim V$ 核对维数，避免算错。",
        ],
    },
    "矩阵可逆、行列式与秩": {
        "de": [
            "1. Entscheide zuerst, ob die Matrix quadratisch ist. Nur dann ist Invertierbarkeit im üblichen Sinn möglich.",
            "2. Nutze $A$ invertierbar $\\Longleftrightarrow\\det A\\ne0\\Longleftrightarrow\\operatorname{rang}A=n$.",
            "3. Für eine konkrete Inverse verwende $(A\\mid I)\\sim(I\\mid A^{-1})$.",
            "4. Bei Parameteraufgaben berechne $\\det A(\\alpha)$, setze die Nullstellen als Sonderfälle und untersuche dort den Rang.",
            "5. Bei Beweisaufgaben nutze Standardformeln wie $\\det(AB)=\\det A\\det B$, $(AB)^{-1}=B^{-1}A^{-1}$ und $\\operatorname{rang}(AB)\\le\\min(\\operatorname{rang}A,\\operatorname{rang}B)$.",
        ],
        "zh": [
            "先看矩阵尺寸。不是方阵时不能谈普通意义下的可逆；若乘积是方阵，也要看秩能不能满。",
            "判断可逆最省力的链条是 $A$ 可逆 $\\Longleftrightarrow\\det A\\ne0\\Longleftrightarrow\\operatorname{rang}A=n$。",
            "要求逆矩阵时，不要硬猜，用增广矩阵 $(A\\mid I)$ 做 Gauss-Jordan，左边化成 $I$，右边就是 $A^{-1}$。",
            "参数题先算行列式。行列式不为零的参数直接满秩；行列式为零的参数要单独代入做行化简。",
            "证明题常用行列式乘法、逆矩阵乘法顺序反转、秩不等式。比如 $5\\times3$ 乘 $3\\times5$ 的结果最多秩 $3$，所以不可能是 $5\\times5$ 可逆矩阵。",
        ],
    },
    "子空间、基、维数与仿射空间": {
        "de": [
            "1. Eine Basis braucht zwei Eigenschaften: Sie erzeugt den Raum und ist linear unabhängig.",
            "2. Lineare Unabhängigkeit prüft man über $\\sum_i\\lambda_i v_i=0$.",
            "3. Eine affine Hülle wird durch Abziehen eines Basispunktes linearisiert: $p+\\operatorname{span}(q_i-p)$.",
            "4. Die Dimension des affinen Raums ist die Dimension des zugehörigen Richtungsraums.",
            "5. Für Summen von Unterräumen kann man entweder Erzeuger reduzieren oder $\\dim(U+V)=\\dim U+\\dim V-\\dim(U\\cap V)$ nutzen.",
        ],
        "zh": [
            "基不是“看着顺眼的一组向量”，而是同时满足张成和线性无关。",
            "判断线性无关就设线性组合为零：$\\lambda_1v_1+\\cdots+\lambda_kv_k=0$，最后只能推出所有系数为零才无关。",
            "仿射空间题先选一个点 $p$，把其他点都减去 $p$，这样就变成方向向量的线性空间问题。",
            "方向空间的秩就是仿射空间维数。平行仿射空间只换起点，不换方向空间。",
            "求 $U+V$ 时，把所有生成向量放在一起行化简，主元个数就是维数；也可以用维数公式做检查。",
        ],
    },
    "群、同构与相似": {
        "de": [
            "1. Für eine Untergruppe prüfe: neutrales Element, Abgeschlossenheit und Inverses.",
            "2. Bei parametrisierten Matrizen muss zuerst das Produkt zweier allgemeiner Elemente berechnet werden.",
            "3. Wenn das Produkt der Matrizen einer einfachen Parameteroperation entspricht, ist der Isomorphismus meistens schon sichtbar.",
            "4. Für Isomorphie zeige Homomorphie, Injektivität und Surjektivität.",
            "5. Bei Ähnlichkeit $B=S^{-1}AS$ bleiben viele Strukturen erhalten, besonders Invertierbarkeit, Potenzen und Matrixpolynome.",
        ],
        "zh": [
            "群题不要从抽象定义硬背，先算两个一般元素的乘积，看参数怎么变化。",
            "如果出现 $M(a)M(b)=M(ab)$，那它对应的是乘法群；如果出现 $M(a)M(b)=M(a+b)$，那它对应的是加法群。",
            "子群证明按三件事走：单位元在里面、乘积还在里面、逆元还在里面。",
            "同构证明要写清楚：保运算、单射、满射。参数矩阵族通常用“参数映到矩阵”的函数。",
            "相似题用 $B=S^{-1}AS$。例如 $B^2=S^{-1}A^2S$，所以 $A$ 满足的矩阵多项式，$B$ 也满足。",
        ],
    },
    "矩阵幂、归纳与多项式方程": {
        "de": [
            "1. Bei Potenzformeln beginnt man mit dem Induktionsanfang.",
            "2. Die Induktionsannahme wird in $A^{n+1}=A^nA$ eingesetzt.",
            "3. Danach wird nur noch die Matrixmultiplikation vereinfacht, bis die Formel mit $n+1$ entsteht.",
            "4. Für negative Potenzen braucht man zuerst Invertierbarkeit und dann $A^{-n}=(A^n)^{-1}$.",
            "5. Bei Matrixpolynomen wie $A^2=3A+4I$ kann man Terme umstellen, um direkt eine Inverse zu finden.",
        ],
        "zh": [
            "矩阵幂公式题本质不是拼命乘，而是归纳法：先验证起点，再证明从 $n$ 到 $n+1$。",
            "归纳步固定写成 $A^{n+1}=A^nA$，把假设的闭式代进去，再做一次矩阵乘法。",
            "若题目问负幂，必须先证明 $A$ 可逆，然后用 $A^{-n}=(A^n)^{-1}$。",
            "矩阵方程题要会“移项找逆”。比如 $A^2=3A+4I$ 可写为 $A(A-3I)=4I$，所以 $A^{-1}=\\frac14(A-3I)$。",
            "相似矩阵满足同样的多项式方程，因为 $S^{-1}p(A)S=p(S^{-1}AS)$。",
        ],
    },
    "线性映射与矩阵表示": {
        "de": [
            "1. Linearität zeigt man mit $f(\\lambda x+\\mu y)=\\lambda f(x)+\\mu f(y)$.",
            "2. Die darstellende Matrix in der Standardbasis ist $M=(f(e_1),\\ldots,f(e_n))$.",
            "3. Der Kern entsteht aus $Mx=0$, das Bild aus dem Spaltenraum von $M$.",
            "4. Für $f(x)=x+(a^Tx)b$ ist die Matrix $M=I+ba^T$.",
            "5. In endlichdimensionalen Räumen entscheidet der Kern über Injektivität und der Rang über Surjektivität.",
        ],
        "zh": [
            "线性映射先验证加法和数乘合在一起：$f(\\lambda x+\mu y)=\\lambda f(x)+\mu f(y)$。",
            "写矩阵时最稳的方法是算 $f(e_1),\\ldots,f(e_n)$，这些像向量就是矩阵的列。",
            "核用 $Mx=0$ 解，像用列空间看，秩就是列空间维数。",
            "秩一扰动 $f(x)=x+(a^Tx)b$ 的矩阵是 $I+ba^T$，因为 $(ba^T)x=b(a^Tx)$。",
            "可逆/单射/满射用核和秩判断：同维空间里，核为零、满秩、可逆是同一件事的不同说法。",
        ],
    },
    "特征值、特征空间与对角化": {
        "de": [
            "1. Eigenwerte sind Nullstellen von $\\chi_A(\\lambda)=\\det(A-\\lambda I)$.",
            "2. Der Eigenraum zu $\\lambda$ ist $\\ker(A-\\lambda I)$.",
            "3. Algebraische Vielfachheit kommt aus dem charakteristischen Polynom; geometrische Vielfachheit ist die Dimension des Eigenraums.",
            "4. Eine Matrix ist diagonalisierbar, wenn es genügend viele linear unabhängige Eigenvektoren gibt.",
            "5. Für $A+cI$ werden die Eigenwerte um $c$ verschoben, die Eigenvektoren bleiben gleich.",
        ],
        "zh": [
            "先算特征多项式 $\chi_A(\lambda)=\det(A-\lambda I)$，根就是特征值。",
            "每个特征值都要代回去解 $(A-\lambda I)x=0$，这个解空间就是特征空间。",
            "代数重数看特征多项式中因子的次数，几何重数看特征空间维数。",
            "对角化不是“有特征值”就行，而是要凑够 $n$ 个线性无关特征向量。",
            "如果 $Av=\lambda v$，那么 $(A+cI)v=(\lambda+c)v$，所以平移矩阵只平移特征值。",
        ],
    },
    "正交投影、最小二乘与内积": {
        "de": [
            "1. Schreibe die Projektion als Linearkombination der Basisvektoren des Unterraums.",
            "2. Der Fehlervektor muss orthogonal zum Unterraum sein.",
            "3. Daraus entstehen Gleichungen $\\langle v-\\hat v,u_i\\rangle=0$.",
            "4. In Matrixform sind das die Normalgleichungen $A^TAx=A^Tb$.",
            "5. Die Lösung liefert $\\hat v$, danach ist $z=v-\\hat v$.",
        ],
        "zh": [
            "投影题先设 $\hat v=c_1u_1+\cdots+c_ku_k$，因为投影一定在 $W$ 里面。",
            "关键条件是误差 $z=v-\hat v$ 垂直于整个 $W$，所以只需让它垂直于 $W$ 的一组基。",
            "写出 $\langle v-\hat v,u_i\rangle=0$ 得到线性方程组。",
            "如果用矩阵表示，这就是最小二乘的法方程 $A^TAx=A^Tb$。",
            "求出系数后得到 $\hat v$，再用 $z=v-\hat v$，最后检查 $z\perp W$。",
        ],
    },
    "图、邻接矩阵与矩阵变换": {
        "de": [
            "1. Bei einer linearen Transformation ist die $i$-te Spalte von $A$ gleich $Ae_i$.",
            "2. Der Spaltenraum ist der Spann der Bildvektoren der Standardbasis.",
            "3. Der Rang ist die Dimension dieses Spaltenraums.",
            "4. Der Kern besteht aus allen Linearkombinationen der Ausgangsvektoren, die auf $0$ abgebildet werden.",
            "5. Bei Adjazenzmatrizen zählt $(A^k)_{ij}$ Wege der Länge $k$ von $i$ nach $j$.",
        ],
        "zh": [
            "图形变换题要盯住标准基：$Ae_i$ 就是矩阵第 $i$ 列。",
            "列空间就是这些像向量张成的空间，秩就是它的维数。",
            "如果图像被压到直线或平面，行列式通常为 0，因为体积被压扁了。",
            "核是被映到 0 的方向，通常从列之间的线性关系读出来，再用 $Ax=0$ 核对。",
            "邻接矩阵题用路径计数：$(A^k)_{ij}$ 等于从点 $i$ 到点 $j$ 长度为 $k$ 的路径条数。",
        ],
    },
    "抽象向量空间、函数空间与对偶": {
        "de": [
            "1. Für Unterräume prüfe Nullvektor, Addition und skalare Multiplikation.",
            "2. Für Funktionenräume werden Addition und Skalarmultiplikation punktweise geprüft.",
            "3. Die duale Basis erfüllt $g_i(u_j)=\\delta_{ij}$.",
            "4. Lineare Abbildungen sind durch ihre Werte auf einer Basis eindeutig bestimmt.",
            "5. Für Produkträume laufen alle Rechnungen komponentenweise.",
        ],
        "zh": [
            "抽象空间题仍然是老三样：零元、加法封闭、数乘封闭。",
            "函数空间不要怕，把等式逐点检查即可，例如奇函数集合对加法和数乘封闭。",
            "对偶基的定义是 $g_i(u_j)=\delta_{ij}$，它像一个“坐标读取器”。",
            "证明对偶基线性无关时，设 $\sum c_ig_i=0$，代入 $u_j$ 就能单独抓出 $c_j=0$。",
            "直积空间按分量做运算，维数等于各分量维数之和。",
        ],
    },
}


def source_table():
    actual = Counter(item[0] for item in ITEMS)
    rows = [
        "| 试卷文件 | 原卷主 Aufgabe 数 | 本文件纳入数 | 核对 |",
        "|---|---:|---:|---|",
    ]
    for exam, n in EXPECTED.items():
        rows.append(f"| {exam} | {n} | {actual[exam]} | {'一致' if n == actual[exam] else '不一致'} |")
    rows.append(f"| **总计** | **{sum(EXPECTED.values())}** | **{len(ITEMS)}** | **一致** |")
    return rows


def formula_lines(topic):
    rows = ["| 名称 | 公式 | 应用场景 |", "|---|---|---|"]
    for name, formula, scene in FORMULAS.get(topic, []):
        rows.append(f"| {table_cell(name)} | {table_cell(formula)} | {table_cell(scene)} |")
    return rows


def table_cell(value):
    return str(value).replace("|", "\\|")


def render_solution_steps(steps):
    return "\n".join(steps)


def render_chinese_concrete_steps(solution):
    math_blocks = re.findall(r"\$\$(.*?)\$\$", solution, flags=re.S)
    if not math_blocks:
        return clean_chunk(solution)

    labels = [
        "第 1 步：把题目对象写成可计算的矩阵/公式形式。",
        "第 2 步：进行第一次关键化简，通常是消去主元下方元素或代入定义。",
        "第 3 步：继续化简，把已经得到的主元用于消去其它位置。",
        "第 4 步：把左侧整理成目标形式，例如单位矩阵、阶梯形、特征方程或所需等式。",
        "第 5 步：读取最终答案，并用相应公式解释结论。",
    ]
    lines = []
    for i, block in enumerate(math_blocks):
        label = labels[i] if i < len(labels) else f"第 {i + 1} 步：继续按照上一行结果化简并读取结论。"
        lines.append(label)
        lines.append("")
        lines.append(f"$${block.strip()}$$")
        lines.append("")
    return "\n".join(lines).strip()


def render_chinese_problem(zh_q, original_problem):
    if not original_problem:
        return zh_q

    math_blocks = re.findall(r"\$\$(.*?)\$\$", original_problem, flags=re.S)

    lines = [zh_q]
    if math_blocks:
        lines.append("")
        lines.append("题目中的公式、矩阵和参数：")
        lines.append("")
    for block in math_blocks:
        lines.append(f"$${block.strip()}$$")
        lines.append("")
    return "\n".join(lines).strip()


def clean_chunk(text):
    text = text.strip()
    text = re.sub(r"(?m)^\s*\*\*\(\d+\s*Punkte\)\*\*\s*$", "", text)
    text = re.sub(r"(?m)^\s*\(\d+\s*Punkte\)\s*$", "", text)
    text = re.sub(r"(?m)^\s*\d+n?\(\d+\s*Punkte\)\s*$", "", text)
    text = re.sub(r"\s*\*\*\(\d+\s*Punkte\)\*\*", "", text)
    text = re.sub(r"\(\d+\s*Punkte\)", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def render_cheatsheet():
    lines = ["## 全卷公式 Cheatsheet", ""]
    lines.append("> 考试可带小抄时，优先背这一部分：公式名、公式、什么时候用。")
    lines.append("")
    for category, rows in CHEATSHEET.items():
        lines.append(f"### {category}")
        lines.append("")
        lines.append("| 公式/工具 | 公式 | 应用场景 |")
        lines.append("|---|---|---|")
        for name, formula, usage in rows:
            lines.append(f"| {table_cell(name)} | {table_cell(formula)} | {table_cell(usage)} |")
        lines.append("")
    return lines


BAD_OCR_CHARS = set("​")
BAD_OCR_SNIPPETS = (
    "x∈R3x",
    "x↦Axx",
    "A∈R3×3A",
    "V=RnV",
    "A∪BA",
)


def is_bad_ocr(text):
    return any(ch in text for ch in BAD_OCR_CHARS) or any(snippet in text for snippet in BAD_OCR_SNIPPETS)


def marker_pattern(exam):
    if exam in {"ss00", "ss01", "ss08", "ss25"}:
        return re.compile(r"(?m)^## Aufgabe\s+(\d+)\s*$")
    if exam.startswith("ss22") or exam.startswith("ss24"):
        return re.compile(r"(?m)^Aufgabe\s+(\d+)\s*$")
    if exam in {"ss20", "ss21"}:
        return re.compile(r"(?m)^\s*(\d+)\.\s+")
    return re.compile(r"(?m)^\s*\f?\s*(\d+)n?\s*\(6 Punkte\)\s*$")


def load_exam_chunks():
    chunks = {}
    for exam in EXPECTED:
        path = TEXT_DIR / f"{exam}.txt"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        pattern = marker_pattern(exam)
        matches = list(pattern.finditer(text))
        if not matches and exam == "ss19":
            # The ss19 extraction contains form-feed/control characters around task numbers.
            pattern = re.compile(r"(?m)^\s*\f?\s*(\d+)\s*$")
            matches = [m for m in pattern.finditer(text) if 1 <= int(m.group(1)) <= EXPECTED[exam]]
        for idx, match in enumerate(matches):
            no = int(match.group(1))
            if no < 1 or no > EXPECTED[exam]:
                continue
            start = match.start()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
            chunks[(exam, no)] = clean_chunk(text[start:end])
    return chunks


SOLUTION_MARKERS = [
    "### Lösung:",
    "### L枚sung:",
    "Lösung:",
    "L枚sung:",
    "Lösung:",
    "Lo虉sung:",
    "Beweis:",
    "### Lösung",
]


def split_problem_solution(chunk):
    if not chunk:
        return "", ""
    positions = [chunk.find(marker) for marker in SOLUTION_MARKERS if chunk.find(marker) != -1]
    if not positions:
        return clean_chunk(chunk), ""
    pos = min(positions)
    return clean_chunk(chunk[:pos]), clean_chunk(chunk[pos:])


def main():
    actual = Counter(item[0] for item in ITEMS)
    assert sum(EXPECTED.values()) == len(ITEMS)
    for exam, expected in EXPECTED.items():
        assert actual[exam] == expected, (exam, expected, actual[exam])

    grouped = defaultdict(list)
    for item in ITEMS:
        grouped[item[2]].append(item)
    original_chunks = load_exam_chunks()

    lines = []
    lines.append("# 历史考试考点汇总：完整题目与题解")
    lines.append("")
    lines.append("> 说明：本文件按 `历史考试` 根目录主试卷整理；每个主 `Aufgabe` 独立成题，子问并入同一题。PDF 中部分早年公式 OCR 有乱码，因此这里采用“完整可练习题意 + 完整解题流程”的整理方式，而不是只贴 OCR 原文。")
    lines.append("")
    lines.extend(render_cheatsheet())
    lines.append("## 0. 来源与数量核对")
    lines.extend(source_table())
    lines.append("")

    for topic, rows in grouped.items():
        lines.append(f"## {topic}")
        lines.append("")
        lines.append("### 1. 所涉及的公式")
        lines.extend(formula_lines(topic))
        lines.append("")
        for exam, no, _, de_q, zh_q, de_short, zh_short in rows:
            sol = TOPIC_SOLUTIONS[topic]
            original = original_chunks.get((exam, no), "")
            original_problem, original_solution = split_problem_solution(original)
            override = MANUAL_OVERRIDES.get((exam, no))
            if override:
                original_problem = clean_chunk(override["problem"])
                original_solution = clean_chunk(override["solution"])
            else:
                # Only manually reviewed entries are allowed in the final study file.
                # Raw OCR from old exam PDFs is too noisy and must not be presented as a finished solution.
                original_problem = ""
                original_solution = ""
            if not override and is_bad_ocr(original_solution):
                original_solution = ""
                if is_bad_ocr(original_problem):
                    original_problem = ""
            elif not override and is_bad_ocr(original_problem):
                original_problem = ""
            lines.append(f"### {exam} Aufgabe {no}")
            lines.append("")
            lines.append("#### 2. Deutsche Aufgabe")
            if original_problem:
                lines.append(original_problem)
            else:
                lines.append(de_q)
            lines.append("")
            lines.append("#### 3. 中文题目")
            if override and override.get("zh_problem"):
                lines.append(clean_chunk(override["zh_problem"]))
            else:
                lines.append(render_chinese_problem(zh_q, original_problem))
            lines.append("")
            lines.append("#### 4. Deutsche Lösung")
            if original_solution:
                lines.append(original_solution)
            else:
                lines.append("**待逐题重写 / Muss noch einzeln sauber ausgearbeitet werden.**")
            lines.append("")
            lines.append("#### 5. 中文解答")
            if override and override.get("zh_solution"):
                lines.append(clean_chunk(override["zh_solution"]))
                lines.append("")
            elif original_solution:
                lines.append(f"核心考点：**{topic}**。")
                lines.append("")
                lines.append("中文化具体计算步骤如下。这里保留原卷的矩阵化简、公式推导和结论，并按步骤说明每一行在做什么：")
                lines.append("")
                lines.append(render_chinese_concrete_steps(original_solution))
                lines.append("")
            else:
                lines.append(f"核心考点：**{topic}**。")
                lines.append("")
                lines.append("**待逐题重写。** 当前条目还没有经过人工清洗，不能当作最终解答使用。")
                lines.append("")

    topic_counts = Counter(item[2] for item in ITEMS)
    reviewed_count = sum(1 for exam, no, *_ in ITEMS if (exam, no) in MANUAL_OVERRIDES)
    pending_count = len(ITEMS) - reviewed_count
    lines.append("## 6. 知识点考察次数统计")
    lines.append("")
    lines.append("| 考点 | 考察题数 | 涉及题目 |")
    lines.append("|---|---:|---|")
    for topic, count in topic_counts.most_common():
        refs = "；".join(f"{exam} Aufgabe {no}" for exam, no, t, *_ in ITEMS if t == topic)
        lines.append(f"| {topic} | {count} | {refs} |")
    lines.append(f"| **总计** | **{len(ITEMS)}** | 与来源核对表一致 |")
    lines.append("")
    lines.append("### 核对结论")
    lines.append("")
    lines.append(f"- 历年试卷主 Aufgabe 总数：{sum(EXPECTED.values())}。")
    lines.append(f"- 本文件纳入题目总数：{len(ITEMS)}。")
    lines.append(f"- 已逐题人工重写题目数：{reviewed_count}。")
    lines.append(f"- 待逐题人工重写题目数：{pending_count}。")
    lines.append("- 之后只把人工重写后的题目标为完整题解；未重写条目不会再用 OCR 原文或通用模板冒充答案。")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} with {len(ITEMS)} full QA entries.")


if __name__ == "__main__":
    main()
