# -*- coding: utf-8 -*-
start_hour, end_hour= [int(i) for i in input().split()]
duration = 0
if start_hour == end_hour:
  duration = 24
elif start_hour > end_hour:
  while start_hour != end_hour:
    duration = duration + 1
    start_hour = start_hour + 1
    if start_hour == 24:
      start_hour = 0
else:
  duration = end_hour - start_hour
print(f'O JOGO DUROU {duration} HORA(S)')