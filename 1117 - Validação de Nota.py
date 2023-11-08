"""Faça um programa que leia as notas referentes às duas avaliações
de um aluno. Calcule e imprima a média semestral. Faça com que o 
algoritmo só aceite notas válidas (uma nota válida deve pertencer
ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O
programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota 
invalida". Quando duas notas válidas forem lidas, deve ser impressa
a mensagem "media = " seguido do valor do cálculo. O valor deve ser
apresentado com duas casas após o ponto decimal.
"""
sum_notes = 0
for i in range(2):
  while True:
    i = float(input())
    if 0 <= i <= 10:
      sum_notes += i
      break
    else:
      print('nota invalida')
print(f'media = {(sum_notes / 2):.2f}')
