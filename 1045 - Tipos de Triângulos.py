# -*- coding: utf-8 -*-
from math import pow

a, b, c = sorted([float(i) for i in input().split()], reverse=True)
a2, b2, c2 = pow(a, 2), pow(b, 2), pow(c, 2)

if a >= b + c:
  print('NAO FORMA TRIANGULO')
else:
  if a2 == b2 + c2:
    print('TRIANGULO RETANGULO')
  if a2 > b2 + c2:
    print('TRIANGULO OBTUSANGULO')
  if a2 < b2 + c2:
    print('TRIANGULO ACUTANGULO')
  if a == b == c:
    print('TRIANGULO EQUILATERO')
  if a == b and a != c or a == c and a != b or b == c and b != a:
    print('TRIANGULO ISOSCELES')
