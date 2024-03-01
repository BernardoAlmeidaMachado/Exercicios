try:
    idade = float(input("Digite sua idade: "))
    e_brasileiro = input("Você é brasileiro? (s/n) ").lower()
    if e_brasileiro in ["s", "si", "sim"]:
        if idade >= 18:
            print("Você pode votar.")
        else:
            print("Você não pode votar.")
    elif e_brasileiro in ["n", "na", "nã", "nao", "não"]:
        print("Você não pode votar.")
    else:
        print("A resposta deve ser 'sim' ou 'não'.")
except ValueError:
    print("O valor fornecido deve ser um número.")