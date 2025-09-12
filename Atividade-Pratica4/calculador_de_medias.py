def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno(a) para continuar ou fim para encerrar. ")
            if entrada.lower() == 'fim':
                print("Encerrando! ")
                break
            nota = float(entrada)

            if nota >= 0 and nota <= 10:
                notas.append(nota)
            else:
                print("Nota invalida. Digite um valor entre 0 e 10. ")
                continue
        except ValueError:
            print("Entrada invalida. Digite um numero. ")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A media da turma: {media:.2f}")
        print(f"Total de notas registradas: {len(notas)}")      

registrar_notas()












