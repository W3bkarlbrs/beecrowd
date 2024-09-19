cod = int(input())
qnt = int(input())

if cod == 1:
    cod_preco = float(4.00)
elif cod == 2:
    cod_preco = float(4.50)
elif cod == 3:
    cod_preco = float(5.00)
elif cod == 4:
    cod_preco = float(2.00)
elif cod == 5:
    cod_preco = float(1.50)

total = cod_preco * qnt

print("Total: R$ {:.2f}".format(total))
