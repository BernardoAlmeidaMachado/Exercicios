string = input("Digite uma string: ")
e_inteiro = True
for n in range(0, len(string)):
    if (n == 0) and string[n] == "-" and len(string) > 1:
        continue
    elif string[n] in "0123456789":
        pass
    else:
        print(f"{string} não é um número inteiro.")
        e_inteiro = False
        break
if e_inteiro:
    print(f"{string} é um número inteiro.")