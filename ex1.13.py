try:
    print("Digite as dimensões de um retângulo: ")
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))
    area = largura * altura
    perimetro = (largura * 2) + (altura * 2)
    print(f"A área desse reângulo é {area}, e o perímetro é {perimetro}.")
except ValueError:
    print("O valor fornecido deve ser um número.")