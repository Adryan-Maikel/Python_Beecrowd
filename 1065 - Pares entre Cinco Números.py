"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores
digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de
valores pares lidos.
"""
even_numbers = []
for i in range(5):
  number = int(input())
  even_numbers.append(number) if number % 2 == 0 else 0
print(f'{len(even_numbers)} valores pares')
