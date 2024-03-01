import math

try:
    print("Digite o raio de um círculo: ")
    raio = float(input("Raio: "))
    perimetro = 2*math.pi*raio
    print(f"O perímetro desse círculo é {perimetro}.")
except ValueError:
    print("O valor fornecido deve ser um número.")