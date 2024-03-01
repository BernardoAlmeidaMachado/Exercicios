numero = 0
lista1 = []
lista2 = []
media = 0
medias = []
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    numero = input(f"(Lista 1) Número {contador}: ")

    if numero.lower() == "":
        break
    else:
        try:
            numero = float(numero)
            contador += 1
            lista1.append(numero)
        except ValueError:
            print("O número deve ser um valor int ou float.")

contador = 1

while True:
    numero = input(f"(Lista 2) Número {contador}: ")

    if numero.lower() == "":
        break
    else:
        try:
            numero = float(numero)
            contador += 1
            lista2.append(numero)
        except ValueError:
            print("O número deve ser um valor int ou float.")

if len(lista1) != len(lista2):
    if len(lista1) > len(lista2):
        print("Existem mais itens na lista 1 do que na lista 2.")
    else:
        print("Existem mais itens na lista 2 do que na lista 1.")
else:
    for num1, num2 in zip(lista1, lista2):
        media = (num1 + num2) / 2
        medias.append(media)

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Médias: {medias}")