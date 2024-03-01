try:
    print("Digite o seu peso e altura: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso/(altura * altura)
    print(f"O seu IMC é {imc}.")
except ValueError:
    print("O valor fornecido deve ser um número.")