values = input().split(" ")
a, b, c = [int(i) for i in values]
bigger_ab = (a + b + abs(a - b)) / 2
bigger = (bigger_ab + c + abs(bigger_ab - c)) / 2
print("{} eh o maior".format(int(bigger)))
