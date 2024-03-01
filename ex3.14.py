try:
    numero = int(input("Digite um número: "))
    e_primo = True
    for y in range(1, numero + 1):
        if (numero % y == 0) and y != 1 and y != numero:
            e_primo = False
    if e_primo:
        print(f"{numero} é primo.") 
    else:
        print(f"{numero} não é primo.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")