from math import sqrt
a, b, c = [float(i) for i in input().split()]
if a == 0 or b == 0 or c == 0:
  print("Impossivel calcular")
else:
  delt = b ** 2 - 4 * a * c 
  if delt < 0:
    print("Impossivel calcular")
  else:
    x1 = (-b + sqrt(delt)) / (2 * a)
    x2 = (-b - sqrt(delt)) / (2 * a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(x1, x2))
