from collections import deque

def orangesRotting(self, grid):
    '''
    this is a BFS problem
    https://leetcode.com/problems/rotting-oranges
    '''
    
    def allRotten():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True
    
    def getFreshNeighbours(i, j):
        candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        return [c for c in candidates if c[0] >=0 and c[1] >=0 and c[0] < len(grid) and c[1] < len(grid[0]) and grid[c[0]][c[1]] == 1]
    
    minsPassed = 0
    freshCount = 0
    q = deque()
    # loop to initialize our q
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                freshCount += 1
    if freshCount == 0:
        return 0
    
    while q:
        if allRotten():
            return minsPassed
        newQ = deque()
        for cell in q:            
            i, j = cell
            for node in getFreshNeighbours(i, j):
                newQ.append(node)
                grid[node[0]][node[1]] = 2
        minsPassed += 1
        q = newQ
            
            
    return -1
        