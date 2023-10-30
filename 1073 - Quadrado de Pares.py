"""
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores
pares, de 1 até N, inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme
o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída
1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso,
configure a precisão adequadamente para que isso não ocorra.
"""
for i in range(2, int(input()) + 1, 2):
  print(f'{i}^2 = {i ** 2}')