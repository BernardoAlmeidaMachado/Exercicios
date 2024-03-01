numeros = []
print("Digite 10 números: ")
try:
    for num in range(1,11):
        numero = int(input(f"Número {num}: "))
        numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    while maior in numeros:
        numeros.remove(maior)
        if len(numeros) != 0:
            segundo_maior = max(numeros)
    while menor in numeros:
        numeros.remove(menor)
        if len(numeros) != 0:
            segundo_menor = min(numeros)
    print(f"O segundo maior número digitado foi {segundo_maior}.")
    print(f"O segundo menor número digitado foi {segundo_menor}.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")

