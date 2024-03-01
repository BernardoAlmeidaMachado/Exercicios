try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura**2)
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc <= 24.9:
        print("Você está com o peso normal.")
    elif imc <= 29.9:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")
except ValueError:
    print("O valor fornecido deve ser um número.")