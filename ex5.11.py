numero = 0
numeros = []
numeros_pares = []
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
            print("A nota deve ser um valor int ou float.")
            continue

        contador += 1
        numeros.append(numero)

numeros_pares = list(filter(lambda x:x % 2 == 0, numeros))
print(f"Lista original: {numeros}")
print(f"Nova lista: {numeros_pares}")