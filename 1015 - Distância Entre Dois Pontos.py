from math import sqrt
x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]
distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("{:.4f}".format(distance))
