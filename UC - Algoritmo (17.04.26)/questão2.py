idade_str = input("Digite a sua idade: ")
idade = int(idade_str)
if idade >= 16:
    print("Pode votar!")
elif idade <16:
    print("Ainda não pode votar.")