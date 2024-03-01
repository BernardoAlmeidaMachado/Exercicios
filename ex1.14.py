try:
    print("Digite a base e a altura de um triângulo: ")
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = (base*altura)/2
    print(f"A área desse triângulo é {area}.")
except ValueError:
    print("O valor fornecido deve ser um número.")