"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos
valores ímpares que estão entre os valores fornecidos na entrada que
deverá caber em um inteiro.
"""
x = int(input())
y = int(input())
total = 0
for i in range(y + 1, x):
  total += i if i % 2 != 0 else 0
print(total)
