# -*- coding: utf-8 -*-
line = input().split(" ")
A, B, C = line
A = float(A)
B = float(B)
C = float(C)
print("TRIANGULO: %.3f" %((A*C) / 2))
print("CIRCULO: %.3f" %(3.14159 * C**2))
print("TRAPEZIO: %.3f" %(((A + B) * C ) / 2))
print("QUADRADO: %.3f" %(B * B))
print("RETANGULO: %.3f" %(A * B))
