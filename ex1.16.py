try:
    print("Digite o valor inicial de um investimento, a taxa de juros e o número de anos: ")
    valor_inicial = float(input("Valor inicial: "))
    taxa_de_juros = float(input("Taxa de juros: "))
    numero_de_anos = int(input("Número de anos: "))
    valor_final = valor_inicial
    for ano in range(0, numero_de_anos):
        valor_final += (valor_final * (taxa_de_juros / 100))
    print(f"O valor final desse investimento, considerando juros compostos, é {valor_final}.")
except ValueError:
    print("O valor fornecido deve ser um número (o número de anos deve ser inteiro).")