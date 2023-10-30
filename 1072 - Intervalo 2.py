"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X
que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos
estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica
o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores
estão fora (out) do intervalo.
"""
# -*- coding: utf-8 -*-

in_out = []
number = int(input())
for i in range(number):
  in_out.append(True) if 10 <= int(input()) <= 20 else in_out.append(False)
print(f'{in_out.count(True)} in\n{in_out.count(False)} out')
