string = input("Digite uma string: ")
e_inteiro = True
contagem_de_pontos = 0
for n in range(0, len(string)):
    if (n == 0) and string[n] == "-" and len(string) > 1:
        continue
    elif string[n] in "0123456789.":
        pass
    else:
        print(f"{string} não é um número.")
        e_inteiro = False
        break
if e_inteiro:
    for caractere in string:
        if caractere == ".":
            contagem_de_pontos += 1
    if contagem_de_pontos != 1:
        print(f"{string} não é um número real.")
    else:
        print(f"{string} é um número real.")
