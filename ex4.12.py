import nltk

frase = input("Digite uma frase: ")
palavras = nltk.word_tokenize(frase)
o_s = 0
a_s = 0

for palavra in palavras:
    if palavra[-1].lower() == "o":
        o_s += 1
    elif palavra[-1].lower() == "a":
        a_s += 1

print(f"Palavras terminadas com 'o': {o_s}")
print(f"Palavras terminadas com 'a': {a_s}")