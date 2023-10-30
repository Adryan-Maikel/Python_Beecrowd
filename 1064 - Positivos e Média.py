"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram
positivos. Na próxima linha, deve-se mostrar a média de todos os valores
positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha
deve mostrar a média dos valores positivos digitados.
"""
# -*- coding: utf-8 -*-
numbers_positives = []
for i in range(6):
  number = float(input())
  numbers_positives.append(number) if number > 0 else 0
print(
  f'{len(numbers_positives)} valores positivos\n'
  f'{round(sum(numbers_positives) / len(numbers_positives), 1)}'
)
