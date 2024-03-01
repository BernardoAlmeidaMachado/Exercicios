try:
    print("Digite três números: ")
    numero_1 = float(input("Número 1: "))
    numero_2 = float(input("Número 2: "))
    numero_3 = float(input("Número 3: "))
    soma = (numero_1 + numero_2 + numero_3)
    print(f"A soma dos três números digitados é {soma}.")
except ValueError:
    print("O valor fornecido deve ser um número.")