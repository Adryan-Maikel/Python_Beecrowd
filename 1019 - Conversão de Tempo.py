from math import trunc
seconds = int(input())
hours = trunc(seconds / 3600)
seconds = seconds % 3600
minutes = trunc(seconds / 60)
seconds = seconds % 60
print("{}:{}:{}".format(hours, minutes, seconds))
