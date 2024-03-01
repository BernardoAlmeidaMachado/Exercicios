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

alunos_e_notas_arredondadas = {name : round(nota) for name, nota in zip(alunos_e_notas.keys(), alunos_e_notas.values())}

print(f"Notas originais: {alunos_e_notas}")
print(f"Notas arredondadas: {alunos_e_notas_arredondadas}")
