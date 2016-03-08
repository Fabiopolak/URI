# -*- coding: utf-8 -*-
value = input().split(" ")
a, b, c = value
a = int(a)
b = int(b)
c = int(c)
largerAB = (a + b + abs(a-b))/2
print("%d eh o maior" %((largerAB + c + abs(largerAB-c))/2))
