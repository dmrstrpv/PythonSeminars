# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

n = math.pi
d = 0.001
i = 0
while d < 1:
    i += 1
    d = d*10
print(round(n, i))