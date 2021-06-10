# Python program to solve
# Gold Mine problem

MAX = 100


# Resuelve el problema de la mina de oro con el metodo fuerza bruta
def minaOroFuerzaBruta(matrizMina, m, n):
    # Create a table for storing
    # intermediate results
    # and initialize all cells to 0.
    # The first row of
    # goldMineTable gives the
    # maximum gold that the miner
    # can collect when starts that row
    goldTable = [[0 for i in range(n)]
                 for j in range(m)]

    matrizMaximos=[]
    maximos=[]
    for col in range(n - 1, -1, -1):
        maximos = []
        for row in range(m):

            # Gold collected on going to
            # the cell on the rigth(->)
            if (col == n - 1):
                right = 0
            else:
                ##print("right", right)
                right = goldTable[row][col + 1]

            # Gold collected on going to
            # the cell to right up (/)
            if (row == 0 or col == n - 1):
                right_up = 0
            else:
                ##print("rightUp",right_up)
                right_up = goldTable[row - 1][col + 1]

            # Gold collected on going to
            # the cell to right down (\)
            if (row == m - 1 or col == n - 1):
                right_down = 0
            else:
                #print("rightDown", right_down)
                right_down = goldTable[row + 1][col + 1]

            # Max gold collected from taking
            # either of the above 3 paths
            maximos.append([max(right, right_up, right_down),matrizMina[row][col]])
            goldTable[row][col] = matrizMina[row][col] + max(right, right_up, right_down)
        matrizMaximos.append(maximos)

    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])
    return res