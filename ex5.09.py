nome = 0
nomes = []
nomes_caixa_alta = []
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    nome = input(f"Nome {contador}: ")

    if nome.lower() == "":
        break
    else:
        contador += 1
        nomes.append(nome)

nomes_caixa_alta = list(map(lambda x:x.upper(), nomes))
print(f"Lista original: {nomes}")
print(f"Nova lista: {nomes_caixa_alta}")