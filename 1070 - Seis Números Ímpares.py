"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares
consecutivos a partir de X, um valor por linha, inclusive o X ser
for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
"""
number = int(input())
number += 1 if number % 2 == 0 else 0
print(number)
for i in range(5):
  number += 2
  print(number)
