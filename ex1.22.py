try:
    print("Digite a distância percorrida por um objeto e o tempo gasto: ")
    distancia = float(input("Distância: "))
    tempo = float(input("Tempo: "))
    velocidade_media = distancia/tempo
    print(f"A velocidade média desse objeto é igual a {velocidade_media}.")
except ValueError:
    print("O valor fornecido deve ser um número.")