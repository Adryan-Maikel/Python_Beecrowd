"""Maria acabou de iniciar seu curso de graduação na faculdade de medicina
e precisa de sua ajuda para organizar os experimentos de um laboratório o
qual ela é responsável. Ela quer saber no final do ano, quantas cobaias 
foram utilizadas no laboratório e o percentual de cada tipo de cobaia
utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos
e coelhos. Para obter estas informações, ela sabe exatamente o número de
experimentos que foram realizados, o tipo de cobaia utilizada e a quanti-
dade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários
casos de teste que vem a seguir. Cada caso de teste contém um inteiro 
Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utili-
zadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia
(R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia
utilizada e o percentual de cada uma em relação ao total de cobaias uti-
lizadas, sendo que o percentual deve ser apresentado com dois dígitos 
após o ponto.
"""
amount_animals = ''
for i in range(0, int(input())):
  amount, animal = [i for i in input().split()]
  amount_animals += int(amount) * animal
amount_c = amount_animals.count("C")
amount_r = amount_animals.count("R")
amount_s = amount_animals.count("S")
amount_animals = len(amount_animals)
print(
  f'Total: {amount_animals} cobaias\n'
  f'Total de coelhos: {amount_c}\n'
  f'Total de ratos: {amount_r}\n'
  f'Total de sapos: {amount_s}\n'
  f'Percentual de coelhos: {(amount_c / amount_animals) * 100:.2f} %\n'
  f'Percentual de ratos: {(amount_r / amount_animals) * 100:.2f} %\n'
  f'Percentual de sapos: {(amount_s / amount_animals) * 100:.2f} %'
)
