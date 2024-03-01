try:
    # S = So + Vot + at^2*1/2
    # xt^2 + yt + z = 0
    # xt^2 = at^2*1/2
    # x = a*1/2
    # yt = vot
    # y = vo
    # z = So - S
    print("Digite a distância (até o solo) e a velocidade inicial de um objeto em queda livre: ")
    distancia = float(input("Distância (m): "))
    velocidade_inicial = float(input("Velocidade inicial (m/s): "))
    s = distancia
    vo = velocidade_inicial
    a = 9.8
    x = a*1/2
    y = vo
    z = 0 - s
    tempo = (-y + (y**2 - 4*x*z)**0.5)/(2*x)
    print(f"Considerando a aceleração da gravidade como 9.8 m/s^2, e desconsiderando a resistência do ar, esse objeto leva {tempo} segundo(s) para atingir o solo")
except ValueError:
    print("O valor fornecido deve ser um número.")