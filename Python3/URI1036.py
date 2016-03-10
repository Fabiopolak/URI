# -*- coding: utf-8 -*-
import math
value = input().split(" ")
A, B, C = value
A = float(A)
B = float(B)
C = float(C)
delta = B*B - 4*A*C
if A==0 or delta<0:
    print('Impossivel calcular')
else:
    print('R1 = %.5f' %(((-B) + math.sqrt(delta))/(2*A)))
    print('R2 = %.5f' %(((-B) - math.sqrt(delta))/(2*A)))


