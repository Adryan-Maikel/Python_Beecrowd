id, quantity = [int(i) for i in input().split()]
prices = [4.00, 4.50, 5.00, 2.00, 1.50]
print("Total: R$ {:.2f}".format(quantity * prices[id-1]))
