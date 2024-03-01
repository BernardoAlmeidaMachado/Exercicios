import nltk

frase = input("Digite uma frase: ")
palavras = nltk.word_tokenize(frase)
frase_sem_espaco = ""
palavras_sem_espaco = []

for palavra in palavras:
    palavras_sem_espaco.append(palavra.strip())

for num in range(0, len(palavras_sem_espaco)):
    if num != len(palavras_sem_espaco) - 1:
        frase_sem_espaco += palavras_sem_espaco[num] + " "
    else:
        frase_sem_espaco += palavras_sem_espaco[num]
        break

print(f"Frase sem espaços desnecessários: {frase_sem_espaco}")