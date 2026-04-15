def calcular():
    try:
        preco1=float(input("Digite o valor"))
        preco2=float(input("Digite o valor"))

        total= preco1 + preco2

        print(f"o total é:{total}")
    
    except ValueError:
        print("digite somente numeros")

        calcular()
