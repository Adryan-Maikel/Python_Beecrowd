from math import trunc
age_in_days = int(input())
years = trunc(age_in_days / 365)
age_in_days = age_in_days % 365
months = trunc(age_in_days / 30)
age_in_days = age_in_days % 30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, age_in_days))
