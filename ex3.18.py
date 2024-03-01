try:
    n = int(input("n: "))
    x = -1
    y = 1
    z = 0
    for num in range(0, n):
        z = x + y
        x = y
        y = z
        print(z)
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")