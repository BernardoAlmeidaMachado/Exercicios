numero = 0
numeros = []
elementos_de_indice_par = []
contador = 1
contador_indices = 0

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    numero = input(f"Número {contador}: ")

    if numero.lower() == "":
        break
    else:
        try:
            numero = float(numero)
            contador += 1
            numeros.append(numero)
        except ValueError:
            print("O valor fornecido deve ser do tipo int ou float.")

for num in range(0, len(numeros)):
    if num % 2 == 0:
        elementos_de_indice_par.append(numeros[num])

elementos_de_indice_par = elementos_de_indice_par[::-1]
numeros_elementos_invertidos = numeros.copy()

for num in range(0, len(numeros)):
    if num % 2 == 0:
        numeros_elementos_invertidos[num] = elementos_de_indice_par[contador_indices]
        contador_indices += 1

print(f"Lista original: {numeros}")
print(f"Lista nova: {numeros_elementos_invertidos}")