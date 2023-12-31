import random
from palavras import PALAVRAS as plvs

while True:
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

    sorteada = dicionario['sorteada']

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





    #PRINTS

    print('============================')
    print('|                          |')
    print('|  Bem-vindoS ao Termovita |')
    print('|                          |')
    print('=====Design de Software=====')
    print('')
    print('')
    print('Comandos: Desisto')
    print('')
    print('REGRAS:')
    print('')
    print(' - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.')
    print(' - A cada tentativa, a palavra escolhida terá suas letras coloridas conforme:')
    print('')
    print(' \033[94m   . Azul \033[30m : a letra está na posição correta;')
    print(' \033[93m   . Amarelo \033[30m : a palavra tem a letra, mas está na posição errada;')
    print(' \033[90m   . Cinza \033[30m : a palavra não tem a letra.')
    print('')
    print(' - Os acentos são ignorados;')
    print(' - As palavras podem possuir letras repetidas.')
    print('')
    print('')



    print('Sorteando uma palavra...')
    print('Já tenho uma palavra, tente descobrir!' )

    #CORES PARA O TERMO
    cor_azul = "\033[94m"
    cor_preta = "\033[30m"
    cor_cinza = "\033[90m"
    cor_amarela = "\033[93m"



    def Tabela(lista_final, maxx, detalhes):
        largura_celula = 3
        separacao = '-' * ((largura_celula + 1) * maxx + 1) + '\n'
        tabela = separacao

        for plvs in lista_final:
            traco = '|'
            for i in plvs:
                traco += f'{i:^{largura_celula}}|'
            tabela += traco + '\n' + separacao

        if len(lista_final) < maxx:
            tabela += f'{("|" + " " * largura_celula) * len(plvs)}|' + '\n' + separacao

        return tabela


    a = 0

    lista_final = []

    i = 0

    tenta = 6

    palavras_tentadas = []

    tabelao = ''

    while tenta != 0:

        print('Você tem {0} tentativa(s)'.format(tenta))

        especulada = input('Qual o seu palpite?')

        print('Insper :: Termovita')
        
        if especulada == sorteada:
            a = 1
            break

        elif especulada == 'Desisto':

            break

        if especulada not in plvs:
            print('não está nos meus dados, escreva outra ;)')
            continue
        if especulada in palavras_tentadas:
            print('Palavra já testada, tente outra :)')
            continue
        

        palavras_tentadas.append(especulada)

        tenta -= 1
        
        posicao = inidica_posicao(sorteada, especulada)

        palavra_colorida = []

        i = 0
        
        for numero in posicao:

            if  numero == 0 :
                azul= cor_azul + especulada[i] + cor_cinza

                palavra_colorida.append(azul)

            elif numero == 1:

                amarelo = cor_amarela + especulada[i] + cor_cinza
            
                palavra_colorida.append(amarelo)
            
            elif numero == 2:
            
                palavra_colorida.append(especulada[i])
            
            i += 1

        lista_final.append (palavra_colorida)

        if especulada in lista_final:
            tenta +=1
            
        tabela = Tabela(lista_final, 6, '--- --- ---' )

        if len(especulada) == 5:
            print(tabela)
        
        else:
            print('A palavra deve conter 5 letras!')
            tenta += 1

        

    if a == 1:
        print('Parabens!!')

    else: 
        print ("Poxa, não foi desta vez...")   

    print('A palvra era...{0}'.format(sorteada))

    final=input('Deseja continuar?(S/N)')
    if final == 'N':
        break


    




