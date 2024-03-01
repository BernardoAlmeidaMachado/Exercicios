print("Digite dois números complexos: ")
try:
    numero1 = complex(input("Número 1: "))
    numero2 = complex(input("Número 2: "))
    soma = numero1 + numero2
    produto = numero1 * numero2
    print(f"Soma: {soma}")
    print(f"Produto: {produto}")
except ValueError:
    print("O valor fornecido deve ser um número complexo (x+yj).")