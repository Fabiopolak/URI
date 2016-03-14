value = input().split(' ')
A, B, C = value
A = float(A)
B = float(B)
C = float(C)
if (A<B+C) and (B<A+C) and (C<A+B):
    print('Perimetro = %.1f' %(A+B+C))
else:
    print('Area = %.1f' %(((A+B)*C)/2))
