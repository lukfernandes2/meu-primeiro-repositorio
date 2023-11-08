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