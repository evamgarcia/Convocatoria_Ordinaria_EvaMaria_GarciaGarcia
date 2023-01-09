def knapsack(precio, pesos, peso_maximo):
    n = len(precio)
    # Crear una matriz de ceros
    K = [[0 for x in range(peso_maximo + 1)] for x in range(n + 1)]
    # Construir la matriz K[][] en el orden bottom-up
    for i in range(n + 1):
        for w in range(peso_maximo + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pesos[i-1] <= w:
                K[i][w] = max(precio[i-1] + K[i-1][w-pesos[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][peso_maximo]

precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100


print (knapsack([103, 60, 70, 5, 15], [12, 23, 11, 15, 7], 100))