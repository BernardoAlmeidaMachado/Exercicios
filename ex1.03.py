try:
    print("Digite três números: ")
    numero_1 = float(input("Número 1: "))
    numero_2 = float(input("Número 2: "))
    numero_3 = float(input("Número 3: "))
    media_aritmetica = (numero_1 + numero_2 + numero_3) / 3
    print(f"A média aritmética dos três números digitados é {media_aritmetica}.")
except ValueError:
    print("O valor fornecido deve ser um número.")