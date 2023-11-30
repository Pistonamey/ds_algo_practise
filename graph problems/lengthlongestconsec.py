# write a function to return the length of the longest consecutive 0's

def longest_path(grid):
    # Define the directions we can move in (up, left, right, down)
    
    def bfs(row,col):
        print(row,col)
        max_length=0
        q=[]
        q.append(((row,col,1)))
        visited=set()
        while q:
            cur_row,cur_col,distance=q.pop(0)
            visited.add((cur_row,cur_col))
            max_length=max(max_length,distance)
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in directions:
                new_row=cur_row+dr
                new_col=cur_col+dc
                if(0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col]==0 and (new_row,new_col) not in visited):
                    q.append(((new_row,new_col,distance+1)))
        return max_length

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return bfs(i,j)

    return 0

grid=[[0,0,1,0],
      [1,0,0,1],
      [0,1,0,1],
      [1,0,0,0]]
print(longest_path(grid))
