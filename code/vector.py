import numpy as np

# 定义
v_numeric = (1, 2, 3, 4, 5)
v_string = ('a', 'b', 'c', 'd', 'e')
v_boolean = (True, False, True, False, True)

# 向量的长度
print(len(v_numeric))

# 向量的加法 - 图形上的意义是向量的平移
v = (1,2)
w = (3,4)
z_a = tuple(v_i + w_i for v_i, w_i in zip(v, w))
print(z_a)

# 向量的标量乘法 - 伸缩Scaling
z_m = tuple(2 * v_i for v_i in v)
print(z_m)

# 向量的线性组合
a = 2
b = 3
z_l = tuple(a * v_i + b * w_i for v_i, w_i in zip(v, w))
print(z_l)

v = np.array((1,2))
w = np.array((3,4))
a = 2
b = 3
z_l = a * v + b * w
print(z_l)

v = np.array((1,2))
w = np.array((3,4))
u = np.array((5,6))
a = 2
b = 3
c = 4
z_l = a * v + b * w + c * u
print(z_l)