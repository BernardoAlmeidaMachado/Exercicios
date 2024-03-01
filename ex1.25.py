import math

try:
    print("Digite o raio de uma esfera: ")
    raio = float(input("Raio: "))
    volume = (4*math.pi*(raio**3))*1/3
    print(f"O volume dessa esfera é {volume}.")
except ValueError:
    print("O valor fornecido deve ser um número.")