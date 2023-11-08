"""Você deve fazer um programa que apresente a sequencia conforme o
exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""
from math import ceil

count, i, j = 0, 0, -1
while i <= 2:
  j += 1
  count += 1
  if f'{i:.1f}'.split('.')[1] == '0':
    if count == 1:
      j += 1
    print(f'I={ceil(i)} J={ceil(j)}')
  else:
    print(f'I={i:.1f} J={j}.{(str(round(i, 1)).split(".")[1])[0]}')
  if count == 3:
    count = 0
    i += 0.2
    j -= 3
 