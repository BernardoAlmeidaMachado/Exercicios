try:
    numero = float(input("Digite um número: "))
    dobro = numero * 2
    print(f"O dobro do número digitado é {dobro}.")
except ValueError:
    print("O valor fornecido deve ser um número.")