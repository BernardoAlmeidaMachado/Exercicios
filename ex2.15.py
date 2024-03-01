try:
    salario = float(input("Digite seu salário: "))
    if salario >= 10000:
        print("Alto salário.")
    else:
        print("Baixo salário.")
except ValueError:
    print("O valor fornecido deve ser um número.")