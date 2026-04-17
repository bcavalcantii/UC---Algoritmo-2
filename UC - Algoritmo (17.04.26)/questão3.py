soma = 0.0
while True:
    preço = float(input("Digite o valor:"))
    if preço == 0:
        break
    soma += preço
print("Valor total:", soma)