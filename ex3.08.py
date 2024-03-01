fatorial = 1

try:
    numero = int(input("Digite um número inteiro: "))
    for numero in range (1, numero + 1):
        fatorial *= numero
    print(f"Fatorial: {fatorial}")
except ValueError:
        print("O valor fornecido deve ser um número inteiro.")