frase1 = input("Digite uma frase: ")

while True:
    palavra_presente = input("Digite uma palavra presente na frase: ")
    if palavra_presente not in frase1.split():
        print("Essa palavra não está presente na frase (verifique as letras maiúsculas).")
        continue
    else:
        break

while True:
    palavra_ausente = input("Digite uma palavra ausente na frase: ")
    if palavra_ausente in frase1.split():
        print("Essa palavra não está ausente na frase (verifique as letras maiúsculas).")
        continue
    else:
        break

frase2 = frase1.replace(palavra_presente, palavra_ausente)
print(f"Nova frase: {frase2}")