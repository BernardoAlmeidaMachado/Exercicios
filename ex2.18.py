try:
    idade = float(input("Digite sua idade: "))
    if idade < 30:
        print("Você é jovem.")
    elif idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")
except ValueError:
    print("O valor fornecido deve ser um número.")