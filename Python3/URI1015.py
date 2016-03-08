# -*- coding: utf-8 -*-
import math
p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
print('%.4f' %(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))))
