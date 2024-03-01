try:
    idade = float(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você não é maior de idade.")
except ValueError:
    print("O valor fornecido deve ser um número.")