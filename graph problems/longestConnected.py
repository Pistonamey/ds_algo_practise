# write a function to find the size of the largest connected region of 0's
def longest(grid):

    visited=set()

    def dfs(row,col):
        if(row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or (row,col) in visited or grid[row][col]==1):
            return 0
        
        visited.add((row,col))
        size=1
        size+=dfs(row+1,col)
        size+=dfs(row,col+1)
        size+=dfs(row-1,col)
        size+=dfs(row,col-1)
        return size
    
    longest_size=0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]==0):
                this_size=dfs(i,j)
                longest_size=max(this_size,longest_size)
    return longest_size
grid = [    [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
]
print(longest(grid))