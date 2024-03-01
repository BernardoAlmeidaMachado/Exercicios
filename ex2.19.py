try:
    tem_impar = False
    print("Digite 5 números inteiros: ")
    numero_1 = int(input("Número 1: "))
    numero_2 = int(input("Número 2: "))
    numero_3 = int(input("Número 3: "))
    numero_4 = int(input("Número 4: "))
    numero_5 = int(input("Número 5: "))
    numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    for numero in numeros:
        if not (numero % 2 == 0):
            tem_impar = True
    if tem_impar:
        print("Há pelo menos um número ímpar.")
    else:
        print("Todos os números digitados são pares.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")
