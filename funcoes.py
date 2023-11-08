import random
from palavras import PALAVRAS as plvs

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

def inidica_posicao(sorteada, especulada):
    if len(sorteada) != len(especulada):
        return []
    resultado = []
    for i in range(len(sorteada)):
        if sorteada[i] == especulada[i]:
            resultado.append(0)
        elif especulada[i] in sorteada:
            resultado.append(1)
        else:
            resultado.append(2)

    return resultado


print('==========================')
print('|                        |')
print('| Bem vindo ao termovita |')
print('|                        |')
print('==========================')