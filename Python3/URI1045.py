# -*- coding: utf-8 -*-
value = input().split(' ')
A, B, C = value
A = float(A)
B = float(B)
C = float(C)
if (A<B):
    menor = A
    A = B
    B = menor
if B<C:
    menor = B
    B = C
    C = menor
if A<B:
    menor = A
    A = B
    B = menor
if A >= (B+C):
    print('NAO FORMA TRIANGULO')
else:
    if A*A == ((B*B)+(C*C)):
        print('TRIANGULO RETANGULO')
    if A*A > ((B*B)+(C*C)):
        print('TRIANGULO OBTUSANGULO')
    if A*A < ((B*B)+(C*C)):
        print('TRIANGULO ACUTANGULO')
    if A==B and B==C:
        print('TRIANGULO EQUILATERO')
    elif A==B or B==C or A==C:
        print('TRIANGULO ISOSCELES')
