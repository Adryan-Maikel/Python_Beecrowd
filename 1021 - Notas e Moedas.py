from math import trunc
amount_total = float(input())
amount = amount_total
notes_100 = trunc(amount / 100)
amount = amount % 100
notes_50 = trunc(amount / 50)
amount = amount % 50
notes_20 = trunc(amount / 20)
amount = amount % 20
notes_10 = trunc(amount / 10)
amount = amount % 10
notes_5 = trunc(amount / 5)
amount = amount % 5
notes_2 = trunc(amount / 2)
amount = amount % 2
coin_1 = trunc(amount / 1)
amount = amount % 1
coin_50 = trunc(amount / .5)
amount = amount % .5
coin_25 = trunc(amount / .25)
amount = amount % .25
coin_10 = trunc(amount / .10)
amount = amount % .10
coin_05 = trunc(amount / .05)
amount = amount % .05
coin_01 = round(amount / .01)
print("""NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01"""
  .format(
    notes_100, notes_50, notes_20, notes_10, notes_5, notes_2, 
    coin_1, coin_50, coin_25, coin_10, coin_05, coin_01
  )
)
