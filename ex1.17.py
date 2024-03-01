try:
    print("Digite o preço de uma mercadoria, o desconto e o imposto: ")
    preco_inicial = float(input("Preço: "))
    desconto = float(input("Desconto (%): "))
    imposto = int(input("Imposto (%): "))
    preco_final = preco_inicial - (preco_inicial * (desconto / 100))
    preco_final = preco_final + (preco_final * imposto/100)
    print(f"O preço final da mercadoria é {preco_final}.")
except ValueError:
    print("O valor fornecido deve ser um número.")