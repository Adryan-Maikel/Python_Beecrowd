"""Leia uma quantidade indeterminada de duplas de valores inteiros X
e Y. Escreva para cada X e Y uma mensagem que indique se estes valo-
res foram digitados em ordem crescente ou decrescente.

Entrada
A entrada contém vários casos de teste. Cada caso contém dois valores
inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores
iguais para X e Y.

Saída
Para cada caso de teste imprima “Crescente”, caso os valores tenham
sido digitados na ordem crescente, caso contrário imprima a mensagem
“Decrescente”."""


while True:
  x, y = [int(i) for i in input().split(' ')]
  if x < y:
    numbers_is = 'Crescente'
  elif x > y:
    numbers_is = 'Decrescente'
  else:
    break
  print(numbers_is)
