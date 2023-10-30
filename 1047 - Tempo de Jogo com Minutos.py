# -*- coding: utf-8 -*-
start_hours, start_minutes, end_hours, end_minutes = [int(i) for i in input().split()]

def calculate_duration_game(start_hours, start_minutes, end_hours, end_minutes, duration_hours = 0, duration_minutes = 0):
  if start_hours == end_hours and start_minutes == end_minutes:
    duration_hours, duration_minutes = 24, 0
    return print(f'O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)')
  while start_minutes != end_minutes:
    duration_minutes += 1
    start_minutes += 1
    if start_minutes == 60:
      start_minutes = 0
      start_hours += 1
  while start_hours != end_hours:
    duration_hours += 1
    start_hours += 1
    if start_hours == 24:
      start_hours = 0
  return print(f'O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)')


calculate_duration_game(start_hours, start_minutes, end_hours, end_minutes)
