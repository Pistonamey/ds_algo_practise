def noislands(grid):
    visited=set()
    def dfs(i,j):
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1 or (i,j) in visited):
            return 
        
        visited.add((i,j))
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

        return
    
    islands=0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]==1 and (i,j) not in visited):
                dfs(i,j)
                islands+=1
    
    return islands

grid = [    [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1]
]

print(noislands(grid))