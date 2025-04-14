def criar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if (i + j) % 2 == 0:
                linha.append('X')
            else:
                linha.append('O')
        tabuleiro.append(linha)
    return tabuleiro


tamanho = 7
tabuleiro_xadrez = criar_tabuleiro(tamanho)

for i in tabuleiro_xadrez:
    print(i)
