# -*- coding: utf-8 -*-
if input() == 'vertebrado':
  if input() == 'ave':
    print('aguia') if input() == 'carnivoro' else print('pomba')
  else:
    print('homem') if input() == 'onivoro' else print('vaca')
else:
  if input() == 'inseto':
    print('pulga') if input() == 'hematofago' else print('lagarta')
  else:
    print('sanguessuga') if input() == 'hematofago' else print('minhoca')
