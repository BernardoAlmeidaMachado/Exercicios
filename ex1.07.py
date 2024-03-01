try:
    print("Digite o nome, preço de custo, preço de venda e a quantidade em estoque de determinado produto: ")
    nome_do_produto = input("Nome do produto: ")
    preco_de_custo = float(input("Preço de custo: "))
    preco_de_venda = float(input("Preço de venda: "))
    quantidade_em_estoque = float(input("Quantidade em estoque: "))
    gasto = preco_de_custo * quantidade_em_estoque
    faturamento = preco_de_venda * quantidade_em_estoque
    lucro = faturamento - gasto
    print(f"O lucro que o estoque de {nome_do_produto} pode gerar se todos os produtos forem vendidos é {lucro}.")
except ValueError:
    print("O valor fornecido deve ser um número.")

