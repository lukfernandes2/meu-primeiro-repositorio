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

listaatualizada = filtra(plvs, 5)




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

dicionario = inicializa(listaatualizada)



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
print('')
print('')
print('Comandos: desisto')
print('')
print('REGRAS!!!!')
print('')
print(' - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.')
print(' - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(' - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print('')
print('    . Azul   : a letra está na posição correta;')
print('    . Amarelo: a palavra tem a letra, mas está na posição errada;')
print('    . Cinza: a palavra não tem a letra.')
print('')
print(' - Os acentos são ignorados;')
print(' - As palavras podem possuir letras repetidas.')
print(' - As palavras podem possuir letras repetidas.')
print('')
print('')



print('sorteando uma palavra...')
print('já tenho uma palavra, tente descobrir!' )

i = 6

while palpite != sorteada:

    print ('Você tem {0} tentativa(s)':.format(i))

    palpite = input('Qual o seu palpite?')

    print('Insper :: Termovita')




