def calcular ():
    try:
        peso = float(input("Digite o seu peso:"))
        altura = float(input("Digite a sua altura:"))
        imc = peso / (altura ** 2)
        print("Seu imc é:", imc)

    except ValueError:
        print("Digite somente números")

calcular ()
