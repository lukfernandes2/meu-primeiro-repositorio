import random

def filtra (listapal, numletras):

    listafinal = []

    for palavra in listapal:

        palavramin = palavra.lower()

        palavra.strip()

        if len(palavramin) == numletras:

            if palavramin not in listafinal:

                listafinal.append(palavramin)
    
    return listafinal


def inicializa (listapal):

    dicfinal = {}

    for palavra in listapal:

        numletras = len(palavra)

        tentativa = numletras + 1

        
    sorteada = random.choice(listapal)

    dicfinal['n'] = numletras

    dicfinal['sorteada'] = sorteada

    dicfinal['especuladas'] = []

    dicfinal['tentativas'] = numletras + 1

    return dicfinal