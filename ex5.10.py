palavra = 0
palavras = []
comprimentos = []
contador = 1

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    palavra = input(f"Nome {contador}: ")

    if palavra.lower() == "":
        break
    elif " " in palavra:
        print("A palavra não pode conter espaços.")
        continue
    else:
        contador += 1
        palavras.append(palavra)

comprimentos = list(map(lambda x:len(x), palavras))
print(f"Lista original: {palavras}")
print(f"Nova lista: {comprimentos}")