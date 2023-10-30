# -*- coding: utf-8 -*-

def check_ddd(input):
  DDDS = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
    # 51: 'Porto Alegre'
  }
  
  for ddd in DDDS:
    if input == ddd:
      return print(DDDS[ddd])
  return print('DDD nao cadastrado')


check_ddd(int(input()))
