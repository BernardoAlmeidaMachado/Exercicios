artigos = ["o", "os", "a", "as", "um", "uns", "uma", "umas"]
frase1 = input("Digite uma frase: ")
frase2 = frase1.lower()

for artigo in artigos:
    if artigo in frase2.split():
        frase2 = frase2.replace(artigo, "")

print(f"Frase sem artigos: {frase2.capitalize()}")