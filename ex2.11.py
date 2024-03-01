try:
    temperatura = float(input("Digite uma temperatura em graus Celsius: "))
    if temperatura < 36:
        print("A temperatura fornecida está abaixo da faixa normal.")
    elif temperatura > 37:
        print("A temperatura fornecida está acima da faixa normal.")
    else:
        print("A temperatura fornecida está dentro da faixa normal.")
except ValueError:
    print("O valor fornecido deve ser um número.")