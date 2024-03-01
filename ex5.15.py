numero = 0
numeros = []
numero_referencia = 0
posicao = -1
contador = 1

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

while True:
    try:
        numero_referencia = float(input("Digite um número de referência: "))
        break
    except ValueError:
        print("O valor fornecido deve ser do tipo int ou float.")

for num in range(0, len(numeros)):
    if numeros[num] > numero_referencia:
        posicao = num
        break

if posicao == -1:
    print("Não existe nenhum elemento maior que o número de referência na lista fornecida.")
else:
    print(f"Posição: {posicao}")