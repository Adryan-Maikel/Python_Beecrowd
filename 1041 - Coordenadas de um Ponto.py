x, y = [float(i) for i in input().split()]


def check_coord(x, y):
  if x == y == 0:
    return print("Origem")
  elif x == 0 and y != 0:
    return print("Eixo Y")
  elif x != 0 and y == 0:
    return print("Eixo X")
  elif x > 0 and y > 0:
    return print("Q1")
  elif x < 0 and y > 0:
    return print("Q2")
  elif x < 0 and y < 0:
    return print("Q3")
  else:
    return print("Q4")


check_coord(x, y)
