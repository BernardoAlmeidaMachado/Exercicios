numero = 0
numeros = []
quadrados = []
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    numero = input(f"Número {contador}: ")

    if numero.lower() == "":
        break
    else:
        try:
            numero = float(numero)
        except ValueError:
            print("O número deve ser um valor int ou float.")
            continue

        contador += 1
        numeros.append(numero)

quadrados = list(map(lambda x:x**2, numeros))
print(f"Lista original: {numeros}")
print(f"Nova lista: {quadrados}")