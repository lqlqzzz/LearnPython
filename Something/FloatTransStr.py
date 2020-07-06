# -*- coding: utf-8 -*-
# @Time : 2020/7/6 14:38
# @Author : LQ

import numpy as np

# float转str
Arr = np.array([[0.0033, 0.00000001], [1, -0.0000005]], dtype=np.float32)
Arr_str = ''
for line in Arr:
    Arr_str = Arr_str + ','.join([str(x) for x in line]) + '|'
print(Arr_str)
# str转float
Arr_float = []
for line in Arr_str[:-1].split('|'):
    line_i = line.split(',')
    Arr_float.append([float(x) for x in line_i])
Arr_np = np.array(Arr_float, dtype=np.float32)
print(Arr_np)
