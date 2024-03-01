try:
    print("Digite a velocidade inicial, a velocidade final e o tempo de transição de uma para outra: ")
    velocidade_inicial = float(input("Velocidade inicial (m/s): "))
    velocidade_final = float(input("Velocidade final (m/s): "))
    tempo = float(input("Tempo (s): "))
    aceleracao = (velocidade_final - velocidade_inicial) / tempo
    print(f"Aceleração: {aceleracao} m/s^2.")
except ValueError:
    print("O valor fornecido deve ser um número.")