linhas = 2
colunas = 3

matriz_dinamica = []

for i in range(linhas):
    linha = []
    
    for j in range(colunas):
        valor = i + j
        linha.append(valor)
    matriz_dinamica.append(linha)
    
print(matriz_dinamica)