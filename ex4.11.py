frase = input("Digite uma frase: ")
substring = ""
for num in range(0, len(frase)):
    substring += frase[num]
    if len(substring) == 6:
        print(substring)
        substring = ""
print(substring)