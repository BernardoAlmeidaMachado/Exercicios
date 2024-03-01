try:
    print("Digite os comprimentos dos catetos de um triângulo retângulo: ")
    cateto_a = float(input("Cateto a: "))
    cateto_b = float(input("Cateto b: "))
    area = cateto_a * cateto_b * 1/2
    print(f"A área desse triângulo é {area}.")
except ValueError:
    print("O valor fornecido deve ser um número.")