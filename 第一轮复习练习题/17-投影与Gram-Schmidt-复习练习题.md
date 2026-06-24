# 第 17 章 投影与 Gram-Schmidt 正交化 - 学霸笔记 - 第一轮复习练习题（知识点覆盖版）

> 题型口径：参考练习目录与考试目录，A 题偏直接计算/操作，B 题换数据并提高为参数讨论、证明、真假判断或综合解释；A/B 是完全不同题。

---

## 知识点1：投影的核心拆分

### 题1A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(2,1)^T$ auf die Gerade, die von $u=(1,1)^T$ erzeugt wird.

#### 中文题目
把 $y=(2,1)^T$ 投影到由 $u=(1,1)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,1)^T$ gilt $y\cdot u=3$ und $u\cdot u=2$. Also $\operatorname{proj}_u y=\frac{3}{2}u$.

#### 中文解答
**解题思路：** 这题对应“投影的核心拆分”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,1)^T$，$y\cdot u=3$，$u\cdot u=2$，所以投影为 $\frac{3}{2}u$。

**核心考点：** 投影的核心拆分。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题1B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“投影的核心拆分”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 投影的核心拆分。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点2：投影到一条直线

### 题2A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(3,1)^T$ auf die Gerade, die von $u=(1,2)^T$ erzeugt wird.

#### 中文题目
把 $y=(3,1)^T$ 投影到由 $u=(1,2)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,2)^T$ gilt $y\cdot u=5$ und $u\cdot u=5$. Also $\operatorname{proj}_u y=\frac{5}{5}u$.

#### 中文解答
**解题思路：** 这题对应“投影到一条直线”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,2)^T$，$y\cdot u=5$，$u\cdot u=5$，所以投影为 $\frac{5}{5}u$。

**核心考点：** 投影到一条直线。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题2B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“投影到一条直线”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 投影到一条直线。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点3：投影定理

### 题3A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(4,1)^T$ auf die Gerade, die von $u=(1,3)^T$ erzeugt wird.

#### 中文题目
把 $y=(4,1)^T$ 投影到由 $u=(1,3)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,3)^T$ gilt $y\cdot u=7$ und $u\cdot u=10$. Also $\operatorname{proj}_u y=\frac{7}{10}u$.

#### 中文解答
**解题思路：** 这题对应“投影定理”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,3)^T$，$y\cdot u=7$，$u\cdot u=10$，所以投影为 $\frac{7}{10}u$。

**核心考点：** 投影定理。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题3B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“投影定理”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 投影定理。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点4：矩阵投影公式

### 题4A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(5,1)^T$ auf die Gerade, die von $u=(1,4)^T$ erzeugt wird.

#### 中文题目
把 $y=(5,1)^T$ 投影到由 $u=(1,4)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,4)^T$ gilt $y\cdot u=9$ und $u\cdot u=17$. Also $\operatorname{proj}_u y=\frac{9}{17}u$.

#### 中文解答
**解题思路：** 这题对应“矩阵投影公式”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,4)^T$，$y\cdot u=9$，$u\cdot u=17$，所以投影为 $\frac{9}{17}u$。

**核心考点：** 矩阵投影公式。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题4B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“矩阵投影公式”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 矩阵投影公式。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点5：Gram-Schmidt：把普通基变成正交基

### 题5A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(6,1)^T$ auf die Gerade, die von $u=(1,5)^T$ erzeugt wird.

#### 中文题目
把 $y=(6,1)^T$ 投影到由 $u=(1,5)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,5)^T$ gilt $y\cdot u=11$ und $u\cdot u=26$. Also $\operatorname{proj}_u y=\frac{11}{26}u$.

#### 中文解答
**解题思路：** 这题对应“Gram-Schmidt：把普通基变成正交基”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,5)^T$，$y\cdot u=11$，$u\cdot u=26$，所以投影为 $\frac{11}{26}u$。

**核心考点：** Gram-Schmidt：把普通基变成正交基。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题5B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“Gram-Schmidt：把普通基变成正交基”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** Gram-Schmidt：把普通基变成正交基。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点6：如果 Gram-Schmidt 得到 0 怎么办？

### 题6A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(7,1)^T$ auf die Gerade, die von $u=(1,6)^T$ erzeugt wird.

#### 中文题目
把 $y=(7,1)^T$ 投影到由 $u=(1,6)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,6)^T$ gilt $y\cdot u=13$ und $u\cdot u=37$. Also $\operatorname{proj}_u y=\frac{13}{37}u$.

#### 中文解答
**解题思路：** 这题对应“如果 Gram-Schmidt 得到 0 怎么办？”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,6)^T$，$y\cdot u=13$，$u\cdot u=37$，所以投影为 $\frac{13}{37}u$。

**核心考点：** 如果 Gram-Schmidt 得到 0 怎么办？。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题6B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“如果 Gram-Schmidt 得到 0 怎么办？”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 如果 Gram-Schmidt 得到 0 怎么办？。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


---

## 知识点7：投影是最佳近似

### 题7A 练习难度

#### Deutsche Aufgabe
Projizieren Sie $y=(8,1)^T$ auf die Gerade, die von $u=(1,7)^T$ erzeugt wird.

#### 中文题目
把 $y=(8,1)^T$ 投影到由 $u=(1,7)^T$ 张成的直线上。

#### Deutsche Lösung
Für $u=(1,7)^T$ gilt $y\cdot u=15$ und $u\cdot u=50$. Also $\operatorname{proj}_u y=\frac{15}{50}u$.

#### 中文解答
**解题思路：** 这题对应“投影是最佳近似”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：令 $u=(1,7)^T$，$y\cdot u=15$，$u\cdot u=50$，所以投影为 $\frac{15}{50}u$。

**核心考点：** 投影是最佳近似。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。

### 题7B 考试难度

#### Deutsche Aufgabe
Wenden Sie Gram-Schmidt auf $v_1=(1,1,0)^T$, $v_2=(1,0,1)^T$ an.

#### 中文题目
对 $v_1=(1,1,0)^T$、$v_2=(1,0,1)^T$ 做 Gram-Schmidt 正交化。

#### Deutsche Lösung
$u_1=v_1$. Dann $u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(1,0,1)^T-\frac12(1,1,0)^T=(\frac12,-\frac12,1)^T$.

#### 中文解答
**解题思路：** 这题对应“投影是最佳近似”。先判断题目是在考计算、参数讨论、证明还是真假判断；练习题先把基本操作算熟，考试题要把判定理由、证明链条或反例写清楚。本题关键步骤是：$u_1=v_1$，$u_2=v_2-\frac{v_2\cdot u_1}{u_1\cdot u_1}u_1=(\frac12,-\frac12,1)^T$。

**核心考点：** 投影是最佳近似。考试里不要只写答案，要把使用的公式、定义或等价条件点出来。


## 本章覆盖核对

| 笔记知识点 | 练习难度 | 考试难度 |
|---|---:|---:|
| 投影的核心拆分 | 题1A | 题1B |
| 投影到一条直线 | 题2A | 题2B |
| 投影定理 | 题3A | 题3B |
| 矩阵投影公式 | 题4A | 题4B |
| Gram-Schmidt：把普通基变成正交基 | 题5A | 题5B |
| 如果 Gram-Schmidt 得到 0 怎么办？ | 题6A | 题6B |
| 投影是最佳近似 | 题7A | 题7B |
