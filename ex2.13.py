try:
    idade = float(input("Digite sua idade: "))
    genero = input("Você é homem ou mulher? (h/m) ")
    if genero in ["h", "ho", "hom", "home", "homem"]:
        if idade >= 65:
            print("Você é elegível para aposentadoria.")
        else:
            print("Você não é elegível para aposentadoria.")
    elif genero in ["m", "mu", "mul", "mulh", "mulhe", "mulher"]:
        if idade >= 60:
            print("Você é elegível para aposentadoria.")
        else:
            print("Você não é elegível para aposentadoria.")
    else:
        print("A resposta deve ser 'homem' ou 'mulher'.")
except ValueError:
    print("O valor fornecido deve ser um número.")