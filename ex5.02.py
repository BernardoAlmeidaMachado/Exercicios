frase = input("Digite uma frase: ").lower()
frase_splited_a = [word for word in frase.split() if "a" in word]
frase_splited_o = [word.replace("a", "o") for word in frase_splited_a]
print(frase_splited_o)