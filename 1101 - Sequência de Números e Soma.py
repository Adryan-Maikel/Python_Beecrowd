"""Leia um conjunto não determinado de pares de valores M e N
(parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior 
e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores
M e N. A última linha de entrada vai conter um número nulo ou
negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o
maior e a soma deles, conforme exemplo abaixo.

Exemplo de Saída
2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""

def calculate_sequence(x, y):
  sum = 0
  x, y = [y, x] if x > y else [x, y]
  for i in range(x, y + 1):
    sum += i
    print(i , end=' ')
  print(f'Sum={sum}')


while True:
  x, y = [int(i) for i in input().split(' ')]
  if x <= 0 or y <= 0:
    break
  else:
    calculate_sequence(x, y)
