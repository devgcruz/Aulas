matriz = [[10, 20, 30], [40, 50, 60]]

for i in range(len(matriz)):        # Itera sobre os índices das linhas
    for j in range(len(matriz[i])): # Itera sobre os índices das colunas da linha atual
        print(f"Elemento na linha {i}, coluna {j}: {matriz[i][j]}")

# Saída:
# Elemento na linha 0, coluna 0: 10
# Elemento na linha 0, coluna 1: 20
# Elemento na linha 0, coluna 2: 30
# Elemento na linha 1, coluna 0: 40
# Elemento na linha 1, coluna 1: 50
# Elemento na linha 1, coluna 2: 60