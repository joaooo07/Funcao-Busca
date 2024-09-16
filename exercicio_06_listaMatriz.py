def busca(valor: object, matriz : list) -> list:
    #Criamos uma função Busca com dois valores, objeto e lista, nossa função retorna uma lista
    lin = len(matriz)
    col = len(matriz[0])

    for i in range(lin):
        for j in range(col):
            if matriz [i][j] == valor:
                return [i,j]
    return [-1,-1] #Retorna -1 se não encontrar o valor na matriz

mat = [

    [9, 92, 8,5],
    [-1,5,7,10],
    [4,7,9,15]
]

resp = busca(4, mat)
print(resp) 