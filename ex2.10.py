def main():
    try:
        print("Digite três números: ")
        numero_1 = float(input("Número 1: "))
        validar_numero(numero_1)
        numero_2 = float(input("Número 2: "))
        validar_numero(numero_2)
        numero_3 = float(input("Número 3: "))
        validar_numero(numero_3)
        media = (numero_1 + numero_2 + numero_3) / 3
        if media == 10:
            print("Aprovado.")
            print("Parabéns.")
        elif media >= 6:
            print("Aprovado.")
        else:
            print("Reprovado.")
    except ValueError:
        print("O valor fornecido deve ser um número de 0 a 10.")

def validar_numero(numero):
    if numero >= 0 and numero <= 10:
        pass
    else:
        raise ValueError
    
if __name__ == "__main__":
    main()