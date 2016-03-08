# -*- coding: utf-8 -*-
age = int(input())
print('%d ano(s)' %(age/365))
print('%d mes(es)' %((age%365)/30))
print('%d dia(s)' %((age%365)%30))
