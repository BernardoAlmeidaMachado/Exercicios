nome = ""
nomes = []
nota = 0
notas = []
lista_decrescente = []
lista_decrescente_correta = []
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    nome = input(f"(Lista de nomes) Nome {contador}: ")

    if nome.lower() == "":
        break
    else:
        contador += 1
        nomes.append(nome)

contador = 1

while True:
    nota = input(f"(Lista de notas) Nota {contador}: ")

    if nota.lower() == "":
        break
    else:
        try:
            nota = float(nota)
            contador += 1
            notas.append(nota)
        except ValueError:
            print("O valor fornecido deve ser do tipo int ou float.")

if len(nomes) != len(notas):
    if len(nomes) > len(notas):
        print("Existem mais itens na lista de nomes do que na lista de notas.")
    else:
        print("Existem mais itens na lista de notas do que na lista de nomes.")
else:
    lista_decrescente = list(zip(notas, nomes))
    lista_decrescente.sort(reverse=True)

    for num in range(0, len(lista_decrescente)):
        tupla = (lista_decrescente[num][1], lista_decrescente[num][0])
        lista_decrescente_correta.append(tupla)

    print(f"Lista de nomes: {nomes}")
    print(f"Lista de notas: {notas}")
    print(f"Lista decrescente: {lista_decrescente_correta}")