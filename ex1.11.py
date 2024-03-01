try:
    # ax^2 + bx + c = 0
    print("Para o modelo ax^2 + bx + c = 0, digite: ")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print(f"x' = {x1}")
    print(f"x'' = {x2}")
except ValueError:
    print("O valor fornecido deve ser um número.")