import math

try:
    print("Digite o valor da medida de um ângulo em radianos: ")
    angulo_rad = float(input("Ângulo (rad): "))
    angulo_graus = math.degrees(angulo_rad)
    print(f"Ângulo (graus) {angulo_graus}.")
except ValueError:
    print("O valor fornecido deve ser um número.")