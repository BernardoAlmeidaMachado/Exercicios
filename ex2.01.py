try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é impar.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")