try:
    numero = float(input("Digite um número: "))
    raiz_quadrada = numero**0.5
    print(f"A raíz quadrada de {numero} é {raiz_quadrada}.")
except ValueError:
    print("O valor fornecido deve ser um número.")