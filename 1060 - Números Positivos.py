"""Faça um programa que leia 6 valores. Estes valores serão somente negativos
ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de
valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos."""
numbers_positive = []
for i in range(6):
  number = float(input())
  numbers_positive.append(number) if number >= 0 else 0
# print(numbers)
print(f'{len(numbers_positive)} valores positivos')
