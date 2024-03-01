import nltk

frase = input("Digite uma frase: ")
palavras = nltk.word_tokenize(frase)

for palavra in palavras:
    num_ocorrencias = frase.count(palavra)
    print(f"{palavra}: {num_ocorrencias}")
