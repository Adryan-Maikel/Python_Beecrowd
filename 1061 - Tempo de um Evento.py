"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser
no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedri-
nho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando
inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá
ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um es-
paço e o dia do mês no qual o evento vai começar. Na linha seguinte, será in-
formado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na 
terceira e quarta linha de entrada haverá outra informação no mesmo formato das
duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima
de 1 minuto.
"""
from datetime import datetime

year, month = 2023, 4
day = int(input().split(' ')[1]) # entrada -> Dia 5
hour, minute, second = [int(i) for i in input().split(' : ')]# 08 : 12 : 23
day_end = int(input().split(' ')[1]) # entrada -> Dia 9        ||   ||   ||
hour_end, minute_end, second_end = [int(i) for i in input().split(' : ')]

start_date = datetime(year,  month, day, hour, minute, second)
end_date = datetime(year, month, day_end, hour_end, minute_end, second_end)
diference = end_date - start_date
diference_hour = str(diference).split(", ")[1].split(":")[0]
diference_minute = str(diference).split(", ")[1].split(":")[1]
diference_second = str(diference).split(", ")[1].split(":")[2]
print(
  f'{diference.days} dia(s)\n'
  f'{diference_hour} hora(s)\n'
  f'{diference_minute} minuto(s)\n'
  f'{diference_second} segundo(s)'
)
