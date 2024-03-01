try:
    # S = So + Vot + at^2*1/2
    # Vo = (S - So - at^2*1/2)/t
    # V^2 = Vo^2 + 2a(S - So)
    # V = (Vo^2 + 2a(S - So))**0.5
    print("Digite a distância percorrida, o tempo gasto e a aceleração de um objeto: ")
    distancia = float(input("Distância: "))
    tempo = float(input("Tempo: "))
    aceleracao = float(input("Aceleração: "))
    velocidade_inicial = (distancia - aceleracao*(tempo**2)/2)/tempo
    velocidade_final = ((velocidade_inicial**2) + (2*aceleracao) * (distancia))**0.5
    print(f"A velocidade inicial desse objeto é igual a {velocidade_inicial}.")
    print(f"A velocidade final desse objeto é igual a {velocidade_final}.")
except ValueError:
    print("O valor fornecido deve ser um número.")