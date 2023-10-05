id_piece_one, number_piece_one, value_piece_one = input().split(" ")
id_piece_two, number_piece_two, value_piece_two = input().split(" ")
total = (float(number_piece_one) * float(value_piece_one)) + (float(number_piece_two) * float(value_piece_two))
print("VALOR A PAGAR: R$ {:.2f}".format(total))
