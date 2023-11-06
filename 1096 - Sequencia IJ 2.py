"""Você deve fazer um programa que apresente a sequencia conforme o 
exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
	
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""
i, j, x = 1, 7, 0
while i < 11:
  x += 1
  print(f'I={i} J={j}')
  j -= 1
  if x == 3:
    i += 2
    x, j = 0, 7
