"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a
posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo
abaixo.
"""
# -*- coding: utf-8 -*-

numbers = []
for i in range(100):
  numbers.append(int(input()))
number_max = max(numbers)
print(
  f'{number_max}\n{numbers.index(number_max) + 1}'
)
