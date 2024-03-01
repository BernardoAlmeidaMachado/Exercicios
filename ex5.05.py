aluno = ""
nota = 0.0
contador = 1
alunos_e_notas = {}

print('Deixe o campo em branco para parar de fornecer dados.')

while True:
    aluno = input(f"Aluno {contador}: ")

    if aluno.lower() == "":
        break

    nota = input(f"Nota de {aluno}: ")

    if nota.lower() == "":
        break
    else:
        try:
            nota = float(nota)
        except ValueError:
            print("A nota deve ser um valor int ou float.")
            continue

        alunos_e_notas[aluno] = nota
        contador += 1

alunos_e_notas_iguais_ou_superiores_a_7 = {name : nota for name, nota in zip(alunos_e_notas.keys(), alunos_e_notas.values()) if nota >= 7}

print(f"Todas as notas: {alunos_e_notas}")
print(f"Notas iguais ou superiores a 7: {alunos_e_notas_iguais_ou_superiores_a_7}")
