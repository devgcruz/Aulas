def criar_matriz_padrao(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = i+j
            linha.append(valor)
        matriz.append(linha)
    return matriz


linhas = 2
colunas = 3

matriz = criar_matriz_padrao(linhas, colunas)

for i in matriz:
    print(i)