chave = 0
chaves = []
valor = 0
valores = []
chaves_e_valores = {}
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    chave = input(f"Chave {contador}: ")

    if chave.lower() == "":
        break
    else:
        contador += 1
        chaves.append(chave)

contador = 1

while True:
    valor = input(f"Valor {contador}: ")

    if valor.lower() == "":
        break
    else:
        contador += 1
        valores.append(valor)

if len(chaves) != len(valores):
    if len(chaves) > len(valores):
        print("Existem mais chaves do que valores.")
    else:
        print("Existem mais valores do que chaves.")
else:
    for key, value in zip(chaves, valores):
        chaves_e_valores[key] = value
    print(f"Dicionário: {chaves_e_valores}")