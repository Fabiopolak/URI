value = input().split(' ')
A, B = value
A = float(A)
B = float(B)
if A%B==0 or B%A==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
