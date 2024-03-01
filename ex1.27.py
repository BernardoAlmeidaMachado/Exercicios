try:
    print("Digite seu nome, seu salário e o valor do imposto: ")
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    imposto_porcentagem = float(input("Imposto (%): "))
    salario_liquido = salario - (salario * imposto_porcentagem/100)
    print(f"Nome: {nome}")
    print(f"Salário Líquido: R${salario_liquido}")
except ValueError:
    print("O valor fornecido deve ser um número.")