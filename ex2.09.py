try:
    string = input("Digite uma string: ")
    string_lista = string.split("/")
    if len(string_lista) != 3:
        raise ValueError
    else:
        if len(string_lista[0]) == 2 and int(string_lista[0]):
            if len(string_lista[1]) == 2 and int(string_lista[1]):
                if int(string_lista[2]):
                    print(f"{string} é uma data no formato mm/dd/aaaa.")
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
except ValueError:
    print(f"{string} não é uma data no formato mm/dd/aaaa.")