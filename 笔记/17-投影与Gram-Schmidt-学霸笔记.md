# 第 17 章：投影与 Gram-Schmidt 正交化 - 学霸笔记

> 讲义：`讲义/17-projektion.pdf`  
> 教材：`分章节教材/05-Orthogonalitaet-und-Projektionen.pdf` 第 5.7 节  
> 核心主题：正交投影（orthogonale Projektion）、投影定理（Projektionstheorem）、Gram-Schmidt 方法（Gram-Schmidt-Verfahren）、最佳近似（beste Annäherung）

---

## 0. 这一章到底在解决什么问题？

给一个向量 $v$ 和一个子空间 $W$，我们经常想问：

> 在 $W$ 里面，哪个向量最像 $v$？

答案是 $v$ 在 $W$ 上的正交投影（orthogonale Projektion）：

$$
\hat v=\operatorname{proj}_W v
$$

剩下的误差：

$$
z=v-\hat v
$$

必须垂直于 $W$：

$$
z\in W^\perp
$$

这就是本章主线。

---

## 1. 投影的核心拆分

对任意 $v\in V$ 和有限维子空间 $W$，可以唯一写成：

$$
v=\hat v+z
$$

其中：

- $\hat v\in W$：投影（Projektion）
- $z\in W^\perp$：残差（Residuum）

直觉：

> $\hat v$ 是 $W$ 里离 $v$ 最近的影子，$z$ 是从影子垂直到原向量的误差。

---

## 2. 投影到一条直线

如果 $L=\operatorname{span}\{u\}$，投影一定形如：

$$
\hat y=cu
$$

残差：

$$
z=y-\hat y=y-cu
$$

必须垂直于 $u$：

$$
\langle u,y-cu\rangle=0
$$

展开：

$$
\langle u,y\rangle-c\langle u,u\rangle=0
$$

所以

$$
c=\frac{\langle u,y\rangle}{\langle u,u\rangle}
$$

投影公式：

$$
\operatorname{proj}_L y=\frac{\langle u,y\rangle}{\langle u,u\rangle}u
$$

---

## 3. 投影定理

设 $W$ 是内积空间 $V$ 的有限维子空间。

### 结论 1：唯一拆分

每个 $v\in V$ 都能唯一写成：

$$
v=\hat v+z
$$

其中：

$$\hat v\in W,\quad z\in W^\perp$$

### 结论 2：用正交基算投影

如果

$$
W=\operatorname{span}\{w_1,\ldots,w_k\}
$$

且 $w_1,\ldots,w_k$ 是 $W$ 的正交基（Orthogonalbasis），那么：

$$
\operatorname{proj}_W v
=
\frac{\langle v,w_1\rangle}{\langle w_1,w_1\rangle}w_1
+\cdots+
\frac{\langle v,w_k\rangle}{\langle w_k,w_k\rangle}w_k
$$

如果是标准正交基，分母都是 1。

---

## 4. 矩阵投影公式

如果 $U\in\mathbb{R}^{n\times k}$ 的列向量构成子空间 $W$ 的正交基，那么：

$$
\operatorname{proj}_W v=U(U^\top U)^{-1}U^\top v
$$

如果 $U$ 的列是标准正交的，那么 $U^\top U=I$，公式简化为：

$$
\operatorname{proj}_W v=UU^\top v
$$

---

## 5. Gram-Schmidt：把普通基变成正交基

Gram-Schmidt 方法（Gram-Schmidt-Verfahren）可以把一组线性无关向量正交化，而且不改变张成空间。

给定：

$$
v_1,\ldots,v_n
$$

构造：

$$
u_1=v_1
$$

$$
u_2=v_2-\operatorname{proj}_{\operatorname{span}\{u_1\}}v_2
$$

$$
u_3=v_3-\operatorname{proj}_{\operatorname{span}\{u_1,u_2\}}v_3
$$

一直做下去：

$$
u_k=v_k-\operatorname{proj}_{\operatorname{span}\{u_1,\ldots,u_{k-1}\}}v_k
$$

得到的 $u_1,\ldots,u_k$ 正交，并且：

$$
\operatorname{span}\{v_1,\ldots,v_k\}
=
\operatorname{span}\{u_1,\ldots,u_k\}
$$

### 如果想要标准正交基

把每个 $u_j$ 标准化：

$$
w_j=\frac{u_j}{\|u_j\|}
$$

---

## 6. 如果 Gram-Schmidt 得到 0 怎么办？

如果 $v_3\in\operatorname{span}\{v_1,v_2\}$，那么前两个向量已经张成了 $v_3$ 所在方向。

Gram-Schmidt 第三步会得到：

$$
u_3=0
$$

这说明 $v_3$ 没有带来新方向，应该丢掉。

所以 Gram-Schmidt 产生基的前提是：原向量组线性无关。否则会出现零向量。

---

## 7. 投影是最佳近似

定理：

如果 $W$ 是 $V$ 的子空间，$v\in V$，那么

$$
\operatorname{proj}_W v
$$

是 $W$ 中对 $v$ 的最佳近似（beste Annäherung）：

$$
\|v-\operatorname{proj}_Wv\|<\|v-w\|
$$

对所有

$$
w\in W,\quad w\neq \operatorname{proj}_Wv
$$

都成立。

这就是最小二乘的几何根源。

---

## 8. R 语言练习

### 8.1 投影到一条直线

```r
y <- c(0, 4, 7)
u <- c(1, 1, 2)

proj_line <- sum(u * y) / sum(u * u) * u
proj_line

resid <- y - proj_line
sum(resid * u)  # 应该接近 0
```

### 8.2 矩阵投影

```r
U <- matrix(c(1, 0,
              1, 1,
              0, 1),
            nrow = 3, byrow = TRUE)

proj <- U %*% solve(t(U) %*% U) %*% t(U) %*% y
proj
```

### 8.3 简单 Gram-Schmidt

```r
v1 <- c(1, 1, 0)
v2 <- c(1, 0, 1)

u1 <- v1
u2 <- v2 - sum(u1 * v2) / sum(u1 * u1) * u1

sum(u1 * u2)

w1 <- u1 / sqrt(sum(u1^2))
w2 <- u2 / sqrt(sum(u2^2))

sum(w1 * w2)
sqrt(sum(w1^2))
sqrt(sum(w2^2))
```

---

## 9. 本章一页复盘

| 问题 | 答案 |
|---|---|
| 投影是什么？ | $W$ 中离 $v$ 最近的向量 |
| 残差是什么？ | $z=v-\hat v$ |
| 残差有什么性质？ | $z\perp W$ |
| 投影到直线公式 | $\frac{\langle u,y\rangle}{\langle u,u\rangle}u$ |
| 投影矩阵公式 | $U(U^\top U)^{-1}U^\top$ |
| Gram-Schmidt 做什么？ | 正交化，不改变 span |
| 投影为什么重要？ | 它是最佳近似 |

最后一句：

> 投影就是把“不在空间里的东西”拉回空间里，而且拉到最近的位置。
