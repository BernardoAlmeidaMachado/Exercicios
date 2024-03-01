try:
    print("Digite o comprimento de dois catetos de um triângulo retângulo: ")
    lado_a = float(input("Cateto a: "))
    lado_b = float(input("Cateto b: "))
    hipotenusa = ((lado_a**2) + (lado_b**2))**0.5
    print(f"O comprimento da hipotenusa desse triângulo é {hipotenusa}.")
except ValueError:
    print("O valor fornecido deve ser um número.")