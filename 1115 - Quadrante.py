"""Escreva um programa para ler as coordenadas (X,Y) de uma quantida-
de indeterminada de pontos no sistema cartesiano. Para cada ponto es-
crever o quadrante a que ele pertence. O algoritmo será encerrado 
quando pelo menos uma de duas coordenadas for NULA (nesta situação 
sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2
valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema carte-
siano se encontra a coordenada lida, conforme o exemplo."""


while True:
  x, y = [int(i) for i in input().split(' ')]
  if x == 0 or y == 0:
    break
  else:
    if x > 0 and y > 0: 
      print('primeiro')
    if x > 0 and y < 0: 
      print('quarto')
    if x < 0 and y > 0: 
      print('segundo')
    if x < 0 and y < 0: 
      print('terceiro')
