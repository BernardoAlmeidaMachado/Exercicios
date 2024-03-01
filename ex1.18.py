try:
    print("Digite a massa e a aceleração de um objeto: ")
    massa = float(input("Massa (kg): "))
    aceleracao = float(input("Aceleração (m/s^2): "))
    forca_resultante = massa * aceleracao
    print(f"Força resultante: {forca_resultante}.")
except ValueError:
    print("O valor fornecido deve ser um número.")