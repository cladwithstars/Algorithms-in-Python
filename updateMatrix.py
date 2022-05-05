def updateMatrix(mat):
    res = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]

    def getAdjacentCells(i, j):
        candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        res = []
        for cell in candidates:
            if cell[0] >= 0 and cell[0] < len(mat) and cell[1] >= 0 and cell[1] < len(mat[0]):
                res.append(cell)
        return res
    visited = set()

    def getDistance(i, j):
        if mat[i][j] == 0:
            return 0
        visited.add((i, j))
        adjCells = getAdjacentCells(i, j)
        adjDistances = []
        for cell in adjCells:
            if cell not in visited:
                adjDistances.append(getDistance(cell[0], cell[1]))
        visited.remove((i, j))
        return 1 + min(adjDistances)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i][j] = getDistance(i, j)
    return res


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

print(updateMatrix(mat))

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
