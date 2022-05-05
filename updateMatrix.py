def updateMatrix(mat):
    res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

    def getAdjacentCells(i, j):
        candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        res = []
        for cell in candidates:
            if cell[0] >= 0 and cell[0] < len(mat) and cell[1] >= 0 and cell[1] < len(mat[0]):
                res.append(cell)
        return res

    def bfs(cell):
        from collections import deque
        q = deque()
        i, j = cell
        q.append(((i, j), 0))
        visited = set()
        while q:
            for i in range(len(q)):
                cell, d = q.popleft()
                x, y = cell
                if mat[x][y] == 0:
                    return d
                visited.add(cell)
                for adjCell in getAdjacentCells(x, y):
                    if adjCell not in visited:
                        q.append(((adjCell[0], adjCell[1]), d + 1))
        return -1

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                res[i][j] = bfs((i, j))
    return res


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

print(updateMatrix(mat))

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
