numeros = []
print("Digite 10 números: ")
try:
    for num in range(1,11):
        numero = int(input(f"Número {num}: "))
        numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior número digitado foi {maior}.")
    print(f"O menor número digitado foi {menor}.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")