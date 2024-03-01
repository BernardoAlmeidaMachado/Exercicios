letra = input("Digite uma letra: ").upper()
if len(letra) != 1 or letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("O valor fornecido deve ser apenas uma letra.")
else:
    if letra in "AEIOU":
        print(f"{letra} é uma vogal.")
    else:
        print(f"{letra} é uma consoante.")