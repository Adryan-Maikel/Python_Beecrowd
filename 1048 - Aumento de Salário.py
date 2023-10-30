# -*- coding: utf-8 -*-

def calculate_new_salary(
  salary,
  REAJUSTS = (0.15, 0.12, 0.10, 0.07, 0.04),
  new_salary = 0,
  ajust = 0
  ):
  if 0 <= salary <= 400.00:
    i = 0
  elif 400.01 <= salary <= 800.00:
    i = 1
  elif 800.01 <= salary <= 1200.00:
    i = 2
  elif 1200.01 <= salary <= 2000.00:
    i = 3
  elif salary > 2000.00:
    i = 4
  ajust = salary * REAJUSTS[i]
  new_salary = salary + ajust
  return print(
    f"Novo salario: {new_salary:.2f}\n"
    f"Reajuste ganho: {ajust:.2f}\n"
    f"Em percentual: {REAJUSTS[i]*100:.0f} %"
  )


calculate_new_salary(salary=float(input()))
