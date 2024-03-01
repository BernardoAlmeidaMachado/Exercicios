import nltk

frase = input("Digite uma frase: ")
palavras = nltk.word_tokenize(frase)

for palavra in palavras:
    posicao = frase.find(palavra)
    print(f"{palavra}: {posicao}")
