try:
    n = int(input("n: "))
    for x in range(1, n + 1):
        fatorial = 1
        for y in range(1, x + 1):
            fatorial *= y
        print(f"{x}! = {fatorial}")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")