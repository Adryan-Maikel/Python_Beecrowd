from math import trunc
amount_total = int(input())
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
notes_1 = trunc(amount / 1)
print(
  "{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00"
  .format(amount_total, notes_100, notes_50, notes_20, notes_10, notes_5, notes_2, notes_1)
  )
