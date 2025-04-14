# Para acessar um elemento de uma matriz
# deve-se usar a sintaxe abaixo.

# Essa primeira chave representa a LINHA
# Esssa segunda chave representa a COLUNA

# valor = matriz[linha][coluna]

#Exemplo:

matriz = [[1,2,3], [4,5,6]]

#        linha 0: [1, 2, 3]
#        linha 1: [4, 5, 6]
#        col 0  col 1  col 2

elemento_central = matriz[1][1]
print(elemento_central)  # Saída: 5

terceiro_elemento_primeira_linha = matriz[0][2]
print(terceiro_elemento_primeira_linha)  # Saída: 3