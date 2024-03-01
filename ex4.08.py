import nltk

print("Digite uma frase com 5 palavras: ")
while True:
    frase = input("Frase: ")
    palavras = nltk.word_tokenize(frase)
    quantidade_de_palavras = len(palavras)
    if quantidade_de_palavras != 5:
        print("A frase deve ter 5 palavras.")
        continue
    else:
        break

for palavra in palavras:
    print(palavra)