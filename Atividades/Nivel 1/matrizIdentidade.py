def criar_matriz_identidade(n):
    
    matriz = []
    
    for i in range(n):
        linha = [0] * n
        linha[i] = 1
        matriz.append(linha)
        
    return matriz

tamanho = 3
matriz = criar_matriz_identidade(tamanho)

for linha in matriz:
    print(linha)