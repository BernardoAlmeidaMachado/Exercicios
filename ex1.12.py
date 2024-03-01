import math

try:
    raio = float(input("Digite o raio de um círculo: "))
    area = (math.pi)*(raio**2)
    comprimento = 2*(math.pi)*(raio)
    print(f"A área do círculo cujo raio é {raio} é {area}.")
    print(f"O comprimento do círculo cujo raio é {raio} é {comprimento}.")    
except ValueError:
    print("O valor fornecido deve ser um número.")