'''
ALGORITMO:
lettura risposte
verifica studenti adiacenti

SD:
dizionari, chiave nome, valore = lista risposte
'''


def leggiRisposte(filename):
    risposte = {}

    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            risposte[parts[0]] = parts[1:]

    return risposte


def controllaCopiature(nome1, nome2, risposte):
    r1 = risposte[nome1]
    r2 = risposte[nome2]
    copiato1 = False
    copiato2 = False

    if r1 == r2:
        print(f'Le risposte di {nome1} e {nome2} sono le stesse')
        return
    # abbiamo almeno una differenza

    for i in range(len(r1)):
        if r1[i] == r2[i]:
            continue
        if r1[i].isalpha() and r2[i].isalpha():
            return
        if r1[i] == '-':
            copiato1 = True
        if r2[i] == '-':
            copiato2 = True

    if copiato1:
        print(f'{nome1} può aver copiato da {nome2}')
    if copiato2:
        print(f'{nome2} può aver copiato da {nome1}')


def controllaStudenti(filename, risposte):
    with open(filename) as file:
        for line in file:
            studenti = line.strip().split()

            for i in range(len(studenti) - 1):
                controllaCopiature(studenti[i], studenti[i + 1], risposte)


def main():
    risposte = leggiRisposte('risposte.txt')
    controllaStudenti('posizioni.txt', risposte)


main()