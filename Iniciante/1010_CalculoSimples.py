codigo_peca1,numero_de_peca1, valor_und_peca1 = input().split()
codigo_peca2,numero_de_peca2, valor_und_peca2 = input().split()
numero_de_peca1 = int(numero_de_peca1)
valor_und_peca1 = float(valor_und_peca1)
numero_de_peca2 = int(numero_de_peca2)
valor_und_peca2 = float(valor_und_peca2)
total = (numero_de_peca1*valor_und_peca1) + (numero_de_peca2 * valor_und_peca2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
