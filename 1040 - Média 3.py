note1, note2, note3, note4 = [float(i) for i in input().split()]
average = (note1 * 2 + note2 * 3 + note3 * 4 + note4 * 1) / 10
print("Media: {:.1f}".format(average))
