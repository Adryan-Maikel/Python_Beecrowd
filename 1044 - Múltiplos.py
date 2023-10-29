# -*- coding: utf-8 -*-
a, b = [int(i) for i in input().split()]
if a > b and a % b == 0 or b > a and b % a == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
