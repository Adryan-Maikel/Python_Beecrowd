"""Leia um valor inteiro N que é a quantidade de casos de teste que
vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. 
  Você deve apresentar a soma de todos os ímpares existentes entre 
X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de 
casos de teste que vem a seguir. Cada caso de teste consiste em 
uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y."""

def calculate_odd_consecutive(repeat):
  for i in range(repeat):
    odd = []
    x, y = [int(input) for input in input().split(' ')]
    x, y = [y, x] if x > y else [x, y]
    for number  in range(x + 1, y):
      odd.append(number) if number % 2 != 0 else 0
    print(sum(odd))


calculate_odd_consecutive(int(input()))
