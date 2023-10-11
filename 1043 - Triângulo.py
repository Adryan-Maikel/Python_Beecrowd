a, b, c = [float(i) for i in input().split()]
print(f"Perimetro = {a + b + c:.1f}" if a < b + c and b < c + a and c < b + a else f"Area = {((a + b) * c) / 2:.1f}")
