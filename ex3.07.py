numero = 0
soma = 0
media = 0
numeros = []

try: 
    while True:
            numero = float(input("Digite um número: "))
            if numero < 0:
                break
            else:
                numeros.append(numero)
    for num in numeros:
        soma += num

    media = soma / len(numeros)

    print(f"Média: {media}")
except ValueError:
        print("O valor fornecido deve ser um número.")