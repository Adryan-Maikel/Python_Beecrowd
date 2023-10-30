"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados
foram pares, quantos valores digitados foram ímpares, quantos valores
digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por 
linha, não esquecendo o final de linha após cada uma.
"""
# -*- coding: utf-8 -*-

numbers = []
for i in range(5):
  number = int(input())
  numbers.append(number)

check_even = lambda number : True if number % 2 == 0 else False
check_positive = lambda number : True if number > 0 else False
check_negative = lambda number : True if number < 0 else False

print(
  f'{list(map(check_even, numbers)).count(True)} valor(es) par(es)\n'
  f'{list(map(check_even, numbers)).count(False)} valor(es) impar(es)\n'
  f'{list(map(check_positive, numbers)).count(True)} valor(es) positivo(s)\n'
  f'{list(map(check_negative, numbers)).count(True)} valor(es) negativo(s)'
)
