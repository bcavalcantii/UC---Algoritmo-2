import random

tentativas = 0
acertou = False
x = random.randint(1, 100) 

while not acertou:
    numero = int(input("digite um número entre 1 e 100: "))
    tentativas += 1

    if numero == x:
        print("acertou!!!")
        acertou = True
   
    elif numero < x:
        print("número muito alto! Tente novamente")
    else:
        print("número muito baixo! Tente novamente")

print(f"Você precisou de {tentativas} tentativas para acertar!")